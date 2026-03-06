ADSKPLP-EV-ARD0Z Hardware Guide
===============================

Block diagram
-------------

Main board
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/block_diagram_main_board.png
   :align: center
   :width: 600px

Expansion board
~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/block_diagram_expansion_board_02-073355-01-a.png
   :align: center
   :width: 400px

2D Board View
-------------

For the PCB designs, the distribution adopted treats to easily understand and visualize which components are essential for the functionality and which are the components placed to simplify the start-up. On one side, for the main board, on the top layer, the essential components are placed, ADC, LDO and voltage reference. Meanwhile, on the bottom layer, we could find the demultiplexer, GPIO expander, EEPROM and level shifter. On the other side, the expasion board has the PGA, buffer and sensor on the top layer, nevertheless the switches and the GPIO are on the bottom layer.

Top and Bottom Main Board View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   *{{:2d_top_view_02_072492_01.png?400|}}{{:2d_bot_view_02_072492_01.png?378|}}

Top and Bottom Expansion Board View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   *{{:adskplp-ev-ard0z:2d_top_view_08-073355-01-a.png?400|}}{{:adskplp-ev-ard0z:2d_bottom_view_08-073355-01-a.png?400|}}

On Board Connectors
-------------------

Analog Connector
~~~~~~~~~~~~~~~~

The main board provides access to 4 different expansion boards via 4 analog connectors. These connectors have 4 pins each:

-  Input 1
-  Input 2
-  GND

The connector allows several input configurations: single-ended, pseudo-differential. For the input configuration follow the SW user guide, XXXXXXX

.. _main-board-1:

Main Board
^^^^^^^^^^

.. container:: centeralign


|image1|

   .. container:: centeralign

      \ **Figure XX Analog connector picture**\

   


**Table 1. Analog connector pinout table**

+-------------+----------------------------------------+-------------+-----------+------------+--------------------------+
| Signal name | Signal description                     | Signal type | Connector | Pin number | Direction Eco Board view |
+=============+========================================+=============+===========+============+==========================+
| ADC_IN1     | Analog input signal from the expansion | Analog      | P6        | 1          | Input                    |
+-------------+----------------------------------------+-------------+-----------+------------+--------------------------+
| ADC_IN0     | Analog input signal from the expansion | Analog      | P6        | 2          | Input                    |
+-------------+----------------------------------------+-------------+-----------+------------+--------------------------+
| AGND        | Ground                                 | Power       | P6        | 3          | Input                    |
+-------------+----------------------------------------+-------------+-----------+------------+--------------------------+
| ADC_IN3     | Analog input signal from the expansion | Analog      | P7        | 1          | Input                    |
+-------------+----------------------------------------+-------------+-----------+------------+--------------------------+
| ADC_IN2     | Analog input signal from the expansion | Analog      | P7        | 2          | Input                    |
+-------------+----------------------------------------+-------------+-----------+------------+--------------------------+
| AGND        | Ground                                 | Power       | P7        | 3          | Input                    |
+-------------+----------------------------------------+-------------+-----------+------------+--------------------------+
| ADC_IN5     | Analog input signal from the expansion | Analog      | P8        | 1          | Input                    |
+-------------+----------------------------------------+-------------+-----------+------------+--------------------------+
| ADC_IN4     | Analog input signal from the expansion | Analog      | P8        | 2          | Input                    |
+-------------+----------------------------------------+-------------+-----------+------------+--------------------------+
| AGND        | Ground                                 | Power       | P8        | 3          | Input                    |
+-------------+----------------------------------------+-------------+-----------+------------+--------------------------+
| ADC_IN7     | Analog input signal from the expansion | Analog      | P9        | 1          | Input                    |
+-------------+----------------------------------------+-------------+-----------+------------+--------------------------+
| ADC_IN6     | Analog input signal from the expansion | Analog      | P9        | 2          | Input                    |
+-------------+----------------------------------------+-------------+-----------+------------+--------------------------+
| AGND        | Ground                                 | Power       | P9        | 3          | Input                    |
+-------------+----------------------------------------+-------------+-----------+------------+--------------------------+

