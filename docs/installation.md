# Installation – Environment Setup

This section describes all the steps required to install the tools used in the OAI Private Network project.

---

## 1. Basic dependencies

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

## 2. Install Docker and Docker Compose (v2)

```bash
# Uninstall old versions (if any)
sudo apt remove -y docker docker-engine docker.io containerd runc

# Install required dependencies
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release

# Add Docker’s official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Add Docker repository
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine and Docker Compose v2
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Enable Docker at boot and add current user to Docker group
sudo systemctl enable docker
sudo usermod -aG docker $USER
```

---

## 3. Clone the project

```bash
git clone https://github.com/OPENAIRINTERFACE/openairinterface5g.git
cd openairinterface5g
```

---

## 4. Compile the gNodeB

```bash
cd cmake_targets
./build_oai -I --gNB
```

> If no SDR is used, use `--rfsim` to simulate the radio:

```bash
sudo ./nr-softmodem -O <config_path> --rfsim
```

---

## 5. 5G Core via Docker

Clone the CN5G repository:

```bash
git clone https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed.git
cd oai-cn5g-fed/docker-compose
```

Download the Docker images:

```bash
./build_all_images --latest
docker-compose up -d
```

---

## 6. Drivers for the Quectel modem

Load the kernel modules:

```bash
sudo modprobe option
sudo modprobe usb_wwan
sudo modprobe qmi_wwan
```

Validate device detection:

```bash
ls /dev/cdc-wdm*
```

---

## 7. File organization

All working files are placed in:

```
~/Documents/quectel/quectel-CM/
~/Documents/openairinterface5g/
~/Documents/oai-cn5g-fed/
```