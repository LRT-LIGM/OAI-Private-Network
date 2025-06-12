# Commandes AT essentielles pour tester un module 5G (ex. : Quectel RM500Q)

Ce document regroupe les commandes AT utiles pour interagir avec un modem 5G dans un environnement de test avec OpenAirInterface.

---

## Lancer minicom
```bash
sudo minicom -D /dev/ttyUSB2
```

## Commandes de base

```text
AT                          → Vérifie si le module répond (doit renvoyer OK)
ATE0                        → Désactive l’écho des commandes (facultatif)
AT+CPIN?                    → Vérifie l’état de la carte SIM (doit afficher +CPIN: READY)
AT+COPS?                    → Vérifie l’opérateur sélectionné automatiquement
AT+COPS=0                   → Force la sélection automatique de l’opérateur
AT+COPS=1,2,"00101"         → Force l’enregistrement sur le PLMN 00101 (OAI)
```

---

## Informations de réseau

```text
AT+CREG?                    → Vérifie l’enregistrement sur le réseau
AT+CEREG?                   → Même chose pour le réseau EPS (LTE/5G)
AT+QENG="servingcell"      → Affiche les infos sur la cellule (RSRP, SINR, etc.)
AT+CSQ                      → Niveau de signal reçu (0-31) et BER
```

---

## Configuration du mode radio

```text
AT+QCFG="nwscanmode"       → Définit le mode de scan (2 = LTE only, 3 = NR5G only)
AT+QCFG="iotopmode"        → Définit le mode 5G préféré (ex. : 1 = SA)
AT+QNWPREFCFG="mode_pref"  → Vérifie les modes préférés (LTE, 5G...)
AT+QNWPREFCFG="nr5g_band"  → Liste ou configure les bandes activées (ex. 78)
```

---

## Commandes de nettoyage / reset

```text
AT+CFUN=1,1                → Redémarre le module (équivalent reset)
AT+QPOWD=1                 → Éteint proprement le module
```

---

## Commandes utiles pour debug

```text
AT+CCLK?                   → Vérifie l’horloge temps réel (utile pour logs)
AT+CPIN?                   → Vérifie l’état SIM
AT+QENG="servingcell"      → Toujours utile pour le statut réseau
```

---

## Exemple de séquence typique de test

```text
AT
AT+CPIN?
AT+COPS=0
AT+CREG?
AT+QENG="servingcell"
```

---

## Références
- [Manuel AT Quectel RM500Q](https://www.quectel.com/product/5g-rm500q-series/)
