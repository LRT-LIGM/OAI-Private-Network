# Weekly Report – srsRAN 4G with EPC (Week of June 17–21, 2025)

## Weekly Objective

* Install, compile, and test `srsRAN_4G` locally
* Set up an LTE core (`srsepc`) and launch an eNodeB (`srsenb`)
* Connect an Android smartphone via SIM card
* Diagnose connection issues

---

## Steps Completed

### 1. Cloning and Compiling `srsRAN_4G`

```bash
git clone https://github.com/srsran/srsRAN_4G.git
cd srsRAN_4G && mkdir build && cd build
cmake .. && make -j$(nproc)
sudo make install
srsran_install_configs.sh user
```

> **Result**: Compilation successful, but `srsepc` binary not found

### 2. Fix Attempts

* Clean rebuild with `ENABLE_EPC=ON`
* Tried multiple branches: `main`, `release_23_11`, `release_22_10`
* Verified paths (`/usr/local/bin`, `build/src/srsepc/`)
* Installed system dependencies:

```bash
sudo apt install libboost-all-dev libsctp-dev libconfig++-dev libssl-dev
```

* Targeted compilation:

```bash
make srsepc
```

> **Result**: No `srsepc` executable generated

### 3. Test with `srsRAN_project` Repository

* Cloned: `https://github.com/srsran/srsRAN_project.git`
* Compilation + install → **successful build logs**
* ⚠️ But still **no `srsenb` or `srsepc`** found on disk

---

## Issues Encountered

* Successful build but missing binaries
* Mismatch between build logs and actual files
* Hypothesis: modules disabled or incompatible with Ubuntu 24.04

---

## Conclusion

* 🔹 `srsepc` not found despite EPC module enabled
* 🔹 No usable binaries to test the radio stack

---

## Recommended Next Steps

* Roll back to a stable version: **Ubuntu 20.04 + srsLTE repo**
* Try a **stable Docker setup (OpenAirInterface or FireCell)**
* Goal: be able to run eNB + EPC and test a real SIM with USRP or Quectel modem

---

*Written by:* Kopethan
*Supervised by:* Mr. Labiod

---
