Using the ADXRS450 Gyro for FRC in LabVIEW
==========================================

| This guide will walk you through the various features of the WPI Library for the ADXRS450 FRC Gyro Board and how to use it in your LabVIEW robot code. If you're looking for a guide in another language, :doc:`click here </wiki-migration/first/adxrs450_gyro_board_frc/java>` for Java or :doc:`here </wiki-migration/first/adxrs450_gyro_board_frc/cpp>` for C++.
| If you need help getting started with the basics of programming your robot in LabVIEW, you may want to check out the WPI Screensteps documentation, which can be found `here <https://wpilib.screenstepslive.com/s/currentCS/m/labview>`_.
| As with any LabVIEW robot project, there are a few places you must place code in order to use the gyro board: Begin.vi, Finish.vi, and any .vi in which you want to access gyro data. The screenshots in this example assume you are starting from the Arcade robot project, but the steps are the same for any robot project.

Setting Up the Gyro in Begin.vi
-------------------------------

Open your robot project, or create a new one if you don't have one created already, and open up your Begin.vi block diagram. This can be found in the project window under Team Code.

| The first step is to create a new instance of the gyro, then assign a reference name to it so that you can call the gyro reference anywhere in your robot code. You can find the gyro VI under WPI Robotics Library --> Sensors --> Gyro. Bring the Gyro Open VI into your Begin.vi code. It doesn't matter where you place it in this VI.
| |image1| |image2| |image3|
| When you first bring the instance into your code, it will default to an analog gyro, so you will need to change the type using the drop-down menu below the VI's icon. Select "XRS450 SPI Open" to tell your robot that you're working with the ADXRS450 board.
| |image4|
| Next, you need to tell LabVIEW which SPI "chip select" (CS) it will be using. Right click on the "SPI Bus" pin on the Open VI and click "Create --> Constant" to insert an enumerated variable. LabVIEW will automatically assign the gyro to CS0, which is the default. **Unless you are using the CS Jumper version of the gyro and want to use C1 or C2 by moving the jumper, do not change this variable!**
| |image5|
| Now you need to assign a reference name to this gyro so that you can refer to it in other VIs. Grab the Registry Set VI from the Gyro palette and place to the right of your Open VI. Then, connect the GyroDevRef pin on the Open VI to the GyroDevRef on the Registry Set VI.
| |image6|
| |image7|
| Now you need to assign a name to your gyro. Right click on the "refnum name" pin on the Registry Set VI and click "Create --> Constant" and create a unique name that you will use to refer to this gyro in the rest of your code. I've left the default value of "My Gyro RefNum" but you can change this to whatever you want.
| |image8|
| |image9|
| ===== Closing Communication in Finish.vi ===== Whenever you open a communication bus in your robot code, you have to close those communications when your robot code finishes, just like you have to close all of the programs running on a computer before you can shut it down properly. This is done in the Finish.vi code. Open your robot project and open up the Finish.vi block diagram. Then, place an instance of the Registry Get VI on the outside of the Flat Sequence Structure (the film strip boxes), and an instance of Gyro Close VI on the inside of the first panel of the Flat Sequence Structure.
| |image10|
| |image11|
| Then, connect the GyroDevRef pins of both VIs together.
| |image12|
| Now, create a string constant by right clicking on the Gyro RefName pin on the Registry Get VI and clicking Create --> Constant. Rename this string to be the same name you used when instantiating the gyro in your Begin.vi code. I've left mine as the default, since that's what I used in my Begin.vi code. You're now ready to call data from the gyro!
| |image13|
| ===== Using the Gyro in Your Robot Code ===== |image14|\ There are several use-cases for using the gyro output in your code. You may want to use the gyro output to accurately track your robot's direction of travel so that you drive straight, or rotate to the right angle. This offers you more precision than simply telling the motors to drive together at the same rate to move forward. For this kind of action, you will use the Get Angle VI. Get Angle counts continuously, so when you've completed a full rotation, it will continue to increase above 360 degrees rather than starting over.
| |image15|\ Sometimes it may be necessary to reset the gyro's "zero degrees" position. All gyros will have some amount of drift over time and it's physically impossible to calibrate out all sources of drift. In this case, you can use the Reset VI to reset the current gyro heading to 0 degrees. When doing this, your robot should be facing the direction you want zero degrees to be, particularly if you are driving with field-oriented drive using an omnidirectional drive base. Otherwise, your robot may begin to behave incorrectly. For this reason, you should never automate this routine. Note that this **does not** recalibrate the gyro, so you don't have to be sitting still to perform this method properly.
|

