from typing import Any

from backend.core.exceptions import (
    ServiceAlreadyRegisteredError,
    ServiceNotFoundError,
)
from backend.core.service_descriptor import ServiceDescriptor


class ServiceContainer:
    """
    Simple dependency injection container.

    Supports:

    - singleton services
    - transient services
    - instance registration
    """

    def __init__(self) -> None:
        self._services: dict[type, ServiceDescriptor] = {}

    def register(
        self,
        service_type: type,
        implementation: type,
        *,
        singleton: bool = True,
    ) -> None:
        """
        Register a service implementation.
        """
        if service_type in self._services:
            raise ServiceAlreadyRegisteredError(service_type.__name__)

        self._services[service_type] = ServiceDescriptor(
            service_type=service_type,
            implementation=implementation,
            singleton=singleton,
        )

    def register_instance(
        self,
        service_type: type,
        instance: Any,
    ) -> None:
        """
        Register an existing singleton instance.
        """
        if service_type in self._services:
            raise ServiceAlreadyRegisteredError(service_type.__name__)

        self._services[service_type] = ServiceDescriptor(
            service_type=service_type,
            instance=instance,
            singleton=True,
        )

    def resolve(self, service_type: type) -> Any:
        """
        Resolve a service instance.
        """
        descriptor = self._services.get(service_type)

        if descriptor is None:
            raise ServiceNotFoundError(service_type.__name__)

        if descriptor.instance is not None:
            return descriptor.instance

        if descriptor.implementation is None:
            raise ServiceNotFoundError(service_type.__name__)

        instance = descriptor.implementation()

        if descriptor.singleton:
            descriptor.instance = instance

        return instance

    def exists(self, service_type: type) -> bool:
        """
        Check whether a service is registered.
        """
        return service_type in self._services

    def unregister(self, service_type: type) -> None:
        """
        Remove a registered service.
        """
        if service_type not in self._services:
            raise ServiceNotFoundError(service_type.__name__)

        del self._services[service_type]

    def clear(self) -> None:
        """
        Remove all registered services.
        """
        self._services.clear()

    def count(self) -> int:
        """
        Return the number of registered services.
        """
        return len(self._services)