.. container:: centeralign


|image2|

   .. container:: centeralign

      \ **Figure XX Analog connector schematic picture**\

   


.. _expansion-board-1:

Expansion Board
^^^^^^^^^^^^^^^

Digital and Power Connector
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The digital and power connector has two main functionalities, the first of them is the supply of the expansion board and the second is the control through different communications. The main board only can connect directly with one board, but if we need to communicate with more than one board the second connector of the expansion shall be connected like a bridge sharing the communication.  

.. _main-board-2:

Main Board
^^^^^^^^^^

.. container:: centeralign


|image3|

   .. container:: centeralign

      \ **Figure XX Digital and Power Main board connector picture**\

   


**Table 2. Digital and Power connector pinout table Main board**

+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| Signal name | Signal description                   | Signal type | Connector | Pin number | Special functionality | Direction Eco Board view |
+=============+======================================+=============+===========+============+=======================+==========================+
| MUX_CS_0    | Chip select 0 from the demultiplexer | Digital     | P10       | 1          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| MUX_CS_1    | Chip select 1 from the demultiplexer | Digital     | P10       | 2          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| MUX_CS_2    | Chip select 2 from the demultiplexer | Digital     | P10       | 3          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| MUX_CS_3    | Chip select 3 from the demultiplexer | Digital     | P10       | 4          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SCK     | SPI clock                            | Digital     | P10       | 5          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SDO     | SPI data output                      | Digital     | P10       | 6          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SDI     | SPI data input                       | Digital     | P10       | 7          | SPI                   | Input                    |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| GND         | Ground                               | Power       | P10       | 8          | Power ground          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SCL     | I2C clock                            | Digital     | P10       | 9          | I2C                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SDA     | I2C data                             | Digital     | P10       | 10         | I2C                   | Input/Output             |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| GND         | Ground                               | Power       | P10       | 11         | Power ground          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_CNV     | PWM for ADC conversion signal        | Digital     | P10       | 12         | PWM                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| GND         | Ground                               | Power       | P10       | 13         | Power ground          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_3.3V    | 3.3V voltage supply                  | Power       | P10       | 14         | Power supply          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| GND         | Ground                               | Power       | P10       | 15         | Power ground          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| REF_2.5     | 2.5V voltage reference               | Power       | P10       | 16         | Voltage reference     | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+

.. container:: centeralign


|image4|

   .. container:: centeralign

      \ **Figure XX Digital and Power connector schematic picture**\

   


.. _expansion-board-2:

Expansion Board
^^^^^^^^^^^^^^^

.. container:: centeralign


|image5|

   .. container:: centeralign

      \ **Figure XX Digital and Power Expansion connector picture**\

   


**Table XX. Digital and Power connector one pinout table Expansion board**

+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| Signal name | Signal description                   | Signal type | Connector | Pin number | Special functionality | Direction Eco Board view |
+=============+======================================+=============+===========+============+=======================+==========================+
| MUX_CS_0    | Chip select 0 from the demultiplexer | Digital     | P2        | 1          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| MUX_CS_1    | Chip select 1 from the demultiplexer | Digital     | P2        | 2          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| MUX_CS_2    | Chip select 2 from the demultiplexer | Digital     | P2        | 3          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| MUX_CS_3    | Chip select 3 from the demultiplexer | Digital     | P2        | 4          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SCK     | SPI clock                            | Digital     | P2        | 5          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SDO     | SPI data output                      | Digital     | P2        | 6          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SDI     | SPI data input                       | Digital     | P2        | 7          | SPI                   | Input                    |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| GND         | Ground                               | Power       | P2        | 8          | Power ground          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SCL     | I2C clock                            | Digital     | P2        | 9          | I2C                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SDA     | I2C data                             | Digital     | P2        | 10         | I2C                   | Input/Output             |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| GND         | Ground                               | Power       | P2        | 11         | Power ground          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_CNV     | PWM for ADC conversion signal        | Digital     | P2        | 12         | PWM                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| GND         | Ground                               | Power       | P2        | 13         | Power ground          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_3.3V    | 3.3V voltage supply                  | Power       | P2        | 14         | Power supply          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| GND         | Ground                               | Power       | P2        | 15         | Power ground          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| REF_2.5     | 2.5V voltage reference               | Power       | P2        | 16         | Voltage reference     | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+

