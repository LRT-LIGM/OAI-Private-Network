> **⚠️ Important Note**  
> This file contains useful information not covered in the main documentation. It is recommended for debugging.

# FlexRIC Execution Log Explanation

This document explains the meaning of important log entries during the execution of the FlexRIC near-RT RIC and the `xapp_gtp_mac_rlc_pdcp_moni` xApp. These logs indicate whether the platform is functioning correctly, which plugins are loaded, and how data subscriptions are managed.

---

## 1. Launching the xApp

```bash
cd ~/
./flexric/build/examples/xApp/c/monitor/xapp_gtp_mac_rlc_pdcp_moni -p /usr/local/lib/flexric/ -c /usr/local/etc/flexric/flexric.conf
```

```log
[UTIL]: Setting the config -c file to /usr/local/etc/flexric/flexric.conf
[UTIL]: Setting path -p for the shared libraries to /usr/local/lib/flexric/
[xAapp]: Initializing ... 
[xApp]: nearRT-RIC IP Address = 127.0.0.1, PORT = 36422
[E2 AGENT]: Opening plugin from path = /usr/local/lib/flexric/libmac_sm.so 
[E2 AGENT]: Opening plugin from path = /usr/local/lib/flexric/librc_sm.so 
[E2 AGENT]: Opening plugin from path = /usr/local/lib/flexric/libslice_sm.so 
[E2 AGENT]: Opening plugin from path = /usr/local/lib/flexric/libgtp_sm.so 
[E2 AGENT]: Opening plugin from path = /usr/local/lib/flexric/libtc_sm.so 
[E2 AGENT]: Opening plugin from path = /usr/local/lib/flexric/libkpm_sm.so 
[E2 AGENT]: Opening plugin from path = /usr/local/lib/flexric/libpdcp_sm.so 
[E2 AGENT]: Opening plugin from path = /usr/local/lib/flexric/librlc_sm.so 
[NEAR-RIC]: Loading SM ID = 142 with def = MAC_STATS_V0 
[NEAR-RIC]: Loading SM ID = 3 with def = ORAN-E2SM-RC 
[NEAR-RIC]: Loading SM ID = 145 with def = SLICE_STATS_V0 
[NEAR-RIC]: Loading SM ID = 148 with def = GTP_STATS_V0 
[NEAR-RIC]: Loading SM ID = 146 with def = TC_STATS_V0 
[NEAR-RIC]: Loading SM ID = 2 with def = ORAN-E2SM-KPM 
[NEAR-RIC]: Loading SM ID = 144 with def = PDCP_STATS_V0 
[NEAR-RIC]: Loading SM ID = 143 with def = RLC_STATS_V0 
[xApp]: DB filename = /tmp/xapp_db_1752065455917967 
 [xApp]: E42 SETUP-REQUEST tx
[xApp]: E42 SETUP-RESPONSE rx 
[xApp]: xApp ID = 7 
[xApp]: Registered E2 Nodes = 1 
Connected E2 nodes = 1
Registered node 0 ran func id = 2 
 Registered node 0 ran func id = 3 
 Registered node 0 ran func id = 142 
 Registered node 0 ran func id = 143 
 Registered node 0 ran func id = 144 
 Registered node 0 ran func id = 145 
 Registered node 0 ran func id = 146 
 Registered node 0 ran func id = 148 
 [xApp]: E42 RIC SUBSCRIPTION REQUEST tx RAN_FUNC_ID 142 RIC_REQ_ID 1 
[xApp]: SUBSCRIPTION RESPONSE rx
[xApp]: Successfully subscribed to RAN_FUNC_ID 142 
[xApp]: E42 RIC SUBSCRIPTION REQUEST tx RAN_FUNC_ID 143 RIC_REQ_ID 2 
[xApp]: SUBSCRIPTION RESPONSE rx
[xApp]: Successfully subscribed to RAN_FUNC_ID 143 
[xApp]: E42 RIC SUBSCRIPTION REQUEST tx RAN_FUNC_ID 144 RIC_REQ_ID 3 
[xApp]: SUBSCRIPTION RESPONSE rx
[xApp]: Successfully subscribed to RAN_FUNC_ID 144 
[xApp]: E42 RIC SUBSCRIPTION REQUEST tx RAN_FUNC_ID 148 RIC_REQ_ID 4 
MAC ind_msg latency = 201 μs
[xApp]: SUBSCRIPTION RESPONSE rx
[xApp]: Successfully subscribed to RAN_FUNC_ID 148 
RLC ind_msg latency = 109 μs
PDCP ind_msg latency = 47 μs
GTP ind_msg latency = 113 μs
MAC ind_msg latency = 120 μs
RLC ind_msg latency = 32 μs
PDCP ind_msg latency = 31 μs
GTP ind_msg latency = 29 μs
MAC ind_msg latency = 33 μs
RLC ind_msg latency = 31 μs
PDCP ind_msg latency = 30 μs
GTP ind_msg latency = 28 μs
MAC ind_msg latency = 36 μs
RLC ind_msg latency = 34 μs
PDCP ind_msg latency = 53 μs
GTP ind_msg latency = 58 μs
MAC ind_msg latency = 40 μs
RLC ind_msg latency = 37 μs
PDCP ind_msg latency = 55 μs
GTP ind_msg latency = 61 μs
MAC ind_msg latency = 47 μs
RLC ind_msg latency = 42 μs
PDCP ind_msg latency = 42 μs
GTP ind_msg latency = 41 μs
MAC ind_msg latency = 38 μs
RLC ind_msg latency = 39 μs
PDCP ind_msg latency = 44 μs
GTP ind_msg latency = 36 μs
MAC ind_msg latency = 36 μs
RLC ind_msg latency = 35 μs
PDCP ind_msg latency = 32 μs
GTP ind_msg latency = 30 μs
MAC ind_msg latency = 36 μs
RLC ind_msg latency = 35 μs
PDCP ind_msg latency = 54 μs
GTP ind_msg latency = 54 μs
MAC ind_msg latency = 60 μs
RLC ind_msg latency = 45 μs
PDCP ind_msg latency = 47 μs
GTP ind_msg latency = 39 μs
[xApp]: E42 RIC_SUBSCRIPTION_DELETE_REQUEST tx RAN_FUNC_ID 142 RIC_REQ_ID 1 
[xApp]: E42 SUBSCRIPTION DELETE RESPONSE rx
[xApp]: E42 RIC_SUBSCRIPTION_DELETE_REQUEST tx RAN_FUNC_ID 143 RIC_REQ_ID 2 
[xApp]: E42 SUBSCRIPTION DELETE RESPONSE rx
[xApp]: E42 RIC_SUBSCRIPTION_DELETE_REQUEST tx RAN_FUNC_ID 144 RIC_REQ_ID 3 
[xApp]: E42 SUBSCRIPTION DELETE RESPONSE rx
[xApp]: E42 RIC_SUBSCRIPTION_DELETE_REQUEST tx RAN_FUNC_ID 148 RIC_REQ_ID 4 
[xApp]: E42 SUBSCRIPTION DELETE RESPONSE rx
[xApp]: Sucessfully stopped 
Test xApp run SUCCESSFULLY
```

