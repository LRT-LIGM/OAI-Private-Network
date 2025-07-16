# 06 - GTP Tunnel Metrics Field Reference

This document lists all fields available in the `gtp_ngu_stats_impl_t` structure — used by the GTP Service Model to report session-level tunnel metrics to your xApp.

These fields are accessible in the `gtp_stats` vector inside `swig_gtp_ind_msg_t`.

---

## How to Use in Python

```python
def handle(self, ind):
    for stat in ind.gtp_stats:
        print(stat.teid, stat.tx_total_bytes, stat.rx_total_bytes, ...)
```

> Use `getattr()` to safely access each field.

---

## Field Reference Table

| Field Name       | Type     | Description                                         |
| ---------------- | -------- | --------------------------------------------------- |
| `teid`           | `uint32` | Tunnel Endpoint Identifier — unique per GTP session |
| `tx_total_bytes` | `uint64` | Total number of bytes transmitted via GTP           |
| `rx_total_bytes` | `uint64` | Total number of bytes received via GTP              |
| `tx_total_pkts`  | `uint64` | Total number of packets transmitted                 |
| `rx_total_pkts`  | `uint64` | Total number of packets received                    |
| `tx_drop_bytes`  | `uint64` | Total number of bytes dropped on transmission       |
| `rx_drop_bytes`  | `uint64` | Total number of bytes dropped on reception          |
| `status`         | `uint8`  | Optional session status or flag                     |

---

## Notes

* `teid` is the primary session key — not per UE, but per GTP tunnel
* Drop values may be `0` if the tunnel is healthy or not implemented
* `status` may be used to reflect tunnel state (active/inactive/errored)

---

## Example: Dump All Fields

```python
for stat in ind.gtp_stats:
    for attr in dir(stat):
        if not attr.startswith("_"):
            try:
                print(f"{attr}: {getattr(stat, attr)}")
            except Exception as e:
                print(f"{attr}: [Error reading: {e}]")
```

---

## Summary

* All fields defined here are from `gtp_data_ie.h`
* Always confirm availability via `dir(stat)` at runtime
* Use `teid` to track per-session performance
