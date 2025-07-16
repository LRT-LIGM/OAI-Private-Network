# softmodem.log — Successful Connection Log

This file contains the complete log (`softmodem.log`) corresponding to a **successful** run of the gNodeB `nr-softmodem` with a correctly programmed and registered SIM card.

---

## File Details

* **File name**: `softmodem.log`
* **Context**:

  * SIM configured with IMSI: `001010000000002`
  * OAI Core: Docker with MySQL (`oai_db`)
  * RAN: `nr-softmodem` launched in `--continuous-tx` mode with SDR (B210)

---

## Raw Log Excerpt

```bash
[UTIL]   running in SA mode (no --phy-test, --do-ra, --nsa option present)
[OPT]   OPT disabled
[HW]   Version: Branch: develop Abrev. Hash: b2c9a1d2b5 Date: Tue May 20 05:46:54 2025 +0000
[GNB_APP]   Initialized RAN Context: RC.nb_nr_inst = 1, RC.nb_nr_macrlc_inst = 1, RC.nb_nr_L1_inst = 1, RC.nb_RU = 1, RC.nb_nr_CC[0] = 1
[NR_PHY]   Initializing gNB RAN context: RC.nb_nr_L1_inst = 1 
[NR_PHY]   Registered with MAC interface module (0x606038e5cfb0)
[NR_PHY]   Initializing NR L1: RC.nb_nr_L1_inst = 1
[NR_PHY]   L1_RX_THREAD_CORE -1 (15)
[NR_PHY]   TX_AMP = 519 (-36 dBFS)
[PHY]   No prs_config configuration found..!!
[GNB_APP]   pdsch_AntennaPorts N1 1 N2 1 XP 1 pusch_AntennaPorts 1
[GNB_APP]   minTXRXTIME 6
[GNB_APP]   SIB1 TDA 1
[GNB_APP]   CSI-RS 1, SRS 1, SINR:0, 256 QAM may be on, delta_MCS off, maxMIMO_Layers -1, HARQ feedback enabled, num DLHARQ:16, num ULHARQ:16
[NR_MAC]   No RedCap configuration found
[GNB_APP]   sr_ProhibitTimer 0, sr_TransMax 64, sr_ProhibitTimer_v1700 0, t300 400, t301 400, t310 2000, n310 10, t311 3000, n311 1, t319 400
[NR_MAC]   Candidates per PDCCH aggregation level on UESS: L1: 0, L2: 2, L4: 0, L8: 0, L16: 0
[RRC]   Read in ServingCellConfigCommon (PhysCellId 0, ABSFREQSSB 641280, DLBand 78, ABSFREQPOINTA 640008, DLBW 106,RACH_TargetReceivedPower -96
[RRC]   absoluteFrequencySSB 641280 corresponds to 3619200000 Hz
[NR_MAC]   TDD period index = 6, based on the sum of dl_UL_TransmissionPeriodicity from Pattern1 (5.000000 ms) and Pattern2 (0.000000 ms): Total = 5.000000 ms
[UTIL]   threadCreate() for MAC_STATS: creating thread with affinity ffffffff, priority 2
[NR_MAC]   PUSCH Target 150, PUCCH Target 200, PUCCH Failure 10, PUSCH Failure 10
[NR_PHY]   Copying 0 blacklisted PRB to L1 context
[NR_MAC]   Set TX antenna number to 1, Set RX antenna number to 1 (num ssb 1: 80000000,0)
[NR_MAC]   TDD period index = 6, based on the sum of dl_UL_TransmissionPeriodicity from Pattern1 (5.000000 ms) and Pattern2 (0.000000 ms): Total = 5.000000 ms
[NR_MAC]   Set TDD configuration period to: 8 DL slots, 3 UL slots, 10 slots per period (NR_TDD_UL_DL_Pattern is 7 DL slots, 2 UL slots, 6 DL symbols, 4 UL symbols)
[NR_MAC]   Configured 1 TDD patterns (total slots: pattern1 = 10, pattern2 = 0)
[NR_PHY]   Set TDD Period Configuration: 2 periods per frame, 20 slots to be configured (8 DL, 3 UL)
[NR_PHY]   TDD period configuration: slot 0 is DOWNLINK
[NR_PHY]   TDD period configuration: slot 1 is DOWNLINK
[NR_PHY]   TDD period configuration: slot 2 is DOWNLINK
[NR_PHY]   TDD period configuration: slot 3 is DOWNLINK
[NR_PHY]   TDD period configuration: slot 4 is DOWNLINK
[NR_PHY]   TDD period configuration: slot 5 is DOWNLINK
[NR_PHY]   TDD period configuration: slot 6 is DOWNLINK
[NR_PHY]   TDD period configuration: slot 7 is FLEXIBLE: DDDDDDFFFFUUUU
[NR_PHY]   TDD period configuration: slot 8 is UPLINK
[NR_PHY]   TDD period configuration: slot 9 is UPLINK
[PHY]   DL frequency 3619200000 Hz, UL frequency 3619200000 Hz: band 48, uldl offset 0 Hz
[PHY]   Initializing frame parms for mu 1, N_RB 106, Ncp 0
[PHY]   Init: N_RB_DL 106, first_carrier_offset 900, nb_prefix_samples 108,nb_prefix_samples0 132, ofdm_symbol_size 1536
[NR_RRC]   SIB1 freq: offsetToPointA 86
[GNB_APP]   F1AP: gNB idx 0 gNB_DU_id 3584, gNB_DU_name gNB-OAI, TAC 1 MCC/MNC/length 1/1/2 cellID 12345678
[GNB_APP]   ngran_DU: Configuring Cell 0 for TDD
[GNB_APP]   SDAP layer is disabled
[GNB_APP]   Data Radio Bearer count 1
[GNB_APP]   Parsed IPv4 address for NG AMF: 172.31.0.150
[UTIL]   threadCreate() for TASK_SCTP: creating thread with affinity ffffffff, priority 50
[X2AP]   X2AP is disabled.
[UTIL]   threadCreate() for TASK_NGAP: creating thread with affinity ffffffff, priority 50
[NGAP]   Starting NGAP layer
[UTIL]   threadCreate() for TASK_RRC_GNB: creating thread with affinity ffffffff, priority 50
[NGAP]   Registered new gNB[0] and macro gNB id 3584
[NGAP]   [gNB 0] check the amf registration state
[GTPU]   Configuring GTPu
[GTPU]   SA mode 
[GTPU]   Configuring GTPu address : 172.31.0.150, port : 2152
[GTPU]   Initializing UDP for local address 172.31.0.150 with port 2152
[GTPU]   Created gtpu instance id: 94
[NR_RRC]   Entering main loop of NR_RRC message task
[NR_RRC]   Accepting new CU-UP ID 3584 name gNB-OAI (assoc_id -1)
[UTIL]   threadCreate() for TASK_GNB_APP: creating thread with affinity ffffffff, priority 50
[NGAP]   Send NGSetupRequest to AMF
[NGAP]   3584 -> 0000e000
[NGAP]   servedGUAMIs.list.count 1
[NGAP]   PLMNSupportList.list.count 1
[NGAP]   PLMNSupportList.list.count 2
[NGAP]   Received NGSetupResponse from AMF
[UTIL]   threadCreate() for TASK_GTPV1_U: creating thread with affinity ffffffff, priority 50
[GNB_APP]   [gNB 0] Received NGAP_REGISTER_GNB_CNF: associated AMF 1
[NR_RRC]   Received F1 Setup Request from gNB_DU 3584 (gNB-OAI) on assoc_id -1
[NR_RRC]   Accepting DU 3584 (gNB-OAI), sending F1 Setup Response
[NR_RRC]   DU uses RRC version 17.3.0
[MAC]   received F1 Setup Response from CU (null)
[MAC]   CU uses RRC version 17.3.0
[MAC]   Clearing the DU's UE states before, if any.
[NR_RRC]   cell PLMN 001.01 Cell ID 12345678 is in service
[MAC]   received gNB-DU configuration update acknowledge
[UTIL]   threadCreate() for time source realtime: creating thread with affinity ffffffff, priority 2
[UTIL]   time manager configuration: [time source: reatime] [mode: standalone] [server IP: 127.0.0.1} [server port: 7374] (server IP/port not used)
[PHY]   RU clock source set as internal
[PHY]   number of L1 instances 1, number of RU 1, number of CPU cores 28
[PHY]   Initialized RU proc 0 (,synch_to_ext_device),
[PHY]   RU thread-pool core string -1,-1 (size 2)
[UTIL]   threadCreate() for Tpool0_-1: creating thread with affinity ffffffff, priority 97
[UTIL]   threadCreate() for Tpool1_-1: creating thread with affinity ffffffff, priority 97
[UTIL]   threadCreate() for ru_thread: creating thread with affinity ffffffff, priority 97
[PHY]   Starting RU 0 (,synch_to_ext_device) on cpu 24
[PHY]   Initializing frame parms for mu 1, N_RB 106, Ncp 0
[PHY]   Init: N_RB_DL 106, first_carrier_offset 900, nb_prefix_samples 108,nb_prefix_samples0 132, ofdm_symbol_size 1536
[PHY]   fp->scs=30000
[PHY]   fp->ofdm_symbol_size=1536
[PHY]   fp->nb_prefix_samples0=132
[PHY]   fp->nb_prefix_samples=108
[PHY]   fp->slots_per_subframe=2
[PHY]   fp->samples_per_subframe_wCP=43008
[PHY]   fp->samples_per_frame_wCP=430080
[PHY]   fp->samples_per_subframe=46080
[PHY]   fp->samples_per_frame=460800
[PHY]   fp->dl_CarrierFreq=3619200000
[PHY]   fp->ul_CarrierFreq=3619200000
[PHY]   fp->Nid_cell=0
[PHY]   fp->first_carrier_offset=900
[PHY]   fp->ssb_start_subcarrier=0
[PHY]   fp->Ncp=0
[PHY]   fp->N_RB_DL=106
[PHY]   fp->numerology_index=1
[PHY]   fp->nr_band=48
[PHY]   fp->ofdm_offset_divisor=8
[PHY]   fp->threequarter_fs=1
[PHY]   fp->sl_CarrierFreq=0
[PHY]   fp->N_RB_SL=0
[PHY]   Setting RF config for N_RB 106, NB_RX 1, NB_TX 1
[PHY]   tune_offset 0 Hz, sample_rate 46080000 Hz
[PHY]   Channel 0: setting tx_gain offset 0, tx_freq 3619200000 Hz
[PHY]   Channel 0: setting rx_gain offset 114, rx_freq 3619200000 Hz
[HW]   openair0_cfg[0].sdr_addrs == '(null)'
[HW]   openair0_cfg[0].clock_source == '0' (internal = 0, external = 1)
[HW]   UHD version 4.8.0.HEAD-0-g308126a4 (4.8.0)
[INFO] [UHD] linux; GNU C++ version 11.4.0; Boost_107400; UHD_4.8.0.HEAD-0-g308126a4
[HW]   Found USRP b200
[INFO] [B200] Detected Device: B210
[INFO] [B200] Operating over USB 3.
[INFO] [B200] Initialize CODEC control...
[INFO] [B200] Initialize Radio control...
[INFO] [B200] Performing register loopback test... 
[INFO] [B200] Register loopback test passed
[INFO] [B200] Performing register loopback test... 
[INFO] [B200] Register loopback test passed
[INFO] [B200] Asking for clock rate 30.720000 MHz... 
[INFO] [B200] Actually got clock rate 30.720000 MHz.
[HW]   Setting clock source to internal
[HW]   Setting time source to internal
CMDLINE: "./nr-softmodem" "-O" "../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf" "--gNBs.[0].min_rxtxtime" "6" "-E" "--continuous-tx" 
[CONFIG] function config_libconfig_init returned 0
Reading 'GNBSParams' section from the config file
Reading 'GNBSParams' section from the config file
Reading 'GNBSParams' section from the config file
Reading 'GNBSParams' section from the config file
Reading 'Timers_Params' section from the config file
Reading 'SCCsParams' section from the config file
Reading 'MsgASCCsParams' section from the config file
DL frequency 3619200000: band 48, UL frequency 3619200000
Reading 'GNBSParams' section from the config file
Reading 'GNBSParams' section from the config file
Reading 'Periodical_EventParams' section from the config file
Reading 'A2_EventParams' section from the config file
Reading 'GNBSParams' section from the config file
Reading 'SCTPParams' section from the config file
Reading 'NETParams' section from the config file
Reading 'GNBSParams' section from the config file
Reading 'GNBSParams' section from the config file
Reading 'NETParams' section from the config file
-- Using calibration table: calib_table_b210_38
[INFO] [B200] Asking for clock rate 46.080000 MHz... 
[INFO] [B200] Actually got clock rate 46.080000 MHz.
[HW]   cal 0: freq 3500000000.000000, offset 44.000000, diff 119200000.000000
[HW]   cal 1: freq 2660000000.000000, offset 49.800000, diff 959200000.000000
[HW]   cal 2: freq 2300000000.000000, offset 51.000000, diff 1319200000.000000
[HW]   cal 3: freq 1880000000.000000, offset 53.000000, diff 1739200000.000000
[HW]   cal 4: freq 816000000.000000, offset 57.000000, diff 2803200000.000000
[HW]   RX Gain 0 114.000000 (44.000000) => 70.000000 (max 76.000000)
[HW]   USRP TX_GAIN:89.75 gain_range:89.75 tx_gain:0.00
[HW]   Actual master clock: 46.080000MHz...
[HW]   Actual clock source internal...
[HW]   Actual time source internal...
[HW]   setting rx channel 0
[HW]   RF board max packet size 1916, size for 100µs jitter 4608 
[HW]   rx_max_num_samps 1916
[HW]   RX Channel 0
[HW]     Actual RX sample rate: 46.080000MSps...
[HW]     Actual RX frequency: 3.619200GHz...
[HW]     Actual RX gain: 70.000000...
[HW]     Actual RX bandwidth: 40.000000M...
[HW]     Actual RX antenna: RX2...
[HW]   TX Channel 0
[HW]     Actual TX sample rate: 46.080000MSps...
[HW]     Actual TX frequency: 3.619200GHz...
[HW]     Actual TX gain: 89.750000...
[HW]     Actual TX bandwidth: 40.000000M...
[HW]     Actual TX antenna: TX/RX...
[HW]     Actual TX packet size: 1916
Using Device: Single USRP:
  Device: B-Series Device
  Mboard 0: B210
  RX Channel: 0
    RX DSP: 0
    RX Dboard: A
    RX Subdev: FE-RX2
  RX Channel: 1
    RX DSP: 1
    RX Dboard: A
    RX Subdev: FE-RX1
  TX Channel: 0
    TX DSP: 0
    TX Dboard: A
    TX Subdev: FE-TX2
  TX Channel: 1
    TX DSP: 1
    TX Dboard: A
    TX Subdev: FE-TX1

[HW]   Device timestamp: 0.177846...
[HW]   [RAU] has loaded USRP B200 device.
[PHY]   RU 0 Setting N_TA_offset to 600 samples (UL Freq 3600120, N_RB 106, mu 1)
[PHY]   Signaling main thread that RU 0 is ready, sl_ahead 6
[PHY]   L1 configured without analog beamforming
[PHY]   Attaching RU 0 antenna 0 to gNB antenna 0
[UTIL]   threadCreate() for Tpool0_-1: creating thread with affinity ffffffff, priority 97
[UTIL]   threadCreate() for Tpool1_-1: creating thread with affinity ffffffff, priority 97
[UTIL]   threadCreate() for Tpool2_-1: creating thread with affinity ffffffff, priority 97
[UTIL]   threadCreate() for Tpool3_-1: creating thread with affinity ffffffff, priority 97
[UTIL]   threadCreate() for Tpool4_-1: creating thread with affinity ffffffff, priority 97
[UTIL]   threadCreate() for Tpool5_-1: creating thread with affinity ffffffff, priority 97
[UTIL]   threadCreate() for Tpool6_-1: creating thread with affinity ffffffff, priority 97
[UTIL]   threadCreate() for Tpool7_-1: creating thread with affinity ffffffff, priority 97
[UTIL]   threadCreate() for L1_rx_thread: creating thread with affinity ffffffff, priority 97
[UTIL]   threadCreate() for L1_tx_thread: creating thread with affinity ffffffff, priority 97
[UTIL]   threadCreate() for L1_stats: creating thread with affinity ffffffff, priority 1
[PHY]   got sync (L1_stats_thread)
TYPE <CTRL-C> TO TERMINATE
[PHY]   got sync (ru_thread)
[HW]   current pps at 2.438191, starting streaming at 3.438191
[PHY]   RU 0 rf device ready
[PHY]   RU 0 RF started cpu_meas_enabled 0
[PHY]   Command line parameters for OAI UE: -C 3619200000 -r 106 --numerology 1 --ssb 516 -E
[NR_MAC]   Frame.Slot 512.0

[NR_MAC]   Frame.Slot 640.0

[NR_MAC]   Frame.Slot 768.0

[NR_MAC]   Frame.Slot 896.0

[NR_MAC]   Frame.Slot 0.0

[NR_MAC]   Frame.Slot 128.0

[NR_MAC]   Frame.Slot 256.0

[NR_PHY]   [RAPROC] 257.19 Initiating RA procedure with preamble 23, energy 56.4 dB (I0 351, thres 120), delay 0 start symbol 0 freq index 0
[NR_MAC]   257.19 UE RA-RNTI 010b TC-RNTI a616: initiating RA procedure
[NR_MAC]   UE a616: Msg3 scheduled at 258.17 (258.7 TDA 3) start 0 RBs 8
[NR_MAC]   UE a616: 258.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 23, timing_offset = 0 (estimated distance 0.0 [m])
[NR_MAC]   258.7 Send RAR to RA-RNTI 010b
[NR_MAC]    258.17 PUSCH with TC_RNTI 0xa616 received correctly
[MAC]   [RAPROC] Received SDU for CCCH length 6 for UE a616
[RLC]   Activated srb0 for UE 42518
[RLC]   Added srb 1 to UE 42518
[NR_MAC]   Activating scheduling Msg4 for TC_RNTI 0xa616 (state WAIT_Msg3)
[NR_RRC]   Decoding CCCH: RNTI a616, payload_size 6
[NR_RRC]   Received UE 5G-S-TMSI-Part1 282007558147
[NR_RRC]   [--] (cellID 0, UE ID 1 RNTI a616) Create UE context: CU UE ID 1 DU UE ID 42518 (rnti: a616, random ue id 41a8f5d803)
[RRC]   activate SRB 1 of UE 1
[NR_RRC]   [DL] (cellID bc614e, UE ID 1 RNTI a616) Send RRC Setup
[NR_MAC]   UE a616 Generate Msg4: feedback at  259.17, payload 225 bytes, next state nrRA_WAIT_Msg4_MsgB_ACK
[NR_MAC]   Adding new UE context with RNTI 0xa616
[NR_MAC]    259.17 UE a616: Received Ack of Msg4. CBRA procedure succeeded!
[NR_RRC]   [UL] (cellID bc614e, UE ID 1 RNTI a616) Received RRCSetupComplete (RRC_CONNECTED reached)
[RRC]   s_tmsi part2 0 (00 00)
[NR_RRC]   5g_s_TMSI: 0x41A8F5D803, amf_set_id: 0x1 (1), amf_pointer: 0x1 (1), 5g TMSI: 0xA8F5D803 
[NGAP]   UE 1: Chose AMF 'OAI-AMF' (assoc_id 7) through selected PLMN Identity index 0 MCC 1 MNC 1
[NGAP]   FIVEG_S_TMSI_PRESENT
[NGAP]   AllowedNSSAI.list.count 1
[NR_RRC]   [--] (cellID bc614e, UE ID 1 RNTI a616) Selected security algorithms: ciphering 0, integrity 2
[NR_RRC]   [UE a616] Saved security key 51
[NR_RRC]   UE 1 Logical Channel DL-DCCH, Generate SecurityModeCommand (bytes 3)
[NR_MAC]   UE a616: reported RSRP index 14 invalid
[NR_RRC]   [UL] (cellID bc614e, UE ID 1 RNTI a616) Received Security Mode Complete
[NR_RRC]   UE 1: Logical Channel DL-DCCH, Generate NR UECapabilityEnquiry (bytes 8, xid 3)
[NR_RRC]   [UL] (cellID bc614e, UE ID 1 RNTI a616) Received UE capabilities
[NR_RRC]   Send message to ngap: NGAP_UE_CAPABILITIES_IND
[NR_RRC]   Adding pdusession 1, total nb of sessions 1
[NR_RRC]   UE 1: configure DRB ID 1 for PDU session ID 1
[NR_RRC]   [--] (cellID bc614e, UE ID 1 RNTI a616) selecting CU-UP ID 3584 based on exact NSSAI match (1:0xffffff)
[RRC]   UE 1 associating to CU-UP assoc_id -1 out of 1 CU-UPs
[E1AP]   UE 1: add PDU session ID 1 (1 bearers)
[GTPU]   [94] Created tunnel for UE ID 1, teid for incoming: 917bc77e, teid for outgoing 2 to remote IPv4: 172.31.0.134, IPv6 ::
[PDCP]   added drb 1 to UE ID 1
[SDAP]   Default DRB for the created SDAP entity: 1 
[RRC]   activate SRB 2 of UE 1
[RLC]   Added srb 2 to UE 42518
[RLC]   Added drb 1 to UE 42518
[RLC]   Added DRB to UE 42518
[NR_RRC]   SRS configured with 1 ports
[RRC]   UE 1 trigger UE context setup request with 1 DRBs
[RRC]   UE a616 replacing existing CellGroupConfig with new one received from DU
[E1AP]   UE 1: updating PDU session ID 1 (1 bearers)
[PDCP]   DRB 1 re-established
[NR_RRC]   [DL] (cellID bc614e, UE ID 1 RNTI a616) Generate RRCReconfiguration (bytes 301, xid 0)
[RRC]   UE 1: PDU session ID 1 modified 1 bearers
[NR_RRC]   [UL] (cellID bc614e, UE ID 1 RNTI a616) Received RRCReconfigurationComplete
[NGAP]   initial_ctxt_resp_p: pdusession ID 1, gnb_addr 172.31.0.150, SIZE 4, TEID 2440808318
[NR_RRC]   Send message to sctp: NGAP_InitialContextSetupResponse
[NR_MAC]   DU received confirmation of successful RRC Reconfiguration
[NR_RRC]   [UL] (cellID bc614e, UE ID 1 RNTI a616) Received RRC UL Information Transfer [13 bytes]
[NR_PHY]   [RAPROC] 273.19 Initiating RA procedure with preamble 5, energy 48.0 dB (I0 353, thres 120), delay 16 start symbol 0 freq index 0
[NR_MAC]   273.19 UE RA-RNTI 010b TC-RNTI f7d6: initiating RA procedure
[NR_MAC]   UE f7d6: Msg3 scheduled at 274.17 (274.7 TDA 3) start 0 RBs 8
[NR_MAC]   UE f7d6: 274.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 5, timing_offset = 16 (estimated distance 625.0 [m])
[NR_MAC]   274.7 Send RAR to RA-RNTI 010b
[NR_MAC]    27510: RA RNTI f7d6 CC_id 0 Scheduling retransmission of Msg3 in (275,17)
[NR_MAC]    27610: RA RNTI f7d6 CC_id 0 Scheduling retransmission of Msg3 in (276,17)
[NR_MAC]    27710: RA RNTI f7d6 CC_id 0 Scheduling retransmission of Msg3 in (277,17)
[NR_MAC]   UE f7d6 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[NR_MAC]   Remove NR rnti 0xf7d6
[NR_MAC]   Frame.Slot 384.0
UE RNTI a616 CU-UE-ID 1 in-sync PH 61 dB PCMAX 21 dBm, average RSRP -56 (14 meas)
UE a616: UL-RI 1, TPMI 0
UE a616: dlsch_rounds 42/0/0/0, dlsch_errors 0, pucch0_DTX 0, BLER 0.03874 MCS (1) 1
UE a616: ulsch_rounds 250/0/0/0, ulsch_errors 0, ulsch_DTX 0, BLER 0.02824 MCS (1) 2 (Qm 2 deltaMCS 0 dB) NPRB 5  SNR 15.0 dB
UE a616: MAC:    TX           1805 RX          47375 bytes
UE a616: LCID 1: TX            355 RX           1714 bytes
UE a616: LCID 2: TX              3 RX             21 bytes
UE a616: LCID 4: TX            700 RX          35894 bytes

[NR_MAC]   Frame.Slot 512.0
UE RNTI a616 CU-UE-ID 1 in-sync PH 48 dB PCMAX 21 dBm, average RSRP -57 (16 meas)
UE a616: UL-RI 1, TPMI 0
UE a616: dlsch_rounds 71/0/0/0, dlsch_errors 0, pucch0_DTX 0, BLER 0.01853 MCS (1) 8
UE a616: ulsch_rounds 340/0/0/0, ulsch_errors 0, ulsch_DTX 0, BLER 0.00798 MCS (1) 6 (Qm 4 deltaMCS 0 dB) NPRB 5  SNR 16.0 dB
UE a616: MAC:    TX           5240 RX          54468 bytes
UE a616: LCID 1: TX            358 RX           1736 bytes
UE a616: LCID 2: TX              3 RX             21 bytes
UE a616: LCID 4: TX            883 RX          40074 bytes

[NR_MAC]   Frame.Slot 640.0
UE RNTI a616 CU-UE-ID 1 in-sync PH 48 dB PCMAX 21 dBm, average RSRP -57 (16 meas)
UE a616: UL-RI 1, TPMI 0
UE a616: dlsch_rounds 73/0/0/0, dlsch_errors 0, pucch0_DTX 0, BLER 0.01501 MCS (1) 6
UE a616: ulsch_rounds 354/0/0/0, ulsch_errors 0, ulsch_DTX 0, BLER 0.00225 MCS (1) 0 (Qm 2 deltaMCS 0 dB) NPRB 5  SNR 14.5 dB
UE a616: MAC:    TX           5570 RX          55025 bytes
UE a616: LCID 1: TX            361 RX           1766 bytes
UE a616: LCID 2: TX              3 RX             21 bytes
UE a616: LCID 4: TX            883 RX          40074 bytes

[NR_MAC]   Frame.Slot 768.0
UE RNTI a616 CU-UE-ID 1 in-sync PH 48 dB PCMAX 21 dBm, average RSRP -57 (16 meas)
UE a616: UL-RI 1, TPMI 0
UE a616: dlsch_rounds 76/0/0/0, dlsch_errors 0, pucch0_DTX 0, BLER 0.01094 MCS (1) 3
UE a616: ulsch_rounds 369/0/0/0, ulsch_errors 0, ulsch_DTX 0, BLER 0.00057 MCS (1) 0 (Qm 2 deltaMCS 0 dB) NPRB 5  SNR 14.5 dB
UE a616: MAC:    TX           5889 RX          55313 bytes
UE a616: LCID 1: TX            364 RX           1796 bytes
UE a616: LCID 2: TX              3 RX             21 bytes
UE a616: LCID 4: TX            883 RX          40074 bytes
```

 Le reste du journal est disponible dans le fichier `softmodem.log` complet.

---

## Indicateurs de succès détectés

- Initialisation du modem sans crash ✅
- Signal 5G capté avec bon SNR ✅
- L’UE s’est connecté au réseau avec succès ✅

---

## Références

- Projet OAI : [openairinterface5g](https://gitlab.eurecom.fr/oai/openairinterface5g)
- Programmation SIM : [OpenCells](https://open-cells.com/index.php/uiccsim-programing/)

## Success Indicators Detected

* Modem initialized without crash ✅
* 5G signal captured with good SNR ✅
* UE successfully connected to the network ✅

---

## References

* OAI Project: [openairinterface5g](https://gitlab.eurecom.fr/oai/openairinterface5g)
* SIM Programming: [OpenCells](https://open-cells.com/index.php/uiccsim-programing/)

