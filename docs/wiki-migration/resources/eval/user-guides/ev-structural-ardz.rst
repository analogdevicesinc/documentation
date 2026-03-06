EV-STRUCTURAL-ARDZ Sensor for Structural Monitoring
===================================================

|

.. important::

   **Notice:** This page has been fully migrated to GitHub.io and is no longer maintained on the Wiki. Please refer to the GitHub link below for the most current and accurate information.

   | https://analogdevicesinc.github.io/documentation/solutions/reference-designs/ad-max32sxwise-sl/ev-structural-ardz/index.html
   | If you would like to contribute updates to this document, please submit your suggestions via a Pull Request on the GitHub page.
   | Thank you for your understanding, and we apologize for any inconvenience this transition may cause.
   


Overview
--------

The :adi:`EV-STRUCTURAL-ARDZ` is a vibration sensor that uses the :adi:`ADXL343` digital output MEMS accelerometer chip and the :adi:`ADIS16203` programmable 360° inclinometer. Aside from providing vibration data, this board also features the :adi:`MAX30210` digital temperature sensor which gives the option to shut down sensitive machines and equipment for smart motor sensing applications. This vibration sensor can also detect if the horizontal position of the sensor changes, which points towards a collapse of the structure where the sensor was deployed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/ev-structural-ardz.png
   :align: center
   :width: 650px

Features
~~~~~~~~

.. container:: box

   
   +----------------------------------------------------------------------------------------------------------------+


   
   | Temperature Sensor                                                                                             |

   +================================================================================================================+

   | ±0.1°C accuracy from +20°C to +50°C                                                                            |

   +----------------------------------------------------------------------------------------------------------------+

   | ±0.15°C accuracy from -20°C to +85°C                                                                           |

   +----------------------------------------------------------------------------------------------------------------+

   | High and low temperature alarms                                                                                |

   +----------------------------------------------------------------------------------------------------------------+

   | Accelerometer                                                                                                  |

   +----------------------------------------------------------------------------------------------------------------+

   | Built-in motion detection features make tap, double-tap, activity, inactivity, and free-fall detection trivial |

   +----------------------------------------------------------------------------------------------------------------+

   | Multipurpose accelerometer with 10- to 13-bit resolution for use in a wide variety of applications             |

   +----------------------------------------------------------------------------------------------------------------+

   | Inclinometer                                                                                                   |

   +----------------------------------------------------------------------------------------------------------------+

   | Digital self-test function                                                                                     |

   +----------------------------------------------------------------------------------------------------------------+

   | Configurable alarm function                                                                                    |

   +----------------------------------------------------------------------------------------------------------------+

   | ±180 output format option                                                                                      |

   +----------------------------------------------------------------------------------------------------------------+
   


| 
| ==== Applications ====

-  Smart motor sensor
-  Tilt sensing, inclinometers
-  Platform control, stabilization, and leveling
-  Motion/position measurement
-  Monitor/alarm devices (security, medical, safety)

| 
| ==== Block Diagram ====
| |image1|

| 
| ----

Hardware Design
===============

| 
| ===== Components and Connections =====

Digital Interface (Arduino)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: indent

   The Arduino interface is a standardized digital interface for various digital communication protocols such as SPI, I2C, and UART. These interface types were standardized by Arduino, which is hardware and software company. Complete details on the PMOD specification can be found `here <https://www.arduino.cc/en/hardware>`__.

   
   The pin map for the Arduino pins is described in the table and its schematic diagram below. |image2|


   
   |image3|

| 
| ==== Sensor Device ====

.. container:: indent

   The board comes with the :adi:`ADXL343` 3-Axis MEMS Accelerometers, :adi:`ADIS16203` Programmable 360° Inclinometer, and :adi:`MAX30210` ±0.1°C Accurate, 16-Bit Digital I2C Temperature Sensor.


   |image4|

--------------

Applications
============

|

.. tip::

   The :adi:`EV-STRUCTURAL-ARDZ` can be used with the :adi:`MAX32670-SX-ARDZ` Base Board, which is a long-range wireless radio development platform based on MAX32670 ultralow power ARM Cortex-M4 microcontroller and SX1261 RF transceiver.

   | Using these platforms together enables users to design solutions based on low-power, long range proprietary radio communication technique.
   | To learn more about the Long Range Wireless Radio solution developed by Analog Devices, visit the :doc:`AD-MAX32SXWISE-SL Long Range Wireless Radio Development Kit User Guide </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl>`
   


