.. _linux ad4052:

AD4052
======

The :adi:`AD4050`, :adi:`AD4052`, :adi:`AD4056`, and :adi:`AD4058` .
are versatile, 16-bit/12-bit, successive approximation register (SAR)
analog-to-digital converters (ADCs) that enable low-power, high-density data
acquisition solutions without sacrificing precision. These ADCs offer a unique
balance of performance and power efficiency, plus innovative features for
seamlessly switching between high-resolution and low-power modes tailored to the
immediate needs of the system.

The :adi:`AD4050`/:adi:`AD4052`/:adi:`AD4056`/:adi:`AD4058` are ideal for
battery-powered, compact data acquisition and edge sensing applications.

The :adi:`EVAL-AD4050-ARDZ`/:adi:`EVAL-AD4052-ARDZ` evaluation boards enable
quick and easy evaluation of the performance and features of the :adi:`AD4050`
or the :adi:`AD4052`, respectively.
The AD4050 and AD4052 are compact, low power, 12-bit or 16-bit (respectively)
Easy Drive successive approximation register (SAR) analog-to-digital converters
(ADCs).

Supported Devices
-----------------

* :adi:`AD4050`
* :adi:`AD4052`
* :adi:`AD4056`
* :adi:`AD4058`

Evaluation Boards
-----------------

* :adi:`EVAL-AD4050-ARDZ`
* :adi:`EVAL-AD4052-ARDZ`

Source Code
-----------

Status
------

.. list-table::
   :header-rows: 1

   - - Source
     - Mainlined?
   - - :git-linux:`git <drivers/iio/adc/ad4052.c>`
     - [No]

Files
-----

.. list-table::
   :header-rows: 1

   - - Function
     - File
   - - driver
     - :git-linux:`ad4052.c <staging/ad4052:drivers/iio/adc/ad4052.c>`
   - - devicetree
     - :git-linux:`ad4052.dts <staging/ad4052:arch/arm/boot/dts/xilinx/zynq-coraz7s-ad4052.dts>`
   - - devicetree bindings doc
     - :git-linux:`ad4052.yaml <staging/ad4052:Documentation/devicetree/bindings/iio/adc/adi,ad4052.yaml>`

Devicetree
----------

External clock
~~~~~~~~~~~~~~

Reference clock used for sampling timing.
May be the same clock as the SPI Controller driver.

::

     clocks {
         ref_clk: ext-clk {
             #clock-cells = <0x0>;
             compatible = "fixed-clock";
             clock-frequency = <150000000>;
             clock-output-names = "ref_clk";
         };
     };

Sampling trigger
~~~~~~~~~~~~~~~~

This PWM generator is used to start the sampling procedure.

::

     adc_trigger: axi-pwm-gen@ {
         compatible = "adi,axi-pwmgen";
         reg = <0x44b00000 0x1000>;
         label = "ad4052_cnv";
         #pwm-cells = <2>;
         clocks = <&cnv_ext_clk>;
     };

ADC node
~~~~~~~~

The AD4052 is a SPI-compatible ADC so it should be under a SPI controller.

.. important::

   The ``spi-max-frequency`` must be a multiple of a 25MHz clock
   and the ``dmas`` handle should use a 64-bit wide data bus.

::

     &spi{
         ad4052: ad4052@0 {
             compatible = "adi,ad4052";
             reg = <0>;
             spi-max-frequency = <25000000>;
             clocks = <&spi_clk>;
             dmas = <&rx_dma 0>;
             dma-names = "rx";
             pwm-names = "cnv";
             pwms = <&adc_trigger 0 0>,
             cnv-gpios = <&gpio0 88 GPIO_ACTIVE_HIGH>;
             gp1-gpios = <&gpio0 87 GPIO_ACTIVE_HIGH>;
             gp0-gpios = <&gpio0 86 GPIO_ACTIVE_HIGH>;
         };
     };

Usage
-----

Kernel configuration
~~~~~~~~~~~~~~~~~~~~

This device depends on a PWM based trigger used to start the sampling procedure.
The first step is to enable the support for AXI_PWMGEN.

