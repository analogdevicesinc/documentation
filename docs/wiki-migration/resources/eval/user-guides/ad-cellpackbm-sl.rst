AD-CELLPACKBM-SL User Guide
===========================

|

.. important::

   We are in the process of migrating our documentation to GitHub.io.

   | The latest version of this page can be found at https://analogdevicesinc.github.io/documentation/solutions/reference-designs/ad-cellpackbm-sl/index.html


.. admonition:: Download
   :class: download

   A concise version of this document is available in portable document format: `AD-CELLPACKBM-SL Quick Start Guide <https://wiki.analog.com/_media/resources/eval/user-guides/ad-cellpackbm-sl/ad-cellpackbm-sl_quick_start_guide.pdf>`__

   


Overview
--------

| The **AD-CELLPACKBM-SL** is a complete BMS kit consisting of the EVAL-ADBMS6830BMSW 16-channel cell monitoring module, the EVAL-ADBMS2950-BASIC pack monitoring module, EVAL-ADBMS6822 isoSPI adapter, and the SDP-K1 microcontroller board.
| This solution is based on high-performance BMS devices that are specifically designed for broad market applications and is suitable for determining the battery's state of charge (SoC) and state of health (SoH), as well as performing important BMS diagnostics.
| The AD-CELLPACKBM-SL can operate either in embedded mode or through a PC-based graphical user interface. Complete with working software and hardware, as well as software examples, this kit makes it easier for customers to prototype and create connected systems and solutions for BMS applications.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-cellpackbm-sl/ad-cellpackbm-sl_angle.jpg
   :width: 600px

| 
| ==== Features ====

-  Accurate voltage and current measurement
-  Highly scalable and ease of integration
-  Robust isoSPI capability implementable in daisy chain high count
-  Inclusive passive balancing with individual pulse-width modulation
-  Isolated power supply between microcontroller and battery monitoring ICs

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

| 
| ==== System Architecture ==== |image1|

| 
| ==== Specifications ==== Below are the absolute maximum ratings of voltages relative to GND unless noted otherwise.

.. container:: center

   
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
   


| 
| ==== What's Inside the Box? ==== The AD-CELLPACKBM-SL package comes with the following boards and accessories:
| |image2|

| 
| ----

Key Components
~~~~~~~~~~~~~~

| 
|

.. container:: indent

   
   EVAL-ADBMS6830BMSW 16-Channel Battery Cell Monitor
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
   The EVAL-ADBMS6830BMSW is a full-featured evaluation board for the ADBMS6830B, a 16-channel battery stack monitor for broad market applications. This board allows multiple boards to be linked through a single twisted pair wire interface (isoSPI) to monitor a long series of cells in a stack. It provides access to full channel monitoring to all cells going to battery pack either in the supply line or in the V+ to V- line. The evaluation board also features reversible isoSPI that can access either path to do measurement functions and serve as a redundant communication path.
   
   .. container:: center

      :doc:`Click here to see the EVAL-ADBMS6830BMSW User Guide </wiki-migration/resources/eval/user-guides/eval-adbms6830bmsw>`

   
   | 
   | ==== EVAL-ADBMS2950-BASIC Battery Pack Monitor ==== The EVAL-ADBMS2950-BASIC battery pack monitoring evaluation board features the ADBMS2950B, a bidirectional current monitor, with 12 buffered high impedance voltage sense inputs, linked through a 2-wire isolated serial interface (isoSPI). This board also features reversible isoSPI, enabling a redundant communication path.
   
   The EVAL-ADBMS2950-BASIC board can be operated on the same isoSPI daisy-chain with other ADBMS2950B and ADBMS6830B devices.
   
   .. container:: center

      :doc:`Click here to see the EVAL-ADBMS2950-BASIC User Guide </wiki-migration/resources/eval/user-guides/eval-adbms2950-basic>`

   
   | 
   | ==== EVAL-ADBMS6822 Dual isoSPI Adapter ==== The :adi:`EVAL-ADBMS6822` is a dual SPI to 2-wire isolated serial port interface (isoSPI) adapter featuring the ADBMS6822. This board allows multiple ADBMS68xx battery monitors through daisy-chain connections. The EVAL-ADBMS6822 evaluation board also features reversible isoSPI, which enables a redundant path to the peripheral units. The PCB components and DuraClik connectors are optimized for low electromagnetic interference (EMI) susceptibility and emissions.
   
   .. container:: center

      :adi:`Click here to see the EVAL-ADBMS6822 User Guide <media/en/technical-documentation/user-guides/eval-adbms6822-ug-2188.pdf>`

   
   | 
   | ==== EVAL-SDP-CK1Z (SDP-K1) Controller Board ==== The EVAL-SDP-CK1Z Controller Board provides a means of communicating with the PC from the other BMS boards in the Cellpack BMS System. The SDP-K1 provides USB connectivity through a USB 2.0 high speed connection to the computer, allowing users to evaluate components on this platform from a PC application. The SDP-K1 is based on an STM32F469NIH6 Arm® Cortex®-M4 microcontroller with the peripheral communication lines available to the daughter board(s) through a 120-pin small footprint connector and Arduino® Uno-compatible headers.
   
   .. container:: center

      :adi:`Click here to see the SDP-K1 User Guide <media/en/technical-documentation/user-guides/EVAL-SDP-CK1Z-UG-1539.pdf>`

   


| 
| ----

Getting Started
~~~~~~~~~~~~~~~

|

.. tip::

   Please refer to the following pages for detailed instructions on how to set up the AD-CELLPACKBM-SL system for evaluation.


   | \* :doc:`AD-CELLPACKBM-SL Hardware User Guide </wiki-migration/resources/eval/user-guides/ad-cellpackbm-sl/hardware>`
   
   -  :doc:`AD-CELLPACKBM-SL Software User Guide </wiki-migration/resources/eval/user-guides/ad-cellpackbm-sl/software>`
   


|

| ----

Resources
~~~~~~~~~

-  :adi:`AD-CELLPACKBM-SL Product Page <AD-CELLPACKBM-SL>`
-  :adi:`EVAL-ADBMS6830BMSW Product Page <EVAL-ADBMS6830BMSW>`
-  :adi:`EVAL-ADBMS6822 Product Page <EVAL-ADBMS6822>`
-  :adi:`SDP-K1 Product Page <SDP-K1>`

| 
| ==== Design & Integration Files ====

.. admonition:: Download
   :class: download

   `AD-CELLPACKBM-SL Design Support Package <https://wiki.analog.com/_media/resources/eval/user-guides/ad-cellpackbm-sl/ad-cellpackbm-sl_design_support_package.zip>`__

   
   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   


| 
| ==== Help and Support ==== For questions and more information, please visit the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone Support Community <reference-designs>`


| 
| |Overview #:resources:eval:user-guides:ad-cellpackbm-sl:hardware|AD-CELLPACKBM-SL Hardware Guide #:resources:eval:user-guides:ad-cellpackbm-sl:software|AD-CELLPACKBM-SL Software Guide#none|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-cellpackbm-sl/ad-cellpackbm-sl_01.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-cellpackbm-sl/ad-cellpackbm-sl_package_contents.png
   :width: 1000px
.. |Overview #:resources:eval:user-guides:ad-cellpackbm-sl:hardware|AD-CELLPACKBM-SL Hardware Guide #:resources:eval:user-guides:ad-cellpackbm-sl:software|AD-CELLPACKBM-SL Software Guide#none| image:: /navigation #/resources/eval/user-guides/ad-cellpackbm-sl
