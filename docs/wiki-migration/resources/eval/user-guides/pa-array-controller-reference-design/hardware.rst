Power Amplifier (PA) Array Controller Hardware User Guide
=========================================================

Overview
--------

| The PA Array Controller Board is a reference design utilizing ADI's portfolio for control, protection, and appropriate bias sequencing of power amplifier (PA) arrays designed for massive multiple input - multiple output (MIMO) and macro base station RF front-end applications.
| The system effectively manages the power-up and power-down progression of 4-channel, 8-channel, and 32-channel power amplifiers while continuously monitoring crucial parameters such as drain voltages, drain current, gate voltages, and temperature. A high-speed DAC is employed to achieve rapid transition between bias point and gate voltage pinch-off within a timeframe of less than 5 microseconds. The biasing sequence, sensor management, and user interface are overseen by the :adi:`MAX32666` microcontroller. Additionally, the system incorporates fault detection capabilities to safeguard the amplifiers against overvoltage, overcurrent, and overtemperature events.

Hardware Configuration
----------------------

Primary Side
~~~~~~~~~~~~

|hw_top_label.jpg|

.. container:: center

   *<fc #000000>Figure 2. PA Array Controller Board Top View</fc>*


Power Supply Connectors
^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/power_input.jpg
   :alt: power_input.jpg
   :align: right
   :width: 200px

-  These connectors are used to supply +48 V to the entire circuitry. The PA Array Controller Board provides an option for the user to use either a barrel jack connector or a two-wire terminal.

   -  **P1** is a power barrel connector jack. The user can use this port if they have a +48 V barrel jack.
   -  **P2** is a two-port terminal connector. Any bench power supply can use this port. Make sure to properly connect the positive and negative terminals of the power supply.

-  The user can choose either of the two power supply connectors, **P1** or **P2**. Note that using these two connectors at the same time is not recommended and can incur damage to the board.

| 
| === LED Indicators === |LED.jpg|

-  The reference design uses four LEDs to indicate its current status:

   -  **DS1** LED indicates that there is a fault event occurring on the **first GaN amplifier**.
   -  **DS2** LED indicates that there is a fault event occurring on the **pre-driver and driver amplifiers**.
   -  **DS3** LED indicates normal operation and good power regulation.
   -  **DS4** LED indicates that there is a fault event occurring on the **second GaN amplifier**.

| 
| === Peripheral Connectors === |peripherals.jpg|

-  These connectors are used for debugging, programming, and communication between the software and hardware.

   -  **P5** -> USB UART-Serial Communication
   -  **P6** -> SWD Debugger

| 
| === Switches === |switch.jpg|

-  The main purpose of the switches is to reset a certain device:

   -  **S1** -> LTC7000_1 Reset
   -  **S2** -> LTC7000_2 Reset
   -  **S3** -> MAX32666 Microcontroller Reset
   -  **S4** -> LTC7000_3 Reset

| 
| === Test Points ===

-  The reference design board is comprised of several test points. The table below describes some of the most significant test points and their descriptions.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/test_points.jpg
   :alt: test_points.jpg
   :align: right
   :width: 500px

=========== ========================== ===========
Test Points                            
=========== ========================== ===========
**TP Name** **Description**            **Voltage**
TP3         U1 LTC7000_1 Output        +48 V
TP6         U2 LTC7000_2 Output        +48 V
TP22        U25 LTC7000_3 Output       +48 V
TP11        U6 MAX17643 Output         +5.6 V
TP15        U10 LT3471 Positive Output +12 V
TP16        U10 LT3471 Negative Output -12 V
TP8         U3 ADM7172 LDO Output      +5 V
TP10        U5 LT3042 LDO Output       +5 V
TP9         U4 LT3042 LDO Output       +5 V
TP14        U9 ADM7150 LDO Output      +5 V
TP13        U8 ADM7170 LDO Output      +1.8 V
TP12        U7 ADM7170 LDO Output      +3.3 V
TP17        U11 ADP161 LDO Output      +1.1 V
=========== ========================== ===========

| 
| === Pin Turrets and Hooks ===

-  The PA Array Controller Board is designed for specific power amplifiers and is used on the RF signal chain, as shown below.


|image1|

.. container:: center

   *<fc #000000>Figure 3. RF Signal Chain</fc>*


