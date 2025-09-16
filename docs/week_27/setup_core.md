# Setting Up the 5G Core (OAI CN5G)

This file documents the installation and configuration of the OpenAirInterface 5G Core (CN5G), performed on a dedicated machine during the internship.

---

## Environment Used

* **Machine**: PC2 (secondary lab machine)
* **OS**: Ubuntu 20.04 / 22.04
* **Docker / docker-compose** installed
* **Project cloned from**:
  [https://github.com/OPENAIRINTERFACE/openairinterface5g](https://github.com/OPENAIRINTERFACE/openairinterface5g)

---

## Main Steps

### 1. Clone the repository

```bash
git clone https://gitlab.eurecom.fr/oai/openairinterface5g.git
cd openairinterface5g
```

---

### 2. Access official documentation

-> Followed tutorial: [`NR_SA_Tutorial_OAI_CN5G.md`](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/NR_SA_Tutorial_OAI_CN5G.md)

---

### 3. Download Docker images

```bash
docker pull oaisoftwarealliance/oai-amf:v2.1.9
docker pull oaisoftwarealliance/oai-smf:v2.1.9
docker pull oaisoftwarealliance/oai-spgwu-tiny:v2.1.9
docker pull oaisoftwarealliance/oai-nrf:v2.1.9
docker pull oaisoftwarealliance/oai-upf:v2.1.9
```

---

### 4. Configure the `docker-compose` file

> File: `docker-compose/docker-compose-basic-vpp.yaml`

*Adjust the environment variables:*

* `TZ=Europe/Paris`
* `NRF_IPV4_ADDRESS`, `AMF_IPV4_ADDRESS`, etc.
* Network interface → corresponds to the Ethernet adapter in use.

---

### 5. Launch the core

```bash
cd docker-compose
docker-compose -f docker-compose-basic-vpp.yaml up -d
```

*Verification:*

```bash
docker ps
```

All containers must be in `healthy` state (check with `docker ps` or `docker inspect`)

---

## Tests

* gNodeB connection to this Core (see `setup_gnb.md`)
* Display logs:

  ```bash
  docker logs oai-amf -f
  ```

---

## Notes

* Using `--net=host` is not required if Docker interfaces are properly configured.
* A custom bridge network can be used if static IP assignment is needed.

---