### Key Log Lines

| Log Line                                     | Meaning                                                                   |
| -------------------------------------------- | ------------------------------------------------------------------------- |
| `[UTIL]: Setting the config ...`             | The config file and plugin path are correctly loaded.                     |
| `[xAapp]: Initializing ...`                  | xApp is starting up.                                                      |
| `[xApp]: nearRT-RIC IP Address = 127.0.0.1`  | xApp will connect to the RIC at loopback address (local machine).         |
| `[E2 AGENT]: Opening plugin from path = ...` | Each RAN SM (Service Model) plugin is loaded from the FlexRIC lib folder. |
| `[NEAR-RIC]: Loading SM ID = ...`            | The RIC core accepts the SMs that the xApp plans to use.                  |
| `[xApp]: DB filename = /tmp/xapp_db_...`     | A temporary SQLite DB file is created to store metric data.               |
| `[xApp]: E42 SETUP-REQUEST tx`               | The xApp initiates a connection with the RIC.                             |
| `[xApp]: E42 SETUP-RESPONSE rx`              | The RIC responded — successful setup.                                     |
| `[xApp]: Registered E2 Nodes = 1`            | The RIC has at least one connected gNB/UE.                                |
| `[xApp]: SUBSCRIPTION RESPONSE rx`           | The xApp has successfully subscribed to a given SM.                       |

