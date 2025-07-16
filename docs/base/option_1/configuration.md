# Configuration – Option 1 (OAI 5G SA with USRP)

This section explains how to configure the system after installation, based on the Option 1 method using a USRP B210 and physical 5G setup.

---

## 1. gNodeB Configuration (gNB)

Navigate to the folder:
```bash
cd ~/openairinterface5g/cmake_targets/ran_build/build/config
```

Edit the file `5GN78.conf` (copied and renamed during installation):
```bash
nano 5GN78.conf
```

### Important Parameters:

- **PLMN Configuration**:
  ```yaml
  plmn_list = ( { mcc = "001"; mnc = "01"; mnc_length = 2; } );
  ```

- **Radio Frequency Band**:
  Ensure you're using an allowed frequency:
  - For Band n78: stay below **3489 MHz**
  - Example:
    ```yaml
    absoluteFrequencySSB = 3404640;
    dl_absoluteFrequencyPointA = 3385560;
    ```

- **Transmission and Reception Gain**:
  ```yaml
  att_tx = 0;
  att_rx = 0;
  ```

- **USRP Serial Number**:
  Replace with your actual USRP serial:
  ```yaml
  sdr_addrs = "serial=8002036";
  ```

> ⚠️ Be careful with indentation, brackets, and semicolons.

---

## 2. Core Network Configuration

Navigate to the CN5G folder:
```bash
cd ~/OAI-5GCN-v2.0.1/docker-compose
```

Edit this file:
```bash
conf/basic_nrf_config.yaml
```

### Key Edits:
- Add the **`sd` value** in the `snssais` section
- Modify **AMF** parameters to match your gNB PLMN
- Optionally update DNS if needed

Example `snssais`:
```yaml
snssais:
  - sst: 1
    sd: "1"
```

Edit MySQL data:
```bash
nano database/oai_db2.sql
```

Add:
- IMSI, KEY, OPC
- `AccessAndMobilitySubscriptionData`
- `AuthenticationSubscription`
- `SessionManagementSubscriptionData`

> ✅ Make sure to format SQL properly (commas, escaped quotes)

---

Ready to launch the system (core + gNB) → see next page
