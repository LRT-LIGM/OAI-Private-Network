# Internship Project – OAI Private Network

Welcome to the documentation for the **OAI-Private-Network-main** project, carried out as part of my second-year internship in the *Networks & Telecommunications* program.

## Internship Objective

Set up a private 5G network using the **OpenAirInterface (OAI)** suite:

* Deploy a **5G Core Network (CN5G)**,
* Configure a **gNodeB**,
* Connect a **User Equipment (UE)**, virtual or physical,
* Perform **connectivity and performance tests**,
* Document the entire procedure for future reuse or improvements.

## Supervisors

* **Internship Supervisor**: Mr. Labiod
* **Technical Advisor**: Mr. Dutriez
* **Institution**: IUT Créteil-Vitry, Université Paris-Est Créteil (UPEC)

## Technical Environment

* Linux Distribution: **Ubuntu 22.04**
* Processor: **x86\_64**
* Virtual SDR using `--rfsim` (radio simulation mode)
* Hardware used: **Quectel RM500Q module**
* Technologies used:

  * Docker, Docker-compose
  * QMI (Qualcomm Modem Interface)
  * `quectel-CM` for modem interface
  * `qmicli` for low-level commands

## Documentation Structure

This documentation is divided into several parts to follow the project’s progress:

1. **Installation** – Steps to install dependencies and tools
2. **Configuration** – Configuration files and parameter details
3. **Quectel Module** – SIM card connection and modem diagnostics
4. **QMI Commands** – Reference of useful commands and their explanation
5. **Tests** – Results from the tests performed
6. **Problems & Solutions** – List of issues and how they were solved
7. **Resources** – Useful links and external documentation
8. **Conclusion** – Reflections on the project, learnings, and recommendations

## Project Tracking

The `.md` files here are viewable through a WebUI thanks to Markdown integration.
Each section can be explored to better understand the project steps or reproduce them in another environment.

---