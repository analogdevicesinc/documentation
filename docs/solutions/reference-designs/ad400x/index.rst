.. _ad400x:

AD40xx/ADAQ4001/ADAQ4003 User Guide
====================================

Introduction
------------

This document describes the AD400x/ADAQ4003 reference design, including the
No-OS software used to control the AD4003 part, HDL design configuration, and
a Linux-based evaluation guide using IIO Oscilloscope.

Overview
--------

The
:adi:`AD4003`/:adi:`AD4007`/:adi:`AD4011`/:adi:`AD4020`
are low noise, low power, high speed, 18-bit, precision successive approximation
register (SAR) analog-to-digital converters (ADCs). The
:adi:`AD4003`, :adi:`AD4007`, and
:adi:`AD4011` offer 2 MSPS, 1 MSPS, and 500 kSPS throughputs,
respectively. They incorporate ease of use features that reduce signal chain
power consumption, reduce signal chain complexity, and enable higher channel
density. The high-Z mode, coupled with a long acquisition phase, eliminates the
need for a dedicated high power, high speed ADC driver, thus broadening the
range of low power precision amplifiers that can drive these ADCs directly while
still achieving optimum performance. The input span compression feature enables
the ADC driver amplifier and the ADC to operate off common supply rails without
the need for a negative supply while preserving the full ADC code range. The low
serial peripheral interface (SPI) clock rate requirement reduces the digital
input/output power consumption, broadens processor options, and simplifies the
task of sending data across digital isolation.

The :adi:`ADAQ4003` is an 18-bit precision data acquisition
sub-system SiP design on a laminate that includes the
:adi:`AD4003` ADC with a fully differential driver the ADA4945,
a reference buffer (the ADA4807), a precision resistor iPassive network on a
separate die along with discrete capacitors and resistors. The device solves
many design challenges for a wide range of applications similar to AD400x, yet
it still provides the flexibility. It offers over 75% area savings compared to
discrete design (i.e. Increased channel density and reduced signal chain BOM)
and reduces TTM.

Applications
~~~~~~~~~~~~

- Automatic test equipment
- Machine automation
- Medical equipment
- Battery-powered equipment
- Precision data acquisition systems

Supported Devices
-----------------

- :adi:`AD4003`
- :adi:`AD4007`
- :adi:`AD4011`
- :adi:`AD4020`
- :adi:`ADAQ4003`

Evaluation Boards
-----------------

- :adi:`EVAL-AD400x-FMCZ`
- :adi:`EVAL-ADAQ40xx`

Supported Platforms
-------------------

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
- `CoraZ7 <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development/>`__

HDL Design Description
----------------------

In the `HDL Reference Designs User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
can be found an in-depth presentation and instructions about the HDL design in
general.

The reference design uses the standard
`SPI Engine Framework <https://analogdevicesinc.github.io/hdl/library/spi_engine/index.html>`__
with an integrated pulse generator, which will provide the required conversion
rate for the ADC.

In order to build the HDL design the user has to go through the following steps:

#. Confirm that you have the right tools (the reference design requires Vivado
   2017.4.1)
#. Clone the HDL GitHub repository (the project is located at
   :git-hdl:`projects/ad40xx_fmc`)
#. Set up the required sampling rate (see caption **Design Configuration**)
#. Build the project (see `Building HDL <https://analogdevicesinc.github.io/hdl/user_guide/build_hdl.html>`__)

Design Configuration
~~~~~~~~~~~~~~~~~~~~

The reference design uses an integrated pulse generator to synchronise the
capture events during continuous conversion. The required sampling rate can be
set in
:git-hdl:`system_bd.tcl <projects/ad40xx_fmc/zed/system_bd.tcl>`
file to the required values:

1) Reference clock frequency for SPI interface clock

::

   set spi_clk_ref_frequency 100

2) Device resolution

::

   set adc_resolution 20

3) The targeted sampling rate:

::

   set adc_sampling_rate 1800000

No-OS Software Setup
--------------------

In order to perform the No-OS software setup the user has to go through the
following steps:

#. Confirm that you have the right tools (the reference design requires XSDK)
#. Clone the No-OS GitHub repository (the project is located at
   :git-no-OS:`projects/pulsar-adc`)
#. Follow the instructions provided by
   the :git-no-OS:`project README <projects/pulsar-adc/README.rst>`.

No-OS Driver Description
-------------------------

The driver has two modes of operation:

- single conversion mode
- offload mode

In single conversion mode a single sample is read from the ADC, while in offload
mode a buffer is loaded with a user specified number.

Functions Declarations
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Function
     - Description
   * - ``int32_t ad400x_init(struct ad400x_dev **device, struct ad400x_init_param init_param)``
     - Initialize the device.
   * - ``int32_t ad400x_remove(struct ad400x_dev *dev)``
     - Free the resources allocated by ad400x_init().
   * - ``int32_t ad400x_spi_reg_read(struct ad400x_dev *dev, uint8_t *reg_data)``
     - Read register.
   * - ``int32_t ad400x_spi_reg_write(struct ad400x_dev *dev, uint8_t reg_data)``
     - Write register.
   * - ``int32_t ad400x_spi_single_conversion(struct ad400x_dev *dev, uint32_t *adc_data)``
     - Read a single sample.

