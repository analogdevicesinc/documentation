Evaluating ADIS165XX family with ROS2
=====================================

Supported Evaluation Boards
---------------------------

-  :adi:`EVAL-ADIS16500`
-  :adi:`EVAL-ADIS16505`
-  :adi:`EVAL-ADIS16507`
-  :adi:`EVAL-ADIS16575` - TBD
-  :adi:`EVAL-ADIS16576` - TBD
-  :adi:`EVAL-ADIS16577` - TBD

EVAL-ADIS165XX Overview
-----------------------

EVAL-ADIS1650X
~~~~~~~~~~~~~~

The ADIS1650X device series is a precision, miniature microelectromechanical system (MEMS) inertial measurement unit (IMU) that includes a triaxial gyroscope and a triaxial accelerometer. Each inertial sensor in the ADIS1650X device series combines with signal conditioning that optimizes dynamic performance. The factory calibration characterizes each sensor for sensitivity, bias, alignment, linear acceleration (gyroscope bias), and point of percussion (accelerometer location). As a result, each sensor has dynamic compensation formulas that provide accurate sensor measurements over a broad set of conditions.

Applications:

-  Navigation, stabilization, and instrumentation
-  Unmanned and autonomous vehicles
-  Smart agriculture and construction machinery
-  Factory/industrial automation, robotics
-  Virtual/augmented reality
-  Internet of Moving Things

EVAL-ADIS1657X
~~~~~~~~~~~~~~

TBD

ROS2 drivers with ADIS165XX family
----------------------------------

Overview IMU-ROS2 driver
~~~~~~~~~~~~~~~~~~~~~~~~

IMU-ROS2 is a application that runs in a ROS2 environment. Specifically IMU-ROS2 is an node. In ROS2 a node can be a publisher, a subscriber or both. Nodes can communicate to each other through topics. The data from topics have different types. A subscriber is a node that receives data through topics. A publisher is a node that sends data through topics. IMU-ROS2 is a publisher node which sends several information on topics. IMU-ROS2 driver reads IMU data using :doc:`LibIIO </wiki-migration/resources/tools-software/linux-software/libiio_internals>`. The image below shows the top-down software architecture:


|image1|

ROS2 topics
~~~~~~~~~~~

Topics are the channels of communication between a publisher and a subscriber. Topics are like pipes and the liquid sent through the pipe is the measured sensor data. Topics have a name for identification. With ROS2 commands like "topic echo" will print on the console the data that is sent over that topic. The data from the topic can be viewed graphically with visualization clients, like RQT.

/imu topic
^^^^^^^^^^

**/imu** is a topic that has a standard type. The type is described here: `Imu Standard Message <http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/Imu.html>`__. This topic is published when measured_data_topic_selection parameter is set to 2. Please see the parameters section for more information about ROS2 parameters. The data is acquired using IIO buffer. In this case the readings are performed on each impulse on the data ready pin of the IMU device.

The topic has the following definition:

.. code:: C

   std_msgs/Header header
   geometry_msgs/Quaternion orientation
   float64[9] orientation_covariance
   geometry_msgs/Vector3 angular_velocity
   float64[9] angular_velocity_covariance
   geometry_msgs/Vector3 linear_acceleration
   float64[9] linear_acceleration_covariance

The ROS2 driver populates the angular_velocity and linear_acceleration with data from the IMU sensor.

/accelgyrotempdata topic
^^^^^^^^^^^^^^^^^^^^^^^^

**/accelgyrotempdata** is a topic with a custom type. This topic is published when measured_data_topic_selection parameter is set to 0. Please see the parameters section for more information about ROS2 parameters. The data is acquired using IIO buffer. In this case the readings are performed on each impulse on the data ready pin of the IMU device.

The topic has the following definition:

.. code:: C

   # 3-axis acceleration [m/s^2]
   geometry_msgs/Vector3 linear_acceleration

   # 3-axis angular velocity [rad/s]
   geometry_msgs/Vector3 angular_velocity

   # imu internal temperature [°C]
   float64 temperature

   # sample timestamp
   int64 timestamp

/velangtempdata topic
^^^^^^^^^^^^^^^^^^^^^

**/velangtempdata** is a topic with a custom type. This topic is published when measured_data_topic_selection parameter is set to 1. Please see the parameters section for more information about ROS2 parameters. The data is acquired using IIO buffer. In this case the readings are performed on each impulse on the data ready pin of the IMU device.

The topic has the following definition:

.. code:: C

   # 3-axis delta velocity (delta between two consecutive measurements) [m/s]
   geometry_msgs/Vector3 delta_velocity

   # 3-axis delta angle (delta between two consecutive measurements) [degrees]
   geometry_msgs/Vector3 delta_angle

   # imu internal temperature [°C]
   float64 temperature

   # sample timestamp
   int64 timestamp

/imufullmeasureddata topic
^^^^^^^^^^^^^^^^^^^^^^^^^^

**/imufullmeasureddata** is a topic with a custom type. This topic is published when measured_data_topic_selection parameter is set to 3. Please see the parameters section for more information about ROS2 parameters. The data is acquired using IIO raw value readings. In this case the readings do not take into account the data ready signal from the device.

The topic has the following definition:

.. code:: C

   # 3-axis acceleration [m/s^2]
   geometry_msgs/Vector3 linear_acceleration

   # 3-axis angular velocity [rad/s]
   geometry_msgs/Vector3 angular_velocity

   # 3-axis delta velocity (delta between two consecutive measurements) [m/s]
   geometry_msgs/Vector3 delta_velocity

   # 3-axis delta angle (delta between two consecutive measurements) [degrees]
   geometry_msgs/Vector3 delta_angle

   # imu internal temperature [°C]
   float64 temperature

/imu1650xdiagdata topic
^^^^^^^^^^^^^^^^^^^^^^^

**/imu1650xdiagdata** is a topic with a custom type. It publishes diagnosis data from the ADIS1650X device when such a device is detected.

The topic has the following definition:

