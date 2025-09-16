# Common Fields in `pdcp_rb_stats_impl_t`

This section lists the most commonly available fields inside each Radio Bearer (RB) entry within a PDCP Indication (`ind.rb_stats`).

Each field represents packet statistics collected per bearer per UE. Use this reference to select the most relevant metrics for your application.

---

## Field Reference Table

| Field Name               | Type      | Description                                                   |
|--------------------------|-----------|---------------------------------------------------------------|
| `rnti`                   | `uint16`  | Radio Network Temporary Identifier (per UE)                   |
| `lcid`                   | `uint8`   | Logical Channel ID                                            |
| `txpdu_pkts`             | `uint64`  | Number of transmitted PDCP packets                            |
| `txpdu_bytes`            | `uint64`  | Number of transmitted PDCP bytes                              |
| `txpdu_sn`               | `uint64`  | Latest transmitted PDCP Sequence Number                       |
| `txpdu_wt`               | `uint64`  | Transmission window threshold                                 |
| `txpdu_bytes_discarded`  | `uint64`  | Bytes discarded before transmission (buffer overflow, etc.)   |
| `txpdu_pkts_discarded`   | `uint64`  | PDUs discarded before transmission                            |
| `txpdu_retx_pkts`        | `uint64`  | Retransmitted PDCP packets                                    |
| `txpdu_retx_bytes`       | `uint64`  | Retransmitted PDCP bytes                                      |
| `rxpdu_pkts`             | `uint64`  | Received PDCP packets                                         |
| `rxpdu_bytes`            | `uint64`  | Received PDCP bytes                                           |
| `rxpdu_dup_pkts`         | `uint64`  | Duplicate PDCP packets received                               |
| `rxpdu_dup_bytes`        | `uint64`  | Duplicate PDCP bytes                                          |
| `rxpdu_ooo_pkts`         | `uint64`  | Out-of-order packets received                                 |
| `rxpdu_ooo_bytes`        | `uint64`  | Out-of-order bytes                                            |
| `rxpdu_drop_pkts`        | `uint64`  | Dropped packets (due to errors or buffer issues)              |
| `rxpdu_drop_bytes`       | `uint64`  | Dropped bytes                                                 |
| `rxpdu_wt`               | `uint64`  | Reordering window threshold                                   |
| `rxpdu_sn`               | `uint64`  | Latest received PDCP Sequence Number                          |
| `rxpdu_valid_pkts`       | `uint64`  | Successfully validated PDUs                                   |
| `rxpdu_valid_bytes`      | `uint64`  | Successfully validated bytes                                  |
| `status`                 | `uint8`   | Optional status flags                                         |

---

## Example Logging (Python)

```python
fields = ['rnti', 'lcid', 'txpdu_bytes', 'rxpdu_bytes', 'txpdu_retx_pkts', 'rxpdu_dup_pkts']

for i, rb in enumerate(ind.rb_stats):
    print(f"\n--- PDCP RB #{i} ---")
    for field in fields:
        value = getattr(rb, field, 'N/A')
        print(f"{field}: {value}")
```

---

## Notes

* Field availability may depend on your FlexRIC version or plugin compilation
* Always confirm with `dir(ind.rb_stats[0])` or `getattr()` to avoid crashes
* Use subset-based logging for clarity and performance

---

> Next: How to debug your callback and prevent crashes
> 👉 [`05_debugging.md`](./05_debugging.md)
