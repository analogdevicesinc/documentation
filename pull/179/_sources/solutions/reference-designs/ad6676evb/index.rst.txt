.. _ad6676evb:

AD6676EVB User Guide
====================

Introduction
------------

The :adi:`AD6676` is a wideband IF receiver subsystem that combines an IF
amplifier, antialiasing filter, 16-bit ADC, and digital signal processing
blocks (NCO, quadrature digital downconverter, decimation, and AGC) into a
single chip.

The AD6676EVB evaluation board provides all of the support circuitry required
to operate the AD6676 in its various modes and configurations. The board
interfaces to the carrier through an FMC connector.

Features
~~~~~~~~

- High instantaneous dynamic range (IIP up to 36 dBm, NSD as low as
  -159 dBFS/Hz)
- On-chip digital signal processing including NCO, quadrature DDC, decimation,
  and AGC
- JESD204B single or dual lane outputs
- SPI interface for setup and control
- On-board LDO regulator powered through the FMC interface

Supported Devices
-----------------

- :adi:`AD6676`

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux
   * - :xilinx:`VC707 <products/boards-and-kits/ek-v7-vc707-g.html>`
     - Yes
     - Yes
   * - :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
     - Yes
     - Yes

HDL Reference Design
--------------------

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad6676evb`
- :git-hdl:`library/axi_ad6676`

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~

The design is built upon ADI's generic HDL reference design framework. ADI
does not distribute pre-built bitstream files, so the project must be built
from source. Clone the HDL repository and, with the correct tools installed,
navigate to the project directory and run ``make``:

.. code-block:: bash

   cd hdl/projects/ad6676evb/zc706
   make

Software Support
----------------

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

The AD6676 Linux driver is an IIO (Industrial I/O) subsystem driver targeting
the :adi:`AD6676` wideband IF receiver subsystem.

- :git-linux:`drivers/iio/adc/ad6676.c`
- :git-linux:`drivers/iio/adc/ad6676.h`

Linux Device Tree
^^^^^^^^^^^^^^^^^

The AD6676 driver is an SPI bus driver instantiated via device tree.

Required device tree properties:

- ``compatible``: Must be ``"ad6676"``
- ``reg``: SPI slave select number

The following device tree properties allow customization of the AD6676
operating parameters:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Property
     - Description
   * - ``adi,adc-frequency-hz``
     - Initial ADC frequency in Hz
   * - ``adi,adc-frequency-fixed-enable``
     - Prevents ADC frequency changes after initial setup
   * - ``adi,use-external-clk-enable``
     - Use external clock
   * - ``adi,decimation``
     - Initial decimation rate (12, 16, 24, or 32)
   * - ``adi,intermediate-frequency-hz``
     - Initial IF in Hz
   * - ``adi,intermediate-frequency-min-hz``
     - Allowed minimum IF in Hz
   * - ``adi,intermediate-frequency-max-hz``
     - Allowed maximum IF in Hz
   * - ``adi,bandwidth-hz``
     - Initial bandwidth in Hz
   * - ``adi,bandwidth-margin-low-mhz``
     - Initial bandwidth margin low in MHz
   * - ``adi,bandwidth-margin-high-mhz``
     - Initial bandwidth margin high in MHz
   * - ``adi,bandwidth-margin-if-mhz``
     - Initial bandwidth margin IF in MHz
   * - ``adi,external-inductance-l-nh``
     - Inductance of external inductors in nH
   * - ``adi,idac1-fullscale-adjust``
     - Initial IDAC_FS (range: 16 to 64)
   * - ``adi,shuffler-control``
     - Initial shuffler control setting
   * - ``adi,shuffler-thresh``
     - Initial shuffler threshold
   * - ``adi,jesd-scrambling-enable``
     - Enables JESD204B link scrambling
   * - ``adi,jesd-use-lvds-syncb-enable``
     - Use LVDS SYNCB
   * - ``adi,jesd-powerdown-sysref-enable``
     - Power down SYSREF
   * - ``adi,jesd-l-lanes``
     - Number of JESD204B lanes
   * - ``adi,jesd-f-frames-per-multiframe``
     - Number of frames per multiframe
   * - ``adi,spi-3wire-enable``
     - Enables SPI 3-wire mode

Example device tree:

- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zc706-adv7511-ad6676-fmc.dts`

