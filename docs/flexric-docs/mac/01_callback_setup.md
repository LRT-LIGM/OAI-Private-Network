# Setting Up the Python MAC Callback

To receive MAC layer metrics in a FlexRIC-based xApp, you need to implement a Python class that overrides the virtual method `handle()` from the C++ interface `ric.mac_cb`.

This section walks you through creating the callback and preparing it to receive MAC Indication messages.

---

## Base Class: `ric.mac_cb`

In the FlexRIC Python SDK (via SWIG), the MAC Service Model defines a callback interface `mac_cb`, which includes the virtual method:

```cpp
virtual void handle(swig_mac_ind_msg_t a) = 0;
```

Your Python class must override this method to receive periodic updates from the E2 Agent.

---

## Python Implementation

Here’s a basic, working version of a callback class:

```python
import time
import ric  # Import FlexRIC SWIG bindings

class MACCallback(ric.mac_cb):
    def __init__(self):
        super().__init__()  # Call the C++ base constructor

    def handle(self, ind):
        print("📥 MAC Indication received")
        print("Type of ind:", type(ind))
        print("Available attributes in ind:", dir(ind))
```

---

## Registering the Callback

In your xApp initialization code, after connecting to the RIC and setting up the MAC SM plugin, register your callback like this:

```python
mac_cb_instance = MACCallback()
mac_plugin = ric.get_mac_sm()  # Or however you obtain the MAC service model

# Register callback
mac_plugin.set_indication_callback(mac_cb_instance)
```

This ensures your `handle()` method is called every time a new MAC Indication is received.

---

## Best Practices

* Always use `super().__init__()` to correctly initialize the base SWIG object.
* Place all logic inside `try/except` blocks to avoid terminating the app due to a Python-side error.
* Use `print(dir(ind))` to explore available attributes in the `ind` object.
* Avoid using unverified fields directly — always check with `hasattr()`.

---

## What’s Next?

In the next section, we’ll explore how to access UE-specific metrics from `ind.ue_stats`, which contains a vector of `mac_ue_stats_impl_t` objects.

> Continue to: [`02_access_ue_stats.md`](./02_access_ue_stats.md)