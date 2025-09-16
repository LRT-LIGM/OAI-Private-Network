# UICC / SIM Programming Commands with `program_uicc`

## Source folder

```bash
cd ~/Documents/uicc-v3.3
```

## Compilation

```bash
g++ -I. -o program_uicc program_uicc.c -lpcsclite
```

> Add `-static-libstdc++ -static-libgcc` to produce a portable version.

---

## Read basic data from the card

```bash
sudo DEBUG=y ./program_uicc
```

## Help command

```bash
sudo ./program_uicc --help
```

## Read current SIM card information

```bash
sudo ./program_uicc -p /dev/ttyUSB4
```

Displays:

* IMSI
* ICCID
* MSISDN
* PLMN
* Service Provider Name (SPN)

---

## Test SIM programmer port

List devices:

```bash
dmesg | grep ttyUSB
```

Access the port:

```bash
ls -l /dev/ttyUSB*
```

---

## Common errors

| Error                      | Cause                                  | Solution                         |
| -------------------------- | -------------------------------------- | -------------------------------- |
| `No ADM code`              | Card is protected                      | Try a different ADM code or card |
| `ATR=""`                   | SIM improperly inserted / invalid port | Check the SIM / change port      |
| `GLIBCXX_3.4.32 not found` | Incompatible binary                    | Recompile with local `g++`       |

---

## References

* OpenCells site: [https://open-cells.com/index.php/uiccsim-programing/](https://open-cells.com/index.php/uiccsim-programing/)
* Official OAI repo: [https://gitlab.eurecom.fr/oai/openairinterface5g](https://gitlab.eurecom.fr/oai/openairinterface5g)
