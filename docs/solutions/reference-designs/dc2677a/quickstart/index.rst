.. _dc2677a quickstart:

Quickstart
===============================================================================

The Quick Start Guide provides simple step by step instructions on how to do an
initial system setup for the :adi:`DC2677A` board.

FPGA-based evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this guide when evaluating with an FPGA carrier board. It covers bitstream
programming and Linux boot.

.. toctree::
   :maxdepth: 1

    On C5SOC <c5soc>

.. _dc2677a carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`DC2677A` uses an HSMC connector to interface with the FPGA carrier.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - DC2677A
   - - `Cyclone V SoC Development Kit
       <https://www.arrow.com/en/products/sockit/arrow-development-tools>`__
     - HSMC

Supported environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - Eval Board
     - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - DC2677A
     - `Cyclone V SoC Development Kit
       <https://www.arrow.com/en/products/sockit/arrow-development-tools>`__
     - Yes
     - Yes
     - No

Hardware setup
-------------------------------------------------------------------------------

The :adi:`DC2677A` board connects to the Cyclone V SoCkit via the HSMC
connector. The carrier setup requires power (12V for carrier, ±16V/±18V for
DC2677A), UART (115200) and Ethernet connections.

C5SOC + DC2677A
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/dc2677a_c5soc_setup.png
   :width: 800
   :align: center
   :alt: DC2677A on Cyclone V SoC Development Kit setup
