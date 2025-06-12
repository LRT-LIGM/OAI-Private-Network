# Installation – Préparation de l’environnement

Cette section décrit toutes les étapes nécessaires pour installer les outils utilisés dans le projet OAI Private Network.

---

## 1. Dépendances de base

Avant de cloner le projet, installer les paquets suivants :

```bash
sudo apt update && sudo apt install -y \
  git cmake build-essential \
  python3 python3-pip python3-dev \
  libboost-all-dev libsctp-dev lksctp-tools \
  libssl-dev libffi-dev libconfig++-dev \
  net-tools iputils-ping \
  usbutils pciutils
```

---

## 2. Installation de Docker et Docker Compose

```bash
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sudo usermod -aG docker $USER
```

> ⚠️ Redémarrer votre session pour appliquer les droits Docker.

---

## 3. Clonage du projet

```bash
git clone https://github.com/OPENAIRINTERFACE/openairinterface5g.git
cd openairinterface5g
```

---

## 4. Compilation du gNodeB

```bash
cd cmake_targets
./build_oai -I --gNB
```

> Si pas de SDR, utiliser `--rfsim` pour simuler la radio :

```bash
sudo ./nr-softmodem -O <chemin_conf> --rfsim
```

---

## 5. Core 5G via Docker

Cloner le dépôt CN5G :

```bash
git clone https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed.git
cd oai-cn5g-fed/docker-compose
```

Télécharger les images Docker :

```bash
./build_all_images --latest
docker-compose up -d
```

---

## 6. Pilotes pour le modem Quectel

Charger les modules :

```bash
sudo modprobe option
sudo modprobe usb_wwan
sudo modprobe qmi_wwan
```

Valider la détection :

```bash
ls /dev/cdc-wdm*
```

---

## 7. Organisation des fichiers

Tous les fichiers de travail sont placés dans :

```
~/Documents/quectel/quectel-CM/
~/Documents/openairinterface5g/
~/Documents/oai-cn5g-fed/
```

---
