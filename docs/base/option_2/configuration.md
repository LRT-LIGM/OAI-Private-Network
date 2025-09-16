# Configuration – Setting up the Private 5G Network

This file details the configuration of each component of the OAI environment: core network, gNodeB, UE, and modem.

---

## 1. 5G Core (CN5G)

### a. Cloning and launching

```bash
wget -O ~/oai-cn5g.zip https://gitlab.eurecom.fr/oai/openairinterface5g/-/archive/develop/openairinterface5g-develop.zip?path=doc/tutorial_resources/oai-cn5g
unzip ~/oai-cn5g.zip
cd oai-cn5g
docker-compose up --build
```

### b. Verification

```bash
docker ps
docker-compose logs -f oai-amf
```

> All containers should show `healthy` status.

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

Launch using `nr-uesoftmodem`:

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

### b. SIM verification

```bash
sudo qmicli -d /dev/cdc-wdm1 --uim-get-card-status
```

### c. Force network connection

```bash
sudo ip link set wwan0 up
sudo udhcpc -i wwan0
```

---

## 5. Scan available networks

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-network-scan
```

> Example output:

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

> Verify that `Registration state: registered`
> and that `DataCap` is not `UNKNOWN`.