**Table XX. Digital and Power connector two pinout table Expansion board**

+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| Signal name | Signal description                   | Signal type | Connector | Pin number | Special functionality | Direction Eco Board view |
+=============+======================================+=============+===========+============+=======================+==========================+
| MUX_CS_1    | Chip select 1 from the demultiplexer | Digital     | P3        | 2          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| MUX_CS_2    | Chip select 2 from the demultiplexer | Digital     | P3        | 3          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| MUX_CS_3    | Chip select 3 from the demultiplexer | Digital     | P3        | 4          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| MUX_CS_0    | Chip select 0 from the demultiplexer | Digital     | P3        | 1          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SCK     | SPI clock                            | Digital     | P3        | 5          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SDO     | SPI data output                      | Digital     | P3        | 6          | SPI                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SDI     | SPI data input                       | Digital     | P3        | 7          | SPI                   | Input                    |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| GND         | Ground                               | Power       | P3        | 8          | Power ground          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SCL     | I2C clock                            | Digital     | P3        | 9          | I2C                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_SDA     | I2C data                             | Digital     | P3        | 10         | I2C                   | Input/Output             |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| GND         | Ground                               | Power       | P3        | 11         | Power ground          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_CNV     | PWM for ADC conversion signal        | Digital     | P3        | 12         | PWM                   | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| GND         | Ground                               | Power       | P3        | 13         | Power ground          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| ARD_3.3V    | 3.3V voltage supply                  | Power       | P3        | 14         | Power supply          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| GND         | Ground                               | Power       | P3        | 15         | Power ground          | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+
| REF_2.5     | 2.5V voltage reference               | Power       | P3        | 16         | Voltage reference     | Output                   |
+-------------+--------------------------------------+-------------+-----------+------------+-----------------------+--------------------------+

.. container:: centeralign


|image6|

   .. container:: centeralign

      \ **Figure XX Digital and Power connector schematic picture**\

   


Arduino Connector
~~~~~~~~~~~~~~~~~

These connectors facilitate the communication and control of the ECO board whose form factor selected is the Arduino one. The Arduino form factor helps to an easy and fast interface to start up with the interaction considering that there is a wide portfolio of controllers with that connector distribution. Moreover, the signals through the connectors have been simplified using only the power supply, the SPI and I2C communications, and just two digital signals (one for the conversion and the other for the ADC interrupt). The idea of sharing as less connections as possible is to be able to stack up different boards to be controlled.

.. container:: centeralign


|image7|

   .. container:: centeralign

      \ **Figure XX Arduino connector picture**\

   


**Table 3. Arduino connector pinout table**

