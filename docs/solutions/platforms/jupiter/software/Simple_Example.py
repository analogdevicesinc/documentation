
import numpy as np
import adi


sdr = adi.adrv9002(uri="ip:10.75.162.75")

# Enable and configure RX0 simply
sdr.rx0_en = 1     # RX channel 0 (I/Q)
sdr.rx1_en = 1     # RX channel 1 (I/Q)

sdr.rx_ensm_mode_chan0 = "rf_enabled"
sdr.rx_ensm_mode_chan1 = "rf_enabled"



# Basic tuning (must be valid for the active profile on Jupiter)
lo = int(2.4e9)
sdr.rx0_lo = lo
sdr.rx1_lo = lo


# Inspect (read-only) values from the active profile
print("Channel 1's Current sample rate:", sdr.rx0_sample_rate)
print("Channel 1's Current RF BW:", sdr.rx0_rf_bandwidth)

print("Channel 2's Current sample rate:", sdr.rx1_sample_rate)
print("Channel 2's Current RF BW:", sdr.rx1_rf_bandwidth)


sdr.rx_buffer_size = 4096

iq = sdr.rx()

# ADRV9002 returns a NumPy array shaped (channels, samples)
rx0 = iq[0]
rx1 = iq[1]

print("RX0 first 10:", rx0[:10])
print("RX1 first 10:", rx1[:10])


