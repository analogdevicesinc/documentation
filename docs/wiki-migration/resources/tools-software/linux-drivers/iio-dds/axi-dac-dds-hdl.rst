AXI DAC HDL Linux Driver
========================

Supported Devices
-----------------

-  :adi:`AD9122`
-  :adi:`AD9136`
-  :adi:`AD9144`
-  :adi:`AD9152`
-  :adi:`AD9154`
-  :adi:`AD9162`
-  :adi:`AD9171`
-  :adi:`AD9172`
-  :adi:`AD9173`
-  :adi:`AD9174`
-  :adi:`AD9175`
-  :adi:`AD9176`
-  :adi:`AD9361`
-  :adi:`AD9364`
-  :adi:`AD9371`
-  :adi:`AD9739A`
-  :adi:`AD9783`

Supported Boards
----------------

| This driver supports the

-  :doc:`AD-FMCOMMS1-EBZ FMC Card </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz>`
-  :doc:`AD-FMCOMMS2-EBZ FMC Card </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>`
-  :doc:`AD-FMCOMMS3-EBZ FMC Card </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>`
-  :doc:`AD-FMCOMMS4-EBZ FMC Card </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>`
-  :doc:`AD-FMCOMMS5-EBZ FMC Card </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz>`
-  :doc:`AD-FMCOMMS11-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcomms11-ebz>`
-  :doc:`AD-FMCDAQ2-EBZ FMC Card </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz>`
-  :doc:`AD-FMCDAQ3-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcdaq3-ebz>`
-  :doc:`AD9739A Native FMC Card / Xilinx Reference Designs </wiki-migration/resources/fpga/xilinx/fmc/ad9739a>`
-  :doc:`AD9739A Evaluation Board, DAC-FMC Interposer & Xilinx Reference Design </wiki-migration/resources/fpga/xilinx/interposer/ad9739a>`
-  :doc:`EVALUATING THE AD9780/AD9781/AD9783 DIGITAL-TO-ANALOG CONVERTERS </wiki-migration/resources/eval/dpg/eval-ad9783>`
-  :doc:`AD9783 Evaluation Board, DAC-FMC Interposer & Xilinx Reference Design </wiki-migration/resources/fpga/xilinx/interposer/ad9783>`
-  :doc:`ADRV9371 FMC Card </wiki-migration/resources/eval/user-guides/mykonos>`
-  :doc:`ADRV9009 & ADRV9008 Prototyping Platform User Guide </wiki-migration/resources/eval/user-guides/adrv9009>`
-  :doc:`AD9171/AD9172/AD9173/AD9174/AD9175/AD9176 Evaluation Board </wiki-migration/resources/eval/dpg/eval-ad9172>`

Supported HDL Cores
-------------------

-  :doc:`Generic AXI DAC </wiki-migration/resources/fpga/docs/axi_dac_ip>`
-  :doc:`DAC JESD204B Transport Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_tpl_dac>`
-  :doc:`AXI_AD9144 </wiki-migration/resources/fpga/docs/axi_ad9144>`
-  :doc:`AXI_AD9361 </wiki-migration/resources/fpga/docs/axi_ad9361>`
-  :doc:`AXI_AD9371 </wiki-migration/resources/fpga/docs/axi_ad9371>`
-  :doc:`AXI_AD9783 </wiki-migration/resources/fpga/docs/axi_ad9783>`

Sub device Documentation (linked mode)
--------------------------------------

-  :doc:`AD9172 DAC Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9172>`

Description
-----------

The AXI DAC DDS HDL driver is the driver for various HDL interface cores which are used on different FPGA designs. The driver is implemented as an Linux IIO driver. It's register map can be found here: :doc:`Base register map (common to all cores) </wiki-migration/resources/fpga/docs/hdl/regmap>`

This driver is independent from the physical layer. So it's being used with CMOS or LVDS type interfaces or the :doc:`JESD204 Interface Framework </wiki-migration/resources/fpga/peripherals/jesd204>`.

There are basically two use case scenarios for this driver, in which this driver controls only the HDL/FPGA transport layer capture core. This mode is called ``standalone mode``, and the converter is fully configured and controlled by a separate driver. The Linux common clock framework is utilized so that this driver knows the sampling frequency of the connected converter DAC device. Alternatively this driver can also be used in a ``linked mode``, where the converter device typically a SPI device must instantiate first. If this has happened this AXI-DAC driver will then probe as well. (Deferred probe mechanism) Finally both the HDL core platform device together with the converter SPI device will register a common IIO device, which will then exhibit a common set of attributes and channels. The converter SPI device driver is handled in a separate source file, which can be found in the same directory this driver exists. The device tree phandle “spibus-connected” is used to connect the AXI-DAC driver with the SPI control driver.

Sometimes there is a common HDL/FPGA transport layer core, which handles both RX/TX or ADC/DMA. This single physical core is then handled by two independent IIO drivers each for one transport data direction. It’s physical address register space is then also split or divided, typically spaced by 0x4000. A good example for this case is the :doc:`AXI_AD9361 </wiki-migration/resources/fpga/docs/axi_ad9361>` HDL core.

The HDL/FPGA transport layer capture core driver portion implements a polyphase dual tone DDS core per channel together with an DMA based waveform buffer mechanism. The buffer can be filled by arbitrary data, which is then typically cyclically repeated or used in a streaming fashion.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-overview.png
   :align: center
   :width: 800px

Source Code
===========

Status
------

