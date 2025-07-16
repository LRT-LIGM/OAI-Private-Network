# FlexRIC xApp – Extendable / Missing Metrics

This document lists potential metrics that are not currently collected by the xApp but could be added by extending the FlexRIC Service Models.

---

## RRC and Control Plane Metrics

- `rrc_state`: UE connection state (IDLE, CONNECTED, SUSPENDED)
- `setup_requests`: Number of RRC Connection Setup Requests
- `paging_messages`: Count of paging transmissions
- `connection_failures`: Failed setups or drops

---

## Mobility Metrics

- `handover_count`: Number of handovers per UE
- `ho_success_rate`: Handover success vs failure
- `reselection_events`: Cell reselection counters
- `cell_id`: Serving/target cell ID tracking

---

## Location and Topology Data

- `cell_global_id`: CGI for UE-cell mapping
- `sector_id`: Sector or beam ID for spatial analysis
- `gps_location`: (if integrated with UE simulator or drive-test)

---

## Bearer-Level QoS Stats

- `srb_id`, `drb_id`: Stats by signaling/data bearer
- `delay`, `jitter`, `packet_loss` per bearer
- `qci` or `5qi`: Quality class for each bearer

---

## Latency and Timing

- `e2e_latency`: Measured from PDCP-to-GTP
- `jitter`: Packet inter-arrival variation
- `processing_delay`: Per layer or interface

---

## Power and Energy Metrics

- `drx_cycle`: Power saving mode activation
- `power_headroom_over_time`: Trend in reported PHR
- `battery_status` (if UE supports feedback)

---

## Application-Level KPIs (Custom KPMs)

- `video_qoe`: Bitrate, buffering, stall duration
- `voip_mos`: Mean Opinion Score for call quality
- `throughput_per_app`: If apps are tagged/classified

---

## Host/System Performance

- `cpu_usage`: Per NF (UPF, AMF, SMF, RIC)
- `memory_usage`: Real-time memory for containers
- `interface_stats`: Linux NIC stats from host

---

## Implementation Note

These metrics can be added by:
- Extending existing SMs in C
- Creating new SMs for FlexRIC
- Using auxiliary tools like host-based collectors or UE simulators
