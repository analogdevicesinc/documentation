Using the ADIS16470 IMU in LabVIEW
==================================

| This guide will walk you through the various features of the ADI-Supplied library for the ADIS16470 and how to use it in your LabVIEW robot code. If you're looking for a guide in another language, :doc:`click here </wiki-migration/first/adis16470_imu_frc/java>` for Java or :doc:`here </wiki-migration/first/adis16470_imu_frc/cpp>` for C++.
| If you need help getting started with the basics of programming your robot in LabVIEW, you may want to check out the WPI Screensteps documentation, which can be found `here <https://docs.wpilib.org/en/latest/docs/software/labview/resources/labview-resources.html>`__.
| ===== Installing the Library ===== First you need to install the library so that you can use the IMU in your code. You can find the library on GitHub `here <https://github.com/juchong/ADIS16470-RoboRIO-Driver/tree/master/LabVIEW>`__. New for 2020, the ADIS16470 LabVIEW libraries can only be installed via the NI Package Manager.
| This library assumes you have a working 2019 LabVIEW Professional installation and 2020.b4 or greater FRC software package already installed on your system. The latest package installer can be found `here <https://github.com/juchong/ADIS16470-RoboRIO-Driver/releases>`__.
| Once downloaded, double-click on the .nipkg file. The pre-installed NI Package Manager utility will extract the necessary files into the correct folders within your LabVIEW installation. Future updates to the library can be installed over previous installations. **LabVIEW must be closed completely before installing the library package!**
| |image1|
| Once you double-click on the installer file, the NI Package Manager will walk you through installing the library. Click Next at the window shown below to install the library.
|

.. note::

   The library version shown in the screenshots on this page may be different than the latest version available on the GitHub page!


| |image2|
| The package manager window should like like below if the library was properly installed.
| |image3|
| ===== Setting Up the IMU in Begin.vi ===== Open your robot project, or create a new one if you don't have one created already, and open up your Begin.vi block diagram. This can be found in the project window under Team Code. All VIs for the ADIS16470 library can be found in the pallet shown below.
| |image4|
| The first step is to create a new instance of the IMU. Bring the Open VI into your Begin.vi code. You can optionally specify a custom calibration time as shown below, but the default is 4 seconds if you don't define it. Remember, it's vital that the robot remains **completely stationary** during this calibration time!
| Now you need to assign a reference name to this IMU so that you can refer to it in other VIs. Grab the Registry Set VI from the ADIS16470 IMU palette and place to the right of your Open VI. Then, connect the ADI IMU DevRef Out pin on the Open VI to the ADI IMU DevRef pin on the Registry Set VI.
| Now you need to assign a name to your IMU. Right click on the "refnum name" pin on the Registry Set VI and click "Create --> Constant" and create a unique name that you will use to refer to this IMU in the rest of your code. I've named mine "MyIMU" but you can change this to whatever you want. When you're done, your IMU blocks in Begin.VI should look like this.
| |image5|
| ===== Using the IMU in Your Robot Code ===== |image6|\ You may want to use the IMU output to accurately track your robot's direction of travel so that you drive straight, or rotate to the right angle. For this kind of action, you will use the Read VI. Read counts continuously, so when you've completed a full rotation, it will continue to increase above 360 degrees rather than starting over at zero.
| |image7|\ If you want to report the current status of the IMU, you can use the Status VI. This will report whether the RoboRIO was able to find the IMU and whether or not it has finished the startup calibration. We will look at an example of how to use this and the Read VIs later.
| |image8|\ Sometimes it may be necessary to reset the IMU's "zero degrees" position. All IMUs will have some amount of drift over time and it's physically impossible to calibrate out all sources of drift. In this case, you can use the Reset VI to reset the current IMU heading to 0 degrees. When doing this, your robot should be facing the direction you want zero degrees to be, particularly if you are driving with field-oriented drive using an omnidirectional drive base. Otherwise, your robot may begin to behave incorrectly. For this reason, you should never automate this routine. Note that this **does not** recalibrate the IMU, so you don't have to be sitting still to perform this method properly.
| |image9|\ On rare occasions, you may want to perform an on-the-fly recalibration of the sensor. **This should never be run after the robot has started moving!** You can use this function if, for example, your robot was moving during the initial calibration. This function will use the currently accumulated readings internal to the sensor as the new offset calibration values and zero the IMU.

Driver Station Example
----------------------

| As an example, let's publish the IMU's angle readings and status to the driver station. We will do this in the Periodic Tasks VI.
| To use any IMU VI, you first have to call the IMU you initialized in Begin.VI. Place an instance of Registry Get inside the 100ms loop and create the constant for your IMU name. **Don't forget to change the constant value to whatever you called your IMU in Begin.vi!** Then, place an instance of the Read VI next to it, and connect the two VIs together
| Now, go to your Dashboard pallet in the WPI Robotics Library and grab the NT Write Value VI and place two of them next to your Read and Status VIs. Note that when you first place this VI in your code, it will show as expecting a Boolean. This VI can actually automatically detect which data type you are feeding it and adjust accordingly. You can also use the drop-down menu below the VI icon and explicitly specify what data type you want it to expect, but it is usually best to leave it set to Automatic. Connect the ADIS1647 Value pin on the Read VI to the Boolean pin on the driver station VI you just placed. You will see that the icon will change to indicate what kind of data you are sending, which in this case is a Variant. Do the same for the ADIS16470 Status pin on the Status VI. Right click on the Name pins for each NT Write Value VI and select Create --> Constant and write a name for each of the indicators that will appear on the Driver Station.
| |image10|

.. |image1| image:: https://raw.githubusercontent.com/juchong/ADIS16470-RoboRIO-Driver/master/docs/nipkg_icon.PNG
.. |image2| image:: https://raw.githubusercontent.com/juchong/ADIS16470-RoboRIO-Driver/master/docs/installing.PNG
.. |image3| image:: https://raw.githubusercontent.com/juchong/ADIS16470-RoboRIO-Driver/master/docs/installed.PNG
.. |image4| image:: https://raw.githubusercontent.com/juchong/ADIS16470-RoboRIO-Driver/master/docs/menu.PNG
.. |image5| image:: https://wiki.analog.com/_media/first/adis16470_imu_frc/470tutoriallabviewopen.png
.. |image6| image:: https://wiki.analog.com/_media/first/adis16470_imu_frc/470tutoriallabviewread.png
.. |image7| image:: https://wiki.analog.com/_media/first/adis16470_imu_frc/470labviewstatus.png
.. |image8| image:: https://wiki.analog.com/_media/first/adis16470_imu_frc/470resetlabview.png
.. |image9| image:: https://wiki.analog.com/_media/first/adis16470_imu_frc/470recal.png
.. |image10| image:: https://wiki.analog.com/_media/first/adis16470_imu_frc/470anglesstatusexamplelabview.png
