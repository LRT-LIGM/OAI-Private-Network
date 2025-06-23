# Semaine du 17 au 21 juin 2025 – Programmation de la carte SIM Sysmocom

## Objectif

Configurer une carte SIM programmable (Sysmocom) afin qu'elle soit utilisable avec un gNodeB (OpenAirInterface), en programmant les champs IMSI, KEY, OPC, ISDN, ACC, SPN, et en vérifiant le fonctionnement de l'authentification AKA.

---

## Matériel utilisé

- Carte SIM Sysmocom (ICCID : 8988211000001037921f)
- Lecteur USB SmartCard compatible PCSC
- Adaptateur série USB (PL2303)
- Port `/dev/ttyUSB0` reconnu
- Logiciel : `program_uicc` (uicc-v3.3 depuis OpenCells)

---

## Étapes réalisées

### 🔹 Préparation de l’environnement

- Installation de `libccid`, `pcscd`, `pcsc-tools`
- Correction du code source `program_uicc.c` pour éviter les erreurs de segmentation
- Recompilation :
  ```bash
  make clean && make
  ```

### 🔹 Tests de lecture

- ICCID correctement lu : `8988211000001037921f`
- Lecture de l'IMSI échouée → fichier manquant ou protégé

### 🔹 Tentatives de programmation

- Codes ADM testés : `00000000`, `12345678`, `11111111`, `22222222`, `68594154`, etc.
- Tous renvoient :
  - `9840` → Security status not satisfied
  - `6983` → Authentication method blocked
- Conclusion : **le bon code ADM est requis** pour programmer les données sensibles

### 🔹 Authentification AKA

- Tests réalisés avec `KEY` et `OPC` → authentification réussie ✅
  ```
  Succeeded to authentify with SQN: 832
  set HSS SQN value as: 864
  ```

---

## Résultats actuels

- La carte SIM répond aux commandes standards
- Écriture IMSI impossible sans code ADM
- L’authentification réseau (AKA) fonctionne

---

## Actions suivantes

- Contacter M. Labiod pour obtenir le **code ADM** de la SIM (ICCID : 8988211000001037921f)
- Refaire un test complet avec le bon code ADM dès que disponible

---

*Rédigé par :* Kopethan\
*Encadré par :* M. Labiod

