# 🧠 Singleton Pattern – COMPLETE Deep Notes (Python)

---

# 1️⃣ What Is Singleton?

Singleton is a **creational design pattern** that:

- Ensures a class has only ONE instance
- Provides a global access point to that instance

It controls **object creation**, not object usage.

---

# 2️⃣ Why Singleton Exists

Problem:
Some components must not have multiple instances because:

- It wastes memory
- It causes inconsistent shared state
- It duplicates expensive resources
- It creates synchronization issues

Singleton ensures:
> One shared instance across the entire application.

---

# 3️⃣ Python Object Creation – Internal Mechanism

When you write:

```
obj = MyClass()
```

Python internally performs:

1. Calls `MyClass.__new__(MyClass)`
2. If returned object is instance of `MyClass`:
   - Calls `MyClass.__init__(obj)`
3. Returns object

Execution order:

```
__new__ → __init__
```

---

# 4️⃣ Deep Difference: `__new__` vs `__init__`

## `__new__(cls)`

- Responsible for creating object
- Allocates memory
- Returns instance
- Can return existing instance
- Can return completely different object

Singleton logic MUST go here.

---

## `__init__(self)`

- Initializes object
- Runs AFTER object creation
- Cannot stop new instance creation
- Runs every time new instance is created

Important internal rule:

If `__new__` returns an object that is NOT instance of the class:

```
isinstance(returned_object, cls) → False
```

Python skips `__init__`.

---

# 5️⃣ Basic Singleton Implementation

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

Flow:

First call:
- `_instance` is None
- New object created
- Stored in `_instance`
- Returned

Second call:
- `_instance` already exists
- Same object returned

---

# 6️⃣ What Happens If `__new__` Returns Something Else?

Example:

```python
class A:
    def __new__(cls):
        return 10

a = A()
```

Result:

- `__new__` returns integer `10`
- `isinstance(10, A)` → False
- `__init__` is skipped
- `a` becomes `10`

This breaks expected class behavior.

---

# 7️⃣ Multithreading Problem (Race Condition)

Problem:

Two threads execute:

```
if _instance is None:
```

Both see `_instance` as None.

Both create object.

Now two instances exist.

This violates Singleton guarantee.

This is called:

> Race Condition

---

# 8️⃣ Thread-Safe Singleton (Using Lock)

Solution: Use a mutual exclusion lock.

```python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance
```

What Lock Does:

- Only one thread enters block at a time
- Prevents simultaneous creation
- Guarantees single instance

---

# 9️⃣ Where Singleton SHOULD Be Used

Infrastructure-level shared services:

- Logger
- Configuration Manager
- Cache Manager
- Metrics Collector
- Feature Flags
- Scheduler
- Thread Pool Manager
- Database Connection Pool Manager

These are:

- Shared
- Global
- System-level components

---

# 🔟 Where Singleton SHOULD NOT Be Used

Domain / Business objects:

- User
- Order
- Account
- Session
- Request
- Invoice
- Product

Reason:

They represent multiple real-world entities.
They require independent state.

---

# 1️⃣1️⃣ Database Interview Trap

Wrong:

> Database connection should be Singleton.

Correct:

> Database connection POOL MANAGER should be Singleton.

Why?

- You need multiple DB connections.
- But only one pool controller.

---

# 1️⃣2️⃣ Interview Signal Words

If question mentions:

- Shared resource
- One source of truth
- Central manager
- Global configuration
- Expensive object creation

→ Think Singleton

If question mentions:

- Per user
- Per request
- Independent entities

→ Not Singleton

---

# 1️⃣3️⃣ Advantages

- Controlled resource usage
- Consistent shared state
- Centralized access
- Prevents duplication

---

# 1️⃣4️⃣ Disadvantages

- Harder to test (global state)
- Hard to mock
- Hidden dependencies
- Can become anti-pattern if overused
- May violate Single Responsibility Principle

---

# 1️⃣5️⃣ Perfect Interview Answer

Singleton is a creational design pattern that restricts a class to one instance and provides a global access point to it, typically used for shared infrastructure components.