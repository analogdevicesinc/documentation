.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0251

.. _eval-cn0251-sdpz:

EVAL-CN0251-SDPZ
=================

Flexible Wide Dynamic Range Signal Conditioner.

Overview
--------

:adi:`CN0251` is a flexible signal conditioning circuit for processing signals
of wide dynamic range, varying from several mV p-p to 20 V p-p. The circuit
provides the necessary conditioning and level shifting and achieves the dynamic
range using the internal programmable gain amplifier (PGA) of the high
resolution analog-to-digital converter (ADC).

A +/-10 V full-scale signal is very typical in process control and industrial
automation applications; however, in some situations, the signal can be as
small as several mV. Attenuation and level shifting is necessary to process a
+/-10 V signal with modern low voltage ADCs. However, amplification is needed
for small signals to make use of the dynamic range of the ADC. Therefore, a
circuit with a programmable gain function is desirable when the input signal
varies over a wide range.

In addition, small signals may have large common-mode voltage swings;
therefore, high common-mode rejection (CMR) is required. In some applications,
where the source impedance is large, high impedance is also necessary for the
analog front-end input circuit.

The circuit uses the :adi:`AD7192` precision sigma-delta ADC with programmable
gain and the :adi:`AD8475` fully-differential attenuating amplifier for signal
conditioning.

.. figure:: cn0251-simplified_schematic.png

   CN0251 simplified schematic

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- :adi:`EVAL-CN0251-SDPZ <CN0251>` evaluation board (CN-0251 board)
- +6 V power supply
- +/-15 V dual power supply
- CN0251 Evaluation Software
- :adi:`ADALM2000` measuring instrument
- Scopy Software (with Scopy project file SigGen.ini)
- USB Type-A to USB Mini-B cable
- USB Type-A to USB Micro-B cable
- PC with Windows XP Service Pack 2 (32-bit) or higher, 2x USB Type-A
  ports, 1 GHz processor, 512 MB RAM, 500 MB available disk space

Hardware Setup
--------------

General Setup
~~~~~~~~~~~~~

- The EVAL-CN0251-SDPZ (CN-0251 Board) connects to the :adi:`EVAL-SDP-CB1Z`
  (SDP-B Board) via the 120-pin connector at **J5**.
- The +6 V power supply powers the CN-0251 board via the screw terminals at
  **J3**.
- The +/-15 V dual power supply powers the CN-0251 board via the screw
  terminals at **J4**.
- The :adi:`EVAL-SDP-CB1Z` (SDP-B Board) connects to the PC via the USB
  Type-A to USB Mini-B cable.
- The :adi:`ADALM2000` connects to the PC via the USB Type-A to USB Micro-B
  cable.
- The :adi:`ADALM2000` connects to the EVAL-CN0251-SDPZ (CN-0251 Board) via
  the screw terminals at **J1**.

.. figure:: cn0251-test_setup.png

   CN0251 test setup

Connecting the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

#. Ensure the jumpers are populated on the EVAL-CN0251-SDPZ (CN-0251 Board)
   as depicted in the figure below.

   - **JP1** and **JP2** configure the analog inputs for single-ended or
     differential inputs.
   - **JP3** and **JP4** configure the gain of the :adi:`AD8475` to be 0.4x
     or 0.8x.

   .. figure:: cn0251-jumpers.png

      CN0251 jumper configuration

#. Connect the :adi:`ADALM2000` to the EVAL-CN0251-SDPZ (CN-0251 Board) as
   depicted in the figures below.

   - The waveform outputs should be connected to **J1:2 (IN1-)** and
     **J1:3 (IN2+)** of the CN-0251 board.
   - The :adi:`ADALM2000` ground should be connected to **AGND** of the
     CN-0251 board.

   .. figure:: cn0251-discovery.png

      ADALM2000 connection to CN0251

#. Connect the +6 V power supply to the screw terminal at **J3**.
#. Connect the +/-15 V power supply to the screw terminal at **J4**.
#. Connect the SDP-B board to the CN-0251 board.

.. figure:: cn0251-discovery_board.png

   CN0251 connected to SDP-B board

