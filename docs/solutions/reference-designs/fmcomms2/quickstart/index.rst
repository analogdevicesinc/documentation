.. _fmcomms2 quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide a simple step by step instruction on how to do an
initial system setup for the :adi:`EVAL-AD-FMCOMMS2` / :adi:`EVAL-AD-FMCOMMS3`
/ :adi:`EVAL-AD-FMCOMMS4` boards on various FPGA development boards. They will
discuss how to program the bitstream, run a no-OS program or boot a Linux
distribution.

.. toctree::

   On ZCU102 <zcu102>
   On KCU105 <kcu105>
   On ZC706 <zc706>
   On ZC702 <zc702>
   On ZED <zed>

.. _fmcomms2/3/4 carriers:

Supported carriers
-------------------------------------------------------------------------------

The AD-FMCOMMS2/3/4-EBZ is, by definition a "FPGA mezzanine card" (FMC), that
means it needs a carrier to plug into. The carriers we support are:

.. list-table::
   :header-rows: 1

   - - Board
     - FMCOMMS2/3/4
   - - :xilinx:`KC705` \*
     - FMC LPC
   - - :xilinx:`KCU105`
     - FMC LPC
   - - :xilinx:`VC707` \*
     - FMC1 HPC
   - - :xilinx:`ZC702`
     - FMC1 LPC
   - - :xilinx:`ZC706`
     - FMC LPC
   - - :xilinx:`ZCU102`
     - FMC HPC0
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC

.. note::

   Support for boards marked with an asterisk (*) was discontinued after the
   hdl_2023_r2 release.

Supported environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - Board
     - HDL
     - Linux Software
     - No-OS Software
   - - :xilinx:`KC705` \*
     - Yes
     - Yes
     - Yes
   - - :xilinx:`KCU105`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`VC707` \*
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
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - Yes

.. note::

   Support for boards marked with an asterisk (*) was discontinued after the
   hdl_2023_r2 release, including in the no-OS repository.

Hardware setup
-------------------------------------------------------------------------------

On most carriers, the AD-FMCOMMS2/3/4-EBZ board connects to the LPC connector
(unless otherwise noted). The carrier setup requires power, UART (115200),
ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections. A few
typical setups are shown below.

ZC702 + FMCOMMS2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Early versions of the ZC702 carriers need to work around `AR# 51438, PG signal
does not assert by default <https://www.xilinx.com/support/answers/51438.html>`_
errata.

.. image:: ../images/fmcomms2_zc702.jpeg
   :width: 800

Go to :ref:`the setup guide <fmcomms2 quickstart zc702>`.

ZC706 + FMCOMMS2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/fmcomms2_zc706.jpeg
   :width: 800

Go to :ref:`the setup guide <fmcomms2 quickstart zc706>`.

ZED + FMCOMMS2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/fmcomms2_zed.jpeg
   :width: 800

Go to :ref:`the setup guide <fmcomms2 quickstart zed>`.

ZCU102 + FMCOMMS2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/fmcomms2_zcu102.jpeg
   :width: 800

Go to :ref:`the setup guide <fmcomms2 quickstart zcu102>`.

KCU105 + FMCOMMS2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/fmcomms2_kcu105.jpeg
   :width: 800

Go to :ref:`the setup guide <fmcomms2 quickstart kcu105>`.

KC705 + FMCOMMS2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/fmcomms2_kc705.jpeg
   :width: 800

Go to :ref:`the setup guide <fmcomms2 quickstart microblaze>`.

VC707 + FMCOMMS2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/fmcomms2_vc707.jpeg
   :width: 800

Go to :ref:`the setup guide <fmcomms2 quickstart microblaze>`.
