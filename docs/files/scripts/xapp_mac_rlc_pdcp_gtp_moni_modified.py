import xapp_sdk as ric
import time
import os
import pdb

####################
#### MAC INDICATION CALLBACK
####################

#  MACCallback class is defined and derived from C++ class mac_cb
class MACCallback(ric.mac_cb):
    def __init__(self):
        ric.mac_cb.__init__(self)

    def handle(self, ind):
        try:
            print(f"📡 MAC Indication received with {len(ind.ue_stats)} UEs")

            for i, ue in enumerate(ind.ue_stats):
                rnti = getattr(ue, 'rnti', 'N/A')
                phr = getattr(ue, 'phr', 'N/A')
                bsr = getattr(ue, 'bsr', 'N/A')
                wb_cqi = getattr(ue, 'wb_cqi', 'N/A')

                dl_mcs1 = getattr(ue, 'dl_mcs1', 'N/A')
                dl_mcs2 = getattr(ue, 'dl_mcs2', 'N/A')
                ul_mcs1 = getattr(ue, 'ul_mcs1', 'N/A')
                ul_mcs2 = getattr(ue, 'ul_mcs2', 'N/A')

                dl_aggr_tbs = getattr(ue, 'dl_aggr_tbs', 'N/A')
                ul_aggr_tbs = getattr(ue, 'ul_aggr_tbs', 'N/A')
                dl_curr_tbs = getattr(ue, 'dl_curr_tbs', 'N/A')
                ul_curr_tbs = getattr(ue, 'ul_curr_tbs', 'N/A')

                dl_sched_rb = getattr(ue, 'dl_sched_rb', 'N/A')
                ul_sched_rb = getattr(ue, 'ul_sched_rb', 'N/A')

                dl_aggr_prb = getattr(ue, 'dl_aggr_prb', 'N/A')
                ul_aggr_prb = getattr(ue, 'ul_aggr_prb', 'N/A')
                dl_aggr_retx_prb = getattr(ue, 'dl_aggr_retx_prb', 'N/A')
                ul_aggr_retx_prb = getattr(ue, 'ul_aggr_retx_prb', 'N/A')

                pusch_snr = getattr(ue, 'pusch_snr', 'N/A')
                pucch_snr = getattr(ue, 'pucch_snr', 'N/A')

                dl_bler = getattr(ue, 'dl_bler', 'N/A')
                ul_bler = getattr(ue, 'ul_bler', 'N/A')

                frame = getattr(ue, 'frame', 'N/A')
                slot = getattr(ue, 'slot', 'N/A')

                print(f"🔸 UE[{i}] RNTI={rnti} | PHR={phr} | BSR={bsr} | CQI={wb_cqi}")
                print(f"    MCS (DL1={dl_mcs1}, DL2={dl_mcs2} | UL1={ul_mcs1}, UL2={ul_mcs2})")
                print(f"    TBS (DL={dl_aggr_tbs}, UL={ul_aggr_tbs} | Curr DL={dl_curr_tbs}, Curr UL={ul_curr_tbs})")
                print(f"    Sched RBs (DL={dl_sched_rb}, UL={ul_sched_rb})")
                print(f"    PRBs Used (DL={dl_aggr_prb}, UL={ul_aggr_prb}) | Retx (DL={dl_aggr_retx_prb}, UL={ul_aggr_retx_prb})")
                print(f"    SNR (PUSCH={pusch_snr} dB | PUCCH={pucch_snr} dB)")
                print(f"    BLER (DL={dl_bler}, UL={ul_bler})")
                print(f"    Frame={frame} | Slot={slot}")

            # Timestamp / latency info
            if hasattr(ind, "tstamp"):
                t_now = time.time_ns() / 1000.0
                t_mac = ind.tstamp / 1.0
                latency = t_now - t_mac
                print(f"\n🕒 MAC tstamp = {t_mac:.0f} μs | Latency = {latency:.2f} μs")
            else:
                print("⚠️ No 'tstamp' found in MAC indication")

        except Exception as e:
            print(f"❌ Error during MAC metric parsing: {e}")

                    # print(dir(ue))  # Uncomment to explore further

####################
#### RLC INDICATION CALLBACK
####################

