from dataclasses import dataclass


@dataclass(frozen=True)
class ModuleManifest:
    id: str
    name: str
    version: str
    description: str
    author: str
    entrypoint: str
    enabled: bool
    dependencies: list[str]
    permissions: list[str]
