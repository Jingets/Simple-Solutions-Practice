from .manifest_factory import ManifestFactory
from .manifest_reader import ManifestReader
from .module_activator import ModuleActivator
from .module_loader import ModuleLoader
from .module_manager import ModuleManager
from .module_mapper import ModuleMapper
from .module_registry import ModuleRegistry

from backend.sdk import ModuleContext


class Platform:
    def __init__(self) -> None:
        self._registry = ModuleRegistry()
        self._manager = ModuleManager()

        self._loader = ModuleLoader(
            reader=ManifestReader(),
            factory=ManifestFactory(),
            mapper=ModuleMapper(),
            registry=self._registry,
        )

        self._activator = ModuleActivator()

    @property
    def registry(self) -> ModuleRegistry:
        return self._registry

    def load_module(self, manifest_path: str) -> None:
        self._loader.load(manifest_path)

    def create_module(self, module_id: str):
        if self._manager.exists(module_id):
            return self._manager.get(module_id)

        descriptor = self._registry.get(module_id)

        module = self._activator.create(descriptor.entrypoint)

        self._manager.add(module_id, module)

        return module

    def install_module(self, module_id: str) -> None:
        module = self.create_module(module_id)
        context = ModuleContext(platform=self)
        module.install(context)

    def start_module(self, module_id: str) -> None:
        module = self.create_module(module_id)
        context = ModuleContext(platform=self)
        module.start(context)

    def stop_module(self, module_id: str) -> None:
        module = self._manager.get(module_id)
        context = ModuleContext(platform=self)
        module.stop(context)

    def uninstall_module(self, module_id: str) -> None:
        module = self._manager.get(module_id)
        context = ModuleContext(platform=self)

        module.uninstall(context)

        self._manager.remove(module_id)