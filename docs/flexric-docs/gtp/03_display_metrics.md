# Displaying GTP Metrics in Terminal Logs

Once you have access to the `gtp_stats` vector from a GTP indication, you can format and display the metrics for debugging, monitoring, or logging purposes.

This guide shows how to log key tunnel statistics and measure latency using the `tstamp`.

---

## Logging Basic Metrics

Here’s a simple example of how to extract and print important GTP stats:

```python
def handle(self, ind):
    try:
        print(f"📡 GTP Indication received with {len(ind.gtp_stats)} TEIDs")

        for i, stat in enumerate(ind.gtp_stats):
            teid = getattr(stat, 'teid', 'N/A')
            tx_bytes = getattr(stat, 'tx_total_bytes', 'N/A')
            rx_bytes = getattr(stat, 'rx_total_bytes', 'N/A')
            tx_pkts = getattr(stat, 'tx_total_pkts', 'N/A')
            rx_pkts = getattr(stat, 'rx_total_pkts', 'N/A')

            print(f"🔸 TEID={teid} | TX={tx_bytes} bytes / {tx_pkts} pkts | RX={rx_bytes} bytes / {rx_pkts} pkts")

    except Exception as e:
        print(f"❌ Error during GTP metric logging: {e}")
```

---

## Adding Timestamp & Latency

Use the `tstamp` field from the indication:

```python
if hasattr(ind, "tstamp"):
    t_now = time.time_ns() / 1000.0  # Current time in μs
    t_gtp = ind.tstamp / 1.0         # Already in μs
    latency = t_now - t_gtp

    print(f"🕒 GTP tstamp = {t_gtp:.0f} μs | Latency = {latency:.2f} μs")
else:
    print("⚠️ No 'tstamp' found in GTP indication")
```

---

## Sample Output

```text
📡 GTP Indication received with 1 TEIDs

🔸 TEID=10853 | TX=1542000 bytes / 1753 pkts | RX=1518000 bytes / 1720 pkts

🕒 GTP tstamp = 1721065239012810 μs | Latency = 301.18 μs
```

---

## Pro Tip: Align Output

Use formatting for consistent log alignment:

```python
print(f"TEID={teid:<6} | TX={tx_bytes:<10} / {tx_pkts:<5} pkts | RX={rx_bytes:<10} / {rx_pkts:<5} pkts")
```

---

## Summary

* Use `getattr()` to safely access metrics per TEID
* Display total bytes/packets sent and received
* Include latency using the `tstamp` field
* Format output for easy terminal readability

---

### Full Example: Display All MAC Metrics (Python)

```python
class GTPCallback(ric.gtp_cb):
    def __init__(self):
        ric.gtp_cb.__init__(self)

    def handle(self, ind):
        try:
            print(f"📡 GTP Indication received with {len(ind.gtp_stats)} tunnels")

            for i, stat in enumerate(ind.gtp_stats):
                teid = getattr(stat, 'teid', 'N/A')
                status = getattr(stat, 'status', 'N/A')

                tx_bytes = getattr(stat, 'tx_total_bytes', 'N/A')
                rx_bytes = getattr(stat, 'rx_total_bytes', 'N/A')
                tx_pkts = getattr(stat, 'tx_total_pkts', 'N/A')
                rx_pkts = getattr(stat, 'rx_total_pkts', 'N/A')
                tx_drop = getattr(stat, 'tx_drop_bytes', 'N/A')
                rx_drop = getattr(stat, 'rx_drop_bytes', 'N/A')

                print(f"🔸 Tunnel[{i}] TEID={teid} | Status={status}")
                print(f"    TX: {tx_pkts} pkts / {tx_bytes} bytes | Drops: {tx_drop} bytes")
                print(f"    RX: {rx_pkts} pkts / {rx_bytes} bytes | Drops: {rx_drop} bytes")

            if hasattr(ind, "tstamp"):
                t_now = time.time_ns() / 1000.0
                t_gtp = ind.tstamp / 1.0
                latency = t_now - t_gtp
                print(f"\n🕒 GTP tstamp = {t_gtp:.0f} μs | Latency = {latency:.2f} μs")
            else:
                print("⚠️ No 'tstamp' found in GTP indication")

        except Exception as e:
            print(f"❌ Error during GTP metric parsing: {e}")
```

> **Tip**: You can copy this block into your Python xApp script or adapt it to log the data elsewhere (CSV, DB, Prometheus...).

---

> Next: Common field descriptions for GTP stats
> 👉 [`04_common_fields.md`](./04_common_fields.md)
