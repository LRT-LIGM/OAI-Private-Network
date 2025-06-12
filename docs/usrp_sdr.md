# Using SDR USRP with OAI

This page documents the use of the **USRP B210** SDR device in the context of the private 5G network project with OpenAirInterface.

## Objective

Enable radio signal transmission and reception via the USRP to:

* Test the PHY layer with the `gNB`
* Verify the radio link with a software or physical `UE` (e.g. Quectel module)

## Preparation

### 1. Install UHD drivers

```bash
sudo apt install libuhd-dev uhd-host
sudo uhd_images_downloader
```

### 2. Verify USRP connection

```bash
uhd_find_devices
uhd_usrp_probe
```

### 3. Launch the gNB with USRP

```bash
cd ~/openairinterface5g/cmake_targets/ran_build/build
sudo ./nr-softmodem -O path/to/gnb-sa.conf
```

Ensure that the following section in the config file is properly defined:

```ini
    rf_config:
      device_args: "type=b200"
      ...
```

## Troubleshooting

* **“Device not found” error**: check USB 3.0 cable, power supply, or `udev` permissions.
* **Weak RX signal**: check frequency, gain, and connected antennas.

> If the USRP has issues, try changing the USB port on your PC.

---

> ⚠️ The USRP must be correctly detected before launching `softmodem`.

## Useful References

* [Official UHD Guide](https://files.ettus.com/manual/)
* [OAI RF Configuration](https://gitlab.eurecom.fr/oai/openairinterface5g/-/wikis)

