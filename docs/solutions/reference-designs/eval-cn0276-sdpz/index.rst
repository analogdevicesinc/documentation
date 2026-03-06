.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0276

.. _eval-cn0276-sdpz:

EVAL-CN0276-SDPZ
=================

High Performance Resolver-to-Digital Converter Circuit.

Overview
--------

:adi:`CN0276` is a high performance 10-bit to 16-bit resolver-to-digital
converter (RDC) circuit. The system converts the modulated output of a resolver
to digital output. The :adi:`AD2S1210` provides an integrated solution for
accurately measuring angular position and velocity with a resolver.

In the system, the :adi:`AD2S1210` generates programmable excitation signals.
The :adi:`AD8692` and :adi:`AD8397` compose a third-order Butterworth low-pass
filter and power amplifier. The resolver's excitation signal has two amplitude
options, chosen by the power supply voltage automatically. The output signals
of the resolver pass through a third-order Butterworth low-pass filter made by
the :adi:`AD8694` to the :adi:`AD2S1210` inputs. Both transmit and receive
filters improve the performance of the RDC and filter out noise to increase EMC
characteristics.

The maximum tracking rate of the RDC is 3125 rps in 10-bit mode
(resolution = 21 arc min) and 156.25 rps in 16-bit mode
(resolution = 19.8 arc sec).

.. figure:: system.png
   :align: center

   CN0276 system block diagram.

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` evaluation board (SDP-B board)
- :adi:`EVAL-CN0276-SDPZ <CN0276>` evaluation board (CN-0276 board)
- Resolver (e.g., TS2620N21E11 from Tamagawa Seiki)
- Adjustable DC power supply: +6 V to +12 V, >500 mA
- USB Type-A to USB Mini-B cable
- PC with the following requirements:

  - Microsoft Windows 7 with SP1 (x86 or x64), or later
  - Intel Core processor (x86 or x64 compatible), 2 GHz or faster
  - At least 4 GB RAM and 8 GB available hard disk space
  - .NET Framework 4.5 or later
  - Microsoft Visual C++ 2010 SP1 Redistributable
  - SDP EEPROM Programmer software (supplied with CD)
  - CN0276 Programming File (supplied with CD)
  - CN0276 SDP Evaluation Software (supplied with CD)

Hardware Setup
--------------

General Setup
~~~~~~~~~~~~~

- The EVAL-CN0276-SDPZ (CN-0276 board) connects to the :adi:`EVAL-SDP-CB1Z`
  (SDP-B board) via the 120-pin connector CON A.
- Use the adjustable DC power supply to power the EVAL-CN0276-SDPZ via the
  **J4** connector.
- The :adi:`EVAL-SDP-CB1Z` (SDP-B board) connects to the PC via the USB
  cable.
- The resolver connects to the EVAL-CN0276-SDPZ via the 6-pin header at
  **J3**.

.. figure:: testdraft.png
   :align: center

   General test setup diagram.

Connecting the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

Connect the resolver to **J3** of the EVAL-CN0276-SDPZ as depicted in the
wiring table below.

.. note::

   If a different resolver is used other than the TS2620N21E11, the wiring
   schematic may be different.

Resolver Wiring (J3)
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - J3 Pin
     - Signal
     - TS2620N21E11 Wire
   * - 1
     - COS
     - Red
   * - 2
     - COSLO
     - Black
   * - 3
     - SINLO
     - Blue
   * - 4
     - SIN
     - Yellow
   * - 5
     - EXC
     - Red/White
   * - 6
     - nEXC
     - Yellow/White

Power Supply Wiring (J4)
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - J4 Pin
     - Type
   * - 1
     - VCC
   * - 2
     - GND

Software Setup
--------------

Installing the Software
~~~~~~~~~~~~~~~~~~~~~~~

#. Extract the file **CN0276_Evaluation_Software.zip** and open the file
   **setup.exe**.

   .. note::

      It is recommended that you install the CN0276 Evaluation Software to the
      default directory path ``C:\Program Files\Analog Devices\`` (32-bit) or
      ``C:\Program Files (x86)\Analog Devices\`` (64-bit), and all National
      Instruments products to ``C:\Program Files\National Instruments\``
      (32-bit) or ``C:\Program Files (x86)\National Instruments\`` (64-bit).

   .. figure:: softwareinstall1.png
      :align: center

      CN0276 evaluation software installer welcome screen.

#. Click **Next** to view the installation review page.

   .. figure:: softwareinstall2.png
      :align: center

      Installation review page.