---

## 2. Metric Collection

After successful subscriptions, periodic data collection begins. Each line corresponds to a received indication message:

### Example:

```log
MAC ind_msg latency = 201 μs
RLC ind_msg latency = 109 μs
PDCP ind_msg latency = 47 μs
GTP ind_msg latency = 113 μs
```

Each log entry shows:

- The **Service Model (SM)** from which the indication comes: `MAC`, `RLC`, `PDCP`, `GTP`, etc.
- The **latency in microseconds** to receive and process the message.

### Interpretation:

These low-latency values (<200 μs) indicate efficient processing and a live data stream from the gNB through E2 interface.

---

## 3. Graceful Shutdown

```log
[xApp]: RIC_SUBSCRIPTION_DELETE_REQUEST tx ...
[xApp]: SUBSCRIPTION DELETE RESPONSE rx
[xApp]: Successfully stopped
Test xApp run SUCCESSFULLY
```

The xApp unsubscribed from each SM cleanly and exited without error.

---

## 4. Running the Near-RT RIC

```bash
cd ~/
./flexric/build/examples/ric/nearRT-RIC
```

**The log**

```log
[UTIL]: Setting the config -c file to /usr/local/etc/flexric/flexric.conf
[UTIL]: Setting path -p for the shared libraries to /usr/local/lib/flexric/
[NEAR-RIC]: nearRT-RIC IP Address = 127.0.0.1, PORT = 36421
[NEAR-RIC]: Initializing 
[NEAR-RIC]: Loading SM ID = 142 with def = MAC_STATS_V0 
[NEAR-RIC]: Loading SM ID = 3 with def = ORAN-E2SM-RC 
[NEAR-RIC]: Loading SM ID = 145 with def = SLICE_STATS_V0 
[NEAR-RIC]: Loading SM ID = 148 with def = GTP_STATS_V0 
[NEAR-RIC]: Loading SM ID = 146 with def = TC_STATS_V0 
[NEAR-RIC]: Loading SM ID = 2 with def = ORAN-E2SM-KPM 
[NEAR-RIC]: Loading SM ID = 144 with def = PDCP_STATS_V0 
[NEAR-RIC]: Loading SM ID = 143 with def = RLC_STATS_V0 
[iApp]: Initializing ... 
[iApp]: nearRT-RIC IP Address = 127.0.0.1, PORT = 36422
[NEAR-RIC]: Initializing Task Manager with 2 threads 
[E2AP]: E2 SETUP-REQUEST rx from PLMN   1. 1 Node ID 3584 RAN type ngran_gNB
[NEAR-RIC]: Accepting RAN function ID 2 with def = ORAN-E2SM-KPM 
[NEAR-RIC]: Accepting RAN function ID 3 with def = ORAN-E2SM-RC 
[NEAR-RIC]: Accepting RAN function ID 142 with def = MAC_STATS_V0 
[NEAR-RIC]: Accepting RAN function ID 143 with def = RLC_STATS_V0 
[NEAR-RIC]: Accepting RAN function ID 144 with def = PDCP_STATS_V0 
[NEAR-RIC]: Accepting RAN function ID 145 with def = SLICE_STATS_V0 
[NEAR-RIC]: Accepting RAN function ID 146 with def = TC_STATS_V0 
[NEAR-RIC]: Accepting RAN function ID 148 with def = GTP_STATS_V0 
[iApp]: E42 SETUP-REQUEST rx
[iApp]: E42 SETUP-RESPONSE tx
[iApp]: SUBSCRIPTION-REQUEST RAN_FUNC_ID 142 RIC_REQ_ID 1 tx 
[iApp]: SUBSCRIPTION-REQUEST RAN_FUNC_ID 143 RIC_REQ_ID 2 tx 
[iApp]: SUBSCRIPTION-REQUEST RAN_FUNC_ID 144 RIC_REQ_ID 3 tx 
[iApp]: SUBSCRIPTION-REQUEST RAN_FUNC_ID 148 RIC_REQ_ID 4 tx 
[NEAR-RIC]: SUBSCRIPTION DELETE REQUEST tx RAN FUNC ID 142 RIC_REQ_ID 1021 
[iApp]: RIC_SUBSCRIPTION_DELETE_REQUEST tx RIC_REQ_ID 1021 
[iApp]: RIC_SUBSCRIPTION_DELETE_RESPONSE tx RAN_FUNC_ID 142 RIC_REQ_ID 1 
[NEAR-RIC]: SUBSCRIPTION DELETE REQUEST tx RAN FUNC ID 143 RIC_REQ_ID 1022 
[iApp]: RIC_SUBSCRIPTION_DELETE_REQUEST tx RIC_REQ_ID 1022 
[iApp]: RIC_SUBSCRIPTION_DELETE_RESPONSE tx RAN_FUNC_ID 143 RIC_REQ_ID 2 
[NEAR-RIC]: SUBSCRIPTION DELETE REQUEST tx RAN FUNC ID 144 RIC_REQ_ID 1023 
[iApp]: RIC_SUBSCRIPTION_DELETE_REQUEST tx RIC_REQ_ID 1023 
[iApp]: RIC_SUBSCRIPTION_DELETE_RESPONSE tx RAN_FUNC_ID 144 RIC_REQ_ID 3 
[NEAR-RIC]: SUBSCRIPTION DELETE REQUEST tx RAN FUNC ID 148 RIC_REQ_ID 1024 
[iApp]: RIC_SUBSCRIPTION_DELETE_REQUEST tx RIC_REQ_ID 1024 
[iApp]: RIC_SUBSCRIPTION_DELETE_RESPONSE tx RAN_FUNC_ID 148 RIC_REQ_ID 4 
[E2AP]: SCTP_SHUTDOWN_EVENT 
[NEAR-RIC]: Removing E2 Node MCC 1 MNC 1 NB_ID 3584 
^C
[NEAR-RIC]: Abruptly ending with signal number = 2
```

### Key Events

| Log Line                               | Meaning                                                  |
| -------------------------------------- | -------------------------------------------------------- |
| `[NEAR-RIC]: Initializing`             | The RIC core starts.                                     |
| `Loading SM ID = ...`                  | Loads supported SMs that xApps or gNB may use.           |
| `E2 SETUP-REQUEST rx from PLMN 1.1`    | A gNB (e.g. from OAI) has connected to the RIC via E2AP. |
| `Accepting RAN function ID ...`        | Confirms support for a specific SM from that gNB.        |
| `SUBSCRIPTION-REQUEST RAN_FUNC_ID ...` | Receives subscription from an xApp.                      |
| `SUBSCRIPTION DELETE REQUEST tx`       | The xApp unsubscribed or crashed.                        |
| `SCTP_SHUTDOWN_EVENT`                  | SCTP connection closed (e.g. gNB or xApp disconnected).  |

---

## Conclusion

This log confirms:

- RIC and xApp start and communicate properly.
- All required SMs (MAC, RLC, PDCP, GTP, etc.) are loaded.
- Subscriptions to the gNB are successful.
- Data is being received and stored.
- The application shuts down gracefully.

---
