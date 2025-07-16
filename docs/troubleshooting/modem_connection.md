# Troubleshooting Modem Connection (Quectel-CM)

This guide provides steps to resolve issues when the modem is not detected or does not get an IP address.

---

## Step 1: Unplug the Modem

Unplug the Quectel modem (USB-C) from the PC.

---

## Step 2: Clean Docker Resources

Recommended method:

```bash
docker rmi -f $(docker images -q)
docker volume prune -f
docker network prune -f
```

Alternative method (more aggressive):

```bash
docker system prune -a
```

---

## Step 3: Rebuild and Launch Core Network

```bash
cd ~/OAI-5GCN-v2.0.1/docker-compose
python3 core-network.py --type start-basic --scenario 1
```

Make sure all containers are running and healthy.

---

## Step 4: Launch gNodeB

```bash
cd ~/openairinterface5g/cmake_targets/ran_build/build/
sudo ./nr-softmodem -O config/5GN78.conf --sa -E --continuous-tx
```

---

## Step 5: Reconnect the Modem

Now reconnect the modem via USB-C. Wait for the gNB to detect the device. You should see detection logs appear.

> When you see things like this below ;
```log
[NR_MAC]   Frame.Slot 768.0
UE RNTI c652 CU-UE-ID 1 in-sync PH 40 dB PCMAX 21 dBm, average RSRP -86 (12 meas)
UE c652: dlsch_rounds 16/1/1/0, dlsch_errors 0, pucch0_DTX 2, BLER 0.09550 MCS (0) 0
UE c652: ulsch_rounds 54/3/1/0, ulsch_errors 0, ulsch_DTX 2, BLER 0.00591 MCS (0) 0 (Qm 2 deltaMCS 0 dB) NPRB 5  SNR 12.5 dB
UE c652: MAC:    TX            414 RX           2604 bytes
UE c652: LCID 1: TX            212 RX           1736 bytes

[NR_MAC]   Frame.Slot 896.0
UE RNTI c652 CU-UE-ID 1 in-sync PH 40 dB PCMAX 21 dBm, average RSRP -86 (9 meas)
UE c652: dlsch_rounds 17/1/1/0, dlsch_errors 0, pucch0_DTX 2, BLER 0.08595 MCS (0) 0
UE c652: ulsch_rounds 67/3/1/0, ulsch_errors 0, ulsch_DTX 2, BLER 0.00150 MCS (0) 0 (Qm 2 deltaMCS 0 dB) NPRB 5  SNR 13.5 dB
UE c652: MAC:    TX            431 RX           2825 bytes
UE c652: LCID 1: TX            212 RX           1736 bytes

[NR_MAC]   Frame.Slot 0.0
UE RNTI c652 CU-UE-ID 1 in-sync PH 38 dB PCMAX 21 dBm, average RSRP -86 (14 meas)
UE c652: dlsch_rounds 19/1/1/0, dlsch_errors 0, pucch0_DTX 2, BLER 0.06962 MCS (0) 0
UE c652: ulsch_rounds 80/3/1/0, ulsch_errors 0, ulsch_DTX 2, BLER 0.00038 MCS (0) 0 (Qm 2 deltaMCS 0 dB) NPRB 5  SNR 13.0 dB
UE c652: MAC:    TX            465 RX           3046 bytes
UE c652: LCID 1: TX            212 RX           1736 bytes

[NR_MAC]   Frame.Slot 128.0
UE RNTI c652 CU-UE-ID 1 in-sync PH 38 dB PCMAX 21 dBm, average RSRP -86 (11 meas)
UE c652: dlsch_rounds 20/1/1/0, dlsch_errors 0, pucch0_DTX 2, BLER 0.06266 MCS (0) 0
UE c652: ulsch_rounds 93/3/1/0, ulsch_errors 0, ulsch_DTX 2, BLER 0.00010 MCS (0) 0 (Qm 2 deltaMCS 0 dB) NPRB 5  SNR 13.5 dB
UE c652: MAC:    TX            482 RX           3267 bytes
UE c652: LCID 1: TX            212 RX           1736 bytes 
```

---

## Step 6: Launch Quectel-CM

After detection (\~1 min), launch:

```bash
cd ~/Documents/quectel/quectel-CM/out
sudo ./quectel-CM -s oai
```

Try this multiple times if it doesn't work the first time.

---

## Step 7: Use AT Command as Fallback

If Quectel-CM does not attach:

```bash
sudo minicom -D /dev/ttyUSB2
```

Then type:

```text
AT+COPS=0
```

> Good luck :) !