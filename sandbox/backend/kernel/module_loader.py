from .manifest_factory import ManifestFactory
from .manifest_reader import ManifestReader
from .module_mapper import ModuleMapper
from .module_registry import ModuleRegistry


class ModuleLoader:
    def __init__(
        self,
        reader: ManifestReader,
        factory: ManifestFactory,
        mapper: ModuleMapper,
        registry: ModuleRegistry,
    ) -> None:
        self._reader = reader
        self._factory = factory
        self._mapper = mapper
        self._registry = registry

    def load(self, manifest_path: str) -> None:
        data = self._reader.read(manifest_path)
        manifest = self._factory.create(data)
        descriptor = self._mapper.to_descriptor(manifest)
        self._registry.register(descriptor)