+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Source                                                                                                                            | Mainlined?                                                                                                           |
+===================================================================================================================================+======================================================================================================================+
| :git-linux:`drivers/iio/frequency/cf_axi_dds.c`                                                                                   | `WIP <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/frequency/cf_axi_dds.c>`__ |
+-----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

Files
-----

+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                                                          |
+==========+===============================================================================================================================================================+
| driver   | :git-linux:`drivers/iio/frequency/ad9122.c`                                                                                                                   |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| driver   | :git-linux:`drivers/iio/frequency/ad9144.c`                                                                                                                   |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| driver   | :git-linux:`drivers/iio/frequency/ad9162.c`                                                                                                                   |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| driver   | :git-linux:`drivers/iio/frequency/ad9172.c`                                                                                                                   |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| driver   | :git-linux:`drivers/iio/frequency/cf_axi_dds.c`                                                                                                               |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| driver   | :git-linux:`drivers/iio/frequency/cf_axi_dds_buffer_stream.c`                                                                                                 |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| include  | :git-linux:`drivers/iio/frequency/cf_axi_adc.h <drivers/iio/frequency/cf_axi_dds.h>`                                                                          |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

Example platform device initialization
======================================

The AXI DAC/DDS driver is a platform driver and can only be instantiated via device tree.

Required devicetree properties:

-  **compatible**: Should always be one of these:

   -  adi,axi-ad9122-6.00.a
   -  adi,axi-ad9136-1.0
   -  adi,axi-ad9144-1.0
   -  adi,axi-ad9162-1.0
   -  adi,axi-ad9172-1.0
   -  adi,axi-ad9361x2-dds-6.00.a
   -  adi,axi-ad9361-dds-6.00.a
   -  adi,axi-ad9364-dds-6.00.a
   -  adi,axi-ad9371-tx-1.0
   -  adi,axi-ad9739a-8.00.b
   -  adi,axi-ad9963-dds-1.00.a
   -  adi,axi-adrv9009-tx-1.0

-  **reg**: Base address and register area size. This parameter expects a register range.

Optional Parameters:

-  **adi,axi-dds-default-scale**: The power up DDS scale in 16-bit fractional representation. On driver probe the default mode is DDS with some default frequency at 0.25 Full Scale. Often this behavior is undesired. The best way to mute the DDS on startup is to set this to 0.
-  **adi,axi-dds-default-frequency**: The power up DDS frequency for all tones.
-  **adi,axi-dds-parity-enable**: If set the HDL core uses Parity Mode. (Default is Frame Mode)
-  **adi,axi-dds-parity-type-odd**: If set the HDL core use odd parity. (Default is even)
-  **adi,axi-dds-1-rf-channel**: If set the HDL core expects 1 RF channel. (Default 2 channels)
-  **adi,axi-interpolation-core-available**: If the FPGA system features an additional interpolation filter, this attribute should be set.
-  **adi,axi-pl-fifo-enable**: If the FPGA system features a PL FIFO (Programmable Logic), this attribute should be set.
-  **dmas**: DMA specifiers for the tx dma. See the DMA client binding: Documentation/devicetree/bindings/dma/dma.txt
-  **dma-names**: DMA request name. Should be "tx" if a dma is present.
-  **spibus-connected**: Phandle to the SPI device (control interface) on which the DAC can be found

Example:

::

   &spi0 {
       status = "okay";

       adc0_ad9361: ad9361-phy@0 {
           #address-cells = <1>;
           #size-cells = <0>;
           #clock-cells = <1>;
           compatible = "ad9361";

           /* SPI Setup */
           reg = <0>;
           spi-cpha;
           spi-max-frequency = <10000000>;

           /* Clocks */
           clocks = <&ad9361_clkin 0>;
           clock-names = "ad9361_ext_refclk";
           clock-output-names = "rx_sampl_clk", "tx_sampl_clk";

       [--- snip ---]

       }
   }

   &fpga_axi {
       tx_dma: dma@7c420000 {
           compatible = "adi,axi-dmac-1.00.a";
           reg = <0x7c420000 0x10000>;
           #dma-cells = <1>;
           interrupts = <0 56 0>;
           clocks = <&clkc 16>;

           dma-channel {
               adi,source-bus-width = <64>;
               adi,destination-bus-width = <64>;
               adi,type = <1>;
               adi,cyclic;
           };
       };

       cf_ad9361_dac_core_0: cf-ad9361-dds-core-lpc@79024000 {
           compatible = "adi,axi-ad9361-dds-6.00.a";
           reg = <0x79024000 0x1000>;
           clocks = <&adc0_ad9361 13>;
           clock-names = "sampl_clk";
           dmas = <&tx_dma 0>;
           dma-names = "tx";
           adi,axi-dds-default-scale = <0>;
       };
   };  

Enabling Linux driver support
=============================

Configure kernel with "make menuconfig" (alternatively use "make xconfig" or "make qconfig")

.. hint::

   The AXI ADC HDL driver may depend on **CONFIG_SPI**


Adding Linux driver support
===========================

Configure kernel with "make menuconfig" (alternatively use "make xconfig" or "make qconfig")

::

   Linux Kernel Configuration
       Device Drivers  --->
       <*>     Industrial I/O support --->
           --- Industrial I/O support
           -*-   Enable ring buffer support within IIO
           -*-     Industrial I/O lock free software ring
           -*-   Enable triggered sampling support

                 *** Direct Digital Synthesis ***
           [--snip--]

           <*>   Analog Devices CoreFPGA AXI DDS driver
           <*>   Analog Devices AD9122 DAC

           [--snip--]

