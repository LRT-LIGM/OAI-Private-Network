# Overview: GTP Metrics in FlexRIC

This document provides an overview of how GTP (GPRS Tunneling Protocol) user-plane metrics are collected and reported via FlexRIC. These metrics represent aggregate traffic data per tunnel (TEID) and are useful for analyzing session-level throughput and reliability.

---

## Files Involved in GTP Metric Handling

| File Path                                           | Role                                                       |
|----------------------------------------------------|------------------------------------------------------------|
| `examples/emulator/agent/sm_gtp.c`                 | GTP Service Model plugin — reports `gtp_ind_msg_t`         |
| `examples/xApp/python3/xapp_mac_rlc_pdcp_gtp_moni.py` | Python xApp defining `GTPCallback`                         |
| `examples/xApp/python3/xapp_sdk.py`                | SWIG Python interface exposing `ric.gtp_cb` and types      |
| `examples/xApp/python3/_xapp_sdk.so`               | Compiled SWIG binding used by Python                       |

---

## Callback Mechanism

Here’s how GTP metric reporting works in FlexRIC:

1. The E2 Agent collects GTP statistics and constructs a `gtp_ind_msg_t` message.
2. This message is sent over E2AP to the Near-RT RIC.
3. The SWIG Python SDK exposes it as a `swig_gtp_ind_msg_t`.
4. Your Python xApp defines a class inheriting from `ric.gtp_cb`, where the `handle()` method is called with the indication.
5. Inside `handle()`, access the vector `gtp_stats` (list of `gtp_ngu_stats_impl_t`) for all active TEID sessions.

---

## Technical Stack

- **C Plugin:** `sm_gtp.c`
- **C Struct:** `gtp_ngu_stats_impl_t` in `gtp_data_ie.h`
- **Python Binding:** `xapp_sdk.py`, `_xapp_sdk.so`
- **Python Callback Interface:** `ric.gtp_cb`
- **xApp Script:** `xapp_mac_rlc_pdcp_gtp_moni.py`

---

## What’s in the Metrics?

The received `ind` object (type `swig_gtp_ind_msg_t`) contains:

- `tstamp`: Timestamp of the message (in microseconds)
- `gtp_stats`: Vector of `gtp_ngu_stats_impl_t`, each containing:
  - Transmit/receive byte and packet totals
  - Drop statistics
  - TEID and session status

---

## Summary

You now understand:
- How GTP statistics flow from the E2 Agent to your Python xApp
- Which files and structures are involved
- What kind of metrics you can expect from GTP reporting

> Next: Set up the Python callback to receive GTP stats  
👉 [`01_callback_setup.md`](./01_callback_setup.md)
