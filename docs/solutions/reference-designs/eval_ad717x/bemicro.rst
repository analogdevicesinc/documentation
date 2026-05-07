.. _eval_ad717x bemicro:

BeMicro SDK Reference Design for AD7176-2
===============================================================================

Supported Devices:

- :adi:`AD7176-2`

Evaluation Boards:

- :adi:`EVAL-AD7176-2SDZ`

Overview
-------------------------------------------------------------------------------

This lab presents the steps to setup an environment for using the
:adi:`EVAL-AD7176-2SDZ` evaluation board together with the
`BeMicro SDK <https://www.intel.com/content/www/us/en/programmable/b/bemicro-sdk.html>`_
USB stick and the Nios II Embedded Development Suite (EDS). Below is
presented a picture of the EVAL-AD7176-2SDZ Evaluation Board with the
BeMicro SDK Platform.

.. image:: images/ad7176_2_bemicro.jpg
   :width: 400

For component evaluation and performance purposes, as opposed to quick
prototyping, the user is directed to use the part evaluation setup. This
consists of:

#. A controller board like the SDP-B (EVAL-SDP-CS1Z)
#. The component SDP compatible product evaluation board
#. Corresponding PC software (shipped with the product evaluation board)

The SDP-B controller board is part of Analog Devices System Demonstration
Platform (SDP). It provides a high speed USB 2.0 connection from the PC to
the component evaluation board. The PC runs the evaluation software. Each
evaluation board, which is an SDP compatible daughter board, includes the
necessary installation file required for performance testing.

The :adi:`EVAL-AD7176-2SDZ` evaluation board is a member of a growing
number of boards available for the SDP. It was designed to help customers
evaluate performance or quickly prototype new AD7176-2 circuits and reduce
design time.

The :adi:`AD7176-2` is a fast settling, highly accurate, high resolution,
multiplexed Σ-Δ analog-to-digital converter (ADC) for low band-width input
signals. Its inputs can be configured as two fully differential or four
pseudo differential inputs via the integrated crosspoint multiplexer. An
integrated precision, 2.5 V, low drift (2 ppm/°C), band gap internal
reference (with an output reference buffer) adds functionality and reduces
the external component count.

More Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`AD7176-2 Product Info <AD7176-2>` — pricing, samples, datasheet
- :adi:`EVAL-AD7176-2SDZ evaluation board user guide
  <static/imported-files/user_guides/UG-478.pdf>`
- `BeMicro SDK
  <https://www.intel.com/content/www/us/en/programmable/b/bemicro-sdk.html>`_
- `Nios II Embedded Development Suite (EDS)
  <http://www.altera.com/devices/processor/nios2>`_

Getting Started
-------------------------------------------------------------------------------

The first objective is to ensure that you have all of the items needed and
to install the software tools so that you are ready to create and run the
evaluation project.

Hardware Items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is presented the list of required hardware items:

- Arrow Electronics
  `BeMicro SDK <https://www.intel.com/content/www/us/en/programmable/b/bemicro-sdk.html>`_
  FPGA-based MCU Evaluation Board
- :adi:`BeMicro SDK/SDP Interposer <sdp-bemicro>` adapter board
- **EVAL-AD7176-2SDZ** evaluation board
- Intel Pentium III or compatible Windows PC, running at 866MHz or faster,
  with a minimum of 512MB of system memory

Software Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is presented the list of required software tools:

- `Quartus II Web Edition
  <http://www.altera.com/products/software/quartus-ii/web-edition/qts-we-index.html>`_
  design software v12.0sp2
- `Nios II EDS <https://www.altera.com/download/software/nios-ii>`_ v12.0sp2

The Quartus II design software and the Nios II EDS is available via the
Altera Complete Design Suite DVD or by downloading from the web.

USB Blaster Driver Installation
-------------------------------------------------------------------------------

