# Debugging & Crash Prevention for PDCP Callback

When working with FlexRIC’s SWIG-based Python interface, a single unhandled exception in your `PDCPCallback.handle()` method can crash the entire xApp.

This guide outlines best practices for debugging, inspecting runtime objects, and preventing app crashes when handling `swig_pdcp_ind_msg_t`.

---

## Common Fatal Error

```text
terminate called after throwing an instance of 'Swig::DirectorMethodException'
what():  SWIG director method error. Error detected when calling 'pdcp_cb.handle'
```

### Why it Happens:

* An exception (e.g., `AttributeError`, `IndexError`) occurred inside `handle()`
* SWIG cannot catch it and propagates the error to C++, killing the process

---

## Always Use try/except

Wrap your entire `handle()` logic in a `try/except` block:

```python
def handle(self, ind):
    try:
        # Your PDCP logic
        ...

    except Exception as e:
        print("❌ ERROR in PDCPCallback.handle():", e)
```

---

## Safe Field Access

Never assume a field exists. Use `getattr()` or `hasattr()`:

```python
tx_bytes = getattr(rb, 'txpdu_bytes', 0)
```

Avoids errors like:

```text
AttributeError: 'pdcp_rb_stats_impl_t' object has no attribute 'txpdu_bytes'
```

---

## Explore with `dir()`

To see all available fields:

```python
print("ind fields:", dir(ind))
print("rb_stats[0] fields:", dir(ind.rb_stats[0]))
```

Useful for checking field names across FlexRIC versions.

---

## Check Vector Length First

Before accessing `rb_stats[0]`, always do:

```python
if len(ind.rb_stats) > 0:
    rb = ind.rb_stats[0]
```

---

## Dump All Fields Safely

Print all PDCP metrics without risking a crash:

```python
for attr in dir(rb):
    if not attr.startswith("_"):
        try:
            print(f"{attr}: {getattr(rb, attr)}")
        except Exception as e:
            print(f"{attr}: [Error reading: {e}]")
```

---

## Summary: Defensive Programming Checklist

| Technique               | Benefit                       |
| ----------------------- | ----------------------------- |
| `try/except`            | Prevents total crash          |
| `getattr()`             | Avoids AttributeError         |
| `dir()` + `print()`     | Discover field names          |
| Length check on vectors | Avoids IndexError             |
| Safe field dumping      | Helps in debugging structures |

---

## Final Tip

The PDCP plugin exposes a large number of metrics — write modular and resilient logging to gradually explore and refine the output based on your needs.

---

> Final step: Full PDCP field reference
> 👉 [`06_field_reference.md`](./06_field_reference.md)