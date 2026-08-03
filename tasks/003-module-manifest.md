# Task-003 — Module Manifest

## Objective

Implement the manifest model.

The manifest describes a module.

It is a data model only.

No YAML parsing.

No filesystem.

No registry.

No loader.

---

## Architecture

Create files:

backend/kernel/module_manifest.py

---

## ModuleManifest

Create immutable dataclass

ModuleManifest

Fields:

id: str

name: str

version: str

description: str

author: str

entrypoint: str

enabled: bool

dependencies: list[str]

permissions: list[str]

---

## Behaviour

No methods.

No validation.

No business logic.

Only immutable data.

---

## Restrictions

No filesystem.

No YAML.

No importlib.

No loader.

No registry.

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