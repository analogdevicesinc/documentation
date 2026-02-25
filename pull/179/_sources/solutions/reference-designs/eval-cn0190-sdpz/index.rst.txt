.. _eval-cn0190-sdpz:

EVAL-CN0190-SDPZ
=================

Multivoltage Power System Reference Design.

Overview
--------

:adi:`CN0190 <CN0190>` is a reference solution for multivoltage power systems.
The design can easily be adapted to customer requirements and provides the most
popular system voltages. The circuit uses an optimum combination of switching
and linear regulators to provide an overall efficiency of approximately 78%
when the outputs are fully loaded. Output power delivered under full load is
approximately 25 W.

The circuit supplies most of the typical power rails required for digital and
analog circuits and also demonstrates an easy way to realize overvoltage,
undervoltage, and overcurrent detection and protection. In addition, this
module shows how to implement sequencing and power margining control.

The circuit is flexible and can accept a wide input voltage range from 6 V to
14 V. This is possible because the highly efficient switching controllers and
regulators used in the first stage of each power rail have correspondingly wide
input ranges. The :adi:`ADM1178` block provides overvoltage and overcurrent
detection and protection for the input supply, as well as hot-swap control for
the whole system. The :adi:`ADM1066` offers a single-chip solution for power
supply monitoring and sequencing control for all of the 12 power rails and also
margining control for the 3.3 V (2 A) rail.

.. figure:: cn0190-hw-1024.jpg
   :align: center

   EVAL-CN0190-EB1Z evaluation board

Required Equipment
------------------

Equivalents can be substituted:

- EVAL-CN0190-EB1Z evaluation board
- Tektronix TDS3034B 4-channel 300 MHz color digital phosphor oscilloscope
- Tektronix P6139A, 500 MHz, 8 pF, 10 MOhm, 10x passive probe
- Agilent N3302A, 150 W, 0--30 A, 0--60 V electronic load module combined
  with N3300A
- Agilent E3631A, 0--6 V/5 A; 0--25 V/1 A, triple output DC power supply
- Agilent 3458A, 8.5 digit digital multimeter
- Fluke 15B digital multimeter
- USB-SDP-CABLEZ
- PC (Windows 2000 or Windows XP) with USB interface

Test Setup
----------

Power Rails Efficiency Measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The test setup for power rails efficiency measurements uses the following
configuration:

.. figure:: block.png
   :align: center

   Test setup functional block diagram for power rails efficiency measurements

.. admonition:: Efficiency Formula

   Efficiency = P\ :sub:`OUT` / P\ :sub:`IN` = (V\ :sub:`OUT` x
   I\ :sub:`OUT`) / (V\ :sub:`IN` x I\ :sub:`IN`)

   - P\ :sub:`OUT` can be calculated by multiplying V\ :sub:`OUT` by
     I\ :sub:`OUT`.
   - V\ :sub:`IN` and I\ :sub:`IN` can be read directly from the display
     window of the Agilent E3631A DC power supply.
   - Electronic load should be set to constant current mode.

Ripple and Transient Response Measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: block2.png
   :align: center

   Test setup functional block diagram for ripple and transient response
   measurements

For ripple and transient response measurements:

- Channel A of the oscilloscope monitors the output voltage of the module.
- Channel B monitors the voltage across the 0.1 Ohm current sense resistor,
  which is proportional to the load current.
- Electronic load should be set to "switch" mode with preset amplitude and
  frequency.

Connectors and Jumper Configurations
------------------------------------

.. figure:: boardwithdes.png
   :align: center

   EVAL-CN0190-EB1Z board connectors and jumper layout

Input Power
~~~~~~~~~~~

Connector 1 accepts the input supply, which should be between +6 V and +14 V.

