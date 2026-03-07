.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp_h1.jpg
   :width: 200px

Preface
=======

The SDP-H1 is used as part of the evaluation system for many ADI components. the SDP-H1 board is designed to be used in conjunction with various ADI component evaluation boards as part of a customer evaluation environement.The SDP provides `USB <https://en.wikipedia.org/wiki/USB>`_ connectivity through a USB 2.0 high speed connection to the computer allowing users to evaluate components on this platform from a PC application. The SDP-H1 has a Xilinx(R) Spartan(r)-6 FPGA and a :adi:`ADSP-BF527` Blackfin processor. It has an Low Pin Count (LPC) FMC connector and a 120 pin connector identical to that found on the SDP-B and SDP-S.

Links
=====

:doc:`Getting Started </wiki-migration/resources/eval/sdp/sdp-h1/getting_started>` - provides software and hardware installation procedure, PC system requirements and basic board information.

:doc:`Hardware Description </wiki-migration/resources/eval/sdp/sdp-h1/hardware_description>` - provides information on the EVAL-SDP-CH1Z components

:doc:`Schematics </wiki-migration/resources/eval/sdp/sdp-h1/schematics>` - provides schematics and other hardware documents

Product Overview
================

This board features :

-  Xilinx Spartan(R)-6 FPGA
-  DDR2

   -  Micron MT47H32M16Hr-25E:G -8Mb x 16 bits x 4 Banks(512 Mb/64Mb)

-  SRAM

   -  ISSI IS61WV25616BLL-10BLI – 256Kb x 16 bits (4 Mb/512 Kb)

-  1 x 160 pin FMC-LPC Connector (See VITA 57 Specification)

   -  Samtec ASP-134603-01
   -  Up to 1,080 Mb/s LVDS
   -  Single Ended LVCMOS
   -  Power

-  Analog Devices :adi:`ADSP-BF527` Blackfin processor

   -  Core performance up to 600 MHz
   -  208 -ball CSP-BGA package
   -  24 MHz CLKIN oscillator

-  32Mb flash memory

   -  `Numonyx M29W320EB <http://www.numonyx.com/Documents/Datasheets/M29W320E.pdf>`_ or
   -  Numonyx M25P32

-  SDRAM memory

   -  `Micron MT48LC16M16A2P-6A <http://www.micron.com/products/ProductDetails.html?product=products/dram/sdram/MT48LC16M16A2P-6A>`_ - 16 Mb x 16 bits (256 Mb/32 MB)

-  2 x 120-pin small foot print connectors

   -  `Hirose FX8-120P-SV1(91) <http://www.hirose.co.jp/cataloge_hp/e57800016.pdf>`_,120 Pin Header

-  Blackfin processor peripherals exposed

   -  SPI
   -  SPORT
   -  TWI/I2C
   -  GPIO
   -  PPI
   -  Asynchronous Parallel

For more information, go to :adi:`The ADI web site <sdp>`.
