FAQ
===

What is the System Demonstration Platform?
------------------------------------------

| The System Demonstration Platform (SDP) is a hardware and software platform that provides a means to communicate from the PC to ADI products and systems that require digital control and/or read back. It can also form the core of complex demonstration/proof of concept systems or ‘Circuits from the Lab’ developments. The hardware element of the platform consists of a series of controller boards, interposer boards and daughter boards.

-  The controller boards allow a connection to the PC via USB 2.0.
-  Interposer board’s route the signals from the SDP connector to a second connector.
-  Daughter boards are the component specific evaluation boards or CftL reference circuit boards.

The software element of the platform is specific to each of the daughter boards designed for the platform. Each product evaluation board or Circuit from the Lab Reference Circuit is shipped with application software for that product.

What hardware does it use?
--------------------------

Controller Boards
~~~~~~~~~~~~~~~~~

| *SDP-B*
| The SDP-B has a Blackfin (BF527) at its core. The ADZS-BF527 has on chip USB 2.0 capabilities as well as many external interface ports such as SPI, SPORT, I2C, GPIO, Timers, UART and a 16-bit parallel interface exposed through two identical 120 pin connectors. The board also has SDRAM and a serial flash to boot from.

| *SDP-S*
| The SDP-B is a serial only controller board. It has USB 2.0 capabilities and external interfaces such as I2C, GPIO and SPI exposed through its single 120 pin connector.

Interposer Boards
~~~~~~~~~~~~~~~~~

| *SDP Breakout Board*
| The SDP breakout board allows each of the individual signals on the 120 pin connector to be monitored via through hole probe points.

Daughter Boards
~~~~~~~~~~~~~~~

SDP daughter boards are designed to meet the SDP Design guidelines ensuring that the boards can connect of either connector on the SDP-B. An SDP daughter board is generally a component evaluation board or Circuits from the Lab reference circuit board.

3rd Party Boards
~~~~~~~~~~~~~~~~

| *BeMicro-SDP Interposer Board*
| This board allows for SDP compatible daughter boards to be connected to the Arrow BeMicro SDK embedded software development kit. The BeMicro-SDP Interposer boards has a 120 pin connector on one side of the board and a Samtec edge connector receptor at the other side.

How big is it?
--------------

| The SDP-B board is 60mm (2.36”) x 70mm (2.75”). The form factor is such that it has two identical connectors.
| The SDP-S board is 60mm (2.36") x 22mm (0.87"). It has one 120 pin connector.
| The SDP Breakout Board is 120mm (4.72”) x 58mm (2.28”).
| The BeMicro-SDP Interposer Board is 19mm (0.74") x 58mm (2.28").

What about power?
-----------------

-  The SDP-B board requires 200mA at 5V. This must be provided via Pin 1 (VIN) on the connector.

   -  All the I/O on the Blackfin is 3.3v only. It is not 5v tolerant due to the fabrication process on which the Blackfin is manufactured.
   -  A 3.3v supply (limited to 20mA) is made available on the connector to allow you power your I/O voltage without having to generate a specific 3.3v supply for this.
   -  The 5V USB is also directly connected to the USB_VBUS pin on the connector.

-  The SDP-S board is powered over USB, requiring approx 83mA.

   -  It provides 3.3V at 20mA as VIO_3.3
   -  It provides 5V +/- 10% on its USB_VBUS line

What about compatibility between controller boards & daughter boards? Will a daughter board work with either controller board?
------------------------------------------------------------------------------------------------------------------------------

Any daughter board that is designed for the SDP-S is compatible with the SDP-B too. The product page for a particular daughter board will list its compatible controller boards. Relevant user software will be the same.

Due to the wide range of interfaces available on the SDP-B, and not on the SDP-S, the above does not apply in reverse.

How much does it cost?
----------------------

SDP-B
~~~~~

$99 - Pricing/Purchasing information is found on the :adi:`SDP-B product page <en/system-demonstration-platform/controller-boards/evaluation/SDP-B/eb.html#ppa_print_table>`.

SDP-S
~~~~~

$49 - Pricing/Purchasing information is found on the :adi:`SDP-S product page <en/system-demonstration-platform/controller-boards/evaluation/SDP-S/eb.html#ppa_print_table>`.

SDP Breakout Board
~~~~~~~~~~~~~~~~~~

$49.95 - Pricing/Purchasing information is found on the :adi:`SDP Breakout Board product page <en/system-demonstration-platform/interposer-boards/evaluation/SDP-BREAKOUT-BOARD/eb.html#ppa_print_table>`.

BeMicro-SDP Interposer Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pricing/Purchasing information is found on the :adi:`BeMicro-SDP Interposer Board product page <SDP-BEMICRO>`.

Where can I get order the hardware?
-----------------------------------

The SDP platform hardware can be ordered online at :adi:`www.analog.com/sdp <sdp>`.

================== ===============
Board Name         Model Name
================== ===============
SDP-B              EVAL-SDP-CB1Z
SDP-S              EVAL-SDP-CS1Z
SDP Breakout Board ADZS-BRKOUT-EX3
================== ===============

The BeMicro-SDP Interposer can be purchased from Arrow at http://www.arrow.com

How do I get started once I have SDP hardware?
----------------------------------------------

You need an SDP controller board (SDP-B or SDP-S) and a compatible daughter board to get started with the SDP.

-  Install the Software provided with the daughter board (component evaluation board or Circuit from the Lab reference circuit).
-  Connect the daughter board to the SDP controller board (SDP-B or SDP-S) and connect to a USB 2.0 port on your PC.
-  Run the installed software.

I can’t connect to the SDP Controller board (SDP-B or SDP-S), what is wrong?
----------------------------------------------------------------------------

Firstly check the SDP board has appeared in the Device Manager of your PC. (Right click on My Computer >> Manage >> Device Manager). Under the "ADI Development Tools" section you should find "Analog Devices System Demonstration Platform SDP-B" or "Analog Devices System Demonstration Platform SDP-S".

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/devmngr.jpg
   :align: center
   :width: 800px

If the SDP controller is correctly installed on your system, ensure that the correct daughter board is connected off one of the connectors. Run the application software.

How do I get started with the BeMicro-SDP Interposer board?
-----------------------------------------------------------

In order to get started with the BeMicro-SDP Interposer board, go to the `BeMicro page on Intel's website <https://www.intel.com/content/www/us/en/programmable/b/bemicro-sdk.html>`__ From here, the BeMicro USB Stick and the BeMicro-SDP Interposer board can be ordered. You will also find the Arrow Training Lab Material.

Where can I get more information on the BeMicro SDK and the BeMicro-SDP Interposer board?
-----------------------------------------------------------------------------------------

Please visit the `BeMicro page on Intel's website <https://www.intel.com/content/www/us/en/programmable/b/bemicro-sdk.html>`__ for more information on getting started with the BeMicro SDK and SDP compatible daughter boards.