Hardware configuration
======================

In case the driver probes successfully and the device gets instantiated. Your systems kernel messages should include a line, which may look like the one shown below.

::

   cf_axi_dds 79024000.cf-ad9361-dds-core-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (8.00.b) at 0x79024000 mapped to 0xf0998000, probed DDS AD9361

Driver testing
==============

Each and every IIO device, typically a hardware chip, has a device folder under /sys/bus/iio/devices/iio:deviceX. Where X is the IIO index of the device. Under every of these directory folders reside a set of files, depending on the characteristics and features of the hardware device in question. These files are consistently generalized and documented in the IIO ABI documentation. In order to determine which IIO deviceX corresponds to which hardware device, the user can read the name file /sys/bus/iio/devices/iio:deviceX/name. In case the sequence in which the iio device drivers are loaded/registered is constant, the numbering is constant and may be known in advance.


Some device attributes control the DDS HDL Core, others features of the DAC and associated clock providers.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      analog:/sys/bus/iio/devices/iio:device2# **cd /sys/bus/iio/devices/**
      root@analog:/sys/bus/iio/devices# **ls**
      iio:device0  iio:device1  iio:device2  iio:device3
      root@analog:/sys/bus/iio/devices#
   
      root@analog:/sys/bus/iio/devices# **cd iio\:device2**
      root@analog:/sys/bus/iio/devices/iio:device2# **ls -l**
      total 0
      drwxr-xr-x 5 root root    0 Jan  1 00:00 .
      drwxr-xr-x 4 root root    0 Jan  1 00:00 ..
      drwxrwxrwx 2 root root    0 Jan  1 00:00 buffer
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 dev
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 name
      lrwxrwxrwx 1 root root    0 Jan  1 00:00 of_node -> ../../../../../firmware/devicetree/base/fpga-axi@0/cf-ad9361-dds-core-lpc@79024000
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage0_TX1_I_F1_frequency
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage0_TX1_I_F1_phase
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage0_TX1_I_F1_raw
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage0_TX1_I_F1_scale
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage1_TX1_I_F2_frequency
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage1_TX1_I_F2_phase
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage1_TX1_I_F2_raw
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage1_TX1_I_F2_scale
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage2_TX1_Q_F1_frequency
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage2_TX1_Q_F1_phase
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage2_TX1_Q_F1_raw
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage2_TX1_Q_F1_scale
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage3_TX1_Q_F2_frequency
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage3_TX1_Q_F2_phase
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage3_TX1_Q_F2_raw
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage3_TX1_Q_F2_scale
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage4_TX2_I_F1_frequency
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage4_TX2_I_F1_phase
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage4_TX2_I_F1_raw
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage4_TX2_I_F1_scale
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage5_TX2_I_F2_frequency
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage5_TX2_I_F2_phase
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage5_TX2_I_F2_raw
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage5_TX2_I_F2_scale
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage6_TX2_Q_F1_frequency
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage6_TX2_Q_F1_phase
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage6_TX2_Q_F1_raw
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage6_TX2_Q_F1_scale
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage7_TX2_Q_F2_frequency
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage7_TX2_Q_F2_phase
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage7_TX2_Q_F2_raw
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage7_TX2_Q_F2_scale
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_altvoltage_sampling_frequency
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_voltage0_calibphase
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_voltage0_calibscale
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_voltage1_calibphase
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_voltage1_calibscale
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_voltage2_calibphase
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_voltage2_calibscale
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_voltage3_calibphase
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_voltage3_calibscale
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 out_voltage_sampling_frequency
      drwxrwxrwx 2 root root    0 Jan  1 00:00 power
      drwxrwxrwx 2 root root    0 Jan  1 00:00 scan_elements
      lrwxrwxrwx 1 root root    0 Jan  1 00:00 subsystem -> ../../../../../bus/iio
      -rw-rw-rw- 1 root root 4096 Jan  1 00:00 uevent
      root@analog:/sys/bus/iio/devices/iio:device2#
   


Show device name
~~~~~~~~~~~~~~~~

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device2# **cat name**
      cf-ad9361-dds-core-lpc
   


Show/Set DDS frequency
~~~~~~~~~~~~~~~~~~~~~~

Values are in Hz.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device2# **cat out_altvoltage0_TX1_I_F1_frequency**
      9279985
      root@analog:/sys/bus/iio/devices/iio:device2# **echo 500000 > out_altvoltage0_TX1_I_F1_frequency**
      root@analog:/sys/bus/iio/devices/iio:device2# **cat out_altvoltage0_TX1_I_F1_frequency**
      500163
   


Show/Set DDS Phase
~~~~~~~~~~~~~~~~~~

Values are in milli degrees.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device2# **cat out_altvoltage0_TX1_I_F1_phase**
      89995
      root@analog:/sys/bus/iio/devices/iio:device2# **echo 91000 > out_altvoltage0_TX1_I_F1_phase**
      root@analog:/sys/bus/iio/devices/iio:device2# **cat out_altvoltage0_TX1_I_F1_phase**
      90995
   


Enable/Disable DDS Channel
~~~~~~~~~~~~~~~~~~~~~~~~~~

1 for enable, 0 for disable.

With the introduction of the big channel MUX (REG_CHAN_CNTRL_7, DAC_DDS_SEL) starting with HDV Version > 7.00, the RAW attribute has some side effects, that need to be understood. In many situations for example when the Buffer mode is used, it’s not desirable to write this attribute.

HDL Version < 7.00.a
^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/iio-dds/dds_data_sel_v7-.png
   :width: 500px

