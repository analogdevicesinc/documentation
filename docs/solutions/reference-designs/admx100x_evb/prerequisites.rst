.. _admx100x prerequisites:

Prerequisites
=============

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
----------------------

#. The :adi:`ADMX1001` or :adi:`ADMX1002` signal generator module
#. The :adi:`EVAL-ADMX100X-FMCZ` evaluation board (includes 12 V wall adapter)
#. A controller board. Our recommended one can be found :ref:`here <admx100x-evb quickstart carriers>`.

   - AMD Xilinx `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     (supports both :adi:`ADMX1001` and :adi:`ADMX1002`); also requires an SD
     card (at least 16 GB), a Micro-USB cable (UART), and a LAN cable (Ethernet)
   - :adi:`SDP-H1 <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/sdp-h1.html>`
     (recommended, required for ADMX1001 acquisition channel)
   - :adi:`SDP-S <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-cs1z.html>`
     or :adi:`SDP-B <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-cb1z.html>`
     with :adi:`SDP-I-PMOD <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/sdp-i-pmod.html>`
     interposer (ADMX1002 only); also requires a 6-pin PMOD cable and a 6 V
     power adapter

#. USB cable (for SDP controller to PC connection)
#. Some way to interact with the evaluation board:

   - Host PC
   - SMA cables for signal routing to oscilloscope or spectrum analyzer
     (optional)
   - External common-mode voltage source, if not using on-board DAC via P4
     (optional)

Software prerequisites
----------------------

#. SDP USB drivers — must be installed before the GUI
#. :adi:`ADMX100X GUI <media/en/evaluation-boards-kits/evaluation-software/admx100x-evaluation-software.zip>`
   software that will run on Windows 10 or later
#. For ZedBoard: :external+kuiper:doc:`ADI Kuiper Linux <index>` SD card image
