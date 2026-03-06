ADBMS6830B Broad Market Kit Reference Design User Guide
=======================================================

Overview
--------

| |image1| The **ADBMS6830B Broad Market Kit** is a combined multicell battery-stack, pack monitor, and agnostic to any MCU (Arduino form factor and Featherboard) modular solution to the broad market space. It highlights the accuracy, robustness and scalability of :adi:`ADBMS6830`, a 16-channel battery-stack monitor as well as pack monitor :adi:`ADBMS2950`. Multiple boards can be linked through a 2-wire isolated serial interface (isoSPI) to monitor a long series cell in a stack. This solution allows customer to perform BMS capability of Analog Devices in the wider audience of broad market. Combined with capability in reversible isoSPI, as easy to use communication path.
| The **ADBMS6830B Broad Market Kit** can be operated in Embedded mode or through a PC using different microcontroller. The microcontroller provides a standard SPI interface which can be translated to isoSPI in the docker board and then connected to the EVAL-ADBMS6830 isoSPI port, then connect as well to the EVAL-ADBMS2950 isoSPI port where both are docked to the DEV board which has a ready reversible isoSPI ADBMS68222 chip to communicate with the MCUs.
| This complete battery monitoring system (BMS) solution is suitable to perform state of charge (SoC) and state of health (SoH), state of power (SOP) to a wide range application in broad market in the industrial, consumer, agricultural, and other adjacent business segments.

Features
--------

-  Accurate Measurement on Voltage and Current
-  Highly scalable and ease of integration
-  Robust ISO SPI capability implementable in daisy chain high count
-  Inclusive passive balancing with individual pulse-width modulation
-  Wide range of input supply 11V to 60V range
-  Isolated power supply between microcontroller and Battery Monitoring chips
-  Stackable and Daisy Chain up to 10 6830 boards

Applications
------------

-  IoT Battery Management
-  Industrial Machine Vision
-  Power Tools
-  Mobile Robotics Battery Management
-  Industrial Equipment Battery Monitoring
-  Adaptive Battery Type System Monitoring
-  Portable Energy Storage Systems
-  Electric Two-Wheelers (E2W such as E-scooter, E-bikes)
-  Light Electric Vehicles

--------------

Simplified Block Diagram
------------------------

|image2|

.. container:: centeralign

   *Figure 2: EVAL-ADBMS6830 Simplified Block Diagram*


Board Definition
----------------

ADBMS6830
~~~~~~~~~

| |image3| The ADBMS6830 is a multicell battery stack monitor that measures up to 16 series connected battery cells with a lifetime total measurement error (TME) of less than 2 mV over the full temperature range. The measurement input range of −2 V to +5.5 V.
| ==== ADBMS2950 ==== |image4| The ADBMS2950 is a battery pack monitor that measures the current flowing in and out of a battery pack by sensing the voltage drop over a shunt resistor with a very low offset. It can cater up to 1KV voltage. ADBMS2950 can also detect overcurrent conditions using fast overcurrent ADCs with digital threshold comparators and communicate their results through dedicated overcurrent alert lines with minimum delay.
| ==== Docker Board ==== |image5| ADBMS6830B or Open Market Dev Board. This board can basically connect Arduino, Featherboard, Shields and Wings that can be used and utilized in your development activity. Some features of this board also include snipping ready SPI and Iso-SPI lines, I2C PMOD connect to BMS, cell protection relay for balancing, redundant iso-SPI connection, agnostic MCU usability.
| ==== PCB Connector (Auxiliary board) ==== |image6| This PCB connector Has the capability to flexibly and easily connect either to Battery Cell Emulator (DS2427A) or to actual cell. Used to do also measure stack voltage of cell going to the docker board. This can be use a well if you have limited space of deployment where you can stack the cell monitoring connection.

--------------

Available BMS Measurements
--------------------------

The ADBMS6830B Broad Market Reference Design can be use both in 2 modes it can either be as Embedded Application or As PC based Application. A quick glance of this functions are listed in below table.

