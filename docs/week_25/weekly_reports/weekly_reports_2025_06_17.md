> **⚠️ Important Note**  
> This file contains useful information not covered in the main documentation. It is recommended for debugging.

# Week of June 17–21, 2025 – OAI 5G Internship Progress Report

## Main Objective

Test the connection of a UE (modem or smartphone) to a 5G Standalone (SA) infrastructure using the OpenAirInterface stack:

* Launch the gNodeB (`nr-softmodem`)
* Connect the AMF via Docker
* Verify UE attachment and GUTI assignment

---

## Work Completed

### 1. gNodeB Launch

* Launched `nr-softmodem` in SA mode on band **n78 (3619.2 MHz)**:

  ```bash
  sudo ./nr-softmodem -O ...gnb.sa.band78.fr1.106PRB.usrpb210.conf --continuous-tx -E
  ```

  * USRP B210 recognized (RX/TX OK, frequency and gains properly configured)
  * Continuous transmission enabled (`--continuous-tx`)

### 2. AMF Status

* AMF container running and healthy:

  ```bash
  docker ps | grep amf → healthy
  ```
* NGAP communication established between gNB and AMF (SCTP port 38412)

### 3. UE Attachment Test

* Partial registration detected:

  * `5GMM-REGISTERED` visible on AMF side
  * SIM card IMSI correctly received
  * But **no GUTI assigned** (empty field)
* `nr-softmodem` logs → multiple uplink errors:

  * `UL Failure`, `RSRP = 0`, `out-of-sync`
  * UE seems **not transmitting or not being properly received**

### 4. Additional Key Result

* AMF shows a UE connection with IMSI `001010000059463` → **attachment observed**

### 5. Optimization Attempts

* Added `--tune-offset` to reduce DC noise
* Lowered `min_rxtxtime` to 8
* Physically placed UE close to the antenna

---

## Analysis

| Component     | Status  | Observations                          |
| ------------- | ------- | ------------------------------------- |
| gNodeB        | OK      | Connected to AMF, active transmission |
| AMF           | OK      | Running, regular NRF heartbeat        |
| UE (SIM card) | Partial | IMSI received, but no GUTI assigned   |
| Radio Layer   | KO      | No uplink data received from UE       |

> GUTI (Globally Unique Temporary Identifier): a temporary identifier assigned to a UE upon registration to a 5G network. It avoids reusing the IMSI every time.

---

## Next Steps

* Verify **SIM card configuration** (KEY, OPC, IMSI)
* Confirm **SA mode support** on the UE used
* Continue analyzing AMF logs:

  ```bash
  docker logs oai-amf -f
  ```
* Test with another UE or SIM if needed
* Try using `nr-uesoftmodem` in `--rfsim` mode

---

*Written by:* Kopethan
*Supervised by:* Mr. Labiod

---
