# 04 - Core Network Status Check (OAI CN5G)

## Objective

Verify the successful deployment and health of the OAI 5G Core Network using `docker-compose` and analyze service registration with NRF.

---

## Docker Launch

### Launch Command

```bash
python3 core-network.py --type start-basic --scenario 1
```

### Output (Expected)

* All containers should launch:

  * `mysql`, `oai-nrf`, `oai-amf`, `oai-smf`, `oai-upf`
  * `oai-ausf`, `oai-udm`, `oai-udr`, `oai-ext-dn`

### Sample Output

```
[INFO] OAI 5G Core network started, checking the health status...
[INFO] All components are healthy
```

---

## Health Check

```bash
docker-compose -f docker-compose-basic-nrf.yaml ps -a
```

Verify `State` column shows `Up (healthy)`.

> ❗ If a service shows `(unhealthy)` → run `docker logs <container>` to investigate.

---

## NRF Registration Checks

```bash
curl -s -X GET --http2-prior-knowledge http://<nrf_ip>:8080/nnrf-nfm/v1/nf-instances?nf-type="AMF"
```

Expected response should include:

```
192.168.70.138  (AMF)
192.168.70.135  (SMF)
192.168.70.133  (UPF)
192.168.70.134  (AUSF)
192.168.70.137  (UDM)
192.168.70.136  (UDR)
```

---

## Interface Overview

| Component | Key Ports Used   | Notes                         |
| --------: | ---------------- | ----------------------------- |
|     `AMF` | 38412/sctp, 8080 | Connects to gNB               |
|     `SMF` | 8805/udp         | Interfaces with UPF via N4    |
|     `UPF` | 2152/udp         | Handles GTP-U                 |
|     `NRF` | 8080             | Central registry for all NFs  |
| `UDM/UDR` | 8080             | User data + subscription info |
|    `AUSF` | 8080             | Authentication services       |

---

## Troubleshooting

### If `oai-ext-dn` is `unhealthy`

* Confirm it has access to the network

* Example healthcheck:

  ```yaml
  test: /bin/bash -c "ip r | grep 12.1.1"
  ```

* Verify that `12.1.1.0/26` or similar is part of the UPF/SMF configuration.

### If SMF ↔ UPF fail

* Check SMF logs for:

  ```
  UPF did not answer to N4 Association request
  ```

* Check `ipv4_subnet` and `dnn` mapping in the config YAML files

---

## Confirmed Working

* All containers launched via `docker-compose`
* NRF shows successful NF instance registration
* `oai-ext-dn` pings from wwan0 (tested from host)

---

## Confirmed Issues

* Internet reachability from `oai-ext-dn` still fails (diagnosed separately)
* DNS resolution through the core not functional yet

---
