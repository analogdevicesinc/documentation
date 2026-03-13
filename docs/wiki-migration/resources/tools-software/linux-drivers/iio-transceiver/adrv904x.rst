ADRV904x Integrated Radio Frequency Transceiver Linux device driver
===================================================================

The :adi:`ADRV9040 <en/products/adrv9040.html>` is a highly integrated, radio frequency (RF) agile transceiver offering eight transmitters, two observation receivers for monitoring transmitter channels, eight receivers, integrated LO and clock synthesizers, and digital signal processing functions to provide a complete transceiver solution. The device provides the high radio performance and low power consumption demanded by cellular infrastructure applications such as small cell basestation radios, macro 3G/4G/5G systems, and massive MIMO base stations.

Supported Devices
-----------------

-  :adi:`ADRV9040 <en/products/adrv9040.html>`

Evaluation Boards
-----------------

-  :adi:`ADRV904x-HB/PCBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADRV9026.html>`

Overview
--------

The ADRV9040 is a highly integrated, system on chip (SoC) radio frequency (RF)
agile transceiver with integrated digital front end (DFE). The SoC contains
eight transmitters, two observation receivers for monitoring transmitter
channels, eight receivers, integrated LO and clock synthesizers, and digital
signal processing functions. The SoC meets the high radio performance and low
power consumption demanded by cellular infrastructure applications including
small cell basestation radios, macro 3G/4G/5G systems, and massive MIMO base
stations.

The Rx and Tx signal paths use a zero-IF (ZIF) architecture that provides wide
bandwidth with dynamic range suitable for contiguous and noncontiguous
multicarrier base station applications. The ZIF architecture has the benefits of
low power plus RF frequency and bandwidth agility. The lack of aliases and
out-of-band images eliminates anti-aliasing and image filters. This reduces both
system size and cost, also making band independent solutions possible.

The device also includes two wide-bandwidth observation path receiver
sub-systems for monitoring transmitter outputs. This SoC subsystem includes
automatic and manual attenuation control, dc offset correction, quadrature error
correction (QEC), and digital filtering. GPIOs that provide an array of digital
control options are also integrated.

Multi-band capability is enabled by dual LO functionality, additional LO
dividers and wideband operation. This allows 4 individual band profiles1 within
the tuneable range, thereby maximizing use case flexibility.

The SoC has fully integrated digital front end (DFE) functionality which
includes carrier digital up/down conversion (CDUC and CDDC), crest factor
reduction (CFR), digital pre-distortion (DPD), closed loop gain control (CLGC)
and voltage standing wave ratio (VSWR) monitor.

The CDUC feature of the ADRV9040 filters and places individual component
carriers within the band of interest. The CDDC feature, with its 8 parallel
paths, processes each carrier individually before sending over the serial data
interface.

The CDUC and CDDC reduce SERDES interface data rates in non-contiguous carrier
configurations. This integration also reduces power compared to an equivalent
FPGA based implementation.

The CFR engine of the ADRV9040 reduces the peak-to-average ratio of the input
signal, enabling higher efficiency transmit line ups while reducing the
processing load on baseband processors.

The SoC also contains a fully integrated DPD engine for use in power amplifier
(PA) linearization. DPD enables high efficiency PAs, reducing the power
consumption of base station radios and the number of SERDES lanes interfacing
with baseband processors. The DPD engine incorporates a dedicated long-term DPD
(LT-DPD) block which provides support for GaN PAs. The ADRV9040 tackles the
charge trapping property of GaN PAs with its LT-DPD block; therefore, improving
emissions and EVM. The SoC includes an ARM Cortex-A55 quad core processor to
independently serve DPD, CLGC, and VSWR monitor features. The dedicated
processor, together with the DPD engine, provides industry leading DPD
performance.

The serial data interface consists of eight serializer lanes and eight
deserializer lanes. The interface supports both the JESD204B and JESD204C
standards and both fixed and floating-point data formats are supported. The
floating-point format allows internal automatic gain control (AGC) to be
transparent to the baseband processor.

The ADRV9040 is powered directly from 0.8 V, 1.0 V, and 1.8 V regulators and is
controlled via a standard SPI serial port. Comprehensive power-down modes are
included to minimize power consumption in normal use. The device is packaged in
a 27 mm × 20 mm, 736-ball grid array.

Applications
~~~~~~~~~~~~

-  3G/4G/5G TDD/FDD small cell, massive MIMO and macro base stations

Description
-----------

This is a Linux industrial I/O (:doc:`IIO </wiki-migration/software/linux/docs/iio/iio>`) subsystem driver, targeting RF Transceivers. The industrial I/O subsystem provides a unified framework for drivers for many different types of converters and sensors using a number of different physical interfaces (i2c, spi, etc). See :doc:`IIO </wiki-migration/software/linux/docs/iio/iio>` for more information.

