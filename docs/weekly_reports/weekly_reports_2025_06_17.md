# Semaine du 17 au 21 juin 2025 – Suivi de stage OAI 5G

## Objectif principal

Tester la connexion d’un UE (modem ou smartphone) à une infrastructure 5G Standalone (SA) en utilisant la stack OpenAirInterface :

- Lancer le gNodeB (`nr-softmodem`)
- Connecter l'AMF via Docker
- Vérifier l’attachement de l’UE et l’attribution d’un GUTI

---

## Travaux réalisés

### 1. Lancement du gNodeB

- Lancement de `nr-softmodem` en mode SA sur la bande **n78 (3619.2 MHz)** :
  ```bash
  sudo ./nr-softmodem -O ...gnb.sa.band78.fr1.106PRB.usrpb210.conf --continuous-tx -E
  ```
  - USRP B210 reconnu (RX/TX OK, fréquence et gains bien configurés)
  - Transmission continue activée (`--continuous-tx`)

### 2. Statut de l’AMF

- Conteneur AMF lancé et en bon état :
  ```bash
  docker ps | grep amf → healthy
  ```
- Communication NGAP établie entre gNB et AMF (port SCTP 38412)

### 3. Test de l’attachement d’un UE

- Enregistrement partiel détecté :
  - `5GMM-REGISTERED` visible côté AMF
  - IMSI de la carte SIM correcte
  - Mais **pas de GUTI attribué** (champ vide)
- Logs `nr-softmodem` → nombreuses erreurs uplink :
  - `UL Failure`, `RSRP = 0`, `out-of-sync`
  - L’UE semble **ne pas transmettre ou être mal reçu**

### 4. Résultat supplémentaire important

- L'AMF affiche une connexion UE avec l'IMSI 001010000059463 → **attachement visible**

### 5. Tentatives d’optimisation

- Ajout de `--tune-offset` pour réduire le bruit DC
- Réduction du `min_rxtxtime` à 8
- Placement physique proche de l'antenne

---

## Analyse

| Élément        | État    | Observations                          |
| -------------- | ------- | ------------------------------------- |
| gNodeB         | OK      | Connecté à l’AMF, transmission active |
| AMF            | OK      | En ligne, heartbeat NRF régulier      |
| UE (carte SIM) | Partiel | IMSI reçue, mais aucun GUTI attribué  |
| Couche radio   | KO      | Pas de données UL reçues du modem/UE  |

> GUTI (Globally Unique Temporary Identifier) : identifiant temporaire attribué à un UE lors de l’enregistrement sur un réseau 5G. Il évite de réutiliser l’IMSI à chaque fois.

---

## Prochaines actions

- Vérifier la configuration de la **carte SIM** (clé, OPC, IMSI)
- Confirmer le **support du mode SA** sur l’UE utilisé
- Continuer l’analyse des logs AMF :
  ```bash
  docker logs oai-amf -f
  ```
- Tester avec un autre UE ou une autre SIM si besoin
- Tester avec `nr-uesoftmodem` en mode `--rfsim`

---

*Rédigé par :* Kopethan *Encadré par :* M. Labiod

