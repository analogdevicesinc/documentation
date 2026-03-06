AD-FMCOMMS1-EBZ Linux support
=============================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.


   
   |image1|

Analog Devices provides full Linux support for the AD-FMCOMMS1-EBZ. Depending on which FPGA platform you are using the steps to perform to setup the system slightly differ:

-  :doc:`ML605 (Microblaze) </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/microblaze_ml605>`
-  :doc:`KC705 (Microblaze) </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/microblaze_kc705>`
-  :doc:`ZC702, ZC706, ZED (Zynq) </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/zynq>`

Descriptions of the individual Linux device drivers for the different parts on the AD-FMCOMMS1-EBZ can be found at:

-  :doc:`AD9523-1: Low Jitter Clock Generator with 14 LVPECL/LVDS/HSTL/29 LVCMOS Outputs </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9523>`
-  :doc:`ADF4351: Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4350>`
-  :doc:`AD8366: DC to 600 MHz, Dual-Digital Variable Gain Amplifiers </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
-  :doc:`AD9643: 14-Bit, 170/210/250 MSPS, 1.8 V Dual Analog-to-Digital Converter (ADC) </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-  :doc:`AD9122: Dual, 16-Bit, 1200 MSPS, TxDAC+® Digital-to-Analog Converter </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/software/fmcomms1_linux_dd.png
   :align: center

.. image:: https://wiki.analog.com/_media/navigation AD-FMCOMMS1-EBZ#none#./
   :alt: Software#baremetal|No-OS drivers

.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/software/tux.png
