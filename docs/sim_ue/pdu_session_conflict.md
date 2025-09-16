# RRC Error: PDU Session Already Exists

## Error Message Encountered

```text
[NR_RRC]   UE 1: already has existing PDU session 1 rejecting PDU Session Resource Setup Request
```

---

## Meaning

This error indicates that the **gNodeB** already has an **active PDU session** (ID = 1) for the UE.
When a new request arrives with the same ID, it is rejected.

---

## Possible Causes

* The UE (modem or softmodem) is trying to create a session that is already active.
* The gNodeB is keeping an **old PDU context**.
* The core (AMF/SMF) has not released previous sessions.

---

## Recommended Solutions

### 1. Restart all services to clean contexts

```bash
# 5G Core
cd ~/Documents/oai-cn5g
docker-compose down
docker-compose up -d

# gNodeB
sudo pkill nr-softmodem
sudo ./nr-softmodem -O <conf-file> ...
```

---

### 2. Restart the UE (modem or softmodem)

#### Quectel Modem:

```bash
AT+CFUN=1,1
```

#### Soft UE (`nr-uesoftmodem`):

```bash
sudo pkill nr-uesoftmodem
sudo ./nr-uesoftmodem ...
```

---

### 3. Manual PDU Session cleanup in MySQL

*Use with caution.*

```sql
DELETE FROM SmfRegistrations WHERE supi = '001010000000005';
```

Then restart the SMF:

```bash
docker-compose restart oai-smf
```

---

## To Avoid

* Do not relaunch `nr-softmodem` repeatedly without restarting the UE or the core.
* This will maintain an invalid context on the gNodeB side.

---

## Reference

* Source: `nr-softmodem` logs, RRC layer
* Context: 5G SA simulation with OpenAirInterface + USRP/Quectel
