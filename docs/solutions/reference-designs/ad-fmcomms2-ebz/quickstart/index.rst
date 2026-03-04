.. _fmcomms2 quickstart:

Quick start guides
===============================================================================

The Quick start guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-AD-FMCOMMS2` board on various FPGA
development boards. In these guides, we will discuss how to program the bitstream,
run a no-OS program or boot a Linux distribution.

.. toctree::

   On KCU105 <kcu105>
   On ZC702 <zc702>
   On ZC706 <zc706>
   On ZCU102 <zcu102>
   On ZED <zed>

.. _fmcomms2 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD-FMCOMMS2`, is, by definition a "FPGA mezzanine card" (FMC);
that means it needs a carrier to plug into.

The carriers we support are listed below, as well as the FMC port where to
connect the evaluation board:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - AD-FMCOMMS2
   - - :xilinx:`KCU105`
     - FMC LPC
   - - :xilinx:`ZC702`
     - FMC LPC
   - - :xilinx:`ZC706`
     - FMC LPC
   - - :xilinx:`ZCU102`
     - FMC HPC0
   - - :xilinx:`ZED`
     - FMC LPC

Supported Environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - :xilinx:`KCU105`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`ZC702`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`ZC706`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`ZCU102`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`ZED`
     - Yes
     - Yes
     - Yes

Hardware setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`EVAL-AD-FMCOMMS2` boards connect to the LPC
connector (unless otherwise noted). The carrier setup requires power,
UART (115200), Ethernet (Linux), HDMI (if available) and/or JTAG (no-OS)
connections. A few typical setups are shown below.

KCU105 + EVAL-AD-FMCOMMS2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../images/ad9081_zcu102_setup.png
   :width: 800

ZC702 + EVAL-AD-FMCOMMS2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../images/ad9081_zcu102_setup.png
   :width: 800

ZC706 + EVAL-AD-FMCOMMS2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../images/ad9081_zcu102_setup.png
   :width: 800

ZCU102 + EVAL-AD-FMCOMMS2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../images/ad9081_zcu102_setup.png
   :width: 800

ZED + EVAL-AD-FMCOMMS2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../images/ad9081_vck190_setup.jpg
   :width: 800
