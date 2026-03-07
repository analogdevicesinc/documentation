AD8460 IIO DAC Linux Driver
===========================

The AD8460 is a “bits in, power out” high voltage, high-power, highspeed driver optimized for large output current (up to ±1 A) and high slew rate (up to ±1800 V/μs) at high voltage (up to ±40 V) into capacitive loads. Combining a 14-bit high-speed DAC, a high voltage, high output current (HV-HI) analog driver, and fault monitoring and protection circuits,

Supported Devices
-----------------

-  :adi:`AD8460`

Evaluation Boards
-----------------

-  :adi:`EVAL-AD8460SDZ`

Description
-----------

This is a Linux industrial I/O (:doc:`IIO </wiki-migration/software/linux/docs/iio/iio>`) subsystem driver, targeting single-channel serial interface DACs. The industrial I/O subsystem provides a unified framework for drivers for many different types of converters and sensors using a number of different physical interfaces (i2c, spi, etc). See :doc:`IIO </wiki-migration/software/linux/docs/iio/iio>` for more information.

Source Code
===========

Status
------

+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Source                                                                                                     | Mainlined?                                                                                                 |
+============================================================================================================+============================================================================================================+
| `git <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad8460.c>`_  | `WIP <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/iio/dac/ad8460.c>`_  |
+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

Files
-----

+-------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Function    | File                                                                                                                                  |
+=============+=======================================================================================================================================+
| driver      | :git-linux:`drivers/iio/dac/ad8460.c`                                                                                                 |
+-------------+---------------------------------------------------------------------------------------------------------------------------------------+
| dt-bindings | :git-linux:`Documentation/devicetree/bindings/iio/dac/adi,ad8460.yaml`                                                                |
+-------------+---------------------------------------------------------------------------------------------------------------------------------------+

Example platform device initialization
======================================

Devicetree
----------

Required devicetree properties:

-  ``compatible``: Needs to be "adi," followed by the name of the device. E.g. "adi,ad8460"
-  ``reg``: The chipselect number used for the device
-  ``spi-max-frequency``: Maximum SPI clock frequency
-  ``clocks``: SYNC clock
-  ``refio-1p2v-supply``: Voltage reference for full-scale adjustment
-  ``adi,external-resistor-ohms``:

Optional devicetree properties:

-  ``adi,range-microvolt``:
-  ``adi,range-microamp``:
-  ``adi,max-millicelsius``:

::


   /{
       refio_1_2: regulator-refio_1_2 {
           regulator-name = "refio_1_2";
           regulator-min-microvolt = <120000>;
           regulator-max-microvolt = <1200000>;
           regulator-always-on;
       };

       clocks {
           sync_ext_clk: ext-clk {
               #clock-cells = <0x0>;
               compatible = "fixed-clock";
               clock-frequency = <500000>;
               clock-output-names = "sync_ext_clk";
           };
       };
   };

   &spi0 {
       status = "okay";

       ad8460: dac@0 {
           compatible = "adi,ad8460";
           reg = <0>;
           spi-max-frequency = <8000000>;

           clocks = <&sync_ext_clk>;
           clock-names = "sync_clk";

           refio-1p2v-supply = <&refio_1_2>;

           adi,external-resistor-ohms = <2000>;
           adi,range-microvolt = <(-40000000) 40000000>;
           adi,range-microamp = <(-50000) 50000>;
           adi,max-millicelsius = <50000>;
       };
   };

Adding Linux driver support
===========================

Configure kernel with "make menuconfig" (alternatively use "make xconfig" or "make qconfig")

::

   Linux Kernel Configuration
       Device Drivers  --->
           ...
           <*>     Industrial I/O support --->
               --- Industrial I/O support
               ...
               Digital to analog converters  ---> 
                   ...
                   <*> Analog Devices AD8460 driver
                   ...
               ...
           ...

Driver testing
==============

.. include:: ../software/linux/docs/iio/iio_snippets.rst

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/# cd /sys/bus/iio/devices/
      root@analog:/sys/bus/iio/devices# ls
      iio:device0  iio:device1  iio_sysfs_trigger
      root@analog:/sys/bus/iio/devices# cd iio:device1
      root@analog:/sys/bus/iio/devices/iio:device1# ls -l
      total 0
      drwxr-xr-x 2 root root    0 Apr  5 04:17 buffer
      drwxr-xr-x 2 root root    0 Apr  5 04:17 buffer0
      -r--r--r-- 1 root root 4096 Apr  5 04:17 dev
      drwxr-xr-x 2 root root    0 Apr  5 04:17 events
      -r--r--r-- 1 root root 4096 Apr  5 04:17 name
      lrwxrwxrwx 1 root root    0 Apr  5 04:17 of_node -> ../../../../../../../../firmware/devicetree/base/axi/spi@e0006000/dac@0
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_current0_raw
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_powerdown
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_powerdown_mode
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw0
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw1
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw10
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw11
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw12
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw13
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw14
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw15
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw2
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw3
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw4
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw5
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw6
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw7
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw8
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_raw9
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_sampling_frequency
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_scale
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_symbol
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 out_voltage0_toggle_en
      -r--r--r-- 1 root root 4096 Apr  5 04:17 out_voltage_powerdown_mode_available
      drwxr-xr-x 2 root root    0 Apr  5 04:17 power
      drwxr-xr-x 2 root root    0 Apr  5 04:17 scan_elements
      lrwxrwxrwx 1 root root    0 Apr  5 04:17 subsystem -> ../../../../../../../../bus/iio
      -rw-r--r-- 1 root root 4096 Apr  5 04:17 uevent
   


