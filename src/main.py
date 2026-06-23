import tomllib
from src.fan import Fan

def main():
    with open("config.toml", "rb") as f:
        config = tomllib.load(f)

    fan = Fan(config["host"], config["token"])
    if not fan.validate():
        raise Exception("Fan is not supported")

    fan.on()
    fan.set_speed(20)