::

   *The bias lines of these amplifiers must be connected to their desired pinouts on the reference design board. Refer to the table below for the correct pin assignments. 

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/pinouts.jpg
   :align: center
   :width: 500px

.. container:: center round box

   
   =============== ================================== ============
   Pin Assignments                                    
   =============== ================================== ============
   **Pin Name**    **Description**                    **Pin Type**
   5V0_802         HMC802A VDD Pin                    Hook
   EN_802          HMC802A Enable Pin                 Hook
   5V0_PDA         ADL5611 VPOS Pin                   Hook
   5V0_DA          BTS6201U VCC Pin                   Hook
   EN_DA           BTS6201U Enable Pin                Hook
   VDC1            A5M36TG140 LDMOS Carrier Drain Pin Hook
   VDP1            A5M36TG140 LDMOS Peaking Drain Pin Hook
   VGC1            A5M36TG140 LDMOS Carrier Gate Pin  Hook
   VGP1            A5M36TG140 LDMOS Peaking Gate Pin  Hook
   VDC2            A5M36TG140 GaN Carrier Drain Pin   Turret
   VDP2            A5M36TG140 GaN Peaking Drain Pin   Turret
   VGC2            A5M36TG140 GaN Carrier Gate Pin    Hook
   VGP2            A5M36TG140 GaN Peaking Gate Pin    Hook
   VD1             GTRB384608FC-V1 GaN Main Drain Pin Turret
   VD2             GTRB384608FC-V1 GaN Peak Drain Pin Turret
   VG1             GTRB384608FC-V1 GaN Main Gate Pin  Hook
   VG2             GTRB384608FC-V1 GaN Peak Gate Pin  Hook
   =============== ================================== ============
   


Secondary Side
~~~~~~~~~~~~~~

|image2|

.. container:: center

   *<fc #000000>Figure 4. PA Array Controller Board Bottom View</fc>*


--------------

System Setup
------------

Note that this user guide only allows the user to test and measure the time transition of the following:

-  **AD3552R DAC settling time**

   -  From pinch-off to normal operating voltage
   -  From normal operating to pinch-off voltage

-  **Fault detection up to DAC pinch-off voltage**

.. note::

   The PA Array Controller Board was not fully characterized, so this user guide only tests and measures the settling time of the three DACs and fault detection.


| 
| ==== Equipment Needed ==== The following is the list of items needed to replicate the timing test.

Hardware
^^^^^^^^

-  PA Array Controller Board
-  One (1) programmable power supply

   -  It should accommodate a voltage level of +30 V to +60 V

-  Two (2) micro-USB to USB cable

   -  For UART-Serial communication
   -  For SWD Debugger

-  One (1) :adi:`MAX32625PICO` rapid development platform with SWD cable
-  One (1) 4-channel oscilloscope
-  One (1) oscilloscope probe
-  Six (6) 10 nF capacitors (act as a load for all 6 gate pins)

.. warning::

   The PA Array Controller Board was not fully characterized yet. Using actual amplifiers as a load is **NOT RECOMMENDED**. Instead, use a 10 nF capacitor.


| 
| === Firmware ===

-  <<Insert updated firmware link>>

| 
| ==== General Test Setup ==== This section describes the basic setup and connections to bring-up the board.

|image3|

.. container:: center

   *<fc #000000>Figure 5. Setting up the Hardware </fc>*


-  Connect the 10-pin SWD debug cable to port P6 of the PA Array Board.
-  Connect the other end of the SWD debug cable to the MAX32625PICO.
-  Use the micro-USB to USB cable to connect the MAX32625PICO to your PC or laptop. This connection allows the user to upload firmware to the board.
-  Then, connect the other micro-USB to USB cable to port P5. This connection allows the USB-to-UART communication.
-  Connect the positive terminal of the +48 V power supply to port P2.1.
-  Then, connect the negative terminal to port P2.2. Do not turn on the power supply yet.
-  Lastly, connect the osc probe to the oscilloscope.

| 
| === Firmware Setup ===

-  Install any serial terminal on your PC or laptop. (e.g., Putty, TeraTerm)
-  Note that the board is already pre-loaded with firmware.

| 
| === Basic Operation ===

