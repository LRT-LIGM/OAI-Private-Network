# Successful SIM Programming via `program_uicc`

This session documents a successful programming of a SIM card using the `program_uicc` binary in a 5G test environment (OpenAirInterface).

---

## Session Information

* **Command used**:

```bash
sudo ./program_uicc \
  --adm 12345678 \
  --imsi 001010000000005 \
  --isdn 00000001 \
  --acc 0001 \
  --key 6874736969202073796d4b2079650a73 \
  --opc 504f20634f6320504f50206363500a4f \
  --spn "OpenCells01" \
  --authenticate \
  --noreadafter
```

## Result:

```bash
Existing values in USIM
ICCID: 89330061100000000022
WARNING: iccid luhn encoding of last digit not done 
USIM IMSI: 001010000000002
PLMN selector: : 0x00f1107c
Operator Control PLMN selector: : 0x00f1107c
Home PLMN selector: : 0x00f1107c
USIM MSISDN: 00000002
USIM Service Provider Name: OpenAirInterface

Setting new values
Succeeded to authentify with SQN: 2752
set HSS SQN value as: 2784
```

---

## Programmed Parameters

| Element  | Value                              |
| -------- | ---------------------------------- |
| IMSI     | `001010000000005`                  |
| MSISDN   | `00000001`                         |
| ACC      | `0001`                             |
| Key K    | `6874736969202073796d4b2079650a73` |
| OPC      | `504f20634f6320504f50206363500a4f` |
| SPN      | `OpenCells01`                      |
| ADM Code | `12345678`                         |

---

## Result

* **Authentication successful** (`Succeeded to authentify`)
* SQN read from the SIM: `2752`
* SQN updated in the SIM: `2784`
* No blocking issue related to ADM code

---

## Notes

* This SIM card can now be registered in the AMF by adding the IMSI and keys into the `oai_db` database.
* The `--noreadafter` option prevents **re-reading** the SIM after writing (useful for batch programming).