.. note::

   In my example below, I'm going to be reporting the gyro angle to the driver station from the Teleop.vi. In practice, you should really put this type of action in the PeriodicTasks.vi, but this is just an example. These steps will apply to anywhere you want to use either of the VIs listed above.


| To use any Gyro VI, you first have to call the Gyro you initialized in Begin.VI. You saw this when we completed our gyro setup in Finish.vi. Go ahead and place an instance of Gyro Registry Get in your block diagram and create the constant for your gyro name. **Don't forget to change the constant value to whatever you called your gyro in Begin.vi!** I've left mine as the default, since that is what I used.
| |image16|
| Now, place an instance of the Get Angle VI next to it, and wire it up as shown below, just like you did for Gyro Close in your Finish.vi block diagram. Then, go to your Dashboard pallet in the WPI Robotics Library and grab the NT Write Value VI and place it next to your Get Angle VI. Note that when you first place this VI in your code, it will show as expecting a Boolean. This VI can actually automatically detect which data type you are feeding it and adjust accordingly. You can also use the drop-down menu below the VI icon and explicitly specify what data type you want it to expect, but it is usually best to leave it set to Automatic as shown below.
| |image17|
| Now, connect the Angle pin on the Get Angle VI to the Boolean pin on the driver station VI you just placed. You will see that the icon will change to indicate what kind of data you are sending, which in this case is a Double. Right click on the Name pin and select Create --> Constant and write a name for the indicator that will appear on the Driver Station.
| |image18|

.. |image1| image:: https://wiki.analog.com/_media/first/beginvifindinggyrostep1.png
.. |image2| image:: https://wiki.analog.com/_media/first/beginvifindinggyrostep2.png
.. |image3| image:: https://wiki.analog.com/_media/first/beginvifindinggyrostep3.png
.. |image4| image:: https://wiki.analog.com/_media/first/beginviplacegyro.png
.. |image5| image:: https://wiki.analog.com/_media/first/beginvicreatespiport.png
.. |image6| image:: https://wiki.analog.com/_media/first/beginviplacegyroref.png
.. |image7| image:: https://wiki.analog.com/_media/first/beginviconnectrefset.png
.. |image8| image:: https://wiki.analog.com/_media/first/beginvicreatestringname.png
.. |image9| image:: https://wiki.analog.com/_media/first/beginvidone.png
.. |image10| image:: https://wiki.analog.com/_media/first/finishviblocksneeded.png
.. |image11| image:: https://wiki.analog.com/_media/first/finishviblocksnplaced.png
.. |image12| image:: https://wiki.analog.com/_media/first/finishviblocksconnected.png
.. |image13| image:: https://wiki.analog.com/_media/first/finishvidone.png
.. |image14| image:: https://wiki.analog.com/_media/first/gyrogetanglevi.png
.. |image15| image:: https://wiki.analog.com/_media/first/gyroresetvi.png
.. |image16| image:: https://wiki.analog.com/_media/first/teleopviexamplegetrefnum.png
.. |image17| image:: https://wiki.analog.com/_media/first/teleopvidriverstationwrite.png
.. |image18| image:: https://wiki.analog.com/_media/first/teleopvidone.png
