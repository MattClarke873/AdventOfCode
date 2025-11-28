import sys
import requests
import math
from datetime import datetime, timedelta
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QLineEdit,
    QGridLayout, QCheckBox
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon, QPixmap

# ------------------------------
# OpenSky OAuth2 credentials
# ------------------------------
CLIENT_ID = "matclarke216@hotmail.co.uk-api-client"
CLIENT_SECRET = "XmXzCEY8zI8rsgukS96zrfXXFmF7z1U7"

def get_token():
    url = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Token request failed: {response.status_code} {response.text}")

# ------------------------------
# Helper functions
# ------------------------------
def miles_to_box(lat_center, lon_center, miles):
    delta_lat = miles / 69.0
    delta_lon = miles / (69.0 * math.cos(math.radians(lat_center)))
    latMin = round(lat_center - delta_lat, 7)
    latMax = round(lat_center + delta_lat, 7)
    lonMin = round(lon_center - delta_lon, 7)
    lonMax = round(lon_center + delta_lon, 7)
    return latMin, latMax, lonMin, lonMax

def get_data(latMin, latMax, lonMin, lonMax):
    """Get all aircraft in area (full-area search)"""
    token = get_token()
    url = f"https://opensky-network.org/api/states/all?lamin={latMin}&lomin={lonMin}&lamax={latMax}&lomax={lonMax}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('states', [])
    else:
        return []

def get_specific_aircraft(icao_list):
    """Fetch only aircraft in the ICAO list, batching in 10s"""
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    all_states = []

    for i in range(0, len(icao_list), 10):
        # Force ICAO24 codes to lowercase (fix for OpenSky API)
        batch = [icao.lower() for icao in icao_list[i:i + 10]]
        icao_params = "&".join([f"icao24={icao}" for icao in batch])
        url = f"https://opensky-network.org/api/states/all?{icao_params}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            try:
                data = response.json()
                if data and "states" in data and data["states"]:
                    all_states.extend(data["states"])
            except ValueError:
                print(f"Invalid JSON returned for batch {batch}")
        else:
            print(f"Request failed: {response.status_code} {response.text}")

    return all_states

def search_aircraft(latMin, latMax, lonMin, lonMax, specific_only=True):
    """
    Main search function. Returns a list of aircraft dicts.
    """
    if specific_only:
        # predefined helicopters
        s92 = ["407780","407657","4077B3","406A2C","406E52","4070FF","406683","408249"] 
        h175 = ["408276","4071D1","40736B","4076C5","407356","407B52","407C68"]
        aw139 = ["407155","407154"]
        all_icao = s92 + h175 + aw139
        states = get_specific_aircraft(all_icao)
    else:
        states = get_data(latMin, latMax, lonMin, lonMax)

    final = []
    for state in states:
        icao = state[0]
        url = f"https://hexdb.io/api/v1/aircraft/{icao}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            on_ground = state[8]
            kts = int(round(state[9]*1.943844,0) if state[9] else 0)
            baro_altitude = int(round(state[7]*3.28084,0) if state[7] else 0)
            final.append({
                "icao": icao,
                "Registration": data.get("Registration", "Unknown"),
                "Callsign": state[1],
                "Squawk": state[14],
                "Manufacturer": data.get("Manufacturer", "Unknown"),
                "Type": data.get("Type", "Unknown"),
                "Vertical_rate": state[11],
                "kts": kts if not on_ground else 0,
                "OnGround": on_ground,
                "baro_altitude": baro_altitude,
                "true_track": state[10],
                "geo_altitude" : state[13]
            })
        elif response.status_code == 404:
            print(f"{icao} not found in HexDB, skipping...")
        else:
            print(f"Request failed {response.status_code}: {response.text}")
    return final

