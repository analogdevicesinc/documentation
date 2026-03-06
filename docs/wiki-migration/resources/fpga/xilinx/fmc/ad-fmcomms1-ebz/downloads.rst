FMComms1 Downloads
==================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



.. admonition:: Download
   :class: download

   
   -  `Schematic <https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/fmcomms1-revbschematic.pdf>`__
   -  `Assembly Files <https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/20_011018b-assy.zip>`__
   -  `Build Files <https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/20_011018b.zip>`__
   


FPGA Reference Designs on GitHub :

.. admonition:: Download
   :class: download

   
   -  :git-fpgahdl_xilinx:`archive/ad_fmcomms1_ebz_edk_14_1_2012_12_14`.zip
   -  :git-fpgahdl_xilinx:`archive/ad_fmcomms1_ebz_edk_14_1_2012_12_14`.tar.gz
   -  https://github.com/analogdevicesinc/fpgahdl_xilinx.git
   


The repository will not contain Xilinx core generator and IP files. You must obtain these files from Xilinx.

.. hint::

   
   -  Questions? :ez:`Ask Help & Support <fpga>`.
   


Tar file contents
-----------------

The tar file contains, in most cases, the following files and/or directories. To rebuild the reference design simply double click the XMP file and run the tool. To build SDK, select a workspace and use the C file to build the elf file. Please refer to `Xilinx EDK documentation <https://www.xilinx.com/support/documentation/dt_edk_edk13-2.htm>`__ for details.

In the case of Zynq, the same procedure applies, except that you must create a FSBL or run the PS7 initialization tcl scripts before the SDK program.

+-------------------+------------------------------------------------------------------------------------------------------+
| license.txt       | ADI license & copyright information.                                                                 |
+-------------------+------------------------------------------------------------------------------------------------------+
| system.mhs        | MHS file.                                                                                            |
+-------------------+------------------------------------------------------------------------------------------------------+
| system.xmp        | XMP file (use this file to build the reference design).                                              |
+-------------------+------------------------------------------------------------------------------------------------------+
| data/             | UCF file and/or DDR MIG project files.                                                               |
+-------------------+------------------------------------------------------------------------------------------------------+
| docs/             | Documentation files (Please note that this wiki page is the documentation for the reference design). |
+-------------------+------------------------------------------------------------------------------------------------------+
| sw/               | Software (Xilinx SDK) & bit file(s).                                                                 |
+-------------------+------------------------------------------------------------------------------------------------------+
| cf_lib/edk/pcores | pcores (if used).                                                                                    |
+-------------------+------------------------------------------------------------------------------------------------------+
