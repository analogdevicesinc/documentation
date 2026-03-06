Basic Quick Start Guide
=======================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



Required Hardware
-----------------

HW Platform(s) required:

-  One of the following baseboards:

   -  `Xilinx Virtex-6 ML605 <https://www.xilinx.com/ml605>`__
   -  `Xilinx Kintex-7 KC705 <https://www.xilinx.com/kc705>`__
   -  `Xilinx Virtex-7 VC707 <https://www.xilinx.com/vc707>`__
   -  `Xilinx Zynq ZC702 <https://www.xilinx.com/zc702>`__
   -  `Zed Board (Z\ ynq E\ valuation & D\ evelopment Board) <http://www.zedboard.org/content/overview>`__

-  The analog front end hardware platform:

   -  :adi:`AD-FMCOMMS1-EBZ <en/evaluation/eval-fmcomms/eb.html>` (ADI)

-  Optional:

   -  Signal generator (~2.4GHz), optional
   -  Spectrum analyser (~2.4GHz), optional

Since there is a big piece of software, all reference designs are based around Microblaze or ARM (Zynq) with associated AXI supporting pieces (UART, I\ :sup:`2`\ C, etc.).

**For VC707, use FMC2_HPC, for all others use FMC_LPC or FMC1_LPC.**

Required Software
-----------------

-  Xilinx ISE (Programmer (IMPACT) is sufficient for the demo and is available on Webpack). Please use a version the same as or higher than the one used in the reference design.
-  A UART terminal (Tera Term/Hyperterminal), Baud rate 57600 (for 7 series), 115200 (for Zynq devices).
-  Chipscope for busplot of received signals.

Bit file
--------

-  Download the gzip file and extract the **sw/cf_xcomm\_<board>.bit** file.

Running Demo (SDK) Program
--------------------------

7 Series Devices
~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/cf_xcomm_kc705_setup.jpg
   :alt: KC705 setup
   :width: 200px

-  Set the UART Terminal baud rate to 57600.
-  Set the spectrum analyzer center frequency to 2.4GHz, span 500MHz.
-  Set the signal generator frequency to 2.406GHz (0dBm).
-  Program the device.
-  The UART messages are shown below.
-  The spectrum analyzer and chipscope plots are shown below.

Zynq Devices
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/cf_xcomm_zc702_setup.jpg
   :alt: ZC702 setup
   :width: 200px

-  Set the UART Terminal baud rate to 115200.
-  Set the spectrum analyzer center frequency to 2.4GHz, span 500MHz.
-  Set the signal generator frequency to 2.406GHz (0dBm).
-  ZC702, set SW10 to "01" position (USB-JTAG).
-  ZC702, set J27 and J28 to pin "1" (switch position).
-  ZC702, set J21, J20, J22, J25 and J26 to pin "3" (GND).
-  Run the tcl script cf_xcomm_zc702.tcl on a xmd prompt. (xmd -tcl sw/cf_xcomm_zc702.tcl).
-  Press 'q' to exit the HDMI audio loop in the UART terminal.
-  The UART messages are shown below.
-  The spectrum analyzer and chipscope plots are shown below.

A typical XMD transcript is shown below (the commands are highlighted).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/cf_xcomm_zc702_xmd.jpg
   :alt: XMD Terminal
   :width: 200px

Results
~~~~~~~

If XMD commands were successful, you will see the UART window messages as below. The only difference in Zynq and non-Zynq boards are that the Zynq boards include the HDMI display cores.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/cf_xcomm_zc702_uart.jpg
   :alt: UART Terminal
   :width: 200px

The DAC outputs for 70MHz/90MHz (2.330GHz/2.310GHz centered at 2.4GHz) tones is shown below.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/cf_xcomm_kc705_spectrum.jpg
   :alt: Spectrum Analyzer
   :width: 200px

The ADC bus plots on chipscope is shown below, the fft core stores the data (upto 1024) for display and may be viewed anytime when FFT core is idle. The first sample is synchronized with trigger port 0. The plot below scales and offsets the signals to make the display less crowded. A chipscope project file can be found in the sw directory.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/cf_xcomm_kc705_chipscope.jpg
   :alt: Chipscope Plot
   :width: 200px