::

   Symbol: PWM_AXI_PWMGEN [=y]
   Type  : tristate
   Prompt: Analog Devices AXI PWM generator
      Location:
        -> Device Drivers
          -> Pulse-Width Modulation (PWM) Support (PWM [=y])
      Defined at drivers/pwm/Kconfig:78
      Depends on: PWM [=y] && HAS_IOMEM [=y]
      Selected by [y]:
      - KERNEL_ALL_ADI_DRIVERS [=y]

Another required component is the SPI controller. The AD4052 has a specific
set of SPI timing requirements that are supported by the
:external+hdl:ref:`spi_engine` IP.

::

     Symbol: SPI_AXI_SPI_ENGINE [=y]
     Type  : tristate
     Prompt: Analog Devices AXI SPI Engine controller
       Location:
         -> Device Drivers
           -> SPI support (SPI [=y])
       Defined at drivers/spi/Kconfig:112
       Depends on: SPI [=y] && SPI_MASTER [=y] && HAS_IOMEM [=y]
       Selected by [y]:
       - KERNEL_ALL_ADI_DRIVERS [=y]


And finally, enable support for the AD4630 device family.

::

   Symbol: AD4052 [=y]
   Type  : tristate
   Prompt: Analog Device AD4052 ADC Driver
     Location:
       -> Device Drivers
         -> Industrial I/O support (IIO [=y])
           -> Analog to digital converters
     Defined at drivers/iio/adc/Kconfig:47
     Depends on: IIO [=y] && SPI [=y] && PWM [=y] && GPIOLIB [=y]
     Selects: IIO_BUFFER [=y] && IIO_BUFFER_DMA [=y] && IIO_BUFFER_DMAENGINE [=y]

Driver testing
~~~~~~~~~~~~~~

This device can be found under */sys/bus/iio/devices/*

One way to check if the device and driver are present is using **iio_info**:

.. shell::
   :no-path:

   $iio_info
        iio:device0: ad4052 (buffer capable)
                1 channels found:
                        voltage0:  (input, index: 0, format: le:s16/32>>0)
                        2 channel-specific attributes found:
                                attr  0: raw value: 12167
                                attr  1: sampling_frequency value: 1000000
                1 device-specific attributes found:
                                attr  0: waiting_for_supplier value: 0
                3 buffer-specific attributes found:
                                attr  0: data_available value: 0
                                attr  1: direction value: in
                                attr  2: length_align_bytes value: 8
                1 debug attributes found:
                                debug attr  0: direct_reg_access value: 0x10
                No trigger on this device

You can go to the device folder using:

.. shell::
   :no-path:

   $cd $(grep -rw /sys/bus/iio/devices/*/name -e "ad4052" -l | xargs dirname)

.. note::

   As specified in the devicetree section, the device supports
   multiple functional modes.
   This example describes the steps for the 24-bit burst averaging mode.

In the folder there are several files that can set specific device attributes:

.. shell::

   /sys/bus/iio/devices/iio:device0
   $ls -l
    total 0
    drwxr-xr-x 2 root root    0 Nov 16 21:27 buffer
    drwxr-xr-x 2 root root    0 Nov 16 21:27 buffer0
    -r--r--r-- 1 root root 4096 Nov 16 21:27 dev
    drwxr-xr-x 2 root root    0 Nov 16 21:27 events
    -rw-r--r-- 1 root root 4096 Nov 16 21:27 in_voltage_oversampling_ratio
    -rw-r--r-- 1 root root 4096 Nov 16 21:27 in_voltage_raw
    -rw-r--r-- 1 root root 4096 Nov 16 21:27 in_voltage_sampling_frequency
    -r--r--r-- 1 root root 4096 Nov 16 21:27 in_voltage_sampling_frequency_available
    -r--r--r-- 1 root root 4096 Nov 16 21:27 name
    lrwxrwxrwx 1 root root    0 Nov 16 21:27 of_node -> ../../../../../../../../firmware/devicetree/base/fpga-axi@0/spi@44a00000/ad4052@0
    drwxr-xr-x 2 root root    0 Nov 16 21:27 power
    drwxr-xr-x 2 root root    0 Nov 16 21:27 scan_elements
    lrwxrwxrwx 1 root root    0 Nov 16 21:27 subsystem -> ../../../../../../../../bus/iio
    -rw-r--r-- 1 root root 4096 Nov 16 21:27 uevent
    -r--r--r-- 1 root root 4096 Nov 16 21:27 waiting_for_supplier