Source Code
===========

Status
------

+-----------------------------------------------------------------------------------------------------+------------+---+
| Source                                                                                              | Mainlined? | ' |
+=====================================================================================================+============+===+
| `git <https://github.com/analogdevicesinc/linux/tree/koror_dev/drivers/iio/adc/koror/adrv904x.c>`_  | No         |   |
+-----------------------------------------------------------------------------------------------------+------------+---+

Files
-----

+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Function           | File                                                                                                                                       |
+====================+============================================================================================================================================+
| driver source file | `drivers/iio/adc/koror/adrv904x.c <https://github.com/analogdevicesinc/linux/tree/koror_dev/drivers/iio/adc/koror/adrv904x.c>`_            |
+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| driver source file | `drivers/iio/adc/koror/adrv904x_conv.c <https://github.com/analogdevicesinc/linux/tree/koror_dev/drivers/iio/adc/koror/adrv904x_conv.c>`_  |
+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| driver include     | `drivers/iio/adc/koror/adrv904x.h <https://github.com/analogdevicesinc/linux/tree/koror_dev/drivers/iio/adc/koror/adrv904x.h>`_            |
+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Koror API driver   | `drivers/iio/adc/koror <https://github.com/analogdevicesinc/linux/tree/koror_dev/drivers/iio/adc/koror>`_                                  |
+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

Interrelated Device Drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`JESD204 (FSM) Interface Linux Kernel Framework </wiki-migration/resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
-  :doc:`JESD204 Interface Framework </wiki-migration/resources/fpga/peripherals/jesd204>`

Receive AXI-ADC driver
^^^^^^^^^^^^^^^^^^^^^^

+----------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                                          |
+==========+===============================================================================================================================================+
| driver   | :git-linux:`drivers/iio/adc/cf_axi_adc_core.c`                                                                                                |
+----------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| driver   | :git-linux:`drivers/iio/adc/cf_axi_adc_ring_stream.c`                                                                                         |
+----------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| include  | :git-linux:`drivers/iio/adc/cf_axi_adc.h`                                                                                                     |
+----------+-----------------------------------------------------------------------------------------------------------------------------------------------+

Transmit AXI-DAC / DDS driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                              |
+==========+===================================================================================================================================+
| driver   | :git-linux:`drivers/iio/frequency/cf_axi_dds.c`                                                                                   |
+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| include  | :git-linux:`drivers/iio/frequency/cf_axi_adc.h <drivers/iio/frequency/cf_axi_dds.h>`                                              |
+----------+-----------------------------------------------------------------------------------------------------------------------------------+

AXI JESD204B HDL driver
^^^^^^^^^^^^^^^^^^^^^^^

+----------+---------------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                                  |
+==========+=======================================================================================================================================+
| driver   | :git-linux:`drivers/iio/jesd204/axi_jesd204_rx.c`                                                                                     |
+----------+---------------------------------------------------------------------------------------------------------------------------------------+
| driver   | :git-linux:`drivers/iio/jesd204/axi_jesd204_tx.c`                                                                                     |
+----------+---------------------------------------------------------------------------------------------------------------------------------------+

AXI JESD204B GT (Gigabit Tranceiver) HDL driver (XILINX/ALTERA-INTEL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+-------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                          |
+==========+===============================================================================================================================+
| driver   | :git-linux:`drivers/iio/jesd204/axi_adxcvr.c`                                                                                 |
+----------+-------------------------------------------------------------------------------------------------------------------------------+

Device Driver Customization
===========================

Please follow the link here for detailed options and examples:

-  :doc:`ADRV904x Device Driver Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv904x-customization>`

Processors
==========

The ADRV904x contains dedicated signal processing blocks, ADCs, DACs, two ARM
processor cores and a co-processor called the stream processor. The firmware for
the ARM cores is a pre-compiled binary. The stream co-processor binary is user
generated.

Stream Processor
----------------

A stream processor is a processor within the transceiver tasked with performing
a series of configuration tasks based on some event. After a request from the
user, the stream processor performs a series of predefined actions that are
loaded into the stream processor during device initialization. This processor
takes full advantage of the speed of the internal register buses for efficient
execution of commands.

The stream processor can access and modify registers independently, avoiding the
need for ARM interaction.

The stream processor is a processor within the ADRV904x which performs a series
of configuration tasks based on an event. When requested the stream processor
performs a series of pre-defined actions which are loaded into the stream
processor during initialization. This processor takes advantage of the internal
register bus speed for efficient execution of commands. The stream processor
accesses and modifies registers independently, avoiding the need for ARM
interaction.

The stream processor executes “streams” or series of tasks for:

-  Tx datapath Enable/Disable
-  Rx datapath Enable/Disable
-  ORx datapath Enable/Disable

The stream processor image changes with different configurations. For example,
the stream that enables the receivers are different depending on the JESD
configuration. It is therefore necessary to save a stream image for each
configuration. When the user saves the configuration files (.bin) using the
configurator, a stream binary image is generated automatically (a separate .bin
file). This stream image file should then be used when initializing the device
with the configuration in question. It is also necessary to save a stream image
file every time the firmware version is updated as stream image files can be
specific to versions of ARM and API.

The following are examples of how the stream files can differ:

-  The framer choices for observation receiver and receiver
-  For link sharing purposes
-  If floating point formatting is being used on receiver and observation
   receiver paths, the stream image can change

Nineteen separate stream processors exist in the device, each of which is
responsible for the execution of some dedicated functionality within the device.
These can be divided into two broad categories: slice stream processors and the
core stream processor.

Slice and Core Stream Processors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are eighteen slice stream processors, one each for the eight Tx, Rx
datapaths, and two for the ORx datapaths. These ORx datapaths are not shared
with the internal Tx channel loopback paths that facilitate data collection
during the various Tx calibrations however for external LO leakage calibrations
the ORx path is used. The existence of individual slice stream processors for
each datapath enables true real-time parallel operation of all individual Tx,
Rx, and ORx datapaths.

Each slice stream processor may only access the digital register sub maps
corresponding to its specific functionality. For example, the Tx slice stream
processors can only access the Tx digital sub-maps.

The core stream processor has access to the entire device. The core stream
processor services GPIO pin-based streams and any custom streams that are cross
domain.

Platform File
~~~~~~~~~~~~~

The stream binary ``stream_image.bin`` must be stored in the /lib/firmware folder, or compiled into the kernel using the CONFIG_FIRMWARE_IN_KERNEL, CONFIG_EXTRA_FIRMWARE config options. Multiple stream binaries can be added. However a unique name must be given. The stream binary loaded during driver probe can be specified using following device tree property:

stream-firmware-name = “stream_image.bin”;

Note that this is user generated with ADI evaluation software.

+----------+--------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                               |
+==========+====================================================================================================================+
| Steam    | `firmware/stream_image.bin <https://github.com/analogdevicesinc/linux/blob/koror_dev/firmware/stream_image.bin>`_  |
+----------+--------------------------------------------------------------------------------------------------------------------+

