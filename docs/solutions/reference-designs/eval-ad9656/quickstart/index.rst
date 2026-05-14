.. _ad9656_fmc quickstart:

Quickstart
===============================================================================

The Quick start guides provide simple step by step instructions on how to do an
initial system setup for the :adi:`EVAL-AD9656` board on various FPGA
development boards.

FPGA-based evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use these guides when evaluating with an FPGA carrier board. They cover
bitstream programming and no-OS programs.

.. toctree::

   On ZCU102 <zcu102>

.. _ad9656_fmc carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9656`, is, by definition a "FPGA mezzanine card" (FMC); that
means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD9656
   - - :xilinx:`ZCU102`
     - FMC HPC0

Supported environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - :xilinx:`ZCU102`
     - Yes
     - No
     - Yes

Hardware setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`EVAL-AD9656` board connects to the HPC0 connector
(unless otherwise noted). The carrier setup requires power, UART (115200), and
JTAG (no-OS) connections. A few typical setups are shown below.

ZCU102 + EVAL-AD9656
-------------------------------------------------------------------------------

.. image:: ../images/ad9656_zcu102_no_os_setup.png
   :width: 800

Go to :ref:`the setup guide <ad9656_fmc quickstart zcu102>`.

Windows-based evaluation (HSC-ADC-EVALEZ)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this guide when evaluating with the :adi:`HSC-ADC-EVALEZ <hsadcevalboard>`
data capture kit and VisualAnalog/SPIController software on a Windows PC.

.. toctree::

   On HSC-ADC-EVALEZ <hsc-adc-evalez>
