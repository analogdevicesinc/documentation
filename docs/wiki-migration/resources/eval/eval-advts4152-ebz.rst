=======ADVTS-4152 Combo Power Supply Solution=========

**SPECIFICATION**

-  Main Input battery voltage range: 4V to 38V
-  Back- up battery charge voltage: 3.4V -4.2V Lithium Ion or Lithium -Iron Phosphate
-  Battery Input Selectable Switch at S1, S2, S3
-  Output Voltage and Current: Vout(max) – 5V, Iout(max) – 3A
-  Output Ripple Voltage - -3.842mV

**FEATURES**

Integrated Solution:

-  Fault Protection and Surge Stopper for load dump, cold crank, reverse polarity input and overcurrent
-  Pin Selectable Back-up battery charging using Li-Ion or LiPeO4
-  Seamless auto switch from main input battery to back-up batteries
-  High overvoltage transient capability of up to 200V while continually output 5V

.. image:: https://wiki.analog.com/_media/wiki/advts4152/product_picture.png
   :align: center
   :width: 400px

**EQUIPMENT NEEDED**

-  DC Power Supply or 12V car battery
-  Li-Ion 3.7V or 4.1V LiPeO4 battery
-  Resistive or Electronic Load
-  Load dump emulator
-  Oscilloscope

--------------

EVAL-ADVTS4152-EBZ Overview
===========================

The :adi:`EVAL-ADVTS4152` demonstration board is intended for systems that require a constant output voltage of 5V like in a Vehicle tracking system (VTS). It is run by a main battery source with a back-up battery in case of unwanted shortage of supply happens in the input. Demo board features the three main parts that function as one to achieve the highest performance and reliability of the board. These parts are:

:adi:`LT4356-1`: a surge stopper that protects high voltage transients such as load dumps to electronic automotive loads, with wide range input capability of 4V to 80V and clamps to a desirable voltage output that suites will suite your design need. It also provides protection against reverse input and cold crank.

:adi:`LT8609A <LT8609>`: a compact, high efficiency and high speed synchronous monolithic step-down switching regulator that outputs desired max current of 3A continuously.

And, :adi:`LTC4040`: supply rail and backup battery that contains high current step-up DC/DC regulator that backup the supply from a single cell Li-Ion or LiFePO4 and help power the system when the main supply cuts off. The demo board has an EMI filter installed for automotive standard requirement and optional ADT6401 circuit for over temp protection if the design needs to protect abnormal high DC Input.

EVAL-ADVTS4152-EBZ is a board that can easily be integrated and can speed up faster time to market.

--------------

Introduction
============

EVAL-ADVTS4152-EBZ Board Hardware

.. image:: https://wiki.analog.com/_media/wiki/advts4152/product_hardware_details.png
   :align: center
   :width: 600px

:adi:`EVAL-ADVTS4152-EBZ <EVAL-ADVTS4152>` is consist of three major sections. These are the Fault Protection and Surge Stopper, Step-Down Regulator, Back-Up Supply. These three blocks work together to provide reliable and efficient power to the downstream electronics like VTS. It can operate across a wide range of input voltage of 80V DC and surge voltage of up to 210V.

EVAL-ADVTS4152-EBZ Block Diagram


|image1|

Section 1: This section functions as a Fault Protection that is mainly driven by the LT4356-1 IC. This IC protects the board from surge and overvoltage, this keeps the system work in a desired operating voltage range. When a surge event occurs, the LT4356-1 clamps the voltage at 38V allowing the board to maintain its operation at a certain time standard for automotive while the surge.

.. image:: https://wiki.analog.com/_media/wiki/advts4152/product_schematic_section_1.png
   :align: center
   :width: 600px

::

                                                   Section 1: LT4356-1 Schematic
                   

Section 2: This section function as step-down regulator in the board and is mainly catered by the LT8609A IC – a highly efficiency and high speed synchronous monolithic step-down switching regulator which keeps the output level at a constant voltage of 5V a max current of 3A.The LT8609A burst mode operation enables high efficiency down to very low output current while keeping the output ripple below 10mVpeak-peak.

LT8609A has a SYNC pin that allows synchronization to an external clock or spread spectrum modulation for low EMI operation.

.. image:: https://wiki.analog.com/_media/wiki/advts4152/schematic_diagram_section_2.png
   :align: center
   :width: 600px

::

                                                   Section 2: LT8609A Schematic
                   

Section 3: This section function as a back-up supply or battery back-up power manager in the board. Mainly catered by the LTC4040 IC – a high-current step-up DC-to-DC regulator to back up the supply from a single-cell Lithium Ion or Lithium-Iron-Phosphate battery.

When the main input supply is available, the LTC4040 chip step-up regulator operates in reverse as a step-down battery charger to the Li-Ion or LiFePO4. The charging voltage can be configured via selectable pin S3, S2 and S1. Check the performance summary table for reference.

.. image:: https://wiki.analog.com/_media/wiki/advts4152/schematic_diagram_section_3.png
   :align: center
   :width: 600px

