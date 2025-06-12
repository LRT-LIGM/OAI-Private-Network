# Erreur RRC : PDU Session déjà existante

## Message d’erreur rencontré

```text
[NR_RRC]   UE 1: already has existing PDU session 1 rejecting PDU Session Resource Setup Request
```

---

## Signification

Cette erreur indique que le **gNodeB** a déjà une **session PDU active** (ID = 1) pour l'UE.  
Quand une nouvelle requête arrive avec le même ID, elle est rejetée.

---

## Causes possibles

- L’UE (modem ou softmodem) tente de créer une session déjà active.
- Le gNodeB conserve un **ancien contexte PDU**.
- Le core (AMF/SMF) n’a pas libéré les sessions précédentes.

---

## Solutions recommandées

### 1. Redémarrer tous les services pour nettoyer les contextes

```bash
# Core 5G
cd ~/Documents/oai-cn5g
docker-compose down
docker-compose up -d

# gNodeB
sudo pkill nr-softmodem
sudo ./nr-softmodem -O <conf-file> ...
```

---

### 2. Redémarrer l'UE (modem ou softmodem)

#### Modem Quectel :
```bash
AT+CFUN=1,1
```

#### Soft UE (`nr-uesoftmodem`) :
```bash
sudo pkill nr-uesoftmodem
sudo ./nr-uesoftmodem ...
```

---

### 3. Nettoyage manuel de la session PDU dans MySQL

*À utiliser avec précaution.*

```sql
DELETE FROM SmfRegistrations WHERE supi = '001010000000005';
```

Puis redémarrer le SMF :
```bash
docker-compose restart oai-smf
```

---

## À éviter

- Ne pas relancer `nr-softmodem` en boucle sans redémarrer l'UE ou le core.
- Cela maintient un contexte invalide côté gNodeB.

---

## Référence

- Source : logs `nr-softmodem`, RRC layer
- Contexte : simulation 5G SA avec OpenAirInterface + USRP/Quectel