ARM Processor
-------------

The transceiver is equipped with two ARM M4 processors, CPU0 and CPU1, for Radio
functionality. There is a separate A55 processor dedicated DFE features, like
DPD, CLGC, VSWR. This section outlines ARM processor used for Radio features.
The firmware for these ARM processors is loaded during the initialization
process. CPU0 is loaded first, followed by CPU1 then CPU0 is started which will
then start CPU1. The firmware memory size is 641 kB. The ARMs are tasked with
configuring the transceiver for the selected use case, performing initial
calibrations of the signal paths and maintaining device performance over time
through tracking calibrations.

Platform File
~~~~~~~~~~~~~

The fimware loaded during driver probe are specified using following device tree
property:

adi,arm-firmware-name = "ADRV9040_FW.bin";

This is the pre-compiled firmware binary for the embedded dual core ARM
processors in the ADRV904x transceiver, which mainly consists of ADI proprietary
algorithms used to calibrate the transceiver. It is delivered as part of
ADRV904x software package.

+------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Function               | File                                                                                                                     |
+========================+==========================================================================================================================+
| ARM processor firmware | `firmware/ADRV9040_FW.bin <https://github.com/analogdevicesinc/linux/blob/koror_dev/firmware/ADRV9025_DPDCORE_FW.bin>`_  |
+------------------------+--------------------------------------------------------------------------------------------------------------------------+

DFE Processor
-------------

The DFE processor is an ARM A55 quad-core processor for implementing DFE
application software such as DPD, CLGC and VSWR algorithms.

Platform File
~~~~~~~~~~~~~

The firmware files for these processors must be stored in the /lib/firmware
folder, or compiled into the kernel using the CONFIG_FIRMWARE_IN_KERNEL,
CONFIG_EXTRA_FIRMWARE config options. The fimware loaded during driver probe is
specified using following device tree property:

adi,arm-dfe-firmware-name = "ADRV9040_DFE_CALS_FW.bin";

This is the pre-compiled firmware binary for the embedded quad core A55 DFE
processors in the ADRV904x transceiver, which mainly consists of ADI proprietary
DFE algorithms such as DPD, CLGC and VSWR.

+------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Function               | File                                                                                                                               |
+========================+====================================================================================================================================+
| DFE processor firmware | `firmware/ADRV9040_DFE_CALS_FW.bin <https://github.com/analogdevicesinc/linux/blob/koror_dev/firmware/ADRV9040_DFE_CALS_FW.bin>`_  |
+------------------------+------------------------------------------------------------------------------------------------------------------------------------+