.. _hdl-version-7.00.a-1:

HDL Version > 7.00.a
^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/iio-dds/dds_data_sel_v7+.png
   :width: 500px

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device2# **cat out_altvoltage0_TX1_I_F1_raw**
      1
   


Show/Set DDS Scale
~~~~~~~~~~~~~~~~~~

DDS amplitude: range 0.00 ... 1.00 (relative to full scale)

.. tip::

   When disabling the DAC Buffer/DMA mode and a transition into DDS tone output mode is not desired - Scale of all channels should be set to 0.00. See also device tree attribute: adi,axi-dds-default-scale


.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device2# **cat out_altvoltage0_TX1_I_F1_scale**
      0.500000
      root@analog:/sys/bus/iio/devices/iio:device2# **cat out_altvoltage0_TX1_I_F1_scale**
      1.000000 0.500000 0.250000 0.125000 ...
      root@analog:/sys/bus/iio/devices/iio:device2# **echo 0.25 > out_altvoltage0_TX1_I_F1_scale**
      root@analog:/sys/bus/iio/devices/iio:device2# **cat out_altvoltage0_TX1_I_F1_scale**
      0.250000
   


DAC internal or external Gain, DC Offset, and Phase adjustments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Depending on the platform. These attributes may control converter internal or external processing blocks.

The AD9122 features Gain, DC Offset, and Phase adjustment for sideband suppression. These features can be controlled via following attributes:

-  out_voltage0_calibbias
-  out_voltage0_calibscale
-  out_voltage0_phase
-  out_voltage1_calibbias
-  out_voltage1_calibscale
-  out_voltage1_phase

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device2# **grep "" out_voltage* **
      out_voltage0_calibbias:0
      out_voltage0_calibscale:505
      out_voltage0_phase:0
      out_voltage1_calibbias:0
      out_voltage1_calibscale:505
      out_voltage1_phase:0
   


External synchronization
~~~~~~~~~~~~~~~~~~~~~~~~

The :doc:`DAC TPL HDL </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_tpl_dac>` core supports the :doc:`EXT_SYNC </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_tpl_dac>` feature, allowing to synchronize multiple channels within a DAC or across multiple instances. This feature can also synchronize between the :doc:`ADC TPL HDL </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_tpl_adc>` and :doc:`DAC TPL HDL </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_tpl_dac>` core.

There are two device attributes which allows controlling this feature: ``sync_start_enable`` and ``sync_start_enable_available`` reading the later returns the available modes which depend on HDL core synthesis parameters. The options are explained below. Reading 'sync_start_enable' returns either 'arm' while waiting for the external synchronization signal or 'disarm' otherwise.

-  ``arm``: Setting this key will arm the trigger mechanism sensitive to an external sync signal. Once the external sync signal goes high it synchronizes channels within a DAC, and across multiple instances. This key has an effect only the EXT_SYNC synthesis parameter is set.

-  ``disarm``: Setting this key will disarm the trigger mechanism sensitive to an external sync signal. This key has an effect only the EXT_SYNC synthesis parameter is set.

-  ``trigger_manual``: Setting this key will issue an external sync event if it is hooked up inside the fabric. This key has an effect only the EXT_SYNC synthesis parameter is set.

Example:
^^^^^^^^

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device3# **cat sync_start_enable_available**                                                                                                                       
      **arm disarm trigger_manual**
      root@analog:/sys/bus/iio/devices/iio:device3# **cat sync_start_enable**
      **disarm**
      root@analog:/sys/bus/iio/devices/iio:device3# **echo arm > sync_start_enable**                                                                                                                                 
      root@analog:/sys/bus/iio/devices/iio:device3# **cat sync_start_enable**
      **arm**
      root@analog:/sys/bus/iio/devices/iio:device3# **echo trigger_manual > sync_start_enable**                                                                                                                      
      root@analog:/sys/bus/iio/devices/iio:device3# **cat sync_start_enable**
      **disarm**
   


Buffer management
-----------------

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/bus/iio/devices/iio:device3> **ls -l buffer**
      total 0
      -rw-r--r--    1 root     root          4096 Jan  1 00:12 enable
      -rw-r--r--    1 root     root          4096 Jan  1 00:12 length
      -r--r--r--    1 root     root          4096 Jan  1 00:12 watermark
   


The Industrial I/O subsystem provides support for various ring buffer based data acquisition methods. Apart from device specific hardware buffer support, the user can chose between two different software ring buffer implementations. One is the IIO lock free software ring, and the other is based on Linux kfifo. Devices with buffer support feature an additional sub-folder in the /sys/bus/iio/devices/deviceX/ folder hierarchy. Called deviceX:bufferY, where Y defaults to 0, for devices with a single buffer.

Every buffer implementation features a set of files:

| **length**
| Get/set the number of sample sets that may be held by the buffer.

| **enable**
| Enables/disables the buffer. This file should be written last, after length and selection of scan elements.

| **watermark**
| A single positive integer specifying the maximum number of scan elements to wait for. Poll will block until the watermark is reached. Blocking read will wait until the minimum between the requested read amount or the low water mark is available. Non-blocking read will retrieve the available samples from the buffer even if there are less samples then watermark level. This allows the application to block on poll with a timeout and read the available samples after the timeout expires and thus have a maximum delay guarantee.

| **data_available**
| A read-only value indicating the bytes of data available in the buffer. In the case of an output buffer, this indicates the amount of empty space available to write data to. In the case of an input buffer, this indicates the amount of data available for reading.

