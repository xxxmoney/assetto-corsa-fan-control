from miio import DeviceFactory
from miio import Device
from miio import DeviceInfo
from miio import Fan1C
from src.constants import REQUIRED_METHODS
from src.logger import logger
from src.speed_translation import speed_to_level, SpeedLevel


class Fan:
    _host: str
    _token: str
    _device: Device

    def __init__(self, host: str, token: str):
        self._device = DeviceFactory.create(host, token)

    def validate(self) -> bool:
        is_valid = set(REQUIRED_METHODS).issubset(self.methods)
        logger.debug(f"Validation: {is_valid}")
        return is_valid

    @property
    def methods(self) -> list[str]:
        methods = [m for m in dir(self._device) if not m.startswith('_')]
        logger.debug(f"Methods: {methods}")
        return methods

    @property
    def info(self) -> DeviceInfo:
        info = self._device.info()
        logger.debug(f"Info: {info}")
        return info

    def on(self):
        logger.debug("On")
        self._device.on()

    def off(self):
        logger.debug("Off")
        self._device.off()

    def set_speed(self, speed: int):
        logger.debug(f"Speed: {speed}")

        if speed < 0 or speed > 100:
            raise ValueError("Speed must be between 0 and 100")

        # Special handling for 1C (it has 3 levels of speed)
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
                self._device.set_speed(speed)