-  Now that we are finished setting up the hardware and firmware. We will begin to measure the timing response of each AD3552R DAC.
-  Let's start to measure the settling time of the DAC on the GaN gate pins (VGC2, VGP2, VG1, VG2).
-  Connect a 10 nF capacitive load on each GaN gate pins (VGC2, VGP2, VG1, VG2) pin with respect to ground.
-  The positive and negative terminals of all channels of the oscilloscope probe must connect in parallel to each of the capacitor pins.
-  Now, set the required configurations of the oscilloscope:

   -  -3 V on rising edge trigger value
   -  1 µs/div and 2 V/div

-  Refer to Figure 5 for the complete hardware setup.
-  Open any serial terminal; in this case, we will use the TeraTerm.
-  The TeraTerm window will appear, select **"Serial"** and choose the right COM port of the device.
-  Press the **"Setup"** tab, select **"Serial Port"**. A new window will pop up.
-  Set the **"Speed"** or baud rate to **115200**. Make sure that the COM port number is correct. Then, press **"New Setting"** once done.
-  Then, go to terminal setup, and under the new-line group, change the **Receive** to **"AUTO"** and **Transmit** to **"CR+LF"**.
-  Once finished, press **S3** switch to reset the MAX32666 MCU. Upon resetting, the CLI default will appear. Refer to the image below.\

|image4|

.. container:: center

   
   *<fc #000000>Figure 6. Command Line Interface</fc>*


-  The CLI will give the user four command options:

   -  **0 - Menu** command will display the CLI default
   -  **1 - Start GAN1 and GAN2 Power Up Test** command will execute the pinch-off to normal operating voltage transition of two DACs for the two GaN amplifiers.
   -  **2 - Start LDMOS Power Up Test** command will execute the pinch-off to normal operating voltage transition of the LDMOS DAC.
   -  **3 - Start System Power Down Test** command will execute the normal operating to pinch-off voltage transition of all three (3) DACs.
   -  **4 - Start Fault Detection Test** command will execute the fault detection time response.

.. important::

   
   Warning: CLI command selections are strictly sequential to properly measure the voltage setting time and fault event. The user needs to follow this sequence: Command: 1 -> 2 -> 3. If the user makes a mistake, press **S3** to reset the MCU and start again.


-  Press command **"1"** on the serial terminal. The oscilloscope will display the voltage transition and the time response. The result should be the same as the images below.\



|image5|

.. container:: center

   
   *<fc #000000>Figure 7. VGC2 Voltage Time Response</fc>*


\



|image6|

.. container:: center

   *<fc #000000>Figure 8. VGP2 Voltage Time Response</fc>*


\



|image7|

.. container:: center

   *<fc #000000>Figure 9. VG1 Voltage Time Response</fc>*


\



|image8|

.. container:: center

   *<fc #000000>Figure 10. VG2 Voltage Time Response</fc>*


-  Let's measure this time the DAC voltage transition of the LDMOS gate pins (VGC1, VGP1).
-  Connect a 10 nF capacitive load on each LDMOS gate pins (VGC1, VGP1) pin with respect to ground.
-  The positive and negative terminals of the oscilloscope probe must connect in parallel to each of the capacitor pins.
-  Adjust oscilloscope settings:

   -  Trigger value: +1 V on rising edge

-  Press command **"2"** on the serial terminal. The result should be the same as the images below.\


|image9|

.. container:: center

   
   *<fc #000000>Figure 11. VGC1 Voltage Time Response</fc>*


\



|image10|

.. container:: center

   *<fc #000000>Figure 12. VGP1 Voltage Time Response</fc>*


-  At this point, all the gate pins are in the normal operating voltage state. We are now ready to measure the voltage transition from normal operating to pinch-off voltage.
-  Connect all 4-channels of the oscilloscope probes in parallel with all the capacitor pins.
-  Adjust oscilloscope settings:

   -  Trigger value: -3 V on falling edge

-  Press command **"3"** on the serial terminal. The result should be the same as the image below.\


|image11|

.. container:: center

   
   *<fc #000000>Figure 13. VGC2 Voltage Time Response</fc>*


\



|image12|

.. container:: center

   *<fc #000000>Figure 14. VGP2 Voltage Time Response</fc>*


\



|image13|

