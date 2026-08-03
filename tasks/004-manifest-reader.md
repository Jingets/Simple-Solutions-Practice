# Task-004 — Manifest Reader

## Objective

Implement manifest reader.

The reader loads a manifest.yaml file.

The reader returns raw dictionary data.

The reader does NOT create ModuleManifest.

The reader does NOT validate data.

The reader does NOT access ModuleRegistry.

---

## Architecture

Create files:

backend/kernel/manifest_reader.py

---

## Dependencies

Use PyYAML.

---

## Class

ManifestReader

---

## Methods

read(path: str) -> dict

---

## Behaviour

Read YAML file.

Return dictionary.

If file does not exist

raise FileNotFoundError

If YAML is invalid

raise ValueError

---

## Restrictions

No registry.

No loader.

No importlib.

No singleton.

No logging.

No dependency injection.

No business logic.

No caching.

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