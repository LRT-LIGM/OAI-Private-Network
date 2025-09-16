# Overview: PDCP Metrics in FlexRIC

This document explains how PDCP (Packet Data Convergence Protocol) layer metrics are collected, transported, and handled within a FlexRIC-based xApp using Python and SWIG.

PDCP metrics are useful for analyzing packet behavior such as retransmissions, duplicate handling, out-of-order delivery, and overall data integrity at the protocol layer just above RLC.

---

## Files Involved in PDCP Metric Handling

| File Path                                           | Role                                                        |
|----------------------------------------------------|-------------------------------------------------------------|
| `examples/emulator/agent/sm_pdcp.c`                | Implements PDCP SM plugin and generates `pdcp_ind_msg_t`    |
| `examples/xApp/python3/xapp_mac_rlc_pdcp_gtp_moni.py` | Python xApp that defines `PDCPCallback`                     |
| `examples/xApp/python3/xapp_sdk.py`                | SWIG interface exposing `ric.pdcp_cb`, `swig_pdcp_ind_msg_t`, etc. |
| `examples/xApp/python3/_xapp_sdk.so`               | Compiled SWIG shared object                                 |

---

## Callback Mechanism

The reporting pipeline for PDCP metrics is as follows:

1. The E2 Agent sends a `pdcp_ind_msg_t` containing PDCP metrics.
2. The message is passed to the RIC via E2AP.
3. Python bindings (SWIG) expose it as `swig_pdcp_ind_msg_t`.
4. Your xApp receives the message via the `handle(self, ind)` method in a class derived from `ric.pdcp_cb`.
5. The `rb_stats` field in `ind` provides per-bearer metrics.

---

## Technical Stack

- **C Service Model:** `sm_pdcp.c`
- **PDCP Metric Struct:** `pdcp_rb_stats_impl_t` in `pdcp_data_ie.h`
- **SWIG Binding:** `xapp_sdk.py`, `_xapp_sdk.so`
- **Python Callback Interface:** `ric.pdcp_cb`
- **Python xApp Script:** `xapp_mac_rlc_pdcp_gtp_moni.py`

---

## What’s in the Metrics?

The object received in `handle(self, ind)` is a `swig_pdcp_ind_msg_t` containing:

- `tstamp`: Timestamp of the metrics (in microseconds)
- `rb_stats`: Vector of `pdcp_rb_stats_impl_t` entries, one per Radio Bearer

Each `rb_stats` entry provides metrics like:
- Sent/received packet and byte counts
- Retransmission and discard statistics
- Duplicate, out-of-order, and dropped packet info
- Sequence numbers and windows

---

## Summary

You now understand:
- Which components are responsible for PDCP metric generation and reporting
- How the callback mechanism delivers metrics to your Python xApp
- What kind of data the PDCP metrics contain

> Next: Set up your own callback class  
👉 [`01_callback_setup.md`](./01_callback_setup.md)
