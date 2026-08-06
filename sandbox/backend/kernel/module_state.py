from enum import Enum


class ModuleState(str, Enum):
    """
    Runtime state of a module.
    """

    DISCOVERED = "discovered"
    INSTALLED = "installed"
    RUNNING = "running"
    STOPPED = "stopped"
    FAILED = "failed"