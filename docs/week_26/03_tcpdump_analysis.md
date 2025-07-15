# 03 - Tcpdump Analysis of WWAN Interface

## Objective

Analyze traffic on `wwan0` using `tcpdump` to observe outgoing requests and incoming responses. This helps diagnose issues like DNS failure, packet loss, and routing errors.

---

## Tools Used

- `tcpdump`: packet capture tool

```bash
sudo tcpdump -i wwan0
```

---

## Observations from Live Capture

### Successful ICMP to Gateway

```text
oai-2 > _gateway: ICMP echo request
_gateway > oai-2: ICMP echo reply
```

→ Shows the device can reach the local gateway (`10.10.0.1`) via ICMP
→ Confirms basic IP link is functional

---

### No Replies from Public IPs (e.g., 8.8.8.8)

* ICMP echo requests to 8.8.8.8 were sent
* No replies received

→ Either packets are dropped by the operator
→ Or no upstream NAT/routing available at the network level

---

### DNS Requests Sent, No Replies

```text
oai-2.XXXXX > 172.21.3.100.domain: A? google.com.
```

→ Repeated DNS queries sent from `wwan0`
→ No DNS replies captured
→ Confirmed with `dig @172.21.3.100` showing timeout

---

### ICMP Time Exceeded

```text
oai-2 > oai-2: ICMP time exceeded in-transit
```

→ Indicates TTL expired before reaching the destination
→ Packets may be looping or misrouted in the network

---

## Summary Table

| Packet Type       | Destination          | Observed? | Reply? | Notes                              |
| ----------------- | -------------------- | --------- | ------ | ---------------------------------- |
| ICMP ping         | `10.10.0.1`          | Yes     | Yes  | Local gateway reachable            |
| ICMP ping         | `8.8.8.8`, `1.1.1.1` | Yes     | No   | Upstream connectivity fails        |
| DNS query         | `172.21.3.100`       | Yes     | No   | No reply, even though queries sent |
| ICMP TTL Exceeded | local                | Yes     | -      | Sign of TTL expiration loops       |

---

## 🔎 Analysis

* DNS queries exit the system but do not return.
* ICMP to gateway works, confirming the modem is online.
* ICMP to Internet fails completely (even after masquerading).
* `tcpdump` confirms packet egress, but no ingress = carrier block, APN restriction, or no NAT beyond gateway.

---

## Possible Issues

* No IP forwarding beyond `10.10.0.1`
* Carrier blocks public routing for the APN used
* DNS server unreachable (or not allowed to reply)
* TTL expiry suggests misconfigured NAT or upstream router issue

---

## Confirmed Working

* `tcpdump` shows outgoing traffic clearly
* Local ping to gateway works fine
* `quectel-CM` sets up IP + DNS properly

---

## Confirmed Failing

* No Internet reachability
* No DNS resolution
* All external replies blocked or not routed back

---