+-------------+-------------------------------------------+-------------+---------------------+------------------+------------------------------+
| Signal name | Signal description                        | Signal type | Arduino Pin/Port    | Special function | Direction Arduino board view |
+=============+===========================================+=============+=====================+==================+==============================+
| ARD_3.3V    | 3.3V voltage supply                       | Power       | CON = P2 PIN = 4    | Voltage supply   | Output                       |
+-------------+-------------------------------------------+-------------+---------------------+------------------+------------------------------+
| GND         | Ground supply                             | Power       | CON = P2 PIN = 6, 7 | Voltage supply   | Output                       |
+-------------+-------------------------------------------+-------------+---------------------+------------------+------------------------------+
| ARD_SCL     | I2C clock                                 | Digital     | CON = P4 PIN =      | I2C              | Output                       |
+-------------+-------------------------------------------+-------------+---------------------+------------------+------------------------------+
| ARD_SDA     | I2C data                                  | Digital     | CON = P2 PIN = 4    | I2C              | Input/Output                 |
+-------------+-------------------------------------------+-------------+---------------------+------------------+------------------------------+
| ARD_SCK     | SPI                                       | Digital     | CON = P4 PIN =      | SPI              | Output                       |
+-------------+-------------------------------------------+-------------+---------------------+------------------+------------------------------+
| ARD_SDO     | SPI                                       | Digital     | CON = P4 PIN =      | SPI              | Output                       |
+-------------+-------------------------------------------+-------------+---------------------+------------------+------------------------------+
| ARD_SDI     | SPI                                       | Digital     | CON = P4 PIN =      | SPI              | Input                        |
+-------------+-------------------------------------------+-------------+---------------------+------------------+------------------------------+
| ARD_CS      | SPI                                       | Digital     | CON = P4 PIN =      | SPI              | Output                       |
+-------------+-------------------------------------------+-------------+---------------------+------------------+------------------------------+
| ARD_CNV     | PWM for ADC conversion signal             | Digital     | CON = P4 PIN =      | PWM              | Output                       |
+-------------+-------------------------------------------+-------------+---------------------+------------------+------------------------------+
| ARD_CNV     | PWM for ADC conversion signal (redundant) | Digital     | CON = P4 PIN =      | PWM              | Output                       |
+-------------+-------------------------------------------+-------------+---------------------+------------------+------------------------------+

.. container:: centeralign


|image8|

   .. container:: centeralign

      \ **Figure XX Arduino connector schematic picture**\

   


Power supplies and Voltage reference
------------------------------------

The evaluation board receives power through the controller board when connected to the PC via USB, then the regulators generate the required power supply levels from 3.3V

1.2V Power supply
~~~~~~~~~~~~~~~~~

The 1.2 voltage supply is used to feed the Level shifter which part number is ADG3308BCPZ and the digital part of the AD4696. The part number implemented for the functionality is ADP165ACPZ-1.2

.. container:: centeralign


|image9|

   .. container:: centeralign

      \ **Figure XX 1.2V supply board picture**\

   


2.5V Voltage Reference
~~~~~~~~~~~~~~~~~~~~~~

The 2.5 voltage is the voltage reference for the ADC (AD4696), this voltage is shared via digital connector. The part number implemented for the functionality is ADR3425ARJZ

.. container:: centeralign


|image10|

   .. container:: centeralign

      \ **Figure XX 2.5V reference board picture**\

   


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

Schematic
---------

.. _main-board-3:

Main board
~~~~~~~~~~

`02-072492-01-a.pdf <https://wiki.analog.com/_media/adskplp-ev-ard0z/02-072492-01-a.pdf>`__

.. _expansion-board-3:

Expansion board
~~~~~~~~~~~~~~~

`02-073355-01-a.pdf <https://wiki.analog.com/_media/adskplp-ev-ard0z/02-073355-01-a.pdf>`__

Bill of Materials
-----------------

.. _main-board-4:

Main board
~~~~~~~~~~

`05-072492-01-a.pdf <https://wiki.analog.com/_media/adskplp-ev-ard0z/05-072492-01-a.pdf>`__

.. _expansion-board-4:

Expansion board
~~~~~~~~~~~~~~~

`05-073355-01-a.pdf <https://wiki.analog.com/_media/adskplp-ev-ard0z/05-073355-01-a.pdf>`__

.. |image1| image:: https://wiki.analog.com/_media/analog_connector_02_072492_01.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/analog_connectors_schematic_02_072492_01.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/digital_connector_02_072492_01.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/digital_connector_schematic_02_072492_01.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/digital_connector_02_073355_01.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/digital_connector_schematic_02_073355_01.png
   :width: 800px
.. |image7| image:: https://wiki.analog.com/_media/host_connector_02_072492_01.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/arduino_connector_schematic_02_072492_1.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/1_2v_ldo_02_072492_01.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/2_5V_Vref_02_072492_01.png
   :width: 400px
