# Common Fields in `gtp_ngu_stats_impl_t`

This section describes the most frequently used fields available in each GTP tunnel stat entry (`gtp_ngu_stats_impl_t`) provided in `ind.gtp_stats`.

These fields represent session-level GTP-U metrics for each active TEID (Tunnel Endpoint Identifier).

---

## Field Reference Table

| Field Name        | Type      | Description                                          |
|-------------------|-----------|------------------------------------------------------|
| `teid`            | `uint32`  | Tunnel Endpoint Identifier (per GTP session)         |
| `tx_total_bytes`  | `uint64`  | Total transmitted bytes on the GTP tunnel            |
| `rx_total_bytes`  | `uint64`  | Total received bytes on the GTP tunnel               |
| `tx_total_pkts`   | `uint64`  | Total transmitted packets                            |
| `rx_total_pkts`   | `uint64`  | Total received packets                               |
| `tx_drop_bytes`   | `uint64`  | Dropped bytes on transmission (e.g., buffer issues)  |
| `rx_drop_bytes`   | `uint64`  | Dropped bytes on reception                           |
| `status`          | `uint8`   | Optional tunnel status flag (e.g., active/inactive)  |

---

## Safe Logging Example

```python
fields = ['teid', 'tx_total_bytes', 'rx_total_bytes', 'tx_total_pkts', 'rx_total_pkts']

for stat in ind.gtp_stats:
    print("\n--- GTP TEID Stats ---")
    for field in fields:
        val = getattr(stat, field, 'N/A')
        print(f"{field}: {val}")
```

---

## Notes

* `teid` is unique per tunnel — not per UE
* Drop metrics (`tx_drop_bytes`, `rx_drop_bytes`) may be 0 if not implemented or no loss occurred
* `status` is optional and may represent availability or health of the tunnel

---

## Recommended Strategy

* Track `tx_total_bytes` and `rx_total_bytes` for throughput analysis
* Monitor `tx_drop_bytes` / `rx_drop_bytes` for loss detection
* Use `teid` as the primary key for indexing tunnel sessions

---

> Next: Debugging GTP callback behavior and avoiding crashes
> 👉 [`05_debugging.md`](./05_debugging.md)
