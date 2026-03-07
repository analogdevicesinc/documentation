EV-COG-AD4050LZ MCU COG
=======================

The :adi:`EV-COG-AD4050LZ` is an MCU COG board for the :adi:`ADuCM4050` MCU.

Main Features
-------------

-  `ADuCM4050 <https://wiki.analog.com/www.analog.com/aducm4050>`_ (LFCSP package) - Ultra Low Power ARM Cortex-M4F MCU
-  Compact form factor (3.5 cm X 7.5 cm) - Easy to deploy.
-  On board debugger capability (CMSIS DAP compatible)
-  Multiple power options and current monitoring test-points.
-  On-board sensors: Accelerometer (ADXL362) and Temperature Sensor (ADT7420)
-  Optional expansion capability - Using application specific add-on cards (*Gears*)
-  Optional connectivity options - Using RF modules (*Connectivity Cogs*)

.. warning::

   LFXTAL feature on ADuCM4050 is not supported currently


Board
-----

Front-Side
~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/25072017-tile-revb-front.png
   :alt: 25072017-tile-revb-front.png

Back-Side
~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/25072017-tile-revb-back.png
   :alt: 25072017-tile-revb-back.png

Power
-----

The MCU Cog board offers flexibility in terms of power supply and power muxing options. This is achieved with the use of jumpers on the board. The Cog board also offers multiple test points for monitoring current consumption.

Power Supply Options
~~~~~~~~~~~~~~~~~~~~

The MCU Cog offers the following power supply options:

::

   -5V USB power (USB microB connector)
   -3V CR2032 Coin cell (Cell holder - BT1)
   -3V - 6V Rechargeable Li-Ion Battery (JST Connector - P6)
   -3V - 6V External Supply from an MCU Cog Add-on card (via Connector C1)

Power Muxing Options
~~~~~~~~~~~~~~~~~~~~

For details of the power muxing scheme, refer to the figure below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/23062017-tile-revb-power-mux-scheme.png

.. danger::

   Do not insert shunt b/w positions 5 & 6 of JH4 when using USB supply. Doing so can permanently damage this board.


.. tip::

   Refer to the *Jumper Settings* section further below for details on power related jumpers on the board


Power Regulator
~~~~~~~~~~~~~~~

The MCU Cog board uses an on-board switching regulator - the :adi:`ADP5300 <en/products/power-management/switching-power-converters/switching-regulators/adp5300.html>`, which is a high efficiency, ultra-low power step down regulator. The MCU has complete control over the switching modes of the regulator via GPIO. The pin-mapping is shown in the table below.


|direct|

Current Measurement Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The MCU Cog enables IOT developers to measure and profile current consumption at different places on the board to enable isolation of current consumption hotspots. The current measure test points shown in the table below can be used along with a digital multimeter to profile current consumption.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/24072017-tile-revb-current-test-points.png
   :alt: 24072017-tile-revb-current-test-points.png

Programming & Debug Options
---------------------------

The MCU Cog offers the following debug options:

::

   -On-board CMSIS-DAP debugger (USB microB connector)
   -JLINK-9 Connector for access to SWD interface (P26)
   -Access to SW interface to an MCU Cog Add-on card (via Connector C2)

.. tip::

   It is possible to route UART over USB through the on-board CMSIS-DAP debugger. The maximum baud rate that can be achieved in this case is 230400


Wireless Connectivity Options
-----------------------------

The MCU Cog board offers support for ADI RF daughter-cards such as the EV-ADF70301-915AZ via the "EV-COG-BLEINTP1" connectivity Cog board that can be attached at Connector P2. This connectivity Cog board also has on-board BTLE circuit enabling the MCU Cog board to use BTLE communication as well. More details regarding wireless connectivity options are available on the :doc:`EV-COG-BLEINTP1 Wiki page </wiki-migration/resources/eval/user-guides/ev-cog-bleintp1z>`.

Buttons/LED(s)
--------------

The MCU Cog offers 2 buttons and 2 LED(s) that can be used by the Application. The default GPIO connections are shown in the tables below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/24072017-tile-revb-buttons-leds2.png
   :alt: 24072017-tile-revb-buttons-leds2.png

Expansion Connectors
--------------------

One of the USP of the MCU Cog is access to ALL GPIO via Expansion Connectors ("C1" and "C2") for an Add-on card to utilize in its Application. This enables developers to confidently build final form factor hardware without having to worry about porting their firmware. The figures below capture the pin-mapping and jumpers that need to be changed to get external access (via the expansion connectors) to GPIO (as well as power/reset, etc).

|image1|\ |image2|

Jumper Settings
---------------

The MCU Cog offers flexibility in terms of power muxing options and the facility to route any GPIO externally via the expansion connectors "C1" and "C2". This is achieved with the use of jumpers. The MCU Cog has two types of jumpers - those labelled "JHx" and which are 2x2 1.27mm pitch headers and those labelled "JPx" and which are solder jumpers. The "JHx" jumpers are expected to be used more frequently than the "JPx" jumpers. The figures below capture the jumper settings. |power-jumpers.png| |image3|


|image4|

MCU Cog Design and Integration Files
------------------------------------

`21052017-iot-devkit-tile-revb-schematics.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/21052017-iot-devkit-tile-revb-schematics.pdf>`_

::

     MCU Cog revB Schematics 
     MCU Cog revB Layout
     MCU Cog revB BOM
     

Add-on (Gear) Template
~~~~~~~~~~~~~~~~~~~~~~

For developers designing a Cog add-on board, the template schematic/board files below might be a useful starting point. The board file has the placement of the expansion connectors as well as place-bound rules embedded.

`Template Design Files (Cadence Allegro v16.6) <https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/20-047257-01a.zip>`_

.. |direct| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/24072017-tile-revb-adp5300-gpio.png
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/c1-conn-mapping.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/c2-conn-mapping.png
.. |power-jumpers.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/power-jumpers.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/10082017-sensor-jumpers.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/10082017-debug-jumpers.png
