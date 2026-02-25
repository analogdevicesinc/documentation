.. _eval-cn0385-ardz:

EVAL-CN0385-FMCZ
=================

Isolated Multichannel Data Acquisition System.

Overview
--------

:adi:`CN0385` is an isolated multichannel data acquisition system that is
compatible with standard industrial signal levels. The components are
specifically selected to optimize settling time between samples, providing
18-bit performance at channel switching rates up to roughly 750 kHz.

The CN0385 can process eight gain-independent channels and is compatible with
both single-ended and differential input signals. The analog front end includes
the :adi:`ADG5207` multiplexer, the :adi:`AD8251` programmable gain
instrumentation amplifier (PGIA), the :adi:`AD8475` as a precision ADC driver
for performing the single-ended-to-differential conversion, and the
:adi:`AD4003`, an 18-bit, 2 MSPS Precision ADC. Gain configurations of 0.4,
0.8, 1.6, and 3.2 are available.

.. figure:: cn0385_1_simplifiedcircuitschematic.png
   :align: center

   Simplified circuit schematic

The maximum sample rate of the system is 2 MSPS in Turbo Mode for single
channel continuous sampling. The channel switching logic is synchronous to the
ADC conversions, and the maximum channel switching rate is 1.5 MHz. Channel
switching rates up to 100 kHz also provide 18-bit performance.

A complete design support package for the EVAL-CN0385-FMCZ evaluation board
containing schematics, layouts (native and Gerber), and bill-of-materials can
be found at: `CN0385-DesignSupport
<https://www.analog.com/CN0385-DesignSupport>`__.

Required Equipment
------------------

- EVAL-CN0385-FMCZ Evaluation Board
- :adi:`EVAL-SDP-CH1Z <SDP>` Controller Board (SDP-H1 Board)
- +5 V to +12 V power supply or wall wart (+9 V wall wart included)
- `CN0385 Evaluation Software <https://www.analog.com/CN0385>`__
- PC with a USB port and Windows XP, Windows Vista (32-bit), or Windows 7, 8,
  or 10 (32-bit) with .NET 4.0 framework installed (included in installation
  of SDP Drivers)
- USB type A to USB type mini-B cable
- Precision signal generators/DC sources

General Setup
-------------

- The EVAL-CN0385-FMCZ board connects to the :adi:`EVAL-SDP-CH1Z <SDP>` SDP-H1
  Board via the 160-pin connector.
- Refer to the Jumper Settings table for setting the EVAL-CN0385-FMCZ board to
  the desired power, reference, and signal chain configuration.
- The included +9 V power supply connects to P3 on the EVAL-CN0385-FMCZ board.
- The :adi:`EVAL-SDP-CH1Z <SDP>` SDP-H1 Board connects to the PC via the USB
  cable.

.. figure:: cn0385_2_generalsetupblockdiagram.png
   :align: center

   General setup block diagram

Connecting the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

#. Configure the various jumper positions to the desired settings (refer to the
   Jumper Settings table below).
#. Connect P1 of the EVAL-CN0385-FMCZ (CN0385 Evaluation Hardware) to the
   :adi:`EVAL-SDP-CH1Z <SDP>` (SDP-H1 Board).
#. Connect the included 12 V supply to Jack J7 on the :adi:`EVAL-SDP-CH1Z <SDP>`
   (SDP-H1 Board) board.
#. Connect the USB Cable to J1 on the :adi:`EVAL-SDP-CH1Z <SDP>` (SDP-H1 Board)
   board.
#. Connect the included 9 V supply to P3 on the EVAL-CN0385-FMCZ board.
#. Connect the USB Cable to the PC.

Jumper Settings
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Jumper Ref Des
     - Default
     - Function
   * - J2
     - A
     - Select external 9 V adaptor or bench DC 9 V from P3 or J1
   * - S1
     - A, B, C, D, E, F, G, H
     - Differential Inputs for all 8 channels

Installing the Software
-----------------------

#. Download the `CN0385 Evaluation Software
   <https://www.analog.com/CN0385>`__ and unzip the
   **CN0385_Evaluation_Software.zip** folder and run **setup.exe**.

   .. figure:: cn0385_3_install1.png
      :align: center

      Extracting the evaluation software

   .. figure:: cn0385_4_install2.png
      :align: center

      Running setup.exe

   .. figure:: cn0385_5_install3.png
      :align: center

      Installation wizard welcome screen

#. Click **Next** to view the installation review page.

   .. figure:: cn0385_6_install4.png
      :align: center

      Installation review page

#. Click **Next** to start the installation.

   .. figure:: cn0385_7_install5.png
      :align: center

      Installation in progress

