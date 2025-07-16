# Common Fields in `rlc_rb_stats_impl_t`

This section documents the commonly available fields exposed in each Radio Bearer (RB) entry from the RLC Indication message (`ind.rb_stats`).

These fields may vary depending on your FlexRIC version or how the RLC Service Model was compiled. Always use `dir(rb)` to verify field availability at runtime.

---

## Field Reference Table

| Field Name | Type     | Description                                      |
|------------|----------|--------------------------------------------------|
| `rnti`     | `uint16` | Radio Network Temporary Identifier (UE-level ID) |
| `mode`     | `uint8`  | RLC Mode: 1=AM, 2=UM, etc.                        |
| `tx_bytes` | `uint64` | Number of transmitted bytes                      |
| `rx_bytes` | `uint64` | Number of received bytes                         |
| `sn_tx`    | `uint32` | Last transmitted sequence number                 |
| `sn_rx`    | `uint32` | Last received sequence number                    |
| `lcid`     | `uint8`  | Logical Channel ID (optional depending on config)|

> Note: Field names and types are inferred from common FlexRIC builds. Use `print(dir(rb))` to confirm in your setup.

---

## Accessing These Fields in Python

To safely access fields, use `getattr()`:

```python
for rb in ind.rb_stats:
    rnti = getattr(rb, 'rnti', 'N/A')
    tx = getattr(rb, 'tx_bytes', 0)
    rx = getattr(rb, 'rx_bytes', 0)
    print(f"RNTI: {rnti}, TX: {tx}, RX: {rx}")
```

---

## Example: Logging Select Fields

```python
fields = ['rnti', 'mode', 'tx_bytes', 'rx_bytes', 'sn_tx', 'sn_rx']

for i, rb in enumerate(ind.rb_stats):
    print(f"\n--- RB #{i} ---")
    for f in fields:
        val = getattr(rb, f, 'N/A')
        print(f"{f}: {val}")
```

---

## Recommended Strategy

* Build a subset of important fields for your use case
* Gracefully skip missing fields with `"N/A"` fallback
* Confirm which fields are active via runtime checks (`dir()`)

---

> Next: Debugging your callback and avoiding crashes
> 👉 [`05_debugging.md`](./05_debugging.md)
