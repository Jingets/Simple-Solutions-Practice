from backend.kernel import Platform

platform = Platform()

platform.load_module(
    "backend/modules/system/manifest.yaml"
)

module = platform.create_module("system")