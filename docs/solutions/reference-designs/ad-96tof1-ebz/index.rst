.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-96tof1-ebz

.. _ad-96tof1-ebz:

AD-96TOF1-EBZ
=============

3D Time-of-Flight Depth Sensing Evaluation Platform.

General Description
-------------------

.. figure:: board_revc.jpg
   :width: 500 px
   :align: right

   AD-96TOF1-EBZ Board (Rev. C)

The :adi:`AD-96TOF1-EBZ` is an evaluation platform for 3D depth perception
development. When paired with a processor board from the 96Boards ecosystem or
Raspberry Pi family, it provides a proven hardware platform for 3D software and
algorithm development.

The full system hardware consists of two main boards:

- **Laser Transmitter Board** -- generates infrared light pulses using 4
  individual VCSELs with precision drivers positioned to minimize sensor
  shadowing.
- **AFE (Analog Front End) Receiver Board** -- integrates a Panasonic CCD
  sensor with the :adi:`ADDI9036` ToF signal processor. The board is compliant
  with the 96Boards mezzanine specification and supports connection to
  Raspberry Pi boards via a MIPI connector.

Features
~~~~~~~~

- Modular design enabling flexible depth sensing system configuration
- 640 x 480 pixel resolution at up to 30 fps
- 940 nm VCSEL illumination with 110 x 85 degree batwing diffuser
- 90 x 69.2 degree receive field of view with 940 nm bandpass filter
- Multiple operating range modes for near-field to far-field coverage
- Industry-standard threaded tripod adapter mount
- IEC 60825-1 Class 1 laser safety certified
- Complete open-source software SDK

Specifications
--------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Parameter
     - Value
   * - Resolution
     - 640 x 480 pixels
   * - Frame Rate
     - Up to 30 fps (dependent on processor, OS and host interface)
   * - Range (Near Mode)
     - 25 cm to 80 cm
   * - Range (Medium Mode)
     - 30 cm to 4.5 m (Rev. B: 80 cm to 3 m)
   * - Range (Far Mode)
     - 3 m to 6 m
   * - Accuracy
     - < 2% across all ranges
   * - Laser
     - 940 nm VCSEL (Finisar I940-G2332-NBC-D1-110B85R)
   * - Diffuser
     - 110 x 85 degree batwing
   * - Receive Field of View
     - 90 x 69.2 degrees
   * - ToF Signal Processor
     - :adi:`ADDI9036`
   * - CCD Sensor
     - Panasonic MN34906BL
   * - Operating Temperature
     - -20 C to 85 C
   * - Power Input
     - 5 V DC
   * - Maximum Power Consumption
     - 20 W
   * - Connectors
     - 96Board mezzanine high/low-speed expansion, Raspberry Pi camera connector
   * - Connectivity
     - USB, WiFi, Ethernet

Package Contents
----------------

.. figure:: box_contents.jpg
   :width: 500 px

   AD-96TOF1-EBZ Package Contents

The development kit includes:

- Laser Transmitter Board
- AFE Mezzanine Board
- 5 V power supply with cords
- SD card with evaluation software
- Quick Start Guide

Key Components
--------------

Laser Board
~~~~~~~~~~~

The laser board generates modulated infrared light pulses to illuminate the
scene. It contains four individual VCSELs with appropriate precision drivers
and power components, positioned to minimize shadowing around the AFE sensor.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Component
     - Part Number
   * - VCSEL
     - Finisar I940-G2332-NBC-D1-110B85R
   * - MOSFET Driver
     - :adi:`ADP5202` (Rev. D); :adi:`ADP3624` (Rev. B/C)
   * - Power Converter
     - :adi:`ADP2504`
   * - Switching MOSFET
     - EPC2007C
   * - Temperature Sensor
     - :adi:`ADT7410`

AFE Board
~~~~~~~~~

The AFE board is the receiver portion of the system. It combines a CCD sensor
with the :adi:`ADDI9036` ToF signal processor and includes an EEPROM for
firmware and calibration data storage.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Component
     - Part Number
   * - CCD Sensor
     - Panasonic MN34906BL
   * - ToF Signal Processor
     - :adi:`ADDI9036`
   * - Lens
     - JCD J6920B with 940 nm bandpass filter
   * - EEPROM
     - AT24CM01-XHM-B
   * - Temperature Sensor
     - :adi:`ADT7410`
   * - Power Management
     - :adi:`ADP5071`, :adi:`LTC3119`, :adi:`ADP7112`, :adi:`ADP5023`

Software Development
--------------------

.. figure:: sdk_stack.png
   :width: 600 px

   AD-96TOF1-EBZ SDK Architecture

The platform includes a complete open-source SDK supporting Windows and Linux
with wrappers for multiple programming languages and frameworks:

- C/C++ native API
- Python bindings
- MATLAB integration
- OpenCV support
- Open3D integration
- ROS (Robot Operating System) wrappers

The SDK provides a multi-layered architecture: the depth camera connects via
MIPI-CSI to the processor board, which uses V4L2 capture drivers to interface
with the native SDK. User applications run on top of host SDK wrappers.

The complete ADI 3D ToF software suite is available on GitHub:
`aditof_sdk <https://github.com/analogdevicesinc/aditof_sdk>`__

Laser Safety Certification
--------------------------

The AD-96TOF1-EBZ complies with:

- IEC 60825-1:2014 and IEC 60825-1:2007 (Class 1 laser product)
- 21 CFR 1040.10 and 1040.11
- Laser Notice No. 50 (June 24, 2007)

Help and Support
----------------

For questions and more information about this product, connect with us through
the :ez:`3D ToF Depth Sensing <depth-perception-ranging-technologies/lidar-solutions/3d-tof-depth-sensing>` community on EngineerZone.
