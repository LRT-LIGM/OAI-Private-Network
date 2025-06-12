# Internship Project – OAI Private Network

Welcome to the documentation of the **OAI-Private-Network-main** project, carried out as part of my 2nd-year internship in the BUT Networks & Telecommunications program.

## Internship Objective

Set up a private 5G network using the **OpenAirInterface (OAI)** suite:

* Deploy a **5G Core (CN5G)**,
* Configure a **gNodeB**,
* Connect a **UE (User Equipment)** (virtual or physical),
* Perform **connectivity and performance tests**,
* Document the entire procedure for future handover or improvement.

## Supervisors

* **Internship supervisor**: Mr. Labiod
* **Technical advisor**: Mr. Clément
* **Institution**: IUT Créteil-Vitry, Université Paris-Est Créteil (UPEC)

## Technical Environment

* Linux distribution: **Ubuntu 22.04**
* Processor: **x86\_64**
* Virtual SDR with `--rfsim` (radio simulation mode)
* Hardware used: **Quectel RM500Q module**
* Technologies used:

  * Docker, Docker Compose
  * QMI (Qualcomm Modem Interface)
  * `quectel-CM` for modem interface
  * `qmicli` for low-level commands

## Documentation Structure

This documentation is divided into several parts to follow the project's progress:

1. **Installation** – Steps to install dependencies and tools
2. **Configuration** – Details of configured files and parameters
3. **Quectel Module** – SIM card connection and modem diagnostics
4. **QMI Commands** – Directory of useful commands and their explanation
5. **Tests** – Results of the tests performed
6. **Issues & Solutions** – List of blockers and their resolutions
7. **Resources** – Useful links and external documentation
8. **Summary** – Project feedback, lessons learned, and recommendations

## Project Tracking

The `.md` files provided here can be read via a WebUI thanks to Markdown integration.
Each section can be reviewed to better understand the project steps or to reproduce it in another environment.