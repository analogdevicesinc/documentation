.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0393

.. _eval-cn0393-ardz:

EVAL-CN0393-FMCZ
=================

Isolated 2-Channel Simultaneous Sampling DAQ.

Overview
--------

:adi:`CN0393` is a two-channel bank-isolated data acquisition (DAQ) system,
with a multi-ADC simultaneous sampling architecture. The system achieves high
channel density and isolation between the bank and the digital backplane while
maintaining exceptional performance.

.. figure:: cn0393_figure_1.png
   :align: center

   CN0393 simplified block diagram

The design makes efficient use of isolation channels by configuring the
analog-to-digital converters (:adi:`ADAQ7988`) in daisy-chain mode and
utilizing an isolator product with trimmed delay clock feature
(:adi:`ADuM3150`). Power generation is also simplified using an isolator with an
integrated PWM controller and transformer driver to perform DC-to-DC conversion
across the isolation barrier (:adi:`ADuM3470`).

Each DAQ channel features programmable gain instrumentation amplifiers
(:adi:`AD8251`) for channel-independent gain setting and high-input impedance
for easy interfacing with a variety of sensors and input sources.

The multi-ADC simultaneous sampling architecture achieves many channels without
sample rate limitations inherent in multiplexed DAQ signal chains. The
analog front-end (AFE) design is also simpler than the multiplexed option,
because the system's dynamic requirements are less strict. Each channel's
corresponding samples also occur at the same time, while sequential sampling
systems do not.

Digital bank-isolated DAQ designs provide protection for digital backend
circuitry and reduce ground loop and common mode interference between banks.

Required Equipment
------------------

- EVAL-CN0393-FMCZ circuit evaluation board (160-pin FMC connector interface)
- :adi:`EVAL-SDP-CH1Z` (SDP-H1) controller board
- CN0393 Evaluation Software
- +12 V DC switched-mode power supply
- USB Type A to Mini-B cable
- Low distortion, low noise signal source(s)
- PC with USB port running Windows XP, Vista (32-bit), or Windows 7/8/10
  (32-bit) with .NET 4.0 framework

Getting Started
---------------

The EVAL-CN0393-FMCZ has a 160-pin FMC connector to interface with a digital
host.

.. note::

   Install the evaluation software **before** connecting the hardware to
   ensure drivers are available when the board is first detected.

The EVAL-CN0393-FMCZ evaluation hardware features an isolation trench that
separates two ground planes. Ensure proper ground connections and avoid bridging
isolated planes.

Software Installation
~~~~~~~~~~~~~~~~~~~~~

1. Download and extract the CN0393 software package, then run ``setup.exe`` to
   launch the installation wizard.

   .. figure:: cn0393install1.png
      :align: center
      :width: 500

      Software installer welcome screen

2. Select the destination directory and click Next.

   .. figure:: cn0393install2.png
      :align: center
      :width: 500

      Destination directory selection

3. Review the installation details. Click Next to begin the installation.

   .. figure:: cn0393install3.png
      :align: center
      :width: 500

      Installation review and progress

4. Upon completion, click Next to initiate the installation of the ADI SDP
   Drivers (version 2.2.118.111).

   .. figure:: cn0393install4.png
      :align: center
      :width: 500

      CN0393 software installation complete

5. The SDP Drivers wizard appears. Click Next, then Install to proceed with
   driver installation.

   .. figure:: cn0393install5.png
      :align: center
      :width: 500

      SDP driver installation

6. When driver installation completes, click Close to finish setup.

   .. figure:: cn0393install6.png
      :align: center
      :width: 500

      Driver installation complete

Hardware Setup
~~~~~~~~~~~~~~

1. Connect **P1** on the EVAL-CN0393-FMCZ to **J4** on the EVAL-SDP-CH1Z
   (SDP-H1) board via the 160-pin FMC connector before applying power.
2. Connect the +12 V power supply to the EVAL-SDP-CH1Z via the +12V_VIN jack.
3. Connect the hardware to the PC via USB cable.
4. Verify the connection through Windows Device Manager -- the board should
   appear under **ADI Development Tools** if drivers were installed correctly.

Using the Evaluation Software
------------------------------

The CN0393 Evaluation Software interfaces with the EVAL-SDP-CH1Z and
EVAL-CN0393-FMCZ hardware.

USB Connection
~~~~~~~~~~~~~~

If the hardware is properly connected to the PC, the evaluation software will
automatically establish a connection. Successful connection displays "Hardware
Connection and Initialization Complete" in the status bar.

.. figure:: cn0393_no_hardware_detected.png
   :align: center
   :width: 400

   No hardware detected dialog

If the hardware is not detected, a popup appears offering the option to rescan
or enter standalone mode.

.. figure:: cn0393_standalone_notification.png
   :align: center
   :width: 400

   Standalone mode notification

Configure Tab
~~~~~~~~~~~~~

