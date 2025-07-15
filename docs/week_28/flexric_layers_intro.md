# FlexRIC - Protocol Stack Layers Explained

This document introduces and explains the different protocol stack layers involved in FlexRIC monitoring: **MAC**, **RLC**, **PDCP**, and **GTP**. These are part of the 5G NR (and LTE) protocol stack and are responsible for handling all user and control data transferred through the RAN.

---

## 1. MAC — Medium Access Control

**Layer**: Sub-layer of Layer 2 (Data Link Layer)

### Purpose:
- Manages access to the radio channel
- Performs scheduling and resource allocation
- Handles retransmissions via HARQ

### Main Functions:
- Allocation of PRBs (Physical Resource Blocks)
- MCS (Modulation and Coding Scheme) control
- CQI/PHR feedback management
- Fast retransmissions with HARQ

### Common Metrics:
- `dl_aggr_prb`, `ul_aggr_prb`
- `phr` (Power Headroom Report)
- `mcs1`, `mcs2`
- `wb_cqi` (Wideband CQI)
- `dl_bler`, `ul_bler`

---

## 2. RLC — Radio Link Control

**Layer**: Between PDCP and MAC (Layer 2)

### Purpose:
- Provides reliable or unreliable data delivery depending on mode
- Handles segmentation and reassembly of packets

### Modes:
- AM (Acknowledged Mode): reliable with ARQ
- UM (Unacknowledged Mode): no retransmission
- TM (Transparent Mode): for broadcast

### Common Functions:
- Retransmission counters
- Number of PDUs/SDUs sent/received
- Delay and reorder buffer statistics

---

## 3. PDCP — Packet Data Convergence Protocol

**Layer**: Highest layer in Layer 2 (interface to IP)

### Purpose:
- Provides security and header compression
- Ensures packet ordering and duplication handling

### Main Functions:
- Ciphering/deciphering of data
- Header compression (ROHC)
- SN numbering, reordering

### Common Metrics:
- `txpdu_bytes`, `rxpdu_bytes`
- `txsdu_bytes`, `rxsdu_bytes`
- Reordering statistics

---

## 4. GTP — GPRS Tunneling Protocol (User Plane)

**Layer**: Transport layer in the Core Network (between gNB and UPF)

### Purpose:
- Encapsulates IP packets into tunnels for user-plane forwarding

### Main Functions:
- Tunnel creation and identification via TEID
- Carries user data from/to Internet via UPF

### Common Metrics:
- Packet count per tunnel
- Tunnel latencies or byte counters (if available)

---

## Visual Summary of Protocol Stack:

```
        ┌────────────────────────────┐
        │        IP / RRC            │  ← Application & signaling
        ├────────────────────────────┤
        │          PDCP              │  ← Encryption, compression
        ├────────────────────────────┤
        │           RLC              │  ← Segmentation, ARQ
        ├────────────────────────────┤
        │           MAC              │  ← Scheduling, HARQ, PRBs
        ├────────────────────────────┤
        │           PHY              │  ← Antennas, modulation
```

And in the core network:

```
       UE ⇄ gNB ⇄ GTP-U ⇄ UPF ⇄ Internet
```

---

## Conclusion
These layers work together to ensure reliable and efficient data transfer from the user to the internet and vice versa. FlexRIC allows you to observe real-time metrics from each layer for performance monitoring and control purposes.

