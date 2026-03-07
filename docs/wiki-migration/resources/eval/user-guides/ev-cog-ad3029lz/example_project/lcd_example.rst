LCD (EADOGM128x6) INTERFACE WITH EV-COG-AD3029LZ
================================================

Introduction
------------

This document explains about the hardware and software setup, which is required to interface a LCD (EADOGM128W6) with the EV-COG-AD3029LZ through SPI interface.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/cog_gear_display.png
   :width: 600px

The hardware details cover the COG jumper settings and also the pin mapping between the LCD (EADOGM128W6) and the EV-COG-AD3029LZ. The software details cover the software development kit required and the software architecture of the code base written to interface the LCD with the EV-COG-AD3029LZ.

Boards and Accessories required
-------------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/cog_gear.png
   :width: 700px

a.) EV-COG-AD3029LZ (left) b.) AD-GEAR-DISPLAY1Z (right)

Hardware interface
------------------

This section contains hardware related information about AD-GEAR-DISPLAY1Z and the EV-COG-AD3029-LZ. Links are provided to the WiKi page of the target COG-AD3029-LZ, the Schematics, BOMs and technical documentations at the end of this page.

Connection Diagram
~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/cog_lcd_connection.png
   :width: 600px

The LCD backlight (if present) is controllable by the GPIO Expander. Please refer to the schematics of the LCD Gear expander in the Docs folder of the lcd_example project for more information.

Board Interface
~~~~~~~~~~~~~~~

-  Connect the AD-GEAR-DISPLAY1Z via it’s Cog connectors to the EV-COG-AD3029LZ’s expansion connectors.\


|image1|

Pin Connection
~~~~~~~~~~~~~~

==================== ======================
EV-COG-AD3029LZ pins AD-GEAR-DISPLAY1Z pins
==================== ======================
GPIO22 / SPI1_CLK    SCL_SCK
GPIO23 / SPI1_MOSI   SI
GPIO08 / LCD_A0      A0
GPIO25 / SPI1_CS0    CS_N
GPIO28 / LCD_RST     RST_N
==================== ======================

LCD Backlight
~~~~~~~~~~~~~

The LCD has a corresponding backlight that can be purchased separately and soldered beneath the LCD. The gear does not come included with the components needed to support the LCD backlight by default and the components need to be added as per the schematic.

Software Details
----------------

This section contains software related information about AD-GEAR-DISPLAY1Z and the EV-COG-AD3029-LZ. Links are provided to the user guides, BSPs, software tool chains and the example project at the end of this page.

Application files
~~~~~~~~~~~~~~~~~

The example software provided consists mainly of the following

-  LCD_test.c
-  LCD_test.h
-  CCES project files (\*.svc, \*.project, \*.cproject).
-  The application uses the ADuCM302x-Rel 2.0.0 driver BSP for CCES.
-  CrossCore Embedded Studio 2.6.0 or higher is advised to be used.

Application flow
~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/lcd_flow.png
   :width: 600px

-  A BMP-LCD tool application is provided in the Docs folder of the lcd_example project to convert bitmap image to be displayed into an array of hex bytes that can be included in the source code and used to display an image.
-  All the APIs for using the LCD is within the LCD_test.c file. In the next release the APIs to interact with the LCD will be moved to a separate file.

IDE Setup and example application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section covers the various steps involved in getting the LCD_example application code to run on EV-COG-AD3029LZ after the hardware setup is done.

Following are the steps involved,

-  Download and install CrossCore Embedded Studio 2.6.0 or higher.
-  Download the lcd_example project from `lcd_example.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/lcd_example.zip>`_
-  The lcd_example project is also available on `Bitbucket <https://bitbucket.analog.com/projects/IOTTGAPPS/repos/lcd-ev-cog-aducm3029lz/browse>`_.
-  Import the source into CCES workspace and run the application software and see the results displayed on the LCD.

Upon successfully flashing the project into the COG, it will lead to displaying the Analog Devices logo on the LCD screen followed by the messages "IoT Apps" and "LCD test Application".

References and Links
--------------------

-  :adi:`ADuCM3029 Hardware Reference Manual <media/en/dsp-documentation/processor-manuals/ADuCM302x-mixed-signal-control-processor-hardware-reference.pdf>`
-  :doc:`EV-COG-AD3029LZ User guide with the BSP </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz>`
-  `EA-DOGM128w6 (LCD) <http://www.lcd-module.com/eng/pdf/grafik/dogm128e.pdf>`_
-  Schematics of EV-COG-AD3029LZ and AD-GEAR-DISPLAY1Z are found in the Docs folder of the lcd_example project.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/cog_gear_connection.png
   :width: 600px
