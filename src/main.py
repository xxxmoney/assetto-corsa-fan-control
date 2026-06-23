import json
import tomllib
from time import sleep

from src.constants import SPEED_FILE_PATH
from src.fan import Fan

fan: Fan

def main():
    with open("config.toml", "rb") as f:
        config = tomllib.load(f)

    fan = Fan(config["host"], config["token"])
    if not fan.validate():
        raise Exception("Fan is not supported")

    while True:
        check_speed()
        sleep(1)


def check_speed():
    if not SPEED_FILE_PATH.exists():
        return

    value = json.loads(SPEED_FILE_PATH.read_text(encoding="utf-8"))
    fan.set_speed(value["percentage"])
