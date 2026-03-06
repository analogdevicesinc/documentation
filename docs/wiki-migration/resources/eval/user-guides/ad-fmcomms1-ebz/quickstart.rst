AD-FMCOMMS1-EBZ Quick Start Guides
==================================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



The Quick Start Guides provide a simple step by step instruction on how to do an initial system setup for the :adi:`AD-FMCOMMS1-EBZ <en/evaluation/eval-fmcomms/eb.html>` on various FPGA development boards. They will discuss how to install the bitstream and how to boot a Linux distribution and give an basic introduction to the tools available.

Quick Start Guides are available for

-  :doc:`Linux on KC705, VC707 </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/microblaze_kc705>`
-  :doc:`Linux on ZC702, ZC706, ZED </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/zynq>`
-  :doc:`no-OS Drivers </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/no_os_microblaze>`

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/xcomm_zed_linux.jpg
   :alt: FMCOMMS1 on Zed board running linux
   :width: 800px

If you are looking for a quick check on the hardware, you may use the :doc:`No-OS software </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/software/baremetal>`. You will need to build the bit file then use the no-os sources to generate the elf file.
