.. _eval_ad717x prerequisites:

Prerequisites
===============================================================================

What you need depends on which workflow you intend to follow. All workflows
require an AD717x/AD411x-based evaluation board as a starting point.

Common Hardware
-------------------------------------------------------------------------------

An :adi:`AD717x <en/lp/001/ad717x-family.html>`/:adi:`AD411x <en/products/ad4111.html>`-based
evaluation board:

- :adi:`EVAL-AD4111SDZ` / :adi:`EVAL-AD4112SDZ`
- :adi:`EVAL-AD7172-2SDZ` / :adi:`EVAL-AD7173-8SDZ`
- :adi:`EVAL-AD7175-2SDZ` / :adi:`EVAL-AD7176-2SDZ` /
  :adi:`EVAL-AD7177-2SDZ`

ACE Software Evaluation
-------------------------------------------------------------------------------

Reference: :ref:`eval_ad717x ace`

Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`EVAL-AD7173-8ARDZ` evaluation board (or compatible eval board)
- :adi:`SDP-K1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>`
  controller board
- USB Type-A to USB Micro-B cable

Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`ACE (Analysis | Control | Evaluation) software
  <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`

  - Install with **Precision Converter Components** selected
  - Enable the **LibIIO Wrapper** during installation

.. DE10-Nano No-OS Quickstart
.. -------------------------------------------------------------------------------
..
.. Reference: :ref:`eval_ad717x de10nano`

Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Any AD717x/AD411x evaluation board (see `Common Hardware`_ above)
- :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
  FPGA development board

  - 5 V/2 A wall power supply with barrel jack (included with DE10-Nano)
  - Mini-USB to USB Type-A cable (included with DE10-Nano)

- Ethernet cable
- UART terminal application (e.g. Tera Term, PuTTY, or Minicom)
  at 115200 baud (8N1)

Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Intel Quartus Prime
  <https://www.intel.com/content/www/us/en/products/details/fpga/development-tools/quartus-prime.html>`_
  (Lite edition is sufficient)
- :external+no-OS:doc:`AD717x No-OS Driver <drivers/adc/ad717x>`

Renesas RL78G13 Microcontroller No-OS Driver
-------------------------------------------------------------------------------

Reference: :ref:`eval_ad717x ad7175_mcu_driver`,
:ref:`eval_ad717x ad7176_mcu_driver`

Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Renesas Demo Kit for RL78G13 (YRDKRL78G13)
  <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_
- :adi:`EVAL-AD7175-2SDZ` (for the AD7175-2 driver) or
  :adi:`EVAL-AD7176-2SDZ` (for the AD7176-2 driver)
- Five jumper wires for the SPI connection (CS, DIN, DOUT, SCLK, GND)

Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `IAR Embedded Workbench for Renesas RL78 Kickstart
  <http://www.iar.com/en/Products/IAR-Embedded-Workbench/Renesas-RL78/>`_

BeMicro SDK / Nios II Reference Design
-------------------------------------------------------------------------------

Reference: :ref:`eval_ad717x bemicro`

Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Arrow Electronics
  `BeMicro SDK <https://www.intel.com/content/www/us/en/programmable/b/bemicro-sdk.html>`_
  FPGA-based MCU Evaluation Board
- :adi:`BeMicro SDK/SDP Interposer <sdp-bemicro>` adapter board
- :adi:`EVAL-AD7176-2SDZ` evaluation board
- Windows PC (Intel Pentium III or compatible, 866 MHz or faster,
  512 MB RAM minimum)

Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Quartus II Web Edition
  <http://www.altera.com/products/software/quartus-ii/web-edition/qts-we-index.html>`_
  design software v12.0sp2
- `Nios II EDS <https://www.altera.com/download/software/nios-ii>`_ v12.0sp2
- USB Blaster driver (included with Quartus II installation)

FMC-SDP Interposer / Xilinx KC705 Reference Design
-------------------------------------------------------------------------------

Reference: :ref:`eval_ad717x interposer`

Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Xilinx KC705 FPGA board rev C
  <https://www.xilinx.com/products/boards-and-kits/EK-K7-KC705-G.htm>`_
- FMC-SDP adapter board
- :adi:`EVAL-AD7175-2SDZ` or :adi:`EVAL-AD7176-2SDZ` evaluation board

Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Xilinx ISE 14.3

.. note::

   ADI does not offer FPGA carrier platforms for sale or loan; obtaining
   one is a normal part of the development or evaluation process.
