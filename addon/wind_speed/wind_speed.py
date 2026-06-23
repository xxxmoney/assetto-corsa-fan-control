from pathlib import Path
import ac
import acsys
import json
import re
import os, sys, platform
from third_party.sim_info import *

#
#                    CHANGE THIS IF NEEDED:
#                    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
assetto_path = Path("C:/Program Files (x86)/Steam/steamapps/common/assettocorsa")
#                    ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
#
#

speed_file_path = Path("%appdata%/AssettoCorsaFanControl/speed.json")
simInfo = SimInfo()
my_car_id = 0
window_width = 350
window_height = 175
label_height = 35
speed_threshold = 2
default_max_speed = 300
timeout = 0.2
log_prefix = "Wind Speed| "

app_window = None
label_model = None
label_speed = None
label_max_speed = None
car_model = None
last_speed = 0
max_speed = None
timer = 0


def acMain(ac_version):
    global app_window, label_model, label_speed, label_max_speed, max_speed

    app_window = ac.newApp("Wind Speed")
    ac.setSize(app_window, window_width, window_height)

    label_model = ac.addLabel(app_window, "Model: ")
    ac.setPosition(label_model, 30, label_height * 1)

    label_speed = ac.addLabel(app_window, "Speed: ")
    ac.setPosition(label_speed, 30, label_height * 2)

    label_max_speed = ac.addLabel(app_window, "Max Speed: ")
    ac.setPosition(label_max_speed, 30, label_height * 3)

    # Reset speed file
    set_speed_file(0)

    return "Wind Speed"


def acUpdate(deltaT):
    global max_speed, car_model, last_speed, default_max_speed, timer
    timer += deltaT

    if timer < timeout:
        return

    timer = 0

    if not car_model:
        car_model = ac.getCarName(my_car_id)

    if not max_speed:
        max_speed = parse_max_speed(car_model)
    # If max speed not parsed, set default
    if not max_speed:
        log("Max speed not parsed, setting default: " + str(default_max_speed))
        max_speed = default_max_speed

    speed = int(ac.getCarState(my_car_id, acsys.CS.SpeedKMH))

    # Threshold difference reached, call to update fan speed
    if abs(speed - last_speed) > speed_threshold:
        log("Speed changed: " + str(last_speed) + " -> " + str(speed))
        last_speed = speed
        percentage = int(speed / max_speed * 100)

        set_speed_file(percentage)

    # Update UI
    if label_speed and speed:
        ac.setText(label_speed, "Speed: " + str(speed) + " km/h")
    if label_model and car_model:
        ac.setText(label_model, "Model: " + car_model)
    if label_max_speed and max_speed:
        ac.setText(label_max_speed, "Max Speed: " + str(max_speed) + " km/h")

def acShutdown():
    pass  # No specific shutdown actions needed

def log(message):
    ac.log(log_prefix + message)
    ac.console(log_prefix + message)

def parse_max_speed(model):
    if not model:
        log("Model is empty")
        return None

    log("Parsing max speed for model: " + model + "...")
    path = assetto_path / "/content/cars/" / model + "/ui/ui_car.json"
    log("Path: " + path)

    if not os.path.exists(path):
        log("Path does not exist: " + path)
        return None

    with open(path, 'r', encoding='utf-8-sig') as file:
        config = json.load(file, strict=False)

    log("Config: " + str(config))

    config_value = config['specs']['topspeed']

    if not config_value:
        log("Config value is empty")
        return None

    log("Config value: " + config_value)

    match = re.search(r'\d+', config_value)
    if not match:
        log("Match not found")
        return None

    log("Max speed parsed: " + match.group())
    return int(match.group())

def set_speed_file(percentage):
    log("Setting fan speed: " + str(percentage) + "%")

    # Write speed percentage to json file
    try:
        speed_file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(speed_file_path, 'w', encoding='utf-8') as file:
            json.dump({"percentage": percentage}, file)
    except Exception as e:
        log("Error writing to file: " + str(e))
