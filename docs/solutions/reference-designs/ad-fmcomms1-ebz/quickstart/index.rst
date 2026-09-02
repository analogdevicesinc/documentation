.. _ad_fmcomms1_ebz quickstart:

AD-FMCOMMS1-EBZ Quick Start Guides
==================================

.. warning::

   Analog Devices uses six designations to inform our customers where a
   semiconductor product is in its
   :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`.
   From emerging innovations to products which have been in production for
   twenty years, we understand that insight into life cycle status is important.
   Device life cycles are tracked on their individual product pages on
   `analog.com <https://www.analog.com/>`_, and should always be consulted
   before making any design decisions.

   This particular article/document/design has been retired or deprecated,
   which means it is no longer maintained or actively updated, even though the
   devices themselves may be Recommended for New Designs or in
   Production. This page is here for historical/reference purposes only.

The Quick Start Guides provide a simple step by step instruction on how to do an
initial system setup for the :adi:`AD-FMCOMMS1-EBZ <eval-fmcomms>`
on various FPGA development boards. They will discuss how to install the
bitstream and how to boot a Linux distribution and give an basic introduction to
the tools available.

Quick Start Guides are available for

- :ref:`Linux on KC705, VC707 <ad_fmcomms1_ebz quickstart microblaze-kc705>`
- :ref:`Linux on ZC702, ZC706, ZED <ad_fmcomms1_ebz quickstart zynq>`
- :ref:`no-OS Drivers <ad_fmcomms1_ebz quickstart no-os-microblaze>`

.. image:: ../images/xcomm_zed_linux.jpg
   :alt: FMCOMMS1 on Zed board running linux
   :width: 800

If you are looking for a quick check on the hardware, you may use the
:dokuwiki:`No-OS software <resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/reference_design_no_os>`.
You will need to build the bit file then use the no-os sources to generate the
elf file.

.. toctree::
   :hidden:

   zynq
   microblaze_kc705
   microblaze_ml605
   no_os_microblaze
   zynq_box
