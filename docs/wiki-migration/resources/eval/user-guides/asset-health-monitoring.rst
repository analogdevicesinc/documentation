ASSET HEALTH MONITORING
=======================

The Asset Health Monitoring demo using ADXL372 accelerometer is designed for long-period monitoring |image1| of the physical condition of high-value assets.With its extremely low power capabilities, the ADXL372 micropower high-g MEMS accelerometer targets Internet of Things (IoT) solutions where shock and impact on a unit during storage, transit, or use would adversely affect its function, safety, or reliability. Representative assets include materials inside shipping and storage containers, factory machinery, and battery powered products where there may be lengthy quiet periods punctuated by spontaneous, severe impacts.

General Description
-------------------

The ultralow power MEMS sensor, :adi:`ADXL372 <media/en/technical-documentation/data-sheets/ADXL372.pdf>`, has an “instant on” feature and can wake up immediately to acquire the entire waveform, which significantly reduces standby power drain. The resulting low current requirement of less than two microamps while waiting for an impact typically yields years of operation from a single small battery when the sensor is used in a motion-activated system. By using the ADXL372 MEMS accelerometer as part of a remote edge-node device in an IoT application, transient events can be captured and categorized by a localized processor beforehand by being sent to the cloud or other data center via a wireless link. Keeping the analysis localized saves power, time, and prevents unnecessary transfer of data for an event that is actually insignificant.

The wide bandwidth of 3200 Hz and dynamic range of ±200 g make it an excellent fit for a diverse set of asset health-monitoring applications including monitoring of concussions for indication of Traumatic Brain Injury in both athletes and military personnel.

-  **Features of ADXL372**

   -  22 µA at 3200 Hz ODR, 2.5 V supply
   -  ±200 g measurement range
   -  200 Hz to 3200 Hz user selectable bandwidth with 4-pole antialiasing filter
   -  Wide supply range: 1.6 V to 3.5 V
   -  12-bit output at 100 mg/LSB scale factor
   -  Wide temperature range: −40°C to +105°C

Demo Setup
----------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/capture.png
   :align: center
   :width: 700px

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  Transmitter Node

      -  ADuCM4050 EZ-KIT
      -  Wireless Arduino Shield
      -  ADXL372
      -  ADF703x RF Daughter Board with antenna
      -  BLE-LINK Bluetooth 4.0 module

   -  Receiver Node

      -  ADuCM4050 EZ-KIT
      -  ADF703x RF Daughter Board with antenna
      -  Arduino LCD shield with LCD

-  Software

   -  Asset Health Monitoring Firmware

      -  Android Graph IoT App

Setting Up the Hardware
-----------------------

Transmitter node:-

-  To power up the node using USB cable , place the jumper on 3&4 of JP12.
-  Place the wireless arduino shield on the EZ-kit.
-  Place the RF module ADF703x on P1, P2,P3 connectors of the EZ kit and connect the antenna on the TX end
-  The following connections are required between ADXL372 and the arduino shield

   -  Short VS and VIO on ADXL

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adxl.png
   :align: center
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/capture2.png
   :align: center
   :width: 400px

Receiver node:-

-  To power up the node using USB cable , place the jumper on 3&4 of JP12.
-  Place the arduino LCD shield with LCD on the EZ-kit.
-  Place the RF module ADF703x on P1, P2,P3 connectors of the EZ kit and connect the antenna on the RX end

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/capture1.png
   :align: center
   :width: 400px

-  Following rework is required on the LCD shield such that the mcu could control the lcd.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/rework.jpg
   :align: center
   :width: 400px

Obtaining the source code
-------------------------

.. admonition:: Download
   :class: download

   
   The source code has to be inserted from the github
   
   |


Outputting Data
---------------

Once the above setup is ready, move the ADXL in either x,y or z direction. The following message is displayed on the LCD screen:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/output.png
   :align: center
   :width: 500px

Android Mobile app "Graph IOT" would display following graph:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/mobileapp.png
   :align: center
   :width: 500px

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adxl372-cmyk-1860x1860-title-print_webready.jpg
   :width: 250px
