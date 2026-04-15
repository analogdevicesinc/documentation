.. _eval-ad777x quickstart:

Quick start
===============================================================================

The quick start guide provides step-by-step instructions on how to do
an initial system setup for the :adi:`EVAL-AD7770-AD7779` evaluation
board on the supported FPGA development board. This guide covers how to
prepare the Kuiper Linux SD card and boot the system.

.. toctree::

   On ZedBoard <zed>
   On SDP-K1 / Nucleo-L552ZEQ (legacy) <sdp>

.. _eval-ad777x carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD7770-AD7779` connects to the FPGA carrier via an FMC
LPC connector.

.. list-table::
   :header-rows: 1

   * - FPGA board
     - :adi:`EVAL-AD7770-AD7779`
   * - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`_
     - FMC LPC

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - ZedBoard
     - Yes
     - Yes
     - In development

Hardware setup
-------------------------------------------------------------------------------

The :adi:`EVAL-AD7770-AD7779` mounts on the ZedBoard via the FMC LPC
connector. The carrier setup requires a Micro-USB cable for UART, a
network cable for Ethernet, and a prepared Kuiper Linux SD card.

ZedBoard + EVAL-AD7770-AD7779
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/zed_setup.jpeg
   :alt: ZedBoard with EVAL-AD7770-AD7779 evaluation board mounted on
         the FMC LPC connector
   :width: 800

   ZedBoard with EVAL-AD7770-AD7779 hardware setup

Go to :ref:`the quick start guide <eval-ad777x quickstart zed>`.