.. code:: C

   # if true, one of the datapaths experienced an overrun condition
   bool diag_data_path_overrun

   # if true, the most recent imu memory flash failed
   bool diag_flash_memory_update_error

   # if true, the total number of SPI SCLK cycles is not equal to an integer multiple of 16
   bool diag_spi_communication_error

   # if true, the imu voltage across VDD and GND < 2.9V, which causes data processing to stop
   bool diag_standby_mode

   # if true, the imu self-test routine failed
   bool diag_sensor_self_test_error

   # if true, there is a failure in imu flash memory
   bool diag_flash_memory_test_error

   # if true, the internal data sampling clock does not synchronize with the external clock (only in scaled sync mode)
   bool diag_clock_error

   # if true, a failure occurred on accelerometer
   bool diag_acceleration_self_test_error

   # if true, a failure occurred on gyroscope 1
   bool diag_gyroscope1_self_test_error

   # if true, a failure occurred on gyroscope 2
   bool diag_gyroscope2_self_test_error

   # if true, a checksum error occurred in the previous SPI transaction
   bool diag_checksum_error_flag

   # if true, the imu flash memory was written more times than the data-sheet specified endurance
   bool diag_flash_memory_write_count_exceeded_error

   # the value of the imu flash writes
   uint32 flash_counter

   # the number of lost samples in imu driver, applies only when buffer readings are performed
   uint32 lost_samples_count

/imu1657xdiagdata topic
^^^^^^^^^^^^^^^^^^^^^^^

**/imu1657xdiagdata** is a topic with a custom type. It publishes diagnosis data from the ADIS1657X device when such a device is detected.

The topic has the following definition:

.. code:: C

   # if true, the imu failed to initialize properly
   bool diag_sensor_initialization_failure

   # if true, one of the datapaths experienced an overrun condition
   bool diag_data_path_overrun

   # if true, the most recent imu memory flash failed
   bool diag_flash_memory_update_error

   # if true, the total number of SPI SCLK cycles is not equal to an integer multiple of 16
   bool diag_spi_communication_error

   # if true, the imu voltage across VDD and GND < 2.9V, which causes data processing to stop
   bool diag_standby_mode

   # if true, the imu self-test routine failed
   bool diag_sensor_self_test_error

   # if true, there is a failure in imu flash memory
   bool diag_flash_memory_test_error

   # if true, the internal data sampling clock does not synchronize with the external clock (only in scaled sync mode)
   bool diag_clock_error

   # if true, a failure occurred on x axis gyroscope
   bool diag_x_axis_gyroscope_failure

   # if true, a failure occurred on y axis gyroscope
   bool diag_y_axis_gyroscope_failure

   # if true, a failure occurred on z axis gyroscope
   bool diag_z_axis_gyroscope_failure

   # if true, a failure occurred on x axis accelerometer
   bool diag_x_axis_accelerometer_failure

   # if true, a failure occurred on y axis accelerometer
   bool diag_y_axis_accelerometer_failure

   # if true, a failure occurred on z axis accelerometer
   bool diag_z_axis_accelerometer_failure

   # if true, a fault occurred in the imu microcontroller
   bool diag_aduc_mcu_fault

   # if true, a checksum error occurred in the previous SPI transaction
   bool diag_checksum_error_flag

   # if true, the imu flash memory was written more times than the data-sheet specified endurance
   bool diag_flash_memory_write_count_exceeded_error

   # the value of the imu flash writes
   uint32 flash_counter

   # the number of lost samples in imu driver, applies only when buffer readings are performed
   uint32 lost_samples_count

/imuidentificationdata topic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**/imuidentificationdata** is a topic with a custom type. It publishes device specific identification data.

The topic has the following definition:

.. code:: C

   # firmware revision for the imu internal firmware
   string firmware_revision

   # firmware date for the imu internal firmware
   string firmware_date

   # imu product identification
   uint32 product_id

   # imu lot specific serial number
   uint32 serial_number

   # imu gyroscope measurement range
   string gyroscope_measurement_range

ROS2 topic commands examples with IMU-ROS2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to see the available sub-commands for ROS2 topic, simply type **ros2 topic -h** as shown below:

::

   **ros2 topic -h**
   usage: ros2 topic [-h] [--include-hidden-topics] Call `ros2 topic <command> -h` for more detailed usage. ...

   Various topic related sub-commands

   optional arguments:
     -h, --help            show this help message and exit
     --include-hidden-topics
                           Consider hidden topics as well

   Commands:
     bw     Display bandwidth used by topic
     delay  Display delay of topic from timestamp in header
     echo   Output messages from a topic
     find   Output a list of available topics of a given type
     hz     Print the average publishing rate to screen
     info   Print information about a topic
     list   Output a list of available topics
     pub    Publish a message to a topic
     type   Print a topic's type

     Call `ros2 topic <command> -h` for more detailed usage.

The following command shows the available topics in IMU-ROS2 application:

For ADIS1650X:

::

   **ros2 topic list**
   /accelgyrotempdata
   /imu
   /imu1650xdiagdata
   /imufullmeasureddata
   /imuidentificationdata
   /velangtempdata

For ADIS1657X:

::

   **ros2 topic list**
   /accelgyrotempdata
   /imu
   /imu1657xdiagdata
   /imufullmeasureddata
   /imuidentificationdata
   /velangtempdata

The following command can be used to print the data on a topic:

::

   **ros2 topic echo /imufullmeasureddata**
   linear_acceleration:
     x: -0.249862855
     y: -0.006555846
     z: 9.818095782
   angular_velocity:
     x: 0.000122688
     y: -0.000615318
     z: -0.000237882
   delta_velocity:
     x: -0.00062054
     y: -1.4628000000000001e-05
     z: 0.024211456
   delta_angle:
     x: -1.9228e-05
     y: 0.000234498
     z: -0.000161557
   temperature: 21.5

::

   **ros2 topic echo /accelgyrotempdata**
   linear_acceleration:
     x: -58.396143267
     y: 326.283689094
     z: 0.0
   angular_velocity:
     x: 0.00039317999999999997
     y: -0.002359314
     z: 0.315359286
   temperature: 22.6
   timestamp: 1690526282692819125