Gain Tables
-----------

The Gain table for the RX path must also be loaded during boot/setup phase. This
is also loaded using the firmware framework.

This is the front end gain look up tables for the ADRV904x receiver. It is a
default table delivered as part of ADRV904x software package. User can also
generate custom gain tables.

adi,rx-gaintable-names = "ADRV9040_RxGainTable.csv";

+--------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Function                 | File                                                                                                                               |
+==========================+====================================================================================================================================+
| RX Gain Correction table | `firmware/ADRV9040_RxGainTable.csv <https://github.com/analogdevicesinc/linux/blob/koror_dev/firmware/ADRV9040_RxGainTable.csv>`_  |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------+

Profile Binary
--------------

The ADRV904x’s configuration for a particular use case is programmed through the
profile binary. The profile consists of the filter coefficients, clock rates,
signal blocks, DFE resources to enable/disable for a particular use case.

This is a user generated with ADI evaluation software. Please refer to ADRV904x
Evaluation System User Guide for steps to generate the profile binary.

adi,device-config-name = "DeviceProfileTest.bin";

+--------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Function                 | File                                                                                                                         |
+==========================+==============================================================================================================================+
| RX Gain Correction table | `firmware/DeviceProfileTest.bin <https://github.com/analogdevicesinc/linux/blob/koror_dev/firmware/DeviceProfileTest.bin>`_  |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------+

Enabling Linux driver support
=============================

Configure kernel with "make menuconfig" (alternatively use "make xconfig" or
"make qconfig").

.. hint::

   The ADRV904x driver depends on CONFIG_SPI

Adding Linux driver support
===========================

Configure kernel with "make menuconfig" (alternatively use "make xconfig" or
"make qconfig")

::

   Linux Kernel Configuration
       Device Drivers  --->
       <*>     Industrial I/O support --->
           --- Industrial I/O support
           - *-   Enable ring buffer support within IIO
           - *-     Industrial I/O lock free software ring
           - *-   Enable triggered sampling support

                  Analog to digital converters 
           [--snip--]

           - *- Analog Devices High-Speed AXI ADC driver core
           < > Analog Devices AD9361, AD9364 RF Agile Transceiver driver
           < > Analog Devices AD9371 RF Transceiver driver
           < > Analog Devices ADRV9009/ADRV9008 RF Transceiver driver
           < > Analog Devices ADRV9025/ADRV9026/ADRV9029 RF Transceiver driver
                   <*> Analog Devices ADRV904X/ADRV9040 RF Transceiver driver
           < > Analog Devices AD6676 Wideband IF Receiver driver
           < > Analog Devices AD9467, AD9680, etc. high speed ADCs
           < > Analog Devices Motor Control (AD-FMCMOTCON) drivers

           [--snip--]

       Frequency Synthesizers DDS/PLL  --->
               Direct Digital Synthesis  --->
               <*> Analog Devices CoreFPGA AXI DDS driver
           Clock Generator/Distribution  --->
               < > Analog Devices AD9508 Clock Fanout Buffer
               < > Analog Devices AD9523 Low Jitter Clock Generator
               <*> Analog Devices AD9528 Low Jitter Clock Generator
               < > Analog Devices AD9548 Network Clock Generator/Synchronizer
               < > Analog Devices AD9517 12-Output Clock Generator

       <*>   JESD204 High-Speed Serial Interface Support  --->
           --- JESD204 High-Speed Serial Interface Support
           < >   Altera Arria10 JESD204 PHY Support
           <*>   Analog Devices AXI ADXCVR PHY Support
           < >   Generic AXI JESD204B configuration driver
           <*>   Analog Devices AXI JESD204B TX Support
           <*>   Analog Devices AXI JESD204B RX Support

Driver testing / API
====================

Each and every IIO device, typically a hardware chip, has a device folder under
/sys/bus/iio/devices/iio:deviceX. Where X is the IIO index of the device. Under
every of these directory folders reside a set of files, depending on the
characteristics and features of the hardware device in question. These files are
consistently generalized and documented in the IIO ABI documentation. In order
to determine which IIO deviceX corresponds to which hardware device, the user
can read the name file /sys/bus/iio/devices/iio:deviceX/name. In case the
sequence in which the iio device drivers are loaded/registered is constant, the
numbering is constant and may be known in advance.

.. tip::

   \ TIP: An example program which uses the interface can be found here:

   
   -  :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
   

*General attribute naming convention:*

