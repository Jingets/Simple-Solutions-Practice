# Task 012 — Service Container

## Objective

Implement a minimal dependency injection container for the platform.

The implementation must be production-quality, simple, deterministic and fully typed.

Do NOT use external DI libraries.

Use only the Python standard library.

---

## Existing architecture

backend/

    core/

    kernel/

    sdk/

Kernel already contains:

- Platform
- ModuleRegistry
- ModuleLoader
- ModuleActivator
- ModuleManager

SDK already contains:

- Module
- ModuleContext

---

## Create the following files

backend/core/service_descriptor.py

backend/core/service_container.py

backend/core/service_provider.py

backend/core/exceptions.py

---

## Update

backend/sdk/context.py

backend/kernel/platform.py

---

## Requirements

### ServiceDescriptor

Dataclass.

Fields:

- service_type
- implementation
- singleton

---

### ServiceContainer

Responsibilities:

register()

register_instance()

resolve()

exists()

clear()

Support singleton services.

Support transient services.

Raise custom exceptions.

---

### ServiceProvider

Read-only wrapper around ServiceContainer.

Expose only:

resolve()

exists()

Modules must never register services directly.

---

### Exceptions

Create:

ServiceNotFoundError

ServiceAlreadyRegisteredError

---

### ModuleContext

Extend ModuleContext.

Add

services: ServiceProvider

Platform: Platform

Modules should access services as

context.services.resolve(Logger)

---

### Platform

Platform owns ServiceContainer.

Expose

platform.services

Create ServiceProvider automatically.

Pass ServiceProvider into ModuleContext.

---

## Constraints

No globals.

No decorators.

No reflection.

No metaclasses.

No external libraries.

Python 3.14

PEP8

Complete type hints.

Google-style docstrings.

---

## Output

Return complete files.

For every file output

=== FILE: path/to/file.py

followed by the complete source.

No explanations.