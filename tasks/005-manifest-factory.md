# Task-005 — Manifest Factory

## Objective

Implement a factory that converts raw manifest data into a ModuleManifest object.

The factory is responsible only for object construction and required field validation.

The factory does NOT read files.

The factory does NOT access ModuleRegistry.

The factory does NOT create ModuleDescriptor.

The factory does NOT load modules.

---

## Architecture

Create files:

backend/kernel/manifest_factory.py

---

## Dependencies

Use:

backend/kernel/module_manifest.py

---

## Class

ManifestFactory

---

## Methods

create(data: dict) -> ModuleManifest

---

## Required fields

id

name

version

description

author

entrypoint

enabled

---

## Optional fields

dependencies

permissions

If absent, use empty lists.

---

## Behaviour

If any required field is missing:

raise ValueError

The error message must contain the missing field name.

Return a ModuleManifest instance.

Do not modify the input dictionary.

---

## Restrictions

No filesystem.

No YAML.

No registry.

No loader.

No importlib.

No singleton.

No logging.

No dependency injection.

No async.

No threading.

No business logic.

---

## Output format

THIS FORMAT IS MANDATORY.

Return plain text only.

Do not use Markdown.

Do not use code fences.

Output every file exactly as:

=== FILE: relative/path ===

<file contents>

Nothing else.