| **length_align_bytes**
| Using the high-speed interface. DMA buffers may have an alignment requirement for the buffer length. Newer versions of the kernel will report the alignment requirements associated with a device through the \`length_align_bytes\` property.

| **scan_elements**
| The scan_elements directory contains interfaces for elements that will be captured for a single triggered sample set in the buffer.


.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/bus/iio/devices/iio:device3> **ls -l scan_elements**
      total 0
      -rw-r--r--    1 root     root          4096 Jan  1 00:00 out_voltage0_en
      -r--r--r--    1 root     root          4096 Jan  1 00:00 out_voltage0_index
      -r--r--r--    1 root     root          4096 Jan  1 00:00 out_voltage0_type
      -rw-r--r--    1 root     root          4096 Jan  1 00:00 out_voltage1_en
      -r--r--r--    1 root     root          4096 Jan  1 00:00 out_voltage1_index
      -r--r--r--    1 root     root          4096 Jan  1 00:00 out_voltage1_type
   


| **in_voltageX_en / in_voltageX-voltageY_en / timestamp_en:**
| Scan element control for triggered data capture. Writing 1 will enable the scan element, writing 0 will disable it

| **in_voltageX_type / in_voltageX-voltageY_type / timestamp_type:**
| Description of the scan element data storage within the buffer and therefore in the form in which it is read from user-space. Form is [s|u]bits/storage-bits. s or u specifies if signed (2's complement) or unsigned. bits is the number of bits of data and storage-bits is the space (after padding) that it occupies in the buffer. Note that some devices will have additional information in the unused bits so to get a clean value, the bits value must be used to mask the buffer output value appropriately. The storage-bits value also specifies the data alignment. So u12/16 will be a unsigned 12 bit integer stored in a 16 bit location aligned to a 16 bit boundary. For other storage combinations this attribute will be extended appropriately.

| **in_voltageX_index / in_voltageX-voltageY_index / timestamp_index:**
| A single positive integer specifying the position of this scan element in the buffer. Note these are not dependent on what is enabled and may not be contiguous. Thus for user-space to establish the full layout these must be used in conjunction with all \_en attributes to establish which channels are present, and the relevant \_type attributes to establish the data storage format.


Low level register access
-------------------------

This page contains a few lose documentation snippets used in various spots.

IIO device files
================

Each and every IIO device, typically a hardware chip, has a device folder under /sys/bus/iio/devices/iio:deviceX. Where X is the IIO index of the device. Under every of these directory folders reside a set of files, depending on the characteristics and features of the hardware device in question. These files are consistently generalized and documented in the IIO ABI documentation. In order to determine which IIO deviceX corresponds to which hardware device, the user can read the name file /sys/bus/iio/devices/iio:deviceX/name. In case the sequence in which the iio device drivers are loaded/registered is constant, the numbering is constant and may be known in advance.

IIO devices with trigger consumer interface
===========================================

If deviceX supports triggered sampling, it’s a so called trigger consumer and there will be an additional folder /sys/bus/iio/device/iio:deviceX/trigger. In this folder there is a file called current_trigger, allowing controlling and viewing the current trigger source connected to deviceX. Available trigger sources can be identified by reading the name file /sys/bus/iio/devices/triggerY/name. The same trigger source can connect to multiple devices, so a single trigger may initialize data capture or reading from a number of sensors, converters, etc.

|

.. hint::

   **Trigger Consumers:**

   | Currently triggers are only used for the filling of software ring buffers and as such any device supporting INDIO_RING_TRIGGERED has the consumer interface automatically created.


**Description:** Read name of triggerY

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/bus/iio/devices/triggerY/> **cat name**
      irqtrig56
   


**Description:** Make irqtrig56 (trigger using system IRQ56, likely a GPIO IRQ), to current trigger of deviceX

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/bus/iio/devices/iio:deviceX/trigger> **echo irqtrig56 > current_trigger**
   


**Description:** Read current trigger source of deviceX

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/bus/iio/devices/iio:deviceX/trigger> **cat current_trigger**
      irqtrig56
   


Standalone trigger drivers
==========================

+-----------------------------------------------+-------------------------------------------------------------------------------+
| name                                          | description                                                                   |
+===============================================+===============================================================================+
| iio-trig-gpio                                 | Provides support for using GPIO pins as IIO triggers.                         |
+-----------------------------------------------+-------------------------------------------------------------------------------+
| iio-trig-rtc                                  | Provides support for using periodic capable real time clocks as IIO triggers. |
+-----------------------------------------------+-------------------------------------------------------------------------------+
| `iio-trig-sysfs <iio-trig-sysfs>`__           | Provides support for using SYSFS entry as IIO triggers.                       |
+-----------------------------------------------+-------------------------------------------------------------------------------+
| `iio-trig-bfin-timer <iio-trig-bfin-timer>`__ | Provides support for using a Blackfin timer as IIO triggers.                  |
+-----------------------------------------------+-------------------------------------------------------------------------------+

Buffer management
=================

The Industrial I/O subsystem provides support for various ring buffer based data acquisition methods. Apart from device specific hardware buffer support, the user can chose between two different software ring buffer implementations. One is the IIO lock free software ring, and the other is based on Linux kfifo. Devices with buffer support feature an additional sub-folder in the /sys/bus/iio/devices/deviceX/ folder hierarchy. Called deviceX:bufferY, where Y defaults to 0, for devices with a single buffer.

Every buffer implementation features a set of files:

| **length**
| Get/set the number of sample sets that may be held by the buffer.

| **enable**
| Enables/disables the buffer. This file should be written last, after length and selection of scan elements.

| **watermark**
| A single positive integer specifying the maximum number of scan elements to wait for. Poll will block until the watermark is reached. Blocking read will wait until the minimum between the requested read amount or the low water mark is available. Non-blocking read will retrieve the available samples from the buffer even if there are less samples then watermark level. This allows the application to block on poll with a timeout and read the available samples after the timeout expires and thus have a maximum delay guarantee.

| **data_available**
| A read-only value indicating the bytes of data available in the buffer. In the case of an output buffer, this indicates the amount of empty space available to write data to. In the case of an input buffer, this indicates the amount of data available for reading.

| **length_align_bytes**
| Using the high-speed interface. DMA buffers may have an alignment requirement for the buffer length. Newer versions of the kernel will report the alignment requirements associated with a device through the \`length_align_bytes\` property.

| **scan_elements**
| The scan_elements directory contains interfaces for elements that will be captured for a single triggered sample set in the buffer.

Typical ADC scan elements
=========================

| **in_voltageX_en / in_voltageX-voltageY_en / timestamp_en:**
| Scan element control for triggered data capture. Writing 1 will enable the scan element, writing 0 will disable it

| **in_voltageX_type / in_voltageX-voltageY_type / timestamp_type:**
| Description of the scan element data storage within the buffer and therefore in the form in which it is read from user-space. Form is [s|u]bits/storage-bits. s or u specifies if signed (2's complement) or unsigned. bits is the number of bits of data and storage-bits is the space (after padding) that it occupies in the buffer. Note that some devices will have additional information in the unused bits so to get a clean value, the bits value must be used to mask the buffer output value appropriately. The storage-bits value also specifies the data alignment. So u12/16 will be a unsigned 12 bit integer stored in a 16 bit location aligned to a 16 bit boundary. For other storage combinations this attribute will be extended appropriately.

| **in_voltageX_index / in_voltageX-voltageY_index / timestamp_index:**
| A single positive integer specifying the position of this scan element in the buffer. Note these are not dependent on what is enabled and may not be contiguous. Thus for user-space to establish the full layout these must be used in conjunction with all \_en attributes to establish which channels are present, and the relevant \_type attributes to establish the data storage format.

Event Management
================

The Industrial I/O subsystem provides support for passing hardware generated events up to userspace.

In IIO events are not used for passing normal readings from the sensing devices to userspace, but rather for out of band information. Normal data reaches userspace through a low overhead character device - typically via either software or hardware buffer. The stream format is pseudo fixed, so is described and controlled via sysfs rather than adding headers to the data describing what is in it.

Pretty much all IIO events correspond to thresholds on some value derived from one or more raw readings from the sensor. They are provided by the underlying hardware.

**Examples include:**

-  Straight crossing a voltage threshold
-  Moving average crosses a threshold
-  Motion detectors (lots of ways of doing this).
-  Thresholds on sum squared or rms values.
-  Rate of change thresholds.
-  Lots more variants...

Events have timestamps.

**The Interface:**

-  Single user at a time.

-  Simple chrdev per device (aggregation across devices doesn't really make sense for IIO as you tend to really care which sensor caused the event rather than just that it happened.)

**The format is:**

.. code:: c

   /**
    * struct iio_event_data - The actual event being pushed to userspace
    * @id:     event identifier
    * @timestamp:  best estimate of time of event occurrence (often from
    *      the interrupt handler)
    */
   struct iio_event_data {
       u64 id;
       s64 timestamp;
   };

Typical event attributes
========================

| **/sys/bus/iio/devices/iio:deviceX/events**
| Configuration of which hardware generated events are passed up to user-space.

-  **Threshold Events:**

| **<type>Z[\_name]_thresh[\_rising|falling]_en**
| Event generated when channel passes a threshold in the specified (\_rising|_falling) direction. If the direction is not specified, then either the device will report an event which ever direction a single threshold value is called in (e.g. <type>[Z][\_name]\_<raw|input>_thresh_value) or <type>[Z][\_name]\_<raw|input>_thresh_rising_value and <type>[Z][\_name]\_<raw|input>_thresh_falling_value may take different values, but the device can only enable both thresholds or neither. Note the driver will assume the last p events requested are to be enabled where p is however many it supports (which may vary depending on the exact set requested. So if you want to be sure you have set what you think you have, check the contents of these attributes after everything is configured. Drivers may have to buffer any parameters so that they are consistent when a given event type is enabled a future point (and not those for whatever event was previously enabled).

| **<type>Z[\_name]_thresh[\_rising|falling]_value**
| Specifies the value of threshold that the device is comparing against for the events enabled by <type>Z[\_name]_thresh[\_rising|falling]_en. If separate attributes exist for the two directions, but direction is not specified for this attribute, then a single threshold value applies to both directions. The raw or input element of the name indicates whether the value is in raw device units or in processed units (as \_raw and \_input do on sysfs direct channel read attributes).

-  **Rate of Change Events:**

| **<type>[Z][\_name]_roc[\_rising|falling]_en**
| Event generated when channel passes a threshold on the rate of change (1st differential) in the specified (\_rising|_falling) direction. If the direction is not specified, then either the device will report an event which ever direction a single threshold value is called in (e.g. <type>[Z][\_name]\_<raw|input>_roc_value) or <type>[Z][\_name]\_<raw|input>_roc_rising_value and <type>[Z][\_name]\_<raw|input>_roc_falling_value may take different values, but the device can only enable both rate of change thresholds or neither. Note the driver will assume the last p events requested are to be enabled where p is however many it supports (which may vary depending on the exact set requested. So if you want to be sure you have set what you think you have, check the contents of these attributes after everything is configured. Drivers may have to buffer any parameters so that they are consistent when a given event type is enabled a future point (and not those for whatever event was previously enabled).

| **<type>[Z][\_name]_roc[\_rising|falling]_value**
| Specifies the value of rate of change threshold that the device is comparing against for the events enabled by <type>[Z][\_name]_roc[\_rising|falling]_en. If separate attributes exist for the two directions, but direction is not specified for this attribute, then a single threshold value applies to both directions. The raw or input element of the name indicates whether the value is in raw device units or in processed units (as \_raw and \_input do on sysfs direct channel read attributes).

-  **Magnitude Events:**

| **<type>Z[\_name]_mag[\_rising|falling]_en**
| Similar to in_accel_x_thresh[\_rising|_falling]_en, but here the magnitude of the channel is compared to the threshold, not its signed value.

| **<type>Z[\_name]_mag[\_rising|falling]_value**
| The value to which the magnitude of the channel is compared. If number or direction is not specified, applies to all channels of this type.

-  **Temporal Conditions:**

| **<type>[Z][\_name][\_thresh|_roc][\_rising|falling]_period**
| Period of time (in seconds) for which the condition must be met before an event is generated. If direction is not specified then this period applies to both directions.

Low level register access via debugfs (direct_reg_access)
=========================================================

Some IIO drivers feature an optional debug facility, allowing users to read or write registers directly. Special care needs to be taken when using this feature, since you can modify registers on the back of the driver.

.. tip::

   To simplify direct register access you may want to use the libiio :doc:`iio_reg </wiki-migration/resources/tools-software/linux-software/libiio/iio_reg>` command line utility.


Accessing debugfs requires root privileges.

In order to identify if the IIO device in question feature this option you first need to identify the IIO device number.

Therefore read the name attribute of each IIO device

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# grep "" /sys/bus/iio/devices/iio\:device*/name
      /sys/bus/iio/devices/iio:device0/name:ad7291
      /sys/bus/iio/devices/iio:device1/name:ad9361-phy
      /sys/bus/iio/devices/iio:device2/name:xadc
      /sys/bus/iio/devices/iio:device3/name:adf4351-udc-rx-pmod
      /sys/bus/iio/devices/iio:device4/name:adf4351-udc-tx-pmod
      /sys/bus/iio/devices/iio:device5/name:cf-ad9361-dds-core-lpc
      /sys/bus/iio/devices/iio:device6/name:cf-ad9361-lpc
      root@analog:~# 
   


Change directory to **/sys/kernel/debug**/iio/ iio:deviceX and check if the direct_reg_access file exists.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# cd /sys/kernel/debug/iio/iio\:device1
      root@analog:/sys/kernel/debug/iio/iio:device1# ls direct_reg_access 
      direct_reg_access
   


**Reading**

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/kernel/debug/iio/iio:device1# echo 0x7 > direct_reg_access                                                                                                                                 
      root@analog:/sys/kernel/debug/iio/iio:device1# cat direct_reg_access 
      0x40
   


**Writing**

Write ADDRESS VALUE

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/kernel/debug/iio/iio:device1# echo 0x7 0x50  > direct_reg_access                                                                                                                            
      root@analog:/sys/kernel/debug/iio/iio:device1# cat direct_reg_access 
      0x50
   


**Accessing HDL CORE registers**

| Special ADI device driver convention for devices that have both:
| \* a SPI/I2C control interface

-  and some sort of HDL Core with registers (AXI)

In this case when accessing the HDL Core Registers always set BIT31.

The register map for typical ADI HDL cores can be found here: :doc:`Register Map </wiki-migration/resources/fpga/docs/hdl/regmap>`

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/kernel/debug/iio/iio:device6# echo 0x80000000 > direct_reg_access                                                                                                                           
      root@analog:/sys/kernel/debug/iio/iio:device6# cat direct_reg_access 
      0x80062
   


IIO pointers
============

-  IIO mailing list: linux-iio@vger.kernel.org
-  `IIO Linux Kernel Documentation sysfs-bus-iio-\* <https://www.kernel.org/doc/Documentation/ABI/testing>`__
-  `IIO Documentation <https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-bus-iio>`__
-  :doc:`IIO test and visualization application </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`libiio - IIO system library </wiki-migration/resources/tools-software/linux-software/libiio>`
-  :doc:`libiio - Internals </wiki-migration/resources/tools-software/linux-software/libiio_internals>`
-  :doc:`Pointers and good books </wiki-migration/resources/tools-software/pointers>`
-  `IIO High Speed <https://events.static.linuxfound.org/sites/events/files/slides/iio_high_speed.pdf>`__
-  `Software Defined Radio using the IIO framework <http://video.fosdem.org/2015/devroom-software_defined_radio/iiosdr.mp4>`__
-

