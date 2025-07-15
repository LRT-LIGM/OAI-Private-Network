# Configuration Files – OAI 5G SA and FlexRIC

This section explains the key configuration files used in our deployment: `flexric.conf`, gNB parameters, and runtime database location.

---

## 1. `flexric.conf` File (used by Near-RT RIC and xApps)

This file is essential for both the Near-RT RIC and xApp operation. Below is a breakdown of the relevant parts:

### ➤ Active gNBs

```ini
Active_gNBs = ( "gNB-OAI" );
```

Defines which gNB to monitor.

### ➤ PLMN and NR Cell Identity

```ini
gNB_ID    =  0xe00;
gNB_name  =  "gNB-OAI";
plmn_list = ({ mcc = 001; mnc = 01; mnc_length = 2; });
nr_cellid = 12345678L;
```

### ➤ Frequency and Bandwidth

```ini
absoluteFrequencySSB = 640896;
dl_frequencyBand     = 78;
dl_carrierBandwidth  = 106;
ul_frequencyBand     = 78;
ul_carrierBandwidth  = 106;
```

### ➤ RAN Configuration

This includes:

- TDD pattern
- PUSCH/PUSCH targets
- Initial BWP
- SSB parameters
- Power and gain values

### ➤ Network Interfaces

```ini
NETWORK_INTERFACES : {
    GNB_IPV4_ADDRESS_FOR_NG_AMF = "0.0.0.0/24";
    GNB_IPV4_ADDRESS_FOR_NGU    = "0.0.0.0/24";
    GNB_PORT_FOR_S1U            = 2152;
};
```

Used by the gNB to bind interfaces.

### ➤ E2 Agent Section

```ini
e2_agent = {
  near_ric_ip_addr = "127.0.0.1";
  sm_dir = "/usr/local/lib/flexric/";
};
```

Defines where to find FlexRIC Shared Libraries (plugins for MAC, PDCP, GTP, etc).

---

## 2. Runtime Generated SQLite DB

Each run of xApp creates a SQLite DB in `/tmp/`, e.g.:

```
/tmp/xapp_db_1752065455917967
```

It contains tables like:

- `MAC_UE`
- `PDCP_bearer`
- `GTP_NGUT`
- `RLC_bearer`

This file is queried using:

```bash
sqlite3 /tmp/xapp_db_*.db
```

---

## 3. Debug Tips

- If xApp fails with `CHECK constraint failed: phr > -24 AND phr < 41`, it may be due to bad or missing input data.
- This constraint is enforced implicitly, even if not visible in `sqlite3_wrapper.c`.
- Use `PRAGMA table_info(MAC_UE);` to explore schema.

---
