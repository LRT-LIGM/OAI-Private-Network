# Setting Up the Python RLC Callback

To receive RLC layer metrics in your FlexRIC-based xApp, you need to implement a Python class that inherits from the SWIG-exposed interface `ric.rlc_cb`.

This file explains how to create the callback, override the method to receive metrics, and register the callback to start receiving indications.

---

## Base Class: `ric.rlc_cb`

In the FlexRIC Python SDK, the RLC Service Model provides a virtual callback interface:

```cpp
virtual void handle(swig_rlc_ind_msg_t a) = 0;
```

Your Python class should override this `handle()` method to receive real-time updates from the E2 Agent.

---

## Python Implementation

Here is a minimal implementation of the RLC callback class:

```python
import ric  # Import FlexRIC SWIG bindings

class RLCCallback(ric.rlc_cb):
    def __init__(self):
        super().__init__()  # Initialize the base SWIG object

    def handle(self, ind):
        print("📥 RLC Indication received")
        print("Type of ind:", type(ind))
        print("Available attributes in ind:", dir(ind))
```

---

## Registering the Callback

In your xApp’s main logic, after initializing the RIC connection and loading the RLC SM plugin, register the callback like this:

```python
rlc_cb = RLCCallback()
hndlr = ric.report_rlc_sm(conn[i].id, ric.Interval_ms_1, rlc_cb)
```

This tells FlexRIC to send RLC metrics every 1ms for the selected E2 Node and pass them to your `handle()` method.

> You can adjust `ric.Interval_ms_1` to other intervals like `Interval_ms_10` or `Interval_ms_100`.

---

## Best Practices

* Always call `super().__init__()` in your constructor to avoid SWIG initialization issues.
* Wrap all your `handle()` logic in `try/except` to avoid crashing the app due to Python errors.
* Use `dir(ind)` and `dir(ind.rb_stats[0])` to explore available fields at runtime.
* Log only verified or available fields using `getattr()` or `hasattr()`.

---

## What’s Next?

In the next section, we’ll look at how to access and parse the `rb_stats` field from the `ind` object, which contains RLC statistics for each radio bearer.

> Continue to: [`02_access_rb_stats.md`](./02_access_rb_stats.md)