::

   **ros2 topic echo /imu**
   header:
     stamp:
       sec: 0
       nanosec: 0
     frame_id: ''
   orientation:
     x: 0.0
     y: 0.0
     z: 0.0
     w: 1.0
   orientation_covariance:
   - -1.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   angular_velocity:
     x: -0.003145728
     y: -0.003538968
     z: 0.313786422
   angular_velocity_covariance:
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   linear_acceleration:
     x: -397.265561616
     y: 326.28366815
     z: 0.0
   linear_acceleration_covariance:
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0
   - 0.0

::

   **ros2 topic echo /velangtempdata**
   delta_velocity:
     x: -41.550993528
     y: 80.262316482
     z: 0.0
   delta_angle:
     x: -2.09e-07
     y: -2.09e-07
     z: 0.0
   temperature:22.5
   timestamp: 1690527392354411778

::

   **ros2 topic echo /imu1657xdiagdata**
   diag_sensor_initialization_failure: false
   diag_data_path_overrun: false
   diag_flash_memory_update_error: false
   diag_spi_communication_error: false
   diag_standby_mode: false
   diag_sensor_self_test_error: false
   diag_flash_memory_test_error: false
   diag_clock_error: false
   diag_x_axis_gyroscope_failure: false
   diag_y_axis_gyroscope_failure: false
   diag_z_axis_gyroscope_failure: false
   diag_x_axis_accelerometer_failure: false
   diag_y_axis_accelerometer_failure: false
   diag_z_axis_accelerometer_failure: false
   diag_aduc_mcu_fault: false
   diag_checksum_error_flag: false
   diag_flash_memory_write_count_exceeded_error: false
   flash_counter: 2
   lost_samples_count: 0

::

   **ros2 topic echo /imuidentificationdata**
       total count change:1135893
       total count: 1135893---
   firmware_revision: '0.16'
   firmware_date: 03-02-2023
   product_id: 16577
   serial_number: 54
   gyroscope_measurement_range: +/-500_degrees_per_sec

Topics for adis1650x

::

   **ros2 topic echo /imu1650xdiagdata**
   diag_data_path_overrun: false
   diag_flash_memory_update_error: false
   diag_spi_communication_error: false
   diag_standby_mode: false
   diag_sensor_self_test_error: false
   diag_flash_memory_test_error: false
   diag_clock_error: false
   diag_acceleration_self_test_error: false
   diag_gyroscope1_self_test_error: false
   diag_gyroscope2_self_test_error: false
   diag_checksum_error_flag: false
   diag_flash_memory_write_count_exceeded_error: false
   flash_counter: 69
   lost_samples_count: 0

::

   **ros2 topic echo /imuidentificationdata**
       total count change:143208
       total count: 143208---
   firmware_revision: '1.6'
   firmware_date: 06-27-2019
   product_id: 16505
   serial_number: 1205
   gyroscope_measurement_range: +/-500_degrees_per_sec

ROS2 parameters
~~~~~~~~~~~~~~~

Overview
^^^^^^^^

The ros2 parameters are a way to send variable data from command line to a node. With this, the node can read data from console and execute commands like send data to a specific topic or make the node to run in a specific way.

ADIS1650X parameters
^^^^^^^^^^^^^^^^^^^^

+----------------------------------+------------------------------------+------------------------------------------------------------------------+
| Parameter Name                   | Allowed Values                     | Parameter Description                                                  |
+==================================+====================================+========================================================================+
| accel_calibbias_x                | -2,147,483,648 up-to 2,147,483,647 | x-axis acceleration offset correction                                  |
+----------------------------------+------------------------------------+------------------------------------------------------------------------+
| accel_calibbias_y                | -2,147,483,648 up-to 2,147,483,647 | y-axis acceleration offset correction                                  |
+----------------------------------+------------------------------------+------------------------------------------------------------------------+
| accel_calibbias_z                | -2,147,483,648 up-to 2,147,483,647 | z-axis acceleration offset correction                                  |
+----------------------------------+------------------------------------+------------------------------------------------------------------------+
| anglvel_calibbias_x              | -2,147,483,648 up-to 2,147,483,647 | x-axis gyroscope offset correction                                     |
+----------------------------------+------------------------------------+------------------------------------------------------------------------+
| anglvel_calibbias_y              | -2,147,483,648 up-to 2,147,483,647 | y-axis gyroscope offset correction                                     |
+----------------------------------+------------------------------------+------------------------------------------------------------------------+
| anglvel_calibbias_z              | -2,147,483,648 up-to 2,147,483,647 | z-axis gyroscope offset correction                                     |
+----------------------------------+------------------------------------+------------------------------------------------------------------------+
| command_to_execute               | "software_reset"                   | trigger the selected command in the imu device                         |
|                                  | "flash_memory_test"                |                                                                        |
|                                  | "flash_memory_update"              |                                                                        |
|                                  | "sensor_self_test"                 |                                                                        |
|                                  | "factory_calibration_restore"      |                                                                        |
+----------------------------------+------------------------------------+------------------------------------------------------------------------+
| filter_low_pass_3db_frequency    | [10, 20, 40, 80, 164, 360, 720]    | filter low pass 3db frequency                                          |
+----------------------------------+------------------------------------+------------------------------------------------------------------------+
| internal_sensor_bandwidth        | 0 up-to 1                          | 0 for wide bandwidth                                                   |
|                                  |                                    | 1 for 370 Hz                                                           |
+----------------------------------+------------------------------------+------------------------------------------------------------------------+
| linear_acceleration_compensation | 0 up-to 1                          | 0 for disabling linear acceleration compensation                       |
|                                  |                                    | 1 for enabling linear acceleration compensation                        |
+----------------------------------+------------------------------------+------------------------------------------------------------------------+
| measured_data_topic_selection    | 0 up-to 3                          | 0 for publishing measured data on /accelgyrotempdata topic             |
|                                  |                                    | 1 for publishing measured data on /accelgyrotempdata topic             |
|                                  |                                    | 2 for publishing measured data on /imu topic                           |
|                                  |                                    | 3 for publishing measured data on /imufullmeasureddata topic (default) |
+----------------------------------+------------------------------------+------------------------------------------------------------------------+
| point_of_percussion_alignment    | 0 up-to 1                          | 0 for disabling point of percussion alignment                          |
|                                  |                                    | 1 for enabling point of percussion alignment                           |
+----------------------------------+------------------------------------+------------------------------------------------------------------------+
| sampling_frequency               | 1.0 up-to 2000.0                   | device sampling frequency                                              |
+----------------------------------+------------------------------------+------------------------------------------------------------------------+

