System Demonstration Platform Blackfin (SDP-B)
==============================================

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/img_6087.jpg
   :width: 500px

Preface
-------

The SDP-B is used as part of the evaluation system for many ADI components. The SDP-B board is designed to be used in conjunction with various ADI component evaluation boards as part of a customer evaluation environment. The SDP provides `USB <https://en.wikipedia.org/wiki/USB>`_ connectivity through a USB 2.0 high speed connection to the computer allowing users to evaluate components on this platform from a PC application. The SDP-B is based on :adi:`ADSP-BF527` Blackfin processor, with the Blackfin processor peripheral communication lines available to the component daughter board through the two identical 120-pin small footprint connectors

Links
-----

:doc:`Getting Started </wiki-migration/resources/eval/sdp/sdp-b/getting_started>` - provides software and hardware installation procedure, PC system requirements and basic board information.

:doc:`Hardware Description </wiki-migration/resources/eval/sdp/sdp-b/hardware_description>` - provides information on the EVAL-SDP-CB1Z components.

:doc:`Schematics </wiki-migration/resources/eval/sdp/sdp-b/schematics>` - provides schematics and other hardware documents.

:doc:`Peripherals Explained </wiki-migration/resources/eval/sdp/sdp-b/peripherals>` - outlines the peripherals on the SDP-B and their implementation.

Product Overview
----------------

The board features:

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