|libiio introduction|

.. image:: https://wiki.analog.com/_media/page>resources/tools-software/linux-drivers/need_help#need help&noheader&firstseconly&noeditbtn
   :alt: page>resources/tools-software/linux-drivers/need_help#need help&noheader&firstseconly&noeditbtn

.. |libiio introduction| image:: https://wiki.analog.com/_media/youtube>p_VntEwUe24


AD9122 Clocking concept
-----------------------

There are three different clocks associated with the DAC.

-  Data/Interface Clock (DCI)
-  DAC Clock (DACCLK)
-  Reference Clock (REFCLK)

The Data/Interface Clock (DCI) is shared with the DDS HDL Core.

The default AD9122 driver configuration uses a concept called Direct Clocking. This means an external clock provider must supply DCI and DACCLK. In case the DAC interpolation feature is not used and the DAC operates in Word-Mode then DCI = DACCLK.

| When N interpolation is used following equation must be satisfied.
| N = {1, 2, 4, 8}
| DACCLK = N \* DCI and DACCLK <= 1230MHz
| The *out_altvoltage_interpolation_frequency_available* attribute allows you to query the supported interpolation frequencies for a given Interface Clock (*out_altvoltage_X_sampling_frequency*) by exercising possible settings on the clock provider. In case the clock provider is not capable providing exactly the requested rate, the mode is removed from the list.