| |image7|

.. container:: centeralign

   **Available Measurements or Functions for Embedded Application**


| For the PC based using BMS GUI, please refer to the BMS GUI for the available measurements or functions.

Typical Hardware Configuration
------------------------------

| This section describes how to typically set-up and connect ADBMS6830B Kit boards and do get functional readings. Generally, it operates on two modes which will be describe in Modes of Operation Section. These steps will guide user to get the boards functionally running.
| ==== Start Up Connection ==== 

.. raw:: html

   <details><summary>Click to expand</summary>

**CELL MONITORING SETUP**

-  Connect EVAL-ADBMS6830B J1 connector with the PCB connector. Make sure to tightly screw the pins.
-  Place the EVAL-ADBMS6830 board at the bottom of the Docker board and ensure to properly mate GPIO pinouts of EVAL-ADBMS6830B to the female GPIO slot (P17, P14) and the cell monitoring male header pinouts (P6, P16) of the Docker board. Allow the connector to snap to ensure that is properly mated.
-  Connect the 2-wire twisted pair from EVAL-ADBMS6830B J3 (ISO-SPI A) to P18 connector of the Docker board.
-  In case a DS2427A is available, power it up via USB and rotate the know to select voltage range you want. Voltage range for the DS2427A ranges from 1.5V-4.5V.
-  Then connect this emulator to the J1 of PCB Connector. If none is available, you can use wire to directly connect to the actual battery cells. Make sure to tighten the screws.
-  For the MCU, currently the supported model is the MAX32666 in embedded mode. you can utilize the feather board version of this MCU and place it plug it on the Docker board feather board connection slot. For the other mode of operation (PC based GUI). You can utilize the MAX32666 Featherboard or the SDP-K1 with Arduino form factor for this mode.
-  Once you were able to do the steps above. You can now start basic cell measurements by utilizing the ADBMS6830B Broadmarket Kit software's. Please refer to software section for the Embedded mode and PC based mode.

.. note::

   
   -  Make sure that you are ESD safe when performing this set-up.
      \* For SDP-K1 or other Arduino for factor board, please check the method of connection shown on below picture for guidance.
   
   |


| **PACK MONITORING SETUP**

-  Connect EVAL-ADBMS2950-BASIC pack monitor HV1 connector with a cable to the V\ :sub:`BAT+` (pin1) of connector P10 in the Docker board. Then connect HVS01 of the EVAL-ADBMS2950-BASIC to GND- (pin2) of P11 in the Docker board.
-  Connect V\ :sub:`BAT-` of the shunt resistor to the GND- of the Docker board.
-  The connect or supply via USB cable the EVAL-ADBMS2950-BASIC to enable 5V V\ :sub:`reg` for the chip.
-  You can now utilize or run the ADBMS6830B Broadmarket Kit software's to check functional reading for current measurement. Please refer to software section for the Embedded mode and PC based mode.

.. note::

   In Daisy chain mode for cell monitor, the VBAT- of the cell monitor is sometime = GND-

.. raw:: html

   </details>


Modes of Operation - Pin Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

|

.. note::

   The ADBMS6830B Broad Market Kit Reference Design has two modes of operation: **Embedded System Mode** and **PyBMS-Based**.


| **EMBEDDED SYSTEM MODE (no-OS, MCU)** |image8|

-  Attach the BMS Connector Board to C1 of the EVAL-ADBMS6830B.
-  Align the GPIO GND header pins of the EVAL-ADBMS6830MCS to P14 and P17 of the Docker Board. P1 and P2 of the BMS Connector Board to P6 and P16 of the Docker Board.
-  Attach the Feather Board to P7 and P15 of the Docker Board.

| 
| **PyBMS-BASED (PC)** |image9|

-  Attach the BMS Connector Board to C1 of the EVAL-ADBMS6830MCS.
-  Align the SDP-K1 P5 header pins to ICSP of the Docker Board.

