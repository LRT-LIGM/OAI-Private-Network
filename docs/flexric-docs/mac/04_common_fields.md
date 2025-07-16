# Common Fields in `mac_ue_stats_impl_t`

This section documents the most commonly used fields exposed in each UE entry (`mac_ue_stats_impl_t`) inside the `ue_stats` vector.

These fields may vary depending on your version of FlexRIC or how the MAC SM plugin is built, so use `dir(ue)` to confirm which ones are available in your environment.

---

## Field Reference Table

| Field Name      | Type     | Description                                                   |
|------------------|----------|---------------------------------------------------------------|
| `rnti`           | `uint16` | Radio Network Temporary Identifier – unique ID per UE         |
| `dl_mcs`         | `uint8`  | Downlink Modulation and Coding Scheme index                   |
| `ul_mcs`         | `uint8`  | Uplink Modulation and Coding Scheme index                     |
| `bsr`            | `uint8`  | Buffer Status Report value                                    |
| `phr`            | `int8`   | Power Headroom Report                                         |
| `harq_tx`        | `uint8`  | HARQ TX status or count                                       |
| `harq_rx`        | `uint8`  | HARQ RX status or count                                       |
| `dl_cqi`         | `uint8`  | Downlink Channel Quality Indicator (CQI)                      |
| `ul_cqi`         | `uint8`  | Uplink CQI (if implemented)                                   |
| `timing_advance` | `uint16` | Timing Advance (used for scheduling alignment)                |
| `pucch_snr`      | `float`  | Signal-to-noise ratio on PUCCH (if available)                 |
| `pdsch_bler`     | `float`  | Downlink block error rate                                     |
| `pusch_bler`     | `float`  | Uplink block error rate                                       |
| `dl_retx`        | `uint8`  | Number of DL retransmissions (HARQ)                           |
| `ul_retx`        | `uint8`  | Number of UL retransmissions (HARQ)                           |

---

## Notes

- Some fields may not be implemented in your FlexRIC MAC plugin build.
- If you access a field that doesn't exist, it will throw an exception — always use `getattr()` or `hasattr()` to verify.
- Use `dir(ind.ue_stats[0])` to dynamically discover available attributes at runtime.

---

## Example: Logging Select Fields

```python
fields = ['rnti', 'dl_mcs', 'ul_mcs', 'bsr', 'phr', 'harq_tx', 'harq_rx']

for i in range(len(ind.ue_stats)):
    ue = ind.ue_stats[i]
    print(f"\n--- UE #{i} ---")
    for f in fields:
        value = getattr(ue, f, 'N/A')
        print(f"{f}: {value}")
```

---

## Recommended Strategy

* Build your own subset of "important" fields based on your use case (e.g. HARQ for retransmission analysis, BSR for buffer trends).
* Skip or log unknown fields as `"N/A"` to keep output clean and crash-free.

---

> Next: How to debug SWIG-related errors and avoid app crashes
👉 [`05_debugging.md`](./05_debugging.md)
