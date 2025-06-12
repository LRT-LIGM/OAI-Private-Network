# Utilisation du SDR USRP avec OAI

Cette page documente l'utilisation du périphérique SDR **USRP B210** dans le cadre du projet de réseau privé 5G avec OpenAirInterface.

## Objectif

Permettre la transmission et la réception des signaux radio via l’USRP pour :

- Tester la couche PHY avec le `gNB`
- Vérifier le lien radio avec un `UE` logiciel ou physique (par exemple module Quectel)

## Préparation

### 1. Installation des drivers UHD

```bash
sudo apt install libuhd-dev uhd-host
sudo uhd_images_downloader
```

### 2. Vérification de la connexion USRP

```bash
uhd_find_devices
uhd_usrp_probe
```

### 3. Lancement du gNB avec l’USRP

```bash
cd ~/openairinterface5g/cmake_targets/ran_build/build
sudo ./nr-softmodem -O path/to/gnb-sa.conf
```

Assurez-vous que la section suivante du fichier de config est bien définie :

```ini
    rf_config:
      device_args: "type=b200"
      ...
```

## Résolution d’erreurs

* **Erreur “Device not found”** : vérifier câble USB 3.0, alimentation, ou permissions `udev`.
* **Signal RX faible** : vérifier fréquence, gain, et antennes connectées.

> Si USRP pousse probrème, essaye de le changer le port USB dans votre PC.

---

> ⚠️ L’USRP doit être reconnu correctement avant de lancer le `softmodem`.

## Références utiles

* [Guide officiel UHD](https://files.ettus.com/manual/)
* [Configuration RF OAI](https://gitlab.eurecom.fr/oai/openairinterface5g/-/wikis)
