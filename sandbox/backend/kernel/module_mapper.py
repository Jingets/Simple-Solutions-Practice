from .module_descriptor import ModuleDescriptor
from .module_manifest import ModuleManifest


class ModuleMapper:
    def to_descriptor(self, manifest: ModuleManifest) -> ModuleDescriptor:
        return ModuleDescriptor(
            id=manifest.id,
            name=manifest.name,
            version=manifest.version,
            description=manifest.description,
            author=manifest.author,
            entrypoint=manifest.entrypoint,
            enabled=manifest.enabled,
        )