#. Click **Next** to start the installation. After the installation, the
   installer for the ADI SDP Drivers will execute.

   .. figure:: softwareinstall3.png
      :align: center

      ADI SDP Drivers installer.

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended that you install the drivers to the default directory
      path ``C:\Program Files\Analog Devices\SDP\DriversR2\`` (32-bit) or
      ``C:\Program Files (x86)\Analog Devices\SDP\DriversR2\`` (64-bit).

   .. figure:: softwareinstall4.png
      :align: center

      SDP Drivers installation location.

#. Press **Next** to install the SDP Drivers and complete the installation of
   all software. Click **Finish** when done.

   .. figure:: softwareinstall5.png
      :align: center

      SDP Drivers installation complete.

Using the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Establishing a USB Connection Link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Follow the instructions to properly install the software and connect the
   hardware as described in the previous sections.
#. Open the file named **CN0276.exe** in the installation directory.

   .. note::

      If the software was installed to the default location it will be found at
      ``C:\Program Files\Analog Devices\CN0276\CN0276.exe`` (32-bit) or
      ``C:\Program Files (x86)\Analog Devices\CN0276\CN0276.exe`` (64-bit).

#. Click the **Connect** button. A window with a progress bar will load.

   .. figure:: software4.png
      :align: center

      USB connection progress window.

#. Upon success, the System Status String Indicator will display the SDP-B
   board serial number.

.. important::

   After powering on the EVAL-CN0276-SDPZ, the configuration data must be
   written to the :adi:`AD2S1210` before the first run.

Capturing Data
^^^^^^^^^^^^^^^

#. Establish a USB connection link.
#. Write the configuration data to the :adi:`AD2S1210`.
#. Set the number of samples.
#. Click the **Start** button.
#. When the sample count is reached or the **Stop** button is pressed, the
   conversion will halt.

Software Control and Indicator Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: slide1.png
   :align: center

   Evaluation software interface overview (1 of 3).

.. figure:: slide2.png
   :align: center

   Evaluation software interface overview (2 of 3).

.. figure:: slide3.png
   :align: center

   Evaluation software interface overview (3 of 3).

#. **Connect/Disconnect Button** -- Toggles the SDP-B board USB connection
   to the CN-0276 board. A connection to the SDP-B board must be made to use
   the software.
#. **Start Button** -- Begins collecting conversion data and presents the
   acquisitions in the chart.
#. **Stop Button** -- Stops collecting data from the CN-0276 board.
#. **Samples Setting** -- Sets the number of samples for each acquisition.
#. **Run Mode Setting** -- Enables persistent running mode of RDC samples.
#. **Control Tabs**

   - **Data Analyze** -- Shows the acquired data analyzed result in histogram.
   - **RDC Output** -- Includes two indicators showing the position and
     velocity output of the RDC, updated in real time when the RDC is
     converting.
   - **RDC Configuration** -- Read and write the internal registers of the
     :adi:`AD2S1210`.
   - **SDP Information** -- Shows the SDP-B board information when USB
     connection is available.

#. **SDP Status String Indicator** -- Displays a message from the SDP-B board.
#. **RDC Working Status LED** -- Shows the RDC working status; when the RDC
   is converting this LED lights up, otherwise it is off.
#. **Position Indicator** -- Displays the RDC position output in hexadecimal.
#. **Velocity Indicator** -- Displays the RDC velocity output in revolutions
   per second (rps).
#. **Configuration Write to AD2S1210** -- These values will be written to the
   AD2S1210 registers when the Write Configuration button is pressed.
#. **AD2S1210 Register Value** -- Read back values of the AD2S1210 registers.
#. **AD2S1210 Fault LED** -- Shows the fault status of the AD2S1210.
#. **Write Configuration Button** -- Writes the configuration area values to
   the AD2S1210 registers.

Documents
---------

- `AD2S1210 Data Sheet
  <https://www.analog.com/media/en/technical-documentation/data-sheets/AD2S1210.pdf>`__
- :adi:`CN0276 Circuit Note <CN0276>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0276-SDPZ Design & Integration Files
   <https://www.analog.com/cn0276-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD2S1210 Product Page <AD2S1210>`
- :adi:`AD8692 Product Page <AD8692>`
- :adi:`AD8397 Product Page <AD8397>`
- :adi:`AD8694 Product Page <AD8694>`
- :adi:`EVAL-SDP-CB1Z Product Page <EVAL-SDP-CB1Z>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
