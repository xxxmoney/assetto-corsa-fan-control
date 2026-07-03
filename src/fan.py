from functools import cached_property
from miio import DeviceFactory
from miio import Device
from miio import DeviceInfo
from miio import Fan1C
from src.fan_mappings import FAN_MAPPINGS
from src.logger import logger
from src.speed_translation import speed_to_level, SpeedLevel


class Fan:
    _host: str
    _token: str
    _device: Device
    _is_valid: bool

    def __init__(self, host: str, token: str):
        self._host = host
        self._token = token

    def initialize(self):
        self._device = DeviceFactory.create(self._host, self._token)

    @cached_property
    def methods(self) -> list[str]:
        methods = [m for m in dir(self._device) if not m.startswith('_')]
        logger.debug(f"Methods: {methods}")
        return methods

    @cached_property
    def info(self) -> DeviceInfo:
        info = self._device.info()
        logger.debug(f"Info: {info}")
        return info

    def on(self):
        logger.debug("On")
        if isinstance(self._device, Fan1C):
            self._device.on()
        else:
            mapping = FAN_MAPPINGS[self.info.model]
            self._device.send("set_properties", [{"did": "1", "siid": mapping["power"]["siid"], "piid": mapping["power"]["piid"], "value": True}])

    def off(self):
        logger.debug("Off")
        if isinstance(self._device, Fan1C):
            self._device.off()
        else:
            mapping = FAN_MAPPINGS[self.info.model]
            self._device.send("set_properties", [{"did": "1", "siid": mapping["power"]["siid"], "piid": mapping["power"]["piid"], "value": False}])

    def set_speed(self, speed: int):
        logger.debug(f"Speed: {speed}")

        if speed < 0 or speed > 100:
            raise ValueError("Speed must be between 0 and 100")

        # Special handling for 1C (3 levels of speed)
        if isinstance(self._device, Fan1C):
            level = speed_to_level(speed)
            logger.debug(f"Set speed level: {speed}->{level}")

            if level == SpeedLevel.OFF:
                self.off()
            else:
                self.on()
                self._device.set_speed(level.value)
        else:
            logger.debug(f"Set normal speed: {speed}")

            if speed == 0:
                self.off()
            else:
                self.on()

                mapping = FAN_MAPPINGS[self.info.model]
                if mapping["speed_type"] is "stepless":
                    self._device.send("set_properties",[{"did": "1", "siid": mapping["speed"]["siid"], "piid": mapping["speed"]["piid"], "value": speed}])
                elif mapping["speed_type"] is "gear":
                    raise NotImplementedError("TODO: implement gear")
                else:
                    raise ValueError(f"Speed type is not supported: {mapping["speed_type"]}")