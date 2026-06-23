from miio import DeviceFactory
from miio import Device
from miio import DeviceInfo
from miio import Fan1C
from src.constants import REQUIRED_METHODS
from src.speed_translation import speed_to_level


class Fan:
    _host: str
    _token: str
    _device: Device

    def __init__(self, host: str, token: str):
        self._device = DeviceFactory.create(host, token)

    def validate(self) -> bool:
        return set(REQUIRED_METHODS).issubset(self.methods)

    @property
    def methods(self) -> list[str]:
        return [m for m in dir(self._device) if not m.startswith('_')]

    @property
    def info(self) -> DeviceInfo:
        return self._device.info()

    def on(self):
        self._device.on()

    def off(self):
        self._device.off()

    def set_speed(self, speed: int):
        if speed < 0 or speed > 100:
            raise ValueError("Speed must be between 0 and 100")

        # Special handling for 1C (it has 3 levels of speed)
        if isinstance(self._device, Fan1C):
            self._device.set_speed(speed_to_level(speed).value)
        else:
            self._device.set_speed(speed)