================================= ===============
IIO sysfs attribute naming prefix Target
================================= ===============
Transceiver                       
in_voltage0\_[…]                  RX1
in_voltage1\_[…]                  RX2
...                               ...
in_voltage7\_[…]                  RX8
in_voltage8\_[…]                  Observation RX1
in_voltage9\_[…]                  Observation RX2
out_altvoltage0\_[…]              TRX LO1
out_altvoltage1\_[…]              TRX LO2
out_altvoltage2\_[…]              TRX AUX LO
out_voltage0\_[…]                 TX1
out_voltage1\_[…]                 TX2
...                               ...
out_voltage7\_[…]                 TX8
================================= ===============

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# cd /sys/bus/iio/devices/      0          0          0          │┘
      root@analog:/sys/bus/iio/devices# ls
      iio:device0  iio:device2  iio:device4
      iio:device1  iio:device3  iio_sysfs_trigger
      root@analog:/sys/bus/iio/devices# cd  iio:device2
      root@analog:/sys/bus/iio/devices/iio:device2# ls -al
      total 0
      drwxr-xr-x 3 root root    0 May 14 12:41 .
      drwxr-xr-x 6 root root    0 May 14 12:41 ..
      -rw-r--r-- 1 root root 4096 May 14 12:41 calibrate
      -rw-r--r-- 1 root root 4096 May 14 12:41 calibrate_rx_qec_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 calibrate_tx_lol_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 calibrate_tx_qec_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_temp0_input
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage0_bb_dc_offset_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage0_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage0_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage0_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage0_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage1_bb_dc_offset_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage1_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage1_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage1_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage1_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage2_bb_dc_offset_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage2_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage2_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage2_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage2_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage3_bb_dc_offset_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage3_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage3_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage3_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage3_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage4_bb_dc_offset_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage4_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage4_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage4_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage4_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage5_bb_dc_offset_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage5_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage5_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage5_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage5_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage6_bb_dc_offset_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage6_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage6_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage6_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage6_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage7_bb_dc_offset_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage7_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage7_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage7_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage7_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage8_bb_dc_offset_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage8_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage8_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage8_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage8_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage9_bb_dc_offset_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage9_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage9_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage9_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage9_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage_sampling_frequency
      -rw-r--r-- 1 root root 4096 May 14 12:41 jesd204_fsm_ctrl
      -r--r--r-- 1 root root 4096 May 14 12:41 jesd204_fsm_error
      -r--r--r-- 1 root root 4096 May 14 12:41 jesd204_fsm_paused
      --w------- 1 root root 4096 May 14 12:41 jesd204_fsm_resume
      -r--r--r-- 1 root root 4096 May 14 12:41 jesd204_fsm_state
      -r--r--r-- 1 root root 4096 May 14 12:41 name
      lrwxrwxrwx 1 root root    0 May 14 12:41 of_node -> ../../../../../../../../firmware/devicetree/base/axi/spi@ff040000/adrv904x-phy@0
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_altvoltage0_LO1_frequency
      -r--r--r-- 1 root root 4096 May 14 12:41 out_altvoltage0_LO1_label
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_altvoltage1_LO2_frequency
      -r--r--r-- 1 root root 4096 May 14 12:41 out_altvoltage1_LO2_label
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage0_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage0_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage0_lo_leakage_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage0_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage0_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage1_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage1_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage1_lo_leakage_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage1_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage1_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage2_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage2_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage2_lo_leakage_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage2_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage2_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage3_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage3_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage3_lo_leakage_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage3_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage3_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage4_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage4_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage4_lo_leakage_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage4_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage4_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage5_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage5_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage5_lo_leakage_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage5_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage5_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage6_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage6_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage6_lo_leakage_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage6_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage6_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage7_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage7_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage7_lo_leakage_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage7_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage7_rf_bandwidth
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage_sampling_frequency
      drwxr-xr-x 2 root root    0 May 14 12:41 power
      lrwxrwxrwx 1 root root    0 May 14 12:41 subsystem -> ../../../../../../../../bus/iio
      -rw-r--r-- 1 root root 4096 May 14 12:41 uevent
      -r--r--r-- 1 root root 4096 May 14 12:41 waiting_for_supplier
      root@analog:/sys/bus/iio/devices/iio:device2#
   

Show device name
----------------

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device2# cat name
      adrv904x-phy
   

Show device temperature
-----------------------

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device2# cat in_temp0_input
      72000
   

Channel Enable/Powerdown Controls
---------------------------------

For use cases where pin control mode is not used or required, these attributes
can be used to enable/disable the Rx/Tx signal paths while in the ENSM radio_on
state.

-  in_voltage0_en
-  in_voltage1_en
-  ...
-  in_voltage7_en
-  out_voltage0_en
-  out_voltage1_en
-  ...
-  out_voltage7_en

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device2# cat in_voltage0_en
      1
      root@analog:/sys/bus/iio/devices/iio:device2# echo 0 > in_voltage0_en
      root@analog:/sys/bus/iio/devices/iio:device2# cat in_voltage0_en
      0
   