ADIS1657X parameters
^^^^^^^^^^^^^^^^^^^^

+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| Parameter Name                              | Allowed Values                     | Parameter Description                                                  |
+=============================================+====================================+========================================================================+
| accel_calibbias_x                           | -2,147,483,648 up-to 2,147,483,647 | x-axis acceleration offset correction                                  |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| accel_calibbias_y                           | -2,147,483,648 up-to 2,147,483,647 | y-axis acceleration offset correction                                  |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| accel_calibbias_z                           | -2,147,483,648 up-to 2,147,483,647 | z-axis acceleration offset correction                                  |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| anglvel_calibbias_x                         | -2,147,483,648 up-to 2,147,483,647 | x-axis gyroscope offset correction                                     |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| anglvel_calibbias_y                         | -2,147,483,648 up-to 2,147,483,647 | y-axis gyroscope offset correction                                     |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| anglvel_calibbias_z                         | -2,147,483,648 up-to 2,147,483,647 | z-axis gyroscope offset correction                                     |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| bias_correction_time_base_control           | 0 up-to 12                         | time base control                                                      |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| command_to_execute                          | "software_reset"                   | trigger the selected command in the imu device                         |
|                                             | "flash_memory_test"                |                                                                        |
|                                             | "flash_memory_update"              |                                                                        |
|                                             | "sensor_self_test"                 |                                                                        |
|                                             | "factory_calibration_restore"      |                                                                        |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| filter_low_pass_3db_frequency               | [10, 20, 40, 80, 164, 360, 720]    | filter low pass 3db frequency                                          |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| internal_sensor_bandwidth                   | 0 up-to 1                          | 0 for wide bandwidth                                                   |
|                                             |                                    | 1 for 370 Hz                                                           |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| linear_acceleration_compensation            | 0 up-to 1                          | 0 for disabling linear acceleration compensation                       |
|                                             |                                    | 1 for enabling linear acceleration compensation                        |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| measured_data_topic_selection               | 0 up-to 3                          | 0 for publishing measured data on /accelgyrotempdata topic             |
|                                             |                                    | 1 for publishing measured data on /accelgyrotempdata topic             |
|                                             |                                    | 2 for publishing measured data on /imu topic                           |
|                                             |                                    | 3 for publishing measured data on /imufullmeasureddata topic (default) |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| point_of_percussion_alignment               | 0 up-to 1                          | 0 for disabling point of percussion alignment                          |
|                                             |                                    | 1 for enabling point of percussion alignment                           |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| sampling_frequency                          | 1.0 up-to 4000.0                   | device sampling frequency                                              |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| x_axis_accelerometer_bias_correction_enable | 0 up-to 1                          | 0 x-axis accelerometer bias correction disabled                        |
|                                             |                                    | 1 x-axis accelerometer bias correction enabled                         |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| y_axis_accelerometer_bias_correction_enable | 0 up-to 1                          | 0 y-axis accelerometer bias correction disabled                        |
|                                             |                                    | 1 y-axis accelerometer bias correction enabled                         |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| z_axis_accelerometer_bias_correction_enable | 0 up-to 1                          | 0 z-axis accelerometer bias correction disabled                        |
|                                             |                                    | 1 z-axis accelerometer bias correction enabled                         |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| x_axis_gyroscope_bias_correction_enable     | 0 up-to 1                          | 0 x-axis gyroscope bias correction disabled                            |
|                                             |                                    | 1 x-axis gyroscope bias correction enabled                             |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| y_axis_gyroscope_bias_correction_enable     | 0 up-to 1                          | 0 y-axis gyroscope bias correction disabled                            |
|                                             |                                    | 1 y-axis gyroscope bias correction enabled                             |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+
| z_axis_gyroscope_bias_correction_enable     | 0 up-to 1                          | 0 z-axis gyroscope bias correction disabled                            |
|                                             |                                    | 1 z-axis gyroscope bias correction enabled                             |
+---------------------------------------------+------------------------------------+------------------------------------------------------------------------+

ROS2 parameter commands examples with IMU-ROS2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To view the ROS2 parameters from the imu_ros2_node just run the command **ros2 param list /imu_ros2_node**. Examples are shown below:

ADIS1650X
"""""""""

::

   **ros2 param list /imu_ros2_node**
   accel_calibbias_x
   accel_calibbias_y
   accel_calibbias_z
   anglvel_calibbias_x
   anglvel_calibbias_y
   anglvel_calibbias_z
   command_to_execute
   filter_low_pass_3db_frequency
   internal_sensor_bandwidth
   linear_acceleration_compensation
   measured_data_topic_selection
   point_of_percussion_alignment
   sampling_frequency

ADIS1657X
"""""""""

::

   **ros2 param list /imu_ros2_node**
   accel_calibbias_x
   accel_calibbias_y
   accel_calibbias_z
   anglvel_calibbias_x
   anglvel_calibbias_y
   anglvel_calibbias_z
   bias_correction_time_base_control
   command_to_execute
   filter_low_pass_3db_frequency
   internal_sensor_bandwidth
   linear_acceleration_compensation
   measured_data_topic_selection
   point_of_percussion_alignment
   sampling_frequency
   x_axis_accelerometer_bias_correction_enable
   x_axis_gyroscope_bias_correction_enable
   y_axis_accelerometer_bias_correction_enable
   y_axis_gyroscope_bias_correction_enable
   z_axis_accelerometer_bias_correction_enable
   z_axis_gyroscope_bias_correction_enable

If you want to find out more information about a parameter **ros2 param describe /imu_ros2_node param_name** command can be used. Examples are shown below:

command_to_execute parameter description
""""""""""""""""""""""""""""""""""""""""

::

   ** ros2 param describe /imu_ros2_node command_to_execute**
   Parameter name: command_to_execute
     Type: string
     Description: command_to_execute values:
        software_reset: performs a software reset on the device 
        flash_memory_test: performs a flash memory test on the device 
        flash_memory_update: performs a flash memory update on the device 
        sensor_self_test: performs a sensor self test on the device 
        factory_calibration_restore: performs a factory calibration restore on the device
        bias_correction_update: triggers a bias correction, using the bias correction factors
     Constraints:

measured_data_topic_selection parameter description
"""""""""""""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node measured_data_topic_selection**
   Parameter name: measured_data_topic_selection
     Type: integer
     Description: measured_data_topic_selection values:
        0: measured data is published on /accelgyrotempdata topic 
        1: measured data is published on /velangtempdata topic 
        2: measured data is published on /imu topic 
        3: measured data is published on /imufullmeasureddata topic (default)
     Constraints:
       Min value: 0
       Max value: 3
       Step: 1

anglvel_calibbias_x parameter description
"""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node anglvel_calibbias_x**
   Parameter name: anglvel_calibbias_x
     Type: integer
     Description: x-axis acceleration offset correction
     Constraints:
       Min value: -2147483648
       Max value: 2147483647
       Step: 1

anglvel_calibbias_y parameter description
"""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node anglvel_calibbias_y**
   Parameter name: anglvel_calibbias_y
     Type: integer
     Description: y-axis acceleration offset correction
     Constraints:
       Min value: -2147483648
       Max value: 2147483647
       Step: 1

anglvel_calibbias_z parameter description
"""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node anglvel_calibbias_z**
   Parameter name: anglvel_calibbias_z
     Type: integer
     Description: z-axis acceleration offset correction
     Constraints:
       Min value: -2147483648
       Max value: 2147483647
       Step: 1

accel_calibbias_x parameter description
"""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node accel_calibbias_x**
   Parameter name: accel_calibbias_x
     Type: integer
     Description: x-axis acceleration offset correction
     Constraints:
       Min value: -2147483648
       Max value: 2147483647
       Step: 1

accel_calibbias_y parameter description
"""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node accel_calibbias_y**
   Parameter name: accel_calibbias_y
     Type: integer
     Description: y-axis acceleration offset correction
     Constraints:
       Min value: -2147483648
       Max value: 2147483647
       Step: 1

accel_calibbias_z parameter description
"""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node accel_calibbias_z**
   Parameter name: accel_calibbias_z
     Type: integer
     Description: z-axis acceleration offset correction
     Constraints:
       Min value: -2147483648
       Max value: 2147483647
       Step: 1

filter_low_pass_3db_frequency parameter description
"""""""""""""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node filter_low_pass_3db_frequency**
   Parameter name: filter_low_pass_3db_frequency
     Type: integer
     Description: Low pass 3db frequency
     Constraints:
       Min value: 0
       Max value: 720
       Step: 1

internal_sensor_bandwidth parameter description
"""""""""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node internal_sensor_bandwidth**
   Parameter name: internal_sensor_bandwidth
     Type: integer
     Description: 0 for wide bandwidth  
          1 for 370 Hz
     Constraints:
       Min value: 0
       Max value: 1
       Step: 1

point_of_percussion_alignment parameter description
"""""""""""""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node point_of_percussion_alignment**
   Parameter name: point_of_percussion_alignment
     Type: integer
     Description: 0 for disabling point of percussion alignment  
          1 for enabling point of percussion alignment
     Constraints:
       Min value: 0
       Max value: 1
       Step: 1

linear_acceleration_compensation parameter description
""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node linear_acceleration_compensation**
   Parameter name: linear_acceleration_compensation
     Type: integer
     Description: 0 for disabling linear acceleration compensation  
          1 for enabling linear acceleration compensation
     Constraints:
       Min value: 0
       Max value: 1
       Step: 1

