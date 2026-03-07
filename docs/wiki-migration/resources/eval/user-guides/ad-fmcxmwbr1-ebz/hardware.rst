AD-FMCXMWBR1-EBZ Hardware
=========================

The :adi:`AD-FMCXMWBR1-EBZ` is a board that provides connectivity between\ `X-MWblocks <https://www.xmicrowave.com/product-category/x-mwblocks/>`_ and research and development tools. At the moment there is no common control path between the X-MW controller and an FPGA that can be used in controlling the hardware which makes it difficult to merge and do reproduceable tests on both kind of platforms. X-Microwave modules provide solutions for prototyping RF and microwave circuits faster, easier and at a lower cost. They offer a broad selection of ADI parts as drop-in X-MW blocks in different configurations and optimized for different frequencies. Using this system will be possible to create RF and Microwave designs that incorporate X-MW building blocks and are controlled either with the X-MW controller or with a FPGA device.

--------------

Kit Contents
------------

+----------------------+---------------------------------------------------------------------+
| AD-FMCXMWBR1-EBZ Kit |                                                                     |
+======================+=====================================================================+
| AD-FMCBRIDGE1A       | FMC Card with level translators and power supplies; BR-066232 RevB  |
+----------------------+---------------------------------------------------------------------+
| AD-FMCBRIDGE1B       | Prototyping board with access to all signals of interest; BR-066233 |
+----------------------+---------------------------------------------------------------------+
| Ribbon cable         | For signal rails                                                    |
+----------------------+---------------------------------------------------------------------+
| Custom cable         | For power rails                                                     |
+----------------------+---------------------------------------------------------------------+

The FMC Xmicrowave bridge Kit contains both the FMC Xmicrowave Bridge Board and the FMC Xmicrowave Protoplate Board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/ad-fmcxmwbr1-ebz_kit_set.jpg
   :align: center
   :width: 800px

.. container:: centeralign

   Figure. Contents of the AD-FMCXMWBR1-EBZ kit


The boards are connected using a ribbon cable for the signal rails and another cable for the power rails.

--------------

Specifications
--------------

|image1|

.. container:: centeralign

   Figure 2. Block Diagram of the FMC Xmicrowave bridge


+-------------------------+--------------------------------------------------------------------------------------------------+
| Key Features            |                                                                                                  |
+=========================+==================================================================================================+
| **User interfaces**     | FMC standard connector for connection to FMC development kit (from Xilinx or Intel)​             |
+-------------------------+--------------------------------------------------------------------------------------------------+
|                         | RaspberryPi 40pin header for connection to X-MW controller                                       |
+-------------------------+--------------------------------------------------------------------------------------------------+
| **Voltage translation** | Control of modules with different voltage requirements while allowing compatibility between ICs​ |
+-------------------------+--------------------------------------------------------------------------------------------------+
| **Power Supplies**      | Access to power supplies available in the FMC​                                                   |
+-------------------------+--------------------------------------------------------------------------------------------------+
|                         | Create new power rails suitable to power LDOs and create bias voltages in the prototyping area​  |
+-------------------------+--------------------------------------------------------------------------------------------------+
| **Connectivity**        | Provide a bridge between X-MW protoplate and an FMC development kit​                             |
+-------------------------+--------------------------------------------------------------------------------------------------+

Connectivity and User interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  FMC standard connector (FMC+ compatible)
-  Raspberry Pi standard 40 pin connector
-  Connector headers for the cables that connect the adapter PCB and the interface PCB

Because it is intended to be compatible with various development boards, the FMC bridge cannot be built as a single board. The proposed solution is inspired from the design of the X-MW protoplate. An interface PCB, attached to the prototyping plate, will be connected to an FMC card with some ribbon cables for power and signals. There are two controlling modes for the AD-FMCXMWBR1-EBZ: with an FMC compatible device or an Raspberry Pi compatible device(such as the X-MW controller). The FMC bridge will direct from the development board to the protoplate two SPI buses, two I2C buses and 8 GPIO pins.

