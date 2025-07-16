# Displaying PDCP Metrics in Terminal Logs

Once you're able to access `rb_stats` from a PDCP indication, the next step is to extract and format the data for logging or debugging purposes.

This section demonstrates how to display key PDCP fields and measure reporting latency using the `tstamp`.

---

## Logging Basic Metrics

Here's an example of logging selected PDCP fields per Radio Bearer:

```python
def handle(self, ind):
    try:
        print(f"📡 PDCP Indication with {len(ind.rb_stats)} RBs")

        for i, rb in enumerate(ind.rb_stats):
            rnti = getattr(rb, 'rnti', 'N/A')
            lcid = getattr(rb, 'lcid', 'N/A')
            tx_bytes = getattr(rb, 'txpdu_bytes', 'N/A')
            rx_bytes = getattr(rb, 'rxpdu_bytes', 'N/A')
            retx_pkts = getattr(rb, 'txpdu_retx_pkts', 'N/A')
            dup_pkts = getattr(rb, 'rxpdu_dup_pkts', 'N/A')

            print(f"🔸 RB[{i}] RNTI={rnti} | LCID={lcid} | TX={tx_bytes} | RX={rx_bytes}")
            print(f"    Retx={retx_pkts} | Dup={dup_pkts}")

    except Exception as e:
        print(f"❌ Error during PDCP logging: {e}")
```

---

## Calculating Timestamp & Latency

You can compare the reporting time to current time:

```python
if hasattr(ind, "tstamp"):
    t_now = time.time_ns() / 1000.0  # Current time in μs
    t_pdcp = ind.tstamp / 1.0        # Already in μs
    latency = t_now - t_pdcp

    print(f"🕒 PDCP tstamp = {t_pdcp:.0f} μs | Latency = {latency:.2f} μs")
else:
    print("⚠️ No 'tstamp' found in PDCP indication")
```

---

## Sample Output

```text
📡 PDCP Indication with 2 RBs

🔸 RB[0] RNTI=43150 | LCID=3 | TX=1040000 | RX=1038200
    Retx=12 | Dup=4

🕒 PDCP tstamp = 1721064982003210 μs | Latency = 289.74 μs
```

---

## Pro Tip: Format for Readability

Use f-string formatting to align your log output:

```python
print(f"RB[{i}] RNTI={rnti:<6} | LCID={lcid:<2} | TX={tx_bytes:<8} | RX={rx_bytes:<8}")
```

---

## Summary

* Display useful PDCP metrics like TX/RX bytes, retransmissions, duplicates
* Use the `tstamp` field to calculate latency
* Wrap all logging in `try/except` blocks
* Align your logs for easy reading

---

### Full Example: Display All MAC Metrics (Python)

```python
class PDCPCallback(ric.pdcp_cb):
    def __init__(self):
        ric.pdcp_cb.__init__(self)

    def handle(self, ind):
        try:
            print(f"📡 PDCP Indication received with {len(ind.rb_stats)} RBs")

            for i, rb in enumerate(ind.rb_stats):
                rnti = getattr(rb, 'rnti', 'N/A')
                lcid = getattr(rb, 'lcid', 'N/A')
                status = getattr(rb, 'status', 'N/A')

                tx_pkts = getattr(rb, 'txpdu_pkts', 'N/A')
                tx_bytes = getattr(rb, 'txpdu_bytes', 'N/A')
                tx_sn = getattr(rb, 'txpdu_sn', 'N/A')
                tx_wt = getattr(rb, 'txpdu_wt', 'N/A')
                tx_disc_pkts = getattr(rb, 'txpdu_pkts_discarded', 'N/A')
                tx_disc_bytes = getattr(rb, 'txpdu_bytes_discarded', 'N/A')
                tx_retx_pkts = getattr(rb, 'txpdu_retx_pkts', 'N/A')
                tx_retx_bytes = getattr(rb, 'txpdu_retx_bytes', 'N/A')

                rx_pkts = getattr(rb, 'rxpdu_pkts', 'N/A')
                rx_bytes = getattr(rb, 'rxpdu_bytes', 'N/A')
                rx_dup_pkts = getattr(rb, 'rxpdu_dup_pkts', 'N/A')
                rx_dup_bytes = getattr(rb, 'rxpdu_dup_bytes', 'N/A')
                rx_ooo_pkts = getattr(rb, 'rxpdu_ooo_pkts', 'N/A')
                rx_ooo_bytes = getattr(rb, 'rxpdu_ooo_bytes', 'N/A')
                rx_drop_pkts = getattr(rb, 'rxpdu_drop_pkts', 'N/A')
                rx_drop_bytes = getattr(rb, 'rxpdu_drop_bytes', 'N/A')
                rx_valid_pkts = getattr(rb, 'rxpdu_valid_pkts', 'N/A')
                rx_valid_bytes = getattr(rb, 'rxpdu_valid_bytes', 'N/A')
                rx_sn = getattr(rb, 'rxpdu_sn', 'N/A')
                rx_wt = getattr(rb, 'rxpdu_wt', 'N/A')

                print(f"🔸 RB[{i}] RNTI={rnti} | LCID={lcid} | Status={status}")
                print(f"    TX: {tx_pkts} pkts / {tx_bytes} bytes | SN={tx_sn} | WT={tx_wt}")
                print(f"        Discarded: {tx_disc_pkts} pkts / {tx_disc_bytes} bytes | Retx: {tx_retx_pkts} pkts / {tx_retx_bytes} bytes")
                print(f"    RX: {rx_pkts} pkts / {rx_bytes} bytes | SN={rx_sn} | WT={rx_wt}")
                print(f"        Duplicates: {rx_dup_pkts} pkts / {rx_dup_bytes} bytes")
                print(f"        Out-of-Order: {rx_ooo_pkts} pkts / {rx_ooo_bytes} bytes")
                print(f"        Dropped: {rx_drop_pkts} pkts / {rx_drop_bytes} bytes")
                print(f"        Validated: {rx_valid_pkts} pkts / {rx_valid_bytes} bytes")

            if hasattr(ind, "tstamp"):
                t_now = time.time_ns() / 1000.0
                t_pdcp = ind.tstamp / 1.0
                latency = t_now - t_pdcp
                print(f"\n🕒 PDCP tstamp = {t_pdcp:.0f} μs | Latency = {latency:.2f} μs")
            else:
                print("⚠️ No 'tstamp' found in PDCP indication")

        except Exception as e:
            print(f"❌ Error during PDCP metric parsing: {e}")
```

> **Tip**: You can copy this block into your Python xApp script or adapt it to log the data elsewhere (CSV, DB, Prometheus...).

---

> Next: Field overview for all common PDCP metrics
> 👉 [`04_common_fields.md`](./04_common_fields.md)