sampling_frequency parameter description
""""""""""""""""""""""""""""""""""""""""

ADIS1650X

::

   **ros2 param describe /imu_ros2_node sampling_frequency**
   Parameter name: sampling_frequency
     Type: double
     Description: Device sampling frequency
     Constraints:
       Min value: 1.0
       Max value: 2000.0
       Step: 0.1

ADIS1657X

::

   **ros2 param describe /imu_ros2_node sampling_frequency**
   Parameter name: sampling_frequency
     Type: double
     Description: Device sampling frequency
     Constraints:
       Min value: 1.0
       Max value: 4000.0
       Step: 0.1

bias_correction_time_base_control parameter description only for ADIS1657X
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node bias_correction_time_base_control**
   Parameter name: bias_correction_time_base_control
     Type: integer
     Description: Time base control
     Constraints:
       Min value: 0
       Max value: 12
       Step: 1

x_axis_gyroscope_bias_correction_enable parameter description only for ADIS1657X
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node x_axis_gyroscope_bias_correction_enable**
   Parameter name: x_axis_gyroscope_bias_correction_enable
     Type: integer
     Description: 0 x-axis gyroscope bias correction disabled  
          1 x-axis gyroscope bias correction enabled
     Constraints:
       Min value: 0
       Max value: 1
       Step: 1

y_axis_gyroscope_bias_correction_enable parameter description only for ADIS1657X
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node y_axis_accelerometer_bias_correction_enable**
   Parameter name: y_axis_accelerometer_bias_correction_enable
     Type: integer
     Description: 0 y-axis accelerometer bias correction disabled  
          1 y-axis accelerometer bias correction enabled
     Constraints:
       Min value: 0
       Max value: 1
       Step: 1

z_axis_gyroscope_bias_correction_enable parameter description only for ADIS1657X
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node z_axis_accelerometer_bias_correction_enable**
   Parameter name: z_axis_accelerometer_bias_correction_enable
     Type: integer
     Description: 0 z-axis accelerometer bias correction disabled  
          1 z-axis accelerometer bias correction enabled
     Constraints:
       Min value: 0
       Max value: 1
       Step: 1

x_axis_accelerometer_bias_correction_enable parameter description only for ADIS1657X
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node x_axis_accelerometer_bias_correction_enable**
   Parameter name: x_axis_accelerometer_bias_correction_enable
     Type: integer
     Description: 0 x-axis accelerometer bias correction disabled 
           1 x-axis accelerometer bias correction enabled
     Constraints:
       Min value: 0
       Max value: 1
       Step: 1

y_axis_accelerometer_bias_correction_enable parameter description only for ADIS1657X
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node y_axis_gyroscope_bias_correction_enable**
   Parameter name: y_axis_gyroscope_bias_correction_enable
     Type: integer
     Description: 0 y-axis gyroscope bias correction disabled  
          1 y-axis gyroscope bias correction enabled
     Constraints:
       Min value: 0
       Max value: 1
       Step: 1

z_axis_accelerometer_bias_correction_enable parameter description only for ADIS1657X
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

   **ros2 param describe /imu_ros2_node z_axis_gyroscope_bias_correction_enable**
   Parameter name: z_axis_gyroscope_bias_correction_enable
     Type: integer
     Description: 0 z-axis gyroscope bias correction disabled  
          1 z-axis gyroscope bias correction enabled
     Constraints:
       Min value: 0
       Max value: 1
       Step: 1

If you want to view the value of a parameter, use the **ros2 param get /imu_ros2_node parameter_name** command. An example is shown below:

::

   **ros2 param get /imu_ros2_node sampling_frequency**
   Double value is: 2000.0

If you want to view the value of a parameter, use the **ros2 param get /imu_ros2_node parameter_name** command. An example is shown below:

::

   **ros2 param set /imu_ros2_node sampling_frequency 1000.0**
   Set parameter successful

You can load all ROS2 parameter in imu_ros2_node from file located in config folder by using **ros2 param load /imu_ros2_node config_file.yaml**. An example is shown below:

::

   **ros2 param load /imu_ros2_node src/imu-ros2/config/imu1657x_config.yaml** 
   Set parameter accel_calibbias_x successful
   Set parameter accel_calibbias_y successful
   Set parameter accel_calibbias_z successful
   Set parameter anglvel_calibbias_x successful
   Set parameter anglvel_calibbias_y successful
   Set parameter anglvel_calibbias_z successful
   Set parameter filter_low_pass_3db_frequency successful
   Set parameter internal_sensor_bandwidth successful
   Set parameter point_of_percussion_alignment successful
   Set parameter linear_acceleration_compensation successful
   Set parameter bias_correction_time_base_control successful
   Set parameter x_axis_gyroscope_bias_correction_enable successful
   Set parameter y_axis_gyroscope_bias_correction_enable successful
   Set parameter z_axis_gyroscope_bias_correction_enable successful
   Set parameter x_axis_accelerometer_bias_correction_enable successful
   Set parameter y_axis_accelerometer_bias_correction_enable successful
   Set parameter z_axis_accelerometer_bias_correction_enable successful
   Set parameter sampling_frequency successful
   Set parameter command_to_execute successful
   Set parameter measured_data_topic_selection successful

You can also read all ROS2 parameter in imu_ros2_node by using **ros2 param dump /imu_ros2_node**. An example is shown below:

::

   **ros2 param dump /imu_ros2_node**
   Saving to:  ./imu_ros2_node.yaml
   **cat imu_ros2_node.yaml**
   /imu_ros2_node:
     ros__parameters:
       accel_calibbias_x: 0
       accel_calibbias_y: 0
       accel_calibbias_z: 0
       anglvel_calibbias_x: 0
       anglvel_calibbias_y: 0
       anglvel_calibbias_z: 0
       bias_correction_time_base_control: 10
       command_to_execute: no_command
       filter_low_pass_3db_frequency: 720
       internal_sensor_bandwidth: 0
       linear_acceleration_compensation: 1
       measured_data_topic_selection: 3
       point_of_percussion_alignment: 1
       sampling_frequency: 4000.0
       use_sim_time: false
       x_axis_accelerometer_bias_correction_enable: 0
       x_axis_gyroscope_bias_correction_enable: 1
       y_axis_accelerometer_bias_correction_enable: 0
       y_axis_gyroscope_bias_correction_enable: 1
       z_axis_accelerometer_bias_correction_enable: 0
       z_axis_gyroscope_bias_correction_enable: 1

imu-ros2 software development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Building on PC
^^^^^^^^^^^^^^

Prerequisites: imu-ros2 can be used with ROS2 humble distribution. To install humble distribution you can fallow the next tutorial: https://docs.ros.org/en/humble/Installation.html

imu-ros2 is using LibIIO. To instal the latest version of LibIIO follow the steps described here: :doc:`libiio </wiki-migration/resources/tools-software/linux-software/libiio>`

Source code: The imu-ros2 project source code can be found on ADI GitHub: https://github.com/analogdevicesinc/imu-ros2

In order to be able to build imu-ros2 on your PC, follow the next steps:

-  Create a folder ros2_ws/src
-  Clone the imu-ros2 project into src folder.
-  Go to ros2_ws folder and open a terminal.
-  Type the following command in the terminal: **colcon build**

In order to be able to run the imu-ros2 project on you PC, follow the next steps:

-  Go to ros2_ws and open a terminal
-  Type the following command in the terminal: **source install/setup.sh**
-  Type the following command in the terminal: **ros2 run imu_ros2 imu_ros2_node**

In order to be able to run the imu-ros2 system tests on your PC, follow the next steps:

-  Go to ros2_ws and open a terminal
-  Type the following command in the terminal: **source install/setup.sh**
-  Type the following command in the terminal: **cd install/imu_ros2/lib/imu_ros2_test**
-  Type the following command in the terminal: **./imu_ros2_test_node**

Building on ADI ROS2 Kuiper
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ADIS ROS2 Kuiper image already comes with ROS2 Humble and LibIIO installed. The image can be used with RPI3 and RPI4 and offers support for a wide range of ADI products, including ADIS1650X and ADIS1657X products with ROS2 driver support.

In order to be able to build imu-ros2 on Kuiper, follow the next steps:

-  Open a terminal in the home directory and type the following command: **cd ros2_ws/src**
-  Type the following command in the terminal: **git clone** `imu-ros2 <https://github.com/analogdevicesinc/imu-ros2>`__
-  Go to ros2_ws folder and type the following command in the terminal: **colcon build --symlink-install --packages-skip-build-finished --packages-up-to imu_ros2**

In order to be able to run the imu-ros2 project on Kuiper, follow the next steps:

-  Open a terminal in the home directory and type the following command: **cd ros2_ws/src**
-  Type the following command in the terminal: **sudo su** and type-in the password
-  Type the following command in the terminal: **source install/setup.sh**
-  Type the following command in the terminal: **ros2 run imu_ros2 imu_ros2_node**

In order to be able to run the imu-ros2 system tests on your PC, follow the next steps:

-  Go to ros2_ws and open a terminal
-  Type the following command in the terminal: **source install/setup.sh**
-  Type the following command in the terminal: **cd install/imu_ros2/lib/imu_ros2_test**
-  Type the following command in the terminal: **./imu_ros2_test_node**

Running system test
~~~~~~~~~~~~~~~~~~~

.. code:: C

   cd ros2_ws/src

run commands:

.. code:: C

   source install/setup.sh

   cd install/imu_ros2/lib/imu_ros2_test

We have to run just a test at once because not all publishers write on topic and tests must wait for data to be publish on topic. In another terminal run the imu_ros2_node

To run a test just write in terminal:

.. code:: C

   ./imu_ros2_test_node --gtest_filter="AccelGyroTempSubscriberTest*"

This will run AccelGyroTempSubscriberTest. Example of output for test ImuFullMeasuredDataSubscriberTest

.. code:: C

   Note: Google Test filter = ImuFullMeasuredDataSubscriberTest*

   [==========] Running 1 test from 1 test suite.

   [----------] Global test environment set-up.

   [----------] 1 test from ImuFullMeasuredDataSubscriberTest

   [ RUN      ] ImuFullMeasuredDataSubscriberTest.test_imu_full_measured_data_publisher

   [INFO] [1689060992.445404833] [rclcpp_iiowrapper]: device name: adis16577-3

   [INFO] [1689060992.510431448] [rclcpp_test_imu_full_measured_data]:  acceleration: 0.049021 -0.013857 9.848952 and gyroscope: 0.022495 -0.002413 0.001495 

    delta_velocity: 0.000005 -0.000005 0.001210 delta_angle: 0.000100 -0.000138 -0.000022 and temperature: 19.800000

   [       OK ] ImuFullMeasuredDataSubscriberTest.test_imu_full_measured_data_publisher (83 ms)

   [----------] 1 test from ImuFullMeasuredDataSubscriberTest (83 ms total)



   [----------] Global test environment tear-down

   [==========] 1 test from 1 test suite ran. (84 ms total)

   [  PASSED  ] 1 test.

The available tests are: AccelGyroTempSubscriberTest, Imu1650xDiagSubscriberTest, Imu1657xDiagSubscriberTest, ImuFullMeasuredDataSubscriberTest, ImuIdentificationSubscriberTest, ImuSubscriberTest, VelAngTempSubscriberTest

Create doxygen documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For creating the documentation go to folder imu-ros2 and create a folder with name doc. Open a terminal in this folder and execute command:

.. code:: C

   doxygen Doxyfile

The documentation site is created in doc/doxygen/html folder. For view the documentation just open the html page with the name index.html.

Class description
~~~~~~~~~~~~~~~~~

imu-ros2 application has publishers that write data on topic.

For that a C++ class is created that read data from device and write data on topic.

Every RosPublisher classes has some key functions like init(), setMessageProvider(), run().

For example:

**AccelGyroTempRosPublisher** is a class that publishing acceleration, gyroscope and temperature.

This class initializes the ros Node class. It set message provider with a variable that is a type of AccelGyroTempDataProviderInterface. It also run on thread reading from data provider and write on a ros2 publisher.

This class has some functions:

.. code:: C


   void init(Node)

This function initialize the class with a ros2 Node instance.

.. code:: C


   void setMessageProvider(AccelGyroTempDataProviderInterface * dataProvider)

This function set data message provider with a variable that inherit AccelGyroTempDataProviderInterface.

This interface has a method like getData that return by parameter imu_ros2::msg::AccelGyroTempData message that it will be published on a topic. AccelGyroTempDataProvider class that implement above interface has a member of type IIOWrapper for accessing data from device.

.. code:: C


   run()

Run on thread the reading from message provider and write on topic the data.

**Imu1650xDiagRosPublisher** is a class that publishing adis1650x diagnosis data.

This class initializes the ros Node class. It set message provider with a variable that is a type of Imu1650xDiagDataProviderInterface. It also run on thread reading from data provider and write on a ros2 publisher.

This class has some functions:

.. code:: C


   void init(Node)

This function initialize the class with a ros2 Node instance.

.. code:: C


   void setMessageProvider(Imu1650xDiagDataProviderInterface * dataProvider)

This function set data message provider with a variable that inherit Imu1650xDiagDataProviderInterface.

This interface has a method like getData that return by parameter imu_ros2::msg::Imu1650xDiagData message that it will be published on a topic. Imu1650xDiagDataProvider class that implement above interface has a member of type IIOWrapper for accessing data from device.

.. code:: C


   run()

Run on thread the reading from message provider and write on topic the data.

**Imu1657xDiagRosPublisher** is a class that publishing adis1657x diagnosis data.

This class initializes the ros Node class. It set message provider with a variable that is a type of Imu1657xDiagDataProviderInterface. It also run on thread reading from data provider and write on a ros2 publisher.

This class has some functions:

.. code:: C


   void init(Node)

This function initialize the class with a ros2 Node instance.

.. code:: C


   void setMessageProvider(Imu1657xDiagDataProviderInterface * dataProvider)

This function set data message provider with a variable that inherit Imu1657xDiagDataProviderInterface.

This interface has a method like getData that return by parameter imu_ros2::msg::Imu1657xDiagData message that it will be published on a topic. Imu1657xDiagDataProvider class that implement above interface has a member of type IIOWrapper for accessing data from device.

.. code:: C


   run()

Run on thread the reading from message provider and write on topic the data.

**ImuFullMeasuredDataRosPublisher** is a class that publishing acceleration, gyroscope, temperature, delta velocity and delta angle.

This class initializes the ros Node class. It set message provider with a variable that is a type of ImuFullMeasuredDataProviderInterface. It also run on thread reading from data provider and write on a ros2 publisher.

This class has some functions:

.. code:: C


   void init(Node)

This function initialize the class with a ros2 Node instance.

.. code:: C


   void setMessageProvider(ImuFullMeasuredDataProviderInterface * dataProvider)

This function set data message provider with a variable that inherit ImuFullMeasuredDataProviderInterface.

This interface has a method like getData that return by parameter imu_ros2::msg::ImuFullMeasuredData message that it will be published on a topic. ImuFullMeasuredDataProvider class that implement above interface has a member of type IIOWrapper for accessing data from device.

.. code:: C


   run()

Run on thread the reading from message provider and write on topic the data.

**ImuRosPublisher** is a class that publishing acceleration and gyroscope on a standard imu ros message.

This class initializes the ros Node class. It set message provider with a variable that is a type of ImuDataProviderInterface. It also run on thread reading from data provider and write on a ros2 publisher.

This class has some functions:

.. code:: C


   void init(Node)

This function initialize the class with a ros2 Node instance.

.. code:: C


   void setMessageProvider(ImuDataProviderInterface * dataProvider)

This function set data message provider with a variable that inherit ImuDataProviderInterface.

This interface has a method like getData that return by parameter sensor_msgs::msg::Imu message that it will be published on a topic. ImuDataProvider class that implement above interface has a member of type IIOWrapper for accessing data from device.

.. code:: C


   run()

Run on thread the reading from message provider and write on topic the data.

**ImuIdentificationRosPublisher** is a class that publishing product id, serial number.

This class initializes the ros Node class. It set message provider with a variable that is a type of ImuIdentificationDataProviderInterface. It also run on thread reading from data provider and write on a ros2 publisher.

This class has some functions:

.. code:: C


   void init(Node)

This function initialize the class with a ros2 Node instance.

.. code:: C


   void setMessageProvider(ImuIdentificationDataProviderInterface * dataProvider)

This function set data message provider with a variable that inherit ImuIdentificationDataProviderInterface.

This interface has a method like getData that return by parameter imu_ros2::msg::ImuIdentificationData message that it will be published on a topic. ImuIdentificationDataProvider class that implement above interface has a member of type IIOWrapper for accessing data from device.

.. code:: C


   run()

Run on thread the reading from message provider and write on topic the data.

**VelAngTempRosPublisher** is a class that publishing delta velocity, delta angle and temperature.

This class initializes the ros Node class. It set message provider with a variable that is a type of VelAngTempDataProviderInterface. It also run on thread reading from data provider and write on a ros2 publisher.

This class has some functions:

.. code:: C


   void init(Node)

This function initialize the class with a ros2 Node instance.

.. code:: C


   void setMessageProvider(VelAngTempDataProviderInterface * dataProvider)

This function set data message provider with a variable that inherit VelAngTempDataProviderInterface.

This interface has a method like getData that return by parameter imu_ros2::msg::VelAngTempData message that it will be published on a topic. VelAngTempDataProvider class that implement above interface has a member of type IIOWrapper for accessing data from device.

.. code:: C


   run()

Run on thread the reading from message provider and write on topic the data.

**IIOWrapper** class. This is a wrapper class for libiio library and offer functions for accesing iio capabilities.

**ImuControlParameters** class. This class modifies libiio parameters with ros2 parameters read from console. This class has a run method that read ros2 parameters and update with values in libiio. For example to modify the filter_low_pass_3db_frequency ros parameter just write in another terminal

.. code:: C


   ros2 param set imu_ros2_node filter_low_pass_3db_frequency 10

Examples
~~~~~~~~

adis1650x device console topic echo and rqt

Topic: imufullmeasureddata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_imufullmeasureddata.gif
   :align: left

.. raw:: html

   </details>


Topic: imuidentificationdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_imuidentificationdata.gif
   :align: left

.. raw:: html

   </details>


Topic: imu1650xdiagdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_imu1650xdiagdata.gif
   :align: left

.. raw:: html

   </details>


Topic: imu



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_imu.gif
   :align: left

.. raw:: html

   </details>


Topic: accelgyrotempdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_accel.gif
   :align: left

.. raw:: html

   </details>


Topic: velangtempdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_velang.gif
   :align: left

.. raw:: html

   </details>


Topic in rqt: velangtempdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_velang_rqt.gif
   :align: left

.. raw:: html

   </details>


Topic in rqt: accelgyrotempdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_accel_rqt.gif
   :align: left

.. raw:: html

   </details>


Topic in rqt: imu



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_imu_rqt.gif
   :align: left

.. raw:: html

   </details>


Topic in rqt: imu1650xdiagdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_rqt_imu1650xdiagdata.gif
   :align: left

.. raw:: html

   </details>


Topic in rqt: imuidentificationdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_rqt_imuidentificationdata.gif
   :align: left

.. raw:: html

   </details>


Topic in rqt: imufullmeasureddata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_rqt_imufullmeasureddata.gif
   :align: left

.. raw:: html

   </details>


adis1657x device console topic echo and rqt

Topic: accelgyrotempdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_accel_77.gif
   :align: left

.. raw:: html

   </details>


Topic: imu



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_imu_std_77.gif
   :align: left

.. raw:: html

   </details>


Topic: imu1657xdiagdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_imudiagdata_77.gif
   :align: left

.. raw:: html

   </details>


Topic: imufullmeasureddata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_imufullmeasureddata_77.gif
   :align: left

.. raw:: html

   </details>


Topic: imuidentificationdada



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_imuidentificationdata_77.gif

.. raw:: html

   </details>


Topic: velangtempdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_velang_77.gif
   :align: left

.. raw:: html

   </details>


Topic in rqt: velangtempdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_velang_rqt_77.gif
   :align: left

.. raw:: html

   </details>


Topic in rqt: imuidentificationdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_imuidentificationdata_rqt_77.gif
   :align: left

.. raw:: html

   </details>


Topic in rqt: imufullmeasureddata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_imufullmeasureddata_rqt_77.gif
   :align: left

.. raw:: html

   </details>


Topic in rqt: imu1657xdiagdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_diag_77_rqt.gif
   :align: left

.. raw:: html

   </details>


Topic in rqt: imu



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_imu_std_rqt_77.gif
   :align: left

.. raw:: html

   </details>


Topic in rqt: accelgyrotempdata



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/peek_accel_rqt_77.gif
   :align: left

.. raw:: html

   </details>


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/ros_architecture.png
