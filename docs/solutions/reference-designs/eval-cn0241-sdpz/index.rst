.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0241

.. _eval-cn0241-sdpz:

EVAL-CN0241-SDPZ
=================

High-Side Current Sensing with Input Overvoltage Protection

.. important::

   This particular reference design has been **RETIRED** or **DEPRECATED**,
   which means it is no longer supported. This page is here for
   historical/reference purposes only.

Overview
--------

High-side current monitors are likely to encounter overvoltage conditions from
transients or when the monitoring circuits are connected, disconnected, or
powered down. This circuit uses the overvoltage protected :adi:`ADA4096-2` op
amp connected as a difference amplifier to monitor the high-side current. The
:adi:`ADA4096-2` has input overvoltage protection, without phase reversal or
latch-up, for voltages of 32 V higher than and lower than the supply rails.

The circuit is powered by the :adi:`ADP3336` adjustable low dropout 500 mA
linear regulator, which can also be used to supply power to other parts of the
system, if desired. Its input voltage can range from 5.2 V to 12 V when set for
a 5 V output. To save power, the current sensing circuit can be powered down by
removing power to the :adi:`ADP3336`; however, the power source, such as a
solar panel, can still operate.

This applies voltage to the inputs of the unpowered ADA4096-2; however, no
latch-up or damage occurs for input voltages up to 32 V. If slower throughput
rates are required, the :adi:`AD7920` can also be powered down between samples.
The :adi:`AD7920` draws a maximum of 5 uW when powered down and 15 mW when
powered up. The :adi:`ADA4096-2` requires only 120 uA under operational
conditions. When operating at 5 V, this is only 0.6 mW. The :adi:`ADP3336`
draws only 1 uA in the shutdown mode.

.. figure:: cn0241-hw-1024.jpg
   :width: 600px
   :align: center

   EVAL-CN0241-SDPZ evaluation board

Required Equipment
------------------

- :adi:`EVAL-CN0241-SDPZ <CN0241>` evaluation board
- :adi:`EVAL-SDP-CB1Z <EVAL-SDP-CB1Z>` controller board (SDP-B board)
- CN0241 Evaluation Software
- DC power supply capable of driving 6 V / 1 A
- DC power supply capable of driving 5 V / 2.5 A
- 2 Ohm / 12 W load resistor
- USB cable
- PC with Windows XP up to Windows 7 with USB interface

Hardware Setup
--------------

Block Assignments
~~~~~~~~~~~~~~~~~~

.. figure:: cn0241-hw-1024_l.jpg
   :width: 700px
   :align: center

   EVAL-CN0241-SDPZ block assignments

#. Connect :adi:`EVAL-CN0241-SDPZ <CN0241>` **(CN0241 Board)** to the
   :adi:`EVAL-SDP-CB1Z <EVAL-SDP-CB1Z>` **(SDP-B Board)** via the 120-pin
   connector **(SDP CONN)**.

#. Connect a 6 V power supply to the **+6V** and **GND** pins on the board. If
   available, a 6 V wall wart can be connected to the barrel connector, **J5**,
   in place of the 6 V power supply.

#. Connect the 5 V / 2.5 A DC supply to +VIN and GND on **J1**. Also connect
   the 2 Ohm / 12 W load resistor to LOAD and GND on **J1**.

#. **J2** is for SPI breakout.

.. figure:: cn0241-06-1024_setup.png
   :width: 550px
   :align: center

   EVAL-CN0241-SDPZ test setup

Installing the Evaluation Software
------------------------------------

#. Download and extract the file **CN0241 Evaluation Software** and open
   **setup.exe**.

   .. note::

      It is recommended that you install the CN0241 Evaluation Software to the
      default directory path ``C:\Program Files (x86)\Analog Devices\CN0241\``
      and all National Instruments products to
      ``C:\Program Files\National Instruments\``.

   .. figure:: cn0241-1.png
      :width: 500px
      :align: center

      CN0241 installer welcome screen

#. Click **Next** and accept the license agreement.

   .. figure:: cn0241-2.png
      :width: 500px
      :align: center

      License agreement

#. Click **Next** to view the installation review page.

   .. figure:: cn0241-3.png
      :width: 500px
      :align: center

      Installation review

