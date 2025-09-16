# Python xApps for FlexRIC – Monitoring and Control

## Objective

This document provides details about the Python-based xApps located in `flexric/examples/xApp/python3/`. These applications allow users to subscribe to RAN metrics and send slicing control messages via the E2 interface using FlexRIC.

---

## 1. xapp_mac_rlc_pdcp_gtp_moni.py – Metrics Monitoring

### Purpose

This xApp subscribes to four types of Service Models:
- **MAC** (Medium Access Control)
- **RLC** (Radio Link Control)
- **PDCP** (Packet Data Convergence Protocol)
- **GTP** (GPRS Tunneling Protocol)

It measures the latency of each indication message received and prints it in microseconds.

### How It Works

- Connects to all available E2 nodes using `ric.conn_e2_nodes()`
- Defines a callback class for each protocol (e.g., `MACCallback`)
- Each callback prints:
  ```
  <PROTOCOL> Indication tstamp = <timestamp> latency = <latency> μs
  ```

### Execution

```bash
python3 xapp_mac_rlc_pdcp_gtp_moni.py
```

### Output

Metrics are printed to stdout. This script is useful for performance evaluation and latency tracking.

---

## 2. xapp_slice_moni_ctrl.py – Slice Monitoring & Control

### Purpose

This xApp both:
- Monitors RAN and UE slice configurations
- Sends control messages to add, associate, delete, and reset slices dynamically

### Features

- **Monitors slices** and saves stats to `rt_slice_stats.json`
- **Controls slicing** for various algorithms:
  - `STATIC`: Fixed positions
  - `NVS`: Rate or capacity based
  - `EDF`: Deadline-based

### Execution

```bash
python3 xapp_slice_moni_ctrl.py
```

### Process

1. Reports slice stats every 5ms using `report_slice_sm`
2. Sends control messages using:
   - `fill_slice_ctrl_msg("ADDMOD", ...)`
   - `fill_slice_ctrl_msg("ASSOC_UE_SLICE", ...)`
   - `fill_slice_ctrl_msg("DEL", ...)`
   - `fill_slice_ctrl_msg("ADDMOD", reset_slices)`

### Output

- File `rt_slice_stats.json` contains the full state of RAN/UE slices in JSON
- Terminal logs show success/failure of control operations

---

## 3. watch_slice_stats – Realtime Utility (Optional)

A simple script to observe slice statistics, likely used to watch the contents of `rt_slice_stats.json`. Not essential but useful for quick JSON data inspection.

---

## 4. Additional Notes

- All Python xApps require the `xapp_sdk` Python bindings (SWIG wrapped)
- FlexRIC must be running (`nearRT-RIC`) before launching any xApp
- The xApps work independently and can be adapted for logging, visualization, or automation

---

## Recommendation

Keep all Python xApps documented together unless one grows into a major standalone tool. This structure is good for initial handoff and onboarding.