**So following example:**

| Assuming the clock provider can only provide following rates: 1000MHz / X, X = {1..1023}.
| This results in following rates:
| 1000, 500, 333.33, 250, 200, 166.66, 142.85, 125, 111.11, ...

-  In case the interface clock is set to 125MHz, then 1x, 2x, 4x and 8x interpolation is possible.

-  Assuming the interface clock is set to 166.66MHz, then only 1x, 2x interpolation is possible. 4x interpolation won't work since 666.66MHz cannot be supplied by the clock provider.

The half-band interpolation filters have selectable pass bands that allow the center frequencies to be moved in increments of one-half their input data rate. The premodulation block provides a digital upconversion of the incoming waveform by one-half the incoming data rate, fDATA. This can be used to frequency-shift base- band input data to the center of the interpolation filter pass band.

The available center shift frequencies for a given Interface Clock (*out_altvoltage_X_sampling_frequency*), can be queried using the *out_altvoltage_interpolation_center_shift_frequency_availabl*\ e attribute.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@linaro-ubuntu-desktop:/sys/bus/iio/devices/iio:device4# **cat out_altvoltage_1A_sampling_frequency**
      491520000
   
      root@linaro-ubuntu-desktop:/sys/bus/iio/devices/iio:device4# **cat out_altvoltage_interpolation_frequency_available**
      491520000 983040000
   
      root@linaro-ubuntu-desktop:/sys/bus/iio/devices/iio:device4# **cat out_altvoltage_interpolation_frequency**
      491520000
   
      root@linaro-ubuntu-desktop:/sys/bus/iio/devices/iio:device4# **cat out_altvoltage_interpolation_center_shift_frequency**
      0
   


