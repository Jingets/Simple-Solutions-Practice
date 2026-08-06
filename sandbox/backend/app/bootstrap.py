from backend.kernel import Platform


platform = Platform()


def bootstrap() -> Platform:
    print("BOOTSTRAP START")

    print("PLATFORM CREATED")

    platform.load_module(
        "backend/modules/system/manifest.yaml"
    )

    print("MODULE LOADED")

    platform.install_module("system")

    print("MODULE INSTALLED")

    platform.start_module("system")

    print("MODULE STARTED")

    return platform