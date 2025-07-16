# Accessing UE Stats from MAC Indication

Each time the MAC callback is triggered, your `handle()` method receives a parameter `ind`, which is of type `swig_mac_ind_msg_t`.

This object contains a key field:

```python
ind.ue_stats
```

This is a SWIG-wrapped `std::vector<mac_ue_stats_impl_t>`, containing one entry per connected UE (User Equipment).

---

## Looping Over `ue_stats`

You can iterate over this vector like a regular Python list:

```python
def handle(self, ind):
    try:
        num_ues = len(ind.ue_stats)
        print(f"📦 Number of UEs in indication: {num_ues}")

        for i in range(num_ues):
            ue = ind.ue_stats[i]
            print(f"UE #{i} object:", ue)

    except Exception as e:
        print("❌ Error accessing UE stats:", e)
```

---

## Exploring Available Fields

To understand what metrics are exposed, use `dir()` on the first UE:

```python
ue = ind.ue_stats[0]
print("Available fields:", dir(ue))
```

This will show you all exposed methods and attributes for the `mac_ue_stats_impl_t` object.

---

## Recommended Pattern

Accessing values safely ensures your app won't crash from missing fields:

```python
for i in range(len(ind.ue_stats)):
    ue = ind.ue_stats[i]

    try:
        rnti = getattr(ue, 'rnti', None)
        dl_mcs = getattr(ue, 'dl_mcs', None)
        ul_mcs = getattr(ue, 'ul_mcs', None)

        print(f"UE[{i}] RNTI: {rnti}, DL MCS: {dl_mcs}, UL MCS: {ul_mcs}")

    except Exception as ue_err:
        print(f"⚠️ Error reading UE[{i}]:", ue_err)
```

---

## Clean Field Dump (Optional)

To print all accessible values without knowing the field names in advance:

```python
for attr in dir(ue):
    if not attr.startswith("_"):
        try:
            print(f"{attr}: {getattr(ue, attr)}")
        except Exception as e:
            print(f"{attr}: [Error reading: {e}]")
```

This is especially useful for reverse-engineering undocumented structures.

---

## Summary

* `ind.ue_stats` is a vector of UE metrics
* Loop through it with `len()` and indexing (`ind.ue_stats[i]`)
* Use `getattr()` and `dir()` to explore safely
* Always use `try/except` to avoid crashing due to unexpected attribute errors

---

> Next: Display metrics and timestamps
 [`03_display_metrics.md`](./03_display_metrics.md)
