# Commandes de programmation UICC / SIM avec `program_uicc`

## Dossier source
```bash
cd ~/Documents/uicc-v3.3
```

## Compilation
```bash
g++ -I. -o program_uicc program_uicc.c -lpcsclite
```
> Ajoute `-static-libstdc++ -static-libgcc` pour une version portable.

---

## Reads basic data in the card
```bash
sudo DEBUG=y ./program_uicc
```

## Pouir aider
```bash
sudo ./program_uicc --help
```

## Lire les informations actuelles de la carte SIM
```bash
sudo ./program_uicc -p /dev/ttyUSB4
```

Affiche :
- IMSI
- ICCID
- MSISDN
- PLMN
- Service Provider Name (SPN)

---

## Tester le port du programmateur SIM
Lister les périphériques :
```bash
dmesg | grep ttyUSB
```

Accès au port :
```bash
ls -l /dev/ttyUSB*
```

---

## Erreurs courantes

| Erreur | Cause | Solution |
|--------|-------|----------|
| `No ADM code` | Carte protégée | Essayer un autre ADM ou carte |
| `ATR=""` | SIM mal insérée / port invalide | Vérifie / change de port |
| `GLIBCXX_3.4.32 not found` | Binaire incompatible | Recompiler avec `g++` local |

---

## Références
- Site OpenCells : https://open-cells.com/index.php/uiccsim-programing/
- Repo OAI officiel : https://gitlab.eurecom.fr/oai/openairinterface5g
