from dataclasses import dataclass
from typing import TYPE_CHECKING

from backend.core.service_provider import ServiceProvider

if TYPE_CHECKING:
    from backend.kernel.platform import Platform


@dataclass(slots=True)
class ModuleContext:
    """
    Runtime context passed to every module.
    """

    platform: "Platform"
    services: ServiceProvider