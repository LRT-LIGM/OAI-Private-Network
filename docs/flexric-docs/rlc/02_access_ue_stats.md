# Accessing RLC Bearer Stats from Indication

When the RLC callback is triggered, the `handle()` method receives an object `ind` of type `swig_rlc_ind_msg_t`.

This object contains a key field:

```python
ind.rb_stats
```

This is a SWIG-wrapped vector of `rlc_rb_stats_impl_t` — each entry represents the RLC statistics for a specific Radio Bearer (RB), typically one per UE or per bearer.

---

## Looping Over `rb_stats`

You can iterate through the vector like a regular Python list:

```python
def handle(self, ind):
    try:
        num_rbs = len(ind.rb_stats)
        print(f"📦 Number of RBs in indication: {num_rbs}")

        for i in range(num_rbs):
            rb = ind.rb_stats[i]
            print(f"RB #{i} object:", rb)

    except Exception as e:
        print("❌ Error accessing RB stats:", e)
```

---

## Exploring Available Fields

Use `dir()` to inspect what attributes each `rb_stats` element has:

```python
rb = ind.rb_stats[0]
print("Available fields:", dir(rb))
```

Depending on your FlexRIC version, you might see fields like:

* `rnti`
* `tx_bytes`, `rx_bytes`
* `mode`, `sn_tx`, `sn_rx`
* ... and more.

---

## Safe Field Access Example

Here’s how to log basic fields with safe defaults:

```python
for i in range(len(ind.rb_stats)):
    rb = ind.rb_stats[i]

    try:
        rnti = getattr(rb, 'rnti', None)
        tx_bytes = getattr(rb, 'tx_bytes', None)
        rx_bytes = getattr(rb, 'rx_bytes', None)

        print(f"RB[{i}] RNTI: {rnti}, TX: {tx_bytes}, RX: {rx_bytes}")

    except Exception as e:
        print(f"⚠️ Error reading RB[{i}]:", e)
```

---

## Full Dump (Optional)

To log all available fields dynamically:

```python
for attr in dir(rb):
    if not attr.startswith("_"):
        try:
            print(f"{attr}: {getattr(rb, attr)}")
        except Exception as e:
            print(f"{attr}: [Error reading: {e}]")
```

This is especially useful when you're unsure of the exact structure of `rlc_rb_stats_impl_t`.

---

## Summary

* `ind.rb_stats` contains one entry per Radio Bearer with RLC stats
* Use `len()` and indexing to loop through the vector
* Use `getattr()` to safely access fields
* Use `dir()` to discover available attributes at runtime

---

> Next: Display RLC metrics and timestamps in terminal logs
> --> [`03_display_metrics.md`](./03_display_metrics.md)