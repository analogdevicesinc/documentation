ADXRS450 Gyro Board for FIRST Robotics
======================================

| The :adi:`ADXRS450` gyro board is a single-axis industrial sensor, designed to get teams up and running quickly without having to load 3rd-party libraries. This gyro is readily accessible through FIRST Choice and is recommended for all teams, including those with no gyro experience. It plugs directly into the SPI port on the RoboRIO and libraries are already included in WPILib - all you have to do is declare it in your robot code and use it!
| Supporting code for the :adi:`ADXRS450` is only available for programming languages supported by FIRST. If your team wants to use this board on other platforms or with other programming languages, please refer to the :adi:`ADXRS450` product datasheet for more information on how to communicate with this gyro.
| If you're looking for information on other ADI donation resources, `click here <https://wiki.analog.com/first/first_robotics_donation_resources>`_ to go back to the main page.
| ===== Getting Started ===== There are currently three versions of the FRC Gyro board. The libraries detailed on this page apply to all of these versions, however there are some considerations to take into account for each one.
| |image1|\ ==== FRC Accelerometer & Gyroscope (Rev. A) ==== This version was made available to FRC teams through the 2016 FRC season. It includes both the :adi:`ADXRS450` gyroscope and the :adi:`ADXL362` accelerometer. Both sensors on this board continue to be supported by WPILib, so the accelerometer library can be used to read acceleration data just like the gyro library is used to read rotation rate.
| |image2|\ ==== FRC Gyro with Chip Select Jumper (Rev. B) ==== This version of the gyro board was available for the 2017 and 2018 FRC seasons. The accelerometer was removed in favor of a jumper that allows you to configure the Chip Select (CS) pin used to communicate with the sensor. This change allowed users to have other sensors (or SPI peripherals) on the bus without the gyro interfering. To use the libraries built into WPILib without any changes, the jumper should be installed as shown in the image to the left. If you want to use a different setting, you will need to change the Chip Select (CS) pin address in your robot code. The sections below detail how to do this for each of the three supported languages.
| ==== FRC Gyro With Solderable Jumpers (Rev. C) ==== This is the lower-cost, more robust version of the sensor board made available to teams for the 2019 FRC season. To make using the sensor even easier for teams, we removed the chip select pin jumpers and added a solderable jumper. This change improves reliability as there is no risk of the jumper accidentally getting lost or removed, but still allows teams the flexibility of adding additional devices to the SPI bus.
| ===== A Note on Offset Calibration ===== To help the robot minimize start-up drift and improve overall sensor performance, an offset calibration function has been built into the gyro driver. This function captures several seconds worth of data and calculates an average offset which is then applied to the sensor output. By default, calibration is automatically started once the RoboRIO begins executing user code and usually takes about 10 seconds to complete.
|

.. important::

   The gyro used in the :adi:`ADXRS450` measures *angular rate*, not *angle!* Any movement during the offset calibration routine **will** introduce some error into **every** sensor measurement! Over time, this error, will appear as "drift" in your angle measurement. **It is VERY important that the robot remains completely stationary during this calibration period!**\


|

.. tip::

   Offset calibration should be performed as soon as the robot is powered on to prevent the routine from interfering with any autonomous code execution. If your gyro angle readings are drifting drastically, clicking **Restart Robot Code** in the driver station will force the RoboRIO to re-execute the offset calibration routine. This should fix any drift issues caused by a bad offset measurement.


| ===== Using the Gyro on Your Robot ===== |image3|\ The figure to the right illustrates the direction of rotation which will generate a positive response from the ADXRS450 gyroscope.
| For more information on how to add gyro functionality to your robot code, select your team's programming language from the list below.
| :doc:`Using the Gyro in LabVIEW </wiki-migration/first/adxrs450_gyro_board_frc/labview>`
| :doc:`Using the Gyro C++ </wiki-migration/first/adxrs450_gyro_board_frc/cpp>`
| :doc:`Using the Gyro in Java </wiki-migration/first/adxrs450_gyro_board_frc/java>`

.. |image1| image:: https://wiki.analog.com/_media/first/gyroaccel.jpg
.. |image2| image:: https://wiki.analog.com/_media/first/am-3555-2.jpg
   :width: 150px
.. |image3| image:: https://wiki.analog.com/_media/first/adxrs450_rotation_figure.jpg
