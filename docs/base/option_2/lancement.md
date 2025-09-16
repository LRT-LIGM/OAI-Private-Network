# Component Launch Guide

This page documents the steps required to launch the components of the OAI Private Network project.

---

## Prerequisites

* The `docker-compose` files for the 5G Core must be properly configured.
* The gNodeB (`nr-softmodem`) and/or `nr-uesoftmodem` must be successfully compiled.
* Check the availability of USRP interfaces or use `--rfsim` for simulation.

---

## Launch the 5G Core (CN5G)

```bash
cd ~/Documents/oai-cn5g
git checkout develop
sudo docker compose up
```

---

## Launch the gNodeB with B210

Manually add the missing IP address:

```bash
sudo ip addr add 172.31.0.150/24 dev oai-cn5g
```

```bash
cd ~/Documents/openairinterface5g/cmake_targets/ran_build/build
sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 6 -E --continuous-tx
```

> [NR_SA_Tutorial_OAI_CN5G](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/2025.w04/doc/NR_SA_Tutorial_OAI_CN5G.md?ref_type=tags)

---

## Launch the gNodeB (with radio simulation)

```bash
cd ~/Documents/openairinterface5g/cmake_targets/ran_build/build
sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 6 --rfsim
```

> Use `--rfsim` if you do not have a physical SDR connected.

---

## Launch the Simulated UE

```bash
cd ~/Documents/openairinterface5g/cmake_targets/ran_build/build
sudo ./nr-uesoftmodem -r 106 --numerology 1 --band 78 -C 3619200000 --uicc0.imsi 001010000000001 --rfsim
```

---

Last updated: 2025-06-03