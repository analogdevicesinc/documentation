EV-COG-SMARTMESH1Z
==================

Introduction
============

EV-COG-SMARTMESH1Z combines reliability and ultra low-power with a native Internet Protocol (IP) layer for a robust, standards-based offering perfect for a broad range of applications. It provides robust wire-free connectivity for applications where low power, reliability, and ease of deployment matter. EV-COG-SMARTMESH1Z is configured in the slave mode and is driven by an external micro-controller.The communication between the controller and EV-COG-SMARTMESH1Z takes place via UART.

The features of SmartMesh IP enabled by EV-COG-SMARTMESH1Z are as follows:-

-  Programming the device using an external micro-controller via Flash SPI lines
-  Flow control for UART communication
-  Obtaining network time for accurate time stamping
-  Switching between CLI and API modes of operation
-  Programming and debugging via J-link
-  Radio silence for radio free sensor data acquisition

This user guide describes the connector pin out,and jumper settings available on board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/intro_pic.png
   :align: center
   :width: 300px

The hardware details covers the wire connections between the EV-COG-SMARTMESH1Z and EV-COG-AD3029LZ along with useful links that provides more details pertaining to EV-COG-AD3029LZ and EV-COG-SMARTMESH1Z.

Hardware details
================

Board image
-----------

Primary-side
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/primary_side_fin.png
   :align: center
   :width: 500px

Secondary-side
~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/secondary_side_fin.png
   :align: center
   :width: 300px

The board consists of

-  32 pin Hirose connector (P1)
-  UART mode switch (SW1)
-  Tag connect point (TC1)
-  Antenna terminal (J4)
-  Flow control jumpers(JP1, JP2, JP3)

32 pin Hirose connector
~~~~~~~~~~~~~~~~~~~~~~~

The Hirose connector P1 interfaces the EV-COG-SMARTMESH1Z board with the MCU Cog. The connector carries VDD, UART, Flash SPI lines and GPIO signals from MCU cog board. The pinout details are given in the following table

================================ ============= ===================
Hirose connector (P1) pin number pin name      MCU Cog signal name
================================ ============= ===================
1                                VSUPPY        VDD_RF
2                                VSUPPY        VDD_RF
3                                GND           GND
4                                GND           GND
5                                UART_RX_MCU   MCU/UART0_RX
6                                JMP_TX_RTSN   RF_INT
7                                UART_TX_MCU   MCU/UART0_TX
8                                RADIO_INHIBIT MCU/SPI2_CS3
9                                GND           GND
10                               IPCS_MISO     MCU/SPI2_MISO
11                               N.C           RF_SYS_WAKE
12                               IPCS_MOSI     MCU/SPI2_MOSI
13                               FLASH_P_ENn   MCU/GPIO08
14                               IPCS_SCK      MCU/SPI2_CLK
15                               N.C           P.D [GND, 100K]
16                               GND           GND
17                               SLEEPn        P.U [VDD_RF, 100K]
18                               JMP_TX_CTSN   SPI2_RDY
19                               N.C.          N.C
20                               N.C           SS_TO_RF
21                               TIMEn         GPIO27
22                               RESETn        GPIO_RF_RESET
23                               N.C           C2/54
24                               N.C           C2/55
25                               N.C           C2/58
26                               N.C.          RF_SYS_WAKE
27                               N.C           C2/59
28                               IPCS_SSn      SPI2_CS0
29                               GND           GND
30                               GND           GND
31                               VSUPPY        VDD_RF
32                               VSUPPY        VDD_RF
================================ ============= ===================

The following figure shows EV-COG-SMARTMESH1Z connected to EV-COG-AD3029LZ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/interface_fin.jpg
   :align: center
   :width: 300px

Schematics, PCB layout, Bill of materials
-----------------------------------------

.. admonition:: Download
   :class: download

   
   EV-COG-SMARTMESH1Z Rev A Design and Integration Files
   
   -  `Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/schematics_ev-cog-smartmesh1z.pdf>`_ (PDF)
   -  `Bill of materials <https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/05-048367-01-a.pdf>`_ (PDF)
   -  `Fabrication Files <https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/fab.zip>`_ (Zip)
   -  `Assembly Files <https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/assy.zip>`_ (zip)
   


Example Software
================

.. admonition:: Download
   :class: download

   Click :doc:`Here </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz/example_project/temp_sensor_smartmesh>` to visit the example software page, and to download the source code from Analog Devices Git repository


Help and support
================

For help and support on the EV-COG-SMARTMESH1Z use the following `SmartMesh-IP_support_link <http://www.linear.com/products/smartmesh_ip#techsupport>`_ and for the EV-COG-AD3029LZ use :doc:`EV-COG-AD3029_support_link </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz/help_support>`.

For more information contact us at :ez:`EngineerZone <community/analog-microcontrollers/aducm302x>` or Email
