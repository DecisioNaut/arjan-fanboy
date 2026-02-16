# Concrete Examples from ArjanCodes

Complete refactoring journeys showing how to evolve code through SOLID principles and patterns.

## Table of Contents

1. [Order Payment System Evolution](#example-1-order-payment-system-evolution)
2. [Strategy Pattern Evolution](#example-2-strategy-pattern-evolution)
3. [Dependency Injection with Protocols](#example-3-dependency-injection-with-protocols)
4. [MVC Pattern](#example-4-mvc-pattern)
5. [Composition Over Inheritance](#example-5-composition-over-inheritance)

## Example 1: Order Payment System Evolution

### Stage 1: Violation of SRP
```python
class Order:
    def pay(self, payment_type: str, security_code: str):
        if payment_type == "debit":
            print("Processing debit")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit")
            self.status = "paid"
```

### Stage 2: Extract Payment (SRP Fix)
```python
class Order:
    def total_price(self): ...

class PaymentProcessor:
    def pay_debit(self, order, security_code): ...
    def pay_credit(self, order, security_code): ...
```

### Stage 3: Open/Closed Principle
```python
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code): pass

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit")
        order.status = "paid"
```

### Stage 4: Liskov Substitution Fix
```python
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order): pass  # No security_code in signature

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
```

### Stage 5: Interface Segregation
```python
class SMSAuthorizer:
    def verify_code(self, code): ...
    def is_authorized(self) -> bool: ...

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: SMSAuthorizer):
        self.authorizer = authorizer
```

### Stage 6: Dependency Inversion (Final)
```python
class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool: pass

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
```

## Example 2: Strategy Pattern Evolution

### Before (Rigid)
```python
class CustomerSupport:
    def __init__(self, processing_strategy: str = "fifo"):
        self.processing_strategy = processing_strategy
    
    def process_tickets(self):
        if self.processing_strategy == "fifo":
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif self.processing_strategy == "filo":
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)
```

### After (OOP Strategy)
```python
class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        pass

class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets):
        return tickets.copy()

class CustomerSupport:
    def __init__(self, processing_strategy: TicketOrderingStrategy):
        self.processing_strategy = processing_strategy
```

### Pythonic (Functional)
```python
from typing import Callable

Ordering = Callable[[list[SupportTicket]], list[SupportTicket]]

def fifo_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return tickets.copy()

def filo_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return list(reversed(tickets))

class CustomerSupport:
    def process_tickets(self, ordering: Ordering):
        ticket_list = ordering(self.tickets)
        for ticket in ticket_list:
            self.process_ticket(ticket)
```

## Example 3: Dependency Injection with Protocols

```python
from typing import Protocol

class EmailSender(Protocol):
    def send_message(self, to_email: str, subject: str, body: str) -> None: ...

@dataclass
class Person:
    name: str
    email: str
    email_sender: EmailSender  # Injected dependency
    
    def send_welcome_email(self) -> None:
        self.email_sender.send_message(
            to_email=self.email,
            subject="Welcome",
            body=f"Hello {self.name}!"
        )
```

## Example 4: MVC Pattern

```python
class Model:
    def __init__(self):
        self.data = []
    
    def append(self, item):
        self.data.append(item)

class View(ABC):
    @abstractmethod
    def setup(self, controller): pass
    
    @abstractmethod
    def append_to_list(self, item): pass
    
    @abstractmethod
    def start_main_loop(self): pass

class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
    
    def start(self):
        self.view.setup(self)
        self.view.start_main_loop()
    
    def handle_action(self):
        item = generate_new_item()
        self.model.append(item)
        self.view.append_to_list(item)
```

## Example 5: Composition Over Inheritance

### Before (Inheritance)
```python
class Employee: pass
class Manager(Employee): pass
class SeniorManager(Manager): pass
class Director(SeniorManager): pass
```

### After (Composition)
```python
from enum import StrEnum

class Role(StrEnum):
    EMPLOYEE = "Employee"
    MANAGER = "Manager"
    SENIOR_MANAGER = "Senior Manager"
    DIRECTOR = "Director"

class Employee:
    def __init__(self, role: Role):
        self.role =role
```
