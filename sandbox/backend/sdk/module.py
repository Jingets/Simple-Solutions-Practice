from abc import ABC, abstractmethod

from .module_context import ModuleContext


class Module(ABC):
    @abstractmethod
    def install(self, context: ModuleContext) -> None:
        pass

    @abstractmethod
    def start(self, context: ModuleContext) -> None:
        pass

    @abstractmethod
    def stop(self, context: ModuleContext) -> None:
        pass

    @abstractmethod
    def uninstall(self, context: ModuleContext) -> None:
        pass