Local Oscillator Control (LO)
-----------------------------

The device contains two RF PLLs. Each RF PLL uses the PLL block common to all
synthesizers in the device and employs a high performance VCO for best phase
noise performance. The reference for RF PLL 0 and 1 are sourced from the
reference generation block of the device. The RF PLLs are fractional-N
architectures. A default modulus value is programmed automatically by firmware
to provide an exact frequency on at least a 1 kHz raster using reference clocks
that are integer multiples of 122.88 MHz. The ORx NCO will also operate on an
exact 1 kHz raster providing 0 Hz error between the Tx LO and the ORx NCO.

The RF LO frequency is derived by dividing down the VCO output in the LOGEN
block. The tunable range of the RF LO is 450-7100 MHz. It is recommended to
re-run the init cals when crossing a divide-by-2 boundary specified in the
ADRV904x System Development User Guide (Table 46) or when changing the LO Freq
by ±100 MHz or more from the frequency at which the init cals were performed.

+-------------------------------+

| Attribute                     |

+===============================+

| out_altvoltage0_LO1_frequency |

+-------------------------------+

| out_altvoltage1_LO2_frequency |

+-------------------------------+

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      cat out_altvoltage0_LO1_frequency
      3765000000
      root@analog:/sys/bus/iio/devices/iio:device2# echo 3764000000 > out_altvoltage0_LO1_frequency
      root@analog:/sys/bus/iio/devices/iio:device2# cat out_altvoltage0_LO1_frequency
      3764000000
   

Signal Path Configuration
-------------------------

TX Signal Path
~~~~~~~~~~~~~~

The ADRV904x family of devices' transmitters consists of a tuning baseband low
pass filter, up-convert quadrature mixers and a RF variable gain amplifier. The
baseband filter has a tunable bandwidth of 300MHz to 840MHz. The bandwidth is
tuned at initialization via the loopback path and implemented in the ARM
firmware. The up converter has fixed gain which reduces quadrature errors that
would be associated with attenuation changes in the mixer stages. A unique
architecture of up converters was chosen to reduce 3rd and 5th harmonics. By
lowering these harmonics reduces the linearity requirements of the RF VGA as
well as reducing the risk of aliasing these harmonics in the TX loopback path.

The RF VGA has 32dB of attenuation range and higher gain resolution is achieved
by use of digital gain adjustments. Transmit power control is implemented to
minimize the interaction with the baseband processor.

Properties
^^^^^^^^^^

The following settings are available for each TX channel:

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device2# ls -la | grep out_voltage0
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage0_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage0_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage0_lo_leakage_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage0_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 out_voltage0_rf_bandwidth
   

Primary Signal Bandwidth
^^^^^^^^^^^^^^^^^^^^^^^^

To query TX Primary Signal Bandwidth:

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device2# cat out_voltage0_rf_bandwidth
      400000000
   

Hardware Gain
^^^^^^^^^^^^^

To query and modify TX Hardware Gain:

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device2# cat out_voltage0_hardwaregain
      -6.000000 dB
      root@analog:/sys/bus/iio/devices/iio:device2# echo -12 > out_voltage0_hardwaregain
      root@analog:/sys/bus/iio/devices/iio:device2# cat out_voltage0_hardwaregain
      -12.000000 dB
   

RX Signal Path
~~~~~~~~~~~~~~

The ADRV904x RX path consists of an RF attenuator followed by a current mode
passive mixer. The output current of the mixer is passed through a
transimpedance amplifier (TIA) filter then digitized with continuous time
pipeline ADC. The digital baseband provides most of the filtering and decimation
required. Analog power detectors are not in the signal chain but are built into
the ADC of each RX channel.

RF input is 100 ohms differential. Single ended 50-ohm sources would drive into
a 1:2 balun. The RF attenuator is a pi resistive network with 256 gain settings
but only 0-32dB range is used. The RX AGC indexes the digital gain look up table
to control the attenuation of the Rx front-end.

Properties
^^^^^^^^^^

The following settings are available for each RX channel:

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device2# ls -la | grep in_voltage1
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage1_bb_dc_offset_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage1_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage1_hardwaregain
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage1_quadrature_tracking_en
      -rw-r--r-- 1 root root 4096 May 14 12:41 in_voltage1_rf_bandwidth
   

Advanced Debug Facilities
-------------------------

The ADRV904x driver supports advanced debug controls via the kernel `debugfs <https://en.wikipedia.org/wiki/debugfs>`_. These controls are mostly to debug which settings are currently configured in the device. How these device files/controls can be used is described here.

