# Configuration – 5G Private Network Setup

This file details the configuration of each component in the OAI environment: core network, gNodeB, UE, and modem.

---

## 1. Core 5G (CN5G)

### a. Cloning and launch

```bash
git clone https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed.git
cd oai-cn5g-fed/docker-compose
./build_all_images --latest
docker-compose up -d
```

### b. Verification

```bash
docker ps
docker-compose logs -f oai-amf
```

> All containers must be `healthy`.

---

## 2. gNodeB (RAN)

### a. Compilation

```bash
cd openairinterface5g/cmake_targets
./build_oai -I --gNB
```

### b. Launch in simulation mode (without SDR)

```bash
sudo ./nr-softmodem -O ./targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.conf --rfsim
```

> The `--rfsim` option allows testing without radio hardware.

---

## 3. UE – User Equipment

Launch with `nr-uesoftmodem`:

```bash
sudo ./nr-uesoftmodem -O ./targets/PROJECTS/GENERIC-NR-5GC/CONF/ue.conf --rfsim
```

---

## 4. Quectel Modem Configuration

### a. Launch the `quectel-CM` tool

```bash
cd ~/Documents/quectel/quectel-CM/out
sudo ./quectel-CM -s ebouygtel.com
```

### b. SIM check

```bash
sudo qmicli -d /dev/cdc-wdm1 --uim-get-card-status
```

### c. Force network connection

```bash
sudo ip link set wwan0 up
sudo udhcpc -i wwan0
```

---

## 5. Scan for available networks

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-network-scan
```

> Example result:

```
Network [6]:
	MCC: '208'  MNC: '20'  Description: 'BYTEL'
	Status: current-serving, roaming, not-forbidden
```

---

## 6. Check connection status

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-get-serving-system
```

> Check that `Registration state: registered`
> and that `DataCap` is not `UNKNOW`.

---