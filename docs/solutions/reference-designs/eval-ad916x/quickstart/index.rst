.. _eval-ad916x quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-AD916X` boards.

.. toctree::

   ZCU102 <zcu102>

.. _eval-ad916x carriers:

Supported carriers
-------------------------------------------------------------------------------

The currently supported carrier is:

- :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` on HPC0

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   - - Board
     - HDL
     - Linux software
     - no-OS software
   - - :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
     - Yes
     - Yes
     - No

Hardware setup
-------------------------------------------------------------------------------

The :adi:`EVAL-AD916X` connects to the :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
through the FMC connector (HPC0). The carrier setup requires a power supply,
UART or Ethernet connections as needed. An RF spectrum analyzer can be used to
verify and visualize the DAC output spectrum.

ZCU102 + EVAL-AD9164
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad9164fmc+zcu102.png
   :width: 800
