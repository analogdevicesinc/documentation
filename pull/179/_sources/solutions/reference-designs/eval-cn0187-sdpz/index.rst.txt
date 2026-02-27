.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0187

.. _eval-cn0187-sdpz:

EVAL-CN0187-SDPZ
=================

Crest Factor, Peak, and RMS RF Power Measurement.

Overview
--------

:adi:`CN0187` is a crest factor, peak, and RMS RF power measurement circuit
optimized for high speed, low power, and single 3.3 V supply operation. The
circuit measures peak and RMS power at any RF frequency from 450 MHz to 6 GHz
over a range of approximately 45 dB. The measurement results are converted to
differential signals in order to eliminate noise and are provided as digital
codes at the output of a 12-bit SAR ADC with serial interface and integrated
reference. A simple two-point calibration is performed in the digital domain.

.. figure:: cn0187-hw-1024.jpg
   :align: center
   :width: 500px

   EVAL-CN0187-SDPZ evaluation board

The EVAL-CN0187-SDPZ board connects to ADI's System Demonstration Platform
(SDP) and is powered by a +6 V supply or +6 V wall wart.

Required Equipment
------------------

- :adi:`EVAL-CN0187-SDPZ <CN0187>` evaluation board
- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- CN0187 Evaluation Software (supplied with provided CD in kit)
- Power supply: +6 V, or +6 V wall wart
- USB Type-A to USB Mini-B cable
- RF signal source (>6 GHz capable)
- Coaxial RF cable with SMA connectors

Minimum PC Requirements
~~~~~~~~~~~~~~~~~~~~~~~~

- Windows XP SP2, Windows Vista, or Windows 7
  Business/Enterprise/Ultimate editions
- Intel Pentium processor (x86 compatible), 1 GHz or faster
- 512 MB RAM and 2 GB available hard disk space
- .NET 3.5 Framework

Installing the Software
------------------------

#. Extract the file **CN0187 Eval Software.zip** and run **setup.exe**.

   .. note::

      It is recommended that you install the CN0187 Evaluation Software to the
      default directory path ``C:\Program Files\Analog Devices\CN0187\`` and all
      National Instruments products to ``C:\Program Files\National Instruments\``.

   .. figure:: step1.png
      :align: center

      CN0187 Evaluation Software installer welcome screen

#. Click **Next** to view the installation review page.

   .. figure:: step2.png
      :align: center

      Installation review page

#. Click **Next** to start the installation.

   .. figure:: step3.png
      :align: center

      Installation progress

#. Upon completion of the CN0187 Evaluation Software installation, the
   installer for the ADI SDP Drivers will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: step4.png
      :align: center

      ADI SDP Drivers installer

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended that you install the drivers to the default directory
      path ``C:\Program Files\Analog Devices\SDP\Drivers``.

#. Press **Next** to install the SDP Drivers and complete the installation of
   all software. Click **Finish** when done.

Connecting the Hardware
------------------------

.. figure:: cn0187_block_diagram_v1.png
   :align: center

   EVAL-CN0187-SDPZ hardware connection block diagram

#. Connect the 120-pin connector on the EVAL-CN0187-SDPZ circuit board to the
   connector marked **CON A** on the :adi:`EVAL-SDP-CB1Z` evaluation (SDP)
   board. Nylon hardware should be used to firmly secure the two boards, using
   the holes provided at the ends of the 120-pin connectors.
#. Using an appropriate RF cable, connect the RF signal source to the
   EVAL-CN0187-SDPZ board via the SMA RF input connector.
#. With power to the supply off, connect a +6 V power supply to the pins
   marked **+6 V** and **GND** on the board. If available, a +6 V wall wart
   can be connected to the barrel jack connector on the board and used in place
   of the +6 V power supply.
#. Connect the USB cable, supplied along with the :adi:`EVAL-SDP-CB1Z`
   evaluation board, from the SDP board to the USB port on the PC.

