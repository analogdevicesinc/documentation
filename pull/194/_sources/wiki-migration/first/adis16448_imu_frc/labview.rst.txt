.. important::

   After 2020, we will begin to phase out the ADIS16448 IMU in favor of the newer ADIS16470 with updated features. We strongly encourage teams that have not obtained one of the newer IMUs to consider getting one from FIRST Choice this year. The ADIS16448 IMU is still supported, but stock will be limited and library updates/releases for this device will be slower.


Using the ADIS16448 IMU in LabVIEW
==================================

| This guide will walk you through the various features of the ADI-Supplied library for the ADIS16448 and how to use it in your LabVIEW robot code. If you're looking for a guide in another language, :doc:`click here </wiki-migration/first/adis16448_imu_frc/java>` for Java or :doc:`here </wiki-migration/first/adis16448_imu_frc/cpp>` for C++.
| If you need help getting started with the basics of programming your robot in LabVIEW, you may want to check out the WPI Screensteps documentation, which can be found `here <https://wpilib.screenstepslive.com/s/currentCS/m/labview>`_.
| ===== Installing the Library ===== First you need to install the library so that you can use the IMU in your code. You can find the library on GitHub `here <https://github.com/juchong/ADIS16448-RoboRIO-Driver/tree/master/LabVIEW>`_. You have two options for installing the library.
| ==== Self-Extracting Installer ==== The installer can be found `here on the releases page for the library <https://github.com/juchong/ADIS16448-RoboRIO-Driver/releases>`_. Run the installer as administrator and the installer will automatically extract the files to the right location. If it installed right, the VIs for the IMU board will be found under WPI Robotics Library --> Sensors --> Third Party Sensors --> ADIS16448 IMU.
| |image1| |image2| |image3|
| ==== Manual Installation ==== If you want to do your installation manually, `you can find the folder on GitHub <https://github.com/juchong/ADIS16448-RoboRIO-Driver/tree/master/LabVIEW>`_. Copy the ADIS16448 IMU folder into your Robot Project folder, then drag it from there onto the project explorer in LabVIEW. If you've done this correctly, the library will appear in your project like this.
| |image4|
| ===== Setting Up the IMU in Begin.vi ===== Open your robot project, or create a new one if you don't have one created already, and open up your Begin.vi block diagram. This can be found in the project window under Team Code.
| The first step is to create a new instance of the IMU, then assign a reference name to it so that you can call the gyro reference anywhere in your robot code. Bring the Open VI into your Begin.vi code. It doesn't matter where you place it in this VI.
| |image5|
| Now you need to assign a reference name to this IMU so that you can refer to it in other VIs. Grab the Registry Set VI from the ADIS16448 IMU palette and place to the right of your Open VI. Then, connect the ADI IMU DevRef Out pin on the Open VI to the ADI IMU DevRef pin on the Registry Set VI.
| |image6|
| Now you need to assign a name to your IMU. Right click on the "refnum name" pin on the Registry Set VI and click "Create --> Constant" and create a unique name that you will use to refer to this IMU in the rest of your code. I've named mine "MyIMU" but you can change this to whatever you want.
| |image7|
| You will also need to set whether the IMU will calibrate upon opening. Right click on the Calibrate On Open pin on the Open VI and click Create Constant. **Leave this at the default TRUE value!** Failing to do this may cause undesired operation of your IMU!
| |image8|
| While it isn't necessary, it's good practice to create constants for the Yaw Axis and Algorithm pins. **Do not change these values!** While this library is capable of AHRS, FRC teams will obtain better performance by not using it.
| |image9|
| ===== Closing Communication in Finish.vi ===== Whenever you open a communication bus in your robot code, you have to close those communications when your robot code finishes, just like you have to close all of the programs running on a computer before you can shut it down properly. This is done in the Finish.vi code. Open your robot project and open up the Finish.vi block diagram. Then, place an instance of the Registry Get VI on the outside of the Flat Sequence Structure (the film strip boxes), and an instance of the Close VI on the inside of the first panel of the Flat Sequence Structure.
| |image10|
| Then, connect the ADI IMU DevRef pins of both VIs together.
| |image11|
| Now, create a string constant by right-clicking on the Gyro RefName pin on the Registry Get VI and clicking Create --> Constant. Rename this string to be the same name you used when instantiating the gyro in your Begin.vi code. This way your robot knows what you are trying to close. You're now ready to call data from the gyro!
| |image12|
| ===== Using the IMU in Your Robot Code ===== |image13|\ There are several use-cases for using the IMU output in your code. You may want to use the IMU output to accurately track your robot's direction of travel so that you drive straight, or rotate to the right angle. This offers you more precision than simply telling the motors to drive together at the same rate to move forward. For this kind of action, you will use the Get Angles VI. Get Angles counts continuously, so when you've completed a full rotation, it will continue to increase above 360 degrees rather than starting over.
| |image14|\ Sometimes it may be necessary to reset the IMU's "zero degrees" position. All IMUs will have some amount of drift over time and it's physically impossible to calibrate out all sources of drift. In this case, you can use the Reset VI to reset the current IMU heading to 0 degrees. When doing this, your robot should be facing the direction you want zero degrees to be, particularly if you are driving with field-oriented drive using an omnidirectional drive base. Otherwise, your robot may begin to behave incorrectly. For this reason, you should never automate this routine. Note that this **does not** recalibrate the IMU, so you don't have to be sitting still to perform this method properly.
| ===== Driver Station Example ===== As an example, let's publish the IMU's angle readings to the driver station. We will do this in the Periodic Tasks VI.
| To use any IMU VI, you first have to call the IMU you initialized in Begin.VI. You saw this when we completed our IMU setup in Finish.vi. Go ahead and place an instance of Registry Get inside the 100ms loop and create the constant for your IMU name. **Don't forget to change the constant value to whatever you called your IMU in Begin.vi!**
| |image15|
| Now, place an instance of the Get Angles VI next to it, and wire it up as shown below, just like you did for Close in your Finish.vi block diagram.
| |image16|
| Now, go to your Dashboard pallet in the WPI Robotics Library and grab the NT Write Value VI and place it next to your Get Angle VI. Note that when you first place this VI in your code, it will show as expecting a Boolean. This VI can actually automatically detect which data type you are feeding it and adjust accordingly. You can also use the drop-down menu below the VI icon and explicitly specify what data type you want it to expect, but it is usually best to leave it set to Automatic. Connect the Angles pin on the Get Angles VI to the Boolean pin on the driver station VI you just placed. You will see that the icon will change to indicate what kind of data you are sending, which in this case is a Variant. Right click on the Name pin and select Create --> Constant and write a name for the indicator that will appear on the Driver Station.
| |image17|
| |image18|
| |image19|

.. |image1| image:: https://wiki.analog.com/_media/first/beginvifindinggyrostep1.png
.. |image2| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_thirdparty.png
.. |image3| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_libfolder.png
.. |image4| image:: https://raw.githubusercontent.com/juchong/ADIS16448-RoboRIO-Driver/master/Reference/RobotProject.PNG
.. |image5| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_open.png
.. |image6| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_devref.png
.. |image7| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_nameassign.png
.. |image8| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_caltrue.png
.. |image9| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_otherconstants.png
.. |image10| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_finishvis.png
.. |image11| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_finishconnect.png
.. |image12| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_finishref.png
.. |image13| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_getangles.png
.. |image14| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_reset.png
.. |image15| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_examplerefget.png
.. |image16| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_examplegetangles.png
.. |image17| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_exampleconnect.png
.. |image18| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_exampleconfirm.png
.. |image19| image:: https://wiki.analog.com/_media/first/adis16448_imu_frc/448_examplefrontpanelname.png