Show device name
----------------

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device1# $ cat name
      ad8460
   


Enable power down mode for the device
-------------------------------------

| **Description:**
| /sys/bus/iio/devices/iio:deviceX/out_voltageY_powerdown

Writing 1 causes channel Y to enter power down mode. Clearing returns to normal operation.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device1# echo 1 > out_voltage0_powerdown 
      root@analog:/sys/bus/iio/devices/iio:device1# cat out_voltage0_powerdown
      1
      root@analog:/sys/bus/iio/devices/iio:device1# echo 0 > out_voltage0_powerdown
      root@analog:/sys/bus/iio/devices/iio:device1# cat out_voltage0_powerdown
      0
   


Manual toggling between input modes
-----------------------------------

| **Description:**
| /sys/bus/iio/devices/iio:deviceX/out_voltageY_toggle_en

Writing 1 causes channel Y to enter Arbitrary Pattern Generator (APG) mode. Clearing sets it to Arbitrary Waveform Generator (AWG) mode

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device1# echo 1 > out_voltage0_toggle_en
      root@analog:/sys/bus/iio/devices/iio:device1# cat out_voltage0_toggle_en
      1
      root@analog:/sys/bus/iio/devices/iio:device1# echo 0 > out_voltage0_toggle_en
      root@analog:/sys/bus/iio/devices/iio:device1# cat out_voltage0_toggle_en
      0
   


Set pattern memory values for APG mode
--------------------------------------

| **Description:**
| /sys/bus/iio/devices/iio:deviceX/out_voltageY_raw[0~15]

Allows writing of up to 16 14-bit values in pattern memory

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device1# echo 8192 > out_voltage0_raw0
      root@analog:/sys/bus/iio/devices/iio:device1# cat out_voltage0_raw0
      8192
      root@analog:/sys/bus/iio/devices/iio:device1# echo 16364 > out_voltage0_raw1
      root@analog:/sys/bus/iio/devices/iio:device1# cat out_voltage0_raw1
      16364
   


Set pattern depth for APG mode
------------------------------

| **Description:**
| /sys/bus/iio/devices/iio:deviceX/out_voltageY_symbol

Writing any value from 0 to 15 will set pattern depth

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device1# echo 3 > out_voltage0_symbol
      root@analog:/sys/bus/iio/devices/iio:device1# cat out_voltage0_symbol
      3
   


Set programmable quiescent current
----------------------------------

| **Description:**
| /sys/bus/iio/devices/iio:deviceX/out_currentY_raw

Write raw value of programmable quiescent current. User must follow the format as per datasheet.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device1# echo 143 > out_current0_raw
      root@analog:/sys/bus/iio/devices/iio:device1# cat out_current0_raw
      143
   


Enable fault monitoring thresholds
----------------------------------

| **Description:**
| /sys/bus/iio/devices/iio:deviceX/events/out_currentY_thresh_falling_en
| /sys/bus/iio/devices/iio:deviceX/events/out_currentY_thresh_rising_en
| /sys/bus/iio/devices/iio:deviceX/events/out_voltageY_thresh_falling_en
| /sys/bus/iio/devices/iio:deviceX/events/out_voltageY_thresh_rising_en
| /sys/bus/iio/devices/iio:deviceX/events/out_tempY_thresh_rising_en
| Writing 1 will arm the device against fault events, while clearing disarms the device. The IIO event attributes correspond to the following: OVERCURRENT_SNK, OVERCURRENT_SRC, OVERVOLTAGE_NEG, OVERVOLTAGE_POS, and OVERTEMPERATURE.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device1# cd events
      root@analog:/sys/bus/iio/devices/iio:device1/events# echo 1 > out_currentY_thresh_rising_en
      root@analog:/sys/bus/iio/devices/iio:device1/events# cat out_currentY_thresh_rising_en
      1
   


Set fault monitoring thresholds
-------------------------------

| **Description:**
| /sys/bus/iio/devices/iio:deviceX/events/out_currentY_thresh_falling_value
| /sys/bus/iio/devices/iio:deviceX/events/out_currentY_thresh_rising_value
| /sys/bus/iio/devices/iio:deviceX/events/out_voltageY_thresh_falling_value
| /sys/bus/iio/devices/iio:deviceX/events/out_voltageY_thresh_rising_value
| /sys/bus/iio/devices/iio:deviceX/events/out_tempY_thresh_rising_value
| The raw value set determines the threshold that triggers the fault alarm, which automatically shuts down the device if the device is armed. The IIO event attributes correspond to the following: OVERCURRENT_SNK, OVERCURRENT_SRC, OVERVOLTAGE_NEG, OVERVOLTAGE_POS, and OVERTEMPERATURE.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:/sys/bus/iio/devices/iio:device1# cd events
      root@analog:/sys/bus/iio/devices/iio:device1/events# echo 64 > out_currentY_thresh_rising_value
      root@analog:/sys/bus/iio/devices/iio:device1/evemts# cat out_currentY_thresh_rising_value
      64
   

