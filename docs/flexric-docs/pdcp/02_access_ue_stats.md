# Accessing PDCP Radio Bearer Stats

When your `PDCPCallback.handle()` method is triggered, it receives an object `ind` of type `swig_pdcp_ind_msg_t`.

This object contains the field:

```python
ind.rb_stats
```

This is a SWIG-wrapped `std::vector<pdcp_rb_stats_impl_t>` — one entry per Radio Bearer (RB). Each entry contains detailed PDCP statistics for a particular UE bearer.

---

## Looping Over `rb_stats`

You can iterate over `rb_stats` as you would with a Python list:

```python
def handle(self, ind):
    try:
        num_rb = len(ind.rb_stats)
        print(f"📦 Number of PDCP RBs: {num_rb}")

        for i in range(num_rb):
            rb = ind.rb_stats[i]
            print(f"RB #{i}: {rb}")

    except Exception as e:
        print("❌ Error accessing PDCP RB stats:", e)
```

---

## Exploring Available Fields

To discover which fields are available in your current FlexRIC build:

```python
rb = ind.rb_stats[0]
print("Available fields:", dir(rb))
```

This will typically include fields like:

* `rnti`, `lcid`
* `txpdu_bytes`, `txpdu_pkts`
* `rxpdu_bytes`, `rxpdu_pkts`
* `rxpdu_dup_pkts`, `rxpdu_ooo_bytes`, etc.

---

## Recommended Access Pattern

Always access attributes safely using `getattr()`:

```python
for i in range(len(ind.rb_stats)):
    rb = ind.rb_stats[i]

    try:
        rnti = getattr(rb, 'rnti', None)
        tx_bytes = getattr(rb, 'txpdu_bytes', None)
        rx_bytes = getattr(rb, 'rxpdu_bytes', None)

        print(f"RB[{i}] RNTI: {rnti}, TX: {tx_bytes}, RX: {rx_bytes}")

    except Exception as e:
        print(f"⚠️ Error reading RB[{i}]:", e)
```

---

## Optional: Full Field Dump

To print all accessible fields for debugging:

```python
for attr in dir(rb):
    if not attr.startswith("_"):
        try:
            print(f"{attr}: {getattr(rb, attr)}")
        except Exception as e:
            print(f"{attr}: [Error reading: {e}]")
```

---

## Summary

* `ind.rb_stats` contains per-bearer PDCP statistics
* Loop over it using `len()` and indexing
* Use `getattr()` for safe access
* Use `dir()` to inspect what fields are exposed by your SWIG bindings

---

> Next: Display and format metrics with timestamps
> 👉 [`03_display_metrics.md`](./03_display_metrics.md)
