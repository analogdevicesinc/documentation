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

- :dokuwiki:`IIO Oscilloscope <resources/tools-software/linux-software/iio_oscilloscope>`
