.. _eval-cn0270-sdpz:

EVAL-CN0270-EB1Z
=================

4--20 mA Transmitter with HART Communication

Overview
--------

:adi:`CN0270 <CN0270>` is a complete 4--20 mA transmitter with HART (Highway
Addressable Remote Transducer) communication system. It uses the :adi:`AD5420`,
a 16-bit 4--20 mA current source DAC, and :adi:`AD5700`/:adi:`AD5700-1`, a low
power HART modem. The circuit can be configured with various process control
current loop standards such as 4--20 mA, 0--20 mA, and 0--24 mA. This circuit
adheres to the HART physical layer specifications as defined by the HART
Communication Foundation, for example, the analog rate of change and noise
during silence specifications.

The EVAL-CN0270-EB1Z evaluation board comes with an onboard ADI microcontroller
that handles communication between the system and the evaluation software. It
also complies with the double PMOD form factor for use with external processors.

Required Equipment
------------------

- EVAL-CN0270-EB1Z evaluation board
- USB-SWD/UART-EMUZ board (included with kit)
- CN0270 Evaluation Software (supplied with provided CD in kit)
- DC power supply, 24 V recommended (12 V to 36 V compatible)
- Multimeter
- USB Type-A plug to USB Mini-B plug cable

General Setup
--------------

- The board is supplied via terminal block **P1**, +24 V DC is recommended.
- The current loop output is derived from terminal block **P3**.
- The **USB-SWD/UART-EMUZ** connects to the **J-Link header** for control
  using the evaluation software.

.. figure:: cn0270_board.png
   :width: 600px

   EVAL-CN0270-EB1Z evaluation board

.. figure:: cn0270_jlink_connect.png
   :width: 300px

   J-Link connection to the EVAL-CN0270-EB1Z

Jumper Configuration
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 10 15 35

   * - Jumper
     - Setting
     - Function
   * - P2
     - OPEN
     - Disconnects the 499 Ohm load resistor across current output and GND
   * - P2
     - SHORT
     - Connects a 499 Ohm load resistor across current output and GND
   * - PMOD
     - OPEN
     - Control is via onboard processor and J-Link header. Choose this option
       if you want to connect the board using the J-Link USB and use the CN0270
       Evaluation Software.
   * - PMOD
     - SHORT
     - Control is via PMOD headers. Choose this option if you want to use the
       circuit for prototyping or with external processors.
   * - XTAL
     - Towards position 1
     - AD5700-1 is clocked using the on-chip oscillator
   * - XTAL
     - Towards position 0
     - AD5700-1 is clocked using the 3.6864 MHz crystal

Installing the Software
-------------------------

#. Extract the file **CN0270 Eval Software.zip** and open the file
   **setup.exe**.

   .. note::

      It is recommended that you install the CN0270 Evaluation Software to the
      default directory path ``C:\Program Files\Analog Devices\CN0270\`` and all
      National Instruments products to ``C:\Program Files\National Instruments\``.

#. Click **Next** to view the installation review page.

#. Click **Next** to start the installation.

#. Upon completion of the installation of the CN0270 Evaluation Software, the
   installer for the ADuCM360 and Segger J-Link Drivers will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

#. Click **I Agree** to accept the software license agreement and initiate the
   installation.

#. Select only **ADuCM360** and **Segger J-Link Software** on the options
   shown.

   .. important::

      Only these two options are required and included with the installer. To
      download the full ADuCM360 software bundle, please see the Additional
      Info section.

Using the Evaluation Software
------------------------------

Main Window
~~~~~~~~~~~~

This window contains the block diagram of the system and gives access to the
different controls and indicators.

.. figure:: cn0270_main_window.png
   :width: 500px

   CN0270 evaluation software main window

.. list-table::
   :header-rows: 1
   :widths: 10 40

   * - Control
     - Description
   * - Output Current
     - Accepts a numerical value and sets the output current accordingly.
       Entering a value will also update the DAC Code field to the
       corresponding value.
   * - DAC Code
     - Accepts data in HEX format and sets the output current according to the
       code. Entering a value will also update the Output Current field to the
       corresponding value.
   * - Test Current
     - Enables/disables the test current on the output. Test current slews the
       output between zero scale and full scale.
   * - AD5420 Config
     - Opens the AD5420 Configuration window.
   * - HART Modem
     - Opens the HART Modem window.
   * - HART Activity Indicator
     - Indicates when data has been received on the HART interface. The data may
       be viewed in the HART Modem window.
   * - Reset
     - Resets both the system and evaluation software back to default working
       settings.
   * - Status Bar
     - Displays a message to the user detailing the current state of the
       software.

AD5420 Configuration Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This window allows for configuration of the current output section of the
circuit. This window must be closed to resume operation of the software.

.. figure:: cn0270_ad5420_window.png
   :width: 400px

   AD5420 configuration window

.. list-table::
   :header-rows: 1
   :widths: 15 35

   * - Control
     - Description
   * - Output Enabled
     - Triggers the output enabled operation when clicked.
   * - Output Range
     - Drop menu to configure the output range of the AD5420 by selecting the
       desired output.
   * - Digital Slew Rate Control
     - Enable Button: Enables/Disables the Digital Slew Rate Control.
       Step Size: defines by how much the output value changes at each update.
       Update Rate: defines the rate at which the digital slew is updated.
   * - Configure
     - Applies new configurations and closes the configuration window.
   * - Cancel
     - Closes the configuration window without changes.

HART Modem Window
~~~~~~~~~~~~~~~~~~

This window holds the controls and displays for transmitting and reading data
from the HART interface. This window can run in parallel to the main window.

.. figure:: cn0270_ad5700_window.png
   :width: 400px

   HART Modem window

.. list-table::
   :header-rows: 1
   :widths: 15 35

   * - Control
     - Description
   * - Receive Buffer
     - Displays the received HART data. The **HART Page** tab shows the HART
       data divided into the corresponding packets. The **Raw** tab shows all
       HART data bytes received during the last transmission.
   * - Transmit Buffer
     - Transmit data defined by the user. The **HART Page** tab allows
       configuring the HART packet to be transmitted (the software will
       automatically format the HART packet from the values entered). The
       **Raw** tab allows defining data to be sent without formatting.
   * - Copy Data from Rx Buffer
     - Copies data from the receive buffer to the transmit buffer.
   * - Transmit Data
     - Transmits HART data based on the values entered.

Documents
---------

- :adi:`CN0270 Circuit Note <CN0270>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0270-EB1Z Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0270-DesignSupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - PADS project

Additional Information
----------------------

- :adi:`AD5420 Product Page <AD5420>`
- :adi:`AD5700 Product Page <AD5700>`
- :adi:`AD5700-1 Product Page <AD5700-1>`
- :adi:`ADuCM360 Product Page <ADUCM360>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
