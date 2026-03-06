AMR Current Sensing Hardware User Guide
=======================================

Features
========

-  500A DC and AC
   \* <1mArms Noise
   \* <1% Error in Clamp Center
   \* <1% Positional Sensitivity within Clamp
   \* More than 40dB Rejection to Stray Fields
   \* Negligible Hysteresis
   \* 28mm Wire Opening

Hardware Required
=================

-  Castor Sensor Board
   \* Gemini Acquisition Board
   \* 5V Wall Adapter

.. container:: centeralign

   \ |image1|\ *Figure 1. Gemini and Castor System*


General Description
===================

This user guide describes the hardware functionality of the AMR Array Based Contactless Current Sensing System. The AMR contactless current sensing system comprised of the Gemini acquisition board and Castor sensor board shown in Figure 1. The coreless AMR array architecture ensures negligible hysteresis in an ultrathin form factor (PCB + 1mm sensor height). It is constructed using standard PCB manufacturing processes. The system is capable of measuring ±500A DC and 500A AC TrueRMS up to 1kHz signals with a typical error of <1%. It features a high dynamic range with <1mArms noise. The system can be powered by a 5V wall adapter or alternately by battery. It will run stand-alone with the LCD display or there is an optional PC GUI available for visualizing the data collected.

System Description
==================

| The AMR Array Based Contactless Current Sensing System measures the current flowing in a wire by sensing the magnetic field induced from the wire inside the clamp. An array of ADAF1080 magnetic field sensors is used to significantly reduce the effects of stray field and positional uncertainty. This approach also results in minimal hysteresis, high dynamic range, excellent performance over temperature, and a thin clamp form factor.
| The ADAF1080 is an integrated ±8mT AMR field sensor and conditioner. It is capable of bandwidths up to 2MHz, though for this clamp design the firmware is targeted at a much lower frequency range.
| The array of sensors is conditioned to a single output via an ADA4807-1 amplifier, which also acts as the ADC driver and a 5kHz, double pole, multiple feedback low-pass filter.
| The ADA4807-1 output is sampled by the AD7988-1, a 16-bit, 100ksps, SAR ADC, and the data is captured and processed on an ADuCM4050 Cortex M4 MCU. The DC Current, AC Current and Frequency are calculated and displayed on the LCD along with the temperature.
| The data can also be visualized in a PC GUI for further analysis.
| The system is typically powered by either a 5V wall adapter or battery. See Power Supply in the Gemini Acquisition Board section for more details on either powering the board by battery or alternately by USB for demonstration purposes.

System Performance
------------------

======================= ======================== ======= =====
Parameter               Test Conditions/Comments Value   Unit
======================= ======================== ======= =====
Range                                                    
DC                      Clamp Center             ±500    A
AC                      Clamp Center;            500     Arms
:::                     1.42 Crest Factor        :::     :::
Frequency               -                        15 - 1k Hz
\                                                        
Noise                   10A input                0.9     mArms
\                                                        
Accuracy                Clamp Center             1       %
Orientation Variation                            ±25     mA
Temperature Variation                            0.05    %/°C
Positional Sensitivity                           1       %
Interference Rejection  (>99% Attenuation)       -40     dB
\                                                        
Measurement Update Rate                          4       Hz
Measurement Settling                             2       s
======================= ======================== ======= =====

|

.. important::

   The Frequency, Measurement Update Rate and Settling are limited primarily by the firmware's configuration settings.

   | The Orientation variation specified at ±25 mA is due to rejection of earth's magnetic field. Performing a null will remove this error source for that specific orientation.
   


Castor Sensor Board
===================

| |image2|

.. container:: centeralign

   Figure 2. Castor Sensor Board


The Castor board performs the sensing portion of the AMR Array Based Contactless Current Sensing System. The 28mm wire opening easily accommodates up to a 600kcmil wire. The jaw is also only 12.5mm wide and <2.5mm thick.



| All the signals required to operate the Castor board are provided from the Gemini board through the connectors P1 and P2. This includes signals for ADAF1080 flipping, calibration, gain selection as well as all power supplies required.
|

.. container:: centeralign

   \ |image3|\ *Figure 3. Castor Main Board Components*


