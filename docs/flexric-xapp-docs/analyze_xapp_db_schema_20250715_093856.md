# FlexRIC xApp Metrics DB – Schema Reference and Query Guide

This document provides a summary of the key tables and fields stored in the xApp SQLite database (`xapp_db_<timestamp>`) created during runtime. It is intended to help future developers, researchers, or engineers extract and understand network data.

---

## Key Tables Overview

| Table           | Description                                           |
|-----------------|-------------------------------------------------------|
| `MAC_UE`        | MAC-layer UE stats (throughput, PRBs, MCS, CQI, etc.) |
| `PDCP_bearer`   | PDCP-layer bearer stats (Tx/Rx SDUs & PDUs)           |
| `RLC_bearer`    | RLC-layer stats (buffer usage, retransmissions)       |
| `GTP_NGUT`      | GTP-U tunnel information (RNTI, TEID, QFI)            |
| `KPM_LabelInfo` | KPM metric labels and attributes                      |
| `KPM_MeasRecord`| Raw measurement values (associated to labels)         |
| `SLICE`         | Configured RAN slices and algorithm parameters        |
| `UE_SLICE`      | UE ↔ Slice associations (per RNTI and slice ID)       |

---

## 🔍 Example Fields (per table)

### `MAC_UE`
- `rnti`: UE identifier
- `dl_aggr_tbs`, `ul_aggr_tbs`: Aggregated Transport Block Sizes
- `dl_mcs1`, `ul_mcs1`: Modulation & Coding Scheme values
- `pusch_snr`, `pucch_snr`: SNR measurements
- `dl_bler`, `ul_bler`: Block Error Rates

### `PDCP_bearer`
- `txpdu_bytes`, `rxpdu_bytes`: Total PDCP payload
- `rxpdu_oo_pkts`, `rxpdu_dd_pkts`: Out-of-order / duplicate packets
- `rnti`, `rbid`: UE + radio bearer ID

### `RLC_bearer`
- `txpdu_bytes`, `rxpdu_bytes`: Total bytes sent/received
- `txpdu_retx_pkts`: Retransmissions
- `rxpdu_dup_bytes`: Duplicate bytes received

### `GTP_NGUT`
- `teidgnb`, `teidupf`: Tunnel Endpoint IDs for gNB and UPF
- `qfi`: QoS Flow Identifier
- `rnti`: UE identifier

### `SLICE`
- `id`: Slice ID
- `label`: Custom label (e.g., s1, s2)
- `type`: Slice algorithm (STATIC, EDF, NVS)
- `type_param0..2`: Slice-specific parameters (e.g., deadlines, bandwidth)

### `UE_SLICE`
- `rnti`: UE identifier
- `dl_id`: Associated downlink slice ID

---

## Export Commands

```bash
sqlite3 /tmp/xapp_db_<timestamp> -header -csv "SELECT * FROM MAC_UE;" > mac_metrics.csv
sqlite3 /tmp/xapp_db_<timestamp> -header -csv "SELECT * FROM RLC_bearer;" > rlc_metrics.csv
sqlite3 /tmp/xapp_db_<timestamp> -header -csv "SELECT * FROM PDCP_bearer;" > pdcp_metrics.csv
sqlite3 /tmp/xapp_db_<timestamp> -header -csv "SELECT * FROM SLICE;" > slice_config.csv
sqlite3 /tmp/xapp_db_<timestamp> -header -csv "SELECT * FROM UE_SLICE;" > ue_slice.csv
```

---

## Notes

- You can inspect table definitions using `.schema TABLE` inside `sqlite3`.
- Each record includes a `tstamp` and cell ID info (MCC, MNC, gNB ID…).
- Ideal for building data pipelines, dashboards, or anomaly detection.