.. container:: center

   *<fc #000000>Figure 15. VG1 Voltage Time Response</fc>*


\



|image14|

.. container:: center

   *<fc #000000>Figure 16. VG2 Voltage Time Response</fc>*


\



|image15|

.. container:: center

   *<fc #000000>Figure 17. VGC1 Voltage Time Response</fc>*


\



|image16|

.. container:: center

   *<fc #000000>Figure 18. VGP1 Voltage Time Response</fc>*


.. note::

   Note that the capacitor value used in the feedback loop of the transimpedance amplifier is 100 pF. The relationship between speed and oscillation ripple is inversely proportional. We can achieve a faster settling time but must sacrifice a much cleaner oscillation, and vice versa.


-  We are done capturing the voltage transition from power-up and power-down. Now, we will capture the time it takes from when the fault is detected until the DAC outputs the gate pinch-off voltage.
-  We have already gathered data from the fault protection circuit, LTC7000. When it detects a fault event, it sends a signal from LTC7000 to the MCU in approximately 1 microsecond. This value will then be added to the system power-down measurement and the time it takes for the MCU to process the fault flag up to the DAC command.\

|image17|

.. container:: center

   
   *<fc #000000>Figure 19. LTC7000 -> MCU GPIO Fault Flag Time </fc>*


-  Follow the following steps:
-  Place the positive terminal of the oscilloscope probe into the provided wire, as shown in the image below. Then connect the negative terminal of the oscilloscope probe to the GND of the board.\

|image18|

.. container:: center

   
   *<fc #000000>Figure 20. Fault Detection Time Measurement Setup</fc>*


-  Set the required oscilloscope settings.

   -  Trigger value: +1 V
   -  1 µs/div and 1 V/div

-  For this test, we will introduce an overvoltage fault. To do this, increase the voltage from the external power supply from +48 V to +56 V. This will cause a fault event since the preset threshold for an overvoltage is +55 V.
-  The oscilloscope will display a similar time response as shown below.\

|image19|

.. container:: center

   
   *<fc #000000>Figure 21. MCU Processing Time</fc>*


-  The overall time from LTC7000 fault detection up to the DAC pinch-off voltage is shown on Table 2 below.

--------------

Summary of Results
~~~~~~~~~~~~~~~~~~

System Power Up and System Power Down Summary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  The below table shows the summary of our time response test for each DAC. As shown below, we achieved the <5 µs time requirement.

+-----------------+-------------------------------+---------------------------+---------------------------+------------------------+--------------------------+
| Timing Response |                               |                           |                           |                        |                          |
+=================+===============================+===========================+===========================+========================+==========================+
| **Pin Name**    | **Description**               | **Pinch-off voltage (V)** | **Operating Voltage (V)** | **Power-up time (us)** | **Power-down time (µs)** |
+-----------------+-------------------------------+---------------------------+---------------------------+------------------------+--------------------------+
| VGC1            | A5M36TG140 LDMOS Carrier Gate | 0                         | +3.8                      | 2.09                   | 2.25                     |
+-----------------+-------------------------------+---------------------------+---------------------------+------------------------+--------------------------+
| VGP1            | A5M36TG140 LDMOS Peaking Gate | 0                         | +1.9                      | 1.65                   | 2.01                     |
+-----------------+-------------------------------+---------------------------+---------------------------+------------------------+--------------------------+
| VGC2            | A5M36TG140 GaN Carrier Gate   | -5                        | -2                        | 1.95                   | 2.05                     |
+-----------------+-------------------------------+---------------------------+---------------------------+------------------------+--------------------------+
| VGP2            | A5M36TG140 GaN Peaking Gate   | -5                        | -2.6                      | 1.73                   | 1.95                     |
+-----------------+-------------------------------+---------------------------+---------------------------+------------------------+--------------------------+
| VG1             | GTRB384608FC-V1 GaN Main Gate | -5                        | -2.75                     | 1.81                   | 2.00                     |
+-----------------+-------------------------------+---------------------------+---------------------------+------------------------+--------------------------+
| VG2             | GTRB384608FC-V1 GaN Peak Gate | -5                        | -2.75                     | 1.81                   | 2.00                     |
+-----------------+-------------------------------+---------------------------+---------------------------+------------------------+--------------------------+

