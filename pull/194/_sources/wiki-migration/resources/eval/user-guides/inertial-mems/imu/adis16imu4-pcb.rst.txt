ADIS16IMU4/PCBZ Breakout Board Wiki-Guide
=========================================

GENERAL DESCRIPTION
-------------------

The :adi:`ADIS16IMU4/PCBZ <eval-adis16imu4>` is a kit of components that simplifies the process of connecting ADIS1646x IMU products to an embedded processor development platform or to the :adi:`EVAL-ADIS2` evaluation system. This kit has four KEY components: interface board, stand-off, mounting hardware and a ribbon cable.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_intro_01.jpg
   :width: 350px

**NOTE**: The :adi:`ADIS16IMU4/PCBZ <eval-adis16imu4>` kit *DOES NOT* include any of the IMU products that it supports. Those parts must be ordered separately.

ORDERING
--------

:adi:`Click here <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADIS16IMU4.html#eb-discussions>` to order the :adi:`ADIS16IMU4/PCBZ <eval-adis16imu4>`

FEATURES
--------

| \* ADIS1646x-Compatible Breakout Board
| \* 44mm x 47mm Interface Board Size
| \* M2x0.4mm Mounting Hardware Kit
| \* 7mm Spacer for flat surface interface
| \* 16-pinm 12-inch Ribbon Cable
| \* RoHS Compliant

PRODUCT SUPPORT
---------------

The :adi:`ADIS16IMU4/PCBZ <eval-adis16imu4>` provides support for the following IMU models:

+--------------------------------------------------------+


| MODEL NUMBER                                           |

+========================================================+

| :adi:`ADIS16460AMLZ <adis16460>`   |

+--------------------------------------------------------+

| :adi:`ADIS16465-1BMLZ <adis16465>` |

+--------------------------------------------------------+

| :adi:`ADIS16465-2BMLZ <adis16465>` |

+--------------------------------------------------------+

| :adi:`ADIS16465-3BMLZ <adis16465>` |

+--------------------------------------------------------+

| :adi:`ADIS16467-1BMLZ <adis16467>` |

+--------------------------------------------------------+

| :adi:`ADIS16467-2BMLZ <adis16467>` |

+--------------------------------------------------------+

| :adi:`ADIS16467-3BMLZ <adis16467>` |

+--------------------------------------------------------+

KIT CONTENTS
------------

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                 | PICTURE  |
+=============================================================================================================================================================================================================================================================================================================================================================================================+==========+
| The **Interface PCB** contains two interface connectors. The first connector is a dual-row, 14-pin (2x7) socket that mates directly to IMUs from the ADIS1646x family. The second connector is a dual-row, 16-pin (2x8) header that easily connects to standard 1mm ribbon cable connectors, which provides a simple way to connect the ADIS1646x to an existing embedded processor system. | |image5| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| The **Spacer** helps mount the **Interface PCB** to a flat surface by providing recess holes for mounting hardware that fastens the **ADIS1646x** to the **Interface PCB**.                                                                                                                                                                                                                 | |image6| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| The **Ribbon Cable** connects to the 16-pin connector on the **Interface PCB** and provides a good starting point for connecting to an embedded process system.                                                                                                                                                                                                                             | |image7| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| The **M2 Hardware Kit** includes (8) M2x0.4x14mm machine screws, (8) M2 washers and (8) M2x0.4mm nuts. These M2 hardware components help fasten the ADIS1646x to the interface PCB and the interface PCB to the test surface in a system                                                                                                                                                    | |image8| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

INTERFACE PCB DESIGN
--------------------

TOP-LEVEL BOARD VIEW
~~~~~~~~~~~~~~~~~~~~

