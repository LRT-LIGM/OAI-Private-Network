# 05 - External Data Network (ext-dn) Debugging

## Context

The container `oai-ext-dn` is designed to simulate an external data network for UE internet access via UPF.

---

## Configuration

**docker-compose-basic-nrf.yaml** snippet:

```yaml
oai-ext-dn:
  privileged: true
  init: true
  container_name: oai-ext-dn
  image: oaisoftwarealliance/trf-gen-cn5g:latest
  environment:
    - UPF_FQDN=oai-upf
    - UE_NETWORK=10.10.0.0/24
    - USE_FQDN=yes
  healthcheck:
    test: /bin/bash -c "ip r | grep 12.1.1"
    interval: 10s
    timeout: 5s
    retries: 5
  networks:
    public_net:
      ipv4_address: 192.168.70.135
```

---

## Observations

* The `oai-ext-dn` container often reports **`(unhealthy)`**.
* Even though IPs are correctly assigned (`10.10.0.2`), **outbound connectivity fails** (no ping or curl success).
* DNS server provided: `172.21.3.100` → **not reachable**

---

## Testing Commands

### Check connectivity to UPF

```bash
ping 192.168.70.132
```

✅ Works from host via `wwan0`

### Check ping to public IP

```bash
ping -I wwan0 8.8.8.8
```

❌ Fails: 100% packet loss

---

## Tcpdump Analysis

```bash
sudo tcpdump -i wwan0
```

* ICMP to `8.8.8.8` leaves the host.
* **No ICMP reply comes back**.
* DNS queries are sent to `172.21.3.100` but no response is received.

---

## NAT & Routing Attempts

### Applied Rules

```bash
sudo iptables -t nat -F POSTROUTING
sudo iptables -t nat -A POSTROUTING -o wwan0 -j MASQUERADE
```

* IP forwarding enabled: `cat /proc/sys/net/ipv4/ip_forward → 1`
* Routes:

  ```bash
  default via 10.10.0.1 dev wwan0
  10.10.0.0/30 dev wwan0 proto kernel scope link src 10.10.0.2
  ```

Still, **no internet access** from `ext-dn`.

---

## Manual Test from Container

```bash
docker exec -it oai-ext-dn bash
ping 8.8.8.8
```

❌ No response
✅ `ping 10.10.0.1` works (gateway reachable)

---

## Summary

| Test                                | Result      |
| ----------------------------------- | ----------- |
| ping gateway `10.10.0.1`            | OK        |
| ping public IP `8.8.8.8`            | Fails     |
| dig via DNS `172.21.3.100`          | Timeout   |
| IP assigned to `wwan0`              | 10.10.0.2 |
| NAT/MASQUERADE via `iptables`       | Applied   |
| Interface `wwan0` route and gateway | OK        |

---
