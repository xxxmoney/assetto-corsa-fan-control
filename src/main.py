import json
import tomllib
from time import sleep
from src.constants import SPEED_FILE_PATH
from src.fan import Fan
from src.logger import logger

def main():
    logger.info(f"Started App")

    logger.info("Loading config")
    with open("config.toml", "rb") as f:
        config = tomllib.load(f)

    logger.info(f"Setting up fan")
    fan = Fan(config["host"], config["token"])
    fan.initialize()

    while True:
        if not SPEED_FILE_PATH.exists():
            logger.warning("Speed file does not exist")
            return

        logger.info("Loading speed file")
        speed_value = json.loads(SPEED_FILE_PATH.read_text(encoding="utf-8"))
        logger.info(f"Setting up fan")

        fan.set_speed(speed_value["percentage"])

        sleep(1)

if __name__ == "__main__":
    main()

