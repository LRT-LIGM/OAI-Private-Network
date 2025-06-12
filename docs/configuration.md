# Configuration – Mise en place du réseau privé 5G

Ce fichier détaille la configuration de chaque composant de l’environnement OAI : core réseau, gNodeB, UE et modem.

---

## 1. Core 5G (CN5G)

### a. Clonage et lancement

```bash
wget -O ~/oai-cn5g.zip https://gitlab.eurecom.fr/oai/openairinterface5g/-/archive/develop/openairinterface5g-develop.zip?path=doc/tutorial_resources/oai-cn5g
unzip ~/oai-cn5g.zip
cd oai-cn5g
docker-compose up --build
```


### b. Vérification

```bash
docker ps
docker-compose logs -f oai-amf
```

> Tous les conteneurs doivent être en `healthy`.

---

## 2. gNodeB (RAN)

### a. Compilation

```bash
cd openairinterface5g/cmake_targets
./build_oai -I --gNB
```

### b. Lancement en mode simulation (sans SDR)

```bash
sudo ./nr-softmodem -O ./targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.conf --rfsim
```

> L’option `--rfsim` permet un test sans matériel radio.

---

## 3. UE – User Equipment

Lancement avec `nr-uesoftmodem` :

```bash
sudo ./nr-uesoftmodem -O ./targets/PROJECTS/GENERIC-NR-5GC/CONF/ue.conf --rfsim
```

---

## 4. Configuration du modem Quectel

### a. Lancer l’outil `quectel-CM`

```bash
cd ~/Documents/quectel/quectel-CM/out
sudo ./quectel-CM -s ebouygtel.com
```

### b. Vérification SIM

```bash
sudo qmicli -d /dev/cdc-wdm1 --uim-get-card-status
```

### c. Forcer la connexion réseau

```bash
sudo ip link set wwan0 up
sudo udhcpc -i wwan0
```

---

## 5. Scan des réseaux disponibles

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-network-scan
```

> Exemple de résultat :

```
Network [6]:
	MCC: '208'  MNC: '20'  Description: 'BYTEL'
	Status: current-serving, roaming, not-forbidden
```

---

## 6. Vérification de l’état de connexion

```bash
sudo qmicli -d /dev/cdc-wdm1 --nas-get-serving-system
```

> Vérifier que `Registration state: registered`
> et que `DataCap` n’est pas `UNKNOW`.

---
