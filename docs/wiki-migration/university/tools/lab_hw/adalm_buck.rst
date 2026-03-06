ADALM-BUCK-ARDZ
===============

Overview
--------

The :adi:`ADALM-BUCK-ARDZ` board is a companion module for the Buck Basics lab exercise: :doc:`Activity: Buck Converter Basics </wiki-migration/university/courses/electronics/buck_converter_basics>`

This lab exercise can be done on a breadboard using parts from the ADALP2000 parts kit, but it is too involved to do in a hands-on seminar session or single-day workshop. The ADALM-BUCK-ARDZ module is designed to eliminate the assembly time associated with constructing the circuit on a breadboard, while keeping all of the measurements and experiments intact.

Figure 1 shows the various connections, and along with the schematic below can be used as a guide as you work through the lab exercise.

.. image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm_buck/adalm_buck_connections_rev2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1. ADALM-BUCK connections and jumpers


ADALM-BUCK-ARDZ Jumpers and Connections
---------------------------------------

The default jumper configurations for this board model are as follows:

+------------+--------------------------------------------+-----------------------------------------------------------+
| Jumper     | Function                                   | Default Setting                                           |
+============+============================================+===========================================================+
| P1         | Power Supply Select                        | Shunt installed across pins 2 & 3 (5V from Arduino)       |
+------------+--------------------------------------------+-----------------------------------------------------------+
| P2         | Inductor Tap #                             | Shunt installed across pins 1 & 2 (6 taps/max inductance) |
+------------+--------------------------------------------+-----------------------------------------------------------+
| P3         | Inductor Voltage                           | Open (for M2K connection)                                 |
+------------+--------------------------------------------+-----------------------------------------------------------+
| P5         | DC coupling (remove for AC coupling)       | Shunt installed                                           |
+------------+--------------------------------------------+-----------------------------------------------------------+
| P6         | Output at pin 1, lower 2 pins are GND      | Open (for M2K connection)                                 |
+------------+--------------------------------------------+-----------------------------------------------------------+
| P10        | Arduino Analog input 0                     | Solder Blobbed                                            |
+------------+--------------------------------------------+-----------------------------------------------------------+
| P13        | Override source                            | Shunt installed across pins 1 & 2 (Arduino PWM)           |
+------------+--------------------------------------------+-----------------------------------------------------------+
| P17        | Enable Override                            | Shunt NOT installed                                       |
+------------+--------------------------------------------+-----------------------------------------------------------+
| P18        | Switch Node at pin 1, lower 2 pins are GND | Open (for M2K connection)                                 |
+------------+--------------------------------------------+-----------------------------------------------------------+
| P19        | 10μF output capacitor                      | Shunt installed                                           |
+------------+--------------------------------------------+-----------------------------------------------------------+
| P20        | 47μF output capacitor                      | Shunt installed                                           |
+------------+--------------------------------------------+-----------------------------------------------------------+
| P24        | Arduino PWM output 3                       | Solder Blobbed                                            |
+------------+--------------------------------------------+-----------------------------------------------------------+
| All Others |                                            | Open / no shunt installed                                 |
+------------+--------------------------------------------+-----------------------------------------------------------+

Hardware Setup Procedure
------------------------

Figure 2 shows the ADALM2000 connections for measuring the switch node voltage on Channel 1 and ripple current on Channel 2. The ADALM-BUCK is installed on an Arduino UNO clone with LT1054_voltage_mode_buck_DC_ctrl.ino sketch uploaded (refer to Buck Basics lab exercise for details.)

.. image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm_buck/adalm-buck_m2k_connections.jpg
   :align: center
   :width: 600px

   |

.. container:: centeralign

   Figure 2. ADALM-BUCK to ADALM2000 connections


Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download
   :class: download

   :adi:`ADALM-BUCK-ARDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/adalm-buck-ardz-designsupport.zip>`

   
   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   
   |

| *End of Document*