Using the Evaluation Software
------------------------------

The following section describes the steps required when using the hardware and
software together. Calibrations must be performed, followed by measurement
commands. Please read carefully to understand how to use the demo.

Below are the available software controls grouped according to their location
in the software GUI:

.. figure:: calibrate.png
   :align: center

   CN0187 Evaluation Software GUI overview

Calibration
~~~~~~~~~~~~

.. figure:: sub_calibration_intructions_v1.png
   :align: center

   Calibration instructions

.. important::

   Calibration procedure needs to be done for every change in frequency.

.. figure:: main_cal.png
   :align: center

   Calibration tab

The calibration tab provides the following controls:

**Input:**

#. **Input Power (dBm)** -- Value of a known power level input in dBm.
#. **Frequency (MHz)** -- Value of a known frequency level input in MHz.
#. **Acquire Data** -- Acquire the data from the provided input power and
   frequency level.
#. **Remove List** -- Remove the last data that was provided.
#. **Calibrate Data** -- Execute the calibration process.
#. **Clear Calibration** -- Clear the values from the previous settings.
#. **Save Calibration File** -- Save the current calibration values.
#. **Load Calibration File** -- Load a previously saved calibration file.

**Output:**

#. **Vrms (V)** -- Displays the calculated RMS voltage output from the known
   power level and frequency input.
#. **Peak (V)** -- Displays the calculated peak voltage output from the known
   power level and frequency input.
#. **Calibration Complete** -- Indicates a complete calibration process.

Measure Input Power
~~~~~~~~~~~~~~~~~~~~

.. figure:: main_measure.png
   :align: center

   Measure Input Power tab

.. important::

   The board must be calibrated before input power can be measured.

**Input Buttons:**

#. **Acquire Data** -- Acquire data from the device.
#. **Remove List** -- Remove the last data read.
#. **Clear Data** -- Set all display values to 0.
#. **Save Data to File** -- Save the values displayed.
#. **Peak-Hold Mode (Active Low)** -- Hold the last value read from acquiring
   the data.

**Output:**

#. **Frequency (MHz)** -- Displays the acquired frequency in MHz.
#. **Input Power (dBm)** -- Displays the acquired input power in dBm.
#. **Input Power (Vrms)** -- Displays the acquired input RMS voltage value.
#. **Vrms (V)** -- Displays the calculated RMS voltage value.
#. **Peak (V)** -- Displays the calculated peak voltage value.

Advanced
~~~~~~~~~

.. figure:: main_advance.png
   :align: center

   Advanced settings tab

.. important::

   Do not modify these values unless necessary.

#. **Sclk (Hz)** -- Set the SPI clock reference.
#. **/CS (Hz)** -- Set the chip select clock settings.
#. **Sample Size** -- Set the sample size.

Graphical Output
~~~~~~~~~~~~~~~~~

The graphical output displays measurement data in the following formats:

.. figure:: sub_vrms.png
   :align: center

   Vrms graphical output

.. figure:: sub_peak.png
   :align: center

   Peak graphical output

- **dBm** -- Output displayed in dBm
- **Vrms** -- Output displayed in Vrms

.. figure:: sub_crest.png
   :align: center

   Crest factor graphical output

.. figure:: crest_factor_sample_output.png
   :align: center

   Crest factor sample output

.. note::

   Crest factor is the peak amplitude of the waveform divided by the RMS value
   of the waveform.

Documents
---------

- :adi:`CN0187 Circuit Note <CN0187>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0187-SDPZ Design & Integration Files
   <https://www.analog.com/cn0187-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD629 Product Page <AD629>`
- :adi:`AD8622 Product Page <AD8622>`
- :adi:`AD8475 Product Page <AD8475>`
- :adi:`AD7170 Product Page <AD7170>`
- :adi:`ADuM5402 Product Page <ADUM5402>`
- :adi:`ADR435 Product Page <ADR435>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
