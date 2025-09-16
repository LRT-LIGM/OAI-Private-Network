# FlexRIC xApp Metrics – Collected and Extendable Metrics

This document provides an overview of the available metrics collected by the current FlexRIC xApp configuration (via MAC, RLC, PDCP, GTP, and slicing SMs), followed by a list of additional metrics that can be added for more advanced use cases.

---

## Available Metrics (Collected by Current xApp)

### MAC Layer (MAC_UE)
- `rnti`: UE ID
- `dl_aggr_tbs`, `ul_aggr_tbs`: Aggregated Transport Block Size
- `dl_aggr_prb`, `ul_aggr_prb`: Resource block allocation
- `dl_mcs1`, `ul_mcs1`: MCS index values
- `pusch_snr`, `pucch_snr`: Signal-to-Noise Ratio (SNR)
- `phr`, `bsr`: Power Headroom and Buffer Status
- `dl_bler`, `ul_bler`: Block Error Rates
- `dl_num_harq`, `ul_num_harq`: HARQ round counters
- `dl_sched_rb`, `ul_sched_rb`: RB scheduling stats

### RLC Layer (RLC_bearer)
- Packet stats: `txpdu_bytes`, `rxpdu_bytes`, `txpdu_retx_pkts`
- Duplicate and dropped packet counters
- Buffer occupancy and segmentation
- SDU latency estimation (`txsdu_avg_time_to_tx`)

### PDCP Layer (PDCP_bearer)
- Transmit/receive SDUs and PDUs
- Out-of-order packets
- Reordering stats and packet re-delivery metrics

### GTP Layer (GTP_NGUT)
- `teidgnb`, `teidupf`: Tunnel Endpoint IDs
- `qfi`: QoS Flow Identifiers
- `rnti`: UE association

### KPM (KPM_LabelInfo + KPM_MeasRecord)
- QoS class indicators
- Session types (5QI, sST, sD)
- Measurement records and label metadata

### Slicing Layer (SLICE, UE_SLICE)
- Slice IDs, scheduling algorithm (`STATIC`, `NVS`, `EDF`)
- Slice-specific parameters (rate, deadline, priority, etc.)
- UE ↔ Slice associations
- Number of slices, labels, and UE distribution

---

## Extendable / Missing Metrics

### RRC / Control Plane
- RRC connection state (IDLE, CONNECTED, etc.)
- Connection setup and release counters
- Paging messages (sent/dropped)

### Mobility Metrics
- Handover success/failure
- Cell reselection and mobility event logs
- UE mobility state (stationary/mobile)

### UE Location & Topology
- GPS or sector/cell-level mapping (not available by default)
- TA list, Cell Global ID (CGI)

### Radio Bearer-Specific (SRB/DRB)
- Detailed counters for signaling vs data bearers
- Per-RB throughput and delay

### Latency, Jitter, Delay
- End-to-end latency across PDCP and GTP
- UL/DL jitter measurement (time deviation)

### Energy & Power
- UE power consumption estimate
- Power saving mode status (DRX)

### Application-Level Metrics (Custom KPM)
- MOS (Mean Opinion Score) for VoIP
- Video QoE metrics (buffering, stall ratio, bitrate adaptation)

### Host-Level Metrics
- CPU usage per container
- Memory usage per network function (e.g., SMF, UPF)

---

## Summary

The current xApp already captures a rich and layered dataset suitable for:
- Performance monitoring
- RAN slicing evaluation
- UE-level throughput and quality analysis

Advanced metrics can be integrated by:
- Extending existing Service Models
- Adding new SMs to FlexRIC
- Interfacing with external data collectors or OSS probes

