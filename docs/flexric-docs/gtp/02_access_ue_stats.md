# Accessing GTP Stats from the Indication

When your `GTPCallback.handle()` function is triggered, it receives a `swig_gtp_ind_msg_t` object called `ind`.

This object contains:

```python
ind.gtp_stats
```

This is a vector of `gtp_ngu_stats_impl_t` — each entry provides metrics for one GTP-U tunnel, identified by its `teid`.

---

## Looping Over `gtp_stats`

Use standard Python list iteration:

```python
def handle(self, ind):
    try:
        print(f"📦 GTP Indication contains {len(ind.gtp_stats)} TEIDs")

        for i, stat in enumerate(ind.gtp_stats):
            print(f"GTP[{i}]:", stat)

    except Exception as e:
        print("❌ Error accessing GTP stats:", e)
```

---

## Inspecting Available Fields

You can dynamically check which fields exist:

```python
stat = ind.gtp_stats[0]
print("Fields available in stat:", dir(stat))
```

Typical fields include:

* `teid`
* `tx_total_bytes`, `rx_total_bytes`
* `tx_total_pkts`, `rx_total_pkts`
* `tx_drop_bytes`, `rx_drop_bytes`
* `status`

---

## Safe Field Access Pattern

Always use `getattr()` to prevent crashes:

```python
for stat in ind.gtp_stats:
    teid = getattr(stat, 'teid', 'N/A')
    tx_bytes = getattr(stat, 'tx_total_bytes', 'N/A')
    rx_bytes = getattr(stat, 'rx_total_bytes', 'N/A')
    print(f"TEID={teid} | TX={tx_bytes} | RX={rx_bytes}")
```

---

## Optional: Full Field Dump

```python
for attr in dir(stat):
    if not attr.startswith("_"):
        try:
            print(f"{attr}: {getattr(stat, attr)}")
        except Exception as e:
            print(f"{attr}: [Error reading: {e}]")
```

---

## Summary

* `ind.gtp_stats` is a vector of session-level GTP metrics
* Each entry corresponds to one tunnel (TEID)
* Use `getattr()` and `dir()` to safely inspect and access data

---

> Next: Display GTP metrics and timestamps in logs
> 👉 [`03_display_metrics.md`](./03_display_metrics.md)
