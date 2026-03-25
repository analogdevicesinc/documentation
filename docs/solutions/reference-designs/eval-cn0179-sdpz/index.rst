.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0179

.. _eval-cn0179-sdpz:

EVAL-CN0179-PMDZ
=================

4 mA to 20 mA Current Loop Transmitter

Overview
--------

The :adi:`CN0179 <CN0179>` circuit is a 4 mA to 20 mA current loop transmitter
for communication between a process control system and its actuator. Besides
being cost effective, this circuit offers an industry-leading low power
solution.

The 4 mA to 20 mA current loop has been used extensively in programmable logic
controllers (PLCs) and distributed control systems (DCSs), with digital or
analog inputs and outputs. Current loop interfaces are usually preferred because
they offer the most cost effective approach to long distance noise immune data
transmission.

The combination of the low power :adi:`AD8657` dual op amp, :adi:`AD5641` DAC,
and :adi:`ADR02` reference allows more power budget for higher power devices,
such as microcontrollers and digital isolators. The circuit output is 0 mA to
20 mA of current. The 4 mA to 20 mA range is usually mapped to represent the
input control range from the DAC or microcontroller, while the output current
range of 0 mA to 4 mA is often used to diagnose fault conditions.

Required Equipment
------------------

- :adi:`EVAL-CN0179-PMDZ <EVAL-CN0179-PMDZ>` evaluation board
- :adi:`EVAL-SDP-CB1Z <EVAL-SDP-CB1Z>` evaluation board (SDP-B board)
- :adi:`SDP-PMD-IB1Z <SDP-PMD-IB1Z>` interposer board
- CN0179 Evaluation Software (supplied with provided CD in kit)
- USB Type-A plug to USB Mini-B plug cable
- Agilent E36311A dual DC power supply or equivalent
- Agilent 3458A multimeter or equivalent
- +6 V wall wart power supply

Minimum PC/System Requirements
-------------------------------

- Windows XP SP2, Windows Vista, or Windows 7
  Business/Enterprise/Ultimate editions
- Intel Pentium processor (x86 compatible), 1 GHz or faster
- 512 MB RAM and 2 GB available hard disk space
- .NET 3.5 Framework

Installing the Evaluation Software
------------------------------------

#. Extract the file **CN0179 Eval Software.zip** and open the file
   **setup.exe**.

   .. note::

      It is recommended that you install the CN0179 Evaluation Software to the
      default directory path ``C:\Program Files\Analog Devices\CN0179\`` and all
      National Instruments products to ``C:\Program Files\National Instruments\``.

#. Click **Next** to view the installation review page.

#. Click **Next** to start the installation.

#. Upon completion of the installation of the **CN0179 Evaluation Software**,
   the installer for the **ADI SDP Drivers** will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

#. Press **Next** to set the installation location for the **SDP Drivers**.

   .. note::

      It is recommended that you install the drivers to the default directory
      path ``C:\Program Files\Analog Devices\SDP\Drivers``.

#. Press **Next** to install the **SDP Drivers** and complete the installation
   of all software. Click **Finish** when done.

Hardware Setup
--------------

.. figure:: cn0179-hardware.png
   :width: 600px

   EVAL-CN0179-PMDZ hardware setup diagram

#. Connect the 120-pin connector of the :adi:`SDP-PMD-IB1Z <SDP-PMD-IB1Z>`
   circuit board to the connector marked **CON A** on the
   :adi:`EVAL-SDP-CB1Z <EVAL-SDP-CB1Z>` evaluation (SDP) board. Nylon hardware
   should be used to firmly secure the two boards, using the holes provided at
   the ends of the 120-pin connectors.

#. Place shunt on header **JP1** to give +3.3 V voltage out as seen in the
   label found on the :adi:`SDP-PMD-IB1Z <SDP-PMD-IB1Z>`.

#. Connect the 12-pin right angle male pin header of
   :adi:`EVAL-CN0179-PMDZ <EVAL-CN0179-PMDZ>` to the 12-pin right angle female
   pin header of :adi:`SDP-PMD-IB1Z <SDP-PMD-IB1Z>`.

#. Connect the current meter in series with the Iout terminal block of the
   :adi:`EVAL-CN0179-PMDZ <EVAL-CN0179-PMDZ>`.

#. Connect DC Power Supply (+18 V / GND) to the Power connector **P1**.

#. Plug the mini end of the USB cable into connector **J1** of the
   :adi:`EVAL-SDP-CB1Z <EVAL-SDP-CB1Z>` and connect the other end of the USB
   cable into the laptop or PC.

#. Plug in the wall wart and connect it to connector **J1** of the
   :adi:`SDP-PMD-IB1Z <SDP-PMD-IB1Z>`.

#. Place shunt on Header **J1** to measure the voltage across the load on the
   Iout terminal block. No shunt means current measurement.

Opening and Enabling the Evaluation Software
----------------------------------------------

#. Launch the executable found at ``C:\Program Files\Analog Devices\CN0179``
   and press the **Connect** button.

#. After pressing the **Connect** button, a prompt will appear informing the
   user if the SDP is already connected.

#. Choose between two operating modes:

   - **Normal Operation** -- DAC has normal current consumption of 100 uA
     maximum. In this mode, the DAC is able to start gathering data from the
     system and all the buttons found in the System Controls will be enabled.
   - **Power Down Mode** -- The DAC's current consumption falls to typically
     0.5 uA. DAC is tristated and cannot acquire data from the system. DAC
     registers are unaffected when in power down mode.

Using the Evaluation Software
------------------------------

There are two ways to select the input control on the DAC: one is for setting
the Output Current while the other is for setting the DAC Code.

.. figure:: cn0179-sofware-description.png

   CN0179 evaluation software -- DAC Code input mode

.. figure:: cn0179-sofware-description-0.png

   CN0179 evaluation software -- Output Current input mode

Software Control Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 10 40

   * - Control
     - Description
   * - Enter Hex Code
     - Allows entering a value from 0x000 to 0x3FF.
   * - Iout
     - Shows the calculated output current depending on the input code.
   * - Data Bits
     - Binary equivalent of the code loaded to the :adi:`AD5641` DAC.
   * - VDAC
     - Shows the calculated DAC output voltage depending on the input code.
   * - Enter Output Current
     - Allows entering a value from 0 to 20 (mA).
   * - Data Code
     - Shows the hex code equivalent of the value loaded to the :adi:`AD5641`
       DAC.
   * - Write DAC
     - When pressed, the values/codes entered will be sent to the :adi:`AD5641`
       DAC via SPI.
   * - System Status String Indicator
     - Displays a message to the user detailing the current state of the
       software.
   * - System Status LED Indicator
     - Displays the current state of the software in the form of an LED. There
       are three status LED colors: yellow (Busy), green (Inactive), and red
       (Error).
   * - SDP Board Information
     - Provides details on the firmware version of the Blackfin used by the SDP
       board.

Documents
---------

- :adi:`CN0179 Circuit Note <CN0179>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0179-PMDZ Design & Integration Files
   <https://www.analog.com/cn0179-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD8657 Product Page <AD8657>`
- :adi:`AD5641 Product Page <AD5641>`
- :adi:`ADR02 Product Page <ADR02>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
