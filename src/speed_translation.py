from enum import Enum

class SpeedLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

MAPPING = {
    10: SpeedLevel.LOW,
    35: SpeedLevel.MEDIUM,
    75: SpeedLevel.HIGH
}

def speed_to_level(speed: int) -> SpeedLevel:
    for threshold, level in reversed(MAPPING.items()):
        if speed >= threshold:
            return level

    raise Exception("Unsupported speed")

