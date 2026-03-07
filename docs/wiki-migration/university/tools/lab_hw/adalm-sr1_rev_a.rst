ADALM-SR1 Rev A hardware
========================

.. important::

   DEPRECATED: This page is for rev A of the ADALM-SR1, for those who received boards from the first pilot run. Documentation for the latest revision is at :doc:`ADALM-SR1 hardware </wiki-migration/university/tools/lab_hw/adalm-sr1>`\


Description
-----------

The ADALM-SR1 (Analog Devices Active Learning Module, Switching Regulator #1) board is a companion module for several switching regulator exercises covering buck and boost regulators:

| :doc:`Activity: Boost and Buck converter elements and open-loop operation </wiki-migration/university/labs/open_loop_boost_and_buck_adalm2000>`
| :doc:`Activity: Buck Converters: closed loop operation </wiki-migration/university/labs/closed_loop_buck_adalm2000>`
| :doc:`Activity: Boost Converters: closed loop operation </wiki-migration/university/labs/closed_loop_boost_adalm2000>`

The circuits required for these exercises exceed the complexity that can be constructed on a breadboard, so the ADALM-SR1 is required to run them, although the simulations can be run beforehand to gain insight.

The Figure 1 shows an overview of the board, along with connections to an ADALM2000 (M2K) and meters.

|image1| |image2|

.. container:: centeralign

   Figure 1. ADSRALM overview


ADALM-SR1 Jumpers and Connections
---------------------------------

The ADALM-SR1 uses 0.635mm (0.025-mil) headers for configuration jumpers, signal inputs, and signal outputs. Signal inputs and outputs are 2-conductor headers with 5.08mm (200-mil) pitch so that they cannot be confused with configuration jumpers. The lower conductor is always a ground connection (that is not always used) and an arrow indicates whether the upper conductor is an input or output.

| 

Inductance Selection
~~~~~~~~~~~~~~~~~~~~

+--------------+-----------------------------------+------------------+-------------------+-------------------+--------------------+--------------------+--------------------+
|              | Inductance Selection              |                  |                   |                   |                    |                    |                    |
+==============+===================================+==================+===================+===================+====================+====================+====================+
| Jumper       | P3                                |                  |                   |                   |                    |                    |                    |
+--------------+-----------------------------------+------------------+-------------------+-------------------+--------------------+--------------------+--------------------+
| **Position** | EXT IND                           | 1 TAP            | 2 TAPS            | 3 TAPS            | 4 TAPS             | 5 TAPS             | 6 TAPS             |
+--------------+-----------------------------------+------------------+-------------------+-------------------+--------------------+--------------------+--------------------+
| **Function** | Ext. inductor between TP3 and TP4 | 7.7μH inductance | 31.5μH inductance | 72.6μH inductance | 131.5μH inductance | 216.2μH inductance | 313.4μH inductance |
+--------------+-----------------------------------+------------------+-------------------+-------------------+--------------------+--------------------+--------------------+
|              |                                   |                  |                   |                   |                    |                    |                    |
+--------------+-----------------------------------+------------------+-------------------+-------------------+--------------------+--------------------+--------------------+

\\\\\


|image3|

Topology, FET and Current Sense Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------------------------------------------------------------------+-----------------------+-----------------------------------------+------------------------------------------+
|          | FET Selection                                                        |                       | Current Sense Selection                 |                                          |
+==========+======================================================================+=======================+=========================================+==========================================+
| Jumper   | P37                                                                  |                       | P35                                     |                                          |
+----------+----------------------------------------------------------------------+-----------------------+-----------------------------------------+------------------------------------------+
| Position | BUCK                                                                 | BOOST                 | BUCK                                    | BOOST                                    |
+----------+----------------------------------------------------------------------+-----------------------+-----------------------------------------+------------------------------------------+
| Function | Select buck topology                                                 | Select boost topology | Select the proper FET for buck topology | Select the proper FET for boost topology |
+----------+----------------------------------------------------------------------+-----------------------+-----------------------------------------+------------------------------------------+
|          |                                                                      |                       |                                         |                                          |
+----------+----------------------------------------------------------------------+-----------------------+-----------------------------------------+------------------------------------------+
| Notes    | **Proper selection allows complete inductor waveform to be viewed.** |                       |                                         |                                          |
+----------+----------------------------------------------------------------------+-----------------------+-----------------------------------------+------------------------------------------+

.. image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p37_p35_p25.jpg
   :align: center

Output Capacitors Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+---------------------------------------------------------+----------------------------------------+
|          | Output Capacitors Selection                             |                                        |
+==========+=========================================================+========================================+
| Jumper   | P8, P11                                                 |                                        |
+----------+---------------------------------------------------------+----------------------------------------+
| Position | Installed                                               | Open                                   |
+----------+---------------------------------------------------------+----------------------------------------+
| Function | P8 connect **aditional** 47 :math:`\mu` F capacitance   | Keep only 47 :math:`\mu` F capacitance |
+----------+---------------------------------------------------------+----------------------------------------+
|          | P11 connect **aditional** 470 :math:`\mu` F capacitance | Keep only 47 :math:`\mu` F capacitance |
+----------+---------------------------------------------------------+----------------------------------------+
|          |                                                         |                                        |
+----------+---------------------------------------------------------+----------------------------------------+

.. image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p8_p11.jpg
   :align: center

Feedback Selection
~~~~~~~~~~~~~~~~~~

+----------+--------------------------------------------------+---------------------------------------------------+----------------------------------------+
|          | Feedback Selection                               |                                                   |                                        |
+==========+==================================================+===================================================+========================================+
| Jumper   | P20                                              |                                                   |                                        |
+----------+--------------------------------------------------+---------------------------------------------------+----------------------------------------+
| Position | 5V                                               | 12V                                               | ALT                                    |
+----------+--------------------------------------------------+---------------------------------------------------+----------------------------------------+
| Function | Select feedback resistors used for buck topology | Select feedback resistors used for boost topology | Select experimental feedback resistors |
+----------+--------------------------------------------------+---------------------------------------------------+----------------------------------------+
|          |                                                  |                                                   |                                        |
+----------+--------------------------------------------------+---------------------------------------------------+----------------------------------------+

.. image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p20.jpg
   :align: center

Load Resistors Selection
~~~~~~~~~~~~~~~~~~~~~~~~

+----------+------------------------------------------------------------------------------------------------+--------------------------------------+
|          | Load Resistors Selection                                                                       |                                      |
+==========+================================================================================================+======================================+
| Jumper   | P18, P14, P13, P17, P16, P15                                                                   |                                      |
+----------+------------------------------------------------------------------------------------------------+--------------------------------------+
| Position | Installed                                                                                      | Open                                 |
+----------+------------------------------------------------------------------------------------------------+--------------------------------------+
| Function | P18 connect 200 :math:`\Omega` load resistance                                                 | No aditional load resistor connected |
+----------+------------------------------------------------------------------------------------------------+--------------------------------------+
|          | P14 connect 200 :math:`\Omega` load resistance                                                 | No aditional load resistor connected |
+----------+------------------------------------------------------------------------------------------------+--------------------------------------+
|          | P13 connect 100 :math:`\Omega` load resistance                                                 | No aditional load resistor connected |
+----------+------------------------------------------------------------------------------------------------+--------------------------------------+
|          | P17 connect 50 :math:`\Omega` load resistance                                                  | No aditional load resistor connected |
+----------+------------------------------------------------------------------------------------------------+--------------------------------------+
|          | P16 connect 25 :math:`\Omega` load resistance                                                  | No aditional load resistor connected |
+----------+------------------------------------------------------------------------------------------------+--------------------------------------+
|          | P15 connect 12.5 :math:`\Omega` load resistance                                                | No aditional load resistor connected |
+----------+------------------------------------------------------------------------------------------------+--------------------------------------+
|          |                                                                                                |                                      |
+----------+------------------------------------------------------------------------------------------------+--------------------------------------+
| Notes    | **7V max across 25Ω, 12.5Ω resistors will turn on the Over Power LED illuminates as warning.** |                                      |
+----------+------------------------------------------------------------------------------------------------+--------------------------------------+

.. image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p13_p18.jpg
   :align: center

Duty Cycle Source Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------------------------------------------------------------------------------------------------+----------------------------------+
|          | Duty Cycle Source Selection                                                                        |                                  |
+==========+====================================================================================================+==================================+
| Jumper   | P23                                                                                                |                                  |
+----------+----------------------------------------------------------------------------------------------------+----------------------------------+
| Position | Closed-loop                                                                                        | Manual                           |
+----------+----------------------------------------------------------------------------------------------------+----------------------------------+
| Function | Duty controlled by error amplifier                                                                 | Duty controlled by potentiometer |
+----------+----------------------------------------------------------------------------------------------------+----------------------------------+
|          |                                                                                                    |                                  |
+----------+----------------------------------------------------------------------------------------------------+----------------------------------+
| Notes    | **Current Threshold still operational for safety, determined by Current Threshold Potentiometer.** |                                  |
+----------+----------------------------------------------------------------------------------------------------+----------------------------------+

.. image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p23.jpg
   :align: center

Control Mode Selection
~~~~~~~~~~~~~~~~~~~~~~

+----------+----------------------------------------------------------------------------+---------------------------+
|          | Control Mode Selection                                                     |                           |
+==========+============================================================================+===========================+
| Jumper   | P32                                                                        |                           |
+----------+----------------------------------------------------------------------------+---------------------------+
| Position | Peak Current                                                               | Duty Cycle                |
+----------+----------------------------------------------------------------------------+---------------------------+
| Function | Start on clock rising edge, stop on peak current                           | Direct duty cycle control |
+----------+----------------------------------------------------------------------------+---------------------------+
|          |                                                                            |                           |
+----------+----------------------------------------------------------------------------+---------------------------+
| Notes    | **Closed/open-loop determined by Duty Cycle or Current Threshold jumper.** |                           |
+----------+----------------------------------------------------------------------------+---------------------------+

.. image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p32.jpg
   :align: center

Current Threshold Source Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------------------------------------------------+-----------------------------------------+
|          | Current Threshold Source Selection                                                            |                                         |
+==========+===============================================================================================+=========================================+
| Jumper   | P22                                                                                           |                                         |
+----------+-----------------------------------------------------------------------------------------------+-----------------------------------------+
| Position | Manual                                                                                        | Closed-loop                             |
+----------+-----------------------------------------------------------------------------------------------+-----------------------------------------+
| Function | Threshold controlled by potentiometer                                                         | Threshold controlled by error amplifier |
+----------+-----------------------------------------------------------------------------------------------+-----------------------------------------+
|          |                                                                                               |                                         |
+----------+-----------------------------------------------------------------------------------------------+-----------------------------------------+
| Notes    | **Set Duty Cycle pot to approx. 50%. (not critical, rising edge controls start of the ramp)** |                                         |
+----------+-----------------------------------------------------------------------------------------------+-----------------------------------------+

.. image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p22.jpg
   :align: center

Measurement Points
~~~~~~~~~~~~~~~~~~

+-----------------------+--------------+------------------------------------------------------------------------------------------------+
| Measurement Points    |              |                                                                                                |
+=======================+==============+================================================================================================+
|                       | Name         | Notes                                                                                          |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
| **TP1**               | P_PROT       | Overvoltage/overcurrent protected power.                                                       |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
|                       | |image13|    |                                                                                                |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
| **P1**                | SW_NODE_HI   | Switch node in buck topology.                                                                  |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
|                       | |image14|    |                                                                                                |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
| **P4**                | SW_NODE_LOW  | Switch node in boost topology.                                                                 |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
|                       | |image15|    |                                                                                                |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
| **P2**                | IHIGH        | Current sense amplifier output, boost configurations (0.1Ω sense R, G=7, 1.429A/V net output). |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
|                       | |image16|    |                                                                                                |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
| **P12**               | ILOW         | Current sense amplifier output, buck configurations (0.1Ω sense R, G=7, 1.429A/V net output).  |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
|                       | |image17|    |                                                                                                |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
| **P10, P9, TP5, TP7** | V_OUT        | Experiment output voltage. P10 can be AC coupled by removing P9.                               |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
|                       | |image18|    |                                                                                                |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
| **P5**                | FB_MEAS      | Feedback perturbation measurement (AC coupled).                                                |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
|                       | |image19|    |                                                                                                |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
| **P33**               | CLOCK        | Master clock, 3.3V logic level.                                                                |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
|                       | |image20|    |                                                                                                |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
| **P34**               | GATE CONTROL | FET gate control signal, 3.3V logic level.                                                     |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+
|                       | |image21|    |                                                                                                |
+-----------------------+--------------+------------------------------------------------------------------------------------------------+

Injection Points
~~~~~~~~~~~~~~~~

+------------------+----------------+----------------------------------------------------------------------------------+
| Injection Points |                |                                                                                  |
+==================+================+==================================================================================+
|                  | Name           | Notes                                                                            |
+------------------+----------------+----------------------------------------------------------------------------------+
| **P28**          | ITH MOD        | Peak current control modulation (1.429A/V). Install P29 to DC couple.            |
+------------------+----------------+----------------------------------------------------------------------------------+
|                  | |image25|      |                                                                                  |
+------------------+----------------+----------------------------------------------------------------------------------+
| **P27**          | DUTY CYCLE MOD | Duty Cycle modulation (100%/V). Install P26 to DC couple.                        |
+------------------+----------------+----------------------------------------------------------------------------------+
|                  | |image26|      |                                                                                  |
+------------------+----------------+----------------------------------------------------------------------------------+
| **P7**           | FB_MOD         | Feedback modulation for loop gain measurements (XXV/V). Install P6 to DC couple. |
+------------------+----------------+----------------------------------------------------------------------------------+
|                  | |image27|      |                                                                                  |
+------------------+----------------+----------------------------------------------------------------------------------+

Hardware Setup Procedure
------------------------

Refer to individual lab exercises for detailed setup information.

Auxiliary Circuit Details
-------------------------

The setup and operation of circuitry associated with the lab exercises is described in detail in the exercises themselves. The ADALM-SR1 includes various auxiliary housekeeping and protection circuits described here.

| 

Housekeeping supplies and reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADALM-SR1 has two power inputs. The experiment power input is supplied by the user, and the voltage will vary depending on the experiment being run. An additional micro USB connector is the input for a 5V "housekeeping" supply that powers all of the control circuitry, allowing the experiment power to vary over a wide range. An LT3472 boosts / inverts the 5V supply to +15 / -2V, respectively. This provides a high voltage and slightly negative voltage for the LT1995 current sense amplifiers, and a negative supply for the error amplifier.

| |image28|

An LT1970-1.25 provides an accurate reference for the error amplifier and duty cycle, current threshold adjustment potentiometers.

| |image29|
| ==== Input Overvoltage, Undervoltage, Reverse voltage, and Overcurrent ==== An LTC4368 and associated circuitry protects the experiment power input by only turning on when the supply is between 3V and 15V. The circuit is protected from voltages between -40V and +60V. The LTC4368 also functions as a fuse, shutting off the supply if the current exceeds 2A.

.. image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_power_input_protection.jpg
   :align: center

| 
| ==== Output Overvoltage ==== In boost mode, the ADSRALM can produce high voltages under certain conditions: if the duty cycle is high and the load is light, or if feedback is disconnected. An LTC2912 overvoltage / undervoltage supervisor will disable the switching circuitry if the output exceeds 22V. An SMAJ24A, 24-volt TVS diode provides additional protection.

.. image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_output_overvoltage.jpg
   :align: center

| 
| ==== Inductor, Load Resistor Overtemperature ==== The inductor and onboard load resistors can get warm during certain experiments or if the board is misconfigured. Three temperature sensors measure the inductor temperature and the temperature of the high-dissipation areas of the load resistor bank. If any temperature exceeds 60ºC, switching is disabled for a 1.9 second cool-down period.

The low-resistance loads consist of parallel, single 100Ω, 1/2W resistors - An orange LED near the associated jumpers illuminates when the output voltage exceeds 7V as a warning that these must be disconnected.

The high resistance loads consist of multiples of two 100-ohm, 1/2W resistors in series, which will handle voltages up to 14V. A temperature sensor is still included in case the output voltage exceeds 14V or if the experiment is left running for an extended period of time.

.. image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_overtemperature.jpg
   :align: center

| 

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download
   :class: download

   
   ADALM-SR1 Design & Integration Files (PLACEHOLDERS)
   
   -  `Schematics <https://wiki.analog.com/_media/university/tools/lab_hw/adalm_sr1/02_059790a_top.pdf>`_
   


*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm_sr1/adalm_sr1_overview.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1.jpg
.. |image3| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p3.jpg
.. |image4| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_tp1.jpg
.. |image5| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p1.jpg
.. |image6| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p4.jpg
.. |image7| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p2.jpg
.. |image8| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p12.jpg
.. |image9| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p10_p9_tp5_tp7.jpg
.. |image10| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p5.jpg
.. |image11| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p33.jpg
.. |image12| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p34.jpg
.. |image13| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_tp1.jpg
.. |image14| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p1.jpg
.. |image15| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p4.jpg
.. |image16| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p2.jpg
.. |image17| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p12.jpg
.. |image18| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p10_p9_tp5_tp7.jpg
.. |image19| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p5.jpg
.. |image20| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p33.jpg
.. |image21| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p34.jpg
.. |image22| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p28_p29.jpg
.. |image23| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p27_p26.jpg
.. |image24| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p7_p6.jpg
.. |image25| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p28_p29.jpg
.. |image26| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p27_p26.jpg
.. |image27| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_p7_p6.jpg
.. |image28| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_housekeeping_supplies.jpg
.. |image29| image:: https://wiki.analog.com/_media/university/tools/lab_hw/adalm-sr1_reference.jpg