Runtime Device Driver Customization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Through these controls, the user can run and configure BIST tests. In order to
identify if the IIO device in question (adrv904x-phy) you first need to identify
the IIO device number. Therefore read the name attribute of each IIO device

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# grep "" /sys/bus/iio/devices/iio\:device*/name
      /sys/bus/iio/devices/iio:device0/name:xilinx-ams
      /sys/bus/iio/devices/iio:device1/name:ad9528-1
      /sys/bus/iio/devices/iio:device2/name:adrv904x-phy
      /sys/bus/iio/devices/iio:device3/name:axi-adrv904x-rx-hpc
      /sys/bus/iio/devices/iio:device4/name:axi-adrv904x-tx-hpc
   

Change directory to **/sys/kernel/debug**/iio/ iio:deviceX.

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# cd /sys/kernel/debug/iio/iio\:device2
      root@analog:/sys/kernel/debug/iio/iio:device2# ls -la
      total 0
      drwxr-xr-x 2 root root 0 May 14 12:40 .
      drwxr-xr-x 6 root root 0 Jan  1  1970 ..
      -rw-r--r-- 1 root root 0 May 14 12:40 bist_framer_0_prbs
      -rw-r--r-- 1 root root 0 May 14 12:40 bist_framer_loopback
      -rw-r--r-- 1 root root 0 May 14 12:40 bist_tone
      -rw-r--r-- 1 root root 0 May 14 12:40 direct_reg_access
   

Build-In Self-Test (BIST)
~~~~~~~~~~~~~~~~~~~~~~~~~

Controlling these attribute files directly take effect and therefore don’t require the ``initialize`` sequence. Test functionality exposed here is only meant to route or inject test patterns/data than can be used to validate the Digital Interface or functionality of the device.

PRBS
^^^^

Pseudorandom Binary Sequence (`PRBS <https://en.wikipedia.org/wiki/Pseudorandom_binary_sequence>`_) to Framer 0.

SYNTAX:

**bist_framer_0_prbs** *<Data Source>*

+-------------+

| Data Source |

+=============+

| Value       |

+-------------+

| 0           |

+-------------+

| 1           |

+-------------+

| 2           |

+-------------+

| 3           |

+-------------+

| 4           |

+-------------+

| 5           |

+-------------+

| 6           |

+-------------+

| 7           |

+-------------+

| 8           |

+-------------+

| 14          |

+-------------+

| 15          |

+-------------+

**Example**: Inject ramp PRBS

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/kernel/debug/iio/iio:device2# echo 8 > bist_framer_0_prbs
   

BIST Loopback
^^^^^^^^^^^^^

Allows to digitally loopback framer data into the deframer.

**SYNTAX:**

**bist_framer_loopback** *<Mode>*

===== ==================================
Value Mode
===== ==================================
0     Disable
1     Digital framer -> Digital deframer
===== ==================================

**Example**: Digital TX -> Digital RX

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/kernel/debug/iio/iio:device2# echo 1 > bist_framer_loopback
   

BIST Tone
^^^^^^^^^

User selectable tone (with frequency and gain selection), that can be injected
into the TX path. Tx7 channel is selected.

SYNTAX:

**bist_tone** *<Enable> <Tone Frequency> <Tone Gain>*

+--------+

| Enable |

+========+

| Value  |

+--------+

| 0      |

+--------+

| 1      |

+--------+

+-----------------------------------------------+

| Tone Frequency                                |

+===============================================+

| Signed frequency in Hz of the desired Tx tone |

+-----------------------------------------------+

+----------------------+

| Tone Gain (Optional) |

+======================+

| Value                |

+----------------------+

| 0                    |

+----------------------+

| 1                    |

+----------------------+

| 2                    |

+----------------------+

| 3                    |

+----------------------+

| 4                    |

+----------------------+

| 5                    |

+----------------------+

| 6                    |

+----------------------+

| 7                    |

+----------------------+

| 8                    |

+----------------------+

**Example**: Inject a 12 dB tone at 30 MHz into TX (all channels enabled)

.. container:: box bggreen

   This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/kernel/debug/iio/iio:device2# echo 1 30000 2 > bist_tone
   

Low level register access via debugfs (direct_reg_access)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This page contains a few lose documentation snippets used in various spots.

IIO device files
================

Each and every IIO device, typically a hardware chip, has a device folder under
/sys/bus/iio/devices/iio:deviceX. Where X is the IIO index of the device. Under
every of these directory folders reside a set of files, depending on the
characteristics and features of the hardware device in question. These files are
consistently generalized and documented in the IIO ABI documentation. In order
to determine which IIO deviceX corresponds to which hardware device, the user
can read the name file /sys/bus/iio/devices/iio:deviceX/name. In case the
sequence in which the iio device drivers are loaded/registered is constant, the
numbering is constant and may be known in advance.

