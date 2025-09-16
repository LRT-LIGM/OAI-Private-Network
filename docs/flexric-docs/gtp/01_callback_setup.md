# Setting Up the Python GTP Callback

To receive GTP metrics in your xApp, you need to implement a Python class that inherits from the SWIG-exposed `ric.gtp_cb` interface.

This file explains how to define the callback class, override the `handle()` method, and register it to receive GTP user-plane metrics from the E2 Agent.

---

## Base Class: `ric.gtp_cb`

In the FlexRIC Python SDK, the GTP Service Model provides this callback interface:

```cpp
virtual void handle(swig_gtp_ind_msg_t a) = 0;
```

Your Python class must override this method to handle incoming GTP metrics.

---

## Python Implementation

Here’s a minimal working version of a callback class:

```python
import ric  # FlexRIC SWIG bindings

class GTPCallback(ric.gtp_cb):
    def __init__(self):
        super().__init__()  # Properly initialize base class

    def handle(self, ind):
        print("📥 GTP Indication received")
        print("Type of ind:", type(ind))
        print("Available attributes:", dir(ind))
```

---

## Registering the Callback

Once your xApp is connected to the RIC and the GTP SM is active, register the callback like this:

```python
gtp_cb = GTPCallback()
hndlr = ric.report_gtp_sm(conn[i].id, ric.Interval_ms_1, gtp_cb)
```

You can adjust the reporting interval with `Interval_ms_10`, `Interval_ms_100`, etc.

---

## Best Practices

* Always call `super().__init__()` in the constructor
* Use `try/except` to protect the `handle()` logic from crashing the app
* Use `dir(ind)` and `dir(ind.gtp_stats[0])` to discover available attributes
* Always use `getattr()` or `hasattr()` to access fields safely

---

## What’s Next?

Now that your callback is set up, we’ll show how to extract and inspect the GTP metrics in `ind.gtp_stats`.

> Continue to: [`02_access_gtp_stats.md`](./02_access_gtp_stats.md)

