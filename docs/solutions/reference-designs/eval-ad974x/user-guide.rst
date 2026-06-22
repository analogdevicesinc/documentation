.. _eval-ad974x user-guide:

User guide
===============================================================================

This page covers hardware configuration of the :adi:`EVAL-AD9740` /
:adi:`EVAL-AD9742` / :adi:`EVAL-AD9744` / :adi:`EVAL-AD9748`
evaluation boards and the software environments available for evaluation.

Hardware configuration
-------------------------------------------------------------------------------

VADJ and SD boot settings (ZedBoard)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before inserting the evaluation board, configure the ZedBoard for SD card
boot and set the VADJ supply to 3.3 V.

.. important::

   The :adi:`EVAL-AD9740` / :adi:`EVAL-AD9742` / :adi:`EVAL-AD9744` /
   :adi:`EVAL-AD9748` uses 3.3 V logic levels on the FMC connector.
   VADJ must be set to 3.3 V before powering on.
   Applying a different voltage may damage the evaluation board.

Set the boot mode jumpers on the ZedBoard to SD card boot (MIO[2:6] = 1) and
configure the VADJ selection jumper for 3.3 V output.

.. figure:: ./images/zed_vadj_sd_boot.jpeg
   :alt: ZedBoard SD boot jumper settings
   :align: center
   :width: 600

   ZedBoard SD boot jumper settings.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD9740` / :adi:`EVAL-AD9742` / :adi:`EVAL-AD9744` /
:adi:`EVAL-AD9748` includes a complete on-board power solution.
Two DC/DC converters (LTC3601, ADM7154) generate 3.3 V from the 12 V supplied
through the FMC connector.

Schematic, PCB layout, and bill of materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 60 40
   :header-rows: 1

   * - Description
     - Download
   * - EVAL-AD974X Schematic
     - :adi:`EVAL-AD974X Schematic <media/en/technical-documentation/eval-board-schematic/eval-ad9744-schematic.pdf>`
   * - EVAL-AD974X PCB Layout
     - :adi:`EVAL-AD974X PCB <media/en/technical-documentation/evaluation-documentation/eval-ad9744-pcb-layout.pdf>`
   * - EVAL-AD974X Bill of Materials
     - :adi:`EVAL-AD974X BOM <media/en/technical-documentation/evaluation-documentation/eval-ad9744-bom.csv>`

Software guide
-------------------------------------------------------------------------------

Linux-based IIO (using Kuiper Linux on the ZedBoard) software environment is
available:

Linux IIO environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ZedBoard runs ADI Kuiper Linux with the ``adi-axi-dac`` kernel driver
and the ``axi-ad9740`` Linux IIO driver.

Available client applications on the host:

- :ref:`iio-oscilloscope` - graphical IIO data visualization and DAC
  control
- :external+scopy:doc:`Scopy <index>` - oscilloscope and waveform
  generator
- :git-pyadi-iio:`PyADI-IIO </>` - Python scripting interface

AD974X hardware differences
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9748` board is the 8-bit output variant.
Rest of the hardware is identical to the AD9744 board.

The :adi:`EVAL-AD9740` board is the 10-bit output variant.
Rest of the hardware is identical to the AD9744 board.

The :adi:`EVAL-AD9742` board is the 12-bit output variant.
Rest of the hardware is identical to the AD9744 board.

.. figure:: ./images/ad9744-top.jpeg
   :alt: EVAL-AD74X top view
   :align: center
   :width: 400

   EVAL-AD974X top view.

.. figure:: ./images/ad9744-bottom.jpeg
   :alt: EVAL-AD974X bottom view
   :align: center
   :width: 400

   EVAL-AD974X bottom view.