#. Upon completion of the installation of the **CN0385 Evaluation Software**,
   click **Next** for the installer of the **ADI SDP Drivers** to execute.
   (The SDP drivers include an installation of the .NET 4.0 framework.)

   .. figure:: cn0385_8_install6.png
      :align: center

      CN0385 software installation complete

#. Press **Next** to set the installation location for the **SDP Drivers**.

   .. figure:: cn0385_9_sdpinstallation1.png
      :align: center

      SDP Drivers installation location

   .. figure:: cn0385_10_sdpinstallation2.png
      :align: center

      SDP Drivers installation ready

#. Press **Install** to install the **SDP Drivers** and complete the
   installation of all software. Click **Close** when done.

   .. figure:: cn0385_11_sdpinstallation3.png
      :align: center

      SDP Drivers installation complete

Using the Evaluation Software
------------------------------

Software Control and Indicator Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration Tab
^^^^^^^^^^^^^^^^^

.. figure:: cn0385_12_configtab.png
   :align: center

   Configuration tab

- **External REF (V)** -- Determines the value of the reference voltage used in
  calculations and analysis by the software. Affects aspects of the Waveform and
  Histogram plots (i.e. volt axis values, LSB-to-voltage conversions, etc.).
  Should be set to the value of the reference voltage used on the
  EVAL-CN0385-FMCZ Board (4.096 V by default).
- **Throughput Rate** -- Sets the sample rate of the :adi:`AD4003` (in KSPS).
  Note: the effective sample rate for each channel in the sequence (in KSPS) is
  equal to the value in Sample Rate divided by the number (1, 2, 4, or 8) of
  channels in the sequence.
- **ADC Register Setting** -- Set or clear the :adi:`AD4003` register control
  bits by clicking the corresponding button.
- **Read ADC Register** -- Read back the :adi:`AD4003` register control bits and
  OVP bit, and show them in the following LEDs on the right. "1" turns the LEDs
  on, and "0" turns the LEDs off.
- **ADC Control and Status LEDs** -- After Read ADC Register, the control and
  status bits are assigned to the following LEDs on the right. "1" turns the LEDs
  on, and "0" turns the LEDs off.
- **MUXSequencerEN** -- Set to ON to enable sequence mode, and set to OFF to
  disable sequence mode and use MUX Channel to select the target channel to
  sample.
- **MUX Channel** -- When MUXSequencerEN is OFF, MUX Channel is used to select
  the target channel to sample; When MUXSequencerEN is ON, MUX Channel is used
  to select the last channel (1, 2, 4, or 8) in the sequencer to sample.
- **CHx Gain** -- Select the gain for each channel.
- **Samples** -- Selects the sample number to be performed for each acquisition.
  If the MUXSequencerEN is ON, it is the sample number for each channel.
- **Single Capture** -- Initiates a set of conversion samples for each
  acquisition.
- **Continuous Capture** -- Initiates multiple sets of conversion samples. Each
  set of conversions contains a number of samples set and repeats until
  Continuous Capture is depressed.

Waveform Tab
^^^^^^^^^^^^^

.. figure:: cn0385_13_waveformtab.png
   :align: center

   Waveform tab

- **Waveform Plot** -- Displays the Waveform of the sampled data.
- **Waveform Graph Palette** -- Sets the display range of the Multi-Channel
  Waveform Plot.
- **Y-Axis Display Format** -- Selects whether the data will be displayed in raw
  code values or in equivalent voltage in the Plot. Note: code value to voltage
  conversions are calculated based on the value of VREF in the Configuration Tab.
- **Waveform Analysis** -- Calculation of the captured samples.

Multi-Channel Tab
^^^^^^^^^^^^^^^^^^

.. figure:: cn0385_14_multi-channeltab.png
   :align: center

   Multi-Channel tab

- **Multi-Channel Waveform Plot** -- Displays the data readback from each of the
  active and visible channels in the conversion sequence.
- **Multi-Channel Waveform Graph Palette** -- Sets the display range of the
  Multi-Channel Waveform Plot.
- **Multi-Channel Selectors** -- Selects which channels' data are visible on the
  Multi-Channel Waveform Plot. Note: channels must be included in the sequence
  to be displayed.
- **Y-Axis Display Format** -- Selects whether the data will be displayed in raw
  code values or in equivalent voltage in the Plot. Note: code value to voltage
  conversions are calculated based on the value of VREF in the Configuration Tab.
- **Seq Mode CH to Analysis** -- Selects the channel for the Waveform Analysis
  in channel sequencer mode.
- **Waveform Analysis** -- Calculation of the captured samples.

Histogram Tab
^^^^^^^^^^^^^^

.. figure:: cn0385_15_histogramtab.png
   :align: center

   Histogram tab

