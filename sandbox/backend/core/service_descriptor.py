from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ServiceDescriptor:
    service_type: type
    implementation: type | None = None
    instance: Any | None = None
    singleton: bool = True