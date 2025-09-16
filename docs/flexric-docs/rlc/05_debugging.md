# Debugging & Crash Prevention for RLC Callback

When using FlexRIC’s SWIG-based Python interface, your xApp can crash if unhandled exceptions occur inside the `handle()` method of your `RLCCallback`.

This guide explains how to avoid crashes and debug common issues when working with `ind.rb_stats`.

---

## Common Fatal Error

```text
terminate called after throwing an instance of 'Swig::DirectorMethodException'
what():  SWIG director method error. Error detected when calling 'rlc_cb.handle'
```

### Root Cause:

* A Python error was raised in your `handle()` method
* SWIG cannot catch Python exceptions from virtual methods
* Result: the C++ runtime crashes your entire xApp

---

## Wrap the Entire `handle()` Method

Always use `try/except`:

```python
def handle(self, ind):
    try:
        # Your logic here
        ...

    except Exception as e:
        print("❌ ERROR in RLCCallback.handle():", e)
```

---

## Safe Attribute Access

Never assume a field exists. Use `getattr()` or `hasattr()`:

```python
tx = getattr(rb, "tx_bytes", None)
if tx is not None:
    print("TX Bytes:", tx)
```

This prevents errors like:

```text
AttributeError: 'rlc_rb_stats_impl_t' object has no attribute 'tx_bytes'
```

---

## Explore Objects with `dir()`

At runtime, print attributes to inspect:

```python
print("ind fields:", dir(ind))
print("rb_stats[0] fields:", dir(ind.rb_stats[0]))
```

This is useful for debugging new or undocumented builds.

---

## Check Vector Lengths First

Before accessing `rb_stats[0]`, always check:

```python
if len(ind.rb_stats) > 0:
    rb = ind.rb_stats[0]
```

---

## Safe Full Dump

Print all accessible fields without crashing:

```python
for attr in dir(rb):
    if not attr.startswith("_"):
        try:
            print(f"{attr}: {getattr(rb, attr)}")
        except Exception as e:
            print(f"{attr}: [Error reading: {e}]")
```

---

## Summary of Best Practices

| Technique                  | Purpose                        |
| -------------------------- | ------------------------------ |
| `try/except` in `handle()` | Avoid total xApp crash         |
| `getattr()` / `hasattr()`  | Prevent `AttributeError`       |
| `dir()` exploration        | Discover available fields      |
| Length checks              | Avoid `IndexError` on vectors  |
| Safe dumping               | Debug unknown field structures |

---

## Final Tip

Always treat callback handling as **unsafe** unless proven otherwise. Defensive coding is essential when integrating FlexRIC Python callbacks.

---

> Final Step: Full field reference of RLC metrics
> 👉 [`06_field_reference.md`](./06_field_reference.md)