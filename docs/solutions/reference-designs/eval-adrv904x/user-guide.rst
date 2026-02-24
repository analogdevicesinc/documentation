.. _adrv904x user-guide:

User guide
===============================================================================

The complete user guide of the evaluation board can be found at
:adi:`ADRV904x Evaluation System User Guide (UG-2229) <media/en/technical-documentation/user-guides/eval-adrv904x-ug-2229.pdf>`.

Hardware guide
-------------------------------------------------------------------------------

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power supply comes from the FMC connector, given by the FPGA.

The VADJ values can be checked out in the README.md file of each combination
with an FPGA, at: :git-hdl:`projects/adrv904x`.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design files for the EVAL-ADRV904x evaluation board include:

- Schematics
- PCB Layout
- Bill of Materials
- Design package

Please refer to the :adi:`ADRV9040 product page <ADRV9040>` for
downloadable design files.

Software guide
-------------------------------------------------------------------------------

The evaluation board is supported with the Libiio library. This library is
cross-platform (Windows, Linux, Mac) with language bindings for C, C#, Python,
MATLAB, and others. One easy to example that can be used with it is:

- :dokuwiki:`IIO Oscilloscope <resources/tools-software/linux-software/iio_oscilloscope>`

Required firmware files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADRV904x Linux driver requires the following firmware files to be present
in ``/lib/firmware/`` on the target system:

.. list-table::
   :header-rows: 1

   - - File
     - Description
   - - ``ADRV9040_FW.bin``
     - ARM processor firmware for calibrations and device configuration
   - - ``ADRV9040_DFE_CALS_FW.bin``
     - ARM Cortex-A55 firmware for DFE features (DPD, CLGC, VSWR)
   - - ``stream_image.bin``
     - Stream processor image (user-generated via ADI evaluation software)
   - - ``ADRV9040_RxGainTable.csv``
     - Receiver gain table (default or custom)
   - - ``DeviceProfileTest.bin``
     - Device profile (user-generated configuration file)

These files are included in the Kuiper Linux SD card image.

.. note::

   The ``stream_image.bin`` must be regenerated when updating firmware
   versions, as it is version-specific. The ``DeviceProfileTest.bin`` is
   use-case specific and contains filter coefficients, clock rates, and DFE
   resource settings.

Device variants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two device tree configurations are provided:

- **Default profile** (``zynqmp-zcu102-rev10-adrv904x.dts``): Standard TX/RX
  configuration without observation receiver path activation.
- **NLS profile** (``zynqmp-zcu102-rev10-adrv904x-nls.dts``): Enables the
  observation receiver (ORx) path for transmitter monitoring and DPD
  calibration.

To select the device tree, copy the corresponding ``system.dtb`` to the SD
card boot partition before powering up the board.
