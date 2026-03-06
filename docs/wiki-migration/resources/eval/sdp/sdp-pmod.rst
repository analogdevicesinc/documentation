PMOD to SDP Interposer
======================

Description
-----------

The PMOD interface can be found on many microprocessor development platforms, FPGA development kits, and are a great way to begin prototyping a design. To make it easy for our customers to test and evaluate ADI PMOD boards, the :adi:`SDP-I-PMD <sdp-pmd-ib1z>` was developed to enable quick and easy connection to the ADI system demonstration platform (SDP). This allows for testing the functionality as well as the performance of the circuit using a controlled evaluation environment. Demonstration software is available for many PMOD hardware modules but not all, so please check each project carefully for details.

The :adi:`SDP-I-PMD <sdp-pmd-ib1z>` can be used to connect all ADI PMOD boards directly to the SDP, creating a PC interface via the USB port, and allowing for LabVIEW software development.

Product Overview
----------------

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-i-pmod/sdp-i-pmod.jpg
   :align: center

Pictured above is the :adi:`SDP-I-PMD <sdp-pmd-ib1z>` interposer board which was developed to quickly and easily connect ADI PMOD boards to our system demonstration platform (SDP). The connectors on the SDP-PMD-IB1Z board is marked by the green font on the picture.

PMOD-SDP Hardware Explained
---------------------------

PMOD-SDP Connector and External Power
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SDP-PMD-IB1Z itself won't do anything without the SDP hardware control board and a 6V external power supply through **P5** connector.

The SDP doesn't provide voltage rails for their daughter cards, and PMOD hardware expects host controllers to provide the power. So we had to provide the power for the SDP daughter card(SDP-PMD-IB1Z) and provide the power for the attached PMOD boards, which is why the 6V power supply is there, and why you have to connect it up.

When using the PMOD-SDP interposer board to connect PMOD boards to the PC via the SDP platform, you should be connected to the EVAL-SDP-CB1Z via the CONA connector to the **P1** connector on the SDP-PMD-IB1Z board.

Standard Interfaces Supported
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PMOD is a serial communication protocol and can support the following types of communication.

-  **P4** - Expanded SPI or Expanded UART
-  **P2** and **P3** - Expanded I2C

For a complete understanding of supporting communication protocols and their respective pin outs and form factors please see the official Digilent specification.

`Digilent PMOD Interface Specification <https://wiki.analog.com/_media/resources/eval/sdp/sdp-i-pmod/digilent_pmod_interface_specification.pdf>`__

The **P4** could be working on the both Expanded SPI or Expanded UART mode, the different working mode set by the different jumper position.

--------------

The following picture showing the **P4** working on the Expanded SPI mode jumper position configuration:

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-i-pmod/sdp-i-pmod_jumper-spi.jpg
   :align: center

--------------

The following picture showing the **P4** working on the Expanded UART mode jumper position configuration:

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-i-pmod/sdp-i-pmod_jumper-uart.jpg
   :align: center

--------------

.. important::

   Please make sure the **P4** working mode selection jumper **JP1** in the right position before power on the system. If the PMOD daughter board used **P2** or **P3** I2C interface, **JP1** could set to any position but don't left it open.


PMOD Power Rails Supplied
~~~~~~~~~~~~~~~~~~~~~~~~~

PMOD hardware modules recieve their power from the host controller board. So in this case the SDP-PMD-IB1Z is the host, and we give the option for supplying your PMOD board with either 3.3V or 5V depending on the position of jumper(**JP2**). The position of the jumper will decide the voltage rail passed, so please be careful to know which voltage rail your PMOD board needs before selecting a setting.

.. warning::

   If you set the wrong PMOD power supply voltage configuration jumper **JP2**, permanent damage to the PMOD board may occur! Please make sure the PMOD power supply voltage configuration jumper **JP2** on the right position before power on the system.


--------------

The following jumper position showing the 3.3V power supply PMOD daughter board configuration:

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-i-pmod/sdp-i-pmod_jumper-3.jpg
   :align: center

--------------

The following jumper position showing the 5V power supply PMOD daughter board configuration:

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-i-pmod/sdp-i-pmod_jumper-5.jpg
   :align: center

--------------

Hardware Setup Procedure
------------------------

If you are using the SDP with the PMOD-SDP adaptor board, and any PMOD hardware boards, please use the following setup procedure:

-  Set the right **JP1** and **JP2** according your PMOD daughter board.
-  Connect the PMOD daughter board to **P2** or **P3** or **P4** of the SDP-PMD-IB1Z, depending on SPI/UART or I2C interface.
-  Connect SDP-PMD-IB1Z **P1** to the EVAL-SDP-CB1Z using the 120-pin connector labeled CON A
-  Plug in EVAL-SDP-CB1Z into USB port of computer.

   -  You may need to wait for the SDP device drivers to install if this is the first time using the SDP board.

-  Connect 6V power supply (EVAL-CFTL-6V-PWRZ) to **P5** of SDP-PMD-IB1Z.
-  Wait for 10 seconds.
-  Open up the Device Manager in your computer, and make sure you see ADI Development Tools attached.

.. important::

   When you finished your system evaluation, before disconnect any connector or remove any jumper please disconnect 6V power supply (EVAL-CFTL-6V-PWRZ) from **P5** of SDP-PMD-IB1Z first.


ADI PMOD Compatible Boards
--------------------------

Following is a table of current PMOD boards offered by Analog Devices, and will connect to the PMOD-SDP adaptor board.

+--------------------------------------------+---------------------------------------+------------------------+
| Webpage                                    | Application                           | SDP Software Available |
+============================================+=======================================+========================+
| :adi:`cn0179`                              | 4-20 mA Output Drive                  | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0216`                              | Weigh Scale Measurement               | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0326`                              | pH Measurement                        | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0332`                              | Rotational Speed Measurement          | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0335`                              | 0 - 10V Input Range                   | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0336`                              | 4-20 mA Input Range                   | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0337`                              | RTD Temperature Measurement           | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0346`                              | Relative Humidity Measurement         | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0349`                              | Conductivity Measurement              | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0350`                              | Peizo Vibration Measurement           | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0354`                              | Multichannel Thermocouple Measurement | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0355`                              | Differential Pressure Measurement     | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0357`                              | Toxic Gas Monitoring                  | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0365`                              | High Temperature Data Acquisition     | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0370`                              | Low Noise LED Drive                   | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+
| :adi:`cn0372`                              | Energy Harvesting Data Acquisition    | Yes                    |
+--------------------------------------------+---------------------------------------+------------------------+

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download
   :class: download

   
   SDP-PMD-IB1Z Design & Integration Files (Rev B)
   
   -  `Schematics <https://wiki.analog.com/_media/resources/eval/sdp/sdp-i-pmod/02-042045-01-b.pdf>`__
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/sdp/sdp-i-pmod/05-042045-01-b.xlsx>`__
   -  `Gerber Files <https://wiki.analog.com/_media/resources/eval/sdp/sdp-i-pmod/09-042045-01b.zip>`__
   -  `PCB Assembly Files <https://wiki.analog.com/_media/resources/eval/sdp/sdp-i-pmod/01-042045-01b.zip>`__
   


.. admonition:: Download
   :class: download

   SDP-PMD-IB1Z Design & Integration Files (Rev 0)

   
   -  `Schematics Rev 0 <https://wiki.analog.com/_media/resources/eval/sdp/sdp-i-pmod/eval_sdp-pmod_schematic_reva.pdf>`__
   


Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/SDP-PMD-IB1Z?&v=Rev B>`__ to receive all these great benefits and more!


*End of Document*
