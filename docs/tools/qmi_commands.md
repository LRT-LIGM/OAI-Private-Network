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

> Displays detected networks with their MCC/MNC, status (`available`, `forbidden`, etc.), and technology (RAT: LTE, UMTS...).

---

### Check network connection status

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-get-serving-system
```

> Shows whether the modem is registered, in roaming, etc.

---

## SIM & Card Status

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

> Used if the SIM card is protected with a PIN code.

---

## Network Interfaces

### Bring the `wwan0` interface up

```bash
sudo ip link set wwan0 up
```

---

### Try to obtain an IP via DHCP

```bash
sudo udhcpc -i wwan0
```

> May loop if the modem is not attached to the network.

---

## Connect to the network using `quectel-CM`

```bash
sudo ./quectel-CM -s ebouygtel.com
```

> Starts the connection to the Bouygues APN. Only do this if the SIM is authorized.

---

## Reset the modem (if USB issues occur)

```bash
sudo usb_modeswitch -v 2c7c -p 0801 -R
```

> Resets the USB device in case of non-detection.

---

📌 **Notes**:

* The QMI interface is accessible via `/dev/cdc-wdm1`.
* If the USB port changes or a reset is performed: recheck the device.