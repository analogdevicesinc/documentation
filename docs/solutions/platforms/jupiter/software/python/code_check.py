#-----------------------
## Checking Connectivity
#-----------------------
import numpy as np
import adi
import matplotlib.pyplot as plt

# call adrv9002, set IP
sdr = adi.adrv9002(uri="ip:10.75.162.74") 



# Enable and configure RX0 
sdr.rx0_en = 1     # RX channel 0 (I/Q)
sdr.rx1_en = 1     # RX channel 1 (I/Q)

#---------------
# Setting up Rx
#---------------

sdr.rx_ensm_mode_chan0 = "rf_enabled"
# sdr.rx_ensm_mode_chan1 = "rf_enabled"

# Basic tuning (must be valid for the active profile on Jupiter)
# lo = int(2.4e9)
# sdr.rx0_lo = lo
# sdr.rx1_lo = lo


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

#---------
# Transmit
#---------
TX_ON = True          # True = transmit tone, False = stop TX (see below)
USE_CYCLIC = True     # True = repeats forever (easy for Scopy), False = one-shot buffer
# If you enable two TX channels, you must provide TWO IQ arrays (one per channel). [1](https://analogdevicesinc.github.io/scopy/tests/plugins/adrv9002/adrv9002_tests.html)[2](https://ez.analog.com/rf/wide-band-rf-transceivers/design-support-adrv9001-adrv9007/f/q-a/568350/adrv-9002-eval-board-continuous-transmit-via-software)
TONE_HZ_CH0 = 500000   # TX1 tone (channel 0)
TONE_HZ_CH1 = .7e6   # TX2 tone (channel 1)  <-- change as desired

# sdr.tx0_lo = lo
# sdr.tx1_lo = lo

sdr.tx_enabled_channels = [0,1]   # TX1 and TX2

sdr.tx_ensm_mode_chan0 = "rf_enabled" # Enable Transmit for chan0
sdr.tx_ensm_mode_chan1 = "rf_enabled" # Enable Transmit for chan1

# Optional: set TX LO (only if you want to control carrier here)
# sdr.tx0_lo = lo


# Check sample rate for correct tone placement
fs = float(sdr.tx0_sample_rate)
print("TX sample rate (fs):", fs)


# Build TX waveform(s)
N = 4096
t = np.arange(N) / fs

# Keep amplitude modest to avoid clipping
amp = .8

iq0 = (amp * np.exp(1j * 2 * np.pi * TONE_HZ_CH0 * t)).astype(np.complex64)
iq1 = (amp * np.exp(1j * 2 * np.pi * TONE_HZ_CH1 * t)).astype(np.complex64)


# TRANSMIT / STOP
if TX_ON:
    # Cyclic buffer keeps transmitting the same waveform
    sdr.tx_cyclic_buffer = True

    # Dual TX: pass one waveform per enabled TX channel [1](https://analogdevicesinc.github.io/scopy/tests/plugins/adrv9002/adrv9002_tests.html)[2](https://ez.analog.com/rf/wide-band-rf-transceivers/design-support-adrv9001-adrv9007/f/q-a/568350/adrv-9002-eval-board-continuous-transmit-via-software)
    sdr.tx([iq0, iq1])

    print(f"TX ON: TX1={TONE_HZ_CH0/1e6:.3f} MHz, TX2={TONE_HZ_CH1/1e6:.3f} MHz (cyclic={USE_CYCLIC}).")
    print("To stop: set TX_ON=False and run again, or call tx_destroy_buffer() as shown below.")
else:
    # --- TX OFF METHOD A (recommended): destroy the cyclic buffer if it exists ---
    # Needed because cyclic buffers keep running until destroyed. [2](https://ez.analog.com/rf/wide-band-rf-transceivers/design-support-adrv9001-adrv9007/f/q-a/568350/adrv-9002-eval-board-continuous-transmit-via-software)
    try:
        sdr.tx_destroy_buffer()
        print("TX OFF: destroyed TX buffer (stops cyclic transmit).")
    except Exception as e:
        print("TX OFF: tx_destroy_buffer() not available or no buffer to destroy:", e)



# -------------------------
# Magnitude Spectrum (RX0)
# -------------------------

fs_rx = float(sdr.rx0_sample_rate)   # Sample rate (Hz)
N = len(rx0)

print("RX0 length ", len(rx0))

# Apply window to reduce spectral leakage
window = np.hanning(N)
xw = rx0 * window

# FFT
X = np.fft.fftshift(np.fft.fft(xw))
freq = np.fft.fftshift(np.fft.fftfreq(N, d=1/fs_rx))

# Magnitude in dBFS (relative)
mag_db = 20 * np.log10(np.abs(X) / np.max(np.abs(X)))

plt.figure(figsize=(10, 4))
plt.plot(freq / 1e6, mag_db)
plt.title("RX0 Gain vs Frequency")
plt.xlabel("Frequency [MHz]")
plt.ylabel("Magnitude [dBFS]")
plt.grid(True)
plt.tight_layout()
plt.show()
