.. warning::

   This page is still under construction for the 2020 season! Please check back here for more updates.


ADIS16470 IMU Board for FIRST Robotics
======================================

| The :adi:`ADIS16470` IMU board is ADI's rugged, tactical IMU designed for use in a wide variety of applications, including industrial robots, smart agriculture, and autonomous vehicles. The :adi:`ADIS16470` is a 6 degree-of-freedom IMU, with a 3-axis gyro and a 3-axis accelerometer.
| :adi:`ADIS16470` software and examples for Java, C+ +, and LabVIEW can be found `here <https://github.com/juchong/ADIS16470-RoboRIO-Driver>`_. If your team wants to use this board with other programming languages, please refer to the :adi:`ADIS16470` product datasheet for more information on how to communicate with this IMU via SPI.
| If you're looking for information on other ADI donation resources, `click here <https://wiki.analog.com/first/first_robotics_donation_resources>`_ to go back to the main page.
| |image1|

Getting Started
---------------

| The :adi:`ADIS16470` IMU Board is designed to plug directly into the SPI port on the RoboRIO. The IMU board has an extension with two mounting holes which should be used to secure it to the RoboRIO with #4-40 screws. The figure to the right illustrates the locations of the X, Y, and Z axes in relation to the device package.
| ===== A Note on Offset Calibration ===== To help the robot minimize start-up drift and improve overall sensor performance, an offset calibration function has been built into the IMU driver. This function captures several seconds worth of data and calculates an average offset which is then applied to the sensor outputs. By default, calibration is automatically started once the RoboRIO begins executing user code and usually takes about 10 seconds to complete. The "Ready?" LED indicator will also illuminate once calibration is complete. New in 2020, all three language libraries also have this functionality made available via the "Recalibrate" function.
|

.. important::

   The gyros used in the :adi:`ADIS16470` measure *angular rate*, not *angle!* Any movement during the offset calibration routine **will** introduce some error into **every** sensor measurement! Over time, this error, will appear as "drift" in your angle measurement. **It is VERY important that the robot remains completely stationary during this calibration period!**\


|

.. tip::

   Offset calibration should be performed as soon as the robot is powered on to prevent the routine from interfering with any autonomous code execution. If your gyro angle readings are drifting drastically, clicking **Restart Robot Code** in the driver station will force the RoboRIO to re-execute the offset calibration routine. This should fix any drift issues caused by a bad offset measurement. You can also use the new Recalibrate function available in the 2020 libraries to re-perform the offset calibration (if, for example, the robot was kicked or moved during start-up). This function will also perform a "reset," or re-zero the sensor, so be sure the robot is facing in the direction you want "zero" to be!


| ===== "Reset" vs. "Recalibrate" ===== As mentioned above, the 2020 versions of the libraries include a new function called "recalibrate" that takes advantage of features available on the ADIS16470. It's important to note the difference between "reset" and "recalibrate" as they are very different functions and have differing use cases!
| ==== Recalibrate ==== "Recalibrating" the IMU will reconfigure the offset calibration in the device. Upon startup, the libraries for the ADIS16470 will automatically perform an offset calibration as described above. It does this by taking readings for a few seconds (the default is 4 seconds) and averaging those values together to form an offset, one for each axis. This allows the IMU to calibrate out **some** drift to improve the sensor performance. We discussed above that any movement of the robot during this calibration period will negatively impact sensor performance. Before 2020, there was no function that would allow teams to recalibrate the IMU without restarting robot code. If the robot was bumped or moved during startup, IMU performance would be impaired. The ADIS16470 has an internal feature which continuously averages the internal sensor readings and stores them on the device. The device can be instructed to use these averages as the new internal offset values when a certain command is issued. This is what the new recalibrate function does.
|

.. important::

   The Recalibrate function should **never** be used during match play! Doing so may negatively affect sensor performance if the robot moves before Recalibrate is called, just as bumping the robot during the startup calibration will negatively affect sensor performance!


| ==== Reset ==== "Resetting" the IMU simply "re-zeros" the device. You may recall that gyros output data as degrees per second, not degrees,and we must integrate the readings from the device in order to determine a heading in degrees. When we reset the IMU, we are resetting this integration and starting back at zero. This means that the direction that the robot is facing when you reset the IMU will become the new zero degrees direction.
| ===== Using the ADIS16470 IMU on Your Robot ===== For more information on how to add IMU functionality to your robot code, select your team's programming language from the list below.
| :doc:`Using the ADIS16470 IMU in LabVIEW </wiki-migration/first/adis16470_imu_frc/labview>`
| :doc:`Using the ADIS16470 IMU in C++ </wiki-migration/first/adis16470_imu_frc/cpp>`
| :doc:`Using the ADIS16470IMU in Java </wiki-migration/first/adis16470_imu_frc/java>`

.. |image1| image:: https://wiki.analog.com/_media/first/adis16470_rotation_figure.jpg
   :width: 250px