.. container:: center

   \ *<fc #000000>Table 1. Gate Voltages Timing Response Summary</fc>*


-  Power-up time -> from pinch-off voltage to operating voltage.
-  Power-down time -> from operating voltage to pinch-off voltage.

| 
| === Fault Event Time Response Summary ===

-  The below table shows the summary of our time response test when a fault occurs. As shown below, we achieved the <10 µs time requirement.
-  The total time from fault detection up to the gate pinch-off is given by:

   -  Total time = Fault flag (µs) + MCU Processing time (µs) + RF switch time (µs) + highest power down time between VGC2, VGP2, VG1, VG2 (µs) + highest power down time between VGC1, VGP1
   -  Total time = 1.0898 µs + 3.7078 µs + 0.3 µs + 2.05 µs + 2.25 µs
   -  **Total time = 9.4 µs**

Fault flag time -> time it takes for the MCU to recognize that there is a fault signal coming from the LTC7000.

MCU processing time -> total time for MCU to process the fault flag signal up to commanding the DAC.

RF switch time -> total time for the RF switch to turn-off

Power-down time -> DAC output from operating voltage to pinch-off.

Total time -> time from fault detection to Vgg pinch-off

--------------

Miscellaneous Measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~

As per the customer's request, we are able to test and measure the DAC settling time from these specified voltage levels.

-  Pinch-off voltage: -7 V
-  Operating voltage: -1.2 V

Do note that the firmware loaded on the board doesn't include these measurements. You may request for a separate firmware, if necessary.

-7 V to -1.2 V DAC Settling Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The DAC output voltage settling time from -7 V pinch-off to -1.2 V is 2.31 µs. See the image below.


|image20|

.. container:: center

   *<fc #000000>Figure 22. -7 V to -1.2 V DAC Settling Time</fc>*


-1.2 V to -7 V DAC Settling Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The DAC output voltage settling time from -1.2 V pinch-off to -2 V is 2.31 µs. See the image below.


|image21|

.. container:: center

   *<fc #000000>Figure 23. -1.2 V to -7 V DAC Settling Time</fc>*


--------------

Additional Information and Useful Links
---------------------------------------

-  :adi:`AD-PAARRAY3552R-SL Product Page <AD-PAARRAY3552R-SL>`
-  :adi:`MAX32666 Product Page <MAX32666>`
-  :adi:`AD3552R Product Page <AD3552R>`
-  :adi:`LTC7000 Product Page <LTC7000>`

--------------

Design and Integration Files
----------------------------

.. admonition:: Download
   :class: download

   :adi:`AD-PAARRAY3552R-SL Design & Integration Files <AD-PAARRAY3552R-SL-designsupport.zip>`

   
   -  Schematics
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   


--------------

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/AD-PAARRAY3552R-SL>`__ to receive all these great benefits and more!


*End of Document*

.. |hw_top_label.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/hw_top_label.jpg
   :width: 800px
.. |LED.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/LED.jpg
   :width: 200px
.. |peripherals.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/peripherals.jpg
   :width: 200px
.. |switch.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/switch.jpg
   :width: 200px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/8t8r_signal_chain.jpg
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/hw_bottom.png
   :width: 350px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/hw_setup.jpg
   :width: 700px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/cli_default.jpg
   :width: 700px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgc2_pwr_up_time.png
   :width: 500px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgp2_pwr_up_time.png
   :width: 500px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vg1_vg2_pwr_up_time.png
   :width: 500px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vg1_vg2_pwr_up_time.png
   :width: 500px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgc1_pwr_up_time.png
   :width: 500px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgp1_pwr_up_time.png
   :width: 500px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgc2_pwr_dwn_time.png
   :width: 500px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgp2_pwr_dwn_time.png
   :width: 500px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vg1_vg2_pwr_dwn_time.png
   :width: 500px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vg1_vg2_pwr_dwn_time.png
   :width: 500px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgc1_pwr_dwn_time.png
   :width: 500px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgp1_pwr_dwn_time.png
   :width: 500px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/flag_time.png
   :width: 500px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/fault_setup.jpg
   :width: 500px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/mcu_time.png
   :width: 500px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/-7vto-1.2v.png
   :width: 500px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/-1.2vto-7v.png
   :width: 500px