In the image below are presented the signals on the FMC connector used in this design ( with italic fonts).


|image2|

.. container:: centeralign

   Figure . Pinout of the FMC connector P1


In the X-MW controller mode the protoplate has access to one SPI bus, one I2C bus and many GPIO pins. Connector P10 is compatible with the X-Microwave controller or a RaspberryPi. It can be connected with a ribbon cable and has the pinout as presented in Figure. In the same figure you can see the correspondence between the input pins of the FMC Bridge and the original X-MW protoplate interface board.



|image3|

.. container:: centeralign

   Figure 2. Pinout of the Rpi connector P10


To connect wires on the protoplate you can solder them directly on the holes or use any male pin header with at least 0.230" (5.84mm) mating contact length and 0.320" (8.13mm) post contact length and 0.100" (2.54mm) pitch.

Power
~~~~~

Input Power
^^^^^^^^^^^

By default the AD-FMCXMWBR1-EBZ is supplied by the 12P0V pin the FMC connector. By the FMC standard this pin provides power from the carrier to the mezzanine card with maximum 1 A and maximum 1000 uF capacitive load. Because in max load all the circuits on the board need more than 1A there is an alternative supply method. For applications that require higher load currents, AD-FMCXMWBR1-EBZ can be supplied external from a power supply with the following specifications:

-  Input:100-2040V, 50-60 Hz
-  Output: 12V 5.0A (minimum)
-  Rectangular 6 position output connector compatible with `Molex 0039301060 connector <https://www.digikey.com/en/products/detail/molex/0039301060/561080>`_

|image4|

.. container:: centeralign

   Figure. Pinout of the input power connector P2


The power path selection is achieved using the :adi:`LTC4418` dual channel prioritized powerpath controller. It connects one of the two power supplies to a common output, based on priority and validity. The higher priority supply defined in this case is the external supply.



|image5|

.. container:: centeralign

   Figure. Power path selection on AD-FMCXMWBR1EBZ


The channels of LTC4418 have overvoltage and undervoltage thresholds defined, so the supply is considered valid when the voltage is within the OV UV window for at leas the configured validation time. If the external supply and the FMC 12V supplies are valid, leds DS1 and DS2 will be on, accordingly. The validity thresholds of the input supplies are listed in the table below:

=========================== =================== ============
Input power supply validity                     
=========================== =================== ============
\                           **External supply** **FMC 12V0**
**Channel**                 1 (**prioritized**) 2
**UV threshold**            10 V                10 V
**OV threshold**            13 V                13 V
**Hysteresis**              250mV               250mV
**Inrush limit**            4 A                 4 A
**Validation delay**        16 ms               16 ms
**Vout droop max**          2 V                 2 V
=========================== =================== ============

.. important::

   If connected, the external supply will be prioritized. Both supplies can be connected and valid at the same time.


Output power
^^^^^^^^^^^^

The AD-FMCXMWBR1-EBZ gives user access to the power supply pins of the FMC connector and creates new power supply rails as follows:

-  Direct from FMC:

   -  +12V (1A),

      -  +3.3V (3A),
      -  +VADJ 0-3.3V (4A)

-  New power rails (supplied with an external source):

   -   +6V (1A)

      -  +4V(1A)
      -  18V (50mA)
      -  +3V3 (1A),
      -  2x (1.2 -12V) Pot adjustable
      -  1x ( -6V- 0V) Pot adjustable

      |image6|

.. container:: centeralign

   Figure. Pinout of P11-output power connector


The user will have access on the FMC bridge to the power rails coming directly from the FPGA through the FMC connector. These supplies can be used, along with the power rails created on the FMC bridge(P11). The supply chain should provide some common voltage values suitable for the X-MW modules. Many of these modules have already integrated LDOs at the input so the voltage rails should provide enough headroom for the voltage so it does not drop under the desired value. If there are needed variable bias voltages in the prototype circuit, the FMC bridge will provide three potentiometer adjustable power supplies with a wide range of values.