| 
|

.. note::

   Both were able to perform the two types of connection: **Stacking** or **Daisy Chain Connection**. The only difference in the connection is the microcontroller used.


   | **EVAL-ADBMS6830 STACKING CONNECTION**

-  Using the twisted pair cable, connect isoSPI A of the EVAL-ADBMS6830MCS to isoSPI B of the EVAL-ADBMS2950-BASIC.
-  Connect isoSPI A of the EVAL-ADBMS2950-BASIC to P18 of the Docker Board.
-  Connect HVS01 of the EVAL-ADBMS2950-BASIC to P11 ground terminal of the Docker Board.
-  Connect the VBAT+ terminal of the Docker Board to the EVAL-ADBMS2950-BASIC depending on the required voltage:

   -  to HV1 if voltage is >250V
   -  to HV2 if voltage is between 500V to 700V
   -  to HV3 if voltage is between 700V to 1kV

|

| **EVAL-ADBMS6830 DAISY CHAIN CONNECTION**

-  Connect the isoSPI A of the first EVAL-ADBMS6830MCS to isoSPI B of EVAL-ADBMS2950-BASIC.
-  Connect the isoSPI B of the first EVAL-ADBMS6830MCS to isoSPI A of second EVAL-ADBMS6830MCS.
-  Connect the isoSPI A of the EVAL-ADBMS2950-BASIC to P18 or P19 of the Docker Board.
-  Connect HVS01 of the EVAL-ADBMS2950-BASIC to P11 ground terminal of the Docker Board.
-  Connect the VBAT+ terminal of the Docker Board to the EVAL-ADBMS2950-BASIC depending on the required voltage:

   -  to HV1 if voltage is >250V
   -  to HV2 if voltage is between 500V to 700V
   -  to HV3 if voltage is between 700V to 1kV

.. raw:: html

   </details>


--------------

Software Setup
--------------

Software Installation
~~~~~~~~~~~~~~~~~~~~~

| <fc #ff0000><< insert here >></fc>
| ==== Software Operation ==== <fc #ff0000><< insert here >></fc>
| ----

Modes of Operation
------------------

The **ADBMS6830B Broadmarket BMS Kit** has 2 mode of operation that can be configured by the user. It can support different MCU form factor like the Arduino and the Featherboard which is done in the docker board (note: initially we called it ADBMS6830 OM DEV board). It has also readily available supply connection for both form factor (+3.3V, or 5V) whatever the MCU uses.

Embedded System Mode (no-OS, MCU)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

| The ADBMS6830 Broadmarket Kit can be set-up as a standalone system. It has available drivers for ADBMS6830B module and ADBMS2950 module that can be integrated to different MCU for customer applications. The embedded mode utilizes the no-OS framework to create the drivers. No-OS driver codes can be access via GitHub.
| <fc #ff0000><<Place diagram here>></fc>
| This set-up runs using the no-OS drivers for ADBMS6830B, ADBMS2950 as well as for MAX32666. Link for this drivers are located in <fc #ff0000>(place link here- github)</fc>. Current available MCU used is MAX32666.

Steps:

1. Follow or Perform the Typical Set-up at the top.

2. Check the drivers at this location (github). You should be able to see the ADBMS6830,ADBMS2950 and MAX32666 (or MAX32665).

3. A sample program at the github location (\*paste link here) is available to perform basic functionality on BMS which is supported by the no-OS drivers. for ADBMS6830: (voltage cell measurement, average voltage cell measurement,vref,itemp,gpio,vres,vd)

for ADBMS2950: (current measurement,GPIO, Itemp..)

4. Use the pico programmer to program the MAX32666 Featherboard. Connect the programmer cable to the J12 of MAX32666 Featherboard.

5.Connec the USB- B end connector going MCU and the USB side to the PC.

5. Open Maxim SDK and run the program via Eclipse. (Location of the program)

6. Check the desired program and load the program.

