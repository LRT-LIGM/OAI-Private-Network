# Accessing the MySQL Database in a Docker Container (OAI)

This file summarizes the commands used to access, interact with, and manipulate the `oai_db` database used in the OAI 5G core.

---

## 1. Connect to the MySQL container

```bash
docker exec -it mysql bash
```

Once inside the container:

```bash
mysql -uroot -p
```

> The root password is often `linux` (or defined in `docker-compose.yaml`).

---

## 2. Show available databases

```sql
SHOW DATABASES;
```

---

## 3. Use the OAI database

```sql
USE oai_db;
```

---

## 4. List the tables

```sql
SHOW TABLES;
```

---

## 5. Search for a subscriber via IMSI

```sql
SELECT * FROM AuthenticationSubscription WHERE ueId = '001010000000002';
SELECT * FROM SessionManagementSubscriptionData WHERE ueId = '001010000000002';
SELECT * FROM AccessAndMobilitySubscriptionData WHERE ueId = '001010000000002';
```

---

## 6. Add a new subscriber

> Example with IMSI `001010000000005`

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

## 7. Delete a subscriber (if needed)

```sql
DELETE FROM AuthenticationSubscription WHERE ueId = '001010000000005';
DELETE FROM SessionManagementSubscriptionData WHERE ueId = '001010000000005';
DELETE FROM AccessAndMobilitySubscriptionData WHERE ueId = '001010000000005';
```

---

## 8. Restart related services (after modification)

```bash
docker-compose restart oai-amf
docker-compose restart oai-smf
```

---

## Notes

* These operations are **critical** for the registration and attachment of a 5G UE.
* Always verify the IMSI and keys (`K`, `OPC`) before inserting.