Types Declarations
~~~~~~~~~~~~~~~~~~

.. code-block:: c

   enum ad400x_supported_dev_ids{
       ID_AD4003,
       ID_AD4007,
       ID_AD4011,
       ID_AD4020,
   };

   struct ad400x_dev {
       /* SPI */
       spi_desc            *spi_desc;
       /* Device Settings */
       enum ad400x_supported_dev_ids dev_id;
   };

   struct ad400x_init_param {
       /* SPI */
       spi_init_param          spi_init;
       /* Device Settings */
       enum ad400x_supported_dev_ids dev_id;
       uint8_t num_bits;
       bool turbo_mode;
       bool high_z_mode;
       bool span_compression;
       bool en_status_bits;
   };

Linux Evaluation Guide
----------------------

This section describes how to evaluate :adi:`ADAQ4003` and AD400x family
devices using Linux on the supported platforms.

Linux Supported Platforms
~~~~~~~~~~~~~~~~~~~~~~~~~

CoraZ7 Platform
^^^^^^^^^^^^^^^

**Hardware Required**

- :adi:`EVAL-ADAQ40xx`
- `CoraZ7 <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development/>`__
  board
- A signal generator (in this guide :adi:`ADALM2000` is used)
- 16 GB (or larger) Class 10 (or faster) micro-SD card
- 2x Micro-USB cable
- Ethernet cable
- A host computer (Linux or Windows)

**Setting up the Hardware**

The connections for the setup with CoraZ7 are the following:

- Connect :adi:`EVAL-ADAQ40xx` to the JA PMOD port on CoraZ7.
- Connect the host computer to CoraZ7 using a Micro-USB cable.
- Connect the host computer to :adi:`ADALM2000` using a Micro-USB cable.
- Connect :adi:`ADALM2000` probes to :adi:`EVAL-ADAQ40xx`.

The :adi:`ADALM2000` probes do not plug directly into the :adi:`EVAL-ADAQ40xx`
ADC inputs. To work around this, you can use the ADALM2000 BNC Adapter Board
with additional probes to make a tight connection.

Alternatively, you can use long PCB header pins to adapt :adi:`ADALM2000`
female probes to male probes which can then connect to J1 and J2 internal
connections. For the external part of the ADC connectors, carefully curled
jumper wires may do the trick.

.. figure:: m2k_probe_adapt.jpg

   ADALM2000 probe adaptation using PCB header pins

.. figure:: adaq4003_input_adapt.jpg

   EVAL-ADAQ40xx input adaptation

The :adi:`EVAL-ADAQ40xx` configuration measures (IN+ - IN-) as (J2 - J1).
Connect :adi:`ADALM2000` W1 to :adi:`EVAL-ADAQ40xx` J1, :adi:`ADALM2000` W2 to
J2, and :adi:`EVAL-ADAQ40xx` J1, J2 outer connectors to :adi:`ADALM2000` GND.
With that, :adi:`ADAQ4003` readings will convert :adi:`ADALM2000` W2 - W1 which
we will configure in Scopy as CH2 - CH1.

.. figure:: adaq4003-adalm2000-cora-setup.jpg

   ADAQ4003 with ADALM2000 and CoraZ7 setup

ZedBoard Platform
^^^^^^^^^^^^^^^^^

**Hardware Required**

- :adi:`EVAL-AD400x-FMCZ` or :adi:`EVAL-ADAQ40xx`
- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
  Rev D or later
- A signal generator (in this guide :adi:`ADALM2000` is used)
- 16 GB (or larger) Class 10 (or faster) micro-SD card
- Micro-USB cable
- 12 Vdc, 3 A power supply
- Ethernet cable
- User interface setup (choose one):

  - HDMI monitor, keyboard, and mouse plugged directly into the ZedBoard
  - Host Linux/Mac/Windows computer on the same network as the ZedBoard

.. figure:: adaq4003_test_zed_setup.jpg

   ADAQ4003 test setup with ZedBoard

Software Required
~~~~~~~~~~~~~~~~~

- :ref:`kuiper` Image
- A UART terminal (GNU screen, Picocom, Minicom, PuTTY, etc.), baud rate
  115200 (8N1)
- :ref:`iio-oscilloscope`
- `Scopy <https://wiki.analog.com/university/tools/m2k/scopy>`__

Quick Start Guide
~~~~~~~~~~~~~~~~~

Flash Kuiper Linux to the SD Card
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install :ref:`kuiper` to the SD card. Step-by-step imaging guides are available
for
`Linux hosts <https://wiki.analog.com/resources/tools-software/linux-software/zynq_images/linux_hosts>`__
and
`Windows hosts <https://wiki.analog.com/resources/tools-software/linux-software/zynq_images/windows_hosts>`__.

