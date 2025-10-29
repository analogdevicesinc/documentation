.. _template user-guide:

User guide
===============================================================================

The complete user guide of the evaluation board can be found at
:adi:`ADRV9026/ADRV9029 System Development User Guide (Rev. 0) <media/radioverse-adrv9026/adrv9026-system-development-user-guide-ug-1727.pdf>`.

..
   If there is a complete user guide for the evaluation board, in the form of
   a PDF, on analog.com, then reference it here and do not copy and paste other
   information, as it will be hard to maintain if something changes from revision
   to revision.

Hardware guide
-------------------------------------------------------------------------------

..
   If this section will be too long, then it can be made as a separate page,
   and the user-guide.rst to be transformed into user-guide/index.rst.

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..
   Tables or text describing what jumpers should be put, what resistors, to have
   a different clock path for example.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..
   Specify how the power comes to the evaluation board. For example, it can come
   through the FMC connector, or for others, external power supply through
   banana cables.
   Specify the VADJ.
   The power supply comes from the FMC connector, given by the FPGA.

   The VADJ values can be checked out in the README.md file of each combination
   with an FPGA, at: :git-hdl:``.

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..
   Specify what type of signal should be fed to the inputs of the evaluation board.
   For example, say that "to the SMA connectors at VIN+ and VIN−, the source
   should be a low noise, audio precision signal (such as the Audio Precision
   audio analyzer).

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The archive
:adi:`adrv9026-adrv9029-design-file-package.zip <media/radioverse-adrv9026/adrv9026-adrv9029-design-file-package.zip>`
contains the following:

.. Provide a download link for:
.. - Schematics
.. - PCB Layout
.. - Bill of Materials
.. - Allegro Project
.. - LTspice Simulation File

Software guide
-------------------------------------------------------------------------------

..
   Say if it has a Libiio driver, if it can be used in IIO Oscilloscope, if it
   has a Python application (pyadi-iio), MATLAB, etc. For example,

   The evaluation board is supported with the Libiio library. This library is
   cross-platform (Windows, Linux, Mac) with language bindings for C, C#, Python,
   MATLAB, and others. Two easy examples that can be used with it are:

     - :dokuwiki:`IIO Oscilloscope <resources/tools-software/linux-software/iio_oscilloscope>`
     - :external+pyadi-iio:doc:`index`
