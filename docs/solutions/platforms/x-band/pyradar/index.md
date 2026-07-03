# pyRadar - X-Band Radar Development Framework

Comprehensive guide for setting up and using pyRadar, a Python-based radar development framework for the X-Band Development Kit.

## Overview

**pyRadar** is a modular Python framework designed to simplify radar application development on the X-Band Development Kit. It provides high-level APIs for hardware control, signal processing, and real-time visualization, enabling rapid prototyping of FMCW radar algorithms.

### Key Capabilities

**Hardware Control**
- **AD9081 MxFE Configuration** - Full TX/RX control with NCO, buffer, and channel configuration
- **ADAR1000 Phased Array** - Custom driver for 32-element beamforming control
- **XUD1A Converter** - X/C-band up/down converter configuration with LO control
- **Synchronization** - Precise TDD timing for FMCW radar operation

**Signal Processing**
- **FMCW Processing** - Beat frequency extraction and range calculation
- **Clutter Subtraction** - Baseline mesh capture for static clutter removal
- **Analog Beamforming** - Phase-calibration-based beam steering

**Radar Pilots**
- **FMCW Range** - Single-beam range profile with live PyQtGraph display
- **FMCW Scan** - Electronically steered azimuth sweep with range-angle heatmap

```{important}
pyRadar requires proper hardware setup and calibration before running radar pilots. Follow the complete setup procedure to ensure system functionality.
```

## Installation and Setup

Follow these steps to configure your PC and hardware for pyRadar operation.

### Prerequisites

**Hardware Requirements**:
- X-Band Development Kit with ZCU102, AD9081, XUD1A, and ADAR1000 boards
- 16 GB SD card for Kuiper Linux
- USB to UART cable (included with ZCU102)
- Ethernet connection (direct or USB-to-Ethernet adapter)
- 12V DC power supplies

**Software Requirements**:
- Windows PC (Windows 10 or later recommended)
- Python 3.10.0
- PuTTY or similar terminal emulator
- Balena Etcher or similar SD card imaging tool
- Internet connection for package downloads

### Step 1: Prepare SD Card with Kuiper Linux

Prepare your SD card with the Kuiper Linux operating system:

**See**: {ref}`SD Card Configuration Guide <x-band-sdcard>` for complete instructions on:
- Downloading ADI Kuiper Linux
- Formatting the SD card
- Flashing the image using Balena Etcher
- Verifying the installation

```{note}
Kuiper Linux includes pre-installed ADI tools and drivers required for the X-Band platform.
```

### Step 2: Install CP210x USB-UART Driver

Install the USB to UART bridge driver for serial communication:

1. Visit [Silicon Labs CP210x Driver Page](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
2. Download the driver for your operating system:
   - Windows: CP210x Universal Windows Driver
   - Select appropriate version (x64 recommended)
3. Run the installer with **administrator privileges**
4. Follow the installation wizard
5. Restart your computer if prompted

**Verify Installation**:
- Open Device Manager (Win + X → Device Manager)
- Connect ZCU102 USB cable
- Check "Ports (COM & LPT)" for "Silicon Labs CP210x USB to UART Bridge"
- Note the COM port number (e.g., COM3)

### Step 3: Install PuTTY

Install PuTTY for serial terminal access:

1. Visit [PuTTY Download Page](https://www.putty.org/)
2. Download the appropriate installer:
   - Windows: 64-bit MSI installer recommended
3. Run the installer and follow the installation wizard
4. Launch PuTTY to verify successful installation

**PuTTY Configuration for ZCU102**:
- Connection type: **Serial**
- Serial line: **COM[X]** (use COM port from Device Manager)
- Speed: **115200**
- Data bits: 8
- Stop bits: 1
- Parity: None
- Flow control: None

### Step 4: Install Python 3.10.0

Set up the Python development environment:

1. Visit [Python 3.10.0 Download Page](https://www.python.org/downloads/release/python-3100/)
2. Download the **Windows installer (64-bit)**
3. Run the installer:
   - ✅ **Check "Add Python 3.10 to PATH"**
   - Click "Install Now"
4. Verify installation:
   ```powershell
   python --version
   ```
   Expected output: `Python 3.10.0`

```{important}
Python 3.10.0 is required for compatibility with Genalyzer and other dependencies. Do not use Python 3.11+ as some packages may not be compatible.
```

### Step 5: Install Python IDE

Install your preferred Python development environment:

**Option A: Visual Studio Code (Recommended)**
1. Download from [VS Code Website](https://code.visualstudio.com/)
2. Install the Python extension
3. Configure Python interpreter to 3.10.0

**Option B: PyCharm Community**
1. Download from [JetBrains Website](https://www.jetbrains.com/pycharm/)
2. Install and configure Python 3.10.0 interpreter

**Option C: Spyder**
1. Install via pip:
   ```bash
   pip install spyder
   ```
2. Launch with `spyder` command

### Step 6: Clone pyRadar Repository

Obtain the pyRadar source code:

**Option A: Git Clone ( NOT available at this time)**
```bash
git clone <repository_url>
cd pyRadar
```

**Option B: Download ZIP**
1. Download the pyRadar repository as ZIP or your FAE will share this with you
2. Extract to your desired location
3. Navigate to the extracted folder

### Step 7: Create a Python Virtual Environment to run the code from

To ensure we are running from a verified software build/package installation, we will create a virtual environment using the following steps

1. Open a terminal in the pyRadar directory using your chosen IDE, e.g.
   ```bash
   cd "C:\Users\svc_adefsysplat\Desktop\System_Platform_Team\x-band\pyRadar"
   ```

2. Create the virtual environment:
   ```bash
   python -m venv xbdp_python_venv
   ```

3. Activate the virtual environment:
   ```bash
   .\\xbdp_python_venv\\Scripts\\activate
   ```

4. Upgrade the Python pip version to ensure you are running the latest:
   ```bash
   python -m pip install --upgrade pip
   ```

5. Install all required Python packages
      NOTE: You will need an active internet connection to complete this step

   ```bash
   pip install -r requirements.txt
   ```

This completes the pre-configuration for the software environment

### Step 8: Configure Hardware Connection

Connect to the X-Band Development Kit:

**Physical Setup**:
1. Insert flashed SD card into ZCU102 (slot J1001)
2. Connect USB cable from ZCU102 to PC (for UART)
3. Connect Ethernet cable:
   - **Direct connection**: ZCU102 to PC Ethernet port
   - **Network connection**: ZCU102 to network switch/router
   - **USB-Ethernet adapter**: Configure adapter IP if needed
4. Connect 12V power supplies to all boards
5. Power on the system

**Serial Connection**:
1. Open PuTTY with COM port settings (115200, 8N1)
2. Power on ZCU102
3. Watch boot sequence in PuTTY
4. Login if prompted:
   - Username: `root`
   - Password: `analog`

```{note}
Once logged in, run `iio_attr -c` on the ZCU102 to list all detected IIO devices. You should see **40 devices** in total. A count lower than 40 indicates a hardware detection issue that should be resolved before proceeding.
```

**Network Configuration**:

1. Check ZCU102 eth0 interface IP address:
   ```bash
   ifconfig eth0
   ```

   ```{image} xbdp_ethernet_settings_verification.png
   :alt: Ethernet Settings Verification
   ```

2. Note the IP address (e.g., `192.168.0.101`)

3. Verify connectivity from PC:
   ```bash
   ping 192.168.0.101
   ```

   ```{image} xbdp_ping_eth0_response.png
   :alt: Ping eth0 Response
   ```

```{tip}
For USB-Ethernet adapters, you may need to configure the adapter's IP address to be on the same subnet as the ZCU102 (e.g., PC: 192.168.0.10, ZCU102: 192.168.0.101).
```

### Step 9: Configure pyRadar

Update pyRadar configuration for your system:

1. In `\x-band\pyRadar` directory, open `main.py`in your Python IDE
2. Locate the IP address configuration section:

   ```python
   uri = "ip:192.168.0.101"
   ```

3. Update the IP address to match your ZCU102 from the earlier section (192.168.0.101)

4. Save the file

**Verify ADI Device Detection**:

On the ZCU102, check that devices are detected:
```bash
root@analog:~# iio_info -n <zcu102_ip>
```
You should see AD9081, ADAR1000, and other IIO devices listed.

### Step 10: Run Your First Pilot - FMCW Examples

Test the installation with a simple pilot:

1. In `\x-band\pyRadar` directory, open `main.py` in your IDE.
2. Set the point source frequency at the top of `main.py`:
   ```python
   source_freq_ghz = 10.0694  # Point Source Frequency for calibration in GHz
   ```
3. Run the script:
   ```bash
   python .\main.py
   ```

4. **Calibration Menu** — the first menu prompts you to select a calibration mode:

   ```
   === XBDP Calibration Menu ===
   1. Rx Calibration
   2. Full (Rx & Tx) Calibration
   3. Load saved calibration
   4. Load default calibration
   q. Quit
   ```

   - **Option 1 — RX Calibration**: Place a point source approximately 1.5 m from the front of the Stingray antenna. The ADC data is captured and plotted for review. Press Close to continue, then remove the RF source when prompted.
   - **Option 2 — Full Calibration**: Runs RX calibration first, then prompts you to connect an antenna to J9 on Stingray for TX calibration.
   - **Option 3 — Load saved calibration**: Loads the most recent calibration JSON from the `cal files/` directory.
   - **Option 4 — Load default calibration**: Skips calibration and applies factory defaults (gain=127, phase=0 for all elements).

   ```{important}
   Calibration results are saved automatically to `cal files/` as a timestamped JSON file. Stale calibration files older than 30 days are purged on startup.
   ```

5. After calibration, the hardware connects automatically and the **Pilot Demo Menu** appears:

   ```
   === XBDP Pilot Demo Menu ===
   1. Run the FMCW Range Pilot
   2. Run the FMCW Scan Pilot
   q. Quit
   ```

6. **FMCW Range Pilot (Option 1)**:
   - A live PyQtGraph window opens showing the range profile.
   - Move a reflector in front of the antenna — watch the detected range update in real time.
   - Range resolution is approximately 0.6 m.
   - To exit, close the window; the script completes cleanly.

7. **FMCW Scan Pilot (Option 2)**:
   - You will be asked: `Enable clutter mesh? (Y/n)` — Enter `Y` to capture a static baseline before scanning (recommended for target isolation).
   - A live heatmap opens with angle on the X-axis (degrees) and range on the Y-axis (metres).
   - Move a reflector in front of the antenna — a bright hot spot appears at the target's range and angle.
   - To exit, press the `Q` key; the window closes and the script completes.


## Sample Data and Results

### RX Calibration Example

```{image} rx_cal_plot.png
:alt: RX Calibration Results
```

*Four-channel calibration showing phase and gain matching across all ADC channels. The plot demonstrates successful alignment of all array elements to a common reference.*

**Calibration Metrics**:
- Phase error: < 5° RMS across all channels
- Amplitude error: < 0.5 dB across all channels
- Reference element: Channel 0

### FMCW Range Example

```{image} xbdp-0.6m-distance-fmcw-range.png
:alt: FMCW Scan Visualization
```

*FMCW range showing the captured ADCs on the top graph of the transmitted FMCW signal and the returned beat frequency on the lower graph and resulting Range on the top right of this lower graph.*

**Range Parameters**:
- Range resolution: ~0.6m

### FMCW Scan Example

```{image} xbdp-1.2m-distance-fmcw-scan.png
:alt: FMCW Scan Visualization
```

*FMCW horizon scan showing range-angle heatmap data. The visualization demonstrates the system's ability to detect and locate targets across azimuth angles with range resolution.*

**Scan Parameters**:
- Azimuth range: -60° to +60°
- Range resolution: ~0.6m
- Color scale: Normalized dB

```{tip}
Use sample data to verify your installation and compare results. Similar patterns indicate proper system configuration.
```

## System Architecture

The pyRadar framework is organized as follows:

```
pyRadar/
├── main.py                         # Entry point: menus, config, hardware init
├── requirements.txt                # Python package dependencies
├── cal files/                      # Saved calibration JSON files (auto-created)
├── custom_libs/                    # Custom hardware drivers
│   ├── __init__.py
│   └── adar1000.py                 # Modified ADAR1000 driver for X-Band
├── pilot_functions/                # Radar demonstration pilots
│   ├── __init__.py
│   ├── fmcw_range.py               # FMCW single-beam range pilot
│   └── fmcw_scan.py                # FMCW azimuth scan pilot
├── radar_utils/                    # Core library modules
│   ├── __init__.py
│   ├── hardware_setup.py           # AD9081, XUD1A, and ADAR1000 initialisation
│   ├── calibration.py              # Per-element RX/TX calibration routines
│   ├── cal_manager.py              # Calibration file save/load/purge
│   ├── tx_rx_cal.py                # Full RX and TX calibration sequences
│   ├── signal_processing.py        # DSP functions (FFT, heatmap, beat calc)
│   ├── sync_config.py              # TDD timing and FMCW waveform generation
│   ├── radar_plotting.py           # PyQtGraph real-time visualisation
│   ├── rx_1tone.json               # Single-tone RX calibration config
│   ├── rx_2tone.json               # Dual-tone RX calibration config
│   └── utils.py                    # Miscellaneous helpers
└── tools/                          # Offline post-processing utilities
    ├── check_h5.py                  # Inspect HDF5 capture files
    └── post_process_h5.py           # Post-process captured HDF5 data
```

### Module Descriptions

#### `main.py`
Entry point for the entire pyRadar application.

**Configuration** (edit these at the top of the file):
- `uri` — ZCU102 IP address (default `ip:192.168.0.101`)
- `BW` — chirp bandwidth in Hz (default 250 MHz)
- `num_chirps` — chirps per ADC buffer (default 512)
- `source_freq_ghz` — point-source frequency for calibration (GHz)
- `subarray_modes` — per-subarray role: `{1:"rx", 2:"rx", 3:"tx", 4:"rx"}`

**Shared state dictionaries**:
- `cal` — calibration results: `cal_ant_fix`, `loFreq`, `rx_phase_cal`, `tx_phase_cal`, per-element gain/attenuation dicts
- `hw` — hardware handles: `conv` (AD9081), `sray` (ADAR1000), `tddn` (TDD engine), `PRF`, `subarray`

**Menus** (executed in order on startup):
1. `calibration_menu()` — prompts for calibration mode, then stores results in `cal`
2. `connect_and_configure_xbdp()` — connects to hardware and applies loaded calibration
3. `pilot_menu_loop()` — prompts for pilot selection in a loop

#### `pilot_functions/fmcw_range.py`
**FMCW Range Pilot** — single-beam live range profile.

```python
FMCWRange(conv, tddn, cal_ant_fix, subarray_modes, iq, BW, PRF, duty_cycle)
```
- Continuously captures IQ data and dechirps against the transmitted chirp reference.
- Applies a low-pass filter to reject the sum-frequency product, then FFTs the beat signal.
- Converts the beat frequency to range: `R = c · T · f_beat / (2 · BW)`
- Displays a live PyQtGraph range profile; close the window to exit.

**Printed on launch**:
- TX/RX subarray assignments, enabled ADC channels
- Chirp duration, slope, range resolution, maximum unambiguous range

#### `pilot_functions/fmcw_scan.py`
**FMCW Scan Pilot** — electronically steered azimuth sweep with heatmap display.

```python
FMCWScan(conv, sray, cal_ant_fix, subarray_modes, iq, BW, PRF,
         scan_min, scan_max, scan_step, analog_phase_cal, tx_phase_cal,
         cluttermesh=True)
```
- Sweeps beam from `scan_min` to `scan_max` degrees in `scan_step` increments.
- At each angle, programs new phase values into the ADAR1000 array, captures one ADC frame, dechirps, and FFTs to produce a range column.
- Assembles all columns into a 2-D range×angle heatmap.
- Optional `cluttermesh`: captures a multi-frame static baseline before the live scan and subtracts it to remove fixed clutter.
- Press `Q` to exit. Default scan limits: −25° to +25° in 5° steps.

#### `radar_utils/hardware_setup.py`
Hardware initialisation for AD9081, XUD1A, and ADAR1000.

**Key functions**:

```python
setup_ad9081(url, rx_buffer_size, tx_cyclic_buffer, rx_cyclic_buffer,
             tx_ddr_offload, rx_channel_nco_frequencies,
             tx_channel_nco_frequencies, rx_main_nco_frequencies,
             tx_main_nco_frequencies, rx_enabled_channels)
```
Configures the AD9081 MxFE:
- RX main NCO defaults to 500 MHz; TX main NCO defaults to 4.5 GHz.
- Channel NCOs default to 0 Hz (DC).
- `rx_enabled_channels` controls which ADC channels are active (derived from `subarray_modes`).
- Returns a configured `adi.ad9081` object.

```python
setup_xud1a(conv, channel_modes, lo_freq)
```
Configures the XUD1A up/down converter:
- Sets each subarray channel to RX or TX mode.
- Programs the LO frequency (populated from calibration).

```python
setup_stingray(uri, subarray_modes)
```
Initialises the 8-chip, 32-element ADAR1000 array:
- Maps chip IDs, device layout, and element numbering.
- Returns `(sray, subarray)` — the array object and a per-subarray element mapping.

```python
build_rx_channel_config(subarray_modes)
```
Derives which ADC channels to enable and the subarray-to-data-index mapping used by all signal-processing functions.

#### `radar_utils/calibration.py`
Per-element RX and TX calibration building blocks.

**Channel control**:

| Function | Purpose |
|----------|---------|
| `enable_stingray_channel(obj, elements)` | Enables listed element channels (1–32) for RX or TX |
| `disable_stingray_channel(obj, elements)` | Disables listed element channels |

**Data capture**:

| Function | Purpose |
|----------|---------|
| `data_capture(adc)` | Raw ADC capture — returns 4-channel IQ array |
| `data_capture_cal(adc, cal_values)` | Capture with antenna path-length correction applied |
| `data_capture_test(adc, cal_values)` | Capture for mid-calibration test steps |

**Calibration routines**:

| Function | Purpose |
|----------|---------|
| `rx_gain(obj, adc, subarray, adc_map, element_map)` | Measures per-element RX gain and fits correction codes |
| `phase_analog(sray_obj, adc_obj, ...)` | Null-steering phase calibration (analog domain) |
| `phase_digital(obj, adc, adc_ref, subarray_ref)` | NCO-based digital phase trim |
| `find_phase_delay_fixed_ref(...)` | Finds phase delay using a fixed reference element |

#### `radar_utils/cal_manager.py`
Manages saving, loading, and housekeeping of calibration files.

**Key functions**:

| Function | Purpose |
|----------|---------|
| `save_calibration(cal_ant_fix, loFreq, rx_phase_cal, tx_phase_cal, sray, ...)` | Saves all calibration data to a timestamped JSON in `cal files/` |
| `load_latest_calibration()` | Loads the most recent JSON from `cal files/` |
| `apply_calibration(cal_data, sray)` | Unpacks a loaded cal dict into the `cal` state dict |
| `purge_stale_calibrations(max_age_days=30)` | Deletes cal files older than `max_age_days` |

Calibration JSON files contain: `loFreq`, `cal_ant_fix`, per-element `rx_phase_cal`, `tx_phase_cal`, `rx_gain_dict`, `rx_atten_dict`, `tx_gain_dict`, `tx_atten_dict`, and per-element hardware register snapshots.

#### `radar_utils/tx_rx_cal.py`
Full-system RX and TX calibration sequences.

**Key functions**:

```python
setup(N_rx)
```
Defines the physical subarray-to-element mapping, ADC channel map, and reference elements. Returns all parameters needed to run calibration.

```python
device_init(N_rx, url, default=True)
```
Connects to the ZCU102, constructs the `adar1000_array` object with the correct chip IDs and element map, and sets default NCO frequencies.

```python
rx_cal_full(url, sray, conv, subarray, subarray_ref, subarray_targ,
            adc_map, adc_ref, source_freq_ghz, subarray_modes)
```
Full RX calibration sequence:
1. Gain equalisation — measures per-element power and programmes correction codes.
2. Analog phase calibration — null-steering sweep per element.
3. Digital phase trim — NCO residual removal.
Returns `(cal_ant_fix, loFreq, rx_phase_cal, rx_gain_dict, rx_atten_dict)`.

```python
tx_cal_full(url, sray, conv, subarray, source_freq_ghz, subarray_modes)
```
Full TX calibration sequence using the maximum-power method — sweeps each TX element phase while measuring combined output power. Returns `(tx_phase_cal, tx_gain_dict, tx_atten_dict)`.

#### `radar_utils/signal_processing.py`
DSP building blocks used by both pilots.

| Function | Purpose |
|----------|---------|
| `beat_calc(data, fs, T, BW)` | Extracts beat frequency and estimates range from an FMCW capture |
| `heatmap_gen(sum_data, iq, cross_talk_freq, r_centers, ...)` | Builds one azimuth column of the range-angle heatmap |
| `circular_shift_fft(yf, xf, cross_talk_freq)` | Circularly shifts FFT to zero out the internal cross-talk leakage peak |
| `normalize_heatmap_data(data, floor_db, clip_db)` | Normalises a heatmap to a dB scale with configurable floor and ceiling |
| `init_fft(N)` | Pre-computes Hanning window, coherent gain, and frequency axis for length-N FFT |
| `freq_process(data, min_scale, max_scale, ...)` | 2-D range×Doppler FFT with optional MTI filter |
| `freq_process_complex_batch(data_list, ...)` | Batch version of `freq_process` for multi-subarray processing |
| `apply_range_normalization(rd_db, r_res, exponent, start_bin)` | Compensates R⁴ path loss on a range-Doppler map |
| `apply_cfar_2d(rd_map_db, guard_cells, training_cells, bias_db)` | 2-D CA-CFAR detector |
| `RDRConfig(conv, PRI_ms, BW, num_chirps, signal_freq, output_freq)` | Computes key range-Doppler axis parameters |

#### `radar_utils/sync_config.py`
TDD timing engine and FMCW waveform generation.

```python
sys_sync(conv, tddn, PRF, num_chirps, BW, duty_cycle, mode, subarray_modes)
```
Configures the TDD controller and uploads the TX chirp waveform:
- **FMCW mode**: sets `rx_buffer_size = samples_per_chirp × num_chirps`, programs all TDD channels, generates and tiles the linear-chirp waveform, uploads to the AD9081 DAC cyclic buffer.
- Returns the ideal IQ chirp array `iq` used later for dechirping.

```python
sync_disable(conv, tddn, sray, subarray)
```
Shuts down TDD, disables the DAC cyclic buffer, and disables all Stingray channels cleanly on exit.

#### `radar_utils/radar_plotting.py`
PyQtGraph-based real-time visualisation (replaces matplotlib for live updates).

| Function | Purpose |
|----------|---------|
| `init_fmcw_range_gui()` | Creates PyQtGraph window for the FMCW Range pilot (raw ADC + beat spectrum + range readout) |
| `update_fmcw_range_gui(gui, sub1, sub2, sub4, sum_data, ...)` | Updates all plots in the range GUI each capture loop |
| `init_fmcw_radar_viewer(...)` | Creates the range-angle heatmap window for the FMCW Scan pilot |
| `update_fmcw_radar_viewer(...)` | Updates the heatmap and angle/range cursors each scan sweep |
| `init_rd_gui(...)` | Initialises a range-Doppler map display window |
| `ensure_qt_app()` | Creates a `QApplication` instance if one does not already exist |

### Custom Libraries

**`custom_libs/adar1000.py`** — Modified ADAR1000 Phased Array Beamformer Driver

This custom driver preserves calibrated gain and phase weights when steering the beam. The standard pyadi-iio driver overwrites these values on every beam update; this version maintains the per-element calibration offsets.

```{tip}
The custom ADAR1000 driver is required for proper phased-array beamforming on the X-Band platform. Do not replace it with the standard pyadi-iio version.
```

## Additional Resources

### Documentation
- {external+pyadi-iio:doc}`pyadi-iio Documentation <index>` - Python IIO library reference
- {adi}`AD9081 Product Page <en/products/ad9081.html>` - MxFE datasheet and resources
- {adi}`ADAR1000 Product Page <en/products/adar1000.html>` - Beamformer documentation
- {ref}`Kuiper Linux Documentation <kuiper>` - Linux image documentation

### Tools and Software
- {ref}`IIO Oscilloscope <iio-oscilloscope>` - Real-time IIO device visualization
- {adi}`Genalyzer <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/genalyzer.html>` - Signal analysis library

### Contact and Support
- **pyRadar Author**: Brandon Lopez - brandon.lopez@analog.com
- **ADI Support**: [EngineerZone Community](https://ez.analog.com)
- **GitHub Issues**: Report bugs and request features in repository

## Pilot Deep-Dives

Detailed technical breakdowns of individual radar pilots, covering their signal-processing mechanics and tunable parameters:

```{toctree}
:maxdepth: 2

FMCWScan Pilot <fmcwscan/index>
```

```{seealso}
- {ref}`Hardware Assembly Guide <x-band-assembly>` - X-Band platform assembly instructions
- {ref}`EEPROM Programming <x-band-eeprom>` - FMC EEPROM setup for VADJ
- {ref}`SD Card Configuration <x-band-sdcard>` - Kuiper Linux SD card preparation
- {ref}`ZCU102 Configuration <x-band-zcu102config>` - ZCU102 boot and network setup
```