The USB Blaster is used to program the FPGA on the BeMicro board and also
for data exchange between the system and a PC. To install the driver, plug
the Terasic USB Blaster into one of the PC's USB ports. Your Windows PC
will find the new hardware and try to install the driver.

.. image:: images/image007.png
   :width: 350

Since Windows cannot locate the driver for the device, the automatic
installation will fail and the driver has to be installed manually. In the
**Device Manager** right click on the **USB-Blaster** device and select
**Update Driver Software**.

.. image:: images/image009.png
   :width: 700

In the next dialog box select the option **Browse my computer for driver
software**. A new dialog will open where it is possible to point to the
driver's location. Set the location to
``altera\11.0\quartus\drivers\usb-blaster`` and press **Next**.

+------------------------------------------+------------------------------------------+
| .. image:: images/image011.png           | .. image:: images/image013.png           |
|    :width: 400                           |    :width: 400                           |
+------------------------------------------+------------------------------------------+

.. tip::

   If Windows presents you with a message that the drivers have not passed
   Windows Logo testing, please click **Install this driver software
   anyway**. Upon installation completion a message will be displayed to
   inform that the installation is finished.

+------------------------------------------+------------------------------------------+
| .. image:: images/image017.png           | .. image:: images/image016.jpg           |
|    :width: 400                           |    :width: 400                           |
+------------------------------------------+------------------------------------------+

AD7176-2 Evaluation Project Overview
-------------------------------------------------------------------------------

The evaluation project contains all the source files needed to build a
system that can be used to configure the AD7176-2 and capture data from it.
The system consists of a Nios II softcore processor that is implemented in
the FPGA found on the BeMicro board and a PC application. The softcore
controls the communication with the Device Under Test (DUT) and the data
capture process. The captured data is saved into the onchip RAM of the
BeMicro board and afterwards it is read by the PC application and saved
into a comma separated values (.csv) file that can be used for further data
analysis.

The following components are implemented in the FPGA design:

.. list-table:: System Components
   :header-rows: 1

   * - Name
     - Address
     - IRQ
   * - CPU
     - 0x00000800
     - —
   * - JTAG UART
     - 0x00000090
     - 0
   * - uC-Probe UART
     - 0x000000A0
     - 1
   * - EPCS Flash Controller
     - 0x00001800
     - 2
   * - OnChip RAM
     - 0x00010000
     - —
   * - LED GPIO
     - 0x00000100
     - —
   * - GPIO
     - 0x00002080
     - —
   * - CTRL GPIO
     - 0x000020A0
     - —
   * - SYS ID
     - 0x00000040
     - —
   * - Timer
     - 0x00000060
     - 3
   * - Avalon Master
     - —
     - —
   * - Main PLL
     - 0x00000080
     - —
   * - AD7176_2 0
     - 0x00000120
     - —

The Nios II processor contains a peripheral that implements the
communication protocol with the DUT. The peripheral is divided into three
logical modules: a module which implements the interface with the Avalon bus
and the communication with the onchip RAM, a module which implements an
Avalon master interface which is used to write data directly in the onchip
RAM and a module which is the actual driver of the DUT. The driver can also
be used as standalone in FPGA designs which do not contain a softcore.
Following is presented a block diagram of the HDL driver and a description
of the driver's interface signals.

.. image:: images/ad7176-2_block_diagram.png
   :width: 400
   :alt: HDL driver block diagram

Troubleshooting
-------------------------------------------------------------------------------

In case there is a communication problem with the board the following
actions can be performed in order to try to fix the issues:

- Check that the evaluation board is powered.
- Check that the USB connection cable is properly connected to the device
  and to the computer and that the **USB Blaster Device Driver** is
  installed correctly. If the driver is not correctly installed, perform
  the steps described in the `USB Blaster Driver Installation`_ section.

More Information
-------------------------------------------------------------------------------

- :ez:`Ask questions about the FPGA reference design <community/fpga>`

.. include:: /common/ez_common.rst
