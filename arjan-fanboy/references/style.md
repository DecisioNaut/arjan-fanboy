# Code Style & Conventions from ArjanCodes

Arjan's preferred coding style, naming conventions, and anti-patterns to avoid.

## Table of Contents

### Code Style
1. [Type Hints](#type-hints---always)
2. [Dataclasses](#dataclasses-for-data-containers)
3. [Protocol Classes](#protocol-classes-duck-typing)
4. [Function Naming](#function-naming)
5. [Class Naming](#class-naming)
6. [Module Organization](#module-organization)
7. [Modern Python Features](#use-modern-python-features)
8. [Properties](#properties-over-getterssetters)
9. [Functools](#use-functools-for-functional-patterns)
10. [Dataclass Features](#dataclass-features)

### Anti-Patterns
1. [God Classes](#1-god-classes--low-cohesion)
2. [Intimacy / Feature Envy](#2-intimacy--feature-envy-high-coupling)
3. [Type Issues](#3-not-returningusing-types)
4. [Wildcard Imports](#4-wildcard-imports)
5. [Mutable Defaults](#5-mutable-default-arguments)
6. [Deep Inheritance](#6-deep-inheritance-hierarchies)
7. [Missing Dataclasses](#7-not-using-dataclasses-for-simple-data)
8. [Length Checks](#8-checking-len--0-instead-of-truthiness)
9. [String Enums](#9-using-strings-for-enums)
10. [Overengineering](#10-overengineering--premature-abstraction)

---

## Code Style & Conventions

### Type Hints - Always
```python
def calculate_average(numbers: list[int | float]) -> float:
    return sum(numbers) / len(numbers)

def process_order(email_service: Emailer, order: Order) -> None:
    email_service.send_email(order.customer_email, "Order processed")
```

**Key Points**:
- Use type hints for all function signatures
- Use `Protocol` for structural typing (duck typing)
- Use modern type syntax: `list[str]` instead of `List[str]`
- Use union types with `|` operator: `str | None`
- Import `from __future__ import annotations` for forward references

### Dataclasses for Data Containers
```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)
```

**Benefits over regular classes**:
- Automatic `__init__`, `__repr__`, `__eq__`
- Less boilerplate
- Clear data structure intent
- Use `field()` for advanced features

### Protocol Classes (Duck Typing)
```python
from typing import Protocol

class Notifier(Protocol):
    def send(self, message: str) -> None: ...

class EmailNotifier:
    def send(self, message: str) -> None:
        print(f"Email: {message}")

def notify_user(notifier: Notifier, message: str) -> None:
    notifier.send(message)
```

**When to use**:
- Prefer Protocol over ABC for duck-typed interfaces
- Use ABC when you need concrete shared implementation
- Protocols provide structural subtyping (no inheritance required)

### Function Naming
- **Verbs for actions**: `calculate_total`, `send_email`, `process_order`
- **Adjectives/nouns for queries**: `is_valid`, `has_discount`, `total_price`
- **Lowercase with underscores**: `snake_case` for functions and variables
- **Private with underscore prefix**: `_private_function`, `_internal_helper`

### Class Naming
- **PascalCase**: `PaymentProcessor`, `CustomerSupport`
- **Descriptive and specific**: `DebitPaymentProcessor` not `Processor`
- **Avoid prefixes/suffixes**: Don't use `I` for interfaces or `Abs` for abstract

### Module Organization
```python
# Standard library imports
import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol

# Third-party imports
import pandas as pd

# Local imports
from .models import Order
from .services import EmailService
```

### Use Modern Python Features
```python
# Modern type aliases
type Data = list[dict[str, Any]]

# Type parameters (Python 3.12+)
class Repository[T](ABC):
    @abstractmethod
    def get(self, id: int) -> T: ...

# Structural pattern matching
match payment_type:
    case "debit":
        process_debit()
    case "credit":
        process_credit()
```

### Properties over Getters/Setters
```python
# Don't do this (Java-style)
class Person:
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name

# Do this (Pythonic)
@dataclass
class Person:
    name: str

# Or with property if validation needed
class Person:
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
```

### Use `functools` for Functional Patterns
```python
from functools import lru_cache, partial, cached_property

@lru_cache
def bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)

@dataclass(frozen=True)
class Endpoint:
    url: str
    
    @cached_property
    def parsed(self):
        return urlparse(self.url)
```

### Dataclass Features
```python
@dataclass(frozen=True, slots=True, kw_only=True, order=True)
class User:
    name: str
    age: int
    email: str = field(repr=False)
    _internal: str = field(init=False, repr=False, default="")
```

---

## Anti-Patterns to Avoid

### 1. God Classes / Low Cohesion
**Don't**: Cram all functionality into one class
```python
class Company:
    def find_managers(self): ...
    def find_vice_presidents(self): ...
    def find_interns(self): ...
    def pay_employee(self): ...
    def send_emails(self): ...
    def generate_reports(self): ...
```

**Do**: Split by responsibility
```python
class EmployeeFinder:
    def find_by_role(self, role: Role): ...

class PayrollService:
    def pay_employee(self, employee: Employee): ...
```

### 2. Intimacy / Feature Envy (High Coupling)
**Don't**: Reach into other objects' data
```python
def generate_breadcrumbs(location: Location) -> dict[str, str]:
    return {
        "latitude": str(location.geolocation.latitude),
        "longitude": str(location.geolocation.longitude),
    }
```

**Do**: Let objects handle their own data
```python
@dataclass
class Geolocation:
    latitude: float
    longitude: float
    
    def to_dict(self) -> dict[str, str]:
        return {
            "latitude": str(self.latitude),
            "longitude": str(self.longitude),
        }

def generate_breadcrumbs(geolocation: Geolocation) -> dict[str, str]:
    return geolocation.to_dict()
```

### 3. Not Returning/Using Types
**Don't**: Return booleans or None when more info is needed
```python
def to_uri(s: str | int | bytes) -> URI | bool:  # Bad: mixes types
    if not s:
        return False
    return URI(...)
```

**Do**: Raise exceptions or use Optional
```python
def to_uri(s: str) -> URI:
    if not s:
        raise ValueError("Input cannot be empty")
    return URI(...)
```

### 4. Wildcard Imports
```python
# Don't
from random import *
from string import *

# Do
import random
import string
```

### 5. Mutable Default Arguments
```python
# Don't
def add_item(items=[]):  # Dangerous!
    items.append("new")
    return items

# Do
from dataclasses import field

@dataclass
class Container:
    items: list[str] = field(default_factory=list)
```

### 6. Deep Inheritance Hierarchies
```python
# Don't
class Employee: pass
class Manager(Employee): pass
class SeniorManager(Manager): pass
class Director(SeniorManager): pass

# Do - Use composition with enums
class Role(StrEnum):
    EMPLOYEE = "Employee"
    MANAGER = "Manager"

class Employee:
    def __init__(self, role: Role):
        self.role = role
```

### 7. Not Using Dataclasses for Simple Data
```python
# Don't
class PersonNoDataClass:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.email_addresses = []

# Do
@dataclass
class Person:
    name: str
    address: str
    email_addresses: list[str] = field(default_factory=list)
```

### 8. Checking `len() == 0` Instead of Truthiness
```python
# Don't
if len(tickets) == 0:
    print("No tickets")

# Do
if not tickets:
    print("No tickets")
```

### 9. Using Strings for Enums
```python
# Don't
class Employee:
    role: str  # Can be any string!

# Do
class Role(StrEnum):
    INTERN = "intern"
    MANAGER = "manager"
    
class Employee:
    role: Role
```

### 10. Overengineering / Premature Abstraction
Don't create complex factory hierarchies when a simple dictionary lookup suffices:

```python
# Overengineered
class ExporterFactory:
    @staticmethod
    def create_exporter(format: str) -> Exporter:
        if format == "csv":
            return CSVExporter()
        elif format == "json":
            return JSONExporter()

# Simple and clear
EXPORTERS = {
    "csv": export_to_csv,
    "json": export_to_json,
}
```
