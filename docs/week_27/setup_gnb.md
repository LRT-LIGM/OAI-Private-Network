# gNodeB Configuration with OpenAirInterface

This document describes the installation and execution of the gNodeB (5G base station) using OpenAirInterface as part of the 5G private network project.

---

## Environment Used

* **Machine**: OAIBOX (PC1)
* **SDR Hardware**: None used (`--rfsim` mode)
* **Project cloned from**:
  [https://github.com/OPENAIRINTERFACE/openairinterface5g](https://github.com/OPENAIRINTERFACE/openairinterface5g)

---

## Installation Steps

### 1. Clone the project

```bash
git clone https://gitlab.eurecom.fr/oai/openairinterface5g.git
cd openairinterface5g
```

---

### 2. Compile the gNodeB

```bash
source oaienv
cd cmake_targets
./build_oai -I --gNB --ninja
```

> Wait for the message: `BUILD SUCCESSFUL`

---

### 3. Configuration file

*Example config:*
`targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.band78.tm1.106PRB.usrpb210.conf`

> Important:

* Adjust the name of the network interface used to connect to the Core
* Ensure the AMF IP address is correct

---

### 4. Launch the gNodeB

```bash
sudo ./nr-softmodem -O path/to/gnb.conf --rfsim
```

> The `--rfsim` option is used to simulate the SDR.

---

### 5. Logs to monitor

* NG-Setup establishment with the AMF
* Successful S1 connection
* Continuous logging in the terminal

---

## Key Considerations

* The Core must be running before launching the gNodeB
* The `.conf` files must match the Core configuration (bands, PLMN, etc.)

---
