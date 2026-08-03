from .module_manifest import ModuleManifest


class ManifestFactory:
    _REQUIRED_FIELDS = (
        "id",
        "name",
        "version",
        "description",
        "author",
        "entrypoint",
        "enabled",
    )

    def create(self, data: dict) -> ModuleManifest:
        if not isinstance(data, dict):
            raise ValueError("Manifest data must be a dictionary.")

        for field in self._REQUIRED_FIELDS:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        dependencies = data.get("dependencies", [])
        permissions = data.get("permissions", [])

        if not isinstance(dependencies, list):
            raise ValueError("Field 'dependencies' must be a list.")

        if not isinstance(permissions, list):
            raise ValueError("Field 'permissions' must be a list.")

        return ModuleManifest(
            id=data["id"],
            name=data["name"],
            version=data["version"],
            description=data["description"],
            author=data["author"],
            entrypoint=data["entrypoint"],
            enabled=data["enabled"],
            dependencies=list(dependencies),
            permissions=list(permissions),
        )