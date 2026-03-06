ADE1201 Evaluation Board User Guide
===================================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ade120x/hardware/eval-ade1201ebz.jpg
   :align: center
   :width: 600px

Introduction
------------

The EVAL-ADE1201EBZ reference design board allows the performance of the ADE1201 Binary Input IC to be evaluated in a context very similar to a real binary input interface application. The kit requires purchasing a second board: the controller board for the system demonstration platform (EVAL-SDP-K1) and current sensors. Alternatively the EVAL-SDP-B evaluation board can be used to interface to the ADE1201. The ADE1201 evaluation kit includes evaluation software, written in LabVIEW®, which provides access to the registers and features of the device using a PC interface. Also available are software drivers written in C which can be compiled and loaded to the EVAL-SDP-K1 evaluation board through the MBED online development environment.

Consult the ADE1201 data sheet in conjunction with this user guide when using the evaluation board.

Evaluation Board Hardware
-------------------------

Overview
~~~~~~~~

The EVAL-ADE1201EBZ (which includes the 8 ADE1201 modules) and the SDP-K1 boards are both required to evaluate the ADE1201.

The EVAL-ADE1201EBZ and the SDP-K1 board are purchased and packaged separately, but must be used together. The EVAL-ADE1201EBZ board is connected to the EVAL-SDP-K1 board using the 120-pin connector, P12 on EVAL-ADE1201 and P10 on SDP-K1. The SDP-K1 board consists of an STM32F4469 microcontroller that handles all the communications from the PC to the ADE1201 devices that populate the evaluation board.

Powering the Evaluation Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADE1201 evaluation board requires a 3.3V DC power supply. It can be powered by:

-  Using the SDP connector. Ensure JP1 jumper is inserted.
-  Connecting an external 3.3V source between TP_P3V3 and GND2 board terminals (open the JP1 jumper in this case).
-  Using on-board regulator, ADM7150ACPZ. This is supplied with 5V from either the SDP connector and USB 5V connected to the SDP board or alternatively by connecting an external power supply to P12. Use P11 jumper to select 5V source.

Analog Inputs
~~~~~~~~~~~~~

The ADE1201 Modules are designed to work with input voltages of 10V up to 300V. The input signals are connected to pins P0 - P7. Connect the BI+ inputs to the pins 1 of these connectors and the BI- signals to the pins 2. All high voltage input signals are passed through EMI/EMC compliant and reverse polarity protected front end circuit before the signals are connected to the ADE1201. The components used on the board are the recommended values to be used with the ADE1201.

Digital I/O
~~~~~~~~~~~

The ADE1201 Modules are connected to a common SPI bus on the evaluation board. The Bus is connected to the SDP board and using the hardware addressing mode, the user can communicate directly with each individual ADE1201 device. The IRQ and DOUT1 pins of each ADE1201 are connected to an LED and also back to the SDP board via the connector. They can be monitored through the LabView GUI and also be polled through the example firmware.

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download
   :class: download

   
   EVAL-ADE1201EBZ Rev B Design Files
   
   -  `Schematics (PDF) <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ade120x/hardware/02_048916c_top.pdf>`__
   -  `Layout (PDF) <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ade120x/hardware/08_048916c.pdf>`__
   -  `Bill of Materials (Excel) <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ade120x/hardware/05-048916-01-c.xlsx>`__
   -  `Fabrication Files (zip) <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ade120x/hardware/ade1201ebz_fab_assy.zip>`__
   

