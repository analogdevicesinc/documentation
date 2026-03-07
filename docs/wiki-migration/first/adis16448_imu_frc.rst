.. important::

   After 2020, we will begin to phase out the ADIS16448 IMU in favor of the newer ADIS16470 with updated features. We strongly encourage teams that have not obtained one of the newer IMUs to consider getting one from FIRST Choice this year. The ADIS16448 IMU is still supported, but stock will be limited and library updates/releases for this device will be slower.


ADIS16448 IMU Board for FIRST Robotics
======================================

| The :adi:`ADIS16448` IMU board is ADI's rugged, tactical IMU designed for use in a wide variety of applications, including industrial robots, smart agriculture, and autonomous vehicles. The :adi:`ADIS16448` is a 10 degree-of-freedom IMU, with 3-axis gyro, 3-axis accelerometer, 3-axis magnetometer, and a barometer.
| :adi:`ADIS16448` software and examples for Java, C+ +, and LabVIEW can be found `here <https://github.com/juchong/ADIS16448-RoboRIO-Driver>`_. If your team wants to use this board with other programming languages, please refer to the :adi:`ADIS16448` product datasheet for more information on how to communicate with this IMU via SPI.
| If you're looking for information on other ADI donation resources, `click here <https://wiki.analog.com/first/first_robotics_donation_resources>`_ to go back to the main page.
| ===== Getting Started ===== |image1|\ The :adi:`ADIS16448` IMU Board is designed to plug directly into the MXP port on the RoboRIO. Due to the size of typical FRC robots, AHRS calculations that rely on the magnetometer may be adversely affected by motors and metal objects close to the sensor. The IMU board has two mounting holes which should be used to secure it to the RoboRIO with #4-40 screws. The figure to the right illustrates the X, Y, and Z axis relative to the device package. Note that the IMU is installed on the board *upside down* compared to the image shown here.
| ===== A Note on Offset Calibration ===== To help the robot minimize start-up drift and improve overall sensor performance, an offset calibration function has been built into the IMU driver. This function captures several seconds worth of data and calculates an average offset which is then applied to the sensor outputs. By default, calibration is automatically started once the RoboRIO begins executing user code and usually takes about 10 seconds to complete. If your IMU board has a "Ready?" LED indicator, it will illuminate once calibration is complete.
|

.. important::

   The gyros used in the :adi:`ADIS16448` measure *angular rate*, not *angle!* Any movement during the offset calibration routine **will** introduce some error into **every** sensor measurement! Over time, this error, will appear as "drift" in your angle measurement. **It is VERY important that the robot remains completely stationary during this calibration period!**\


|

.. tip::

   Offset calibration should be performed as soon as the robot is powered on to prevent the routine from interfering with any autonomous code execution. If your gyro angle readings are drifting drastically, clicking **Restart Robot Code** in the driver station will force the RoboRIO to re-execute the offset calibration routine. This should fix any drift issues caused by a bad offset measurement.


| ===== Using the ADIS16448 IMU on Your Robot ===== For more information on how to add IMU functionality to your robot code, select your team's programming language from the list below.
| :doc:`Using the ADIS16448 IMU in LabVIEW </wiki-migration/first/adis16448_imu_frc/labview>`
| :doc:`Using the ADIS16448 IMU in C++ </wiki-migration/first/adis16448_imu_frc/cpp>`
| :doc:`Using the ADIS16448IMU in Java </wiki-migration/first/adis16448_imu_frc/java>`

.. |image1| image:: https://wiki.analog.com/_media/first/adis16448_rotation_figure.jpg
   :width: 400px