The sensor array utilizes 16 ADAF1080 integrated ±8mT AMR field sensors and conditioners. Depending on the form factor and performance requirements, less than 16 sensors is also feasible for a design.
| The ADAF1080 provides minimal hysteresis as well as negligible offset due to its sensor flipping functionality. It also provides excellent performance over temperature and high dynamic range. See Table 1 for specifications.
| The array of sensors is conditioned and aggregated to a single output via an ADA4807-1 amplifier. This also acts as the ADC driver, provides an additional gain of 8, and acts as a 5kHz, double pole, multiple feedback low-pass filter. The ADA4807-1’s low noise of 3.1 nV/√Hz introduces minimal noise into the acquisition signal chain. The analog output of the ADA4807-1 is connected to the connectors going to the Gemini board for acquisition.
| The Castor board is capable of bandwidths up to 2MHz, though for the Castor + Gemini system, the hardware filters and firmware are targeted at a much lower frequency range. See Table 1. It is possible to modify the Castor board filters to run at much higher frequencies and work as a standalone solution with an analog output signal without needing the Gemini board. Contact Analog Devices if this is of significant interest.

|

.. important::

   It is possible to modify the Castor board filters to run at much higher frequencies and work as a standalone solution with an analog output signal without needing the Gemini board.


   | Contact Analog Devices if this is of significant interest.


Plastic Spacers
---------------

|

.. container:: centeralign

   \ |image4|\ *Figure 4. Castor Board Assembly*


Two plastic spacers are provided as shown in Figure 4. These ensure the correct spacing and alignment of the sensor ring. In an end system this alignment would be handled by the mechanical housing.
|

.. warning::

   If the spacers are not used, the alignment may be significantly off which would appear in the results as degraded positional uncertainty and stray field rejection near the clamp opening.


Hardware Link Options
---------------------

.. container:: centeralign

   \ |image5|\ *Figure 5. Castor Jumpers*


The function of the link options is described in the table below. When the user first receives the board, the default link setting on the board are shown in Figure 5.

+---------+--------------+-------------------------------------------------------------------+
| Link    | Default      | Purpose                                                           |
+=========+==============+===================================================================+
| JP1     | A            | Summing Amplifier Voltage Supply                                  |
+---------+--------------+-------------------------------------------------------------------+
| JP4     | A            | ADAF1080 Sensor Vout or VTemp connection to the acquisition board |
+---------+--------------+-------------------------------------------------------------------+
| :::     | :::          | A; Vout                                                           |
+---------+--------------+-------------------------------------------------------------------+
| :::     | :::          | B; Vtemp                                                          |
+---------+--------------+-------------------------------------------------------------------+
| JP3,JP5 | Not inserted | Default: ADAF1080 Gain control via Firmware                       |
+---------+--------------+-------------------------------------------------------------------+
| :::     | :::          | JP3:B; JP5: A; sets ADAF1080s' Gain to 20                         |
+---------+--------------+-------------------------------------------------------------------+
| :::     | :::          | JP3:A; JP5: B; sets ADAF1080s' Gain to 40                         |
+---------+--------------+-------------------------------------------------------------------+
| :::     | :::          | JP3:B; JP5: B; sets ADAF1080s' Gain to 80                         |
+---------+--------------+-------------------------------------------------------------------+
| JP7     | Not inserted | Inserted; Pulls the SYNC EN to Vs                                 |
+---------+--------------+-------------------------------------------------------------------+
| :::     | :::          | Not inserted: Grounds the SYNC EN through a 100k resistor         |
+---------+--------------+-------------------------------------------------------------------+

Gemini Acquisition Board
========================

|image6|

.. container:: centeralign

   Figure 6. Gemini Acquisition Board


Board Description
-----------------

|

.. container:: centeralign

   \ |image7|\ *Figure 7. Gemini Main Board Components*


The Gemini board forms the acquisition portion of the AMR Array Based Contactless Current Sensing System. It performs the data acquisition and processing and can output the data to the onboard LCD display as well as a PC GUI via USB. The board also provides all the power supply generation and conditioning for the system.
| For data acquisition, the board features the AD7988-1, a 16-bit, 100ksps, SAR ADC. Oversampling the AD7988-1 provides a cost effective, high dynamic range, signal acquisition solution. The ADC connects to the MCU via SPI, which runs the ADC at 10ksps by default.
| The MCU is an ADuCM4050, which features a Cortex M4 controller with 512k flash. The Gemini firmware comes pre-installed on the board and performs all required measurement controls, calibration, and communication via the LCD and USB. It also provides a temperature reading with the onboard ADT7420, ±0.20°C accurate temperature sensor.

Power Supply Options
--------------------

