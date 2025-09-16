# Displaying MAC Metrics in Terminal Logs

Once you have access to UE metrics via `ind.ue_stats`, the next step is to log them clearly in your terminal for monitoring, debugging, or analysis.

This section walks through:
- Formatting log output for each UE
- Calculating latency using the `tstamp` field
- Handling missing or malformed data safely

---

## Logging Basic Metrics

Here’s how to iterate through the UEs and print some key fields:

```python
def handle(self, ind):
    try:
        print(f"📡 MAC Indication received with {len(ind.ue_stats)} UEs")

        for i in range(len(ind.ue_stats)):
            ue = ind.ue_stats[i]

            rnti = getattr(ue, 'rnti', 'N/A')
            bsr = getattr(ue, 'bsr', 'N/A')
            dl_mcs = getattr(ue, 'dl_mcs', 'N/A')
            ul_mcs = getattr(ue, 'ul_mcs', 'N/A')

            print(f"🔸 UE[{i}] RNTI={rnti} | BSR={bsr} | DL_MCS={dl_mcs} | UL_MCS={ul_mcs}")

    except Exception as e:
        print(f"❌ Error during UE metrics logging: {e}")
```

---

## Adding Timestamp & Latency

The `ind` object often includes a timestamp (`tstamp`) in microseconds. You can calculate the delay like this:

```python
if hasattr(ind, "tstamp"):
    t_now = time.time_ns() / 1000.0  # Current time in μs
    t_mac = ind.tstamp / 1.0         # Already in μs
    latency = t_now - t_mac

    print(f"🕒 Timestamp = {t_mac:.0f} μs | Latency = {latency:.2f} μs")
else:
    print("⚠️ No 'tstamp' found in MAC indication")
```

This helps track real-time delay between MAC layer event generation and processing.

---

## Clean Terminal Output (Example)

```text
 MAC Indication received with 2 UEs

🔸 UE[0] RNTI=4123 | BSR=80 | DL_MCS=15 | UL_MCS=10
🔸 UE[1] RNTI=4378 | BSR=22 | DL_MCS=18 | UL_MCS=12

 Timestamp = 1721064235794320 μs | Latency = 304.19 μs
```

---

## Pro Tip: Use Formatting for Readability

You can align output using f-strings:

```python
print(f"UE[{i}] RNTI={rnti:<6} | BSR={bsr:<3} | DL_MCS={dl_mcs:<2} | UL_MCS={ul_mcs:<2}")
```

---

## Summary

* Format logs clearly to make metric monitoring easier
* Use `tstamp` for latency analysis
* Always wrap output logic in `try/except` blocks
* Explore optional fields based on `dir(ue)` output

---

### Full Example: Display All MAC Metrics (Python)

```python
class MACCallback(ric.mac_cb):
    def __init__(self):
        ric.mac_cb.__init__(self)

    def handle(self, ind):
        try:
            print(f"📡 MAC Indication received with {len(ind.ue_stats)} UEs")

            for i, ue in enumerate(ind.ue_stats):
                rnti = getattr(ue, 'rnti', 'N/A')
                phr = getattr(ue, 'phr', 'N/A')
                bsr = getattr(ue, 'bsr', 'N/A')
                wb_cqi = getattr(ue, 'wb_cqi', 'N/A')

                dl_mcs1 = getattr(ue, 'dl_mcs1', 'N/A')
                dl_mcs2 = getattr(ue, 'dl_mcs2', 'N/A')
                ul_mcs1 = getattr(ue, 'ul_mcs1', 'N/A')
                ul_mcs2 = getattr(ue, 'ul_mcs2', 'N/A')

                dl_aggr_tbs = getattr(ue, 'dl_aggr_tbs', 'N/A')
                ul_aggr_tbs = getattr(ue, 'ul_aggr_tbs', 'N/A')
                dl_curr_tbs = getattr(ue, 'dl_curr_tbs', 'N/A')
                ul_curr_tbs = getattr(ue, 'ul_curr_tbs', 'N/A')

                dl_sched_rb = getattr(ue, 'dl_sched_rb', 'N/A')
                ul_sched_rb = getattr(ue, 'ul_sched_rb', 'N/A')

                dl_aggr_prb = getattr(ue, 'dl_aggr_prb', 'N/A')
                ul_aggr_prb = getattr(ue, 'ul_aggr_prb', 'N/A')
                dl_aggr_retx_prb = getattr(ue, 'dl_aggr_retx_prb', 'N/A')
                ul_aggr_retx_prb = getattr(ue, 'ul_aggr_retx_prb', 'N/A')

                pusch_snr = getattr(ue, 'pusch_snr', 'N/A')
                pucch_snr = getattr(ue, 'pucch_snr', 'N/A')

                dl_bler = getattr(ue, 'dl_bler', 'N/A')
                ul_bler = getattr(ue, 'ul_bler', 'N/A')

                frame = getattr(ue, 'frame', 'N/A')
                slot = getattr(ue, 'slot', 'N/A')

                print(f"🔸 UE[{i}] RNTI={rnti} | PHR={phr} | BSR={bsr} | CQI={wb_cqi}")
                print(f"    MCS (DL1={dl_mcs1}, DL2={dl_mcs2} | UL1={ul_mcs1}, UL2={ul_mcs2})")
                print(f"    TBS (DL={dl_aggr_tbs}, UL={ul_aggr_tbs} | Curr DL={dl_curr_tbs}, Curr UL={ul_curr_tbs})")
                print(f"    Sched RBs (DL={dl_sched_rb}, UL={ul_sched_rb})")
                print(f"    PRBs Used (DL={dl_aggr_prb}, UL={ul_aggr_prb}) | Retx (DL={dl_aggr_retx_prb}, UL={ul_aggr_retx_prb})")
                print(f"    SNR (PUSCH={pusch_snr} dB | PUCCH={pucch_snr} dB)")
                print(f"    BLER (DL={dl_bler}, UL={ul_bler})")
                print(f"    Frame={frame} | Slot={slot}")

            if hasattr(ind, "tstamp"):
                t_now = time.time_ns() / 1000.0
                t_mac = ind.tstamp / 1.0
                latency = t_now - t_mac
                print(f"\n🕒 MAC tstamp = {t_mac:.0f} μs | Latency = {latency:.2f} μs")
            else:
                print("⚠️ No 'tstamp' found in MAC indication")

        except Exception as e:
            print(f"❌ Error during MAC metric parsing: {e}")
```

> **Tip**: You can copy this block into your Python xApp script or adapt it to log the data elsewhere (CSV, DB, Prometheus...).

---

> Next: Understand the full list of commonly used UE fields
👉 [`04_common_fields.md`](./04_common_fields.md)