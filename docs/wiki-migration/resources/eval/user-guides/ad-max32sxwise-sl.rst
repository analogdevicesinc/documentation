AD-MAX32SXWISE-SL: Long Range Wireless Radio Development Kit based on MAX32670 MCU and SX1261 RF Transceiver
============================================================================================================

|

.. important::

   **Notice:** This page has been fully migrated to GitHub.io and is no longer maintained on the Wiki. Please refer to the GitHub link below for the most current and accurate information.

   | https://analogdevicesinc.github.io/documentation/solutions/reference-designs/ad-max32sxwise-sl/index.html
   | If you would like to contribute updates to this document, please submit your suggestions via a Pull Request on the GitHub page.
   | Thank you for your understanding, and we apologize for any inconvenience this transition may cause.
   


.. admonition:: Download
   :class: download

   `Ultra-low Power Wireless IoT Sensor (Brochure) <https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/ultra-low_power_wireless_iot_sensor_brochure_.pdf>`__


Overview
--------

The :adi:`AD-MAX32SXWISE-SL` development kit is a tool intended for designing solutions based on low-power, long range proprietary radio communication technique. This platform features the SX1261 RF transceiver based on spread spectrum modulation techniques derived from chirp spread spectrum (CSS) technology, and supports a frequency range from 800 MHz to 960 MHz. This solution is also based on the MAX32670 ultralow power microcontroller based on Arm Cortex-M4 processor.

| The kit is composed of a development board and equipped with sensor modules, providing users with a complete system that is suitable for quick prototyping and development of IoT applications. The design includes a gateway, which is crucial for establishing connectivity between the LPWAN devices and the backend or application server. This component is vital for data transfer and communication.
| This also comes with software that allows users to observe nodes in a graphical user interface (GUI) dashboard. This feature enhances the monitoring and management capabilities of the system. To use the development board, users need to flash it with functional firmware. A simple join example has been open-sourced, providing more flexibility and easy customization in terms of firmware development.
| Overall, the :adi:`AD-MAX32SXWISE-SL` development kit offers a comprehensive and user-friendly solution for individuals or developers interested in exploring and implementing LPWAN technology for IoT applications.
| ==== Features ====

-  Provides the user with a platform to evaluate the features and performance of the evaluation kit.
-  Allows the user to prototype and test their IoT applications before moving on to full-scale development.
-  Provides tools for analyzing the power consumption of the device, helping the user to optimize their applications for energy efficiency.
-  Includes development tools, libraries, and documentation to assist user in writing and debugging their code.
-  Helps the user analyze and study the different modulation schemes, data rates, and other parameters relevant to IoT communication.
-  Comes with user-friendly interfaces, documentation, and software tools that simplify the integration process which can save developers time and effort when incorporating the SX1261 into their IoT devices.

| 
| ==== Applications ====

-  Battery-Powered Medical Devices
-  Industrial Sensors
-  Optical Communication Modules
-  Secure Radio Modem Controller
-  Smart Sensor Controller
-  System Housekeeping Controller

| 
| ===== What's Inside the Box? ===== Upon purchase of the AD-MAX32SXWISE-SL kit, the package comes with the following boards and accessories: |image1|

| 
| ===== System Architecture =====
| |image2|

| 
| ===== Specifications =====

.. container:: center box

   
   +------------------------------------------------------------------------------------------------------------------+


   
   | MCU                                                                                                              |

   +==================================================================================================================+

   | Arm Cortex-M4 Core with FPU up to 100 MHz                                                                        |

   +------------------------------------------------------------------------------------------------------------------+

   | 384 kB Flash Memory with error correction                                                                        |

   +------------------------------------------------------------------------------------------------------------------+

   | 160 kB SRAM (128 KB with ECC enabled), optionally preserved in lowest power modes                                |

   +------------------------------------------------------------------------------------------------------------------+

   | Security                                                                                                         |

   +------------------------------------------------------------------------------------------------------------------+

   | Available secure boot                                                                                            |

   +------------------------------------------------------------------------------------------------------------------+

   | Support cryptographic algorithms, including AES-128/192/256, 1024-bit DSA, 2048-bit (CRT) and secure boot loader |

   +------------------------------------------------------------------------------------------------------------------+

   | Power                                                                                                            |

   +------------------------------------------------------------------------------------------------------------------+

   | Ultralow Power Real Time Clock (RTC) with integrated power switch                                                |

   +------------------------------------------------------------------------------------------------------------------+

   | With 300 nA power consumption during sleep mode                                                                  |

   +------------------------------------------------------------------------------------------------------------------+

   | Long Range Radio                                                                                                 |

   +------------------------------------------------------------------------------------------------------------------+

   | Support FSK, GFSK, MSK, GMSK, and Long Range FHSS modulations                                                    |

   +------------------------------------------------------------------------------------------------------------------+

   | Programmable bit rate up to 62.5 kbps and 300 kbps                                                               |

   +------------------------------------------------------------------------------------------------------------------+

   | Support of all major sub-GHz ISM bands from 800 MHz to 960 MHz                                                   |

   +------------------------------------------------------------------------------------------------------------------+

   | High sensitivity: down to -148 dBm                                                                               |

   +------------------------------------------------------------------------------------------------------------------+
   