Getting Started with ADALM2000 and Scopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Use the USB Type-A to USB Micro-B cable to connect the :adi:`ADALM2000`
   to the PC.
#. Upon connecting the ADALM2000 to Scopy, load the project file named
   **SigGen.ini** then click on the **Signal Generator** tab on the left
   pane.
#. Click the **Run** button.

Software Setup
--------------

Software Control and Indicator Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: cn0251-software.png

   CN0251 evaluation software main window

The evaluation software provides the following controls and indicators:

#. **Connect/Reconnect Button** -- When pressed, the SDP-B board makes a USB
   connection to the CN-0251 board. A connection to the SDP-B board must be
   made to use the software.
#. **Capture Data Button** -- When pressed, the SDP-B board collects
   conversion data and presents the acquisitions in the chart.
#. **Save Data Button** -- When pressed, the software saves the data
   collected to a tab-delimited ASCII spreadsheet file.
#. **Control Tabs**:

   - **Data** -- Brings the data collection chart to the front.
   - **Analysis** -- Brings the data analysis histogram to the front.
   - **Configure System** -- Brings the system configuration control to the
     front.
   - **SDP Board Information** -- Brings the SDP board information indicators
     to the front.

#. **Input Channel Drop-Down Menu** -- Selects the channel to capture data
   from.
#. **Input Range Drop-Down Menu** -- Selects the analog input voltage range
   for the selected channel.
#. **AD8475 Gain Indicator** -- Displays the gain setting required from the
   :adi:`AD8475`.

   .. important::

      Jumpers **JP3** and **JP4** on the EVAL-CN0251-SDPZ (CN-0251 Board)
      must be populated to reflect the value displayed by this indicator.

#. **AD7192 Gain Indicator** -- Displays the gain currently programmed into
   the :adi:`AD7192`.
#. **Samples to Capture Control** -- Sets the number of samples to capture
   once the Capture Data button is pressed.
#. **Display Unit Drop-Down Menu** -- Selects chart y-axis units to display.
#. **Chart Controls** -- Allows the user to zoom in, zoom out, and pan
   through the data collected.
#. **System Status String Indicator** -- Displays a message detailing the
   current state of the software.

Establishing a USB Connection Link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Follow the instructions to properly install the software and connect the
   hardware as described in the previous sections.
#. Open the file named **CN0251.exe** in the installation directory.

   .. note::

      If the software was installed to the default location it will be found
      at ``C:\Program Files\Analog Devices\CN0251\CN0251.exe``.

#. Click the **Connect/Reconnect** button. A window with a progress bar will
   load.

   .. figure:: cn0251-software-wait.png

      CN0251 connection progress

#. Upon success, the System Status String Indicator will display
   *Ready to Capture Data*.

Capturing Data
~~~~~~~~~~~~~~

#. Establish a USB connection link.
#. Click the **Input Channel Drop-Down Menu** to select the channel to
   convert.
#. Click the **Input Range Drop-Down Menu** to select the range of the
   analog input voltage.

   .. important::

      Changing this control will change the AD8475 Gain Indicator. Please
      ensure that **JP3** and **JP4** on the EVAL-CN0251-SDPZ (CN-0251
      Board) are populated to reflect the gain displayed by the AD8475 Gain
      Indicator.

#. Input the number of samples to capture into the **Samples to Capture
   Control**.
#. Click the **Capture Data** button and wait until acquisition is complete.

   .. figure:: cn0251-capture-wait.png

      CN0251 data capture in progress

Changing the Display Units
~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Click the **Display Unit Drop-Down Menu** to select the units to display.

Saving Data to a Spreadsheet File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Establish a USB connection link.
#. Capture data.
#. Click the **Save Data** button.
#. Browse to the directory location where the spreadsheet file is to be
   saved.
#. Name the file.
#. Click the **OK** button.

.. note::

   The software saves the spreadsheet file as ASCII text with columns
   separated by tabs.

Documents
---------

- :adi:`CN0251 Circuit Note <CN0251>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0251-SDPZ Design & Integration Files
   <https://www.analog.com/cn0251-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD7192 Product Page <AD7192>`
- :adi:`AD8475 Product Page <AD8475>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
