.. important::

   After 2020, we will begin to phase out the ADIS16448 IMU in favor of the newer ADIS16470 with updated features. We strongly encourage teams that have not obtained one of the newer IMUs to consider getting one from FIRST Choice this year. The ADIS16448 IMU is still supported, but stock will be limited and library updates/releases for this device will be slower.


Using the ADIS16448 IMU Board for FRC in C++
============================================

| This guide will walk you through the various features of the Analog Devices library for the ADIS16448 FRC IMU Board and how to use it in your robot code. If you're looking for a guide in another language, :doc:`click here </wiki-migration/first/adis16448_imu_frc/java>` for Java or :doc:`here </wiki-migration/first/adis16448_imu_frc/labview>` for LabVIEW.
| If you need help getting started with the basics of programming your robot in C++, you may want to check out the WPI Screensteps documentation, which can be found `here <https://wpilib.screenstepslive.com/s/currentCS/m/cpp>`__. Another useful resource can be found `here <https://media.readthedocs.org/pdf/frc-pdr/latest/frc-pdr.pdf>`__.
| ===== Installing the Library ===== In order to use the IMU, you will need to download and install the appropriate library from GitHub. There are two options for installing these libraries. The instructions below assume you are using VS Code, the official supported development environment for FRC.

Online Install
--------------

-  Open FRC Visual Studio Code
-  Click the WPILib command pallete icon
-  Select "Manage Vendor Libraries" in the menu
-  Choose "Install New Libraries (Online)"
-  Paste the following link: http://maven.highcurrent.io/vendordeps/ADIS16448.json

Offline Install
---------------

-  Download the latest release zip from `this page <https://github.com/juchong/ADIS16448-RoboRIO-Driver/releases>`__. The zip will be named adis16448_roborio-[releaseversion].zip.
-  Close all instances of FRC Visual Studio Code
-  If using Windows, extract the zip you downloaded to C:\\Users\\Public\\frc2019. If using Linux or Mac, extract the zip to ~/home/frc2019/.
-  Open FRC Visual Studio Code
-  Click the WPILib command pallete icon
-  Select "Manage Vendor Libraries" in the menu
-  Choose "Install New Libraries (Offline)"
-  Check ADIS16448, then click "OK".

| 
| ===== Instance Definition and Instantiation ===== Before you can use the gyro in your code, you must first define an instance. Where exactly it needs to be defined will depend heavily on how your team organizes its robot code, but it needs to be accessible by the Robot class in order to work properly and give you no build errors. If your team is using an Iterative Robot with a RobotMap structure for example, you would put it inside of the RobotMap class.
| Because the IMU plugs directly into the MXP port, the library will pre-define your SPI port for you. The IMU is a 3-axis sensor, so you will need to tell it which axis is the yaw axis. By default, this will be the Z axis if you don't define anything (with the RoboRIO and the sensor sitting flat on or in the robot, facing up). Don't worry about defining an algorithm argument, the library will take care of this for you. A typical definition and instantiation will look like this:

::

   frc::ADIS16448_IMU imu{};

| 
| ===== Sensor Initialization/Calibration with Calibrate() ===== The IMU library will perform a calibration for you in its constructor, since this calibration **MUST** be performed in order for the IMU to function properly. If you wish to re-calibrate at some point in your code, you can call the Calibrate() function. For more general information about offset calibration, please see the :doc:`general ADIS16448 IMU page </wiki-migration/first/adis16448_imu_frc>`.
| ===== Using GetAngle() and GetRate() ===== Now that your gyro is calibrated when the robot turns on, you can access data from the robot in your code. You can do this using the GetAngle() method to obtain the robot's current yaw heading, or more rarely by using the GetRate() method to obtain the current rotation rate being measured should you happen to need it. The most common places to use these functions are inside of the AutonomousPeriodic() and TeleopPeriodic() methods. If you want a specific angle, you can also call that angle directly using GetAngleX(), GetAngleY(), or GetAngleZ(). You can do the same for rotation rates, using GetRateX(), GetRateY(), and GetRateZ().
|

.. tip::

   As a general note, the GetAngle() functions will count continuously, meaning when they reach 360 degrees, they will continue to 361, not zero. This is to make any functionality in your code using the IMU angle easier to implement without having to keep track of where in the 0-360 range your robot is or how many rotations have happened.


| ===== Re-Zeroing the Sensor with Reset() ===== Sometimes it may be necessary to reset the IMU gyro's “zero degrees” position. All gyros will have some amount of drift over time and it's physically impossible to calibrate out all sources of drift. In this case, you can use Reset() to reset the current gyro heading to 0 degrees. When doing this, your robot should be facing the direction you want zero degrees to be, particularly if you are driving with field-oriented drive using an omnidirectional drive base. Otherwise, your robot may begin to behave incorrectly. For this reason, you should never automate this routine. Note that this **does not** recalibrate the gyro, so you don't have to be sitting still to perform this method properly.
| ===== Drive Straight Example ===== The code block shown below is a modification of the WPI Library gyro drive straight example to use the ADIS16448 IMU instead.

::

   /*----------------------------------------------------------------------------*/
   /* Copyright (c) 2017-2018 FIRST. All Rights Reserved.                        */
   /* Open Source Software - may be modified and shared by FRC teams. The code   */
   /* must be accompanied by the FIRST BSD license file in the root directory of */
   /* the project.                                                               */
   /*----------------------------------------------------------------------------*/

   #include <cmath>

   #include <Drive/DifferentialDrive.h>
   #include <IterativeRobot.h>
   #include <Joystick.h>
   #include <Spark.h>
   #include <ADIS16448_IMU.h>

   /**
     * This is a sample program to demonstrate how to use a gyro sensor to make a
     * robot drive straight. This program uses a joystick to drive forwards and
     * backwards while the gyro is used for direction keeping.
    */
   class Robot : public frc::IterativeRobot {
   public:
       
       void RobotInit() override {
           imu.Calibrate();
       }

       /**
        * The motor speed is set from the joystick while the DifferentialDrive
        * turning value is assigned from the error between the setpoint and the
        * gyro angle.
        */
       void TeleopPeriodic() override {
           double turningValue = (kAngleSetpoint - imu.GetAngleZ()) * kP;
           // Invert the direction of the turn if we are going backwards
           turningValue = std::copysign(turningValue, m_joystick.GetY());
           m_robotDrive.ArcadeDrive(m_joystick.GetY(), turningValue);
       }

   private:
       static constexpr double kAngleSetpoint = 0.0;
           static constexpr double kP = 0.005;

       static constexpr int kLeftMotorPort = 0;
       static constexpr int kRightMotorPort = 1;
       static constexpr int kJoystickPort = 0;

       frc::Spark m_left{kLeftMotorPort};
       frc::Spark m_right{kRightMotorPort};
       frc::DifferentialDrive m_robotDrive{m_left, m_right};
           frc::ADIS16448_IMU imu{};

       frc::Joystick m_joystick{kJoystickPort};
   };

   START_ROBOT_CLASS(Robot)