7. Once done and good you can now remove the USB connector the nyoucannow place the MAX32666 Featherboard on your typical set-up.

8. Apply voltage from 12V-60V to the TP18 of the Dockerboard.

9. To check if the BMS Mesurements, you can place the pico programmer again at J12 on theMAX32666 Featherboard and power it up the pico via USB.

10. Then open teraterm or putty and set-up the port address as seen in the device manager.

11. Set baudrate to 115200 and click ok.

12. You should be able to read now a sample measurement. (paste sample result).

| 
| \*\* OPTIONAL CONNECTIONS **
  ** Connecting ADBMS6830 Docker Board to Another MCU **
  <fc #ff0000><<Insert here>></fc>
  ** IsoSPI Connection \*\*
| <fc #ff0000><<Insert here>></fc>

.. raw:: html

   </details>


PyBMS-Based (PC)
~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

The ADBMS6830 Broad market Kit can also be set-up in applications that uses PC. Generally, this set-up can do basic evaluation functions of the cell monitor (ADBMS6830B) chip and battery pack (ADBMS2950) chip along with different MCU that customers used.

| <fc #ff0000><<Place diagram here>></fc>
| **REQUIREMENTS**

-  Hardware

   -  EVAL-SDP-CK1Z controller board
   -  ADBMS6830 OM Dev Board (Docker board)
   -  2 EVAL-ADBMS6830 dual master isoSPI adapter board
   -  1 EVAL-ADBMS2950 Pack monitor

-  Software

   -  PyBMS- Based BMS GUI

| 
| \*\* ADBMS6830B Kit Setup*\*
| \* This kit is a combination of different module. In order to properly set-up the kit, the user must take note that it is properly grounded to avoid static discharging that may damage the modules.

-  Connect EVAL-ADBMS6830MCS(-B) with the PCB connector to the cell monitoring connector side of the EVAL-ADBMS6830MCS.
-  Connect EVAL-ADBMS6830MCS ISO-SPI A with the twisted 2-wire cable.
-  Then connect the EVAL-ADBMS6830MCS to the Docker board at the bottom mating the GPIO connection at the bottom.
-  Connect also the DC2427A battery emulator at the other end of the PCB Connector while mating the PCB connector female header to the male header connector of the docker board.
-  Then connect the other end of the 2-wire cable to the P18 (should be shorted connect the P24) connector to the docker board.

| 
| \*\* Connecting the Battery Pack EVAL-ADBMS2950-BASIC \*\*

-  Connect the EVAL-ADBMS2950-BASIC to the P24.
-  Connect via cable the VH1 of EVAL-ADBMS2950-BASIC to the VBAT+ of the docker board.
-  Then connect to GND the VBAT- and HVS01 of the EVAL-ADBMS2950-BASIC.
-  You can now run the software and check if you read voltage measurement and current measurement.

| 
| \*\* OPTIONAL CONNECTIONS **
  ** Connecting ADBMS6830 Docker Board to Another MCU **
  <fc #ff0000><<Insert here>></fc>
  ** isoSPI Connection \*\*

  | <fc #ff0000><<Insert here>></fc>

.. raw:: html

   </details>


|

--------------

System Performance
------------------

| <fc #ff0000><< insert here >></fc>

--------------

Performance Summary
-------------------

Below are the absolute maximum ratings of voltages relative to GND unless noted otherwise.

