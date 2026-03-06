.. warning:: Conversion failed for ``resources/tools-software/linux-drivers/iio-inertial-measurement-units/adis165xx``

   Reason: pandoc error: Error at "/tmp/tmponpv3myn.txt" (line 315, column 1):
expecting inline
not found
^ 3-Axis Delta Velocity related device files ^ Description ^
^

.. code-block:: text

   ====== ADIS165XX IIO Inertial Measurement Unit Linux Driver ======
   ===== Supported Devices =====
     * [[adi>ADIS16500]]
     * [[adi>ADIS16505]]
     * [[adi>ADIS16507]]
     * [[adi>ADIS16575]] - TBD: check after it is released
     * [[adi>ADIS16576]] - TBD: check after it is released
     * [[adi>ADIS16577]] - TBD: check after it is released
   
   ===== Overview =====
   
   ==== ADIS1650X ====
   <hidden>
   The ADIS1650X device series is a precision, miniature microelectromechanical system (MEMS) inertial measurement unit (IMU) that includes a triaxial gyroscope and a triaxial accelerometer. Each inertial sensor in the ADIS1650X device series combines with signal conditioning that optimizes dynamic performance. The factory calibration characterizes each sensor for sensitivity, bias, alignment, linear acceleration (gyroscope bias), and point of percussion (accelerometer location). As a result, each sensor has dynamic compensation formulas that provide accurate sensor measurements over a broad set of conditions. 
   
   Applications
     * Navigation, stabilization, and instrumentation
     * Unmanned and autonomous vehicles
     * Smart agriculture and construction machinery
     * Factory/industrial automation, robotics
     * Virtual/augmented reality
     * Internet of Moving Things
   
   {{:resources:tools-software:uc-drivers:adis16500_pcbzangle-web.png?nolink}} 
   </hidden>
   
   ==== ADIS1657X ====
   <hidden>
   - TBD: do after it is released
   </hidden>
   
   ==== Linux Kernel Drivers ====
   This is a Linux industrial I/O ([[software:linux:docs:iio:iio|IIO]]) subsystem driver, targeting SPI interface IMUs.
   The industrial I/O subsystem provides a unified framework for drivers for many different types of converters and sensors using a number of different physical interfaces (i2c, spi, etc). 
   See [[software:linux:docs:iio:iio|IIO]] for more information.
   
   ===== ADIS165XX Family Kernel Drivers =====
   
   ==== Status ====
   ^ Source ^ Mainlined? ^
   |[[repo>linux/tree/dev/adis165x | ADIS165X Development Branch]]| No* |
   
   * Currently only ADIS1650X is mainlined, but with basic functionality. Working on mainlining ADIS1650X and ADIS1657X with other functionalities needed for ROS2 drivers.
   
   ==== Files ====
   
   ^ Function ^ File ^
   | ADIS extended driver | [[linux.github>dev/adis165x/drivers/iio/imu/adis_extd.c | drivers/iio/imu/adis_extd.c]] |
   | ADIS1650X driver | [[linux.github>dev/adis165x/drivers/iio/imu/adis1650x.c | drivers/iio/imu/adis1650x.c]] |
   | ADIS1657X driver | [[linux.github>dev/adis165x/drivers/iio/imu/adis1657x.c | drivers/iio/imu/adis1657x.c]] |
   | ADIS extended header | [[linux.github>dev/adis165x/include/linux/iio/imu/adis_extd.h | include/linux/iio/imu/adis_extd.h]] |
   
   ==== Example platform device initialization ====
   
   === Required properties for the ADIS1650X ===
   <hidden>
     * compatible: Must be one of
       * "adi,adis16500_extd"
       * "adi,adis16505-1_extd"
       * "adi,adis16505-2_extd"
       * "adi,adis16505-3_extd"
       * "adi,adis16507-1_extd"
       * "adi,adis16507-2_extd"
       * "adi,adis16507-3_extd"
     * reg: SPI chip select number for the device
     * spi-cpha: See Documentation/devicetree/bindings/spi/spi-bus.txt
     * spi-cpol: See Documentation/devicetree/bindings/spi/spi-bus.txt
     * interrupts: interrupt mapping for IRQ, accepted values are:
        * IRQF_TRIGGER_RISING
        * IRQF_TRIGGER_FALLING
   </hidden>
   
   === Required properties for the ADIS1657X ===
   <hidden>
     * compatible: Must be one of
       * "adi,adis16575-2_extd"
       * "adi,adis16575-3_extd"
       * "adi,adis16576-2_extd"
       * "adi,adis16576-3_extd"
       * "adi,adis16577-2_extd"
       * "adi,adis16577-3_extd"
     * reg: SPI chip select number for the device
     * spi-cpha: See Documentation/devicetree/bindings/spi/spi-bus.txt
     * spi-cpol: See Documentation/devicetree/bindings/spi/spi-bus.txt
     * interrupts: interrupt mapping for IRQ, accepted values are:
        * IRQF_TRIGGER_RISING
        * IRQF_TRIGGER_FALLING
   </hidden>
   
   ==== Optional properties for the ADIS1650X ====
   <hidden>
     * reset-gpios: must be the device tree identifier of the RESET pin. As the line is active low, it should be marked GPIO_ACTIVE_LOW.
     * spi-max-frequency: Max SPI frequency to use see: Documentation/devicetree/bindings/spi/spi-bus.txt. The maximum supported value is 2MHz.
     * adi,sync-mode: Configures the device sync mode. The following modes are supported:
         * 0 - internal sync mode
         * 1 - direct input sync mode
         * 2 - scaled sync mode
         * 3 - output sync mode
   
     * clocks: phandle to the external clock. Has to be used with direct input sync mode (allowed frequencies: 1900-2100Hz) and scaled sync mode (allowed frequencies: 1-128Hz)
   </hidden>
   
   ==== Optional properties for the ADIS1657X ====
   <hidden>
     * reset-gpios: must be the device tree identifier of the RESET pin. As the line is active low, it should be marked GPIO_ACTIVE_LOW.
     * spi-max-frequency: Max SPI frequency to use see: Documentation/devicetree/bindings/spi/spi-bus.txt. The maximum supported value is 16MHz.
     * adi,sync-mode: Configures the device sync mode. The following modes are supported:
         * 0 - internal sync mode
         * 1 - direct input sync mode
         * 2 - scaled sync mode
         * 3 - output sync mode
   
     * clocks: phandle to the external clock. Has to be used with direct input sync mode (allowed frequencies: 1900-4100Hz) and scaled sync mode (allowed frequencies: 1-400Hz)
   </hidden>
   
   === Example ADIS1650X ===
   <code>
   	imu@0 {
                  compatible = "adi,adis16505-2_extd";
                  adi,sync-mode = <3>;
                  reg = <0>;
                  spi-cpha;
                  spi-cpol;
                  spi-max-frequency = <2000000>;
                  reset-gpios = <&gpio 12 GPIO_ACTIVE_LOW>;
                  interrupts = <4 IRQ_TYPE_EDGE_RISING>;
                  interrupt-parent = <&gpio>;
          };
   </code>
   
   === Example ADIS1657X ===
   <code>
   	imu@0 {
                  compatible = "adi,adis16577-2_extd";
                  adi,sync-mode = <3>;
                  reg = <0>;
                  spi-cpha;
                  spi-cpol;
                  spi-max-frequency = <16000000>;
                  reset-gpios = <&gpio 12 GPIO_ACTIVE_LOW>;
                  interrupts = <4 IRQ_TYPE_EDGE_RISING>;
                  interrupt-parent = <&gpio>;
          };
   </code>
   
   ==== Adding Linux driver support ====
   
   Configure kernel with "make menuconfig".
   == ADIS1650X ==
   <code>
   Linux Kernel Configuration
   	Device Drivers  --->
   		<*>     Industrial I/O support --->
   			--- Industrial I/O support
   			[*]   Enable buffer support within IIO
   			-*-     Industrial I/O buffering based on kfifo
   			-*-   Enable triggered sampling support
   			[--snip--]
   			Inertial measurement units  ---> 
   				[--snip--]
   				<*> Analog Devices ADIS1650X family IMU driver
   				[--snip--]
   </code>
   
   === ADIS1650X ===
   <code>
   Linux Kernel Configuration
   	Device Drivers  --->
   		<*>     Industrial I/O support --->
   			--- Industrial I/O support
   			[*]   Enable buffer support within IIO
   			-*-     Industrial I/O buffering based on kfifo
   			-*-   Enable triggered sampling support
   			[--snip--]
   			Inertial measurement units  ---> 
   				[--snip--]
   				<*> Analog Devices ADIS1657X family IMU driver
   				[--snip--]
   </code>
   
   ==== Hardware configuration ====
   The evaluation kits simplify the process of connecting an IMU to an embedded processor system using a 16-pin, 1mm ribbon cable.
   Here is an example of basic connection from one ADIS device interface connector to the host:(microprocessor):
     DEVICE          HOST MICROPROCESSOR
     * DR   ———————> IRQ GPIO
     * RST  ———————> GPIO
     * CS   <——————— SPI_SEL
     * SCLK <——————— SPI_SCLK
     * DIN  <——————— SPI_MOSI
     * DOUT ———————> SPI_MISO
   
   ==== Example configuration with RPI3/RPI4 ====
   
   === Required Hardware and Hardware Connections ===
   
   == ADIS1650X ==
   
   <hidden>
     * [[ADI>EVAL-ADIS16500]] | [[ADI>EVAL-ADIS16505]] | [[ADI>EVAL-ADIS16507]]
     * Raspberry Pi 3/ Raspberry Pi 4
     * [[ADI>EVAL-ADISIMU1-RPIZ]] with 16-pin, 1mm ribbon cable
   
   {{ :resources:tools-software:linux-drivers:iio-inertial-measurement-units:rpi_falcon.jpg?nolink |}}
   
   </hidden>
   
   == ADIS1657X ==
   
   <hidden>
     * [[ADI>EVAL-ADIS16575]] | [[ADI>EVAL-ADIS16576]] | [[ADI>EVAL-ADIS16577]] - TBD: check after it is released
     * Raspberry Pi 3/ Raspberry Pi 4
     * [[ADI>EVAL-ADISIMU1-RPIZ]] with 16-pin, 1mm ribbon cable
   
   TBD: to add image
   
   </hidden>
   
   
   <WRAP top tip round box 60%>**TIP:**
   An example program which uses the interface can be found here:
     * [[resources:tools-software:linux-software:iio_oscilloscope|IIO Oscilloscope]]
   </WRAP>\\
   
   <WRAP box bggreen><wrap info>This specifies any shell prompt running on the target</wrap>
   <xterm>
   root:/> **cd /sys/bus/iio/devices/**
   root:/sys/bus/iio/devices> **ls**
   iio:device0  trigger0
   
   root:/sys/bus/iio/devices> **cd iio:device0**
   root@analog:/sys/bus/iio/devices/iio:device0# **ls -l**
   total 0
   drwxr-xr-x 2 root root    0 Jul 20 07:17 buffer
   drwxr-xr-x 2 root root    0 Jul 20 07:17 buffer0
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 current_timestamp_clock
   -r--r--r-- 1 root root 4096 Jul 20 07:17 dev
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 filter_low_pass_3db_frequency
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_accel_scale
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_accel_x_calibbias
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_accel_x_raw
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_accel_y_calibbias
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_accel_y_raw
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_accel_z_calibbias
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_accel_z_raw
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_anglvel_scale
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_anglvel_x_calibbias
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_anglvel_x_raw
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_anglvel_y_calibbias
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_anglvel_y_raw
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_anglvel_z_calibbias
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_anglvel_z_raw
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_rot_scale
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_rot_x_raw
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_rot_y_raw
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_rot_z_raw
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_temp_raw
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_temp_scale
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_velocity_scale
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_velocity_x_raw
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_velocity_y_raw
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 in_velocity_z_raw
   -r--r--r-- 1 root root 4096 Jul 20 07:17 name
   lrwxrwxrwx 1 root root    0 Jul 20 07:17 of_node -> ../../../../../../../../firmware/devicetree/base/soc/spi@7e204000/adis1657x@0
   drwxr-xr-x 2 root root    0 Jul 20 07:17 power
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 sampling_frequency
   drwxr-xr-x 2 root root    0 Jul 20 07:17 scan_elements
   lrwxrwxrwx 1 root root    0 Jul 20 07:17 subsystem -> ../../../../../../../../bus/iio
   drwxr-xr-x 2 root root    0 Jul 20 07:17 trigger
   -rw-r--r-- 1 root root 4096 Jul 20 07:17 uevent
   </xterm></WRAP>
   
   ==== ADIS165XX device attributes ====
   
   For a detailed description please see:
   [[git.linux.org>Documentation/ABI/testing/sysfs-bus-iio]]
   
   ^ 3-Axis Accelerometer related device files ^ Description ^
   | in_accel_scale | Scale for the accelerometer channels. |
   | in_accel_x_calibbias | Calibration offset for the X-axis accelerometer channel. |
   | in_accel_x_raw | Raw X-axis accelerometer channel value. |
   | in_accel_y_calibbias | Calibration offset for the Y-axis accelerometer channel. |
   | in_accel_y_raw | Raw Y-axis accelerometer channel value. |
   | in_accel_z_calibbias | Calibration offset for the Z-axis accelerometer channel. |
   | in_accel_z_raw | Raw Z-axis accelerometer channel value. |
   ^ 3-Axis Gyro related device files ^ Description ^
   | in_anglvel_scale | Scale for the gyroscope channels. |
   | in_anglvel_x_calibbias | Calibration offset for the X-axis gyroscope channel. |
   | in_anglvel_x_raw | Raw X-axis gyroscope channel value. |
   | in_anglvel_y_calibbias | Calibration offset for the Y-axis gyroscope channel. |
   | in_anglvel_y_raw | Raw Y-axis gyroscope channel value. |
   | in_anglvel_z_calibbias | Calibration offset for the Z-axis gyroscope channel. |
   | in_anglvel_z_raw | Raw Z-axis gyroscope channel value. |
   ^ Temperature sensor related files ^ Description ^
   | in_temp0_raw | Raw temperature channel value. |
   | in_temp0_scale | Scale for the temperature sensor channel. |
   ^ 3-Axis Delta Angle related device files ^ Description ^
   | in_rot_scale | Scale for the delta angle channels. |
   | in_rot_x_raw | Raw X-axis delta angle channel value. |
   | in_rot_y_raw | Raw Y-axis delta angle channel value. |
   | in_rot_z_raw | Raw Z-axis delta velocity channel value. |.
   ^ 3-Axis Delta Velocity related device files ^ Description ^
   | in_velocity_scale | Scale for the delta angle channels. |
   | in_velocity_x_raw | Raw X-axis delta velocity channel value. |
   | in_velocity_y_raw | Raw Y-axis delta velocity channel value. |
   | in_velocity_z_raw | Raw Z-axis delta velocity channel value. |
   
   ^ Miscellaneous device files ^ Description ^
   | name | Name of the IIO device. |
   | current_timestamp_clock | Current timestamp clock value. |
   | sampling_frequency | Currently selected sample rate. |
   | filter_low_pass_3db_frequency | Bandwidth for the accelerometer and gyroscope channels. |
   
   === Show device name ===
   == ADIS1650X==
   <hidden>
   <WRAP box bggreen><wrap info>This specifies any shell prompt running on the target</wrap>
   <xterm>
   root:/sys/bus/iio/devices/iio:device0> **cat name**
   adis16505-2
   </xterm></WRAP>
   </hidden>
   
   == ADIS1657X==
   <hidden>
   <WRAP box bggreen><wrap info>This specifies any shell prompt running on the target</wrap>
   <xterm>
   root:/sys/bus/iio/devices/iio:device0> **cat name**
   adis16577-2
   </xterm></WRAP>
   </hidden>
   
   === Set sampling frequency ===
   
   The sampling frequency of the device can be set by writing the desired value to the ''sampling_frequency'' file. The driver will automatically round up to the nearest supported sampling frequency.
   
   == ADIS1650X==
   <hidden>
   <WRAP box bggreen><wrap info>This specifies any shell prompt running on the target</wrap>
   <xterm>
   root:/sys/bus/iio/devices/iio:device0> **cat sampling_frequency**
   2000.000000
   pi@raspberrypi:/s
   root:/sys/bus/iio/devices/iio:device0> **echo 1000 > sampling_frequency**
   root:/sys/bus/iio/devices/iio:device0> **cat sampling_frequency**
   1000.000000
   </xterm></WRAP>
   </hidden>
   
   == ADIS1657X==
   <hidden>
   <WRAP box bggreen><wrap info>This specifies any shell prompt running on the target</wrap>
   <xterm>
   root:/sys/bus/iio/devices/iio:device0> **cat sampling_frequency**
   4000.000000
   pi@raspberrypi:/s
   root:/sys/bus/iio/devices/iio:device0> **echo 1000 > sampling_frequency**
   root:/sys/bus/iio/devices/iio:device0> **cat sampling_frequency**
   1000.000000
   </xterm></WRAP>
   </hidden>
   
   === Show channel value ===
   
   A channel value can be read from its ''_raw'' attribute. The value returned by the ''_raw'' attribute is the raw value as reported by the device. To get the processed value of the channel in a standardized unit add the channels ''_offset'' attribute to the ''_raw'' value and multiply the result by ''_scale'' attribute. If no ''_offset'' attribute is present assume 0 for the offset.
   
   ''processed value = (raw + offset) * scale''
   
   The units by the IIO framework are:
     * Acceleration: Meter per Second squared
     * Angular velocity: Rad per second
     * Temperature: milli Degree Celsius
     * Delta angle: Degrees
     * Delta velocity: Meters per Seconds
   
   **Example:**
   <WRAP box bggreen><wrap info>This specifies any shell prompt running on the target</wrap>
   <xterm>
   root:/sys/bus/iio/devices/iio:device0> **cat in_accel_z_raw**
   52612913
   root:/sys/bus/iio/devices/iio:device0> **cat in_accel_scale**
   0.000000187
   </xterm></WRAP>
   
   ''Z-axis acceleration = in_accel_z_raw * in_accel_scale = 52612913 * 0.000000187 m/s^2 = 9.838 m/s^2''
   
   === Set gyro and accel bandwidth ===
   
   The gyro and accel bandwidth can be set by writing the desired value to the ''filter_low_pass_3db_frequency'' attribute. The driver will automatically round up to the nearest supported bandwidth.
   
   **Example:**
   <WRAP box bggreen><wrap info>This specifies any shell prompt running on the target</wrap>
   <xterm>
   root:/sys/bus/iio/devices/iio:device0> **cat filter_low_pass_3db_frequency**
   720.000000
   root:/sys/bus/iio/devices/iio:device0> **echo 360 > filter_low_pass_3db_frequency**
   root:/sys/bus/iio/devices/iio:device0> **cat filter_low_pass_3db_frequency**
   360.000000
   </xterm></WRAP>
   
   
   ==== Trigger management ====
   
   <WRAP round help>
   This driver only supports it's own default trigger source **adis165XX-X-dev0**
   </WRAP>
   
   === ADIS1650X ===
   <WRAP box bggreen><wrap info>This specifies any shell prompt running on the target</wrap>
   <xterm>
   root:/sys/bus/iio/devices/iio:device0> **cat trigger/current_trigger**
   adis16505-2-dev0
   </xterm></WRAP>
   
   === ADIS1657X ===
   <WRAP box bggreen><wrap info>This specifies any shell prompt running on the target</wrap>
   <xterm>
   root:/sys/bus/iio/devices/iio:device0> **cat trigger/current_trigger**
   adis16577-2-dev0
   </xterm></WRAP>
   
   ==== Buffer management ====
   
   <WRAP box bggreen><wrap info>This specifies any shell prompt running on the target</wrap>
   <xterm>
   root:/sys/bus/iio/devices/iio:device0/buffer> **ls**
   **data_available**  **enable**  **length**  **watermark**
   </xterm></WRAP>
   
   {{page>software:linux:docs:iio:iio_snippets#Buffer management&noheader&firstseconly&noeditbtn}}
   
   <WRAP box bggreen><wrap info>This specifies any shell prompt running on the target</wrap>
   <xterm>
   root:/sys/bus/iio/devices/iio:device0/scan_elements> **ls -l**
   total 0
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_accel_x_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_accel_x_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_accel_x_type
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_accel_y_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_accel_y_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_accel_y_type
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_accel_z_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_accel_z_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_accel_z_type
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_anglvel_x_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_anglvel_x_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_anglvel_x_type
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_anglvel_y_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_anglvel_y_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_anglvel_y_type
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_anglvel_z_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_anglvel_z_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_anglvel_z_type
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_rot_x_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_rot_x_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_rot_x_type
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_rot_y_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_rot_y_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_rot_y_type
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_rot_z_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_rot_z_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_rot_z_type
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_temp_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_temp_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_temp_type
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_timestamp_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_timestamp_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_timestamp_type
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_velocity_x_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_velocity_x_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_velocity_x_type
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_velocity_y_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_velocity_y_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_velocity_y_type
   -rw-r--r-- 1 root root 4096 Jul 20 08:42 in_velocity_z_en
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_velocity_z_index
   -r--r--r-- 1 root root 4096 Jul 20 07:17 in_velocity_z_type
   </xterm></WRAP>
   
