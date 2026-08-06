from backend.sdk import Module

from .module_state import ModuleState


class ModuleManager:
    """
    Stores runtime instances and lifecycle state of modules.
    """

    def __init__(self) -> None:
        self._instances: dict[str, Module] = {}
        self._states: dict[str, ModuleState] = {}

    def add(self, module_id: str, module: Module) -> None:
        if module_id in self._instances:
            raise ValueError(
                f"Module '{module_id}' is already instantiated"
            )

        self._instances[module_id] = module
        self._states[module_id] = ModuleState.DISCOVERED

    def get(self, module_id: str) -> Module:
        if module_id not in self._instances:
            raise KeyError(module_id)

        return self._instances[module_id]

    def exists(self, module_id: str) -> bool:
        return module_id in self._instances

    def remove(self, module_id: str) -> None:
        self._instances.pop(module_id, None)
        self._states.pop(module_id, None)

    def clear(self) -> None:
        self._instances.clear()
        self._states.clear()

    def count(self) -> int:
        return len(self._instances)

    #
    # Lifecycle state
    #

    def set_state(
        self,
        module_id: str,
        state: ModuleState,
    ) -> None:
        if module_id not in self._instances:
            raise KeyError(module_id)

        self._states[module_id] = state

    def get_state(
        self,
        module_id: str,
    ) -> ModuleState:
        if module_id not in self._states:
            raise KeyError(module_id)

        return self._states[module_id]