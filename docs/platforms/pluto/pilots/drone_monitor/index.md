---
orphan: true
---

# Pluto Drone Monitor & Control Demo
```{attention}
Work-in-progress
```
## Overview

This demo shows how to use an ADALM-PLUTO (Pluto SDR) as a **passive
spectrum monitor** for common UAV/UAS control and video bands (2.4 GHz
and 5.8 GHz). It provides a real-time spectrogram, basic signal
classification (e.g., *OFDM-ish* vs *narrowband/RC-like*), and a simple
event log. The goal is to demonstrate ADEF-relevant **Counter-UAS
awareness**: seeing band activity, identifying likely signal types, and
discussing next steps such as zooming, hopping detection, or AoA with
additional hardware.

## Hardware Setup

**Required** - 1× ADI ADALM-PLUTO (Pluto SDR) - PC/laptop (Windows,
Linux, or macOS) - USB cable (micro-USB to USB-A/C as appropriate) -
Antenna for **2.4 GHz** (and optionally **5.8 GHz**) with SMA adapter as
needed

**Recommended** - Directional/panel antenna (2.4/5.8 GHz) for better SNR
and spatial discrimination - Fixed attenuators (e.g., 20–40 dB) for
close-range/near-field captures - USB ferrite choke to reduce conducted
noise - Tripod or stand for antenna

**Connections** 1. Connect the antenna to Pluto SDR **RX** port (SMA).
2. Connect Pluto to the host PC via USB. 3. (Optional) If using
Ethernet-over-USB, ensure the Pluto enumerates at 192.168.2.1.

**Power-up & Indicators** - The Pluto powers from USB. After
enumeration, status LEDs should indicate activity. - If using a powered
hub, ensure stable 5 V supply.

**Jumpers/Switches** - Use factory defaults unless you have a specific
configuration. - Ensure the **RF shield** and connectors are secure; no
special jumpers are required.

## Software Setup

**Get the code** - Clone or copy the demo scripts into a working folder
(e.g., `pluto_uav_demo/`). - Example files referenced below: -
`uav_monitor.py` (real-time scan/classifier) - `requirements.txt`
(Python dependencies)

**Install prerequisites** - Python **3.9–3.12** recommended - Install
Pluto/LibIIO support on your OS (driver/udev rules where applicable)

**Create environment and install**

``` bash
# (optional) create a venv
python -m venv .venv

# activate:  Windows PowerShell:
.\.venv\Scripts\Activate.ps1

#  Linux/macOS:
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt
# or minimal:
pip install pyadi-iio numpy matplotlib
```

**requirements.txt (example)**

``` text
pyadi-iio
numpy
matplotlib
# optional for GUI dashboards later:
# pyqtgraph
# flask
# flask-socketio
```

## Running the Demo

**Quick start (2.4 GHz passive scan & classify)**

``` bash
# USB connection (defaults to 192.168.2.1 via USB/Ethernet gadget)
python uav_monitor.py --band 2.4 --device ip:192.168.2.1
```

**Common options** - `--band {2.4,5.8}` : choose target band -
`--device URI` : e.g., `ip:192.168.2.1` or `usb:1.0.5` - `--sr SR` :
sample rate in S/s for scan mode (default ~3e6) - `--rf-bw BW` : analog
filter bandwidth (default ~3e6) - `--step STEP` : scan step in Hz
(default ~2e6) - `--fft N` : FFT size (default 2048) - `--avg ALPHA` :
EWMA average (0–1, default 0.6)

**Example commands**

``` bash
# 5.8 GHz band with slightly larger step and FFT
python uav_monitor.py --band 5.8 --step 3000000 --fft 4096

# Force USB backend URI
python uav_monitor.py --band 2.4 --device usb:1.0.5

# Use wider analog BW and faster scan integration
python uav_monitor.py --band 2.4 --rf-bw 4000000 --int 0.05
```

**What the script does** - Tunes Pluto across the selected band in small
windows (scan mode) - Computes PSD (FFT) and updates: - A rolling
**spectrogram** (time vs frequency offset) - A **live PSD trace** for
the current window - Runs a simple classifier: - **OFDM-ish** (flat,
wider OBW → likely Wi-Fi/video) - **Narrowband** (sharp, small OBW →
likely RC/telemetry) - **Intermediate/Unknown** - Prints a **timestamped
log** of strong detections

## Expected Results

**On success you should see:** - A live **spectrogram** (upper plot)
where active channels appear as bright bands - A **PSD line** (lower
plot) with a visible peak when a signal is in the current window - A
**status line** with: - Center frequency (CF) - Peak offset - Estimated
occupied bandwidth (OBW) - Spectral flatness - Classification label

**Sample terminal log**

``` text
[14:22:31.124Z] CF=2438.000 MHz  Peak=2439.002 MHz  OBW=1.42 MHz  Flat=0.67  Class=OFDM-ish (Wi-Fi/video?)
[14:22:32.211Z] CF=2462.000 MHz  Peak=2461.998 MHz  OBW=0.09 MHz  Flat=0.21  Class=Narrowband (RC/telemetry?)
```

**If you switch to a directional antenna and point at a controller or
FPV link:** - OFDM-like channels (video/Wi-Fi) will appear as broader,
flatter plateaus - RC/telemetry will appear as narrower, sharp peaks

## Troubleshooting (Optional)

**Pluto not found / permission errors** - Windows: install ADI/LibIIO
drivers; replug USB; try different port/cable - Linux: add udev rules
for libiio; run without `sudo` once rules are applied - Verify URI:
`ip:192.168.2.1` usually works over USB-Ethernet gadget

**Flat/noisy spectrum, no signals** - Check antenna type and frequency
band - Move closer to the source (or use a directional antenna) -
Increase integration time (`--int`) or averaging (`--avg`) - Verify
local RF environment actually has activity at that time

**Clipping / overload near strong sources** - Add attenuation (10–40
dB) - Use “slow_attack” AGC (default) or try manual RX gain

**Choppy UI / high CPU** - Reduce FFT size (e.g., 1024) - Increase scan
step to fewer windows - Close other heavy applications

**Plots don’t show (headless)** - Ensure a local display backend
(matplotlib) - On WSL/SSH, use X11 forwarding or run on native OS

## Resources

- ADALM-PLUTO (Pluto SDR) product page and user guides
- LibIIO / pyadi-iio documentation
- Example SDR spectrum/waterfall tutorials (GNU Radio, matplotlib)
- Antenna references for 2.4/5.8 GHz monitoring
- (Optional extensions)
  - Zoom-mode wideband capture (e.g., ~20 MS/s) for full Wi-Fi channel
    view
  - Frequency-hopping (FH-like) detector using short-dwell clustering
  - Flask/Socket.IO dashboard with detection feed and CSV logging
  - Two-channel AoA with external front-end (e.g., phased
    array/beamformer)
