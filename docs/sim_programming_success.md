# Programmation SIM réussie via `program_uicc`

Cette session documente une programmation réussie d’une carte SIM avec le binaire `program_uicc` dans un environnement de test 5G (OpenAirInterface).

---

## Informations de la session

- **Commande utilisée** :
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

## Résultat :
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

## Paramètres programmés

| Élément        | Valeur                                      |
|----------------|----------------------------------------------|
| IMSI           | `001010000000005`                            |
| MSISDN         | `00000001`                                   |
| ACC            | `0001`                                       |
| Clé K          | `6874736969202073796d4b2079650a73`           |
| OPC            | `504f20634f6320504f50206363500a4f`           |
| SPN            | `OpenCells01`                                |
| Code ADM       | `12345678`                                   |

---

## Résultat

- **Authentification réussie** (`Succeeded to authentify`)
- SQN lu depuis la carte : `2752`
- SQN mis à jour dans la SIM : `2784`
- Aucun blocage lié au code ADM

---

## Notes

- Cette carte peut maintenant être enregistrée côté AMF en ajoutant l’IMSI et les clés dans la base de données `oai_db`.
- Le champ `--noreadafter` permet de **ne pas relire** la SIM après écriture (utile en batch).

