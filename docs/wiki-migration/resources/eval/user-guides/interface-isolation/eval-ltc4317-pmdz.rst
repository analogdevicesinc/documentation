EVAL-LTC4317-PMDZ User Guide
============================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/interface-isolation/eval-ltc4317-pmdz/standalone.png
   :align: center
   :width: 600px

GENERAL DESCRIPTION
-------------------

| EVAL-LTC4317-PMDZ features :adi:`LTC4317 <en/products/ltc4317.html>`, a Dual I2C/SMBus Address Translator that enables the hardwired address of one or more I2C or SMBus slave device to be translated to a different address. This evaluation board provides 6-pin PMOD connectors for upstream and downstream connection for compatibility with PMOD form factors such as :adi:`EVAL-ADICUP3029`, an Arduino based Wireless Development Platform for Internet of Things applications based on an ultra-low power ARM Cortex-M3 processor.
| Pmod™ is the Digilent defined standard of Peripheral Modules, small I/O interface boards that offer an ideal way to extend the capabilities of programmable logic and microcontroller boards. They allow sensitive signal conditioning circuits and high-power drive circuits to be placed where they are most effective - near sensors and actuators.
| \* :adi:`LTC4317 <en/products/ltc4317.html>` allows slaves with the same hardwired address to coexist on the same bus. Only discrete resistors are needed

-  :adi:`LTC4317 <en/products/ltc4317.html>` has two output channels for two different sets of slaves.
-  No Software programming is required to configure the :adi:`LTC4317 <en/products/ltc4317.html>` to select the new address and no software programming is required.
-  Up to 127 different address translations are available.
-  Has a Pass-Through Mode Allows General Call Addressing that can be configured using JP2
-  Has ±4kV HBM ESD Ruggedness
-   An ENABLE pin allows bus segments to be enabled and disabled
-  LEDs on the EVAL-LTC4317-PMDZ board such as PWR, RDY1 and RDY2 and various test points on the board allow fault monitoring and easy signal tracing.
-  Has Level Translation for 2.5V, 3.3V and 5V Buses
-  Has Bus Stuck Timeout to automatically recover from abnormal bus conditions like bus stuck low or premature STOP bits
-  Downstream slaves connected to VCC1 and VCC2 can be powered on or off via JP1.

--------------

GENERAL OPERATION
-----------------

|image1| :adi:`LTC4317 <en/products/ltc4317.html>` is an I2C/SMBus address translator. It reads the incoming addresses from the master side and XORs them with the Translation Byte that is set up by configuring resistor dividers on the XORH1, XORL1, XORH2 and XORL2 pins. The two switches, N1 and N2 connect the input bus to the output bus. The :adi:`LTC4317 <en/products/ltc4317.html>` translates the incoming address at the SDAIN pin to a new address at the SDAOUT pin by XORing each incoming bit with the bits from the translation byte; one but at a time by turning the N3 switch on and off. The table below shows an example of how an input address is translated to an output address. In this way, :adi:`LTC4317 <en/products/ltc4317.html>` can allow slaves of the same address to coexist on the same bus. |image2|

--------------

IMPORTANT NOTES
---------------

.. important::

   RLT and RLB are the top and bottom resistors connected to XORL, while RHT and RHB are the top and bottom resistors connected to XORH. On EVAL-LTC4317-PMDZ, RLT1 is a 976k resistor pulled up to VCC, RLB1 is a 102k resistor pulled down to ground, RHT1 is not connected, RHB1 is a 1k resistor pulled down to GROUND, RLT2 is a 976k resistor pulled up to VCC, RLB2 is a 182k resistor pulled down to ground, RHT2 is not connected and RHB2 is a 1k resistor pulled down to GROUND. The Address Translation Byte can be changed by de-soldering these resistors and soldering new resistors with values taken from Table 2 and 3 on the datasheet.


.. important::

   **Pass Through Mode**: If the master wants to communicate with the slave using the general call address, it can temporarily disable address translation by pulling XORH high. This disables address translation and keeps N1 and N2 on regardless of the activity on the buses. Any translation that may be in progress is stopped immediately when XORH goes high.


.. important::

   The address translation byte can be changed during operation by changing the XORH and XORL voltages and toggling the ENABLE pin (high-low-high). This triggers the :adi:`LTC4317 <en/products/ltc4317.html>` to re-read the XORL and XORH voltages. The Enable 1 and Enable 2 pins are connected to VCC via R3 and R4 10k pull-up resistors on EVAL-LTC4317-PMDZ, but they can be de-soldered.


.. important::

   If the ENABLE pin is driven below VENABLE(TH), 1V or if VCC is below the UVLO threshold (1.9V), the :adi:`LTC4317 <en/products/ltc4317.html>` shuts down. The internal shift register storing the address translation byte is cleared, address translation is disabled, the READY pin is pulled low and the quiescent current drops to 350µA.


.. important::

   VCC must be powered from the lower of the two supply voltages from the Upstream and the Downstream buses for level shifting to operate correctly. Refer to Figure 8 on the datasheet.


