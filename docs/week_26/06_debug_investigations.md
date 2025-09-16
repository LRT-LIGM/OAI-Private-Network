> **⚠️ Important Note**  
> This file contains useful information not covered in the main documentation. It is recommended for debugging.

# 06 - Debug Investigations & Manual Commands

## Objective

To investigate the lack of external internet access despite successful IP configuration and modem attachment. This document tracks manual investigations and command-line diagnostics performed during the week.

---

## Environment Overview

- **Modem**: Quectel RM500Q
- **Interface**: `wwan0`
- **Assigned IP**: `10.10.0.2/30`
- **Gateway**: `10.10.0.1`
- **DNS provided**: `172.21.3.100`
- **Tools used**: `ping`, `curl`, `dig`, `tcpdump`, `iptables`, `ip route`, `qmicli`, `mmcli`

---

## Manual Routing & NAT Adjustments

### Route verification

```bash
ip route | grep wwan0
# Output:
default via 10.10.0.1 dev wwan0 
10.10.0.0/30 dev wwan0 proto kernel scope link src 10.10.0.2
```

### NAT rules

```bash
sudo iptables -t nat -F POSTROUTING
sudo iptables -t nat -A POSTROUTING -o wwan0 -j MASQUERADE
```

Also tested SNAT:

```bash
sudo iptables -t nat -A POSTROUTING -s 10.10.0.0/24 -o wwan0 -j SNAT --to-source 10.10.0.2
```

---

## 📡 Connectivity Tests

### Ping gateway

```bash
ping -I wwan0 10.10.0.1
# ✅ Success
```

### Ping public IP

```bash
ping -I wwan0 8.8.8.8
# ❌ No response
```

### DNS Resolution

```bash
dig google.com @172.21.3.100
# ❌ Timeout
```

```bash
curl --interface wwan0 http://neverssl.com
# ❌ No response
```

---

## Tcpdump Analysis

```bash
sudo tcpdump -i wwan0
```

Findings:

* ICMP echo requests to `8.8.8.8` are sent
* No echo replies observed
* DNS requests to `172.21.3.100` are sent repeatedly without any answer
* Gateway `10.10.0.1` responds correctly to pings

---

## Additional Tests & Notes

### qmicli settings check

```bash
sudo qmicli -d /dev/cdc-wdm1 --wds-get-current-settings
```

```text
IPv4 address: 10.10.0.2
IPv4 gateway address: 10.10.0.1
IPv4 primary DNS: 172.21.3.100
```

### ip forwarding check

```bash
cat /proc/sys/net/ipv4/ip_forward
# ✅ 1 (enabled)
```

---

## Blockers & Hypotheses

| Area          | Issue                                      | Notes                            |
| ------------- | ------------------------------------------ | -------------------------------- |
| Internet      | No ping to public IPs                      | NAT and routing confirmed OK     |
| DNS           | Provided server (172.21.3.100) unreachable | Possible external network block  |
| Firewall      | No evidence of local firewall blocking     | Still under observation          |
| ISP / Network | 10.10.0.1 might not route out              | Needs confirmation from provider |

---
