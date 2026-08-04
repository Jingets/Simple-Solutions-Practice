from backend.sdk import Module


class ModuleManager:
    """
    Stores runtime instances of loaded modules.
    """

    def __init__(self) -> None:
        self._instances: dict[str, Module] = {}

    def add(self, module_id: str, module: Module) -> None:
        if module_id in self._instances:
            raise ValueError(f"Module '{module_id}' is already instantiated")

        self._instances[module_id] = module

    def get(self, module_id: str) -> Module:
        if module_id not in self._instances:
            raise KeyError(module_id)

        return self._instances[module_id]

    def exists(self, module_id: str) -> bool:
        return module_id in self._instances

    def remove(self, module_id: str) -> None:
        self._instances.pop(module_id, None)

    def clear(self) -> None:
        self._instances.clear()

    def count(self) -> int:
        return len(self._instances)