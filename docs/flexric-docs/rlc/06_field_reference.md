# 06 - RLC Radio Bearer Metrics Field Reference

This file lists all the known fields in `rlc_rb_stats_impl_t`, which represents one Radio Bearer (RB) entry inside the RLC Indication message (`ind.rb_stats`).

These fields are collected at runtime by the E2 Agent and delivered via the `handle(self, ind)` callback in your xApp.

---

## How to Use in Python

Access values inside the callback like this:

```python
def handle(self, ind):
    for rb in ind.rb_stats:
        print(rb.rnti, rb.tx_bytes, rb.rx_bytes, rb.sn_tx, rb.sn_rx)
```

Always use `getattr()` or `hasattr()` to avoid crashes from missing fields.

---

## Field Reference Table

| Field Name | Type     | Description                                                 |
| ---------- | -------- | ----------------------------------------------------------- |
| `rnti`     | `uint16` | UE identifier (Radio Network Temporary Identifier)          |
| `lcid`     | `uint8`  | Logical Channel ID (optional, may not be reported)          |
| `mode`     | `uint8`  | RLC mode: 1=AM, 2=UM, 3=TM                                  |
| `tx_bytes` | `uint64` | Total number of transmitted bytes on this RB                |
| `rx_bytes` | `uint64` | Total number of received bytes on this RB                   |
| `sn_tx`    | `uint32` | Last transmitted Sequence Number (for AM/UM modes)          |
| `sn_rx`    | `uint32` | Last received Sequence Number (for AM/UM modes)             |
| `tx_sdu`   | `uint32` | Number of SDUs transmitted (optional)                       |
| `rx_sdu`   | `uint32` | Number of SDUs received (optional)                          |
| `tx_pdu`   | `uint32` | Number of PDUs transmitted (optional)                       |
| `rx_pdu`   | `uint32` | Number of PDUs received (optional)                          |
| `tx_retx`  | `uint32` | Number of retransmissions (only for AM mode, if enabled)    |
| `status`   | `uint8`  | Optional status or flags (depends on plugin implementation) |

> These fields may vary depending on your FlexRIC build and RLC SM configuration.

---

## Notes

* If a field is not present in your build, accessing it will throw `AttributeError`
* You can use `dir(ind.rb_stats[0])` to inspect which fields are supported at runtime
* Some fields (like `tx_sdu`, `rx_sdu`, `tx_retx`) may need to be enabled explicitly in the C code

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

* This structure provides detailed RLC-level metrics per Radio Bearer
* Always write safe, dynamic code to adapt to your environment
* Logging these fields helps you analyze UE performance, retransmissions, and reliability