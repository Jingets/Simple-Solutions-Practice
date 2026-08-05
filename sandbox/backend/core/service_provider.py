from typing import Any


class ServiceProvider:
    """
    Read-only facade over ServiceContainer.
    """

    def __init__(self, container: "ServiceContainer") -> None:
        self._container = container

    def resolve(self, service_type: type) -> Any:
        return self._container.resolve(service_type)

    def exists(self, service_type: type) -> bool:
        return self._container.exists(service_type)
