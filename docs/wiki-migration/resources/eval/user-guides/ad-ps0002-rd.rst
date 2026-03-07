AD-PS0002-RD Power Supply Reference Design
==========================================

This single-board reference design presents a fully integrated battery management system, developed using the latest power management technology from Analog Devices Inc. (ADI) for portable applications. The board consolidates a complete power solution for handheld and portable devices, utilizing the latest components from ADI’s power portfolio. It features the MAX77958 USB-C Power Delivery Controller for flexible input options, paired with the MAX77786 1S Battery Charger to manage charging from a single-cell lithium-ion battery. The MAX17300 provides advanced fuel gauging, battery protection, and authentication capabilities, ensuring safe and reliable operation.

To support diverse power requirements, the design includes the MAX77857 Buck-Boost Regulator and the MAX77542 Multi-Phase Buck Converter, enabling up to five individually configurable outputs. The design also integrates the MAX14727 for power path control. For backup power, the MAX38889 utilizes supercapacitor technology to maintain system operation during power interruptions and battery replacements. Additionally, the MAX14611 Logic-Level Translator ensures seamless communication between components operating at different voltage levels.

This compact and cohesive single-board implementation offers a clear advantage in delivering a robust, space-efficient, and scalable battery management solution, ideal for modern portable electronic systems.

.. image:: https://wiki.analog.com/_media/resources/power/ad-ps0002-rd/board_top.jpg
   :align: center
   :width: 600px

| 

Simplified Block diagram
------------------------

.. image:: https://wiki.analog.com/_media/resources/power/ad-ps0002-rd/block_diag.png
   :align: center

System Features
---------------

-  Power Supply Options: Supports both USB-C with Power Delivery and 12V DC input
-  Input Priority: USB-C takes precedence over DC input
-  Battery Type: Single-cell (1S) Lithium-Ion
-  Charging Current: Up to 5A, user-configurable via I²C
-  Battery Authentication: Ensures secure battery identification
-  Backup Power: Supercapacitor-supported battery backup with up to 2.5A maximum output
-  System Output: Integrated buck-boost converter and multi-phase buck converter
-  Programmable Outputs:

   -  Up to 4A per output
   -  Maximum 6A total in buck mode
   -  Up to 4A in boost mode

-  System Communication:

   -  Utilizes MAXUSB interface
   -  Supports I²C communication for system commands, battery state-of-charge (SoC), charging current, and more

Hardware Configuration
~~~~~~~~~~~~~~~~~~~~~~

|image1| |image2|

Pins, Jumper, Test Points
~~~~~~~~~~~~~~~~~~~~~~~~~

Jumper
^^^^^^

