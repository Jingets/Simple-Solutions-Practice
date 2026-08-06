from backend.core.service_container import ServiceContainer
from backend.core.service_provider import ServiceProvider

from .manifest_factory import ManifestFactory
from .manifest_reader import ManifestReader
from .module_activator import ModuleActivator
from .module_loader import ModuleLoader
from .module_manager import ModuleManager
from .module_mapper import ModuleMapper
from .module_registry import ModuleRegistry
from .module_state import ModuleState

from backend.sdk import ModuleContext


class Platform:
    """
    Central platform object.
    """

    def __init__(self) -> None:
        self._registry = ModuleRegistry()
        self._manager = ModuleManager()

        self._container = ServiceContainer()
        self.services = ServiceProvider(self._container)

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

        context = ModuleContext(
            platform=self,
            services=self.services,
        )

        try:
            module.install(context)
            self._manager.set_state(
                module_id,
                ModuleState.INSTALLED,
            )
        except Exception:
            self._manager.set_state(
                module_id,
                ModuleState.FAILED,
            )
            raise

    def start_module(self, module_id: str) -> None:
        module = self.create_module(module_id)

        context = ModuleContext(
            platform=self,
            services=self.services,
        )

        try:
            module.start(context)
            self._manager.set_state(
                module_id,
                ModuleState.RUNNING,
            )
        except Exception:
            self._manager.set_state(
                module_id,
                ModuleState.FAILED,
            )
            raise

    def stop_module(self, module_id: str) -> None:
        module = self._manager.get(module_id)

        context = ModuleContext(
            platform=self,
            services=self.services,
        )

        try:
            module.stop(context)
            self._manager.set_state(
                module_id,
                ModuleState.STOPPED,
            )
        except Exception:
            self._manager.set_state(
                module_id,
                ModuleState.FAILED,
            )
            raise

    def uninstall_module(self, module_id: str) -> None:
        module = self._manager.get(module_id)

        context = ModuleContext(
            platform=self,
            services=self.services,
        )

        module.uninstall(context)

        self._manager.remove(module_id)

    def get_module_state(self, module_id: str) -> ModuleState:
        return self._manager.get_state(module_id)