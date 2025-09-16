# Debugging & Crash Prevention for MAC Callback

When working with FlexRIC’s Python bindings via SWIG, it's easy to crash your entire xApp with a single unhandled Python error — especially inside the `handle()` callback.

This guide explains how to protect your app from:
- `Swig::DirectorMethodException` crashes
- Missing attributes
- Malformed data
- Unexpected runtime behavior

---

## Common Fatal Error

```text
terminate called after throwing an instance of 'Swig::DirectorMethodException'
what():  SWIG director method error. Error detected when calling 'mac_cb.handle'
```

### Why it happens:

* Your `handle()` function throws a Python exception (e.g. `AttributeError`, `IndexError`, etc.)
* SWIG can’t catch it and lets it crash the C++ runtime.

---

## Wrap `handle()` with try/except

Always, always wrap the whole method:

```python
def handle(self, ind):
    try:
        # Your logic here
        ...

    except Exception as e:
        print("❌ ERROR in MACCallback.handle():", e)
```

---

## Safe Attribute Access

Never assume a field exists — use `getattr()` or `hasattr()`:

```python
dl_mcs = getattr(ue, "dl_mcs", None)
if dl_mcs is not None:
    print("DL MCS:", dl_mcs)
```

This prevents errors like:

```text
AttributeError: 'mac_ue_stats_impl_t' object has no attribute 'dl_mcs'
```

---

## Use `dir()` to Explore

Debug live objects at runtime to understand what you’re dealing with:

```python
print("ind attributes:", dir(ind))
print("ue_stats[0] attributes:", dir(ind.ue_stats[0]))
```

Also useful to inspect missing timestamps or unknown vector structures.

---

## Avoid Hardcoded Indexes

Always check that the vector has elements before accessing:

```python
if len(ind.ue_stats) > 0:
    ue = ind.ue_stats[0]
```

---

## Fallback Logging Tool

Use this pattern to dump everything safely:

```python
for attr in dir(ue):
    if not attr.startswith("_"):
        try:
            print(f"{attr}: {getattr(ue, attr)}")
        except Exception as e:
            print(f"{attr}: [Error reading: {e}]")
```

---

## Summary

| Practice                           | Why it's important           |
| ---------------------------------- | ---------------------------- |
| `try/except` inside `handle()`     | Prevents total app crash     |
| `getattr()` / `hasattr()`          | Avoids AttributeError        |
| `dir()` exploration                | Discover undocumented fields |
| Length check on vectors            | Prevents IndexError          |
| Graceful logging of unknown fields | Keeps logs clean and useful  |

---

## Final Tip

FlexRIC is powerful but low-level. Treat every callback as potentially unsafe — defensive programming is essential.

---

> You’ve now completed the full MAC metrics logging guide.
Return to [Overview](./00_overview.md) or begin documenting RLC, PDCP, or SLICE metrics.