.. important::

   During the address translation, if SCLIN stays low or high for more than 30ms without any transitions, the :adi:`LTC4317 <en/products/ltc4317.html>` will abort the address translation and reconnect SDAIN to SDAOUT. It will then wait for a START bit to start a new address translation. This prevents any bus stuck low/ high conditions from permanently disconnecting SDAIN from SDAOUT.


--------------

CONNECTORS
----------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/interface-isolation/eval-ltc4317-pmdz/connectors.png
   :align: center

--------------

JUMPERS
-------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/interface-isolation/eval-ltc4317-pmdz/jumpers.png
   :align: center

--------------

LEDS
----

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/interface-isolation/eval-ltc4317-pmdz/leds.png
   :align: center

--------------

TEST POINT LOCATIONS
--------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/interface-isolation/eval-ltc4317-pmdz/testpoints.png
   :align: center

--------------

GETTING STARTED
---------------

EVAL-LTC4317-PMDZ is easy to set up to evaluate the performance of the :adi:`LTC4317`. Refer to Figure 1 for proper measurement equipment setup and follow the procedure below:

-  Power up the upstream side of the board and the :adi:`LTC4317` via the P1.6 pin. Connect P1.5 to GND and P1.4 and P1.3 to SDA and SCL of the host controller respectively. If the host controller is available in a PMOD form factor, plug in the P1 PMOD connector into the six pin PMOD host connector of the controller.
-  Power up the downstream buses 1-2 using separate power supplies or from the upstream side. To power all the buses using the upstream voltage supply, place the jumpers JP1 in A and B positions. This will connect VCCIN to the VCC1-VCC2 of the downstream buses.
-  Configure the resistors, RLTx, RLBx, RHTx and RHBx to set the desired translation byte for the downstream buses, Busx on the :adi:`LTC4317 <en/products/ltc4317.html>`. By default, the translation byte for Bus 1 is hardwired to '0000001' and the translation byte for Bus 2 is hardwired to '0000010' on the EVAL-LTC4317-PMDZ (Refer to Table 1, Table 2 and Table 3 on the datasheet for more information on how to change the Address Translation Byte). The voltages at the XORH and XORL pins configure the translation byte. The XORL voltage configures the lower 4 translation bits (excluding the R/W bit), while the XORH voltage configures the upper 3 translation bits. Tables 2 and 3 on the datasheet show the recommended resistive divider values. RLT and RLB are the top and bottom resistors connected to XORL, while RHT and RHB are the top and bottom resistors connected to XORH.
-  Slaves can be connected to two different buses for two Independent Address Translations (using two different Translation Bytes that can be set using XORH1, XORL1 and XORH2 and XORH2 pins) or connected to one bus, sharing one channel. In this configuration, they will have their input addresses XORed with the same translation Byte using either set of pins (e.g. XORH1, XORL1 or XORH2 or XORL2).
-  If the master wants to communicate with the slave using the general call address, it can temporarily disable address translation by pulling XORH high. This disables address translation and keeps N1 and N2 on regardless of the activity on the buses, turning on the Pass Through Mode (N1 connects SCLIN to SCLOUT while N2 connects SDAIN to SDAOUT). Any translation that may be in progress is stopped immediately when XORH goes high. Place the jumpers JP2 in A and B positions to turn on the Pass Through Mode.

--------------

DEMO WITH ADICUP3029 AND A Digital SENSOR
-----------------------------------------

List of Hardware:
~~~~~~~~~~~~~~~~~

-  :adi:`EVAL-LTC4317-PMDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-LTC4317.html>` board
-  :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>` Evaluation board
-  :adi:`EVAL-ADT7420-PMDZ <en/products/adt7420.html>` Digital Temperature sensor Evaluation board (x2)
-  Mirco USB to USB cable
-  Windows® Vista 32-bit/64-bit, Windows 7 32-bit/64-bit, Windows 8 32-bit/64-bit, or Windows 10 32-bit/64-bit with USB 2.0 port

For this demo, two :adi:`EVAL-ADT7420-PMDZ <en/products/adt7420.html>` temperature sensor boards were connected to the downstream bus 1 and 2 on the :adi:`EVAL-LTC4317-PMDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-LTC4317.html>`.

Configuring the Hardware
~~~~~~~~~~~~~~~~~~~~~~~~

For this demonstration, we will be testing the Pass through mode of the :adi:`LTC4317 <en/products/ltc4317.html>`. This will allow us to communicate with two temperature sensors with the same address.

-  Place the jumper on JP2 in A and B position on EVAL-LTC4317-PMDZ.
-  Next, Place the jumper on JP1 in A position only on EVAL-LTC4317-PMDZ. This will power up Bus 1 on the downstream which will allow the :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>` to communicate with one of the temperature sensors on the downstream without needing Address Translation.
-  Connect the PMOD connector, P1 on EVAL-LTC4317-PMDZ to the P9 connector on the :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>`
-  Connect the P1 connector of one of the :adi:`EVAL-ADT7420-PMDZ <en/products/adt7420.html>` temperature sensor boards to the P5 pmod connector on the EVAL-LTC4317-PMDZ board.
-  Connect the P1 connector of the second :adi:`EVAL-ADT7420-PMDZ <en/products/adt7420.html>` temperature sensor boards to the P7 pmod connector on the EVAL-LTC4317-PMDZ board.
-  Repeat the steps above with place the jumper on JP1 in B position only on EVAL-LTC4317-PMDZ. This will power up Bus 2 on the downstream which will allow the :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>` to communicate with the second temperature sensor board on the downstream without needing Address Translation.
-  The hardware should be set-up as shown below:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/interface-isolation/eval-ltc4317-pmdz/setup1.png
   :align: center