| 
| ====== System Setup ======

PHASE 1: Hardware Setup
-----------------------

Note that this setup only applies for MAX32670-SX-ARDZ Base Board. Users may use a different base board or microcontroller, however the firmware built for this demo application cannot be used as this is specifically designed for the MAX32670-SX-ARDZ.

| 
| ==== Equipment Needed ====

-  One (1) :adi:`MAX32670-SX-ARDZ` Base Board
-  One (1) :adi:`EV-STRUCTURAL-ARDZ` Sensor Node
-  One (1) MAX32625PICO Rapid Development Platform with 10-pin ribbon cable

   -  with firmware image: :git-max32625pico-firmware-images:`MAX32625PICO Firmware Image for MAX32670 <raw/master/bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin>`

-  One (1) CR123A Battery or any equivalent external DC power supply (+3 V to +4.7 V)

::

      *** Note that this is not included in the kit**
   * One (1) Micro USB to USB cable
   * Host PC (Windows 10 or later)

| 
| |image5|

| 
| \* Insert one CR123A battery (3 V to 4.7 V) into the battery holder (BT1 connector) of the :adi:`MAX32670-SX-ARDZ` Base Board.

.. container:: center round box

   **Make sure to check for the battery polarity in the BT1 connector, refer to the figure below. The DS3 LED will light up indicating that you have inserted the battery correctly and that power is provided in the base board.**\


   |image6|

-  Connect the :adi:`EV-STRUCTURAL-ARDZ` Sensor Node to the :adi:`MAX32670-SX-ARDZ` Base Board by aligning the corresponding Arduino headers on each board.
-  Connect the :adi:`MAX32625PICO` programming adapter to the :adi:`MAX32670-SX-ARDZ` Base Board through the 10-pin ribbon cable.

.. container:: center round box

   
   **Make sure that the MAX32625PICO programming adapter has been flashed with the correct image before connecting it to the MAX32670-SX-ARDZ Base Board. If you do not know how to load the image, click on the instructions below:** 

.. raw:: html

   <details><summary>**How to flash the firmware image in the MAX32625PICO**</summary>

-   Download the firmware image: :git-max32625pico-firmware-images:`MAX32625PICO Firmware Image for MAX32670 <raw/master/bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin>`
   -   Do not connect the MAX32625PICO to the :adi:`MAX32670-SX-ARDZ` Base Board yet.
   -   Connect the MAX32625PICO to the Host PC using the micro USB to USB cable.
   -   Press the button on the MAX32625PICO. **(Do not release the button until the MAINTENANCE drive is mounted)**.\

   |image7|

   -   Release the button once the MAINTENANCE drive is mounted.
   -   Drag and drop (to the MAINTENANCE drive) the firmware image.
   -   After a few seconds, the MAINTENANCE drive will disappear and be replaced by a drive named DAPLINK. This indicates that the process is complete, and the MAX32625PICO can now be used to flash the firmware of the :adi:`MAX32670-SX-ARDZ` Base Board.

.. raw:: html

   </details>

   


-  Connect the :adi:`MAX32625PICO` programming adapter to the Host PC using the micro USB to USB cable.


   


|image8|

| 
|

.. note::

   
   **Once you have completed this setup, proceed to PHASE 2 found in**\ :doc:`ADI Long Range Wireless Radio Software User Guide </wiki-migration/resources/eval/user-guides/longrangewirelessradio/software>`.
   


--------------

Resources
=========

-  :adi:`ADIS16203 Product Page <ADIS16203>`
-  :adi:`MAX30210 Product Page <MAX30210>`
-  :adi:`ADXL343 Product Page <ADXL343>`

| 
| ===== Design and Integration Files =====

.. admonition:: Download
   :class: download

   
   | `EV-STRUCTURAL-ARDZ Design Support Package <https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/ev-structural-ardz-designsupport.zip>`__
   | **REV. B**
   
   -  Schematic
   -  Bill of Materials
   -  Layout
   -  Fabrication Files
   


Help and Support
----------------

For questions and more information about this product, connect with us through the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone Support Community <reference-designs>`


| 

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/ev-structural-ardz_block_diagram.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/ev-structural-ardz_revb.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/hardware/sms/arduino_interface.png
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/ev-structural-ardz_revb2.png
   :width: 800px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/hardware_setup.png
   :width: 800px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/base_board_with_battery.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/max32625pico_maxdap.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/max32670-sx-ardz_to_maxpico.png
   :width: 1500px
