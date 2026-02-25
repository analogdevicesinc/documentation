.. _eval-cn0194-sdpz:

EVAL-CN0194-SDPZ
=================

Galvanically Isolated High Speed Simultaneous Sampling ADC

Overview
--------

:adi:`CN0194 <CN0194>` provides galvanic isolation for high speed, high
accuracy, simultaneous sampling analog-to-digital conversion applications. The
:adi:`AD7685` is a 16-bit, charge redistribution successive approximation (SAR)
analog-to-digital converter (ADC) that operates from a single VDD power supply
from 2.3 V to 5.5 V. It contains a low power, high speed, 16-bit sampling ADC
with no missing codes, no pipeline delay, an internal conversion clock, and a
versatile serial interface port. The ADC also contains a low noise, wide
bandwidth, short aperture delay, track-and-hold circuit. The AD7685 PulSAR ADC
is versatile and allows monitoring of multiple channels through daisy chaining.

.. figure:: cn0194-00-1024_sch.png
   :width: 600px
   :align: center

   CN0194 circuit schematic

Required Equipment
------------------

- :adi:`EVAL-CN0194-SDPZ <EVAL-CN0194-SDPZ>` evaluation board (CN-0194 board)
- :adi:`EVAL-SDP-CB1Z <EVAL-SDP-CB1Z>` evaluation board (SDP-B board)
- Power supply:

  - Adjustable DC power supply, output from +6 V to +12 V, over 500 mA
  - 6 to 12 V DC wall wart
- USB Type-A plug to USB Mini-B plug cable
- PC with the following:

  - Microsoft Windows 7 with SP1 x86 or x64 version, or later
  - Intel Core processor (x86 or x64 compatible), 2 GHz or faster
  - At least 4 GB RAM and 8 GB available hard disk space
  - `.NET Framework 4.5 <http://www.microsoft.com/en-us/download/details.aspx?id=30653>`__
    or later
  - `Microsoft Visual C++ 2010 SP1 Redistributable
    <http://www.microsoft.com/en-us/download/details.aspx?id=13523>`__
  - SDP EEPROM Programmer software (supplied with CD)
  - CN0194 Programming File (supplied with CD)
  - CN0194 SDP Evaluation Software (supplied with CD)

Hardware Setup
--------------

- EVAL-CN0194-SDPZ connects to the SDP-B board via the 120-pin connector
  **CON A**.
- Connect +6 V DC power supplies on the **J1** and **J2** connectors to power
  the EVAL-CN0194-SDPZ.
- EVAL-CN0194-SDPZ is ready to use if diodes **D3**, **D4**, and **D7** light
  up.
- The EVAL-SDP-CB1Z connects to the PC via the USB cable.
- Apply the input signals on the provided points on the board labeled **AIN1**
  and **AIN2**.

Installing the Software
-------------------------

#. Extract the file **CN0194_Evaluation_Software.zip** and open the file
   **setup.exe**.

   .. note::

      It is recommended that you install the CN0194 Evaluation Software to the
      default directory path ``C:\Program Files\Analog Devices\`` (in 32-bit
      OS) or ``C:\Program Files (x86)\Analog Devices\`` (in 64-bit OS), and all
      National Instruments products to ``C:\Program Files\National Instruments\``
      (in 32-bit OS) or ``C:\Program Files (x86)\National Instruments\`` (in
      64-bit OS).

   .. figure:: software_1.jpg
      :align: center

      CN0194 evaluation software installation wizard

#. Click **Next** to view the installation review page.

   .. figure:: software_2.jpg
      :align: center

      Installation review page

#. Click **Next** to start the installation. After the installation, the
   installer for the **ADI SDP Drivers** will execute.

   .. figure:: software_3.jpg
      :align: center

      ADI SDP Drivers installer

#. Press **Next** to set the installation location for the **SDP Drivers**.

   .. note::

      It is recommended that you install the drivers to the default directory
      path ``C:\Program Files\Analog Devices\SDP\DriversR2\`` (in 32-bit OS) or
      ``C:\Program Files (x86)\Analog Devices\SDP\DriversR2\`` (in 64-bit OS).

   .. figure:: software_4.jpg
      :align: center

      SDP Drivers installation location

