import os

def remove_mission_txt(directory="."):
    """Recursively remove all 'mission.txt' files from the given directory and subdirectories."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file == "mission.txt":
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

if __name__ == "__main__":
    remove_mission_txt()