#. Click **Next** to start the installation.

   .. figure:: cn0241-4.png
      :width: 500px
      :align: center

      Installation progress

#. Upon completion of the installation of the **CN0241 Evaluation Software**,
   the installer for the ADI SDP Drivers will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: cn0241-5.png
      :width: 500px
      :align: center

      SDP Drivers installer

#. Click **Next** to set the installation location for the **SDP Drivers**.

   .. note::

      It is recommended that you install the drivers to the default directory
      path ``C:\Program Files\Analog Devices\SDP\Drivers``.

   .. figure:: cn0241-6.png
      :width: 500px
      :align: center

      SDP Drivers installation location

#. Click **Next** to install the **SDP Drivers**. When prompted by Windows
   Security, press **Install**.

   .. figure:: cn0241-7.png
      :width: 500px
      :align: center

      Windows Security driver prompt

#. Click **Finish** to complete the installation.

   .. figure:: cn0241-8.png
      :width: 500px
      :align: center

      Installation complete

Running the System
-------------------

#. Apply power to the 6 V supply (or wall wart) connected to the
   :adi:`CN0241 Evaluation Board <CN0241>`.

#. Connect USB cable from PC to the USB mini connector on the SDP-B board.

#. Launch **CN0241 Evaluation Software** from the default installation
   location.

#. Click **Connect** to start communication between SDP-B and the
   :adi:`CN0241 Evaluation Board <CN0241>`.

#. Upon successful connection, select SDP connector A.

#. Set the desired number of samples.

#. Turn the 5 V / 2.5 A DC supply on when data is ready to be acquired.

#. Adjust the voltage output accordingly to output the amount of current needed
   to be measured.

#. Click **Sample Data** to start acquisition of data.

Using the Evaluation Software
------------------------------

Main Window
~~~~~~~~~~~~

.. figure:: cn0241-main.jpg
   :width: 700px
   :align: center

   CN0241 evaluation software main window

.. list-table::
   :header-rows: 1
   :widths: 10 40

   * - Control
     - Description
   * - Connect Button
     - Starts the connection between the CN0241 Evaluation Board and the SDP-B
       Controller Board.
   * - Disconnect Button
     - Ends the connection between the CN0241 Evaluation Board and the SDP-B
       Controller Board.
   * - Select SDP Connector
     - Selects which 120-pin connection of the SDP-B Board to use.
   * - Sample Size
     - Sets the number of samples.
   * - Sample Data Button
     - Starts the acquisition of measurement data.
   * - Save Data Button
     - Saves the acquired measurement data.
   * - Quit Button
     - Closes the evaluation software.

Display Tabs
^^^^^^^^^^^^^

- **Sample Data Tab** -- Shows the acquired measurement data in terms of ADC
  codes with respect to the samples. By right-clicking within the area, more
  functions can be viewed. Graph palette can be hidden by deselecting it and
  other items can be added such as plot legend, scale legend, etc.

  .. figure:: cn0241-sd.jpg
     :width: 400px
     :align: center

     Sample Data tab

- **Histogram Tab** -- Shows the acquired measurement data in terms of number
  of counts with respect to the ADC codes. The same right-click functions are
  available as in the Sample Data tab.

  .. figure:: cn0241-h.jpg
     :width: 400px
     :align: center

     Histogram tab

- **Configure Tab** -- Contains the following controls:

  - **AD7920 Mode** -- Can choose between two modes:

    - **Power Down Between Conversions**
    - **Normal Operation**
  - **Read Firmware** -- Reads the firmware of the CN0241 Evaluation Board.
  - **Flash LED** -- Flashes the LED on the SDP controller board.

  .. figure:: cn0241-c.jpg
     :width: 400px
     :align: center

     Configure tab

Documents
---------

- :adi:`CN0241 Circuit Note <CN0241>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0241-SDPZ Design & Integration Files
   <https://www.analog.com/cn0241-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - PADS project

Additional Information
----------------------

- :adi:`ADA4096-2 Product Page <ADA4096-2>`
- :adi:`AD7920 Product Page <AD7920>`
- :adi:`ADP3336 Product Page <ADP3336>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
