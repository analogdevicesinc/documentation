ADRD3161-01Z
============

Motor Control module with CANopen CiA 402
"""""""""""""""""""""""""""""""""""""""""

Introduction
------------

.. figure:: res/adrd3161-01z.png
   :width: 30em
   :align: right

   ADRD3161-01Z Motor Control board

The :adi:`ADRD3161-01Z` is an FOC motor driver board based on the :adi:`TMC9660`, capable of
driving Stepper, BLDC, and brushed DC motors with optional quadrature (ABN)
and/or Hall encoders. It communicates via CANopen CiA 402 over 500 kbaud CAN.
For development, the :adi:`TMC9660` may also be accessed directly via UART and thus
controlled / configured via TMCL-IDE.

Specifications
--------------

* 9 - 70 V DC supply
* 10 A max phase current (conservative)
* Supported motor types: 3-phase BLDC/PMSM, 2-phase bipolar stepper, brushed DC
* Supported encoder types: ABN (= ABZ, ABI, quadrature), Digital Hall
* Isolated CAN bus communication, CANopen CiA 402
* Option to solder a brake chopper resistor
* Option to use an electromechanical brake (only in the BLDC configuration)

Supporting hardware:

* :adi:`TMC9660` 70V Smart Gate Driver with Servo (FOC) Controller in HW and Buck Converter
* :adi:`MAX32662` Arm Cortex-M4 Processor with FPU-Based Microcontroller (MCU) with 256KB Flash and 80KB SRAM
* :adi:`ADM3053` Signal and Power Isolated CAN Transceiver with Integrated Isolated DC-to-DC Converter

Connections:

* Power input: screw terminal
* Motor connection: screw terminal
* Debug ports (x2): SWD header
* Encoder interface, isolated: :ref:`Custom connector (8 pin) <adrd3161_cable_encoder>`
* CAN, isolated: 2x :ref:`Custom connector (4 pin) <adrd3161_cable_can>`

Required Hardware
-----------------

* :adi:`ADRD3161-01Z`
* Stepper / BLDC / DC motor. Documented output represents the :adi:`QSH5718-51-28-101-10k <qsh5718>` Stepper.
* DC power supply (9 .. 70 VDC)
* CAN, encoder cables, described in the :doc:`hardware-guide`

To debug / reprogram the device, you will need a MAXDAP compatible debug probe, such as the :adi:`MAX32625PICO`.

User Guides
-----------

.. toctree::

   hardware-guide
   quick-start-guide
   production-guide

Help and Support
----------------

For questions and more information about this product, connect with us through the Analog Devices :ez:`sw-interface-tools/robot-operating-system-ros-sdk` .

