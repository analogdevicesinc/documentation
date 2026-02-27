.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0422

.. _eval-cn0422-ardz:

EVAL-CN0422-EBZ
===============

iCoupler Isolation for HDMI.

Overview
--------

:adi:`CN0422` provides a completely isolated connection between a
High-Definition Multimedia Interface (HDMI) source and HDMI sink device.
Isolation in this circuit increases system safety and robustness by providing
protection against electrical line surges and breaks the ground connection
between bus and digital pins, thereby removing possible ground loops within
the system.

The :adi:`ADP7104` low dropout linear regulator together with :adi:`ADP5302`
high efficiency, ultralow quiescent current step-down regulator provides low
noise supply voltage to the system with high power supply rejection. The
:adi:`ADN4654` 1.1 Gbps Low Voltage Differential Signaling (LVDS) isolator is
used to isolate the CML signals using the coupling and decoupling networks.
The coupling and decoupling networks allow reliable translation between CML and
LVDS voltage levels. The circuit also provides bi-directional isolation of the
Consumer Electronics Control (CEC), Hot Plug Detect (HPD) and Display Data
Channel (DDC) signals using :adi:`ADuM1250` I2C isolators. Two :adi:`ADuM5020`
low emission isolated DC-DC converters provide isolated power to the ADN4654
and ADuM1250 devices. The HDMI V1.3a standard requires that a compliant HDMI
source provide 275 mW of power to an HDMI sink device. The ADuM5020 provides
275 mW to the HDMI sink via the DDC +5V pin located on the HDMI receptacle.

The system can transparently isolate an HDMI interface configured for
resolutions of up to 1280x720 (720p) at 60 Hz and is rated to a withstand
voltage of 2500 V per UL 1577.

.. figure:: sch.jpg
   :width: 800 px
   :align: center

   EVAL-CN0422-EBZ Simplified Circuit Diagram

.. figure:: flow.png
   :align: center

   Isolated HDMI Signal Flow Diagram

Hardware Setup
--------------

To test the EVAL-CN0422-EBZ, first connect a 5 V / 1 A power supply to
connector J5 on the circuit board using a Micro USB Type B cable. This provides
power to the isolation circuitry. The HDMI input is located on the underside of
the board and should be connected to the HDMI source. The HDMI output connector
(J4) is located on the top and should be connected to the HDMI sink. The device
is plug and play; no programming is required to initialize the circuit board.

.. figure:: setup_2.jpg
   :width: 650 px
   :align: center

   EVAL-CN0422-EBZ Connection Overview

Required Equipment
~~~~~~~~~~~~~~~~~~

- EVAL-CN0422-EBZ Circuit Evaluation Board
- :adi:`EVAL-ADV7625-SMZ <ADV7625>` Video Evaluation Board
- Power supply: 5 V 3.6 A DC power supply or 5 V wall wart
- HDMI audio and video source
- 4x HDMI cables, length 1 meter each
- USB-MICRO-B power supply (5 V, 1 A)
- Bulk USB to RS-232 cable
- Two Monitors/Displays with HDMI input

Test Setup
~~~~~~~~~~

.. figure:: setup_1.jpg
   :width: 400 px
   :align: center

   EVAL-CN0422-EBZ Test Setup Block Diagram

Getting Started
~~~~~~~~~~~~~~~

#. Power up the EVAL-ADV7625-SMZ, EVAL-CN0422-EBZ, and the monitors.
#. Configure the EVAL-ADV7625-SMZ in 1:2 HDMI splitter mode by connecting
   the board to a PC/laptop using a bulk USB to RS-232 cable.
#. Install a jumper across J15 on the EVAL-ADV7625-SMZ for programming.
#. Open a serial terminal application such as PuTTY or Tera Term and configure
   the serial settings as 115,200 baud, eight data bits, no parity, one stop
   bit, and no flow control.
#. Using the serial terminal, type the commands ``hdmia a`` and ``hdmia b``.
   Typing ``help`` via RS-232 lists the commands that can be used to control
   the board and indicates the firmware version and build date.
#. Add an HDMI video and audio source to the EVAL-ADV7625-SMZ RxA input (J2).
#. Connect EVAL-ADV7625-SMZ TxA output (J7) to EVAL-CN0422-EBZ input (J3).
#. Connect EVAL-ADV7625-SMZ TxB output (J8) to the HDMI input of a monitor.
#. Connect EVAL-CN0422-EBZ output (J4) to the HDMI input of a monitor.

The HDMI video/audio source appears on both displays. Observing both displays
confirms that the isolated HDMI connection is transparent. Both displays should
be visually identical.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0422-EBZ Design & Integration Files <https://www.analog.com/cn0422-designsupport>`__

   - Schematics
   - Layout Files
   - Gerber Files
   - Assembly Drawing

More Information and Useful Links
---------------------------------

- :adi:`CN0422 Circuit Note Page <CN0422>`
- :adi:`ADN4654 Product Page <ADN4654>`
- :adi:`ADuM1250 Product Page <ADuM1250>`
- :adi:`ADuM5020 Product Page <ADuM5020>`
- :adi:`ADP7104 Product Page <ADP7104>`
- :adi:`ADP5302 Product Page <ADP5302>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`ez/reference-designs`.