Output Power Options
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 25 20 35

   * - Connector
     - Voltage Output
     - Current Output
     - Power Topology
   * - Connector 2
     - +3.3 V
     - 2 A
     - Synchronous Buck
   * - Connector 3
     - +1.8 V
     - 1 A
     - Synchronous Buck
   * - Connector 4
     - +1.5 V
     - 1 A
     - Synchronous Buck
   * - Connector 5
     - +1.0 V
     - 2 A
     - LDO
   * - Connector 6
     - +1.2 V
     - 0.5 A
     - Synchronous Buck
   * - Connector 7
     - +3.0 V
     - 0.1 A
     - LDO
   * - Connector 8
     - -5.0 V
     - 0.2 A
     - Inverted Buck/Boost
   * - Connector 9
     - +5.0 V
     - 1 A
     - Synchronous Buck
   * - Connector 10
     - +2.5 V
     - 1 A
     - Synchronous Buck
   * - Connector 11
     - +3.3 V
     - 0.1 A
     - LDO
   * - Connector 12
     - VDD (+2.5 V, +5 V, +12 V, +15 V)
     - 0.1 A
     - Sepic-Cuk
   * - Connector 13
     - VEE (-2.5 V, -5 V, -12 V, -15 V)
     - 0.1 A
     - Sepic-Cuk

Switch Matrix
~~~~~~~~~~~~~

To select the VDD/VEE outputs on Connector 12 and Connector 13, the switch
matrix must be configured. Use the following table to select the desired output
voltages:

.. figure:: sw1.png
   :align: center

   Switch matrix configuration for VDD/VEE output selection

I2C Programming Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~

The I2C serial interface is on Connector 15:

- Pin 1: SCLK
- Pin 2: SDA
- Pin 3: GND

Software and Driver Installation
---------------------------------

You can design your own control strategy and download it into the ADM1066
through the I2C bus connector (JP1) using the ADM1066 Super Sequencer
evaluation board software.

To create a custom sequencing solution and program the ADM1066, perform the
following steps:

1. Download the USB-SDP-CABLEZ driver.
2. Install the *Super Sequencer Software*.
3. Install *Graphviz*.
4. Install the *prog106x Setup Application Software*.
5. Connect the USB-SDP-CABLEZ to the PC, and the other end to the
   EVAL-CN0190-EB1Z.
6. Download the custom .hex file to the EVAL-CN0190-EB1Z using the Windows
   command prompt.

.. note::

   The ADM1066 comes **pre-programmed out of the box** where all power outputs
   are active at the same time. You do not need to program the board unless you
   want to create your own custom power sequencing/monitoring solution.

Driver Installation
~~~~~~~~~~~~~~~~~~~

1. Install the USB-SDP-CABLEZ driver.
2. Open the file ``setup.exe`` located at the path
   ``\ADMxxxx Run-Time Installer\Installer\Volume\setup.exe``.

   .. figure:: usb1.png
      :align: center

      USB-SDP-CABLEZ driver setup

   .. note::

      It is recommended that you install the software to the default directory.

3. Follow the on-screen prompts to install the software.

   .. figure:: usb2.png
      :align: center

      USB-SDP-CABLEZ driver installation prompts

4. Plug in the USB-SDP-CABLEZ into your PC using the USB cable.
5. Windows will automatically find the new hardware (USB-SDP-CABLEZ) plugged
   into the PC.

   .. figure:: newdevice.png
      :align: center

      Windows new hardware detection for USB-SDP-CABLEZ

Sequencer Software Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open the file ``setup.exe`` located at the path
   ``\SuperSequencer Apps SW Installer\Volume\setup.exe``.

   .. figure:: soft1.png
      :align: center

      SuperSequencer software setup

   .. note::

      It is recommended that you install the SuperSequencer evaluation software
      to the default directory path ``C:\Program Files\``.

