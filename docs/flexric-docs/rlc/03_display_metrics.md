# Displaying RLC Metrics in Terminal Logs

Now that you can access `rb_stats` inside the RLC callback, this section shows how to display these values clearly in your terminal logs for debugging, monitoring, or analysis.

---

## Logging Basic Metrics

Here's a basic example for printing key fields:

```python
def handle(self, ind):
    try:
        print(f"📡 RLC Indication received with {len(ind.rb_stats)} RBs")

        for i, rb in enumerate(ind.rb_stats):
            rnti     = getattr(rb, 'rnti', 'N/A')
            mode     = getattr(rb, 'mode', 'N/A')  # e.g., AM, UM
            tx_bytes = getattr(rb, 'tx_bytes', 'N/A')
            rx_bytes = getattr(rb, 'rx_bytes', 'N/A')
            sn_tx    = getattr(rb, 'sn_tx', 'N/A')
            sn_rx    = getattr(rb, 'sn_rx', 'N/A')

            print(f"🔸 RB[{i}] RNTI={rnti} | Mode={mode} | TX={tx_bytes} | RX={rx_bytes}")
            print(f"    Seq TX={sn_tx} | Seq RX={sn_rx}")

    except Exception as e:
        print(f"❌ Error during RLC metric logging: {e}")
```

---

## Adding Timestamp & Latency

The `ind` object also contains a timestamp (in microseconds). You can calculate how delayed the indication is:

```python
if hasattr(ind, "tstamp"):
    t_now = time.time_ns() / 1000.0  # Current time in μs
    t_rlc = ind.tstamp / 1.0         # Already in μs
    latency = t_now - t_rlc

    print(f"🕒 RLC tstamp = {t_rlc:.0f} μs | Latency = {latency:.2f} μs")
else:
    print("⚠️ No 'tstamp' found in RLC indication")
```

---

## Example Output

```text
 RLC Indication received with 2 RBs

🔸 RB[0] RNTI=43150 | Mode=AM | TX=251203 | RX=194382
    Seq TX=1024 | Seq RX=999

🔸 RB[1] RNTI=43151 | Mode=UM | TX=100293 | RX=202020
    Seq TX=120 | Seq RX=110

 RLC tstamp = 1721064569103520 μs | Latency = 311.28 μs
```

---

## Pro Tip: Align Output

Use string formatting to align logs for better readability:

```python
print(f"RB[{i}] RNTI={rnti:<6} | Mode={mode:<2} | TX={tx_bytes:<8} | RX={rx_bytes:<8}")
```

---

## Summary

* Log key fields like `rnti`, `mode`, `tx_bytes`, `rx_bytes`, `sn_tx`, and `sn_rx`
* Use `tstamp` to compute latency and monitor real-time delays
* Always wrap your logging code with `try/except`
* Format outputs cleanly for better terminal visualization

---

### Full Example: Display All MAC Metrics (Python)

```python
class RLCCallback(ric.rlc_cb):
    def __init__(self):
        ric.rlc_cb.__init__(self)

    def handle(self, ind):
        try:
            print(f"📡 RLC Indication received with {len(ind.rb_stats)} RBs")

            for i, rb in enumerate(ind.rb_stats):
                rnti     = getattr(rb, 'rnti', 'N/A')
                lcid     = getattr(rb, 'lcid', 'N/A')
                mode     = getattr(rb, 'mode', 'N/A')
                tx_bytes = getattr(rb, 'tx_bytes', 'N/A')
                rx_bytes = getattr(rb, 'rx_bytes', 'N/A')
                sn_tx    = getattr(rb, 'sn_tx', 'N/A')
                sn_rx    = getattr(rb, 'sn_rx', 'N/A')
                tx_sdu   = getattr(rb, 'tx_sdu', 'N/A')
                rx_sdu   = getattr(rb, 'rx_sdu', 'N/A')
                tx_pdu   = getattr(rb, 'tx_pdu', 'N/A')
                rx_pdu   = getattr(rb, 'rx_pdu', 'N/A')
                tx_retx  = getattr(rb, 'tx_retx', 'N/A')
                status   = getattr(rb, 'status', 'N/A')

                print(f"🔸 RB[{i}] RNTI={rnti} | LCID={lcid} | Mode={mode} | Status={status}")
                print(f"    TX: {tx_bytes} bytes / {tx_pdu} PDUs / {tx_sdu} SDUs | Retransmissions: {tx_retx}")
                print(f"    RX: {rx_bytes} bytes / {rx_pdu} PDUs / {rx_sdu} SDUs")
                print(f"    SN_TX={sn_tx} | SN_RX={sn_rx}")

            if hasattr(ind, "tstamp"):
                t_now = time.time_ns() / 1000.0
                t_rlc = ind.tstamp / 1.0
                latency = t_now - t_rlc
                print(f"\n🕒 RLC tstamp = {t_rlc:.0f} μs | Latency = {latency:.2f} μs")
            else:
                print("⚠️ No 'tstamp' found in RLC indication")

        except Exception as e:
            print(f"❌ Error during RLC metric parsing: {e}")
```

> **Tip**: You can copy this block into your Python xApp script or adapt it to log the data elsewhere (CSV, DB, Prometheus...).

---

> Next: Explore commonly available RLC fields
> 👉 [`04_common_fields.md`](./04_common_fields.md)
