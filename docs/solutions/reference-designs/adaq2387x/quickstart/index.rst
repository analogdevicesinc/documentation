.. _eval-adaq23875-fmcz quickstart:

Quickstart
===============================================================================

The Quick Start Guide provides step-by-step instructions on how to set up the
:adi:`EVAL-ADAQ23875FMCZ <EVAL-ADAQ23875>` evaluation board on the ZedBoard
FPGA development board running Kuiper Linux, and how to capture and analyse
data using the IIO Oscilloscope application.

.. toctree::

   ZedBoard <zedboard>

.. _eval-adaq23875-fmcz carriers:

Supported carriers
-------------------------------------------------------------------------------

The carrier we support is:

- :xilinx:`ZedBoard (AES-Z7EV-7Z020-G) <products/boards-and-kits/1-8dyf-11.html>`
  on FMC connector

Supported Environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   - - Board
     - HDL
     - Linux Software
     - No-OS Software
   - - :xilinx:`ZedBoard <products/boards-and-kits/1-8dyf-11.html>`
     - Yes
     - Yes
     - No

Hardware Setup
-------------------------------------------------------------------------------

The :adi:`EVAL-ADAQ23875FMCZ <EVAL-ADAQ23875>` connects directly to the
ZedBoard FMC LPC connector. The carrier setup requires a 12 V power supply,
an Ethernet (LAN) connection, and an analog signal source connected via SMA
cable and XLR-to-SMA adapter.

ZedBoard + EVAL-ADAQ23875FMCZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/hardware-connection-adaq23875.jpg
   :align: center
   :width: 600

Next Steps
-------------------------------------------------------------------------------

Proceed to the :ref:`ZedBoard quickstart guide <eval-adaq23875-fmcz quickstart zedboard>`
for detailed setup and evaluation instructions.
