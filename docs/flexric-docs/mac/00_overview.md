
---

## Files Involved in MAC Metric Handling

| File Path | Role |
|-----------|------|
| `examples/emulator/agent/sm_mac.c` | Generates MAC metrics in C and pushes them as `mac_ind_msg_t` |
| `examples/xApp/python3/xapp_mac_rlc_pdcp_gtp_moni.py` | Main Python xApp that receives and logs metrics |
| `examples/xApp/python3/xapp_sdk.py` | SWIG wrapper exposing `ric.mac_cb`, `mac_ue_stats_impl_t`, etc. |
| `examples/xApp/python3/_xapp_sdk.so` | Compiled SWIG shared object loaded by Python |
| `examples/ric/near_ric.c` | Starts the RIC and registers service models |
| `examples/xApp/c/monitor/xapp_gtp_mac_rlc_pdcp_moni.c` | C version of the same monitor (optional reference) |

---

## Callback Mechanism

### Step-by-step:

1. The E2 Agent (C) calls into the MAC SM and emits `mac_ind_msg_t`.
2. This is sent to the RIC using E2AP.
3. The FlexRIC Python SDK receives the message via SWIG and passes it to the `handle()` method inside your Python class (which extends `ric.mac_cb`).
4. Your Python logic in `xapp_mac_rlc_pdcp_gtp_moni.py` processes `ind.ue_stats`, logs the metrics.

---

## Technical Stack

- C Service Model implementation: `sm_mac.c`
- SWIG interface (Python wrapper): `xapp_sdk.py`, `_xapp_sdk.so`
- Python callback interface: `ric.mac_cb`
- Python xApp handler: `MACCallback.handle()`

This allows near real-time extraction of MAC layer metrics in Python without modifying the C source.

---

## What’s in the Metrics?

The `ind` object (type `swig_mac_ind_msg_t`) contains:
- `tstamp`: timestamp of the measurement
- `ue_stats`: vector of `mac_ue_stats_impl_t` containing per-UE stats

These are printed and analyzed in the next sections.

---

## Summary

You now understand:
- What MAC metrics are and how they are used
- Which files are responsible for generating, transporting, and displaying them
- How your Python callback gets called and from where
- The key roles of the FlexRIC agent, RIC, and SWIG bindings

## Next: Set up your own callback class  
> [`01_callback_setup.md`](./01_callback_setup.md)