2. Follow the on-screen prompts to install the software.

   .. figure:: soft2.png
      :align: center

      SuperSequencer installation wizard

   .. figure:: soft3.png
      :align: center

      SuperSequencer license agreement

   .. figure:: soft4.png
      :align: center

      SuperSequencer installation directory selection

   .. figure:: soft5.png
      :align: center

      SuperSequencer installation complete

3. Install Graphviz.

   .. figure:: soft6.png
      :align: center

      Graphviz installation

4. Upon completion, follow the on-screen prompts to install the prog106x Setup
   Application Software.

   .. figure:: soft7.png
      :align: center

      prog106x setup wizard

   .. figure:: soft8.png
      :align: center

      prog106x license agreement

   .. figure:: soft9.png
      :align: center

      prog106x installation directory selection

   .. figure:: soft10.png
      :align: center

      prog106x installation complete

.. note::

   Visit the `Super Sequencer User Guide (UG-063)
   <https://www.analog.com/media/en/technical-documentation/user-guides/UG-063.pdf>`__,
   `Software Programming Tool (UG-049)
   <https://www.analog.com/media/en/technical-documentation/user-guides/UG-049.pdf>`__,
   and `Graphviz User Guide (AN-0975)
   <https://www.analog.com/media/en/technical-documentation/user-guides/AN-0975.pdf>`__
   for more information about the application software and automatic generation
   of state diagrams for the ADM1066.

Using Super Sequencer Software
-------------------------------

Super Sequencer evaluation software enables the user to create a new control
strategy and generate a new Intel hex file for the ADM1066. To generate a new
hex file:

1. Open ``SuperSequencerSoftwareEval.exe`` installed on the PC.

   .. figure:: sequencer_icon.png
      :align: center

      SuperSequencer software icon

2. Assuming all new configurations and controls have been set in the software,
   go to **File** and click **Save Settings to File**.

   .. figure:: savesettings.png
      :align: center

      Save Settings to File menu option

3. Select **Create Intel Hex File** and click **Save**.

   .. figure:: hexfile.png
      :align: center

      Create Intel Hex File dialog

4. Once saving is completed, the new hex file is ready to be downloaded to the
   ADM1066.

Downloading Firmware for ADM1066
---------------------------------

1. Copy the EEPROM hex file (e.g., ``ADM1066_SuperSequencing_REVB.hex``) to the
   root directory on Disk C: (e.g., ``C:\ADM1066_SuperSequencing_REVB.hex``).

2. Plug the USB-to-I2C converter dongle into the USB port on the PC. Plug the
   other end of the cable into JP1 on the right side of the EVAL-CN0190-EB1Z.

   .. figure:: usbtosdp.png
      :align: center

      USB-SDP-CABLEZ connected to the EVAL-CN0190-EB1Z

   .. note::

      Make sure the marks for the signals of JP1 on the PCB match the marks on
      the USB-SDP-CABLEZ:

      - SCL to SCL
      - SDA to SDA
      - GND to GND

3. Turn on the power supply to the EVAL-CN0190-EB1Z.

4. Open the Command Prompt (``C:\Windows\System32\cmd.exe``).

   .. figure:: cmd.png
      :align: center

      Windows Command Prompt

5. In the command prompt, enter:

   .. code-block:: none

      prog106x download 6A c:\ADM1066_SuperSequencing_REVB.hex

   and press Enter.

   .. note::

      The hex file name may differ depending on the user's custom
      configuration.

6. The on-chip EEPROM of ADM1066 is successfully programmed if the screen
   displays the following output after several seconds.

   .. figure:: program.png
      :align: center

      Successful ADM1066 EEPROM programming output

7. Remove power or turn off the power supply, then re-apply power to make the
   ADM1066 update the program from the embedded EEPROM.

Documents
---------

- :adi:`CN0190 Circuit Note <CN0190>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0190-EB1Z Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0190-DesignSupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - PADS project

Additional Information
----------------------

- :adi:`ADM1178 Product Page <ADM1178>`
- :adi:`ADM1066 Product Page <ADM1066>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
