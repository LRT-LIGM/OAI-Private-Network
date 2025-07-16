# 01 - Quectel Modem Configuration (RM500Q)

## General Information

- **Modem**: Quectel RM500Q (via USB)
- **Operation Mode**: QMI (managed using `quectel-CM`)
- **Detected Firmware Version**: `RM520NGLAAR03A04M4G`
- **Driver**: `qmi_wwan`
- **Network Interface**: `wwan0`

## Tools Used

- `quectel-CM`
- `qmicli`
- `ifconfig`, `ip`, `iptables`, `tcpdump`

## Configuration Steps

### 1. Launch the `quectel-CM` manager

```bash
cd ~/Documents/quectel/quectel-CM/out
sudo ./quectel-CM -s oai
```

* The `-s oai` option sets the APN.
* The tool automatically detects `wwan0`.

### 2. Check connection status

```bash
sudo qmicli -d /dev/cdc-wdm1 --wds-get-current-settings
```

**Example output:**

```
IPv4 address: 10.10.0.2
IPv4 subnet mask: 255.255.255.252
IPv4 gateway address: 10.10.0.1
IPv4 primary DNS: 172.21.3.100
```

### 3. IP Configuration

> Automatically handled by the `udhcpc` service inside `quectel-CM`:

```
udhcpc: lease of 10.10.0.2 obtained
```

### 4. Route Check

```bash
ip route | grep wwan0
```

Expected output:

```
default via 10.10.0.1 dev wwan0
10.10.0.0/30 dev wwan0 proto kernel scope link src 10.10.0.2
```

## Issues Observed

* `mmcli` does not detect the modem (expected in QMI mode)
* `ping 8.8.8.8` fails despite the `Attached` status and 5G SA connection
* DNS server `172.21.3.100` doesn’t respond to queries (`dig` fails)

## Verified

* `wwan0` interface is up and has IP
* Route is correctly configured
* Modem status is `Attached` with 5G SA
* Ping to the gateway (`10.10.0.1`) is successful

## Remaining Issues

* No internet access via `wwan0` (no ping to 8.8.8.8, no DNS resolution)
* No visible traffic in `tcpdump` for external addresses

---