Oversampling
^^^^^^^^^^^^

The AD4052 device family has support for a burst averaging mode that's
exposed as the oversampling attribute.
Writing value 0 or 1 returns the device to sample mode.

Display current oversampling value:

.. shell::
   :no-path:

   /sys/bus/iio/devices/iio:device0
   $cat in_voltage_oversampling_ratio
    64

Change the sample averaging count:

.. shell::
   :no-path:

   /sys/bus/iio/devices/iio:device0
   $echo 2048 > in_voltage_oversampling_ratio
   $cat in_voltage_oversampling_ratio
   2048

.. important::

   Please note that averaging on low sampling rates will timeout if
   the default buffer wait time is not modified.

   For single shot readings, it will also timeout in 1 second.

Sample rate for burst and monitor mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Leveraging the device internal clock, the sample rate for burst and monitor
mode can be configured.

Display all available sample rates:

.. shell::
   :no-path:

   $cd /sys/bus/iio/devices/iio\:device0 ; pwd
    /sys/bus/iio/devices/iio:device0
   $cat in_voltage_sampling_frequency_available
    2000000 1000000 300000 100000 33300 10000 3000 500 333 250 200 166 140 125 111

Set the desired sample rate:

.. shell::
   :no-path:

   /cd /sys/bus/iio/devices/iio\:device0 ; pwd
   $echo 1000000 > in_voltage_sampling_frequency
   $cat in_voltage_sampling_frequency
    1000000

Sample rate for buffer reading with PWM trigger
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the desired period of the PWM trigger to set the sampling frequency
of bufferred reading.

.. shell::
   :no-path:

   $cd /sys/bus/iio/devices/iio\:device0/buffer ; pwd
    /sys/bus/iio/devices/iio\:device0/buffer
   $echo 1000000 > sampling_frequency
   $cat sampling_frequency
    1000000

Auto suspend
^^^^^^^^^^^^

The device enters sleep mode (low power) when no acquisition is being made.
Display the current runtime status:

.. shell::
   :no-path:

   $cat /sys/bus/spi/devices/spi0.0/power/runtime_status
    suspend

.. caution::

   The power management methods are coupled to the spi device and not the
   iio device.

There is a timeout of 1 second before the power management puts the device in
sleep mode.
This is to avoid putting the device to sleep when sampling single shot readings
without a buffer.

Monitor mode
^^^^^^^^^^^^

The driver yield a IIO Event for the device threshold interrupt in device
monitor mode.
The event is triggered for either direction (rising or falling the max/min
threshold values).
Configure the device threshold and hysteresis values:

.. shell::
   :no-path:

   $cd /sys/bus/iio/devices/iio\:device0 ; pwd
    /sys/bus/iio/devices/iio:device0
   $echo 1000 > events/thresh_rising_value
   $echo -1000 > events/thresh_falling_value
   $echo 125 > events/thresh_rising_hysteresis
   $echo 125 > events/thresh_falling_hysteresis

Enable monitor mode:

.. shell::
   :no-path:

   /sys/bus/iio/devices/iio\:device0
   $echo 1 > events/thresh_either_en

At monitor mode, since the device is contiguously sampling, the device is active:

.. shell::
   :no-path:

   $cat /sys/bus/spi/devices/spi0.0/power/runtime_status
    active

Threshold events will increment the interrupt count:

.. shell::
   :no-path:

   $cat /proc/interrupts
               CPU0
     ...
     46:          3 GIC-0  90 Edge      ad4052

The driver puts the device in monitor mode after every device access, until
disabling the threshold event with:

.. shell::
   :no-path:

   /sys/bus/iio/devices/iio\:device0
   $echo 0 > events/thresh_either_en

.. caution::

   The device is locked from any other access until the monitor mode is
   disabled.

The user is responsible to catching IIO Event and clearing the device status
register.