IIO devices with trigger consumer interface
===========================================

If deviceX supports triggered sampling, it’s a so called trigger consumer and
there will be an additional folder /sys/bus/iio/device/iio:deviceX/trigger. In
this folder there is a file called current_trigger, allowing controlling and
viewing the current trigger source connected to deviceX. Available trigger
sources can be identified by reading the name file
/sys/bus/iio/devices/triggerY/name. The same trigger source can connect to
multiple devices, so a single trigger may initialize data capture or reading
from a number of sensors, converters, etc.

.. hint::

   Trigger Consumers:

   | Currently triggers are only used for the filling of software ring buffers and as such any device supporting INDIO_RING_TRIGGERED has the consumer interface automatically created.

**Description:** Read name of triggerY

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/bus/iio/devices/triggerY/> cat name
      irqtrig56
   

**Description:** Make irqtrig56 (trigger using system IRQ56, likely a GPIO IRQ), to current trigger of deviceX

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/bus/iio/devices/iio:deviceX/trigger> echo irqtrig56 > current_trigger
   

**Description:** Read current trigger source of deviceX

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root:/sys/bus/iio/devices/iio:deviceX/trigger> cat current_trigger
      irqtrig56
   

Standalone trigger drivers
==========================

+----------------------------------------------------------------------+-------------------------------------------------------------------------------+
| name                                                                 | description                                                                   |
+======================================================================+===============================================================================+
| iio-trig-gpio                                                        | Provides support for using GPIO pins as IIO triggers.                         |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------+
| iio-trig-rtc                                                         | Provides support for using periodic capable real time clocks as IIO triggers. |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `iio-trig-sysfs <https://wiki.analog.com/iio-trig-sysfs>`_           | Provides support for using SYSFS entry as IIO triggers.                       |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `iio-trig-bfin-timer <https://wiki.analog.com/iio-trig-bfin-timer>`_ | Provides support for using a Blackfin timer as IIO triggers.                  |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------+

Buffer management
=================

The Industrial I/O subsystem provides support for various ring buffer based data
acquisition methods. Apart from device specific hardware buffer support, the
user can chose between two different software ring buffer implementations. One
is the IIO lock free software ring, and the other is based on Linux kfifo.
Devices with buffer support feature an additional sub-folder in the
/sys/bus/iio/devices/deviceX/ folder hierarchy. Called deviceX:bufferY, where Y
defaults to 0, for devices with a single buffer.

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

The Industrial I/O subsystem provides support for passing hardware generated
events up to userspace.

In IIO events are not used for passing normal readings from the sensing devices
to userspace, but rather for out of band information. Normal data reaches
userspace through a low overhead character device - typically via either
software or hardware buffer. The stream format is pseudo fixed, so is described
and controlled via sysfs rather than adding headers to the data describing what
is in it.

Pretty much all IIO events correspond to thresholds on some value derived from
one or more raw readings from the sensor. They are provided by the underlying
hardware.

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

-  Simple chrdev per device (aggregation across devices doesn't really make
   sense for IIO as you tend to really care which sensor caused the event rather
   than just that it happened.)

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

Some IIO drivers feature an optional debug facility, allowing users to read or
write registers directly. Special care needs to be taken when using this
feature, since you can modify registers on the back of the driver.

.. tip::

   To simplify direct register access you may want to use the libiio :doc:`iio_reg </wiki-migration/resources/tools-software/linux-software/libiio/iio_reg>` command line utility.

Accessing debugfs requires root privileges.

In order to identify if the IIO device in question feature this option you first
need to identify the IIO device number.

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
-  `IIO Linux Kernel Documentation sysfs-bus-iio-\* <https://www.kernel.org/doc/Documentation/ABI/testing>`_
-  `IIO Documentation <https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-bus-iio>`_
-  :doc:`IIO test and visualization application </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`libiio - IIO system library </wiki-migration/resources/tools-software/linux-software/libiio>`
-  :doc:`libiio - Internals </wiki-migration/resources/tools-software/linux-software/libiio_internals>`
-  :doc:`Pointers and good books </wiki-migration/resources/tools-software/pointers>`
-  `IIO High Speed <https://events.static.linuxfound.org/sites/events/files/slides/iio_high_speed.pdf>`_
-  `Software Defined Radio using the IIO framework <http://video.fosdem.org/2015/devroom-software_defined_radio/iiosdr.mp4>`_
-

|libiio introduction|

*Need Help?*

-  :ez:`Analog Devices Linux Device Drivers Help Forum <linux-software-drivers>`
-  `Ask a Question <https://ez.analog.com/>`_

.. |libiio introduction| image:: https://wiki.analog.com/_media/software/linux/docs/iio/youtube>p_vntewue24
