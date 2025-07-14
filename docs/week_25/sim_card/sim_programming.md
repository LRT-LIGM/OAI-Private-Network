# Week of June 17–21, 2025 – Programming the Sysmocom SIM Card

## Objective

Configure a programmable SIM card (Sysmocom) for use with a gNodeB (OpenAirInterface) by setting the IMSI, KEY, OPC, ISDN, ACC, SPN fields, and verifying AKA authentication functionality.

---

## Hardware Used

* Sysmocom SIM Card (ICCID: 8988211000001037921f)
* USB SmartCard Reader (PCSC compatible)
* USB Serial Adapter (PL2303)
* Recognized port: `/dev/ttyUSB0`
* Software: `program_uicc` (uicc-v3.3 from OpenCells)

---

## Steps Completed

### 🔹 Environment Setup

* Installed `libccid`, `pcscd`, `pcsc-tools`
* Patched the `program_uicc.c` source code to fix segmentation faults
* Recompiled:

  ```bash
  make clean && make
  ```

### 🔹 Read Tests

* ICCID read successfully: `8988211000001037921f`
* IMSI read failed → file missing or access protected

### 🔹 Programming Attempts

* ADM codes tested: `00000000`, `12345678`, `11111111`, `22222222`, `68594154`, etc.
* All returned:

  * `9840` → Security status not satisfied
  * `6983` → Authentication method blocked
* Conclusion: **Correct ADM code is required** to program sensitive fields

### 🔹 AKA Authentication

* Tests run with `KEY` and `OPC` → successful authentication ✅

  ```
  Succeeded to authentify with SQN: 832
  set HSS SQN value as: 864
  ```

---

## Current Results

* SIM card responds to standard commands
* IMSI writing is not possible without ADM code
* Network authentication (AKA) works successfully

---

## Next Actions

* Contact Mr. Labiod to obtain the **ADM code** for the SIM (ICCID: 8988211000001037921f)
* Repeat full test with correct ADM code when available

---

*Written by:* Kopethan
*Supervised by:* Mr. Labiod

---
