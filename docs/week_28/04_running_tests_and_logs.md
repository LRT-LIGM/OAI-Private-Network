# Running Tests & Log Analysis – FlexRIC + xApps

This section describes how we validated the setup by launching the RIC, xApps, and inspecting the resulting logs and metrics.

---

## 1. Running the Near-RT RIC

```bash
./build/examples/ric/nearRT-RIC
```

### Expected Output
- RIC starts on port `36421`
- Receives `E2 SETUP-REQUEST` from gNB
- Accepts all RAN Function IDs (MAC, PDCP, RLC, KPM, etc)

```
[E2AP]: E2 SETUP-REQUEST rx from PLMN 1.1 Node ID 3584
[NEAR-RIC]: Accepting RAN function ID 2 with def = ORAN-E2SM-KPM
...
```


---

## 2. Running the xApp Monitor

```bash
./build/examples/xApp/c/monitor/xapp_gtp_mac_rlc_pdcp_moni -p /usr/local/lib/flexric/ -c /usr/local/etc/flexric/flexric.conf
```

### Expected Output
- Loads shared objects (libmac_sm.so, libgtp_sm.so, etc.)
- Creates runtime database under `/tmp/xapp_db_*.db`
- Subscribes to RAN functions:
```
Successfully subscribed to RAN_FUNC_ID 142  # MAC
Successfully subscribed to RAN_FUNC_ID 143  # RLC
...
```
- Prints periodic latency logs:
```
MAC ind_msg latency = 47 μs
GTP ind_msg latency = 39 μs
...
```

### Runtime Error (fixed)
If the following error occurs:
```
[xApp][SQLite] ERROR: CHECK constraint failed: phr > -24 AND phr < 41
```
This was caused by invalid data insertion (see Fixes doc).

---

## 3. Verifying Collected Metrics

### Access SQLite database:
```bash
sqlite3 /tmp/xapp_db_*.db
.tables
```

### Example queries:
```sql
SELECT * FROM MAC_UE LIMIT 5;
SELECT * FROM PDCP_bearer LIMIT 5;
SELECT * FROM GTP_NGUT LIMIT 5;
```

### Output:
Shows detailed metrics for `rnti`, `dl_aggr_prb`, `txpdu_bytes`, etc. Example:
```
1752065457932655|2|1|1|2|3584|(null)|48|0|5507|47352|...|20.5|22.0|43150|841|...
```

---

## 4. Proper Shutdown

When the test completes successfully, logs end with:
```
[xApp]: Successfully stopped
Test xApp run SUCCESSFULLY
```

---
