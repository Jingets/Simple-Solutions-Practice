from enum import Enum, auto


class ModuleState(Enum):
    INSTALLED = auto()
    STARTED = auto()
    STOPPED = auto()
    UNINSTALLED = auto()