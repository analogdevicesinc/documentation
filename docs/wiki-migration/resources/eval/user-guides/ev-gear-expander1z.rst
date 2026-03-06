EV-GEAR-EXPANDER1Z
==================

Introduction
------------

EV-GEAR-EXPANDER1Z is a "Gear" (expansion add-on board) for MCU Cogs (EV-COG-AD3029LZ & EV-COG-AD4050LZ). This gear is designed for quick prototyping and bread boarding.

-  The board provides easy access to all the MCU GPIO signals by bringing the signals on a header array.
-  It enables

   -  PMOD modules interface Via SPI and I2C

      -  Quick SensorStrobe application prototyping through a dedicated connector
      -  SD Card interface for data logging.
      -  Additional Gears connectivity
      -  "Arduino uno" compatible shields

| This user guide describes the connectors details and jumper settings.
| ======Hardware details======

Board image
-----------

Primary-side
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/picture7_1.png
   :align: center
   :width: 600px

Secondary-side
~~~~~~~~~~~~~~

|image1| The board consists of

-  COG connectors (C1, C2)
-  Gear connectors (D1, D2)
-  Arduino Uno headers (A1, A2, A3, A4, A5)
-  PMOD interfaces (P3, P4, P5)
-  Debug headers (P6, P7, P8)
-  Jumpers and test points

Power option
------------

| The EV-GEAR-EXPANDER1Z board is powered by means of VDD supply from MCU cog through connector C1. The VDD supply is shared between various connectors for PMOD interfaces, SD card reader, Arduino shields and gears.
| Alternately MCU cog can be powered from EV-GEAR-EXPANDER1Z.

-  Power supply header P1 can be used to supply 5V
-  Pin 10 of header P8 can be used to supply 3V

COG connectors
--------------

The COG connectors C1 and C2 interface the EV-GEAR-EXPANDER1Z board with MCU Cog. The connector carries all the GPIO signals from the MCU Cog board. The pinout details are given in the :doc:`expander connector section in EV-COG-AD3029LZ wiki </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz/cog_hw_userguide>`.

.. warning::

   **If any application is not working on MCU COG connected to a EV-GEAR-EXPANDER1Z board, check for the connectivity from MCU COG to EV-GEAR-EXPANDER1Z. If it is found that there is no connectivity, one of the possible reasons could be, accumulation of dust on the Expander connectors C1 and C2. To resolve this, clean the connectors with isopropyl alcohol or any solvent.

   
   Improper connector mating can also result in the loss of connectivity between MCU COG and EV-GEAR-EXPANDER1Z, make sure that shunts installed on COG are not obstructing the connector mating. \**


Gear connectors
---------------

The connectors D1 and D2 can be used to connect a Gear. Gear is an addon application board which can be a custom build to serve the required application.

.. important::

   The gear must have the connector (`DF17(4.0)-60DP-0.5V(57) <https://www.digikey.com/DF17(4.0)-60DP-0.5V(57)>`__) to interface with D1 and D2 connectors.


The pinout details for D1 and D2 are same as that of COG connectors ( C1, C2 :doc:`expander connector section in EV-COG-AD3029LZ wiki </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz/cog_hw_userguide>`).

Arduino Uno headers
-------------------

The headers A1, A2, A3, A4 and A5 support the shields that are Arduino Uno compatible. The following table captures the signals connected to the headers

============== =================== ========== =================
Connector name Connector reference Pin_number Signal_name
============== =================== ========== =================
Arduino        A1                  1          SPI0_MISO
:::            :::                 2          FT_EXT_VDD_OUT
:::            :::                 3          SPI0_CLK
:::            :::                 4          SPI0_MOSI
:::            :::                 5          TT_EXT_RESET_IN
:::            :::                 6          GND
:::            A2                  1          ADC0
:::            :::                 2          EXT_ADC1
:::            :::                 3          EXT_ADC2
:::            :::                 4          ADC3
:::            :::                 5          SPI2_CS3
:::            :::                 6          EXT_GPIO42
:::            A3                  1          NC
:::            :::                 2          FT_EXT_VDD_OUT
:::            :::                 3          TT_EXT_RESET_IN
:::            :::                 4          FT_EXT_VDD_OUT
:::            :::                 5          FT_EXT_SUPPLY_OUT
:::            :::                 6          GND
:::            :::                 7          GND
:::            :::                 8          N.C
:::            A4                  1          P8_12
:::            :::                 2          GPIO27
:::            :::                 3          P33_43
:::            :::                 4          EXT_SPI2_CS1
:::            :::                 5          EXT_INT_WAKE2
:::            :::                 6          INT_WAKE0
:::            :::                 7          EXT_UART0_RXD
:::            :::                 8          EXT_UART0_TXD
:::            A5                  1          I2C0_SCL
:::            :::                 2          I2C0_SDA
:::            :::                 3          VREF_ADC
:::            :::                 4          GND
:::            :::                 5          SPI0_CLK
:::            :::                 6          SPI0_MISO
:::            :::                 7          SPI0_MOSI
:::            :::                 8          SPI0_CS2
:::            :::                 9          EXT_GPIO30
:::            :::                 10         GPIO28
============== =================== ========== =================

