# Setting Up the Python PDCP Callback

To access PDCP metrics in a FlexRIC-based xApp, you need to implement a Python class that inherits from `ric.pdcp_cb` — the callback interface exposed via SWIG.

This guide walks you through creating that class, overriding the `handle()` method, and registering the callback to start receiving periodic PDCP indications.

---

## Base Class: `ric.pdcp_cb`

In the FlexRIC Python SDK, the PDCP Service Model provides the following virtual method:

```cpp
virtual void handle(swig_pdcp_ind_msg_t a) = 0;
```

You must override this in your Python class to receive and process PDCP statistics.

---

## Python Implementation

A minimal working callback class looks like this:

```python
import ric  # FlexRIC SWIG bindings

class PDCPCallback(ric.pdcp_cb):
    def __init__(self):
        super().__init__()  # Initialize the SWIG object properly

    def handle(self, ind):
        print("📥 PDCP Indication received")
        print("Type of ind:", type(ind))
        print("Available attributes:", dir(ind))
```

---

## Registering the Callback

After initializing your xApp and connecting to the RIC, register your callback like so:

```python
pdcp_cb = PDCPCallback()
hndlr = ric.report_pdcp_sm(conn[i].id, ric.Interval_ms_1, pdcp_cb)
```

This sets up a report with 1ms periodicity. You can adjust the interval with other predefined options such as `Interval_ms_10` or `Interval_ms_100`.

---

## Best Practices

* **Always use `super().__init__()`** to initialize the SWIG base class correctly.
* **Wrap all logic in `try/except`** to prevent crashes from runtime errors.
* **Use `dir(ind)` and `dir(ind.rb_stats[0])`** to inspect available fields dynamically.
* **Never hardcode field access** — always use `getattr()` to safely retrieve values.

---

## What’s Next?

In the next step, you'll learn how to loop through the `rb_stats` vector to access detailed per-bearer PDCP metrics.

> Continue to: [`02_access_rb_stats.md`](./02_access_rb_stats.md)

