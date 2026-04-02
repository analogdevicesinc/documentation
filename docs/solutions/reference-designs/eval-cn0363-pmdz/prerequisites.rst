.. _eval-cn0363-pmdz-prerequisites:

Prerequisites
================================================================================

What you need depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
--------------------------------------------------------------------------------

The :adi:`CN0363` HDL reference design and software are designed to
operate with the following hardware and FPGA development system:

#. :adi:`CN0363` hardware: EVAL-CN0363-PMDZ
#. `ZED Board <https://www.avnet.com/americas/products/avnet-boards/avnet-board-families/zedboard/>`_, Rev C or later
#. Some way to interact with the FPGA platform:

   - **Option A (graphical):** USB OTG adapter (Micro-USB to USB-A) for
     keyboard/mouse, HDMI monitor (Full HD)
   - **Option B (serial):** Micro-USB cable for UART console connection,
     a serial terminal application (PuTTY/Tera Term/Minicom, etc.)

#. Two vials: one filled with water and one filled with the sample
   liquid under test
#. Formatted and partitioned 16GB SD card supplied with EVAL-CN0363-PMDZ
   board
#. Ethernet connection for updating SD card

Software prerequisites
--------------------------------------------------------------------------------

#. MicroSD Card imaged with :external+kuiper:doc:`Kuiper Linux <index>`
#. A UART terminal (PuTTY/Tera Term/Minicom, etc.) configured for 115200 baud
   rate (8N1)
#. Boot files for your carrier platform (provided on the SD card or built
   manually)

More Information
--------------------------------------------------------------------------------

-  :doc:`EVAL-CN0363-PMDZ User Guide <user-guide>`
