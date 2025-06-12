# Essential AT Commands for Testing a 5G Module (e.g. Quectel RM500Q)

This document gathers useful AT commands to interact with a 5G modem in a testing environment with OpenAirInterface.

---

## Launch minicom

```bash
sudo minicom -D /dev/ttyUSB2
```

## Basic commands

```bash
AT                          → Check if the module responds (should return OK)
ATE0                        → Disable command echo (optional)
AT+CPIN?                    → Check SIM card status (should display +CPIN: READY)
AT+COPS?                    → Check the automatically selected operator
AT+COPS=0                   → Force automatic operator selection
AT+COPS=1,2,"00101"         → Force registration on PLMN 00101 (OAI)
```

---

## Network information

```bash
AT+CREG?                    → Check network registration
AT+CEREG?                   → Same for EPS network (LTE/5G)
AT+QENG="servingcell"      → Display cell info (RSRP, SINR, etc.)
AT+CSQ                      → Received signal strength (0-31) and BER
```

---

## Radio mode configuration

```bash
AT+QCFG="nwscanmode"       → Set scan mode (2 = LTE only, 3 = NR5G only)
AT+QCFG="iotopmode"        → Set preferred 5G mode (e.g. 1 = SA)
AT+QNWPREFCFG="mode_pref"  → Check preferred modes (LTE, 5G...)
AT+QNWPREFCFG="nr5g_band"  → List or configure enabled bands (e.g. 78)
```

---

## Cleanup / Reset commands

```bash
AT+CFUN=1,1                → Reboot the module (equivalent to reset)
AT+QPOWD=1                 → Properly shut down the module
```

---

## Useful debug commands

```bash
AT+CCLK?                   → Check real-time clock (useful for logs)
AT+CPIN?                   → Check SIM status
AT+QENG="servingcell"      → Always useful for network status
```

---

## Example of a typical test sequence

```bash
AT
AT+CPIN?
AT+COPS=0
AT+CREG?
AT+QENG="servingcell"
```

---

## References

* [Quectel RM500Q AT Manual](https://www.quectel.com/product/5g-rm500q-series/)