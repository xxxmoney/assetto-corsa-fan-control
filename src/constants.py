from pathlib import Path

REQUIRED_METHODS = [
    "on",
    "off",
    "set_speed"
]

SPEED_FILE_PATH = Path.home() / "AppData" / "Roaming" / "AssettoCorsaFanControl" / "speed.json"
