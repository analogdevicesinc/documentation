.. _eval-ad6676 quickstart:

EVAL-AD6676 Quick Start Guides
==============================

The Quick Start Guide provides a simple step by step instruction on how to do an
initial system setup for the :adi:`EVAL-AD6676` board on the :xilinx:`ZC706`
FPGA development board. It will discuss how to program the bitstream, run a
no-OS program or boot a Linux distribution.

.. toctree::

   zc706

.. _ad6676 carriers:

Supported carrier
-----------------

The :adi:`EVAL-AD6676` is, by definition a "FPGA mezzanine card" (FMC), that
means it needs a carrier to plug into. The carrier we support is:

.. list-table::
   :header-rows: 2

   * - Board
     - EVAL-AD6676
   * -
     - **FMC Connector**
   * - :xilinx:`ZC706`
     - HPC

.. Additionally, the board can be used with the
.. :adi:`HSC-ADC-EVALEZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HSC-ADC-EVALEZ.html#eb-overview>`,
.. an ADI FPGA-Based Data Capture Kit. Refer to the
.. :download:`HSC-ADC-EVALEZ Quick Start Guide <../files/HSC-ADC-EVALEZ.pdf>`
.. for setup instructions.

Supported Environments
----------------------

The supported environments are:

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux Software
     - No-OS Software
   * - :xilinx:`ZC706`
     - Yes
     - Yes
     - Yes

Hardware Setup
--------------

The :adi:`EVAL-AD6676` board connects to the HPC FMC connector on the
:xilinx:`ZC706`. The carrier setup requires power, UART (115200), ethernet
(Linux), HDMI (if available) and/or JTAG (no-OS) connections.

ZC706 + EVAL-AD6676
~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/linux_setup_ad6676.jpg
   :align: center
   :width: 600px

.. esd-warning::
