import sys
import Tracker as Tr
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QLabel, QLineEdit, QGridLayout
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon, QPixmap
from datetime import datetime


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("Helicopter Tracker")
        self.setContentsMargins(20, 20, 20, 20)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        """Title"""
        title = QLabel("Aircraft Tracker")
        self.layout.addWidget(title, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

        """Mileage input"""
        milage_label = QLabel('Mileage:')
        self.layout.addWidget(milage_label, 1, 0)
        self.milage_input = QLineEdit()
        self.layout.addWidget(self.milage_input, 1, 1)

        """Search button"""
        submit = QPushButton('Search')
        submit.setFixedWidth(80)
        submit.clicked.connect(self.search)
        self.layout.addWidget(submit, 3, 1, Qt.AlignmentFlag.AlignLeft)

        """Table headers"""
        self.layout.addWidget(QLabel('Registration:'), 4, 1, Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(QLabel('Type:'), 4, 2, Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(QLabel('Kts:'), 4, 3, Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(QLabel('baro_altitude:'), 4, 4, Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(QLabel('vertical_rate:'), 4, 5, Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(QLabel('squawk:'), 4, 6, Qt.AlignmentFlag.AlignCenter)

        """Last updated footer"""
        self.last_updated = QLabel("Last updated: --:--:--")
        self.last_updated.setStyleSheet("color: grey;")
        self.layout.addWidget(self.last_updated, 5, 0, 1, 3, Qt.AlignmentFlag.AlignLeft)

        """Timer for auto-refresh"""
        self.timer = QTimer(self)
        self.timer.setInterval(60_000)  # 30 seconds
        self.timer.timeout.connect(self.search)

    def clear_layout(self):
        """Remove all widgets from the layout except the first 6 rows."""
        count = self.layout.count()
        for i in reversed(range(count)):
            item = self.layout.itemAt(i)
            widget = item.widget()
            if widget:
                row = self.layout.getItemPosition(i)[0]
                if row > 5:  # only remove rows > 5 (keep header + footer)
                    widget.setParent(None)

    def search(self):
        """Run search and display results."""
        # Start timer after first button press
        if not self.timer.isActive():
            self.timer.start()

        self.clear_layout()
        miles = self.milage_input.text()
        aircraft_list = Tr.master(miles)

        for i, aircraft in enumerate(aircraft_list):
            if aircraft["Type"] in ['S-92 A', 'EC175 B (H175)', 'AW.139']:
                print(aircraft)

                on_ground = aircraft["OnGround"]
                kts = str(aircraft["kts"])
                colour = "grey" if on_ground else "white"

                # Aircraft status icon
                label0 = QLabel()
                pixmap = QPixmap("PyQt/PySide_GUI/land.png" if on_ground else "PyQt/PySide_GUI/takeoff.png")
                label0.setPixmap(pixmap.scaled(32, 32))
                self.layout.addWidget(label0, i + 6, 0, Qt.AlignmentFlag.AlignCenter)

                # Data labels
                label1 = QLabel(aircraft["Registration"])
                label1.setStyleSheet(f"color: {colour};")
                self.layout.addWidget(label1, i + 6, 1, Qt.AlignmentFlag.AlignCenter)

                label2 = QLabel(aircraft["Type"])
                label2.setStyleSheet(f"color: {colour};")
                self.layout.addWidget(label2, i + 6, 2, Qt.AlignmentFlag.AlignCenter)

                label3 = QLabel(f"{kts} kt")
                label3.setStyleSheet(f"color: {colour};")
                self.layout.addWidget(label3, i + 6, 3, Qt.AlignmentFlag.AlignCenter)

                label4 = QLabel(f"{aircraft['baro_altitude']} ft")
                label4.setStyleSheet(f"color: {colour};")
                self.layout.addWidget(label4, i + 6, 4, Qt.AlignmentFlag.AlignCenter)

                # Vertical speed icon
                vert_speed = aircraft["Vertical_rate"]
                label5 = QLabel()
                if vert_speed is None:
                    pixmap1 = QPixmap("PyQt/PySide_GUI/nutral.png")
                elif vert_speed > 5:  # going up
                    pixmap1 = QPixmap("PyQt/PySide_GUI/green_up.png")
                elif vert_speed < -5:  # going down
                    pixmap1 = QPixmap("PyQt/PySide_GUI/down_red.png")
                else:
                    pixmap1 = QPixmap("PyQt/PySide_GUI/nutral.png")
                label5.setPixmap(pixmap1.scaled(15, 15))
                self.layout.addWidget(label5, i + 6, 5, Qt.AlignmentFlag.AlignCenter)

                label6 = QLabel(str(aircraft["Squawk"]))
                label6.setStyleSheet(f"color: {colour};")
                self.layout.addWidget(label6, i + 6, 6, Qt.AlignmentFlag.AlignCenter)

        # Update footer time
        self.last_updated.setText(f"Last updated: {datetime.now().strftime("%I:%M %p")}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
