> **⚠️ Important Note**  
> This file contains useful information.

# Metrics Analysis – FlexRIC + OAI 5G SA

This document explains how we interpreted and validated metrics extracted from the FlexRIC xApp runtime database (`/tmp/xapp_db_*.db`).

---

## 1. Accessing the Runtime DB

Each time the xApp is launched, it generates a new SQLite file (e.g. `/tmp/xapp_db_1752065455917967`).  
We used the following command to explore the contents:

```bash
sqlite3 /tmp/xapp_db_*.db
```

Useful commands inside the prompt:

```sql
.tables
PRAGMA table_info(MAC_UE);
SELECT * FROM MAC_UE LIMIT 5;
```

---

## 2. Key Tables and Fields

| Table         | Key Metrics Observed                                              |
| ------------- | ----------------------------------------------------------------- |
| `MAC_UE`      | `rnti`, `dl_aggr_prb`, `ul_aggr_prb`, `dl_bler`, `ul_bler`, `phr` |
| `PDCP_bearer` | `txpdu_bytes`, `rxpdu_bytes`, `txsdu_bytes`, `rxsdu_bytes`        |
| `GTP_NGUT`    | `teid`, `qfi`, and associated timestamps                          |
| `RLC_bearer`  | Not deeply analyzed, but accessible                               |

Sample query:

```sql
SELECT tstamp, rnti, dl_aggr_prb, ul_aggr_prb, dl_bler, ul_bler
FROM MAC_UE
ORDER BY tstamp DESC
LIMIT 10;
```

---

## 3. Observed Results

We validated successful real-time metric collection from a real UE (Quectel CM):

* **MAC Layer:** aggregate PRB allocation was tracked every \~millisecond.
* **PDCP Layer:** SDU/PDU throughput and usage visible.
* **GTP:** consistent timestamps and QFI values.

---

## 4. Edge Case: PHR Constraint Failure

One run failed with:

```
[xApp][SQLite] ERROR: CHECK constraint failed: phr > -24 AND  phr < 41
```

Despite `phr` being `20.5`, the issue may come from rare rounding or null values.
We eventually disabled the constraint in schema creation.

---

## 5. Exporting Data

Metrics can be exported in CSV using:

```bash
sqlite3 /tmp/xapp_db_*.db ".headers on" ".mode csv" \
"SELECT * FROM MAC_UE ORDER BY tstamp DESC LIMIT 10;" > mac_metrics.csv
```

---

## ✅ Summary

FlexRIC integration with a live gNodeB and real UE allows us to track and analyze low-layer metrics such as PRB usage, throughput, and latency.
The setup is validated and ready for further experimentation or visual dashboards.