#. Press **Next** to install the **SDP Drivers** and complete the installation
   of all software. Click **Finish** when done.

   .. figure:: software_5.jpg
      :align: center

      SDP Drivers installation complete

Using the Evaluation Software
------------------------------

Software Control and Indicator Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: software_use.jpg
   :width: 800px
   :align: center

   CN0194 evaluation software main window

.. list-table::
   :header-rows: 1
   :widths: 10 40

   * - Control
     - Description
   * - Connect/Disconnect Button
     - Toggles the SDP-B board USB connection to the CN-0194 board. A
       connection to the SDP-B board must be made to use the software.
   * - Capture Data Button
     - Collects conversion data from the SDP-B board and presents the
       acquisitions in the chart.
   * - Save Data Button
     - Saves the acquired data to a file.
   * - Sample Rate Setting
     - Sets the speed at which the ADC will convert.
   * - Samples Setting
     - Sets the number of samples for each capture data button press.
   * - Channel Display
     - Sets which channel is used and displayed.

Control Tabs
^^^^^^^^^^^^^

- **Time Domain** -- Shows the signal received by the ADC plotted as amplitude
  vs. time.
- **Frequency Domain** -- Shows the signal received by the ADC plotted as
  amplitude vs. frequency. This tab includes indicators for position and
  velocity output of the RDC, updated in real time when the RDC is converting.
- **Histogram** -- Shows the distribution of the captured signal amplitude
  displayed as ADC code.
- **S/W Version Info** -- Shows the SDP-B board information when a USB
  connection is available.

Navigation Tools
^^^^^^^^^^^^^^^^^^

- **Cursor** -- Standard cursor for data inspection.
- **Magnification** -- Contains magnification tools for zooming.
- **Hand** -- Used for navigating through the graph.

Axis Tools
^^^^^^^^^^^

- **Text Box** -- Provides easy graph navigation.
- **Lock** -- Enables/disables auto scroll of the graph.
- **Settings** -- Contains axis settings.

Frequency Analysis Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 15 35

   * - Indicator
     - Description
   * - THD
     - Total harmonic distortion
   * - SNR
     - Signal to noise ratio in decibels
   * - SINAD
     - Signal over noise and amplitude distortion
   * - SFDR
     - Spurious free dynamic range
   * - Sin/N
     - Signal over noise power
   * - Noise floor
     - Noise power level
   * - Fund ampl
     - Amplitude of fundamental frequency
   * - Fund Freq
     - Fundamental frequency of the signal

SDP Firmware Revision Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Major Rev** -- Major firmware revision number.
- **Minor Rev** -- Minor firmware revision number.
- **Date** -- Firmware build date.
- **Host Code Rev** -- Host code revision.
- **BF Code Rev** -- Blackfin code revision.
- **Time** -- Firmware build time.

Establishing a USB Connection Link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Follow the instructions to properly install the software and connect the
   hardware as described in the previous sections.

#. Open the file named **CN0194.exe** in the installation directory.

   .. note::

      If the software was installed to the default location it will be found at
      ``C:\Program Files\Analog Devices\CN0194\CN0194.exe`` (in 32-bit OS) or
      ``C:\Program Files (x86)\Analog Devices\CN0194\CN0194.exe`` (in 64-bit
      OS).

#. Click the **Connect Button**. A window with a progress bar will load.

   .. figure:: software_connect.png
      :align: center

      USB connection progress dialog

#. Upon success, the **System Status String Indicator** will display the SDP
   board serial number.

Capturing Data
~~~~~~~~~~~~~~~

#. Establish a USB connection link.
#. Set the preferred sample rate, samples, and channel.
#. Click the **Capture Data Button**.
#. When the number of samples reaches the samples setting, the converting will
   stop.
#. Click the **Save Data Button** to save the conversion data.

Documents
---------

- :adi:`CN0194 Circuit Note <CN0194>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0194-SDPZ Design & Integration Files
   <https://www.analog.com/cn0194-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD7685 Product Page <AD7685>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