# ------------------------------
# PyQt GUI
# ------------------------------
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("Helicopter Tracker")
        self.setContentsMargins(20, 20, 20, 20)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Title
        self.layout.addWidget(QLabel("Aircraft Tracker"), 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

        # Mileage input
        self.layout.addWidget(QLabel("Mileage:"), 1, 0)
        self.milage_input = QLineEdit()
        self.layout.addWidget(self.milage_input, 1, 1)

        # Checkbox to toggle search mode
        self.specific_only_checkbox = QCheckBox("Search only my helicopters")
        self.specific_only_checkbox.setChecked(True)
        self.layout.addWidget(self.specific_only_checkbox, 2, 0, 1, 2)

        # Search button
        submit = QPushButton("Search")
        submit.setFixedWidth(80)
        submit.clicked.connect(self.search)
        self.layout.addWidget(submit, 3, 1, Qt.AlignmentFlag.AlignLeft)

        # Table headers
        headers = ["Registration", "Type", "Kts", "baro_altitude", "vertical_rate", "Squawk", "Flown Today?"]
        for col, text in enumerate(headers, start=1):
            self.layout.addWidget(QLabel(text), 4, col, Qt.AlignmentFlag.AlignCenter)

        # Footer last updated
        self.last_updated = QLabel("Last updated: --:--:--")
        self.last_updated.setStyleSheet("color: grey;")
        self.layout.addWidget(self.last_updated, 5, 0, 1, 3, Qt.AlignmentFlag.AlignLeft)

        # History store for last 24 hours
        self.history = {}  # {icao: [timestamps]}

        # Timer for auto-refresh
        self.timer = QTimer(self)
        self.timer.setInterval(60_000)  # 1 minute
        self.timer.timeout.connect(self.search)

    def clear_layout(self):
        count = self.layout.count()
        for i in reversed(range(count)):
            item = self.layout.itemAt(i)
            widget = item.widget()
            if widget:
                row = self.layout.getItemPosition(i)[0]
                if row > 5:  # keep header + footer
                    widget.setParent(None)

    def update_history(self, aircraft_list):
        """Store ICAO sightings for the last 24 hours"""
        now = datetime.now()
        cutoff = now - timedelta(hours=24)
        for ac in aircraft_list:
            icao = ac["icao"]
            if icao not in self.history:
                self.history[icao] = []
            self.history[icao].append(now)

            # Keep only last 24 hours
            self.history[icao] = [t for t in self.history[icao] if t > cutoff]

    def has_flown_today(self, icao):
        """Check if aircraft has been seen today (since midnight)"""
        if icao not in self.history:
            return False
        midnight = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return any(t >= midnight for t in self.history[icao])

    def search(self):
        if not self.timer.isActive():
            self.timer.start()

        self.clear_layout()
        miles = int(self.milage_input.text() or 50)  # default 50 miles
        latMin, latMax, lonMin, lonMax = miles_to_box(57.204991, -2.1999049, miles)

        aircraft_list = search_aircraft(latMin, latMax, lonMin, lonMax,
                                        specific_only=self.specific_only_checkbox.isChecked())

        # If specific-only mode, store history
        if self.specific_only_checkbox.isChecked():
            self.update_history(aircraft_list)

        for i, aircraft in enumerate(aircraft_list):
            on_ground = aircraft["OnGround"]

            # Aircraft icon
            label0 = QLabel()
            pixmap = QPixmap("PyQt/PySide_GUI/land.png" if on_ground else "PyQt/PySide_GUI/takeoff.png")
            label0.setPixmap(pixmap.scaled(32,32))
            self.layout.addWidget(label0, i+6, 0, Qt.AlignmentFlag.AlignCenter)

            # Data columns
            self.layout.addWidget(QLabel(aircraft["Registration"]), i+6, 1)
            self.layout.addWidget(QLabel(aircraft["Type"]), i+6, 2)
            self.layout.addWidget(QLabel(f"{aircraft['kts']} kt"), i+6, 3)
            self.layout.addWidget(QLabel(f"{aircraft['baro_altitude']} ft"), i+6, 4)

            # Vertical rate icon
            vert_speed = aircraft["Vertical_rate"]
            label5 = QLabel()
            if vert_speed is None:
                pixmap1 = QPixmap("PyQt/PySide_GUI/nutral.png")
            elif vert_speed > 1:
                pixmap1 = QPixmap("PyQt/PySide_GUI/green_up.png")
            elif vert_speed < -1:
                pixmap1 = QPixmap("PyQt/PySide_GUI/down_red.png")
            else:
                pixmap1 = QPixmap("PyQt/PySide_GUI/nutral.png")
            label5.setPixmap(pixmap1.scaled(15,15))
            self.layout.addWidget(label5, i+6, 5, Qt.AlignmentFlag.AlignCenter)

            # Squawk
            self.layout.addWidget(QLabel(str(aircraft["Squawk"])), i+6, 6)

            # Flown today? (Yes/No)
            flown_today = "Yes" if self.has_flown_today(aircraft["icao"]) else "No"
            self.layout.addWidget(QLabel(flown_today), i+6, 7)

        # Update footer
        self.last_updated.setText(f"Last updated: {datetime.now().strftime('%I:%M %p')}")

# ------------------------------
# Main
# ------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