.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
   
      //[ Set data clock to 122.88 MHz ]//
   
      root@linaro-ubuntu-desktop:/sys/bus/iio/devices/iio:device4# **echo 122880000 > out_altvoltage_1A_sampling_frequency**
   
      //[ List available interpolation DAC frequencies ]//
   
      root@linaro-ubuntu-desktop:/sys/bus/iio/devices/iio:device4# **cat out_altvoltage_interpolation_frequency_available**
      122880000 245760000 491520000 983040000
   
      //[ Select 8x interpolation ]//
   
      root@linaro-ubuntu-desktop:/sys/bus/iio/devices/iio:device4# **echo 983040000 > out_altvoltage_interpolation_frequency**
   
      //[ List available center shift frequencies ]//
   
      root@linaro-ubuntu-desktop:/sys/bus/iio/devices/iio:device4# **cat out_altvoltage_interpolation_center_shift_frequency_available**
      0 61440000 122880000 184320000 245760000 307200000 368640000 430080000 491520000 552960000 614400000 675840000 737280000 798720000 860160000 921600000
   
      //[ Select 2x interpolation ]//
   
      root@linaro-ubuntu-desktop:/sys/bus/iio/devices/iio:device4# **echo 245760000 > out_altvoltage_interpolation_frequency**
   
      //[ List available center shift frequencies ]//
   
      root@linaro-ubuntu-desktop:/sys/bus/iio/devices/iio:device4# **cat out_altvoltage_interpolation_center_shift_frequency_available**
      0 61440000 122880000 184320000
   
      //[ Select center shift frequencies ]//
   
      root@linaro-ubuntu-desktop:/sys/bus/iio/devices/iio:device4# **echo 61440000 > out_altvoltage_interpolation_center_shift_frequency**
   


More Information
================

-  IIO mailing list: linux-iio@vger.kernel.org
-  `IIO Linux Kernel Documentation sysfs-bus-iio-\* <https://www.kernel.org/doc/Documentation/ABI/testing>`__
-  `IIO Documentation <https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-bus-iio>`__
-  :doc:`IIO test and visualization application </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`libiio - IIO system library </wiki-migration/resources/tools-software/linux-software/libiio>`
-  :doc:`libiio - Internals </wiki-migration/resources/tools-software/linux-software/libiio_internals>`
-  :doc:`Pointers and good books </wiki-migration/resources/tools-software/pointers>`
-  `IIO High Speed <https://events.static.linuxfound.org/sites/events/files/slides/iio_high_speed.pdf>`__
-  `Software Defined Radio using the IIO framework <http://video.fosdem.org/2015/devroom-software_defined_radio/iiosdr.mp4>`__
-

|libiio introduction|

.. image:: https://wiki.analog.com/_media/page>resources/tools-software/linux-drivers/need_help#need help&noheader&firstseconly&noeditbtn
   :alt: page>resources/tools-software/linux-drivers/need_help#need help&noheader&firstseconly&noeditbtn

.. |libiio introduction| image:: https://wiki.analog.com/_media/youtube>p_VntEwUe24

