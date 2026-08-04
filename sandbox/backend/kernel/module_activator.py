from importlib import import_module

from backend.sdk import Module


class ModuleActivator:
    def create(self, entrypoint: str) -> Module:
        if ":" not in entrypoint:
            raise ValueError(
                "Entrypoint must have format 'package.module:ClassName'."
            )

        module_name, class_name = entrypoint.split(":", 1)

        module = import_module(module_name)

        try:
            module_class = getattr(module, class_name)
        except AttributeError as exc:
            raise ValueError(
                f"Module class '{class_name}' not found."
            ) from exc

        instance = module_class()

        if not isinstance(instance, Module):
            raise TypeError(
                f"'{entrypoint}' is not a valid SDK Module."
            )

        return instance