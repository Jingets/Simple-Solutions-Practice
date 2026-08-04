class SDKError(Exception):
    pass


class ModuleError(SDKError):
    pass


class PermissionError(SDKError):
    pass


class LifecycleError(SDKError):
    pass