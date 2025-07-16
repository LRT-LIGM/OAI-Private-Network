# Installation – Option 1 (From Scratch with USRP B210)

This guide details all the installation steps used in Option 1 of the project, based on the OAI 5G SA Deployment tutorial (Stage BUT3 R&T).

---

## 1. System Requirements & Preparation

### Minimum requirements:
- 4-core CPU (AMD/Intel x86_64 @3.5GHz+)
- 8GB RAM
- 40GB free space
- Ubuntu 20.04 or 22.04
- USRP B210
- SIM card (Sysmocom or OpenCells)
- USB 3.0 port

### Create a passwordless sudo user:
```bash
sudo visudo
# Add at the bottom (replace <user>)
<user> ALL=(ALL) NOPASSWD: ALL
```
Then:
```bash
sudo -k
```
Test:
```bash
sudo apt update  # should NOT prompt for password
```

---

## 2. System Update & Essentials
```bash
sudo apt update && sudo apt upgrade -y
```

(Optional) Install VSCode:
```bash
sudo apt install -f wget gpg -y
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg

echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null

rm -f packages.microsoft.gpg
sudo apt install -f apt-transport-https -y
sudo apt update
sudo apt install -f code -y
```

Install recommended VSCode extensions:
- One Dark Pro (theme)
- Material Icon Theme
- YAML (Red Hat)
- Bracket Pair Color DLW

---

## 3. UHD Driver Installation (for USRP)
```bash
sudo apt install -f autoconf automake build-essential ccache cmake cpufrequtils doxygen ethtool g++ git inetutils-tools libboost-all-dev libncurses5 libncurses5-dev libusb-1.0-0 libusb-1.0-0-dev libusb-dev python3-dev python3-mako python3-numpy python3-requests python3-scipy python3-setuptools python3-ruamel.yaml -y

git clone https://github.com/EttusResearch/uhd.git ~/uhd
cd ~/uhd
git checkout v4.6.0.0
cd host && mkdir build && cd build
cmake ../
make -j $(nproc)
make test
sudo make install
sudo ldconfig
sudo uhd_images_downloader
```

Check USRP device:
```bash
sudo uhd_find_devices
```

---

## 4. Clone & Build OAI gNB
```bash
git clone https://gitlab.eurecom.fr/oai/openairinterface5g.git ~/openairinterface5g
cd ~/openairinterface5g
git checkout develop

cd cmake_targets
./build_oai -I --install-optional-packages
# Watch the logs if needed:
tail -f ~/openairinterface5g/cmake_targets/log/asn1c_install_log.txt

# Then:
sudo apt install -f libforms-dev libforms-bin -y
./build_oai -I

# Final full build (with USRP, gNB, nrUE):
./build_oai -w USRP --ninja --nrUE --gNB --build-lib "nrscope uescope telnetsrv" -C
```

> ✅ You should see "Build should be successful"

---

## 5. Configuration File Setup
```bash
cd ~/openairinterface5g/cmake_targets/ran_build/build
mkdir config
cp ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf config/

mv config/gnb.sa.band78.fr1.106PRB.usrpb210.conf config/5GN78.conf
```

Edit `5GN78.conf`:
- Adjust **PLMN**, **RF frequencies**, **gain**, and insert:
```yaml
sdr_addrs = "serial=8002036"  # Replace with your USRP serial number
```

---

Ready to proceed to configuration & launch 🚀
