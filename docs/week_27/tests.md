# Connectivity Tests – 5G Private Network

This file summarizes the tests performed throughout the project, along with observations and results.

---

## 1. 5G Core Test (CN5G)

### Objective:

Verify that Docker containers for the core network are starting correctly.

### Commands:

```bash
docker ps
docker-compose logs -f oai-amf
```

### Expected Result:

All containers are `healthy`, and logs show proper activity from AMF, SMF, UPF, etc.

---

## 2. gNodeB Test with `--rfsim`

### Objective:

Launch the gNodeB without physical hardware to simulate a radio environment.

### Command:

```bash
sudo ./nr-softmodem -O CONF/gnb.sa.conf --rfsim
```

### Expected Result:

The gNodeB connects successfully to the core.

---

## 3. UE Test with `--rfsim`

### Command:

```bash
sudo ./nr-uesoftmodem -O CONF/ue.conf --rfsim
```

### Expected Result:

The UE attaches correctly to the network and obtains an IP address.

---

## 4. Network Scan via Quectel Modem

### Command:

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-network-scan
```

### Expected Result:

List of available networks in France (Orange, Free, SFR, BYTEL...).

---

## 5. Network Attachment Test – Bouygues (BYTEL)

### Commands:

```bash
sudo ./quectel-CM -s ebouygtel.com
sudo qmicli -d /dev/cdc-wdm1 --nas-get-serving-system
```

### Issue Encountered:

Status remains: `registration-denied`, `PS: detached`, `DataCap: UNKNOW`, `Forbidden: yes`

---

## 6. DHCP on `wwan0`

### Command:

```bash
sudo udhcpc -i wwan0
```

### Result:

Infinite loop on `sending discover`, no IP obtained → Because the modem is not attached to the network.

---

## 7. Signal Verification

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-get-signal-strength
```

### Example Signal:

```
Network 'umts': '-70 dBm'
SINR (8): '9.0 dB'
```

---
