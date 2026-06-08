.. _fmcomms5-quickstart:

Quick Start
===========

The following guides provide step-by-step instructions for an initial system
setup of the :adi:`AD-FMCOMMS5-EBZ` on various FPGA development boards. They
cover bitstream loading, booting a Linux distribution, and launching the IIO
Oscilloscope for RF waveform capture and playback.

.. toctree::
   :hidden:

   zc702
   zc706
   zcu102

Supported carriers
------------------

The :adi:`AD-FMCOMMS5-EBZ` connects to a carrier board via **two adjacent FMC
connectors**.

.. list-table::
   :header-rows: 1

   -  - Carrier board
      - Connector
   -  - :xilinx:`ZC706`
      - Dual FMC (HPC)
   -  - :xilinx:`ZC702`
      - Dual FMC (LPC)
   -  - :xilinx:`ZCU102`
      - Dual FMC (HPC)

Supported environments
----------------------

.. list-table::
   :header-rows: 1

   -  - Carrier board
      - HDL
      - Linux
      - No-OS
   -  - :xilinx:`ZC706`
      - Yes
      - Yes
      - ---
   -  - :xilinx:`ZC702`
      - Yes
      - Yes
      - ---
   -  - :xilinx:`ZCU102`
      - Yes
      - Yes
      - ---

Hardware setup
--------------

.. image:: ../images/fmcomms5-loopback.jpg
   :alt: AD-FMCOMMS5-EBZ loopback configuration

AD-FMCOMMS5-EBZ + ZC706
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/zc706_fmcomms5.jpg
   :width: 500

AD-FMCOMMS5-EBZ + ZC702
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/zc702_fmcomms5.jpg
   :width: 500

AD-FMCOMMS5-EBZ + ZCU102
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/zcu102_fmcomms5.jpg
   :width: 500

.. warning::

   The ZCU102 requires two FMC spacers to accommodate the
   AD-FMCOMMS5-EBZ. Ensure the spacers are installed before
   connecting the board.

   .. image:: ../images/fmc_spacers.jpg
      :width: 500

Getting started
---------------

- :doc:`ZC702 quick start guide <zc702>`
- :doc:`ZC706 quick start guide <zc706>`
- :doc:`ZCU102 quick start guide <zcu102>`
