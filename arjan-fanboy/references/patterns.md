# Design Patterns from ArjanCodes

Common design patterns that Arjan uses and recommends, with both OOP and Pythonic approaches.

## Table of Contents

1. [Strategy Pattern](#strategy-pattern)
2. [Observer Pattern](#observer-pattern)
3. [Factory Pattern (Pythonic)](#factory-pattern-pythonic)
4. [Template Method Pattern](#template-method-pattern)
5. [Bridge Pattern](#bridge-pattern)
6. [MVC Architecture](#mvc-architecture)

## Strategy Pattern

### Classic OOP Approach
```python
class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        pass

class CustomerSupport:
    def __init__(self, processing_strategy: TicketOrderingStrategy):
        self.processing_strategy = processing_strategy
```

### Functional/Pythonic Approach
```python
Ordering = Callable[[SupportTickets], SupportTickets]

def fifo_ordering(tickets: SupportTickets) -> SupportTickets:
    return tickets.copy()

class CustomerSupport:
    def process_tickets(self, ordering: Ordering):
        ticket_list = ordering(self.tickets)
```

**Key Insight**: Prefer functional approaches for simple strategies

## Observer Pattern

- Use event-driven architecture with event handlers
- Decouple event producers from consumers
- Register event listeners at startup

```python
# Setup patterns
setup_slack_event_handlers()
setup_log_event_handlers()
setup_email_event_handlers()

# Publishing events
post_event("user_upgrade_plan", user)
```

## Factory Pattern (Pythonic)

- Use dictionaries mapping strings to classes/functions
- Avoid complex factory classes when simple lookups suffice

```python
EXPORTERS = {
    "csv": export_to_csv,
    "json": export_to_json,
}

def get_exporter(format: str) -> ExportFn:
    return EXPORTERS[format]
```

## Template Method Pattern

- Define skeleton of algorithm in base class
- Allow subclasses to override specific steps
- Use abstract methods for required implementations
- Provide hooks for optional customization

## Bridge Pattern

- Separate abstraction from implementation
- Use composition to connect them
- Allows independent variation

## MVC Architecture

- Separate Model, View, and Controller concerns
- Use protocols to define interfaces between components
- Controller mediates between Model and View