+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Jumper | Node/Function      | Default Connection | Function                                                                                                                                                             |
+========+====================+====================+======================================================================================================================================================================+
| P3     | CE                 | 1-2\*              | U6: to short CE pin with 5V                                                                                                                                          |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P4     | IN1, IN2, IN3, IN4 | 1-2\*              | U6: to connect input pins to 5V                                                                                                                                      |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P10    | VCC                | 1-2\*              | U14: to connect U14 (VCC, A0, A1, A2) to 1V8 supply                                                                                                                  |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P11    | EN                 | 1-2\*              | U11: to connect enable pin to BATT_P                                                                                                                                 |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P12    | VIN                | 1-2\*              | U9 and U10: connect Vin pins to BATTP/PP_VOUT                                                                                                                        |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P13    | VBUS, VSYS         | 1-2\*              | U2: connect SYS pin with 5V supply                                                                                                                                   |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P16    | QEXT               | 1-2\*              | U8                                                                                                                                                                   |
|        |                    |                    | 1-2: Enable QBEXT pin as PGOOD and disable external BATT to SYS FET circuit. 2-3: Connect 100kΩ pull-up for the external BATT to SYS FET circuit.                    |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P17    | EN                 | 1-2\*              | U3                                                                                                                                                                   |
|        |                    |                    | 1-2: Connects EN to VIN through a 510kΩ pullup resistor for standalone operation. 2-3: Connects EN to VIO. The converter is enabled when both VIN and VIO are valid. |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P18    | VL                 | 1-2\*              | U3                                                                                                                                                                   |
|        |                    |                    | 1-2: Connects VIO to VL. Allow VIO to be powered from VL without the need for a separate VIO supply.                                                                 |
|        |                    |                    | Not installed: Disconnects VIO from VL. VIO needs to be powered from either MAXUSB_INTERFACE# or an external VIO supply.                                             |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P19    | VSYS               | 1-2\*              | U5: Connects SYS pin (U5) to the Vsys (system)                                                                                                                       |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P20    | BATTSP             | 1-2\*              | U8                                                                                                                                                                   |
|        |                    |                    | 1-2: Connects BATSP to BATT                                                                                                                                          |
|        |                    |                    | 2-3: Connects BATSP directly to BATT_P                                                                                                                               |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P21    | VIO                | 1-2\*              | U1: Connects VIO to 5V supply                                                                                                                                        |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P22    | VIO1               | 1-2\*              | U2: Connects VIO1 to 1V8 supply                                                                                                                                      |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P23    | VIO2               | open               | U2: Connects VIO1 to 1V8 supply                                                                                                                                      |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P24    | VIO3               | open               | U3: Connects VIO pin to 1V8 supply                                                                                                                                   |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P26    | VIO8               | 1-2\*              | U8: Connects VIO8 to 1V8 supply                                                                                                                                      |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P27    | VIO4               | 1-2\*              | U4: Connects VIO4 to 1V8 supply                                                                                                                                      |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P29    | MFIO1,3,5,7        | 1-2\*              | U6: to short MFIO1,3,5,7 with 1V8                                                                                                                                    |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P30    | PP_VOUT, CHGIN     | 1-2\*              | U1 and U8: Connects PP_VOUT (U1) with CHGNIN (U2)                                                                                                                    |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P35    | VSYS, IN           | 1-2\*              | U3: Connects IN pin with the Vsys                                                                                                                                    |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P39    | VIN, RUN           | 1-2\*              | U9                                                                                                                                                                   |
|        |                    |                    | 1-2: Connects Vin pin to Run pin                                                                                                                                     |
|        |                    |                    | 2-3: Run pin shorted to PGND                                                                                                                                         |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P40    | VIN, RUN           | 1-2\*              | U10                                                                                                                                                                  |
|        |                    |                    | 1-2: Connects Vin pin to Run pin                                                                                                                                     |
|        |                    |                    | 2-3: Run pin shorted to PGND                                                                                                                                         |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P47    | VIN_U14            | 1-2\*              | U14                                                                                                                                                                  |
|        |                    |                    | 1-2: Connects Vin_14 pin to VIO9                                                                                                                                     |
|        |                    |                    | 2-3: Connects Vin_14 pin shorted to PGND                                                                                                                             |
+--------+--------------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Jumpersolder
^^^^^^^^^^^^

+--------------------+---------------+--------------------+---------------------------------------------------------------+
| Jumpersolder       | Node/Function | Default Connection | Function                                                      |
+====================+===============+====================+===============================================================+
| P5                 | EN_N          | open               | U1: Short to set pin high                                     |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P6                 | PCON          | open               | U1: Short to set pin high                                     |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P7                 | OTG_ENA       | open               | U1: Short to set pin high                                     |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P8                 | OTG_EB        | open               | U1: Short to set pin high                                     |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P9                 | ZVC           | open               | U4: Short to connect pin to GND                               |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P25                | SUSPND        | open               | U8: Short to set pin high                                     |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P28                | FB, SGND      | open               | For 1V8 output setting (with P38 open)                        |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P31, P32, P33, P34 | LX, VSYS      | open               | U8: Short for additional capacitors at LX pin                 |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P36                | DISQBAT       | open               | U8: Short to set pin high                                     |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P37                | STAT          | open               | U8: LED Low-Side Driver Output for Indicating Charging Status |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P38                | FB, SGND      | open               | For 5V output setting (with P28 open)                         |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P41                | INTVCC, PGOOD | short              | For resistor value setting                                    |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P42                | INTVCC, PGOOD | open               | For resistor value setting                                    |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P43                | FB, SGND      | open               | For 1V8 output setting (with P44 open)                        |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P44                | FB, SGND      | short              | For 5V output setting (with P43 open)                         |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P45                | INTVCC, PGOOD | short              | For resistor value setting                                    |
+--------------------+---------------+--------------------+---------------------------------------------------------------+
| P46                | INTVCC, PGOOD | open               | For resistor value setting                                    |
+--------------------+---------------+--------------------+---------------------------------------------------------------+

Test Points
^^^^^^^^^^^

==================== ===========
Test Point           Description
==================== ===========
U4 - MAX17300        
TP31                 SCL/OD
TP20                 SDA/DQ
TP6                  CHG
TP30                 BATT_P
TP32                 DIS
U2 - MAX77958        
TP1                  GPIO0
TP9                  GPIO1
TP10                 GPIO2
TP11                 GPIO3
TP12                 GPIO4
TP13                 GPIO5
TP19                 GPIO6
TP17                 GPIO7
TP18                 GPIO8
P14 - LTPA Connector 
TP1                  W1
U6 - MAX77542        
TP23                 MFIO2
TP25                 MFIO4
TP27                 MFIO6
TP29                 MFIO8
==================== ===========

