# Guide de Lancement des Composants

Cette page documente les étapes nécessaires pour lancer les composants du projet OAI Private Network.

---

## Pré-requis

- Avoir configuré correctement les fichiers `docker-compose` pour le core 5G.
- Avoir compilé avec succès le gNodeB (`nr-softmodem`) et/ou `nr-uesoftmodem`.
- Vérifier la disponibilité des interfaces USRP ou utiliser `--rfsim` pour simuler.

---

## Lancer le Core 5G (CN5G)

```bash
cd ~/Documents/oai-cn5g
git checkout develop
sudo docker compose up
```

---

## Lancer le gNodeB avec B210

Ajout manuel de l’adresse IP manquante :
```bash
sudo ip addr add 172.31.0.150/24 dev oai-cn5g
```

```bash
cd ~/Documents/openairinterface5g/cmake_targets/ran_build/build
sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 6 -E --continuous-tx
```

---

## Lancer le gNodeB (avec simulation radio)

```bash
cd ~/Documents/openairinterface5g/cmake_targets/ran_build/build
sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 6 --rfsim
```

> Utiliser `--rfsim` si vous n'avez pas de SDR physique connecté.

---

## Lancer l’UE Simulé

```bash
cd ~/Documents/openairinterface5g/cmake_targets/ran_build/build
sudo ./nr-uesoftmodem -r 106 --numerology 1 --band 78 -C 3619200000 --uicc0.imsi 001010000000001 --rfsim
```

---

Mise à jour : 2025-06-03