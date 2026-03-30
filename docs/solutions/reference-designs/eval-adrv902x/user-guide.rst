.. _adrv902x user-guide:

User guide
===============================================================================

The complete user guide of the evaluation board can be found at
:adi:`ADRV9026/ADRV9029 System Development User Guide (Rev. 0) <media/radioverse-adrv9026/adrv9026-system-development-user-guide-ug-1727.pdf>`.

Hardware guide
-------------------------------------------------------------------------------

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power supply comes from the FMC connector, given by the FPGA.

The VADJ values can be checked out in the README.md file of each combination
with an FPGA, at: :git-hdl:`projects/adrv9026`.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The archive
:adi:`adrv9026-adrv9029-design-file-package.zip <media/radioverse-adrv9026/adrv9026-adrv9029-design-file-package.zip>`
contains the following:

- Schematics
- PCB Layout
- Bill of Materials
- Allegro Project
- LTspice Simulation File

Software guide
-------------------------------------------------------------------------------

The evaluation board is supported with the Libiio library. This library is
cross-platform (Windows, Linux, Mac) with language bindings for C, C#, Python,
MATLAB, and others. One easy to example that can be used with it is:

.. include-template:: ../common/using-iio-osc.rst.jinja

   has_linux: true
   has_no_os: true

About the IIO devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Main receivers RX1, RX2, RX3, and RX4 are handled by the axi-adrv9025-rx-hpc IIO device.

Channels:

- IIO device channel: ``axi-adrv9025-rx-hpc``
- Receiver inputs:

  - {``voltage0_i``, ``voltage0_q``}: RX1
  - {``voltage1_i``, ``voltage1_q``}: RX2
  - {``voltage2_i``, ``voltage2_q``}: RX3
  - {``voltage3_i``, ``voltage3_q``}: RX4

.. include-template:: ../common/using-scopy.rst.jinja