| 
| ----

Components
==========

When you purchase the :adi:`AD-MAX32SXWISE-SL` development kit, the package comes with the following boards and accessories:

-  Base Board:

   -  :adi:`MAX32670-SX-ARDZ` Base board

-  Component Sensor Nodes:

   -  :adi:`EV-STRUCTURAL-ARDZ` for Structural Monitoring
   -  :adi:`EV-FLOWMETER-ARDZ` for Flow Rate Metering
   -  :adi:`EV-ADE9000SHIELDZ` for Electric Metering

-  Gateway Concentrator

   -  RAK5146 PiHAT Kit
   -  Raspberry Pi 4 Model B with Power Supply Adapter

-  MAX32625PICO Programming Adapter
-  Micro SD Card
-  LAN Cable

| 
| <fc #6495ed>\ **What is a Base Board?**\ </fc>
| A Base Board contains an RF transceiver chip and a microcontroller, which combine all the required elements for long range communication. This platform uses the chirp spread spectrum technique, allowing sensors to connect to a network and send and receive data in long distances.
| ==== MAX32670-SX-ARDZ Base Board ==== This development kit comes with the :adi:`MAX32670-SX-ARDZ` as its base board. This board is consisting of the MAX32670 high-reliability, ultralow power microcontroller based on Arm Cortex-M4 processor, and the SX1261 long range transceiver module.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/max32670-sx-ardz_base_board.png
   :align: center
   :width: 600px

| 

| <fc #6495ed>\ **What are Sensor Nodes?**\ </fc>
| Sensor nodes are devices that wirelessly send or receive messages to and back from the gateways. These devices communicate with nearby gateways connected through a network server. Depending on the intended applications, sensors can transmit various type of data such as temperature, flow rate, vibration, etc.
| Below are the sensor nodes compatible with the MAX32670-SX-ARDZ Base Board. All of these 3 sensors are included in the :adi:`AD-MAX32SXWISE-SL` development kit.

| 
| ==== EV-STRUCTURAL-ARDZ Sensor for Structural Monitoring ==== The :adi:`EV-STRUCTURAL-ARDZ` is a vibration sensor that uses the ADXL343 digital output MEMS accelerometer chip and the ADIS16203 programmable 360° inclinometer. Aside from providing vibration data, this end node also features the MAX30210 digital temperature sensor which gives the option to shut down sensitive machines and equipment for smart motor sensing applications. This vibration sensor can also detect if the horizontal position of the sensor changes, which points towards a collapse of the structure where the sensor was deployed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/ev-structural-ardz.png
   :align: center
   :width: 600px

| 
| ==== EV-FLOWMETER-ARDZ Sensor for Flow Rate Metering ==== The :adi:`EV-FLOWMETER-ARDZ` is an ultrasonic time-of-flight (ToF) flow meter that sends and receives ultrasound waves between piezoelectric transducers in both the upstream and downstream directions in the pipe. By measuring the TOF difference between the upstream and downstream wave travels, utilizing sophisticated digital signal processing techniques, a very accurate flow rate can be calculated.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-flowmeter-ardz_angle.png
   :align: center
   :width: 400px

| 
| ==== EV-ADE9000SHIELDZ Sensor for Electric Metering ==== The :adi:`EV-ADE9000SHIELDZ` is an Arduino shield compatible with Arduino Zero. The shield can be directly interfaced with current transformers and voltage leads. It enables quick evaluation and prototyping of energy and power quality measurement systems with the ADE9000. Arduino library and application examples are provided to simplify implementation of larger systems.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/ev-ade9000shieldz.png
   :align: center
   :width: 600px

--------------

System Setup
============

PHASE 1: Hardware Setup
-----------------------

Note that this setup only applies for MAX32670-SX-ARDZ Base Board. Users may use a different base board or microcontroller, however the firmware built for this demo application cannot be used as this is specifically designed for the MAX32670-SX-ARDZ.

| 
| ==== Equipment Needed ====

-  One (1) :adi:`MAX32670-SX-ARDZ` Base Board
-  One (1) Sensor Node (any of these: :adi:`EV-STRUCTURAL-ARDZ`, :adi:`EV-FLOWMETER-ARDZ`, :adi:`EV-ADE9000SHIELDZ`)
-  One (1) MAX32625PICO Rapid Development Platform with 10-pin ribbon cable

   -  with firmware image: :git-max32625pico-firmware-images:`MAX32625PICO Firmware Image for MAX32670 <raw/master/bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin>`

-  One (1) CR123A Battery or any equivalent external DC power supply (+3 V to +4.7 V)

::

      *** Note that this is not included in the kit**
   * One (1) Micro USB to USB cable
   * Host PC (Windows 10 or later)

| 
| |image3|

| 
| \* Insert one CR123A battery (3 V to 4.7 V) into the battery holder (BT1 connector) of the :adi:`MAX32670-SX-ARDZ` Base Board.

