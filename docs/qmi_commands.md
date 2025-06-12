# Commandes QMI utilisées

Ce document liste et explique toutes les commandes `qmicli` et associées utilisées lors du projet de réseau privé 5G avec le modem Quectel.

---

## Signal & Réseau

### Obtenir la puissance du signal

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-get-signal-strength
````

> Affiche le RSSI, SINR, ECIO... Ex : `Network 'umts': '-70 dBm'`

---

### Scanner les réseaux disponibles

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-network-scan
```

> Affiche les réseaux détectés avec leur MCC/MNC, status (`available`, `forbidden`, etc.) et technologie (RAT : LTE, UMTS...).

---

### Vérifier l’état de la connexion réseau

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-get-serving-system
```

> Permet de voir si le modem est enregistré, s’il est en roaming, etc.

---

## Statut SIM et carte

### Vérifier l’état de la carte SIM

```bash
sudo qmicli -d /dev/cdc-wdm1 --uim-get-card-status
```

> Ex : `SIMStatus: SIM_READY`, `PIN2 state: enabled-not-verified`

---

### Déverrouiller la carte SIM (PIN1 / PIN2)

```bash
sudo qmicli -d /dev/cdc-wdm1 --uim-verify-pin="0000"
```

> Utilisé si la carte SIM est protégée par un code PIN.

---

## Interfaces réseau

### Remettre l’interface wwan0 en ligne

```bash
sudo ip link set wwan0 up
```

---

### Tenter d’obtenir une IP via DHCP

```bash
sudo udhcpc -i wwan0
```

> Peut entrer en boucle si le modem n’est pas attaché au réseau.

---

## Connexion au réseau avec `quectel-CM`

```bash
sudo ./quectel-CM -s ebouygtel.com
```

> Lance la connexion à l’APN Bouygues. À faire uniquement si la SIM est autorisée.

---

## Réinitialiser le modem (si problème USB)

```bash
sudo usb_modeswitch -v 2c7c -p 0801 -R
```

> Pour réinitialiser le périphérique USB en cas de non-détection.

---

📌 **Remarques** :

* L’interface QMI est accessible via `/dev/cdc-wdm1`.
* En cas de changement de port USB ou reset : revérifier le device.

---