.. shell::
   :no-path:

   /sys/bus/iio/devices/iio\:device0
   $echo 0 > events/thresh_either_en
   $echo 0x41 > direct_reg_access
   $cat direct_reg_access
    0x88
   $echo 0x41 0x02 > direct_reg_access
   $cat direct_reg_access
    0x80

Data acquisition
^^^^^^^^^^^^^^^^

The data acquisition is performed using a buffer system:

.. shell::
   :no-path:

   $cd /sys/bus/iio/devices/iio\:device0 ; pwd
    /sys/bus/iio/devices/iio:device0
   $ls buffer
    data_available  enable  length  length_align_bytes  watermark
   $ls scan_elements
    in_voltage0_en  in_voltage0_index  in_voltage0_type

Every buffer implementation features a set of files:

* ``buffer``: length Get/set the number of sample sets that may be held by the buffer.
* ``buffer``: enable Enables/disables the buffer. This file should be written last,
  after length and selection of scan elements
* ``scan_elements``: in_voltage0_en enable/disables the channel output so the
  data won't be buffered for that specific channel.

Enable and read 400 samples:

.. shell::
   :no-path:

   /sys/bus/iio/devices/iio\:device0
   $echo 1 > scan_elements/in_voltage0_en
   $echo 400 > buffer/length
   $echo 1 > buffer/enable
   $hexdump -n 400 /dev/iio\:device0
    0000000 0eaf 0000 0ead 0000 0eb0 0000 0ead 0000
    0000010 0ead 0000 0ea7 0000 0e9d 0000 0e9c 0000
    0000020 0e97 0000 0e93 0000 0e84 0000 0e80 0000
    0000030 0e7f 0000 0e7e 0000 0e7c 0000 0e7d 0000
    0000040 0e7c 0000 0e79 0000 0e75 0000 0e6c 0000
    0000050 0e64 0000 0e63 0000 0e5f 0000 0e51 0000
    0000060 0e4c 0000 0e4f 0000 0e4d 0000 0e4b 0000
    0000070 0e4d 0000 0e4b 0000 0e4c 0000 0e42 0000
    0000080 0e39 0000 0e36 0000 0e33 0000 0e31 0000
    0000090 0e24 0000 0e1c 0000 0e19 0000 0e1a 0000
    00000a0 0e1d 0000 0e1a 0000 0e16 0000 0e19 0000
    00000b0 0e15 0000 0e0c 0000 0e07 0000 0e03 0000
    00000c0 0e03 0000 0e06 0000 0e05 0000 0e04 0000
    00000d0 0e03 0000 0dff 0000 0df0 0000 0dea 0000
    00000e0 0ded 0000 0de5 0000 0ddd 0000 0dd9 0000
    00000f0 0dd7 0000 0dd3 0000 0dd2 0000 0dd1 0000
    0000100 0dcd 0000 0dd1 0000 0dc8 0000 0dc1 0000
    0000110 0dbe 0000 0dbb 0000 0dbc 0000 0daa 0000
    0000120 0da5 0000 0da3 0000 0da2 0000 0d9f 0000
    0000130 0da0 0000 0da1 0000 0da2 0000 0d9d 0000
    0000140 0d91 0000 0d8e 0000 0d89 0000 0d8a 0000
    0000150 0d7a 0000 0d74 0000 0d6f 0000 0d70 0000
    0000160 0d6b 0000 0d6f 0000 0d70 0000 0d73 0000
    0000170 0d6c 0000 0d63 0000 0d5f 0000 0d59 0000
    0000180 0d58 0000 0d4e 0000 0d46 0000 0d42 0000
    0000190
   $echo 0 > buffer/enable

Debug mode
^^^^^^^^^^

You can write and read the ADC registers using debugfs. Here we will read and
write the scratchpad register:

First go to the device debug folder:

.. shell::

   $cd /sys/kernel/debug/iio/iio\:device0 ; pwd
    /sys/kernel/debug/iio/iio:device0

Read the 0xA register:

.. shell::
   :no-path:

   $echo 0xA > direct_reg_access
   $cat direct_reg_access
    0x0

Write and verify the value:

.. shell::
   :no-path:

   $echo 0xA 0x5F > direct_reg_access
   $cat direct_reg_access
    0x5F
