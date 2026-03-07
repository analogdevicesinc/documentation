EV-GEAR-EINK1Z User Guide
=========================

Introduction
------------

EV-GEAR-EINK1Z is a “Gear” (expansion add-on board) for MCU Cogs (EV-COG-AD3029LZ & EV-COG-AD4050LZ). The Gear is used to enable interfacing with EINK Electronic Paper Display (EPD). This gear can be used for quick prototyping and deployment of COG+EPD solutions.

The EV-GEAR-EINK1Z supports these displays

-  EL029TR1 (2.9`\` ePaper Display)
   \* ED057TC6 (5.65`\` ePaper display)

Features
--------

-  24 pin connector for connecting EPD
-  LED to indicate when EPD is powered on
-  emperature and Humidity Sensor SHT31 is present
-  2.5V LDO powers the EPD interface
-  Provision to power the system through CR2450 coin cell

Hardware Details
----------------

Primary side
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-gear-eink1ztop.jpg
   :width: 700px

Secondary side
~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eink_gear_bottom.png
   :width: 700px

Block Diagram
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/epd_block_diagram_2.png
   :width: 700px

Connecting to MCU Cog
---------------------

Connecting EPD to EV-GEAR-EINK1Z
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Step. 1: Unlock the EPD connector
| |image1|
| Step. 2: Insert the display into to EPD connector
| |image2|
| Step. 3: Lock the EPD connector
| |image3|

Connecting EV-GEAR-EINK to MCU-COG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The EV-GEAR-EINK1Z can be powered only if connected to a MCU-COG. Connect the gear to the MCU-Cog as shown in the picture

COG Connectors C1 and C2 are used to interface EV-GEAR-EINK1Z with MCU COG. C1 and C2 connectors carry all the pins necessary to interface EPD with MCU COG. The pinout details of C1 and C2 can be found in :doc:`EV-COG-AD3029LZ MCU Cog </wiki-migration/resources/eval/user-guides/eval-cog-ad3029lz/cog_hw_userguide>`

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eink_gear_1.jpg
   :width: 600px

Place the COG on the EINK-Gear such that COG connectors (C1 and C2) on COG and EINK-Gear connect to each other.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eink_cog_4.png
   :width: 600px

| 
| ====Power options==== There are 3 options to power the COG+EPD setup. The option can be selected using the power-switch on MCU-Cog. <Image>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/power_table_1.png
   :width: 600px

| 
| ====Test points==== For quick debugging, following test points are provided.

-  TP1 : SPI0_MOSI
-  TP2 : SPI0_CLK
-  TP3 : SPI0_MOSI
-  TP4 : SPI0_CS0
-  TP5 : SYS_WAKE3
-  TP6 : GPIO41

| 

EV-GEAR-EINK1Z Design and Integration Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|

.. admonition:: Download
   :class: download

   `EV-GEAR-EINK Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/ev-gear-eink1z_schematics.pdf>`_

   | `EV-GEAR-EINK1Z Layout and BOM <https://wiki.analog.com/_media/resources/eval/user-guides/ev-gear-eink1z_-_fab.zip>`_
   | `EV-GEAR-EINK1Z assembly <https://wiki.analog.com/_media/resources/eval/user-guides/ev-gear-eink1z_-_assembly_files.zip>`_


:doc:`Back </wiki-migration/resources/eval/user-guides/rapidnet-ip>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/epd_unlock.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/epd_conn_display.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/epd_lock.jpg
   :width: 400px