::

                                                   Section 3: LTC4040 Schematic
                   

--------------

EVAL-ADVTS4152-EBZ Normal Operation Connection
==============================================

ADVTS-4152 Combo Power Supply Typical Operation Set-up

The ADVTS-4152 board is typically installed between car battery supply and downstream load. The back-up battery is then attached to the VBACKUP pin to complete the system. The board when applied with 12V or 24 V DC supply coming from car battery then outputs a constant of 5V DC with 3A max current. Once the ADVTS-4152 Combo Power supply board is connected, it is now a good to go in your system.

EVAL-ADVTS4152-EBZ Normal Operation Connection


|image2|

--------------

EVAL-ADVTS4152-EBZ Test Set-up Guide
------------------------------------

Below set-ups are guide to test the :adi:`EVAL-ADVTS4152-EBZ <EVAL-ADVTS4152>`. Follow diagram details and instruction to ensure proper set-up.

EVAL-ADVTS4152-EBZ LOAD DUMP TEST SET-UP |image3| LOAD DUMP TEST SET-UP

1) Connect low voltage power supply (12V or 24V) to the load dump generator input

2) Connect the high voltage power supply to the triggering input of the load dump generator.

3) Connec the output of the load dump generator to the ADVT4152 main input (as shown in the diagram).

4) Connect also the 1A DC electronic load constant current at the output of ADVTS4152 or after the LED indicator.

5) Have those voltage input monitor using oscilloscope as indicated above.

Oscilloscope Setting: all probe at 200ms time interval.

Ch1 - set it to 5V/Div

Ch2 - set it to 10V/Div

Ch3 - set it to 20V/Div

--------------

EVAL-ADVTS4152-EBZ BACK-UP BATTERY TEST SET-UP


|image4|

1) Connect low voltage power supply (12V or 24V) or a car battery with the same input voltage to the main input supply.

2) Connect Li-Ion or LiFePO4 to the battery input located in the below part of the ADVTS4152 board as shown in the diagram above.

3) Connect also the 1A DC electronic load constant current at the output of ADVTS4152 or after the LED indicator.

4) Have those voltage input monitor by follow the probe connections in above diagram.

Oscilloscope Setting: all probe at 200ms time interval.

Ch1 - Main Input - set it to 10V/Div

Ch2 - Back-up Battery Input- set it to 5V/Div

Ch3 - ADVT4152 Output - set it to 5V/Div

--------------

EVAL-ADVTS4152-EBZ BACK-UP OVERCURRENT TEST SET-UP


|image5|

1) Connect low voltage power supply (12V or 24V) or a car battery with the same input voltage to the main input supply.

2) Connect Li-Ion or LiPeO4 to the battery input located in the below part of the ADVTS4152 board as shown in the diagram above.

3) Connect a 1A DC electronic load constant resistance at the output of ADVTS4152 or after the LED indicator.

4) Connect an Ammeter at the ADVTS4152 output.

5) Have those voltage input monitor by follow the probe connections in above diagram.

Oscilloscope Setting: all probe at 200ms time interval.

Ch1 - Main Input - set it to 1A/Div

Ch2 - LT8609A output- set it to 5V/Div

--------------

EVAL-ADVTS4152-EBZ BACK-UP REVERSE POLARITY TEST SET-UP


|image6|

1) Connect low voltage power supply (12V or 24V) or a car battery positive terminal to the negative port of the ADVTS4152 main input and the negative terminal to the positive port.

2) Connect Li-Ion or LiPeO4 to the battery input located in the below part of the ADVTS4152 board as shown in the diagram above.

3) Connect a 1A DC electronic load constant current at the output of ADVTS4152 or after the LED indicator.

4) Connect an Ammeter at the ADVTS4152 output.

4) Have those voltage input monitor by follow the probe connections in above diagram.

Oscilloscope Setting: all probe at 200ms time interval.

Ch1 - Main Input - set it to 5V/Div

Ch2 - ADVTS4152 output- set it to 5V/Div

--------------

Schematic, PCB Layout, Bill of Materials
----------------------------------------

http://wwmbe-hlm.ad.analog.com/apps/hlm/pcb/nhrs/02-064059-01/Schematic

--------------

=====Helpful Links==========

-  Application Note Page

--------------

More Information and Useful Links
---------------------------------

::

    EVAL-ADVTS4152-EBZ Other Important Files

-  :adi:`LT4356-1/LT4356-2 Product Page <LT4356-1>`
-  :adi:`LT8609/LT8609A/LT8609B Product Page <LT8609>`
-  :adi:`LTC4040 Product Page <LTC4040>`
-  :adi:`ADT6401 Product Page <ADT6401>`

*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/wiki/advts4152/product_block_diagram.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/wiki/advts4152/normal_operation_conn.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/wiki/advts4152/load_dump_test_setup.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/wiki/advts4152/backup_bat_test_setup.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/wiki/advts4152/overcurrent_test_setup.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/wiki/advts4152/reverse_polar_test_setup.png
   :width: 600px
