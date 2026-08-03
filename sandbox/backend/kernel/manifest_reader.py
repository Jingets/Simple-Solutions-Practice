from pathlib import Path

import yaml


class ManifestReader:
    def read(self, path: str) -> dict:
        manifest_path = Path(path)

        if not manifest_path.exists():
            raise FileNotFoundError(path)

        try:
            with manifest_path.open("r", encoding="utf-8") as file:
                data = yaml.safe_load(file)

        except yaml.YAMLError as exc:
            raise ValueError(str(exc)) from exc

        if data is None:
            return {}

        if not isinstance(data, dict):
            raise ValueError("Manifest root must be a mapping.")

        return data