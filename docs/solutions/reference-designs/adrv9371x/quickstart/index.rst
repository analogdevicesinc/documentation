Quick Start
================================================================================

The Quick Start Guides provide a simple step by step instruction on how to do an
initial system setup for the :adi:`ADRV9371-N/PCBZ, ADRV9371-W/PCBZ <EVAL-ADRV9371>`,
:adi:`ADRV9375-N/PCBZ and ADRV9375-W/PCBZ<ADRV9375>` boards on
various FPGA development boards. They will discuss how to program the bitstream,
run a no-OS program or boot a Linux distribution.

.. toctree::
   :maxdepth: 1

   On ZCU102 <zcu102>
   On KCU105 <kcu105>
   On ZC706 <zc706>
   On Arria10 SoC <a10soc>
   On Arria10 GX <a10gx>

.. _adrv9371x carriers:

Supported Carriers
--------------------------------------------------------------------------------

The :adi:`ADRV9371/PCBZ <EVAL-ADRV9371>` and :adi:`ADRV9375/PCBZ <ADRV9375>`
are, by definition, "FPGA mezzanine cards" (FMC), which means it needs a carrier
to plug into. The carriers we support are:

.. list-table::
   :header-rows: 1

   * - Board
     - ADRV9371/PCBZ
     - ADRV9375/PCBZ
   * - :xilinx:`ZCU102`
     - FMC HPC0
     - FMC HPC0
   * - :xilinx:`KCU105`
     - FMC1 HPC
     - ---
   * - :xilinx:`ZC706`
     - FMC HPC
     - FMC HPC
   * - `Arria 10 SoC <https://www.altera.com/products/devkit/po-3006/arria-10-sx-soc-development-kit>`_
     - FMCA
     - ---
   * - `Arria 10 GX <https://www.altera.com/products/devkit/po-3017/arria-10-gx-fpga-development-kit>`_
     - Obsolete
     - Obsolete

Supported Environments
--------------------------------------------------------------------------------

The supported environments are:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - no-OS software
   * - :xilinx:`ZCU102`
     - Yes
     - Yes
     - Yes
   * - :xilinx:`KCU105`
     - Yes
     - Yes
     - Yes
   * - :xilinx:`ZC706`
     - Yes
     - Yes
     - Yes
   * - `Arria 10 SoC <https://www.altera.com/products/devkit/po-3006/arria-10-sx-soc-development-kit>`_
     - Yes
     - Yes
     - ---
   * - `Arria 10 GX <https://www.altera.com/products/devkit/po-3017/arria-10-gx-fpga-development-kit>`_
     - Yes
     - Yes
     - Yes

Hardware Setup
--------------------------------------------------------------------------------

In most carriers, the :adi:`ADRV9371/PCBZ <EVAL-ADRV9371>` and
:adi:`ADRV9375/PCBZ <ADRV9375>` boards connect to the HPC connector (unless
otherwise noted). The carrier setup requires power, UART (115200), ethernet
(Linux), HDMI (if available) and/or JTAG (no-OS) connections. A few typical
setups are shown below.

ZCU102 + ADRV9371/PCBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adrv9371x_zcu102_linux_setup.jpg
   :width: 800

KCU105 + ADRV9371/PCBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adrv9371x_kcu105_linux_setup.jpg
   :width: 800

ZC706 + ADRV9371/PCBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adrv9371x_zc706_linux_setup.jpg
   :width: 800

Arria 10 SoC + ADRV9371/PCBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/a10soc_adrv9371.jpg
   :width: 800

Arria 10 GX + ADRV9371/PCBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/arria10-fpga_adrv9371.jpg
   :width: 800