class RLCCallback(ric.rlc_cb):
    def __init__(self):
        ric.rlc_cb.__init__(self)

    def handle(self, ind):
        try:
            print(f"📡 RLC Indication received with {len(ind.rb_stats)} RBs")

            for i, rb in enumerate(ind.rb_stats):
                rnti     = getattr(rb, 'rnti', 'N/A')
                lcid     = getattr(rb, 'lcid', 'N/A')
                mode     = getattr(rb, 'mode', 'N/A')
                tx_bytes = getattr(rb, 'tx_bytes', 'N/A')
                rx_bytes = getattr(rb, 'rx_bytes', 'N/A')
                sn_tx    = getattr(rb, 'sn_tx', 'N/A')
                sn_rx    = getattr(rb, 'sn_rx', 'N/A')
                tx_sdu   = getattr(rb, 'tx_sdu', 'N/A')
                rx_sdu   = getattr(rb, 'rx_sdu', 'N/A')
                tx_pdu   = getattr(rb, 'tx_pdu', 'N/A')
                rx_pdu   = getattr(rb, 'rx_pdu', 'N/A')
                tx_retx  = getattr(rb, 'tx_retx', 'N/A')
                status   = getattr(rb, 'status', 'N/A')

                print(f"🔸 RB[{i}] RNTI={rnti} | LCID={lcid} | Mode={mode} | Status={status}")
                print(f"    TX: {tx_bytes} bytes / {tx_pdu} PDUs / {tx_sdu} SDUs | Retransmissions: {tx_retx}")
                print(f"    RX: {rx_bytes} bytes / {rx_pdu} PDUs / {rx_sdu} SDUs")
                print(f"    SN_TX={sn_tx} | SN_RX={sn_rx}")

            if hasattr(ind, "tstamp"):
                t_now = time.time_ns() / 1000.0
                t_rlc = ind.tstamp / 1.0
                latency = t_now - t_rlc
                print(f"\n🕒 RLC tstamp = {t_rlc:.0f} μs | Latency = {latency:.2f} μs")
            else:
                print("⚠️ No 'tstamp' found in RLC indication")

        except Exception as e:
            print(f"❌ Error during RLC metric parsing: {e}")

####################
#### PDCP INDICATION CALLBACK
####################

class PDCPCallback(ric.pdcp_cb):
    def __init__(self):
        ric.pdcp_cb.__init__(self)

    def handle(self, ind):
        try:
            print(f"📡 PDCP Indication received with {len(ind.rb_stats)} RBs")

            for i, rb in enumerate(ind.rb_stats):
                rnti = getattr(rb, 'rnti', 'N/A')
                lcid = getattr(rb, 'lcid', 'N/A')
                status = getattr(rb, 'status', 'N/A')

                tx_pkts = getattr(rb, 'txpdu_pkts', 'N/A')
                tx_bytes = getattr(rb, 'txpdu_bytes', 'N/A')
                tx_sn = getattr(rb, 'txpdu_sn', 'N/A')
                tx_wt = getattr(rb, 'txpdu_wt', 'N/A')
                tx_disc_pkts = getattr(rb, 'txpdu_pkts_discarded', 'N/A')
                tx_disc_bytes = getattr(rb, 'txpdu_bytes_discarded', 'N/A')
                tx_retx_pkts = getattr(rb, 'txpdu_retx_pkts', 'N/A')
                tx_retx_bytes = getattr(rb, 'txpdu_retx_bytes', 'N/A')

                rx_pkts = getattr(rb, 'rxpdu_pkts', 'N/A')
                rx_bytes = getattr(rb, 'rxpdu_bytes', 'N/A')
                rx_dup_pkts = getattr(rb, 'rxpdu_dup_pkts', 'N/A')
                rx_dup_bytes = getattr(rb, 'rxpdu_dup_bytes', 'N/A')
                rx_ooo_pkts = getattr(rb, 'rxpdu_ooo_pkts', 'N/A')
                rx_ooo_bytes = getattr(rb, 'rxpdu_ooo_bytes', 'N/A')
                rx_drop_pkts = getattr(rb, 'rxpdu_drop_pkts', 'N/A')
                rx_drop_bytes = getattr(rb, 'rxpdu_drop_bytes', 'N/A')
                rx_valid_pkts = getattr(rb, 'rxpdu_valid_pkts', 'N/A')
                rx_valid_bytes = getattr(rb, 'rxpdu_valid_bytes', 'N/A')
                rx_sn = getattr(rb, 'rxpdu_sn', 'N/A')
                rx_wt = getattr(rb, 'rxpdu_wt', 'N/A')

                print(f"🔸 RB[{i}] RNTI={rnti} | LCID={lcid} | Status={status}")
                print(f"    TX: {tx_pkts} pkts / {tx_bytes} bytes | SN={tx_sn} | WT={tx_wt}")
                print(f"        Discarded: {tx_disc_pkts} pkts / {tx_disc_bytes} bytes | Retx: {tx_retx_pkts} pkts / {tx_retx_bytes} bytes")
                print(f"    RX: {rx_pkts} pkts / {rx_bytes} bytes | SN={rx_sn} | WT={rx_wt}")
                print(f"        Duplicates: {rx_dup_pkts} pkts / {rx_dup_bytes} bytes")
                print(f"        Out-of-Order: {rx_ooo_pkts} pkts / {rx_ooo_bytes} bytes")
                print(f"        Dropped: {rx_drop_pkts} pkts / {rx_drop_bytes} bytes")
                print(f"        Validated: {rx_valid_pkts} pkts / {rx_valid_bytes} bytes")

            if hasattr(ind, "tstamp"):
                t_now = time.time_ns() / 1000.0
                t_pdcp = ind.tstamp / 1.0
                latency = t_now - t_pdcp
                print(f"\n🕒 PDCP tstamp = {t_pdcp:.0f} μs | Latency = {latency:.2f} μs")
            else:
                print("⚠️ No 'tstamp' found in PDCP indication")

        except Exception as e:
            print(f"❌ Error during PDCP metric parsing: {e}")

            # print('PDCP rnti = '+ str(ind.rb_stats[0].rnti))

