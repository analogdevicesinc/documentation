.. _eval-ad35xxr evb quickstart:

Quick start
===============================================================================

The quick start guide provides step-by-step instructions for setting up
the :adi:`EVAL-AD3552R` evaluation board on the supported FPGA development
board. This guide covers SD card preparation, hardware setup, and Linux
IIO client usage.

.. toctree::

   On ZedBoard <zed>
   On SDP-H1 <sdp-h1-ace>

.. _eval-ad35xxr evb carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD3552R` connects to the FPGA carrier via an FMC LPC
connector. VADJ must be set to 1.8 V.

.. list-table::
   :header-rows: 1

   * - FPGA board
     - :adi:`EVAL-AD3552RFMCxZ <EVAL-AD3552R>`
   * - `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`_
     - FMC LPC

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`_
     - Yes
     - Yes
     - Yes

Hardware setup
-------------------------------------------------------------------------------

The :adi:`EVAL-AD3552R` connects to the
`ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/
avnet-board-families/zedboard/>`_ via the FMC LPC connector (P1 on the
evaluation board, FMC on the ZedBoard). Before inserting the evaluation
board, set VADJ to 1.8 V and configure the ZedBoard for SD card boot.

ZedBoard + EVAL-AD3552R
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/ad35xxr_setup_linux.jpeg
   :alt: ZedBoard with EVAL-AD3552R inserted into the FMC LPC connector
   :width: 800

   ZedBoard with EVAL-AD3552R hardware setup

Go to :ref:`the quick start guide <eval-ad35xxr evb quickstart zed>`.

SDP-H1 + ACE
-------------------------------------------------------------------------------

The :adi:`EVAL-AD3552R` can also be controlled with the :adi:`EVAL-SDP-H1`
controller board and the :adi:`ACE` software, without any FPGA or Linux
system.

Go to :ref:`the SDP-H1 + ACE quick start guide <eval-ad35xxr evb quickstart sdp-h1-ace>`.