-  *Testing pass through mode with Temperature sensor connected to Bus 1 on the Downstream side. Note that jumper on JP1 is placed in A position.*

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/interface-isolation/eval-ltc4317-pmdz/setup2.png
   :align: center

-  *Testing pass through mode with Temperature sensor connected to Bus 2 on the Downstream side. Note that jumper on JP1 is placed in B position.*

Configuring the EVAL-ADICUP3029 to receive data from EVAL-ADT7420-PMDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two basic ways to program the :adi:`EVAL-ADICUP3029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029.html>` with the software for the :adi:`EVAL-ADT7420-PMDZ <en/products/adt7420.html>`.

-  (Option 1 ) Dragging and Dropping the :git-EVAL-ADICUP360:`Bin B <releases/download/Release-1.0/ADuCM360_demo_adt7420_pmdz.bin>` file to the DAPLINK drive
-  (Option 2 ) Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that Analog Devices creates for testing and evaluation purposes. This is the EASIEST way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters and customize the software to fit your needs, but will be a bit more advanced and will require you to download the CrossCore toolchain.

The software for the **ADuCM360_demo_adt7420** demo can be found here:

Software
~~~~~~~~

.. admonition:: Download
   :class: download

   Bin/Hex files

   
   -  :git-EVAL-ADICUP360:`Bin B <releases/download/Release-1.0/ADuCM360_demo_adt7420_pmdz.bin>`, Binary file to program EVAL-ADICUP3029 to read ADT7420
   -  `Hex B <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc4306_pmdz/hex_b.zip>`_, Hex file to program EVAL-ADICUP3029 to read ADT7420
   
   Complete ADT7420 Source Files
   
   -  :git-EVAL-ADICUP360:`AduCM3029_demo_adt7420 Source Code <projects/ADuCM360_demo_adt7420_pmdz>`
   


.. note::

   For more information on importing, debugging, or other tools related questions, please see the :doc:`tools user guide. </wiki-migration/resources/eval/user-guides/eval-adicup360/tools/cces_user_guide>`


If going with option 2, the user needs to import adt7420_example_noos in their cross core studios workplace. To learn how to do that, visit this page :doc:`cross core studios </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools>`. Once imported, a debug configuration file needs to be set-up . (visit this page :doc:`cross core studios </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools>` for more information)

To see the temperature reading in the console, make sure ADI_APP_USE_BLUETOOTH is set to 0 in the header file (adt7420_app.h) before debugger is launched. Once the debugger is launched, click on the resume button if the program is halted due to breakpoint shown below: |image3| The temperature sensor reading should now be displayed in the console. For detailed information on how to do this, visit the :doc:`ADT7420 PMOD Temperature Demo </wiki-migration/resources/eval/user-guides/eval-adicup360/reference_designs/demo_adt7420>` page on analog wiki


|image4|

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download
   :class: download

   
   :adi:`EVAL-LTC4317-PMDZ Design & Integration Files <LTC4317-designsupport>`
   
   -  `Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/interface-isolation/eval-ltc4317-pmdz/02-056628-01-b.pdf>`_
   -  `Layout <https://wiki.analog.com/_media/resources/eval/user-guides/interface-isolation/eval-ltc4317-pmdz/08_056628b.pdf>`_
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/interface-isolation/eval-ltc4317-pmdz/bom.zip>`_
   


--------------

Additional Information and Useful Links
---------------------------------------

::

   *[[:adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-LTC4317`.html|EVAL-LTC4317-PMDZ]]
   * [[:adi:`LTC4317|LTC4317` Product Page]]
   * [[:adi:`en/analog-dialogue/articles/i2c-communication-protocol-understanding-i2c-primer-pmbus-and-smbus`.html| Understanding PMbus & SMbus]]
   * [[:adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADICUP3029`.html|EVAL-ADICUP3029 Product Page]]
   * [[:adi:`en/products/adt7420`.html| ADT7420 Product Page]]
   * [[/resources/eval/user-guides/eval-adicup3029/tools|Cross Core studio Tool and Driver details]]
   * [[:adi:`media/en/technical-documentation/product-selector-card/4316`.pdf| Address Translator Selector Card]]
   * [[:adi:`en/about-adi/news-room/press-releases/2015/i-c-bus-address-translators-resolve-address-conflicts-with-no-additional-software-coding-or-i-c`.html| Resolving Address Conflicts]]

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/interface-isolation/eval-ltc4317-pmdz/diagram2.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/interface-isolation/eval-ltc4317-pmdz/table1.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc4306_pmdz/targethalted.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc4306_pmdz/readingtemp.gif