PMOD interfaces
---------------

The EV-GEAR-EXPANDER1Z board offers connectors with PMOD SPI, PMOD I2C and PMOD IO/SensorStrobe interfaces. Any PMOD peripheral module with PMOD SPI or PMOD I2C interface can be directly plugged into these connectors. The host MCU communicates to the modules by means of SPI or I2C. The Sensorstrobe connector is a custom connector which provides access to ADuCM3029/ADuCM4050 SensorStrobe signals and few other GPIOs. The pinout details of the PMOD connectors are given below.

====================== =================== ========== ==============
Connector name         Connector reference Pin_number Signal_name
====================== =================== ========== ==============
SensorStrobe connector P3                  1          SS_IO_01
:::                    :::                 2          SS_IO_02
:::                    :::                 3          SS_IO_03
:::                    :::                 4          SS_IO_04
:::                    :::                 5          GND
:::                    :::                 6          FT_EXT_VDD_OUT
PMOD SPI               P4                  1          SPI1_CS0
:::                    :::                 2          SPI1_MOSI
:::                    :::                 3          SPI1_MISO
:::                    :::                 4          SPI1_CLK
:::                    :::                 5          GND
:::                    :::                 6          FT_EXT_VDD_OUT
:::                    :::                 7          INT_WAKE0
:::                    :::                 8          PMOD_8
:::                    :::                 9          GPIO14
:::                    :::                 10         ADXL_ANALOG
:::                    :::                 11         GND
:::                    :::                 12         FT_EXT_VDD_OUT
PMOD I2C               P5                  1          I2C0_SCL
:::                    :::                 2          I2C0_SCL
:::                    :::                 3          I2C0_SDA
:::                    :::                 4          I2C0_SDA
:::                    :::                 5          GND
:::                    :::                 6          GND
:::                    :::                 7          FT_EXT_VDD_OUT
:::                    :::                 8          FT_EXT_VDD_OUT
====================== =================== ========== ==============

Debug headers
-------------

The Debug headers P6, P7 and P8 can be used to probe certain MCU GPIOs. The headers consist of male and female pins. The following table captures the pinout.

============== =================== ========== =============
Connector name Connector reference Pin_number Signal_name
============== =================== ========== =============
Debug header 1 P6                  1          SPI2_RDY
:::            :::                 2          SPI2_CLK
:::            :::                 3          SPI2_MOSI
:::            :::                 4          SPI2_MISO
:::            :::                 5          SPI2_CS0
:::            :::                 6          EXT_INT_WAKE1
:::            :::                 7          GPIO14
:::            :::                 8          EXT_GPIO34
:::            :::                 9          GPIO29
:::            :::                 10         GPIO41
Debug header 2 P7                  1          ADF_GPIO0
:::            :::                 2          ADF_GPIO1
:::            :::                 3          ADF_GPIO2
:::            :::                 4          RF_RTC_OPC1
Debug header 3 P8                  1          EXT_SPI1_CS3
:::            :::                 2          SPI1_CS0
:::            :::                 3          SPI1_MISO
:::            :::                 4          SPI1_MOSI
:::            :::                 5          SPI1_CLK
:::            :::                 6          EXT_RTC1_SS1
:::            :::                 7          GPIO12
:::            :::                 8          GPIO32
:::            :::                 9          GPIO31
:::            :::                 10         TT_EXT_VDD_IN
============== =================== ========== =============

Design Files
------------

.. admonition:: Download
   :class: download

   
   EV-GEAR-EXPANDER1Z Rev B Design and Integration Files
   
   -  `Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/02-046895-01-b-1_.pdf>`__ (PDF)
   -  `Bill of materials <https://wiki.analog.com/_media/resources/eval/user-guides/05-046895-01-b.zip>`__ (zip)
   -  `Fabrication Files <https://wiki.analog.com/_media/resources/eval/user-guides/09-046895-01b.zip>`__ (Zip)
   -  `Assembly Files <https://wiki.analog.com/_media/resources/eval/user-guides/01-046895-01b.zip>`__ (Zip)
   


| 
| End Document
| :doc:`Back </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/picture8.png
   :width: 600px