Featured ADI Devices
--------------------

.. image:: https://wiki.analog.com/_media/resources/power/ad-ps0002-rd/block_diag.png

Power Prioritization and Protection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`MAX14727 <en/products/max14727.html>` functions as both a power prioritizer and protector on the board. It automatically selects USB-C (Channel A) as the preferred input over 12V DC (Channel B), while protecting the system from overvoltage conditions (up to +28V) and surge events (up to 100V). It also prevents reverse current, supports OTG functionality, and includes adjustable overvoltage thresholds and thermal shutdown for enhanced system reliability.

USB-C PD Controller
~~~~~~~~~~~~~~~~~~~

The :adi:`MAX77958 <en/products/max77958.html>` serves as the USB-C Power Delivery (PD) controller on the board. It handles USB-C CC detection, PD negotiation, overvoltage/overcurrent protection, and moisture detection. It also supports legacy USB standards, OTG, and alternate mode configuration. With built-in I²C master capability, it can autonomously configure related devices without host intervention.

1S Battery Charger
~~~~~~~~~~~~~~~~~~

The :adi:`MAX77786 <en/products/max77786.html>` is the board’s main battery charger, supporting fast charging up to 5.5A with Smart Power Selector™. It enables efficient charging, reverse boost operation, and supports various battery chemistries. The charger is highly configurable via I²C and includes features like BC1.2 detection, load disconnection, and dead battery startup.

Battery Backup
~~~~~~~~~~~~~~

The :adi:`MAX38889 <en/products/max38889.html>` manages supercapacitor-based backup power for the board. It charges the storage element when input power is available and seamlessly boosts its voltage to maintain system operation during power loss or battery swaps. It supports up to 3A peak current and is configurable for various backup voltage and current settings.

Fuel Gauge & Battery Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`MAX17300 <en/products/max17300.html>` is a low-power, pack-side fuel gauge and SHA-256 battery authenticator for 1-cell Li-ion/polymer batteries. It uses the ModelGauge m5 algorithm, combining coulomb counting and voltage-based measurements for highly accurate state-of-charge (SOC) reporting. The device also supports dynamic power reporting, providing real-time estimates of the maximum power the battery can safely deliver. Communication and configuration are handled via an I²C interface for secure and intelligent battery management.

5V Output Regulator
~~~~~~~~~~~~~~~~~~~

The :adi:`MAX77857 <en/products/max77857.html>` is a high-efficiency buck-boost converter used to provide a regulated 5V output on the board. It supports a wide input voltage range of 2.5V to 16V, delivering up to 6A in buck mode and 4A in boost mode, with optional I²C control for dynamic voltage adjustment.

Multi-Rail Power Supply
~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`MAX77542 <en/products/max77542.html>` is a high-efficiency step-down converter used to generate key output rails—3.3V, 1.8V, 1.2V, and 0.9V—on the board. It supports a wide input voltage range from 2.8V to 16V, making it suitable for USB PD and Li-ion battery sources. Output voltages are preset via resistors and adjustable through I²C from 0.3V to 5V.

System setup
------------

.. image:: https://wiki.analog.com/_media/resources/power/ad-ps0002-rd/system_overview.svg
   :align: center

Equipment Needed
~~~~~~~~~~~~~~~~

-  AD-PS0002-RD
-  MAXUSB Interface
-  USB-C cable/12V power jack
-  18650 battery
-  PC with GUI

| To be added soon:
| \*Step-by-step instructions on how to connect the boards, power-up, how to run measurements
| \*Sample measurements or readings that users are expected to get when they use the board

Resources
---------

\*\* ADI Parts \*\*

-  :adi:`max77958.html <en/products/max77958.html>`
-  :adi:`max77786.html <en/products/max77786.html>`
-  :adi:`max17300.html <en/products/max17300.html>`
-  :adi:`max77857.html <en/products/max77857.html>`
-  :adi:`max77542.html <en/products/max77542.html>`
-  :adi:`max14727.html <en/products/max14727.html>`
-  :adi:`max38889.html <en/products/max38889.html>`
-  :adi:`max14611.html <en/products/max14611.html>`

Support
-------

Analog Devices will provide **limited** online support for anyone using the reference design with Analog Devices components via the :ez:`Power Management` forum.

It should be noted, that the older the tools' versions and release branches are, the lower the chances to receive support from ADI engineers.

.. |image1| image:: https://wiki.analog.com/_media/resources/power/ad-ps0002-rd/front.svg
.. |image2| image:: https://wiki.analog.com/_media/resources/power/ad-ps0002-rd/back.svg
