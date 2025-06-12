# Accès à la base de données MySQL dans un conteneur Docker (OAI)

Ce fichier récapitule les commandes utilisées pour accéder, interagir et manipuler la base de données `oai_db` utilisée dans le core OAI 5G.

---

## 1. Se connecter au conteneur MySQL

```bash
docker exec -it mysql bash
```

Une fois dans le conteneur :

```bash
mysql -uroot -p
```

> Le mot de passe root est souvent `linux` (ou défini dans `docker-compose.yaml`).

---

## 2. Afficher les bases disponibles

```sql
SHOW DATABASES;
```

---

## 3. Utiliser la base de données OAI

```sql
USE oai_db;
```

---

## 4. Lister les tables

```sql
SHOW TABLES;
```

---

## 5. Rechercher un abonné via l’IMSI

```sql
SELECT * FROM AuthenticationSubscription WHERE ueId = '001010000000002';
SELECT * FROM SessionManagementSubscriptionData WHERE ueId = '001010000000002';
SELECT * FROM AccessAndMobilitySubscriptionData WHERE ueId = '001010000000002';
```

---

## 6. Ajouter un nouvel abonné

> Exemple avec IMSI `001010000000005`

```sql
INSERT INTO AuthenticationSubscription
(ueid, authenticationMethod, encPermanentKey, protectionParameterId,
 sequenceNumber, authenticationManagementField, algorithmId, encOpcKey, supi)
VALUES
('001010000000005', '5G_AKA', '6874736969202073796d4b2079650a73',
 '6874736969202073796d4b2079650a73',
 '{"sqn": "000000000000", "sqnScheme": "NON_TIME_BASED", "lastIndexes": {"ausf": 0}}',
 '8000', 'milenage', '504f20634f6320504f50206363500a4f', '001010000000005');
```

---

## 7. Supprimer un abonné (si nécessaire)

```sql
DELETE FROM AuthenticationSubscription WHERE ueId = '001010000000005';
DELETE FROM SessionManagementSubscriptionData WHERE ueId = '001010000000005';
DELETE FROM AccessAndMobilitySubscriptionData WHERE ueId = '001010000000005';
```

---

## 8. Redémarrer les services liés (après modification)

```bash
docker-compose restart oai-amf
docker-compose restart oai-smf
```

---

## Remarques

- Ces opérations sont **critiques** pour l'enregistrement et l'attachement d'un UE 5G.
- Toujours vérifier l’IMSI et les clés (`K`, `OPC`) avant insertion.
