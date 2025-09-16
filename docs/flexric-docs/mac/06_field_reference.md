# 06 - MAC UE Metrics Field Reference

This document lists all accessible fields in `mac_ue_stats_impl_t` — the structure received in the Python callback `handle(self, ind)` via `ind.ue_stats`.

These metrics are defined in the file:

```
~/flexric/src/sm/mac_data_ie.h
```

## How to Use in Python

In your xApp (e.g. `xapp_mac_rlc_pdcp_gtp_moni.py`), access each metric like this:

```python
def handle(self, ind):
    for ue in ind.ue_stats:
        print(ue.rnti, ue.bsr, ue.phr, ue.pusch_snr, ...)
```

---

## Field Reference

| Field Name           | Type       | Description                                   |
| -------------------- | ---------- | --------------------------------------------- |
| `rnti`               | `uint32_t` | UE Radio Network Temporary Identifier         |
| `bsr`                | `uint32_t` | Buffer Status Report (pending bytes at UE)    |
| `phr`                | `int8_t`   | Power Headroom Report                         |
| `frame`              | `uint16_t` | Frame number                                  |
| `slot`               | `uint16_t` | Slot number within the frame                  |
| `wb_cqi`             | `uint8_t`  | Wideband Channel Quality Indicator            |
| `dl_mcs1`, `dl_mcs2` | `uint8_t`  | Downlink MCS values (e.g. PDSCH layers 1 & 2) |
| `ul_mcs1`, `ul_mcs2` | `uint8_t`  | Uplink MCS values                             |

---

### Throughput and SDUs

| Field Name           | Type       | Description                                |
| -------------------- | ---------- | ------------------------------------------ |
| `dl_aggr_tbs`        | `uint64_t` | Total DL Transport Block Size (aggregated) |
| `ul_aggr_tbs`        | `uint64_t` | Total UL TBS (aggregated)                  |
| `dl_curr_tbs`        | `uint64_t` | Current DL TBS (per reporting window)      |
| `ul_curr_tbs`        | `uint64_t` | Current UL TBS                             |
| `dl_aggr_bytes_sdus` | `uint64_t` | DL SDU payload bytes sent                  |
| `ul_aggr_bytes_sdus` | `uint64_t` | UL SDU payload bytes sent                  |
| `dl_aggr_sdus`       | `uint32_t` | Number of DL SDUs                          |
| `ul_aggr_sdus`       | `uint32_t` | Number of UL SDUs                          |

---

### Scheduling and PRB Usage

| Field Name         | Type       | Description                  |
| ------------------ | ---------- | ---------------------------- |
| `dl_sched_rb`      | `uint64_t` | DL Scheduled Resource Blocks |
| `ul_sched_rb`      | `uint64_t` | UL Scheduled Resource Blocks |
| `dl_aggr_prb`      | `uint32_t` | DL PRB usage                 |
| `ul_aggr_prb`      | `uint32_t` | UL PRB usage                 |
| `dl_aggr_retx_prb` | `uint32_t` | DL PRB retransmissions       |
| `ul_aggr_retx_prb` | `uint32_t` | UL PRB retransmissions       |

---

### HARQ

| Field Name    | Type       | Description                      |
| ------------- | ---------- | -------------------------------- |
| `dl_harq[5]`  | `uint32_t` | DL HARQ stats (per process)      |
| `ul_harq[5]`  | `uint32_t` | UL HARQ stats                    |
| `dl_num_harq` | `uint32_t` | Number of DL HARQ processes used |
| `ul_num_harq` | `uint32_t` | Number of UL HARQ processes used |

---

### Quality Indicators

| Field Name  | Type    | Description                 |
| ----------- | ------- | --------------------------- |
| `pusch_snr` | `float` | PUSCH Signal-to-Noise Ratio |
| `pucch_snr` | `float` | PUCCH Signal-to-Noise Ratio |
| `dl_bler`   | `float` | Downlink Block Error Rate   |
| `ul_bler`   | `float` | Uplink Block Error Rate     |

---

## Notes

* All fields are per-UE and sampled at the RIC callback time.
* If a value appears constant or `0`, verify:

  * The UE is active
  * The metric is reported by the gNB
  * FlatBuffers or Plain encoders include the field