Configuring the SD Card
^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   Linux support for :adi:`ADAQ4003` and similar ADC devices was introduced in
   January 2024. Any :ref:`kuiper` release after that date will have support
   built in.

If using older :ref:`kuiper` releases where no ``zynq-coraz7s-adaq4003`` or
``zynq-zed-adv7511-ad4020`` directory is available, use the boot files from
the table below or follow the subsequent subsections to obtain ``BOOT.BIN``,
``uImage``, and ``devicetree.dtb`` files.

Follow the **Configuring the SD Card for FPGA Projects** section of the
:ref:`kuiper` page.

Copy the following files onto the BOOT partition to configure the SD card:

- **BOOT.BIN** -- Binary blob file which includes the first stage boot loader
  and FPGA bitstream.
- **devicetree.dtb** -- Binary blob containing the specification of what
  hardware is present in the system.
- **uImage** -- Linux kernel image that provides operating system
  functionality.

Getting BOOT.BIN from the HDL Project
""""""""""""""""""""""""""""""""""""""

To achieve high performance with :adi:`ADAQ4003`, the hardware platform must
have an integrated FPGA. To configure the FPGA to properly support
:adi:`ADAQ4003`, ADI engineers provide
`HDL reference projects <https://github.com/analogdevicesinc/hdl>`__ from
which the :git-hdl:`pulsar_adc_pmdz project <projects/pulsar_adc_pmdz>` is
used.

If there is no directory with boot files for your platform of choice under the
SD BOOT partition, follow the build instructions on the
`Building HDL <https://analogdevicesinc.github.io/hdl/user_guide/build_hdl.html>`__
page to build the pulsar project and generate a ``BOOT.BIN`` file.

Getting uImage and devicetree.dtb from the Linux Project
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

If there is no directory with boot files for your platform of choice under the
SD BOOT partition, follow the
`Linux build guide <https://wiki.analog.com/resources/tools-software/linux-build/generic/zynq>`__
to build a new Linux kernel image and device tree blob. After that, replace the
:ref:`kuiper` image with the newly built ``uImage`` and copy the proper
``.dtb`` file for your platform (either ``zynq-coraz7s-adaq4003.dtb`` or
``zynq-zed-adv7511-ad4020.dtb``) from ``arch/arm/boot/dts/`` to the BOOT
partition as ``devicetree.dtb``.

Application Software
~~~~~~~~~~~~~~~~~~~~

:adi:`ADAQ4003` can be managed with :ref:`iio-oscilloscope`, which provides
interfaces for configuring and retrieving data from IIO devices. After
installing IIO Oscilloscope on the host computer, open the application and
connect to the IIO context provided by the :ref:`kuiper` installation running
on the target platform. Both the host machine and the target board must be on
the same network for IIO Oscilloscope to find the correct context.

DMM Tab
^^^^^^^

A quick way of getting data after connecting to the IIO context is to access
the DMM (Digital MultiMeter) tab where single-shot readings from the ADC are
displayed.

.. figure:: iio_osc_conn_adaq4003.gif

   IIO Oscilloscope connection and DMM tab

Debug Tab
^^^^^^^^^

Users can inspect :adi:`ADAQ4003` attributes such as the sampling frequency in
the Debug tab. Edit the value field then click the write button to change
device parameters.

.. figure:: iio_osc_adaq4003_attr.gif

   Inspecting ADAQ4003 attributes in the Debug tab

Buffered Data Capture
^^^^^^^^^^^^^^^^^^^^^

:adi:`ADAQ4003` is a differential ADC and thus converts the difference between
its positive and negative inputs. The :adi:`ADALM2000` can be used to set
different input waveforms to evaluate :adi:`ADAQ4003` performance. Install
`Scopy <https://wiki.analog.com/university/tools/m2k/scopy>`__ on the host
computer to configure :adi:`ADALM2000` output channels.

For a simple test, set a 100 Hz square wave in channel W1 and a 1 kHz sine wave
in channel W2. The difference can then be read with :adi:`ADAQ4003` and the
resulting waveform plotted with IIO Oscilloscope.

.. figure:: iio_osc_adaq4003_buff.gif

   Buffered data capture with 100 Hz square wave (W1) and 1 kHz sine wave (W2)

The next example shows the effect of increasing the sample rate on
characterizing a waveform. With W1 set as a 20 kHz square wave and W2 as a
200 kHz sine wave: at 1 MSPS, the transition from low to high is barely
visible. At 2 MSPS, the resulting waveform is much clearer and the transition
effect is apparent.

.. figure:: iio_osc_adaq4003_buff_2msps.gif

   Buffered data capture at 2 MSPS showing improved waveform characterization

HDL Downloads
-------------

- :git-hdl:`PulSAR ADC HDL Project <projects/pulsar_adc>`

No-OS Downloads
---------------

- :git-no-OS:`PulSAR ADC No-OS Project <projects/pulsar-adc>`