.. container:: center round box

   **Make sure to check for the battery polarity in the BT1 connector, refer to the figure below. The DS3 LED will light up indicating that you have inserted the battery correctly and that power is provided in the base board.**\


   |image4|

-  Connect one <fc #6495ed> **Sensor Node** </fc> to the :adi:`MAX32670-SX-ARDZ` Base Board by aligning the corresponding Arduino headers on each board.

.. tip::

   
   You do not have to set up the three sensor nodes altogether, just choose **one** from the available sensors in the kit:
   
   -  :adi:`EV-STRUCTURAL-ARDZ` for Structural Monitoring
   -  :adi:`EV-FLOWMETER-ARDZ` for Flow Rate Metering
   -  :adi:`EV-ADE9000SHIELDZ` for Electric Metering
   


-  Connect the :adi:`MAX32625PICO` programming adapter to the :adi:`MAX32670-SX-ARDZ` Base Board through the 10-pin ribbon cable.

.. container:: center round box

   
   **Make sure that the MAX32625PICO programming adapter has been flashed with the correct image before connecting it to the MAX32670-SX-ARDZ Base Board. If you do not know how to load the image, click on the instructions below:** 

.. raw:: html

   <details><summary>**How to flash the firmware image in the MAX32625PICO**</summary>

-   Download the firmware image: :git-max32625pico-firmware-images:`MAX32625PICO Firmware Image for MAX32670 <raw/master/bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin>`
   -   Do not connect the MAX32625PICO to the :adi:`MAX32670-SX-ARDZ` Base Board yet.
   -   Connect the MAX32625PICO to the Host PC using the micro USB to USB cable.
   -   Press the button on the MAX32625PICO. **(Do not release the button until the MAINTENANCE drive is mounted)**.\

   |image5|

   -   Release the button once the MAINTENANCE drive is mounted.
   -   Drag and drop (to the MAINTENANCE drive) the firmware image.
   -   After a few seconds, the MAINTENANCE drive will disappear and be replaced by a drive named DAPLINK. This indicates that the process is complete, and the MAX32625PICO can now be used to flash the firmware of the :adi:`MAX32670-SX-ARDZ` Base Board.

.. raw:: html

   </details>

   


-  Connect the :adi:`MAX32625PICO` programming adapter to the Host PC using the micro USB to USB cable.


   


|image6|

| 
|

.. note::

   
   **Once you have completed this setup, proceed to PHASE 2 found in**\ :doc:`ADI Long Range Wireless Radio Software User Guide </wiki-migration/resources/eval/user-guides/longrangewirelessradio/software>`.
   


| 
| ----

Resources
=========

-  :doc:`MAX32670-SX-ARDZ Base Board </wiki-migration/resources/eval/user-guides/max32670-sx-ardz>`

-  :doc:`EV-STRUCTURAL-ARDZ Sensor for Structural Monitoring </wiki-migration/resources/eval/user-guides/ev-structural-ardz>`

-  :doc:`EV-FLOWMETER-ARDZ Sensor for Flow Rate Metering </wiki-migration/resources/eval/user-guides/ev-flowmeter-ardz>`

-  :doc:`EV-ADE9000-SHIELDZ Sensor for Electric Metering </wiki-migration/resources/eval/user-guides/eval-ade9000shieldz/sensor_node/demo>`

| 
| ===== Design and Integration Files =====

.. admonition:: Download
   :class: download

   
   | `AD-MAX32SXWISE-SL Design Support Package <https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/ad-max32sxwise-sl-designsupport.zip>`__
   | \* Schematic
   
   -  Bill of Materials
   -  Layout
   -  Fabrication Files
   
   |


| ====== FAQs ======

.. container:: center round box

   **Q. Why is the serial application not responding after opening the port?**\ ​

   | A. It usually happens whenever the power of the base board is not enough to operate the board.
   | **Q. Can we use other gateways aside from ChirpStack?**
   | A. Customers are not limited to use ChirpStack gateway, it is possible to use other gateways available in the market.
   | **Q. What maximum number a gateway can handle?**
   | A. It depends on the channels available per assigned region and the time division set by the user on sending data from the nodes to gateway.
   | **Q. Is there another way to see the GUI without using the local setup?**
   | A. The GUI can also be accessed through cloud service, but it is not supported by ADI.
   | **Q. What is the maximum distance the gateway and nodes can communicate?**
   | A. The gateway and nodes' maximum and effective range may vary depending on the modulation parameters, transmit power, antenna gain, environmental conditions, and obstacles present in the communication path. In practice, it can reach several kilometers in rural areas with a clear line of sight. The effective range may be shorter in urban areas where obstacle and interference are present.


| ===== Help and Support ===== For questions and more information about this product, connect with us through the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone Support Community <reference-designs>`


| 

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/ad-max32sxwise-sl.png
   :width: 3000px
   :height: 2000px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/ad-max32sxwise-sl_block_diagram.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/hardware_setup.png
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/base_board_with_battery.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/max32625pico_maxdap.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/max32670-sx-ardz_to_maxpico.png
   :width: 1500px
