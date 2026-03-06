ADF7030 INTERFACE WITH EV-COG-AD3029LZ
======================================

Introduction
------------

This document explains about the hardware and software setup, which is required to interface a ADF7030 radio transceiver with the EV-COG-AD3029LZ using SPI protocol. The entire setup is made simple with the use of AD-GEAR-DISPLAY1Z, which contains the slots for the ADF7030 Daughter Card.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/radio_gear.png
   :width: 600px

The hardware details cover the COG jumper settings and also the pin mapping between the ADF7030-1 Daughter card and the EV-COG-AD3029LZ. The software details cover the software development kit required and the software architecture of the code base written to interface the ADF7030 Daughter card with the EV-COG-AD3029LZ.

Boards and Accessories required
-------------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/cog_gear_radio.png
   :width: 800px

a.) EV-COG-AD3029LZ (left) b.) AD-GEAR-DISPLAY1Z (middle) c.) ADF7030 Daughter card (Right)

\* Two of each is required. One for the Transmitter setup and the other for the Receiver setup.

Hardware interface
------------------

This section contains hardware related information about AD-GEAR-DISPLAY1Z, EV-COG-AD3029-LZ and the ADF7030-1 Daughter card. Links are provided to the WiKi page of the target COG-AD3029-LZ, the Schematics, BOMs and technical documentations at the end of this page.

Connection Diagram
~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/cog_adf7030_connection.png
   :width: 700px

\* The AD-GEAR-DISPLAY1Z board is required as it acts as the interface between EV-COG-AD3029LZ and ADF7030-1 Daughter Card.

Board Interface
~~~~~~~~~~~~~~~

-  Connect the AD-GEAR-DISPLAY1Z via it’s Cog connectors to the EV-COG-AD3029LZ’s expansion connectors.\


|image1|

-  Connect the ADF7030-1 Daughter card to the AD-GEAR-DISPLAY1Z via the expansion's radio connectors.\

|image2|

Pin Connection
~~~~~~~~~~~~~~

==================== ============
EV-COG-AD3029LZ pins ADF7030-1 DB
==================== ============
GPIO18 / SPI2_CLK    SCLK
GPIO19 / SPI2_MOSI   MOSI
GPIO20 / SPI2_MISO   MISO
GPIO39 / SPI2_CS3    CS
GPIO01 / INT_PIN0    GPIO3
GPIO35 / INT_PIN1    GPIO4
GPIO35 / TRG_PIN0    GPIO5
GPIO35 / TRG_PIN1    GPIO0
GPIO03 / RST_PIN     RST
==================== ============

Software Details
----------------

This section contains software related information about AD-GEAR-DISPLAY1Z and the EV-COG-AD3029-LZ and the application. Links are provided to the user guides, BSPs, software tool chains and the example project at the end of this page.

Application files
~~~~~~~~~~~~~~~~~

A library consisting of ADF7030-1 specific drivers are provided for interfacing the radio module with the host controller.

The example software provided consists of the following,

-  Three example application projects:

   -  OfflineCalibration

      -  TxPacket
      -  RxPacket

-  ADF7030-1 specific driver source files.

\* The example application requires ADuCM302x-Rel2.0.0 BSP for IAR to be installed.

Software Architecture
~~~~~~~~~~~~~~~~~~~~~

The software architecture for the ADF7030-1 applications is depicted below


|image3|

\* The system specific APIs like SPI, UART, GPIO etc and present in the ADuCM302x-Rel2.0.0 BSP .

\* The Radio control APIs are found in the Driver files provided within the project application folder.

\* The 3 different projects (OfflineCalibration, RX_packet and TX_packet) share the same workspace but only one of them can be set as active at a time.

IDE Setup and example application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section covers the various steps involved in getting the RX_packet and TX_packet application code to run on EV-COG-AD3029LZ after the hardware setup is done.

Following are the steps involved,

-  Download and install IAR Embedded Workbench 7.60.1 or higher.
-  Download and Install TeraTerm or any equivalent Terminal emulator program
-  The ADF7030-1 project is available on `Bitbucket <https://bitbucket.analog.com/projects/IOTTGAPPS/repos/adf7030-1-rf-support-for-3029/browse>`__.
-  Import the source into IAR workspace .
-  Set TX_packet as active project, build and flash it into the transmitter setup.
-  Now, set RX_packet as active project, build and flash it into the receiver setup.
-  open two instances of TeraTerm(Terminal emulator program) each for transmitter and Receiver, press reset on both setups and see RSSI and data being printed on the receiver terminal window.

References and Links
--------------------

-  :adi:`ADuCM3029 Hardware Reference Manual <media/en/dsp-documentation/processor-manuals/ADuCM302x-mixed-signal-control-processor-hardware-reference.pdf>`
-  :doc:`EV-COG-AD3029LZ User guide with the BSP </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz>`
-  Schematics of EV-COG-AD3029LZ and AD-GEAR-DISPLAY1Z are found in the Docs folder of the ADF7030-1 project.
-  :adi:`ADF7030-1 Data sheet <media/en/technical-documentation/data-sheets/ADF7030-1.pdf>`
-  :adi:`ADF7030-1 Software Reference Manual <media/en/technical-documentation/user-guides/ADF7030-1-UG-1002.pdf>`
-  :adi:`ADF7030-1 Hardware Reference Manual <media/en/technical-documentation/user-guides/ADF7030-1-UG-957.pdf>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/cog_gear_connection.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/gear_radio_connection.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/adf7030_flow.png
   :width: 800px
