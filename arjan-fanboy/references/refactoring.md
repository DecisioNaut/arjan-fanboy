# Common Refactoring Patterns from ArjanCodes

Step-by-step refactoring patterns extracted from Arjan's actual code examples.

## Table of Contents

1. [Extract Payment Logic (SRP Violation → Fix)](#1-extract-payment-logic-srp-violation--fix)
2. [Replace Conditionals with Polymorphism (OCP)](#2-replace-conditionals-with-polymorphism-ocp)
3. [Fix Liskov Violation](#3-fix-liskov-violation)
4. [Interface Segregation](#4-interface-segregation)
5. [Introduce Abstraction (DIP)](#5-introduce-abstraction-dip)
6. [Reduce Coupling via Cohesion](#6-reduce-coupling-via-cohesion)

## 1. Extract Payment Logic (SRP Violation → Fix)

**Before**:
```python
class Order:
    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment")
            self.status = "paid"
```

**After**:
```python
class Order:
    def total_price(self): ...

class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print("Processing debit payment")
        order.status = "paid"
```

## 2. Replace Conditionals with Polymorphism (OCP)

**Before**:
```python
def process_tickets(self):
    if self.processing_strategy == "fifo":
        # process FIFO
    elif self.processing_strategy == "filo":
        # process FILO
```

**After**:
```python
class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, tickets): ...

class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets):
        return tickets.copy()
```

## 3. Fix Liskov Violation

**Before (LSP violation - different signature)**:
```python
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code): pass

class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):  # security_code is email!
        print(f"Using email: {security_code}")
```

**After (LSP compliant)**:
```python
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order): pass

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address):
        self.email_address = email_address
    
    def pay(self, order):
        print(f"Using email: {self.email_address}")
```

## 4. Interface Segregation

**Before (clients forced to implement unused methods)**:
```python
class PaymentProcessor(ABC):
    @abstractmethod
    def auth_sms(self, code): pass
    
    @abstractmethod
    def pay(self, order): pass
```

**After (segregated interfaces)**:
```python
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order): pass

class PaymentProcessorSMS(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code): pass
```

**Even Better (Composition over inheritance)**:
```python
class SMSAuthorizer:
    def verify_code(self, code):
        self.authorized = True

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email: str, authorizer: SMSAuthorizer):
        self.authorizer = authorizer
```

## 5. Introduce Abstraction (DIP)

**Before**:
```python
class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: SMSAuthorizer):
        self.authorizer = authorizer  # Concrete dependency
```

**After**:
```python
class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool: pass

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer  # Abstract dependency
```

## 6. Reduce Coupling via Cohesion

**Before**:
```python
# Everything in one class
class Vehicle:
    brand: str
    electric: bool
    catalogue_price: float
    
    def compute_tax(self):
        tax_percentage = 0.05 if not self.electric else 0.02
        return tax_percentage * self.catalogue_price
```

**After**:
```python
@dataclass
class VehicleInfo:
    brand: str
    electric: bool
    catalogue_price: float
    
    def compute_tax(self):
        tax_percentage = 0.02 if self.electric else 0.05
        return tax_percentage * self.catalogue_price

@dataclass
class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo
```