- **Histogram Plot** -- Displays the occurrences of the sampled codes.
- **Waveform Graph Palette** -- Sets the display range of the Histogram Plot.
- **Histogram Analysis** -- Calculation of the captured samples.

FFT Tab
^^^^^^^^

.. figure:: cn0385_16_ffttab.png
   :align: center

   FFT tab

- **FFT Spectrum Plot** -- Displays the FFT frequency response of the sampled
  codes.
- **Waveform Graph Palette** -- Sets the display range of the FFT Plot.
- **Seq Mode CH to Analysis** -- Selects the channel for the FFT Analysis in
  sequencer mode.
- **FFT Analysis** -- Calculation of the captured samples.
- **Show Harmonic Content** -- Shows the fundamental frequency and 2nd to 5th
  harmonics.

File Menu
^^^^^^^^^^

- **Save Captured Data** -- Saves the current captured samples of the CN0385
  Evaluation Software as a .csv file.
- **Load Captured Data** -- Selects a previously saved samples of CN0385
  Evaluation Software.
- **Take Screenshot** -- Captures the CN0385 Evaluation Software GUI and saves
  it as a picture.
- **Print Screenshot** -- Captures the CN0385 Evaluation Software GUI and sends
  it to the printer.
- **Exit** -- Closes the CN0385 Evaluation Software.

Help Menu
^^^^^^^^^^

- **Analog Devices Website** -- Opens the Analog Devices, Inc. website using the
  PC's current default web browser.
- **About** -- Displays the current version information of the CN0385 Evaluation
  Software in a pop-up.

Establishing a USB Connection Link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Verify that the SDP drivers are properly installed (see **Installing the
   Software**).
#. Ensure that the CN0385 Evaluation Hardware and the SDP-H1 Controller Board
   are correctly connected and powered up.
#. Run the `CN0385 Evaluation Software <https://www.analog.com/CN0385>`__
   (**CN0385.exe**).
#. If the CN0385 Evaluation Hardware is properly connected to the PC, the
   evaluation software will automatically establish a connection with the SDP-H1
   Controller Board.
#. If the software does not detect the CN0385 Evaluation Hardware, a pop-up will
   appear with options to reattempt the connection. Selecting **Rescan** will
   attempt to establish the USB connection again.

   .. figure:: cn0385_17_connectionfailure.png
      :align: center

      Connection failure dialog

Configuring a Conversion Sequence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configurations are defined in the Configuration tab. In normal mode the max
sampling rate is 1.5 MSPS. Only when Turbo Mode is enabled, the sampling rate
can go up to 2 MSPS. Turn MUXSequencerEN ON to enable the sequencer for
multi-channel sampling. In the sequencer mode, it can only convert in sequence
from channel 1 to the last channel defined by MUX Channel.

Capturing Samples
~~~~~~~~~~~~~~~~~~

After the configuration is done and the CN0385 Evaluation Hardware and Software
are connected, the software can initiate conversions. To capture samples:

#. Ensure that the value in **VREF** matches the reference voltage being used on
   the CN0385 Evaluation Hardware. Note that the Sample Rate is the sample rate
   of the :adi:`AD4003`, not the effective sample rate for each channel.
#. Select the desired **Sample Rate** and **SCK** rate.

   - Note that the **Sample Rate** is the sample rate of the ADC, not the
     effective sample rate for each channel.

#. Press either **Single Capture** to perform a single burst of sampling
   sequences or **Continuous Capture** to perform repeated bursts of sampling
   sequences until stopped.

Viewing Conversion Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~

After capturing samples or loading a previous set of conversion results, the
data and analysis items for each channel can be viewed using the **Waveform**
tab, the **Histogram** tab, the **FFT** tab and the **Summary** tab.

#. Select the **Multi-Channel** tab to view every channel's data on a single
   plot. The **Multi-Channel Selectors** set the visibility of each channel's
   data.

   .. figure:: cn0385_18_multichanneldata.png
      :align: center

      Multi-channel data view

#. Select the **Waveform** tab to view the sampled channel's data or analysis
   results in non-sequencer mode. The **Histogram** and **FFT** sub-tabs show
   the dc and ac analysis.

   .. figure:: cn0385_19_singlechannelwaveformdata.png
      :align: center

      Single channel waveform data

   .. figure:: cn0385_20_singlechannelhistodata.png
      :align: center

      Single channel histogram data

   .. figure:: cn0385_21_singlechannelfftdata.png
      :align: center

      Single channel FFT data

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0385-FMCZ Design & Integration Files
   <https://www.analog.com/cn0385-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD4003 Product Page <AD4003>`
- :adi:`AD8251 Product Page <AD8251>`
- :adi:`AD8475 Product Page <AD8475>`
- :adi:`ADG5207 Product Page <ADG5207>`
- :adi:`CN0385 Circuit Note <CN0385>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
