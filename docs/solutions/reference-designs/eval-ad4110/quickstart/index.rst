.. _eval-ad4110 quickstart:

Quick start
===============================================================================

The quick start guides provide step-by-step instructions for an initial system
setup of the :adi:`EVAL-AD4110-1SDZ` evaluation board on the supported
platforms. Two paths are available: a Windows-based setup using the
:adi:`SDP-B` controller board and the AD4110-1 evaluation software, and an
FPGA-based setup using the Digilent ZedBoard.

.. toctree::

   sdp-b
   zedboard

.. _eval-ad4110 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD4110-1SDZ` connects to carrier boards via the 120-pin SDP
connector (J1) or the SPI PMOD connector (J2).

.. list-table::
   :header-rows: 1

   * - Carrier board
     - Connector
     - Interface
   * - :adi:`SDP-B`
     - J1 (120-pin SDP)
     - USB to PC (Windows evaluation software)
   * - Digilent ZedBoard
     - J2 (SPI PMOD)
     - PMOD (HDL reference design, No-OS)
   * - :adi:`SDP-K1`
     - Arduino headers
     - UART to PC (Mbed IIO firmware)

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - Carrier board
     - No-OS
     - Eval software
   * - :adi:`SDP-B`
     - ---
     - Yes
   * - ZedBoard
     - Yes
     - ---
   * - :adi:`SDP-K1`
     - Yes (Mbed IIO)
     - ---

Hardware setup
-------------------------------------------------------------------------------

EVAL-AD4110-1SDZ + SDP-B
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board connects to the :adi:`SDP-B` controller board via the
120-pin connector (J1). Secure the two boards together using the plastic
screws and washers provided in the evaluation board kit. Connect ±15 V and
GND to J14 on the evaluation board. Connect the :adi:`SDP-B` board to the PC
using the USB cable.

.. figure:: ../images/ad4110_sdp.jpeg
   :alt: EVAL-AD4110-1SDZ connected to SDP-B controller board
   :align: center
   :width: 800

   EVAL-AD4110-1SDZ with SDP-B hardware setup

EVAL-AD4110-1SDZ + ZedBoard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board connects to the ZedBoard via the SPI PMOD connector (J2)
on the evaluation board and the PMOD headers on the ZedBoard. Connect the SPI
signals using individual jumper wires as described in
:ref:`eval-ad4110 quickstart zedboard`.

.. figure:: ../images/ad4110_setup.jpeg
   :alt: EVAL-AD4110-1SDZ connected to the Digilent ZedBoard via
         PMOD headers
   :align: center
   :width: 800

   EVAL-AD4110-1SDZ with ZedBoard hardware setup
