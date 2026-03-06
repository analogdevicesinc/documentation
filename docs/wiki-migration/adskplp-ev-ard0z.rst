ADSKPLP-EV-ARD0Z User Guide
===========================

| 
| The ADSKPLP-EV-ARD0Z evaluation kit intends to make known the precision low-power platform and underline its main features such as low power or versatility. The main board is designed with an Arduino form factor capable to connect 4 different sensors. The core of the PCB is the SAR ADC of 16bit, the AD4696 with a 2.5V feed by external voltage reference, ADR3425. The AD4696 multiplex the inputs of the connected sensor with different sequence configurations and the alternative of the high Z at the input. Adding the external ADR3425 improves the noise performance of the measure. For communicating the ADC with a host a level shifter is needed, due to the voltage difference between them. The LDO selected for the IO reference pin is the minimum voltage required 1.2V, and the part number is ADC165-1.2V, which helps reduce the consumption of the overall signal chain.  All those components incorporate a shutdown capability or low power consumption. The expansion implements a full resistive bridge sensor for differential pressure measurement from Honywell, concretely 26PC01SMT. The conditioning integrated on the PCB for the sensor signal adaptation has an instrumentation amplifier and RC filter. A programmable gain amplifier with part number MAX41400 has controllable gains via digital pins, helping to adapt to different sensor scales and a shutdown pin for standby mode. For its bias pin, an operational amplifier is required to feed it, the MAX40023 is implemented as a buffer with a voltage divider for that functionality. Low noise spectral density and low current consumption are the most relevant features aligned with the precision low power. This conditioning is able to be bypassed through ADG836LYRMZ switches helping the customers to interconnect the expansion with several Mains with different ADCs reducing the creation of several boards for the same purpose.

Block diagram
-------------

Main Board diagram
~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/block_diagram_main_board.png
   :align: center
   :width: 600px

Expansion board diagram
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/block_diagram_expansion_board_02-073355-01-a.png
   :align: center
   :width: 400px

Equipment Needed
----------------

-   ADSKPLP-EV-ARD0Z evaluation board
   \* Main board

   -  Expansion board

-  :adi:`EVAL-SDP-CK1Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>` System Demonstration Platform
   \* Expansion board
-  USB C cable
   \* PC running Windows with USB 2.0 port

Quick Start Guide
-----------------

| To begin using the evaluation board, do the following:
| \* With the SDP-K1 board disconnected from the USB port of the PC, install the ACE software (can be downloaded online). Restart the PC after the software installation is complete. (For complete software installation instructions, see the Evaluation Software section.)

-  Connect the SDP-K1 board to the ADSKPLP-EV-ARD0Z board.

-  Connect the SDP-K1 board to the PC using the supplied USB cable. Choose to automatically search for the drivers for the SDP-K1 board if prompted by the operating system.
   \*
-  From the Programs menu, go to the Analog Devices subfolder, and click ACE to launch the AD4130-8 ACE Plugin (see the Launching the Software section).

::

           *{{:resources:screenshot_2021-04-01_123406.png?400|}}

Related Documents
-----------------

Main Board Documents
~~~~~~~~~~~~~~~~~~~~

::

   *[[:adi:`AD4696|AD4696]]`
   *[[:adi:`ADP165|ADP165]]`
   *[[:adi:`ADR3425|ADR3425]]`
   *[[:adi:`ADG3308|ADG3308]]`
   *[[:adi:`MAX7320|MAX7320]]`
   *[[:adi:`ADG708|ADG708]]`

Expansion Board Documents
~~~~~~~~~~~~~~~~~~~~~~~~~

::

   *[[:adi:`ADG836|ADG836]]`
   *[[:adi:`MAX41400|MAX41400]]`
   *[[:adi:`MAX40023|MAX40023]]`

Hardware Guide
--------------

| Visit the hardware guide chapter `here <:doc:`/wiki-migration/adskplp-ev-ard0z/hardwareguide`>`__
| **Contents of the Hardware guide**:

-  :doc:`Block diagram </wiki-migration/adskplp-ev-ard0z/hardwareguide>`
-  :doc:`2D Board View </wiki-migration/adskplp-ev-ard0z/hardwareguide>`
-  :doc:`On Board Connectors </wiki-migration/adskplp-ev-ard0z/hardwareguide>`
-  :doc:`Power supplies and Voltage reference </wiki-migration/adskplp-ev-ard0z/hardwareguide>`
-  :doc:`Power supplies and Voltage reference </wiki-migration/adskplp-ev-ard0z/hardwareguide>`
-  :doc:`Schematic </wiki-migration/adskplp-ev-ard0z/hardwareguide>`
-  :doc:`Bill of Materials </wiki-migration/adskplp-ev-ard0z/hardwareguide>`

| 

Software guide
--------------

| Visit the software guide chapter `here <:doc:`/wiki-migration/adskplp-ev-ard0z/softwareguide`>`__
| **Contents of the Software guide**:

-  :doc:`Introduction </wiki-migration/adskplp-ev-ard0z/softwareguide>`
-  :doc:`Useful links </wiki-migration/adskplp-ev-ard0z/softwareguide>`
-  :doc:`Hardware Connections </wiki-migration/adskplp-ev-ard0z/softwareguide>`
-  :doc:`Software Downloads </wiki-migration/adskplp-ev-ard0z/softwareguide>`
-  :doc:`Evaluating ADSKPLP01-EV-ARDZ Using IIO Ecosystem </wiki-migration/adskplp-ev-ard0z/softwareguide>`
-  :doc:`Firmware Structure </wiki-migration/adskplp-ev-ard0z/softwareguide>`
-  :doc:`Embedded Development using the EVAL APIs </wiki-migration/adskplp-ev-ard0z/softwareguide>`

| 
