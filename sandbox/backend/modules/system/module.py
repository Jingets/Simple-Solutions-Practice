from backend.sdk import Module
from backend.sdk import ModuleContext


class SystemModule(Module):
    def install(self, context: ModuleContext) -> None:
        print("[System] install")

    def start(self, context: ModuleContext) -> None:
        print("[System] start")

    def stop(self, context: ModuleContext) -> None:
        print("[System] stop")

    def uninstall(self, context: ModuleContext) -> None:
        print("[System] uninstall")