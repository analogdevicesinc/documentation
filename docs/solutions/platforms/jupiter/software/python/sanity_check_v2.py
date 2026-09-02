import numpy as np
import adi
import matplotlib.pyplot as plt

# Connect to Jupiter
sdr = adi.adrv9002(uri="ip:10.75.162.51")  # <-- Change to your Jupiter's IP

# Enable RF state machines
sdr.rx_ensm_mode_chan0 = "rf_enabled"
sdr.rx_ensm_mode_chan1 = "rf_enabled"
sdr.tx_ensm_mode_chan0 = "rf_enabled"
sdr.tx_ensm_mode_chan1 = "rf_enabled"

# Observe settings set by the profile
print("RX0 sample rate:", sdr.rx0_sample_rate)
print("RX0 RF bandwidth:", sdr.rx0_rf_bandwidth)
print("RX1 sample rate:", sdr.rx1_sample_rate)
print("RX1 RF bandwidth:", sdr.rx1_rf_bandwidth)

# Create two sinewave waveforms for TX
fs = int(sdr.rx0_sample_rate)
N = 2**16
ts = 1 / float(fs)
t = np.arange(0, N * ts, ts)

fc0 = 0.5e6  # Tone 0: 0.5 MHz
i0 = np.cos(2 * np.pi * t * fc0) * 2 ** 14
q0 = np.sin(2 * np.pi * t * fc0) * 2 ** 14
iq0 = i0 + 1j * q0

fc1 = 1e6  # Tone 1: 1.0 MHz
i1 = np.cos(2 * np.pi * t * fc1) * 2 ** 14
q1 = np.sin(2 * np.pi * t * fc1) * 2 ** 14
iq1 = i1 + 1j * q1

# =============================================================================
# STANDALONE TX: split DMA, each channel has its own DMA engine.
# tx1() and tx2() are methods that PyADI adds automatically in split mode.
# If using an MCS image, comment this section out and uncomment the MCS
# section below.
# =============================================================================
sdr.tx_cyclic_buffer = True
sdr.tx2_cyclic_buffer = True
sdr.tx1(iq0)
sdr.tx2(iq1)

# =============================================================================
# MCS TX: shared DMA, send both channels at once.
# If using an MCS image, uncomment this section and comment out the standalone
# section above.
# =============================================================================
# sdr.tx_cyclic_buffer = True
# sdr.tx_enabled_channels = [0, 1]
# sdr.tx([iq0, iq1])

# =============================================================================
# STANDALONE RX: split DMA, each channel has its own DMA engine.
# rx1() and rx2() are methods that PyADI adds automatically in split mode.
# If using an MCS image, comment this section out and uncomment the MCS
# section below.
# =============================================================================
sdr.rx_buffer_size = N
sdr.rx2_buffer_size = N
rx0 = sdr.rx1()
rx1 = sdr.rx2()

# =============================================================================
# MCS RX: shared DMA, receive both channels at once.
# If using an MCS image, uncomment this section and comment out the standalone
# section above.
# =============================================================================
# sdr.rx_enabled_channels = [0, 1]
# sdr.rx_buffer_size = N
# rx_data = sdr.rx()
# rx0 = rx_data[0]
# rx1 = rx_data[1]

print(f"Received {len(rx0)} samples per channel.")
print(f"RX0 max amplitude: {np.max(np.abs(rx0)):.1f}")
print(f"RX1 max amplitude: {np.max(np.abs(rx1)):.1f}")

# Compute spectrum
fs_rx = float(sdr.rx0_sample_rate)

window0 = np.hanning(len(rx0))
xw0 = rx0 * window0
X0 = np.fft.fftshift(np.fft.fft(xw0))
freq0 = np.fft.fftshift(np.fft.fftfreq(len(rx0), 1/fs_rx))
mag_db0 = 20 * np.log10(np.abs(X0) / np.max(np.abs(X0)))

window1 = np.hanning(len(rx1))
xw1 = rx1 * window1
X1 = np.fft.fftshift(np.fft.fft(xw1))
freq1 = np.fft.fftshift(np.fft.fftfreq(len(rx1), 1/fs_rx))
mag_db1 = 20 * np.log10(np.abs(X1) / np.max(np.abs(X1)))

# Plot results
plt.figure(figsize=(10, 4))
plt.plot(freq0 / 1e6, mag_db0, label="RX0", color="tab:blue")
plt.plot(freq1 / 1e6, mag_db1, label="RX1", color="tab:orange")
plt.axvline(fc0 / 1e6, color="tab:blue", linestyle="--", alpha=0.7, label=f"{fc0/1e6:.1f} MHz")
plt.axvline(fc1 / 1e6, color="tab:orange", linestyle="--", alpha=0.7, label=f"{fc1/1e6:.1f} MHz")
plt.title("Jupiter RX Spectrum - TX Loopback Tones")
plt.xlabel("Frequency [MHz]")
plt.ylabel("Magnitude [dB, normalized]")
plt.legend(loc="lower left")
plt.grid(True)
plt.tight_layout()
plt.show()

# Cleanup
sdr.tx_destroy_buffer()
