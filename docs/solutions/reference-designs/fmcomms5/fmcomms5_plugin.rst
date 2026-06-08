.. imported from: https://wiki.analog.com/resources/tools-software/linux-software/fmcomms5_plugin

.. _fmcomms5-plugin:

FMComms5 Plugin Description
===========================

.. |more| replace:: *(see AD9361 linux driver documentation)*

The FMCOMMS5 plugin works with the :ref:`iio-oscilloscope`. You always use
the latest version if possible. Changing any field will immediately write
changes which have been made to the FMComms5 settings to the hardware, and
then read it back to make sure the setting is valid. If you want to set
something that the GUI changes to a different number, that either means that
GUI is rounding (sorry), or the hardware (either the AD9361 or the FPGA
fabric) does not support that mode/precision.

.. note::

   For the main OSC plot window: The allowed channel sections are based on
   following rules:

   - Channels need to enabled pairwise I & Q. (example voltage0 & voltage1
     or voltage2 & voltage3, etc. )
   - The number of enabled pairwise channels need to be equal between the
     two devices.
   - Devices are split as following: voltage0..3 Device A,
     voltage4..7 Device B

If you want to go play with ``/sys/bus/iio/devices/....`` and manipulate the
devices behind the back of the GUI, it's still possible to see the settings by
clicking the "refresh" button at the bottom of the GUI.

If you think the device has a setting that isn't managed by this tab, check
out the :dokuwiki:`fmcomms5 Advanced Plugin </resources/tools-software/linux-software/fmcomms2_advanced_plugin>` for the IIO Oscilloscope.

The FMComms5 view is divided in four sections:

- **Device Global Settings**
- **Receive Chain**
- **Transmit Chain**
- **FPGA Settings**

.. image:: images/fmcomms5_plugin.png
   :align: right
   :width: 380

Device Global Settings
----------------------

- **Active ENSM:** Displays the active mode of the Enable State Machine.
  |more|
- **ENSM Modes:** Selects one of the available modes: FDD and TDD.
  |more|
- **Calibration Mode:** Displays the active calibration mode.
  |more|
- **Calibration Modes:** Selects one of the available modes: auto, manual,
  rf_dc_offs and tx_quad. |more|
- **TRX Rate Governor:** Displays the active option of the Rate Governors.
  |more|
- **TRX Rate Governor Available:** Selects one of the available options:
  nominal and highest_osr. |more|
- **Filter FIR configuration**

  - **FIR parameters file chooser** Allows a FIR filter configuration to
    be loaded from a file. |more|
  - **Enable RX FIR Filter Only:** Enables/Disables the FIR filter on RX
    path. |more|
  - **Enable TX FIR Filter Only:** Enables/Disables the FIR filter on TX
    path. |more|
  - **Enable RX & TX FIR filters:** Enables the FIR filter on both RX and
    TX paths.
  - **Disable All:** Disables the FIR filter on both RX and TX paths.

- **RX Path Rates:** Lists the rates of: BBPLL, ADC, R2, R1, RF, RXSAMP.
  |more|
- **TX Path Rates:** Lists the rates of: TXSAMP, TF, T1, T2, DAC, BBPLL.
  |more|
- **DCXO Coarse Tune:** Selects the attribute for a coarse tune. |more|
- **DCXO Fine Tune:** Selects the attribute for a fine tune. |more|

Note that all settings above apply to both ad9361 devices.

Receive Chain
-------------

- **RF Bandwidth(MHz):** Configures RX analog filters: RX TIA LPF and
  RX BB LPF. |more|
- **Sampling Rate(MSPS):** Selects the sample rate of the ADC. |more|
- **RF Port Select:** Selects the RF Port of the receive channels. |more|
- **RX LO Frequency(MHz):** Selects the RX local oscillator frequency. Range
  70MHz to 6GHz with 1Hz tuning granularity. |more|
- **Fastlock Mode** |more|

  - **Fastlock Profile:** Selects a profile to be stored or recalled.
  - **Store:** Stores the selected profile.
  - **Recall:** Recalls the selected profile.

- **Tracking** |more|

  - **Quadrature**
  - **RF DC**
  - **BB DC**

- **RX**

  - **Hardware Gain(dB):** Controls the RX gain only in Manual Gain
    Control Mode (MGC). |more|
  - **RSSI(dB):** Displays the received strength signal level. |more|
  - **Gain Control:** Displays the active gain mode. |more|
  - **Gain Control Modes:** Selects one of the available modes: manual,
    slow_attack, hybrid and fast_attack. |more|

Note that only **RF Bandwidth**, **Sampling Rate**, **RF Port Select** and
**Tracking** settings apply to both ad9361 devices.

Transmit Chain
--------------

- **RF Bandwidth(MHz):** Configures TX analog filters: TX BB LPF and TX
  Secondary LPF. |more|
- **Sampling Rate(MSPS):** Selects the sample rate of the DAC. |more|
- **RF Port Select:** Selects the RF Port of the transmit channels. |more|
- **TX LO Frequency(MHz):** Selects the TX local oscillator frequency. Range
  70MHz to 6GHz with 1Hz tuning granularity. |more|
- **Fastlock Mode** |more|

  - **Fastlock Profile:** Selects a profile to be stored or recalled.
  - **Store:** Stores the selected profile.
  - **Recall:** Recalls the selected profile.

- **TX**

  - **Attenuation(dB):** Individually controlls attenuation for TX1 and
    TX2. The range is from 0 to -89.75 dB in 0.25dB steps. |more|

Note that only **RF Bandwidth**, **Sampling Rate** and **RF Port Select**
settings apply to both ad9361 devices.

FPGA Settings
-------------

- **Transmit/DDS**

  - **DDS Mode:** Selects on the the available modes:

    - One CW Tone
    - Two CW Tones
    - Independent I/Q Control
    - DAC Buffer Output (Output a data file)
    - Disabled.

  - **Tone**

    - **Frequency(MHz):** Selects the frequency of the tone.
    - **Scale:** Selects the scale of the tone.
    - **Phase(degrees):** Selects the phase of the tone.

- **Receive**

  - **Phase Rotation :** Selects the rotation phase of a RX