####################
#### GTP INDICATION CALLBACK
####################

# Create a callback for GTP which derived it from C++ class gtp_cb
class GTPCallback(ric.gtp_cb):
    def __init__(self):
        ric.gtp_cb.__init__(self)

    def handle(self, ind):
        try:
            print(f"📡 GTP Indication received with {len(ind.gtp_stats)} tunnels")

            for i, stat in enumerate(ind.gtp_stats):
                teid = getattr(stat, 'teid', 'N/A')
                status = getattr(stat, 'status', 'N/A')

                tx_bytes = getattr(stat, 'tx_total_bytes', 'N/A')
                rx_bytes = getattr(stat, 'rx_total_bytes', 'N/A')
                tx_pkts = getattr(stat, 'tx_total_pkts', 'N/A')
                rx_pkts = getattr(stat, 'rx_total_pkts', 'N/A')
                tx_drop = getattr(stat, 'tx_drop_bytes', 'N/A')
                rx_drop = getattr(stat, 'rx_drop_bytes', 'N/A')

                print(f"🔸 Tunnel[{i}] TEID={teid} | Status={status}")
                print(f"    TX: {tx_pkts} pkts / {tx_bytes} bytes | Drops: {tx_drop} bytes")
                print(f"    RX: {rx_pkts} pkts / {rx_bytes} bytes | Drops: {rx_drop} bytes")

            if hasattr(ind, "tstamp"):
                t_now = time.time_ns() / 1000.0
                t_gtp = ind.tstamp / 1.0
                latency = t_now - t_gtp
                print(f"\n🕒 GTP tstamp = {t_gtp:.0f} μs | Latency = {latency:.2f} μs")
            else:
                print("⚠️ No 'tstamp' found in GTP indication")

        except Exception as e:
            print(f"❌ Error during GTP metric parsing: {e}")


####################
####  GENERAL 
####################

ric.init()

conn = ric.conn_e2_nodes()
assert(len(conn) > 0)
for i in range(0, len(conn)):
    print("Global E2 Node [" + str(i) + "]: PLMN MCC = " + str(conn[i].id.plmn.mcc))
    print("Global E2 Node [" + str(i) + "]: PLMN MNC = " + str(conn[i].id.plmn.mnc))

####################
#### MAC INDICATION
####################

mac_hndlr = []
for i in range(0, len(conn)):
    mac_cb = MACCallback()
    hndlr = ric.report_mac_sm(conn[i].id, ric.Interval_ms_1, mac_cb)
    mac_hndlr.append(hndlr)     
    time.sleep(1)

####################
#### RLC INDICATION
####################

rlc_hndlr = []
for i in range(0, len(conn)):
    rlc_cb = RLCCallback()
    hndlr = ric.report_rlc_sm(conn[i].id, ric.Interval_ms_1, rlc_cb)
    rlc_hndlr.append(hndlr) 
    time.sleep(1)

####################
#### PDCP INDICATION
####################

pdcp_hndlr = []
for i in range(0, len(conn)):
    pdcp_cb = PDCPCallback()
    hndlr = ric.report_pdcp_sm(conn[i].id, ric.Interval_ms_1, pdcp_cb)
    pdcp_hndlr.append(hndlr) 
    time.sleep(1)

####################
#### GTP INDICATION
####################

gtp_hndlr = []
for i in range(0, len(conn)):
    gtp_cb = GTPCallback()
    hndlr = ric.report_gtp_sm(conn[i].id, ric.Interval_ms_1, gtp_cb)
    gtp_hndlr.append(hndlr)
    time.sleep(1)

print("Before sleep")

time.sleep(10)

### End


print("Before MAC")
for i in range(0, len(mac_hndlr)):
    ric.rm_report_mac_sm(mac_hndlr[i])

print("Before RLC")
for i in range(0, len(rlc_hndlr)):
    ric.rm_report_rlc_sm(rlc_hndlr[i])

print("Before PDCP")
for i in range(0, len(pdcp_hndlr)):
    ric.rm_report_pdcp_sm(pdcp_hndlr[i])

print("Before GTP")
for i in range(0, len(gtp_hndlr)):
    ric.rm_report_gtp_sm(gtp_hndlr[i])




# Avoid deadlock. ToDo revise architecture 
while ric.try_stop == 0:
    time.sleep(1)

print("Test finished")
