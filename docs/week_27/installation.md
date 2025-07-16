# Installation – Environment Preparation

This section describes all the necessary steps to install the tools used in the OAI Private Network project.

---

## 1. Basic Dependencies

Before cloning the project, install the following packages:

```bash
sudo apt update && sudo apt install -y \
  git cmake build-essential \
  python3 python3-pip python3-dev \
  libboost-all-dev libsctp-dev lksctp-tools \
  libssl-dev libffi-dev libconfig++-dev \
  net-tools iputils-ping \
  usbutils pciutils
```

---

## 2. Installing Docker and Docker Compose

```bash
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sudo usermod -aG docker $USER
```

> ⚠️ Restart your session to apply Docker permissions.

---

## 3. Cloning the Project

```bash
git clone https://github.com/OPENAIRINTERFACE/openairinterface5g.git
cd openairinterface5g
```

---

## 4. Compiling the gNodeB

```bash
cd cmake_targets
./build_oai -I --gNB
```

> If no SDR is used, run in radio simulation mode with `--rfsim`:

```bash
sudo ./nr-softmodem -O <conf_path> --rfsim
```

---

## 5. 5G Core via Docker

Clone the CN5G repository:

```bash
git clone https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed.git
cd oai-cn5g-fed/docker-compose
```

Download Docker images:

```bash
./build_all_images --latest
docker-compose up -d
```

---

## 6. Drivers for Quectel Modem

Load the modules:

```bash
sudo modprobe option
sudo modprobe usb_wwan
sudo modprobe qmi_wwan
```

Validate detection:

```bash
ls /dev/cdc-wdm*
```

---

## 7. File Organization

All working files are placed in:

```
~/Documents/quectel/quectel-CM/
~/Documents/openairinterface5g/
~/Documents/oai-cn5g-fed/
```

---