.. figure:: cn0393configuretab.png
   :align: center

   Configure tab

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Control
     - Description
   * - Single Capture
     - Performs a single set of conversions with the CN0393 hardware.
   * - Continuous Capture
     - Performs repeated sets of conversions with the CN0393 hardware.
   * - Num Samples
     - Sets the number of conversions that will be performed for each channel.
   * - Status
     - Displays operational information and software version details.
   * - Reference Voltage (V)
     - Set to the reference voltage being used on the hardware (default 5 V
       using :adi:`ADR4550`).
   * - Sampling Rate (kSPS)
     - Set to the desired sample rate to be used on the CN0393 hardware.
       Maximum 500 kSPS.
   * - SCK Freq (MHz)
     - Set to the desired SCK frequency to be used on the CN0393 hardware.
       Maximum 40 MHz.
   * - CA Gain
     - Sets the gain of Channel A on the CN0393 hardware.
   * - CB Gain
     - Sets the gain of Channel B on the CN0393 hardware.
   * - CA/CB Input Range
     - Displays the current input range based on gain and reference voltage
       settings.
   * - Flash LED
     - Activates the STATUS LED on the SDP-H1.

**Input Range Configuration:**

The :adi:`AD8251` gain settings are configured via the CA Gain and CB Gain
controls. Hardware updates occur immediately upon new gain selection.

.. list-table::
   :header-rows: 1
   :widths: 20 20

   * - Gain
     - Input Range
   * - 1
     - ±10 V
   * - 2
     - ±5 V
   * - 4
     - ±2.5 V
   * - 8
     - ±1.25 V

Waveform Tab
~~~~~~~~~~~~

Displays time-domain results from the CN0393 hardware.

.. figure:: cn0393_waveformtab.png
   :align: center

   Waveform tab

- **Codes** -- Y-axis shows raw :adi:`ADAQ7988` output codes.
- **Volts** -- Y-axis displays calculated input voltages.
- **Samples** -- X-axis shows sample numbers.
- **Time** -- X-axis displays time in microseconds.

Analysis metrics:

- Peak-to-peak amplitude
- Maximum and minimum amplitudes
- Mean voltage
- Standard deviation
- Fundamental frequency

Histogram Tab
~~~~~~~~~~~~~

Displays histogram results showing the occurrence frequency of output codes.

.. figure:: cn0393histogramtab.png
   :align: center

   Histogram tab

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Metric
     - Description
   * - Max/Min Code
     - Highest and lowest output values with corresponding voltages.
   * - Mean Code
     - Average output value.
   * - Transition Noise
     - Noise measurement of results.
   * - Peak-to-Peak
     - Peak-to-peak amplitude.
   * - RMS
     - Root-mean-square voltage calculation.
   * - LSB
     - Equivalent voltage change resulting in one-bit code change.
   * - Histogram Width
     - Total span of histogram data.

FFT Tab
~~~~~~~

Displays frequency-domain analysis results.

.. figure:: cn0393ffttab.png
   :align: center

   FFT tab

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Metric
     - Description
   * - Max/Min Amplitude
     - Peak voltage values and codes.
   * - Fund. Frequency
     - Fundamental signal frequency.
   * - Fund. Amplitude
     - Fundamental amplitude in dB relative to full-scale.
   * - Dynamic Range
     - Input signal range measurement.
   * - SNR
     - Signal-to-noise ratio.
   * - THD
     - Total harmonic distortion.
   * - SINAD
     - Signal-to-noise-and-distortion ratio.
   * - SFDR
     - Spurious-free dynamic range.
   * - Noise Floor
     - Background noise level in dB.

Summary Tab
~~~~~~~~~~~

Displays all three plots (waveform, histogram, FFT) in a single window
alongside comprehensive analysis summary metrics for both channels.

.. figure:: cn0393_summarytab.png
   :align: center

   Summary tab

Menu Options
~~~~~~~~~~~~

**File Menu:**

- **Reconnect to SDP** -- Reestablishes USB connection.
- **Load Data** (Ctrl+L) -- Imports previously saved ``.tsv`` result files.
- **Save Data** (Ctrl+S) -- Exports current software state and conversion
  results in ``.tsv`` format for external analysis tool integration.
- **Save Image** (Ctrl+I) -- Captures a JPEG image of the current view.
- **Exit** (Ctrl+Q) -- Closes the application.

**Edit Menu:**

- **Reinitialize Default Values** -- Restores all settings to defaults.

**Help Menu:**

- Links to the Analog Devices website, CN0393 product page, user guide,
  context help, and version information.

Capturing Results
~~~~~~~~~~~~~~~~~

Capturing results/samples can be performed by pressing either the Single
Capture or Continuous Capture controls. The number of samples is determined by
the Num Samples parameter. Results are analyzed and displayed on the Waveform,
Histogram, FFT, and Summary tabs following execution.

Standalone Mode
~~~~~~~~~~~~~~~

The CN0393 Evaluation Software can operate in standalone mode when the
evaluation hardware is not connected. Previously saved ``.tsv`` files can be
loaded for offline analysis and visualization with full plotting and analysis
capabilities. This mode activates when the user selects Cancel during hardware
detection or upon connection loss.

Documents
---------

- :adi:`CN0393 Circuit Note <CN0393>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0393-FMCZ Design & Integration Files
   <https://www.analog.com/cn0393-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`ADAQ7988 Product Page <ADAQ7988>`
- :adi:`AD8251 Product Page <AD8251>`
- :adi:`ADuM3470 Product Page <ADUM3470>`
- :adi:`ADuM3150 Product Page <ADUM3150>`
- :adi:`ADR4550 Product Page <ADR4550>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
