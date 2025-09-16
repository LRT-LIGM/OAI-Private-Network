# 06 - PDCP Radio Bearer Metrics Field Reference

This document lists all fields available in `pdcp_rb_stats_impl_t`, the structure used to report PDCP statistics via `ind.rb_stats` in your xApp.

These metrics are exposed from the E2 Agent through the `pdcp_data_ie.h` definition and delivered to your Python callback via `swig_pdcp_ind_msg_t`.

---

## How to Access in Python

In your PDCP callback:

```python
def handle(self, ind):
    for rb in ind.rb_stats:
        print(rb.rnti, rb.txpdu_bytes, rb.rxpdu_bytes, ...)
```

Use `getattr()` for safe access, especially across different FlexRIC builds.

---

## Full Field Reference

| Field Name | Type     | Description        |
| ---------- | -------- | ------------------ |
| `rnti`     | `uint16` | UE identifier      |
| `lcid`     | `uint8`  | Logical Channel ID |

#### Transmit (TX)

| Field Name              | Type     | Description               |
| ----------------------- | -------- | ------------------------- |
| `txpdu_pkts`            | `uint64` | PDCP PDUs transmitted     |
| `txpdu_bytes`           | `uint64` | Total TX bytes            |
| `txpdu_sn`              | `uint64` | Latest TX sequence number |
| `txpdu_wt`              | `uint64` | TX window threshold       |
| `txpdu_bytes_discarded` | `uint64` | Bytes discarded before TX |
| `txpdu_pkts_discarded`  | `uint64` | PDUs discarded before TX  |
| `txpdu_retx_pkts`       | `uint64` | Retransmitted PDUs        |
| `txpdu_retx_bytes`      | `uint64` | Retransmitted bytes       |

#### Receive (RX)

| Field Name          | Type     | Description                                   |
| ------------------- | -------- | --------------------------------------------- |
| `rxpdu_pkts`        | `uint64` | PDCP PDUs received                            |
| `rxpdu_bytes`       | `uint64` | Total RX bytes                                |
| `rxpdu_dup_pkts`    | `uint64` | Duplicate PDUs received                       |
| `rxpdu_dup_bytes`   | `uint64` | Duplicate bytes received                      |
| `rxpdu_ooo_pkts`    | `uint64` | Out-of-order PDUs received                    |
| `rxpdu_ooo_bytes`   | `uint64` | Out-of-order bytes                            |
| `rxpdu_drop_pkts`   | `uint64` | Dropped PDUs (buffer errors, integrity, etc.) |
| `rxpdu_drop_bytes`  | `uint64` | Dropped bytes                                 |
| `rxpdu_wt`          | `uint64` | Reordering window threshold                   |
| `rxpdu_sn`          | `uint64` | Last received sequence number                 |
| `rxpdu_valid_pkts`  | `uint64` | Validated PDUs                                |
| `rxpdu_valid_bytes` | `uint64` | Validated bytes                               |

#### Misc

| Field Name | Type    | Description                   |
| ---------- | ------- | ----------------------------- |
| `status`   | `uint8` | Optional status flags or mode |

---

## Notes

* Field names and types were validated against `pdcp_data_ie.h`
* Some fields may report `0` if not implemented or if no activity occurred
* Always verify availability at runtime with `dir(rb)` or `hasattr()`

---

## Example: Print All Fields Safely

```python
for rb in ind.rb_stats:
    for attr in dir(rb):
        if not attr.startswith("_"):
            try:
                print(f"{attr}: {getattr(rb, attr)}")
            except Exception as e:
                print(f"{attr}: [Error reading: {e}]")
```

---

## Summary

* PDCP metrics give fine-grained insight into bearer performance
* Metrics include transmission, reception, duplicate detection, discards, and sequence tracking
* Defensive access is essential for safe operation across versions