| The board can be supplied by either a 5V wall adapter, battery, or USB. Here is a description of using each of the power options.
| **5V Wall Adapter**; This is the default power option and corresponds to the default jumper positions. The VER05US050-JA from XP POWER wall adapter was used during development, but other brands of adapters should work fine as well.
| **Battery**; A Li-Ion battery, such as the MicroElektronika MIKROE-1120 2Ah, may be connected to P6, labeled “Battery Connector” in Figure 7. To power the board from the battery, refer to Table 3 to slide S2 to the right position. The battery may be charged via the USB port and onboard battery charging circuitry utilizing the LTC4095.
| **USB**; This is only recommended for simple demonstration and not intended for performance evaluation due to high noise on some USB supplies. To use this mode, slide JP3 in left position. Refer to Table 3 for jumpers and switch positions.

.. _hardware-link-options-1:

Hardware Link Options
---------------------

The functions of the link options are described in the table below. Position A of the jumper link corresponds to a “1” on the silkscreen and Position B corresponds to a “3” on the silkscreen.

+------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link | Default       | Purpose                                                                                                                                                 |
+======+===============+=========================================================================================================================================================+
| JP2  | A             | Flip Current Supply independent from Vs Supply                                                                                                          |
+------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::  | :::           | A: Independent; Flip Supply of 5V, Vs supply of 4.6V from LDO                                                                                           |
+------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::  | :::           | B: Flip Supply and Vs Supply are 5V.                                                                                                                    |
+------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| S2   | Left Position | Power Source for the Board                                                                                                                              |
+------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::  | :::           | Left Position: The 5V wall adapter or USB                                                                                                               |
+------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::  | :::           | Right Position: A battery connected to P6 (Underneath the board)                                                                                        |
+------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| JP3  | A             | AD7988-1's reference is from the Vs supply of the ADAF1080, resulting in ratiometric measurement                                                        |
+------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::  | :::           | A: The reference is supplied from a 10uF decoupling capacitor.                                                                                          |
+------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::  | :::           | B: The reference is buffered by an ADA4807. This may be required if the AD7988-1's sampling rate were to be increased from the standard 10kps operation |
+------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

LEDs and Buttons
----------------

.. container:: centeralign

   \ |image8|\ *Figure 8. Buttons and LEDs*


============ ====== ===========================================
LED          Color  When Illuminated
============ ====== ===========================================
DS1          Green  Not Used
DS2          Blue   Not Used
DS3(3V3)     Green  +3.3V Supply ON
DS4(USB)     Yellow USB Connected
:::          :::    Flashes during transfer
DS5(Battery) Green  Attempting to Charge Battery
:::          :::    Flashing Indicated Battery Fault
DS6(PWR)     Red    Power-off or Board Supply out of Regulation
============ ====== ===========================================

Typical Performance Plots
-------------------------

TEST CONDITIONS
---------------

The following Equipment was used for testing;

-  Gemini and Castor Hardware
-  Plastic Spacers inserted on the Castor board
-  The KTPS05-05015U-VI-P1 wall supply from Kaga Electronics USA
-  Fluke 5500A Calibrator as the input current source
-  Fluke 5500A/Coil 50-Turn Current Coil

As per the default configuration, the system had been calibrated at 50Adc. A Null was performed with nothing in clamp (0A). The system was connected via USB cable to the PC GUI Software for analysis and data capture.

Noise, Linearity, and Frequency Response
----------------------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/gemini9.jpg
   :align: center
   :width: 900px

Stray Field and Position Uncertainty
------------------------------------

| Figure 13 through to Figure 16 show the positional uncertainty and stray field rejection performance. |image9|
| **Positional Uncertainty**
| Positional uncertainty is the % error induced from misalignment of the wire within the clamps jaw. Figure 13 shows measurement results for the positional uncertainly with an 8mm coil manually moved around the interior extent of the clamp jaw over a 100 second time period. Worst case reported error is <0.3%. This correlates to the simulated results in Figure 14.
| **Stray Field Rejection**
| Stray field rejection is the induced error as a % of a stray current. Figure 15 shows measurement results from a stray field from an 8mm wire coil carrying 10A of DC current. The coil is manually moved around the clamps outer edge. Worst case induced error from the stray field source is <0.3% which corresponds to >50dB rejection. This correlates to the simulated results in Figure 16.

Other Information
-----------------

-  `Main Page <:doc:`/wiki-migration/resources/eval/ev-adaf1080-16ebz`>`__
-  `Quick Start Guide <:doc:`/wiki-migration/resources/eval/ev-adaf1080-16ebz/quick-start`>`__
-  `Software User Guide <:doc:`/wiki-migration/resources/eval/ev-adaf1080-16ebz/sw-ug`>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/ev-adaf1080-16ebz_kit_top2a.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/castorangle.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/castormainboard_components.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/castorplasticspacers.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/castorpinheader.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/gemini_angle-web.jpg
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/geminicomponents.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/geminibuttonsandleds.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/gemini10.jpg