IIO Attributes
^^^^^^^^^^^^^^

Once the driver is loaded, the following IIO attributes are available at
``/sys/bus/iio/devices/iio:deviceX/``:

.. list-table::
   :header-rows: 1

   * - Attribute
     - Description
   * - ``in_voltage_adc_frequency``
     - ADC clock frequency in Hz. Range with external synthesizer: 2.0 to
       3.2 GHz. Range with internal synthesizer: 2.925 to 3.2 GHz.
   * - ``in_voltage_sampling_frequency``
     - Complex (I/Q) data rate in SPS. Equals FADC / decimation factor.
   * - ``in_voltage_intermediate_frequency``
     - IF to which the ADC is tuned (70 to 450 MHz depending on external
       inductors)
   * - ``in_voltage_bandwidth``
     - ADC bandwidth in Hz. Allowed range: 0.5% to 5% of FADC.
   * - ``in_voltage_bw_margin_low``
     - Lower bandwidth margin for noise-shaping profile in MHz
   * - ``in_voltage_bw_margin_high``
     - Upper bandwidth margin for noise-shaping profile in MHz
   * - ``in_voltage_bw_margin_if``
     - Displacement of first resonator resonance frequency from band-center
       in MHz
   * - ``in_voltage_scale``
     - Full-scale adjustment [0.25, 0.5, 1.0]. Writing 0.5 lowers PIN_0dBFS
       by 6 dB.
   * - ``in_voltage_hardwaregain``
     - Input attenuator setting in dB (0 to -27 dB in 1 dB steps)
   * - ``in_voltage_shuffler_control``
     - Comparator reordering rate (disable, fadc, fadc/2, fadc/3, fadc/4)
   * - ``in_voltage_shuffler_thresh``
     - Dynamic shuffle threshold (0 to 8). Zero means shuffling always
       enabled.
   * - ``in_voltage_test_mode``
     - Interface test mode (off, checkerboard, pn23, pn9, ramp, etc.)

The IIO Oscilloscope application can be used to interact with the AD6676
IIO device driver and visualize captured data. The screenshot below shows
the IIO Oscilloscope connected to the AD6676EVB.

.. figure:: ad6676_osc_screenshot.png
   :align: center

   AD6676 IIO Oscilloscope capture

JESD204B Interface Testing
""""""""""""""""""""""""""

The JESD204B serial interface can be verified using eye scan measurements.
The following figures show example eye diagram results for Lane 0 and Lane 1
of the AD6676EVB JESD204B link.

.. figure:: ad6676_lane0_bert.png
   :align: center

   AD6676 JESD204B eye scan -- Lane 0

.. figure:: ad6676_lane1_bert.png
   :align: center

   AD6676 JESD204B eye scan -- Lane 1

No-OS Project
~~~~~~~~~~~~~

- :git-no-OS:`projects/ad6676-ebz`
- :git-no-OS:`drivers/adc/ad6676`

The No-OS project provides bare metal support for the AD6676EVB. To set up
the software:

#. Clone the No-OS GitHub repository
#. Build the project located at ``projects/ad6676-ebz``
#. Follow the instructions in the
   `ADI No-OS build guide <https://analogdevicesinc.github.io/no-OS/doxygen/build_guides.html>`__

More Information
----------------

- :adi:`AD6676 Product Page <AD6676>`
- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `JESD204B High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__
- `AD6676EVB HDL Project Documentation <https://analogdevicesinc.github.io/hdl/projects/ad6676evb/index.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
