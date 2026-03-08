#!/bin/sh

# Auto-run TX tone script for PlutoSDR (no Python required)
# Equivalent to standalone_pluto_tx.py using iio_attr + DDS
# Transmits a 300 kHz baseband tone with -90° phase shift

cd /media/sda/

# Log file for debugging
LOG=foobar.txt
touch $LOG

echo "=== PlutoSDR TX Tone Script ===" >> $LOG
date >> $LOG

# ----- Configuration (match standalone_pluto_tx.py) -----
LO_FREQ=5399700000          # 5400000000 - 300000 Hz
TX_BASEBAND_FREQ=300000     # 300 kHz baseband tone
TX_GAIN=0                   # TX hardware gain (0 dB = max power)

# ----- Set LED to solid (indicate script is running) -----
echo default-on > /sys/class/leds/led0:green/trigger 2>> $LOG

# ----- Configure TX LO -----
echo "Setting TX LO to $LO_FREQ" >> $LOG
/usr/bin/iio_attr -u local: -c ad9361-phy TX_LO frequency $LO_FREQ >> $LOG 2>&1

# ----- Configure TX gain (attenuation) -----
echo "Setting TX hardwaregain to $TX_GAIN" >> $LOG
/usr/bin/iio_attr -u local: -c -o ad9361-phy voltage0 hardwaregain $TX_GAIN >> $LOG 2>&1

# ----- Enable DDS tone at TX_BASEBAND_FREQ with -90° phase shift -----
# Python waveform: samples = A * (cos(2πft - π/2) + j*sin(2πft - π/2))
#   I = cos(2πft - π/2) = sin(2πft)    → DDS phase = 270000 millideg (≡ -90°)
#   Q = sin(2πft - π/2) = -cos(2πft)   → DDS phase = 180000 millideg (≡ 180°)
#
# DDS channels on cf-ad9361-dds-core-lpc:
#   altvoltage0 = TX1_I_F1   altvoltage1 = TX1_I_F2
#   altvoltage2 = TX1_Q_F1   altvoltage3 = TX1_Q_F2

echo "Configuring DDS tone at ${TX_BASEBAND_FREQ} Hz (phase_shift = -90 deg)" >> $LOG

# TX1_I_F1: sin(2πft) = cos(2πft - 90°) → phase 270000
/usr/bin/iio_attr -u local: -c cf-ad9361-dds-core-lpc altvoltage0 frequency $TX_BASEBAND_FREQ >> $LOG 2>&1
/usr/bin/iio_attr -u local: -c cf-ad9361-dds-core-lpc altvoltage0 scale 0.5 >> $LOG 2>&1
/usr/bin/iio_attr -u local: -c cf-ad9361-dds-core-lpc altvoltage0 phase 270000 >> $LOG 2>&1
/usr/bin/iio_attr -u local: -c cf-ad9361-dds-core-lpc altvoltage0 raw 1 >> $LOG 2>&1

# TX1_I_F2: disable
/usr/bin/iio_attr -u local: -c cf-ad9361-dds-core-lpc altvoltage1 scale 0 >> $LOG 2>&1
/usr/bin/iio_attr -u local: -c cf-ad9361-dds-core-lpc altvoltage1 raw 1 >> $LOG 2>&1

# TX1_Q_F1: -cos(2πft) = cos(2πft + 180°) → phase 180000
/usr/bin/iio_attr -u local: -c cf-ad9361-dds-core-lpc altvoltage2 frequency $TX_BASEBAND_FREQ >> $LOG 2>&1
/usr/bin/iio_attr -u local: -c cf-ad9361-dds-core-lpc altvoltage2 scale 0.5 >> $LOG 2>&1
/usr/bin/iio_attr -u local: -c cf-ad9361-dds-core-lpc altvoltage2 phase 180000 >> $LOG 2>&1
/usr/bin/iio_attr -u local: -c cf-ad9361-dds-core-lpc altvoltage2 raw 1 >> $LOG 2>&1

# TX1_Q_F2: disable
/usr/bin/iio_attr -u local: -c cf-ad9361-dds-core-lpc altvoltage3 scale 0 >> $LOG 2>&1
/usr/bin/iio_attr -u local: -c cf-ad9361-dds-core-lpc altvoltage3 raw 1 >> $LOG 2>&1

echo "TX tone active at LO + ${TX_BASEBAND_FREQ} Hz" >> $LOG
echo "Done." >> $LOG

# ----- Safely unmount the USB drive so it can be removed -----
cd /root
ACTION=remove_all /lib/mdev/automounter.sh