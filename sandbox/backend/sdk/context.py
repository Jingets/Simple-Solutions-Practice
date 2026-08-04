from dataclasses import dataclass


@dataclass(slots=True)
class ModuleContext:
    """
    Runtime context passed to every module.

    Will be extended with services in future versions.
    """

    platform: object | None = None