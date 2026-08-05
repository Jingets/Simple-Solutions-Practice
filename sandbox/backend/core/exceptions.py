class ServiceContainerError(Exception):
    """Base exception for service container."""


class ServiceAlreadyRegisteredError(ServiceContainerError):
    """Raised when a service is already registered."""


class ServiceNotFoundError(ServiceContainerError):
    """Raised when a service cannot be resolved."""