# Debugging & Crash Prevention for GTP Callback

Handling GTP metrics in your Python xApp requires caution, as SWIG-based callbacks can crash your application if an exception occurs inside `handle()`.

This guide covers how to avoid common issues when accessing `ind.gtp_stats`.

---

## Common Fatal Error

```text
terminate called after throwing an instance of 'Swig::DirectorMethodException'
what():  SWIG director method error. Error detected when calling 'gtp_cb.handle'
```

### Root Causes:

* An exception (e.g., `AttributeError`) is thrown in your Python `handle()` method
* SWIG cannot catch this error, so the entire xApp crashes

---

## Always Use try/except

Wrap the full `handle()` logic:

```python
def handle(self, ind):
    try:
        # GTP logic here
        ...

    except Exception as e:
        print("❌ ERROR in GTPCallback.handle():", e)
```

---

## Safe Field Access

Don’t assume all fields are always present — use:

```python
tx = getattr(stat, "tx_total_bytes", None)
```

This prevents errors like:

```text
AttributeError: 'gtp_ngu_stats_impl_t' object has no attribute 'tx_total_bytes'
```

---

## Discover Fields with `dir()`

Use this to inspect what’s available at runtime:

```python
print("GTP stat fields:", dir(ind.gtp_stats[0]))
```

---

## Always Check Vector Size

Avoid accessing `gtp_stats[0]` without checking:

```python
if len(ind.gtp_stats) > 0:
    stat = ind.gtp_stats[0]
```

---

## Dump All Fields Safely

```python
for attr in dir(stat):
    if not attr.startswith("_"):
        try:
            print(f"{attr}: {getattr(stat, attr)}")
        except Exception as e:
            print(f"{attr}: [Error reading: {e}]")
```

---

## Summary of Defensive Techniques

| Practice                  | Benefit                         |
| ------------------------- | ------------------------------- |
| `try/except` block        | Prevents total xApp crash       |
| `getattr()` / `hasattr()` | Avoids `AttributeError`         |
| `dir()` on objects        | Discover field availability     |
| Vector size checks        | Prevents `IndexError`           |
| Graceful field logging    | Enables safe debugging and logs |

---

## Final Tip

Even though GTP metrics are simpler than MAC/PDCP, always treat SWIG callbacks as unsafe zones. Be defensive!

---

> Final step: Full GTP field reference
> 👉 [`06_field_reference.md`](./06_field_reference.md)