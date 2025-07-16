# Environment Setup – OAI 5G SA with FlexRIC

This section describes the environment preparation steps for deploying the OAI 5G SA testbed along with FlexRIC and xApps on a local Linux host.

---

## 1. Hardware and OS

- **Host**: Ubuntu 22.04 LTS
- **SDR**: USRP B210 (connected via USB3)
- **UE**: Quectel RM500Q EVB (USB, exposed as `/dev/cdc-wdm1`)

---

## 2. Repository Cloning

```bash
# Clone FlexRIC
git clone https://gitlab.eurecom.fr/mosaic5g/flexric.git
cd flexric
```

```bash
# Clone OpenAirInterface 5G SA
git clone https://gitlab.eurecom.fr/oai/openairinterface5g.git
cd openairinterface5g
```

---

## 3. Dependency Installation

```bash
sudo apt update
sudo apt install -y build-essential cmake libsqlite3-dev clang sqlite3 libsctp-dev libtool autoconf
```

Additional dependencies may be required based on your system and FlexRIC version:

* `swig`, `libyaml-dev`, `python3-dev`, etc.

---

## 4. Building FlexRIC

```bash
mkdir build && cd build
cmake -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ ..
make -j1
```

✅ Ensure that these binaries are built:

* `build/examples/ric/nearRT-RIC`
* `build/examples/xApp/c/monitor/xapp_gtp_mac_rlc_pdcp_moni`

If any of them is missing, rebuild carefully and inspect the logs.

---

## 5. Building OAI gNodeB

Follow the official [OAI gNB build guide](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/NR_SA_Tutorial_OAI_nrUE.md).

In short:

```bash
cd openairinterface5g
source oaienv
cd cmake_targets
./build_oai -I
./build_oai -c --nr_gnb --gNB
```

Test gNB with:

```bash
sudo ./nr-softmodem -O <gnb-config.conf> --rfsim
```

---

## 6. Configuration Files

FlexRIC and OAI share a common config file:

```bash
sudo cp flexric/flexric.conf /usr/local/etc/flexric/flexric.conf
```

xApp will look for `.so` plugins here:

```bash
/usr/local/lib/flexric/
```

Use symbolic links if needed.

---

## 7. Validating Setup

```bash
# Launch Near-RT RIC
./build/examples/ric/nearRT-RIC

# Launch the xApp
./build/examples/xApp/c/monitor/xapp_gtp_mac_rlc_pdcp_moni -p /usr/local/lib/flexric/ -c /usr/local/etc/flexric/flexric.conf
```

Check for:

* Successful E2 SETUP REQUEST/RESPONSE
* RIC SUBSCRIPTION RESPONSE logs
* SQLite DB created in `/tmp/xapp_db_*.db`

---
