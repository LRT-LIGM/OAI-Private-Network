# 02 - Network Tests and Connectivity Validation

## Objective

Test the modem’s ability to reach external networks (Internet), validate routing and DNS, and ensure proper data path via `wwan0`.

---

## Initial Conditions

- **Modem Interface**: `wwan0`
- **IP Address**: `10.10.0.2/30`
- **Gateway**: `10.10.0.1`
- **DNS**: `172.21.3.100` (provided by operator)
- **Default Route**: Assigned via `quectel-CM`

---

## Tests Performed

### 1. Ping Gateway

```bash
ping -I wwan0 10.10.0.1
```

✅ Successful
→ Confirms local link is functional between host and gateway.

---

### 2. Ping Public IP

```bash
ping -I wwan0 8.8.8.8
ping -I wwan0 1.1.1.1
```

❌ Failed (100% packet loss)
→ No response from external Internet destinations.

---

### 3. DNS Test

```bash
dig google.com @172.21.3.100
```

❌ Failed (timeout)
→ DNS server is unreachable or upstream issue.

---

### 4. Route Inspection

```bash
ip route | grep wwan0
```

✔ Confirmed default route via `10.10.0.1`
✔ No conflicting routes with higher priority

---

### 5. NAT Configuration (iptables)

```bash
sudo iptables -t nat -F POSTROUTING
sudo iptables -t nat -A POSTROUTING -o wwan0 -j MASQUERADE
```

✅ Confirmed rules applied
❌ Still no external reachability

---

### 6. Traffic Monitoring with tcpdump

```bash
sudo tcpdump -i wwan0
```

* ICMP echo requests (to gateway): ✅ Replies received
* DNS requests (to 172.21.3.100): ✅ Sent repeatedly
* DNS replies: ❌ None received
* External pings: ❌ No replies

---

## Analysis

| Test             | Result     | Observation                                  |
| ---------------- | ---------- | -------------------------------------------- |
| Ping Gateway     | OK       | Local modem connection works                 |
| Ping 8.8.8.8     | Failed   | No reachability beyond gateway               |
| DNS Resolution   | Failed   | DNS server unreachable                       |
| NAT Masquerading | Applied  | No effect on connectivity                    |
| tcpdump on wwan0 | Partial | Outgoing packets visible, no inbound replies |

---

## Hypotheses

* Carrier network may block traffic or drop Internet-bound packets
* APN might be restricted (e.g., private, no Internet breakout)
* Route is correct but upstream doesn’t allow forwarding

---

## What Works

* Interface `wwan0` is up and responding
* Gateway (`10.10.0.1`) replies to ICMP
* DNS queries are sent

---

## What Fails

* No reply from any Internet IP
* No DNS resolution
* No data path from modem to Internet

---