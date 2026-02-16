# Core Principles from ArjanCodes

Fundamental design principles that Arjan Egges emphasizes in his Python code.

## Table of Contents

1. [SOLID Principles](#solid-principles)
2. [Coupling and Cohesion](#coupling-and-cohesion)
3. [Dependency Inversion](#dependency-inversion)
4. [Composition Over Inheritance](#composition-over-inheritance)
5. [Key Philosophies](#key-philosophies)
6. [Summary Checklist](#summary-checklist)

## SOLID Principles

Arjan emphasizes SOLID principles as fundamental to good software design:

### Single Responsibility Principle (SRP)
Each class should have one reason to change
- Separate payment logic from order management
- Extract payment processing into dedicated classes

### Open/Closed Principle (OCP)
Open for extension, closed for modification
- Use abstract base classes and inheritance for extensibility
- Create payment processor hierarchies instead of if/elif chains

### Liskov Substitution Principle (LSP)
Subtypes should be substitutable for base types
- Don't change method signatures in subclasses
- Avoid requiring different parameters than the base class

### Interface Segregation Principle (ISP)
Don't force clients to depend on interfaces they don't use
- Split large protocols into smaller, focused ones
- Use composition with `SMSAuthorizer` instead of forcing all payment processors to implement SMS auth

### Dependency Inversion Principle (DIP)
Depend on abstractions, not concretions
- Use Protocol classes or ABC for dependencies
- Inject dependencies rather than creating them internally

## Coupling and Cohesion

### Low Coupling
- Minimize dependencies between modules
- Use abstractions (Protocols/ABC) to decouple components
- Avoid direct references to concrete implementations

### High Cohesion
- Group related functionality together
- Separate concerns into distinct classes (e.g., `VehicleInfo` vs `Vehicle`)
- Each class should have a focused purpose

## Dependency Inversion

**Before (tight coupling)**:
```python
class ElectricPowerSwitch:
    def __init__(self, l: LightBulb):
        self.lightBulb = l
```

**After (loose coupling via abstraction)**:
```python
class Switchable(ABC):
    @abstractmethod
    def turn_on(self): pass
    
    @abstractmethod
    def turn_off(self): pass

class ElectricPowerSwitch:
    def __init__(self, c: Switchable):
        self.client = c
```

## Composition Over Inheritance

- Prefer composition with protocols over deep inheritance hierarchies
- Use dependency injection to compose behavior
- Example: Use separate `Authorizer` classes composed with payment processors

## Key Philosophies

1. **Pragmatism over Perfectionism**: Don't over-engineer; use the simplest solution that works
2. **Pythonic over Dogmatic**: Prefer Python's idioms over rigid OOP patterns (e.g., functions over single-method classes)
3. **Type Safety**: Use type hints everywhere for better IDE support and fewer bugs
4. **Clarity over Cleverness**: Write code that's easy to understand over clever one-liners
5. **Separation of Concerns**: Each module/class/function should have a single, well-defined purpose
6. **Testability**: Design code to be easily testable (dependency injection, pure functions)
7. **Composition over Inheritance**: Build complex behavior by combining simple pieces
8. **Protocol-Oriented Programming**: Use Protocols for flexible, duck-typed interfaces
9. **Functional When Appropriate**: Use functional programming concepts (pure functions, immutability) where they simplify code
10. **Progressive Enhancement**: Start simple, refactor to patterns as complexity grows

## Summary Checklist

When writing code "like Arjan would":

- [ ] Use type hints for all function signatures
- [ ] Use `@dataclass` for data containers
- [ ] Prefer Protocol over ABC for interfaces
- [ ] Apply SOLID principles (especially SRP and DIP)
- [ ] Keep coupling low, cohesion high
- [ ] Use descriptive, verb-based function names
- [ ] Avoid deep inheritance; prefer composition
- [ ] Use functional approaches for simple strategies
- [ ] Avoid mutable default arguments
- [ ] Use `field(default_factory=...)` for dataclass collections
- [ ] Leverage modern Python features (3.10+ syntax)
- [ ] Extract classes when a function grows complex
- [ ] Don't over-engineer; start simple
- [ ] Write self-documenting code with clear names
- [ ] Use enums instead of magic strings