======================================= ======= ======= ======= ====
Parameter                               Minimum Typical Maximum Unit
======================================= ======= ======= ======= ====
System Vin\ :sup:`+` Supply Voltage     6       12      60      V
Cell Monitoring Main Supply Voltage     11              85      V
V\ :sub:`REG` Supply Voltage            4.5     5       5.5     V
V\ :sub:`REF1` 1\ :sup:`st` Reference   3.0     3.2     3.3     V
Voltage No Load                                                 
V\ :sub:`REF2` 2\ :sup:`nd` Reference   2.995   3       24      V
Voltage, 5k Load to V-                                          
C\ :sub:`PIN` Input Range               -2.5            5.5     V
Cell Count                                              16      
Pack Monitoring Main Supply Voltage In  21                      V
Pack Monitoring Main Supply Voltage Out                 1000    V
V\ :sub:`REG` Pack Monitor              4.5     5       5.5     V
Current Input S1A, I1A, I1B             -4              4       V
Current Input S2A, I2A, I2B             -4              4       V
Current Input I3A, I3B                  -4              4       V
MCU Supply Voltage                      3.3             5.5     V
MCU Standalone Supply Range             5               5.5     V
MCU via USB Supply range                3.3             5.5     V
C\ :sub:`x` Voltage                     -0.3            85      V
======================================= ======= ======= ======= ====

--------------

SPI/I2C Communication During Idle and Running Condition
-------------------------------------------------------

| The supply conditions for communication lines are varied. Users can take advantage of any of these supply circumstances. The table below shows how SPI and I2C lines can be used.

Given the parameters below:

-  VP = VDD = VDDS = 3.3V
-  VP = VDD = 5V
-  VDDS = 3.3V
-  VP = VDD = VDDS = 5V

=================== ==== ========= ==== ========= ==== =========
Communication Lines IDLE RUNNING   IDLE RUNNING   IDLE RUNNING
=================== ==== ========= ==== ========= ==== =========
**SCK**             0    0.5 - 0.7 0    0.5 - 0.7 0    0.5 - 0.7
**MISO**            2.5  1.3 - 1.6 2.5  1.3 - 1.6 2.5  2.1 - 2.4
**MOSI**            0    1.5 - 3.3 0    1.5 - 3.3 0    1.5 - 3.3
**CSB**             3.3  1.3 - 1.6 3.3  1.3 - 1.6 3.3  1.3 - 1.6
**CSB1**            3.3  3.3       3.3  3.3       3.3  3.3
**SCL**             3.3  NA        3.3  4.99      5    4.99
**SDA**             3.3  NA        3.3  4.99      5    4.99
=================== ==== ========= ==== ========= ==== =========

--------------

Demo Application
----------------

Use Case: E-Bikes
~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/adbms6830/e-bike_application.png
   :align: center
   :width: 3000px

Use Case: E-Scooters
~~~~~~~~~~~~~~~~~~~~

<fc #ff0000><< insert here >></fc>

--------------

Additional Information and Useful links
---------------------------------------

-  :adi:`ADBMS6830 Product Page <ADBMS6830>`
-  :adi:`ADBMS6822 Product Page <ADBMS6822>`
-  Product pages of the ADI parts used

--------------

Reference Demo and Software Resources
-------------------------------------

-  Link to the project source code (if applicable)
-  Links to the wiki documentation of the IPs that are used in this project (if applicable)
-  Links to the drivers and devicetree source code and wiki documentation (if applicable)
-  Links to reference demo (if applicable)

--------------

Design & Integration Files
--------------------------

.. admonition:: Download
   :class: download

   :adi:`EVAL-ADBMS6830 Design & Integration Files <EVAL-ADBMS6830-DesignSupport.zip>`

   
   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   


--------------

Hardware Registration
---------------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-ADBMS6830?&v=Rev0>`__ to receive all these great benefits and more!


*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/adbms6830/adbms6830b_board_photo.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/adbms6830/adbms6830b_bm_kit_01_block_diagram.png
   :width: 3000px
.. |image3| image:: https://wiki.analog.com/_media/adbms6830/adbms6830.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/adbms6830/adbms2950.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/adbms6830/docker_pins.png
   :width: 1000px
.. |image6| image:: https://wiki.analog.com/_media/adbms6830/pcb_board.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/adbms6830/available_bms_measurements.png
   :width: 3000px
.. |image8| image:: https://wiki.analog.com/_media/adbms6830/embedded.png
   :width: 3000px
.. |image9| image:: https://wiki.analog.com/_media/adbms6830/pc_based.png
   :width: 3000px