|image7|

.. container:: centeralign

   Figure. Power map of AD-FMCXMWBR1-EBZ for maximum load on all supplies


Digital communication
~~~~~~~~~~~~~~~~~~~~~

The X-MW blocks communicate with the controller through digital communication protocols. The paths for communication include:

-  2x SPI rails with CLS, CIPO, COPI and CS0-7 signals
-  2x I2C rails with SDA, SCL signals
-  GPIO0-7

All the above signals can be accessed on the P9 pin header. Using a ribbon cable, the signals are connected to the Protoplate interface board, where all the corresponding pads are labelled.


|image8|

.. container:: centeralign

   Figure. Pinout of the P9 output pin header


Level translation
~~~~~~~~~~~~~~~~~

To be able to use different FPGAs with modules that have different voltage requirements there is necessary to use some level translation IC's. The voltage level translation between the driver device and the receiver devices must be bidirectional and compatible with the common voltage levels of the FPGAs (1.8V, 3.3V). If the two levels do not suit the needs of the user, the 1.8V corresponding pins can be disconnected from the LDO output that generates it ( by desoldering R133) and use P12 as input for the new voltage rail. Each communication protocol can be independently level translated, and the feature is implemented as it follows:

+-----------------+---------------------+-----------------------------------+----------------+
|                 | Level translator IC |                                   | Supply voltage |
+-----------------+---------------------+-----------------------------------+----------------+
| SPI (CLK, COPI) | 74AVC4T774GUX       | 4 inputs, with direction pin each | 0.8V - 3.6V    |
+-----------------+---------------------+-----------------------------------+----------------+
| SPI (CIPO)      | 74LVC1T45GS         | 1 input, 1 direction pin          | 1.2V -3.6V     |
+-----------------+---------------------+-----------------------------------+----------------+
| SPI (CS)        | 74AVCH8T245PW       | 8 inputs, common direction pin    | 0.8V - 3.6V    |
+-----------------+---------------------+-----------------------------------+----------------+
| I2C             | NTS0302JKZ          | 2 inputs                          | 0.95V -3.6V    |
+-----------------+---------------------+-----------------------------------+----------------+
| GPIO            | 74AVC4T774GUX       | 4 inputs, with direction pin each | 0.8V - 3.6V    |
+-----------------+---------------------+-----------------------------------+----------------+

GPIO direction pins are programmable from the FPGA. They are set by default to be 6 output pins and 2 input pins, but the user has the option to configure them as needed either through software or by desoldering the pull-up resistor(VADJ) and soldering it into pulldown (GND) position (footprint is available on the PCB).

Compatibility and Reconfigurability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The FMC bridge is mainly intended to be used with an FMC compatible development board which will be able to control the modules as well as the level translation ICs. Because these developments boards have a higher processing capability we are able to provide paths for two sets of each communication protocol (SPI, I2C) to the protoplate. The direction of the level shifters is also controlled by the FPGA by default. The system was designed in such a way that one SPI bus, one I2C bus and 8GPIO pins can be used in both control modes (not simultaneusly).

--------------

Schematics and CAD files
------------------------

.. admonition:: Download
   :class: download

   
   ::
   
      *[[https://wiki.analog.com/_media/resources/eval/user-guides/02_066232b_top.pdf|AD-FMCBRIDGE1A BR-066232 Rev B Schematics]]
   


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/block_diagram.png
   :width: 900px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/fmc_pinout.png
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/rpi_conn_pinout.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/p2_pinout.png
   :width: 200px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/input_power_priority.png
   :width: 700px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/p11_pinout.png
   :width: 200px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/power_map_revb.png
   :width: 800px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/p9_pinout.png
   :width: 300px
