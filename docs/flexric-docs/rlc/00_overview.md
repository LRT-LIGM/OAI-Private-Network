# Overview: RLC Metrics in FlexRIC

This document explains how RLC (Radio Link Control) layer metrics are handled and accessed using FlexRIC's Python bindings via SWIG. These metrics are periodically sent from the E2 Agent to the Near-RT RIC and processed via a callback in the xApp.

---

## Files Involved in RLC Metric Handling

| File Path                                           | Role                                                         |
|----------------------------------------------------|--------------------------------------------------------------|
| `examples/emulator/agent/sm_rlc.c`                 | Generates RLC metrics and sends `rlc_ind_msg_t`              |
| `examples/xApp/python3/xapp_mac_rlc_pdcp_gtp_moni.py` | Python xApp that defines `RLCCallback`                       |
| `examples/xApp/python3/xapp_sdk.py`                | SWIG interface exposing `ric.rlc_cb`, `swig_rlc_ind_msg_t`, etc. |
| `examples/xApp/python3/_xapp_sdk.so`               | Compiled SWIG shared object loaded by Python                 |

---

## Callback Mechanism

The RLC metric reporting follows this pipeline:

1. The E2 Agent collects RLC statistics and forms a `rlc_ind_msg_t` message.
2. This message is sent to the Near-RT RIC via E2AP.
3. The SWIG-generated Python bindings receive the message as a `swig_rlc_ind_msg_t` object.
4. Your xApp class (inheriting from `ric.rlc_cb`) receives the message via the `handle()` method.
5. The RLC metrics are then logged, analyzed, or stored by your Python code.

---

## Technical Stack

- **C Service Model:** `sm_rlc.c`
- **SWIG Bindings:** `xapp_sdk.py`, `_xapp_sdk.so`
- **Python Interface:** `ric.rlc_cb` and `swig_rlc_ind_msg_t`
- **Main Script:** `xapp_mac_rlc_pdcp_gtp_moni.py`

---

## What’s in the Metrics?

The `ind` object received by `handle(self, ind)` is of type `swig_rlc_ind_msg_t`.

It contains:
- `tstamp`: Timestamp (μs) of when the metric was generated
- `rb_stats`: A list of per-UE, per-RB statistics (e.g., bytes sent/received, sequence numbers, etc.)

Each element of `rb_stats` is of type `rlc_rb_stats_impl_t`.

---

## Summary

You now understand:
- Which files are involved in RLC metric generation and handling
- How the callback mechanism works between the Agent, RIC, and your xApp
- What kind of data is exposed by the RLC metrics interface

> Next: Set up your own RLC callback  
👉 [`01_callback_setup.md`](./01_callback_setup.md)
