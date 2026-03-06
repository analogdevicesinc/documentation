ADAR300x Linux Driver
=====================

Supported Devices
-----------------

-  :adi:`ADAR3000`
-  :adi:`ADAR3001`
-  :adi:`ADAR3002`
-  :adi:`ADAR3003`

Device Tree Example
-------------------

.. code:: c

   #include "zynqmp-zcu102-rev1.0.dts"
   &spi0 {
       status = "okay";
       adar3000: adar3000@0 {
           compatible = "adi,adar3000";
           reg = <0>;
           spi-max-frequency = <1000000>;

           #address-cells = <1>;
           #size-cells = <0>;

           adar3000_0@0 {
               reg = <0>;
               label = "adar3000_0";
           };
                   
                   //...
                   
                   adar3000_15@15 {
               reg = <15>;
               label = "adar3000_15";
           };
                   // Maximum 16 ADAR devices on the same CS
       };
   };

Driver testing
==============

Attribute list
==============

Running the command:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt command

   
   ::
   
      iio_info -n 10.48.65.150
   


Will output something similar:

::

     iio:device1: adar3002_0 (buffer capable)
         33 channels found:
             phase0:  (output, index: 0, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_H_EL0_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power0:  (output, index: 1, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_H_EL0_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase1:  (output, index: 2, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_H_EL1_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power1:  (output, index: 3, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_H_EL1_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase2:  (output, index: 4, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_H_EL2_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power2:  (output, index: 5, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_H_EL2_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase3:  (output, index: 6, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_H_EL3_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power3:  (output, index: 7, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_H_EL3_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase4:  (output, index: 8, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_V_EL0_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power4:  (output, index: 9, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_V_EL0_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase5:  (output, index: 10, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_V_EL1_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power5:  (output, index: 11, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_V_EL1_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase6:  (output, index: 12, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_V_EL2_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power6:  (output, index: 13, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_V_EL2_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase7:  (output, index: 14, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_V_EL3_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power7:  (output, index: 15, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM0_V_EL3_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase8:  (output, index: 16, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_V_EL0_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power8:  (output, index: 17, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_V_EL0_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase9:  (output, index: 18, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_V_EL1_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power9:  (output, index: 19, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_V_EL1_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase10:  (output, index: 20, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_V_EL2_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power10:  (output, index: 21, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_V_EL2_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase11:  (output, index: 22, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_V_EL3_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power11:  (output, index: 23, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_V_EL3_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase12:  (output, index: 24, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_H_EL0_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power12:  (output, index: 25, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_H_EL0_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase13:  (output, index: 26, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_H_EL1_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power13:  (output, index: 27, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_H_EL1_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase14:  (output, index: 28, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_H_EL2_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power14:  (output, index: 29, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_H_EL2_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             phase15:  (output, index: 30, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_H_EL3_DELAY
                 attr  1: raw value: 0
                 attr  2: scale value: 5.714285714
             power15:  (output, index: 31, format: le:u6/8>>0)
             3 channel-specific attributes found:
                 attr  0: label value: BEAM1_H_EL3_ATTENUATION
                 attr  1: raw value: 0
                 attr  2: scale value: 0.492063492
             temp16:  (input, index: 32, format: le:U8/8>>0)
             3 channel-specific attributes found:
                 attr  0: offset value: 86.362000
                 attr  1: raw value: 255
                 attr  2: scale value: 0.911500
         91 device-specific attributes found:
                 attr  0: amp_bias_mute_EL0V value: 3
                 attr  1: amp_bias_mute_EL1V value: 3
                 attr  2: amp_bias_mute_EL2V value: 3
                 attr  3: amp_bias_mute_EL3V value: 3
                 attr  4: amp_bias_operational_EL0H value: 3
                 attr  5: amp_bias_operational_EL0V value: 3
                 attr  6: amp_bias_operational_EL1H value: 3
                 attr  7: amp_bias_operational_EL1V value: 3
                 attr  8: amp_bias_operational_EL2H value: 0
                 attr  9: amp_bias_operational_EL2V value: 3
                 attr 10: amp_bias_operational_EL3H value: 3
                 attr 11: amp_bias_operational_EL3V value: 3
                 attr 12: amp_bias_reset_EL0V value: 3
                 attr 13: amp_bias_reset_EL1V value: 3
                 attr 14: amp_bias_reset_EL2V value: 3
                 attr 15: amp_bias_reset_EL3V value: 3
                 attr 16: amp_bias_sleep_EL0H value: 3
                 attr 17: amp_bias_sleep_EL0V value: 3
                 attr 18: amp_bias_sleep_EL1H value: 3
                 attr 19: amp_bias_sleep_EL1V value: 3
                 attr 20: amp_bias_sleep_EL2H value: 3
                 attr 21: amp_bias_sleep_EL2V value: 3
                 attr 22: amp_bias_sleep_EL3H value: 3
                 attr 23: amp_bias_sleep_EL3V value: 3
                 attr 24: amp_en_mute_EL0V value: 1
                 attr 25: amp_en_mute_EL1V value: 1
                 attr 26: amp_en_mute_EL2V value: 1
                 attr 27: amp_en_mute_EL3V value: 1
                 attr 28: amp_en_operational_EL0H value: 1
                 attr 29: amp_en_operational_EL0V value: 1
                 attr 30: amp_en_operational_EL1H value: 1
                 attr 31: amp_en_operational_EL1V value: 1
                 attr 32: amp_en_operational_EL2H value: 1
                 attr 33: amp_en_operational_EL2V value: 1
                 attr 34: amp_en_operational_EL3H value: 1
                 attr 35: amp_en_operational_EL3V value: 1
                 attr 36: amp_en_reset_EL0V value: 1
                 attr 37: amp_en_reset_EL1V value: 1
                 attr 38: amp_en_reset_EL2V value: 1
                 attr 39: amp_en_reset_EL3V value: 1
                 attr 40: amp_en_sleep_EL0H value: 0
                 attr 41: amp_en_sleep_EL0V value: 0
                 attr 42: amp_en_sleep_EL1H value: 0
                 attr 43: amp_en_sleep_EL1V value: 0
                 attr 44: amp_en_sleep_EL2H value: 0
                 attr 45: amp_en_sleep_EL2V value: 0
                 attr 46: amp_en_sleep_EL3H value: 0
                 attr 47: amp_en_sleep_EL3V value: 0
                 attr 48: beam0_fifo_rd value: 0
                 attr 49: beam0_fifo_wr value: 0
                 attr 50: beam0_load_mode value: direct
                 attr 51: beam0_load_mode_available value: direct memory fifo instant_direct reset mute
                 attr 52: beam0_mode value: direct
                 attr 53: beam0_mode_available value: direct memory fifo instant_direct reset mute
                 attr 54: beam0_ram_index value: 0
                 attr 55: beam0_ram_start value: 0
                 attr 56: beam0_ram_stop value: 63
                 attr 57: beam0_update value: 0
                 attr 58: beam1_fifo_rd value: 0
                 attr 59: beam1_fifo_wr value: 0
                 attr 60: beam1_load_mode value: direct
                 attr 61: beam1_load_mode_available value: direct memory fifo instant_direct reset mute
                 attr 62: beam1_mode value: direct
                 attr 63: beam1_mode_available value: direct memory fifo instant_direct reset mute
                 attr 64: beam1_ram_index value: 0
                 attr 65: beam1_ram_start value: 0
                 attr 66: beam1_ram_stop value: 63
                 attr 67: beam1_update value: 0
                 attr 68: beam2_fifo_rd value: 0
                 attr 69: beam2_fifo_wr value: 0
                 attr 70: beam2_load_mode value: direct
                 attr 71: beam2_load_mode_available value: direct memory fifo instant_direct reset mute
                 attr 72: beam2_mode value: direct
                 attr 73: beam2_mode_available value: direct memory fifo instant_direct reset mute
                 attr 74: beam2_ram_index value: 0
                 attr 75: beam2_ram_start value: 0
                 attr 76: beam2_ram_stop value: 63
                 attr 77: beam2_update value: 0
                 attr 78: beam3_fifo_rd value: 0
                 attr 79: beam3_fifo_wr value: 0
                 attr 80: beam3_load_mode value: direct
                 attr 81: beam3_load_mode_available value: direct memory fifo instant_direct reset mute
                 attr 82: beam3_mode value: direct
                 attr 83: beam3_mode_available value: direct memory fifo instant_direct reset mute
                 attr 84: beam3_ram_index value: 0
                 attr 85: beam3_ram_start value: 0
                 attr 86: beam3_ram_stop value: 63
                 attr 87: beam3_update value: 0
                 attr 88: label value: adar3002_T0
                 attr 89: update_intf_ctrl value: pin
                 attr 90: update_intf_ctrl_available value: pin SPI
         2 buffer-specific attributes found:
                 attr  0: data_available value: 0
                 attr  1: watermark value: 2048
         1 debug attributes found:
                 debug attr  0: direct_reg_access value: 0x18
         No trigger on this device
     iio:device2: one-bit-adc-dac
         4 channels found:
             voltage1:  (output)
             2 channel-specific attributes found:
                 attr  0: label value: RSTB
                 attr  1: raw value: 0
             voltage3:  (output)
             2 channel-specific attributes found:
                 attr  0: label value: RESET
                 attr  1: raw value: 0
             voltage0:  (output)
             2 channel-specific attributes found:
                 attr  0: label value: MUTE
                 attr  1: raw value: 0
             voltage2:  (output)
             2 channel-specific attributes found:
                 attr  0: label value: UPDATE
                 attr  1: raw value: 0
         1 device-specific attributes found:
                 attr  0: label value: long_peack_control

ADAR300x attributes
===================

Channel attributes
~~~~~~~~~~~~~~~~~~

-  label - For better identifying channel
-  raw - Multiplied with scale will result in a physical value.
-  scale - Multiplied with raw will result in a physical value.

   -  delay = raw*scale

      -  gain = raw*scale

Device attributes
~~~~~~~~~~~~~~~~~

-  beamx_fifo_rd - FIFO read pointer
-  beamx_fifo_wr - FIFO write pointer
-  beamx_load_mode - Specifies the section where the beamstate is saved
-  beamx_load_mode_available - Possible values: direct memory fifo instant_direct reset mute
-  beamx_mode - Beam operation mode
-  beamx_mode_available - Possible values: direct memory fifo instant_direct reset mute
-  beamx_ram_index - Starting position in memory for saving beamstates
-  beamx_ram_start - Start beamstate in memory. Default: 0
-  beamx_ram_stop - Stop beamstate in memory. Default: 63
-  beamx_update - Update beamstate
-  update_intf_ctrl - Update mode
-  update_intf_ctrl_available - Update mode available: pin SPI
-  label
-  amp_bias_mute_ELxV
-  amp_bias_operational_ELxH
-  amp_bias_operational_ELxV
-  amp_bias_reset_ELxV
-  amp_bias_sleep_ELxH
-  amp_bias_sleep_ELxV
-  amp_en_mute_ELxV
-  amp_en_operational_ELxH
-  amp_en_operational_ELxV
-  amp_en_reset_ELxV
-  amp_en_sleep_ELxH
-  amp_en_sleep_ELxV

Beam components
~~~~~~~~~~~~~~~

-  **Beam0**: power0, phase0, power1, phase1, power2, phase2, power3, phase3
-  **Beam1**: power4, phase4, power5, phase5, power6, phase6, power7, phase7
-  **Beam2**: power8, phase8, power9, phase9, power10, phase10, power11, phase11
-  **Beam3**: power12, phase12, power13, phase13, power14, phase14, power15, phase15

Read/write attribute
====================

::

   iio_attr -u ip:10.48.65.150 -c adar3002_0 phase0 raw
   0
   iio_attr -u ip:10.48.65.150 -c adar3002_0 phase0 raw 3
   3

Read/write register
===================

Write scratchpad:

::

   iio_reg -u ip:10.48.65.150 adar3002_0 0x0A 0xf3

Read scratchpad:

::

   iio_reg -u ip:10.48.65.150 adar3002_0 0x0A

Read/write instant direct
=========================

Every beam has two mode attributes:

-  beam0_load_mode - Specifies the mode corresponding to where the values are saved. Ex: The device can be into "beam0_mode = instant_direct" and "beam0_load_mode = direct". Data will be saved into registers corresponding to "direct" mode.
-  beam0_mode - Specifies current beam mode for operating.

Select beam state:

::

   iio_attr -u ip:10.48.65.150 -d adar3002_0 beam0_mode instant_direct
   iio_attr -u ip:10.48.65.150 -d adar3002_0 beam0_load_mode instant_direct

Write beam state:

::

   iio_attr -u ip:10.48.65.150 -c adar3002_0 phase0 raw 10
   iio_attr -u ip:10.48.65.150 -c adar3002_0 phase1 raw 11
   iio_attr -u ip:10.48.65.150 -c adar3002_0 phase2 raw 12
   iio_attr -u ip:10.48.65.150 -c adar3002_0 phase3 raw 13

   iio_attr -u ip:10.48.65.150 -c adar3002_0 power0 raw 20
   iio_attr -u ip:10.48.65.150 -c adar3002_0 power1 raw 21
   iio_attr -u ip:10.48.65.150 -c adar3002_0 power2 raw 22
   iio_attr -u ip:10.48.65.150 -c adar3002_0 power3 raw 23

Read beam state

::

   iio_attr -u ip:10.48.65.150 -c adar3002_0 phase0 raw
   iio_attr -u ip:10.48.65.150 -c adar3002_0 phase1 raw 
   iio_attr -u ip:10.48.65.150 -c adar3002_0 phase2 raw 
   iio_attr -u ip:10.48.65.150 -c adar3002_0 phase3 raw 

   iio_attr -u ip:10.48.65.150 -c adar3002_0 power0 raw
   iio_attr -u ip:10.48.65.150 -c adar3002_0 power1 raw
   iio_attr -u ip:10.48.65.150 -c adar3002_0 power2 raw
   iio_attr -u ip:10.48.65.150 -c adar3002_0 power3 raw

For better identifying the channel, read "label" property:

::

   iio_attr -u ip:10.48.65.110 -c adar3002_0 phase0 label
   BEAM0_H_EL0_DELAY

Read/write direct
=================

Same as instant direct, before writing/reading, set load_mode to "direct":

::

   iio_attr -u ip:10.48.65.150 -d adar3002_0 beam0_load_mode direct

Read/write reset
================

Same as instant direct, before writing/reading, set load_mode to "reset":

::

   iio_attr -u ip:10.48.65.150 -d adar3002_0 beam0_load_mode reset

Read/write memory
=================

Using attributes
~~~~~~~~~~~~~~~~

Same as instant direct, before writing/reading, set load_mode to "memory":

::

   iio_attr -u ip:10.48.65.150 -d adar3002_0 beam0_load_mode memory

And set ram index(between 0 and 63):

::

   iio_attr -u ip:10.48.65.150 -d adar3002_0 beam0_ram_index 3

Using buffers
~~~~~~~~~~~~~

Data has to be stored into a file and it can be created with a hex editor. Each beam is composed of 4 elements and each element has two components (delay and attenuation), so one beam state is stored using 8 bytes of data(the util part will be 6 bits in each byte). Those are packed into the driver so that they will occupy only 6 bytes into the memory. Execute commands:

::

   ./add_trigger.sh # should be called only once, trigger is reused
   ./memory_write.sh /sys/bus/iio/devices/iio:device1 3 sample_512bytes.dat memory

Write FIFO
==========

Using file system attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Same as instant direct, before writing, set load_mode to "fifo":

::

   iio_attr -u ip:10.48.65.150 -d adar3002_0 beam0_load_mode fifo

FIFO beam states are write only. Setting the last parameter of the beamstate (phase3, phase7, phase11, phase15), will trigger an actual write/push into FIFO, until then the parameters are stored into a buffer. Reading the beamstate, will return the temporary values saved in the buffer.

Write fifo pointer read:

::

   iio_attr -u ip:10.48.65.150 -d adar3002_0 beam0_fifo_rd
   0

After an update command:

::

   iio_attr -u ip:10.48.65.150 -d adar3002_0 beam0_update 1

The fifo read pointer is incremented if a valid beamstate is present (fifo wr pointer > fifo rd pointer).

Read FIFO write pointer:

::

   iio_attr -u ip:10.48.65.150 -d adar3002_0 beam0_fifo_wr
   1

.. _using-buffers-1:

Using buffers
~~~~~~~~~~~~~

Data has to be stored into a file and it can be created with a hex editor. Each beam is composed of 4 elements and each element has two components (delay and attenuation), so one beam state is stored using 8 bytes of data(the util part will be 6 bits in each byte). Those are packed into the driver so that they will occupy only 6 bytes into the FIFO.

::

   ./add_trigger.sh # should be called only once, trigger is reused
   ./memory_write.sh /sys/bus/iio/devices/iio:device1 0 sample_8bytes.dat fifo

Add trigger
~~~~~~~~~~~

.. code:: bash

   #!/bin/sh
   echo 0 > /sys/bus/iio/devices/iio_sysfs_trigger/add_trigger
   echo sysfstrig0 > /sys/bus/iio/devices/iio:device1/trigger/current_trigger

Memory write
~~~~~~~~~~~~

.. code:: bash

   #!/bin/sh
   #device_name="/sys/bus/iio/devices/iio:device1"
   device_name=$1
   beam=$2
   binary_file=$3
   load_mode=$4

   if [ ! -d "$device_name" ]; then
       echo "$device_name device does not exist."
       exit 1;
   fi

   if [ "$beam" -gt 3 ]; then
       echo "Maximum beams number is 3, please insert a number between 0 and 3"
       exit 1;
   fi

   if [ ! -f "$binary_file" ]; then
       echo "$binary_file binary file does not exist."
       exit 1;
   fi

   if [ "$load_mode" != "memory" ] && [ "$load_mode" != "fifo" ]; then
       echo "Load mode should be \"memory\" or \"fifo\", $load_mode."
       exit 1;
   fi


   dev_name_strs=$(echo $device_name | tr "/" "\n")
   for path in $dev_name_strs
   do
       dev_name=$path
   done

   buffer_length=$(wc -c $binary_file | awk '{print $1}')
   if ((buffer_length % 8)); then
       echo "$binary_file length is $buffer_length, it should be multiple of 8."
       exit 1;
   fi


   echo $load_mode > $device_name/beam"${beam}"_load_mode
   for i in {0..3}
   do
       echo 1 > $device_name/scan_elements/out_phase"$((4*beam+i))"_en
       echo 1 > $device_name/scan_elements/out_power"$((4*beam+i))"_en
   done

   echo $buffer_length > $device_name/buffer/length
   echo 1 > $device_name/buffer/enable

   cat $binary_file > /dev/$dev_name

   echo 1 > /sys/bus/iio/devices/trigger0/trigger_now

   echo 0 > $device_name/buffer/enable
   echo 0 > $device_name/buffer/length

   for i in {0..3}
   do
       echo 0 > $device_name/scan_elements/out_phase"$((4*beam+i))"_en
       echo 0 > $device_name/scan_elements/out_power"$((4*beam+i))"_en
   done

Update
======

Configure update mode:

GPIO:

::

   iio_attr -u ip:10.48.65.150 -d adar3002_0 update_intf_ctrl pin

Or SPI:

::

   iio_attr -u ip:10.48.65.150 -d adar3002_0 update_intf_ctrl SPI

In case of SPI selection, send update command:

::

   iio_attr -u ip:10.48.65.150 -d adar3002_0 beam0_update 1

GPIO control
============

This is done trough "one-bit-adc-dac" device:

::

   iio_attr -u ip:10.48.65.110 -c one-bit-adc-dac voltage2 raw 1

For better identifying the channel, read "label" property:

::

   iio_attr -u ip:10.48.65.110 -c one-bit-adc-dac voltage2 label
   UPDATE
