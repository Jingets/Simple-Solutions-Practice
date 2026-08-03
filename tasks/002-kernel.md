# Task-002 — Kernel

## Objective

Implement the platform kernel.

The kernel is responsible only for module registration.

The kernel does NOT load modules.

The kernel does NOT execute modules.

The kernel does NOT contain business logic.

---

## Architecture

Create files:

backend/kernel/__init__.py

backend/kernel/module_descriptor.py

backend/kernel/module_registry.py

---

## ModuleDescriptor

Create immutable dataclass

ModuleDescriptor

Fields:

id: str

name: str

version: str

description: str

author: str

entrypoint: str

enabled: bool

---

## ModuleRegistry

Implement class

ModuleRegistry

Methods:

register(module: ModuleDescriptor)

get(module_id: str)

all()

exists(module_id: str)

count()

clear()

---

## Behaviour

Registering two modules with the same id must raise

ValueError

all()

returns list[ModuleDescriptor]

get()

returns ModuleDescriptor

If module is absent

raise KeyError

---

## Restrictions

No filesystem.

No YAML.

No importlib.

No plugin loading.

No dependency injection.

No logging.

No singleton.

No global variables.

No threading.

No async.

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