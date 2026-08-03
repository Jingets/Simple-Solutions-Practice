# Task-006 — Module Mapper

## Objective

Implement a mapper that converts ModuleManifest into ModuleDescriptor.

The mapper performs object mapping only.

No validation.

No filesystem.

No registry.

No loader.

No YAML.

---

## Architecture

Create files:

backend/kernel/module_mapper.py

---

## Dependencies

Use:

backend/kernel/module_manifest.py

backend/kernel/module_descriptor.py

---

## Class

ModuleMapper

---

## Methods

to_descriptor(manifest: ModuleManifest) -> ModuleDescriptor

---

## Behaviour

Create and return a new ModuleDescriptor.

Copy all common fields.

Ignore:

dependencies

permissions

The mapper must not modify the source object.

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