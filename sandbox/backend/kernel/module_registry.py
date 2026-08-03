from .module_descriptor import ModuleDescriptor


class ModuleRegistry:
    def __init__(self) -> None:
        self._modules: dict[str, ModuleDescriptor] = {}

    def register(self, module: ModuleDescriptor) -> None:
        if module.id in self._modules:
            raise ValueError("Module with id '" + module.id + "' is already registered")
        self._modules[module.id] = module

    def get(self, module_id: str) -> ModuleDescriptor:
        if module_id not in self._modules:
            raise KeyError(module_id)
        return self._modules[module_id]

    def all(self) -> list[ModuleDescriptor]:
        return list(self._modules.values())

    def exists(self, module_id: str) -> bool:
        return module_id in self._modules

    def count(self) -> int:
        return len(self._modules)

    def clear(self) -> None:
        self._modules.clear()
