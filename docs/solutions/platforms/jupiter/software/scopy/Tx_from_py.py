import numpy as np
import adi

# Step 1: Change this to your Jupiter's IP
URI = "ip:10.75.162.78"

# ----------------------------
# USER OPTIONS
# ----------------------------
TX_ON = True          # Step 2: True = transmit tone, False = stop TX (see below)
USE_CYCLIC = True     # True = repeats forever (easy for Scopy), False = one-shot buffer

# --- Tiny FYI: Dual-TX with different tones ---
# If you enable two TX channels, you must provide TWO IQ arrays (one per channel). [1](https://analogdevicesinc.github.io/scopy/tests/plugins/adrv9002/adrv9002_tests.html)[2](https://ez.analog.com/rf/wide-band-rf-transceivers/design-support-adrv9001-adrv9007/f/q-a/568350/adrv-9002-eval-board-continuous-transmit-via-software)
TONE_HZ_CH0 = 3.8e6   # TX1 tone (channel 0)
TONE_HZ_CH1 = 3.6e6   # TX2 tone (channel 1)  <-- change as desired

# ----------------------------
# Connect
# ----------------------------
sdr = adi.adrv9002(uri=URI)

# ----------------------------
# Pick TX channel(s)
#   Channel 0 -> TX1
#   Channel 1 -> TX2
# ----------------------------
sdr.tx_enabled_channels = [0,1]   # TX1 and TX2

sdr.tx_ensm_mode_chan0 = "rf_enabled" # Enable Transmit for chan0
sdr.tx_ensm_mode_chan1 = "rf_enabled" # Enable Transmit for chan1

# Optional: set TX LO (only if you want to control carrier here)
# sdr.tx0_lo = lo

# ----------------------------
# Check sample rate for correct tone placement
# ----------------------------
fs = float(sdr.tx0_sample_rate)
print("TX sample rate (fs):", fs)

# ----------------------------
# Build TX waveform(s)
# ----------------------------
N = 4096
t = np.arange(N) / fs

# Keep amplitude modest to avoid clipping
amp = .2

iq0 = (amp * np.exp(1j * 2 * np.pi * TONE_HZ_CH0 * t)).astype(np.complex64)
iq1 = (amp * np.exp(1j * 2 * np.pi * TONE_HZ_CH1 * t)).astype(np.complex64)

# ----------------------------
# TRANSMIT / STOP
# ----------------------------
if TX_ON:
    # (Recommended for Scopy) Cyclic buffer keeps transmitting the same waveform
    sdr.tx_cyclic_buffer = USE_CYCLIC

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