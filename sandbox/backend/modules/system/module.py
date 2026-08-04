from backend.sdk import Module
from backend.sdk import ModuleContext


class SystemModule(Module):
    def install(self, context: ModuleContext) -> None:
        pass

    def start(self, context: ModuleContext) -> None:
        pass

    def stop(self, context: ModuleContext) -> None:
        pass

    def uninstall(self, context: ModuleContext) -> None:
        pass