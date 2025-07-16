# Lancement – Option 1 (OAI 5G SA avec USRP B210)

Cette section décrit le lancement du core 5G, du gNodeB et des tests avec UE (SIM réelle ou simulée) selon la méthode Option 1.

---

## 1. Démarrage du Core 5G

```bash
cd ~/OAI-5GCN-v2.0.1/docker-compose
python3 core-network.py --type start-basic --scenario 1
```

Vérifie :
```bash
docker ps
```
→ Tous les conteneurs doivent être `healthy`

---

## 2. Lancement du gNodeB (avec USRP)

### a. Ajouter IP manuellement (si nécessaire)
```bash
sudo ip addr add 172.31.0.150/24 dev oai-cn5g
```

### b. Lancer le softmodem avec config USRP B210 :
```bash
cd ~/openairinterface5g/cmake_targets/ran_build/build
sudo ./nr-softmodem -O config/5GN78.conf --sa -E --continuous-tx
```

**Options :**
- `--sa` : mode Standalone (5G pur)
- `--E` : désactive les threads inutiles
- `--continuous-tx` : transmission continue (utile avec USRP en TDD)

Logs visibles dans le terminal, ou à rediriger :
```bash
... --continuous-tx 2>&1 | tee gNB_B210_log.txt
```

---

## 3. Lancement du gNodeB (en simulation SDR – optionnel)
```bash
sudo ./nr-softmodem -O config/5GN78.conf --rfsim
```

---

## 4. Lancement d’un UE simulé (nr-uesoftmodem)
```bash
sudo ./nr-uesoftmodem -r 106 --numerology 1 --band 78 -C 3619200000 --uicc0.imsi 001010000000001 --rfsim
```

---

## 5. Outils complémentaires

### Wireshark (pour logs NGAP)
```bash
sudo wireshark
```
Filtre :
```
ngap
```
Interface : `demo-oai`

### Analyse des logs AMF :
```bash
docker logs oai-amf -f
```

---

Système prêt ✅ Tu peux maintenant tester avec un smartphone, SIM Quectel ou UE simulé.