In the interface PCB size is approximately 44mm x 47mm and has a thickness of ~1.6mm (0.063"). It has four mounting holes, located in each corner of the PCB, which have a basic diameter of 2.46mm and are located 2.2mm from each edge of the board. J1 is a 2x8 header with 2mm spacing, which supports standard 1mm ribbon cable connections. J2 is a 2x7 socket with 1mm spacing, which provides a direct connection to the Inertial Measurement Unit.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_design_00.png
   :width: 500px

SCHEMATIC
~~~~~~~~~

Insert schematic picture and/or a complete pin assignment list

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_design_01.png
   :width: 500px

J1 CONNECTOR PIN ASSIGNMENTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=== ==================================
PIN FUNCTION
=== ==================================
1   Reset (Active Low)
2   SPI, SCLK (Serial Clock)
3   SPI, ~CS (Chip Select, Active Low)
4   SPI, DOUT (Data Output)
5   Not used
6   SPI, DIN (Data Input)
7   Ground
8   Ground
9   Ground
10  VDD (Power Supply)
11  VDD (Power Supply)
12  VDD (Power Supply)
13  Data ready
14  Input clock (data sampling)
15  Not used
16  Not used
=== ==================================

Ribbon Cable Options
~~~~~~~~~~~~~~~~~~~~

Check out the `TCSD series <https://www.samtec.com/products/tcsd>`_ from `Samtec <https://www.samtec.com>`_, to purchase ribbon cable assemblies, which will mate to J1, on the :adi:`\|ADIS16IMU1/PCB <EVAL-adis16imu1>` and the :adi:`EVAL-ADIS2`.

DUT INSTALLATION
----------------

+-------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| STEP  | DESCRIPTION                                                                                                                                 | PICTURE   |
+=======+=============================================================================================================================================+===========+
| **1** | Using the silk screen and J2 connector interface as a guide, install the IMU onto the Interface PCB                                         | |image19| |
+-------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------+
|       | Incorrect pin registration example #1                                                                                                       | |image20| |
+-------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------+
|       | Incorrect pin registration example #2                                                                                                       | |image21| |
+-------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------+
|       | Incorrect pin registration example #3                                                                                                       | |image22| |
+-------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| **2** | Insert the first machine screw into the IMU body, using a washer                                                                            | |image23| |
+-------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| **3** | On the back side, install the washer and nut, hand-tighten                                                                                  | |image24| |
+-------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| **4** | Repeat the process with the other two machine screws, then use a torque screw driver to tighten the machine screw torque to 24 inch-ounces. | |image25| |
+-------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| **5** | Set the interface board (with IMU installed) on top of the spacer                                                                           | |image26| |
+-------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| **6** | Mount the interface board and spacer to the test surface using the machine screws                                                           | |image27| |
+-------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| **7** | Use the ribbon cable to connect to an embedded processor system                                                                             | |image28| |
+-------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------+

CONNECTING TO THE EVAL-ADIS
---------------------------

+-------+-----------------------------------------------------------------------+-----------+
| STEP  | DESCRIPTION                                                           | PICTURE   |
+=======+=======================================================================+===========+
| **1** | Select the ribbon cable from the ADIS16IMU4/PCBZ kit                  | |image34| |
+-------+-----------------------------------------------------------------------+-----------+
| **2** | Install one side of the ribbon cable onto J1 of the ADIS16IMU/PCBZ    | |image35| |
+-------+-----------------------------------------------------------------------+-----------+
|       |                                                                       | |image36| |
+-------+-----------------------------------------------------------------------+-----------+
|       |                                                                       | |image37| |
+-------+-----------------------------------------------------------------------+-----------+
| **3** | Install the other side of the ribbon cable on to J1 of the EVAL-ADISZ | |image38| |
+-------+-----------------------------------------------------------------------+-----------+

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_component_01.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_component_02.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_component_03.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_component_04.png
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_component_01.png
   :width: 300px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_component_02.png
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_component_03.png
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_component_04.png
   :width: 300px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_01a.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_01b.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_01c.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_01d.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_02.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_03.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_04.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_05.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_06.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_07.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_01a.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_01b.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_01c.png
   :width: 400px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_01d.png
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_02.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_03.png
   :width: 400px
.. |image25| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_04.png
   :width: 400px
.. |image26| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_05.png
   :width: 400px
.. |image27| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_06.png
   :width: 400px
.. |image28| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_pcb_wikiguide_install_07.png
   :width: 400px
.. |image29| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_to_eval_adis_01a.jpg
   :width: 400px
.. |image30| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_to_eval_adis_02a.jpg
   :width: 400px
.. |image31| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_to_eval_adis_02b.jpg
   :width: 400px
.. |image32| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_to_eval_adis_02c.jpg
   :width: 400px
.. |image33| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_to_eval_adis_03.jpg
   :width: 400px
.. |image34| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_to_eval_adis_01a.jpg
   :width: 400px
.. |image35| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_to_eval_adis_02a.jpg
   :width: 400px
.. |image36| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_to_eval_adis_02b.jpg
   :width: 400px
.. |image37| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_to_eval_adis_02c.jpg
   :width: 400px
.. |image38| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16imu4_to_eval_adis_03.jpg
   :width: 400px
