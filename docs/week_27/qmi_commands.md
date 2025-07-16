> **⚠️ Important Note**  
> This file contains useful information not covered in the main documentation. It is recommended for troubleshooting.

# QMI Commands Used

This document lists and explains all `qmicli` and related commands used during the 5G private network project with the Quectel modem.

---

## Signal & Network

### Get signal strength

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-get-signal-strength
```

> Displays RSSI, SINR, ECIO... Example: `Network 'umts': '-70 dBm'`

---

### Scan available networks

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-network-scan
```

> Lists detected networks with their MCC/MNC, status (`available`, `forbidden`, etc.), and technology (RAT: LTE, UMTS...).

---

### Check network connection status

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-get-serving-system
```

> Shows if the modem is registered, roaming, etc.

---

## SIM and Card Status

### Check SIM card status

```bash
sudo qmicli -d /dev/cdc-wdm1 --uim-get-card-status
```

> Example: `SIMStatus: SIM_READY`, `PIN2 state: enabled-not-verified`

---

### Unlock SIM card (PIN1 / PIN2)

```bash
sudo qmicli -d /dev/cdc-wdm1 --uim-verify-pin="0000"
```

> Use if the SIM card is protected with a PIN code.

---

## Network Interfaces

### Bring `wwan0` interface up

```bash
sudo ip link set wwan0 up
```

---

### Try to obtain an IP address via DHCP

```bash
sudo udhcpc -i wwan0
```

> May loop if the modem is not attached to the network.

---

## Network Connection using `quectel-CM`

```bash
sudo ./quectel-CM -s ebouygtel.com
```

> Starts the connection to the Bouygues APN. Only do this if the SIM is authorized.

---

## Reset the modem (in case of USB issue)

```bash
sudo usb_modeswitch -v 2c7c -p 0801 -R
```

> Used to reset the USB device in case it is not detected.

---

**Notes**:

* The QMI interface is accessed via `/dev/cdc-wdm1`.
* If USB port changes or a reset occurs, verify the device again.

---