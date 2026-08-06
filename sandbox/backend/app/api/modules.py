from fastapi import APIRouter

from backend.app.bootstrap import platform

router = APIRouter(prefix="/modules", tags=["Modules"])


@router.get("/")
def get_modules() -> list[dict]:
    result = []

    for manifest in platform.registry.all():
        state = None

        try:
            state = platform.get_module_state(manifest.id).value
        except KeyError:
            state = "not_loaded"

        result.append(
            {
                "id": manifest.id,
                "name": manifest.name,
                "version": manifest.version,
                "enabled": manifest.enabled,
                "state": state,
            }
        )

    return result