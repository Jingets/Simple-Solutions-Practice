from dataclasses import dataclass


@dataclass(frozen=True)
class ModuleDescriptor:
    id: str
    name: str
    version: str
    description: str
    author: str
    entrypoint: str
    enabled: bool
