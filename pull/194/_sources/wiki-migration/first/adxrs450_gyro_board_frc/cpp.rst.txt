Using the ADXRS450 Gyro for FRC in C++
======================================

| This guide will walk you through the various features of the WPI Library for the ADXRS450 FRC Gyro Board and how to use it in your robot code. If you're looking for a guide in another language, :doc:`click here </wiki-migration/first/adxrs450_gyro_board_frc/java>` for Java or :doc:`here </wiki-migration/first/adxrs450_gyro_board_frc/labview>` for LabVIEW.
| If you need help getting started with the basics of programming your robot in C++, you may want to check out the WPI Screensteps documentation, which can be found `here <https://wpilib.screenstepslive.com/s/currentCS/m/cpp>`_. Another useful resource can be found `here <https://media.readthedocs.org/pdf/frc-pdr/latest/frc-pdr.pdf>`_.
| ===== Instance Definition and Instantiation ===== Before you can use the gyro in your code, you must first define an instance. Where exactly it needs to be defined will depend heavily on how your team organizes its robot code, but it needs to be accessible by the Robot class in order to work properly and give you no build errors. If your team is using an Iterative Robot with a RobotMap structure for example, you would put it inside of the RobotMap class. The ADXRS450 has its own dedicated class in the frc namespace and inherits properties from the Gyro class.

| When you instantiate your gyro, you will need to define which SPI port the device will be using. Depending on how you have set up your gyro (:doc:`see notes on the general FRC Gyro page </wiki-migration/first/adxrs450_gyro_board_frc>`), this will vary, but should usually be set to CS0. Alternatively, you can leave the port out of the instantiation and the robot will default to CS0.
| ===== Sensor Initialization/Calibration with Calibrate() ===== Once your gyro is defined and instantiated, you will need to initialize it with a calibration wherever it needs to be in order to execute as soon as the robot is powered on, typically RobotInit(). To do this, you will need to call the Calibrate() method. Calibration is necessary for proper operation and **MUST** be performed before the gyro can be used. For more information, please see the :doc:`general FRC Gyro page </wiki-migration/first/adxrs450_gyro_board_frc>`.
| ===== Using GetAngle() and GetRate() ===== Now that your gyro is calibrated when the robot turns on, you can access data from the robot in your code. You can do this using the GetAngle() method to obtain the robot's current heading, or more rarely by using the GetRate() method to obtain the current rotation rate being measured should you happen to need it. The most common places to use these functions are inside of the AutonomousPeriodic() and TeleopPeriodic() methods.
|

.. tip::

   As a general note, the GetAngle() method will count continuously, meaning when it reaches 360 degrees, it will continue to 361, not zero. This is to make any functionality in your code using the gyro angle easier to implement without having to keep track of where in the 0-360 range your robot is or how many rotations have happened.


| ===== Re-Zeroing the Sensor with Reset() ===== Sometimes it may be necessary to reset the gyro's “zero degrees” position. All gyros will have some amount of drift over time and it's physically impossible to calibrate out all sources of drift. In this case, you can use Reset() to reset the current gyro heading to 0 degrees. When doing this, your robot should be facing the direction you want zero degrees to be, particularly if you are driving with field-oriented drive using an omnidirectional drive base. Otherwise, your robot may begin to behave incorrectly. For this reason, you should never automate this routine. Note that this **does not** recalibrate the gyro, so you don't have to be sitting still to perform this method properly.
| ===== Drive Straight Example ===== As a simple example, we will be modifying the Drive Straight Gyro Example that comes pre-packaged with the WPI library to use the ADXRS450 instead of an analog gyro. This is what you will see when you open the existing example:
| ``/*----------------------------------------------------------------------------*/
  /* Copyright (c) 2017-2018 FIRST. All Rights Reserved.                        */
  /* Open Source Software - may be modified and shared by FRC teams. The code   */
  /* must be accompanied by the FIRST BSD license file in the root directory of */
  /* the project.                                                               */
  /*----------------------------------------------------------------------------*/

  #include <cmath>

  #include <AnalogGyro.h>
  #include <Drive/DifferentialDrive.h>
  #include <IterativeRobot.h>
  #include <Joystick.h>
  #include <Spark.h>

  /**
    * This is a sample program to demonstrate how to use a gyro sensor to make a
    * robot drive straight. This program uses a joystick to drive forwards and
    * backwards while the gyro is used for direction keeping.
   */
  class Robot : public frc::IterativeRobot {
  public:
      void RobotInit() override {
          m_gyro.SetSensitivity(kVoltsPerDegreePerSecond);
      }

      /**
       * The motor speed is set from the joystick while the DifferentialDrive
       * turning value is assigned from the error between the setpoint and the
       * gyro angle.
       */
      void TeleopPeriodic() override {
          double turningValue = (kAngleSetpoint - m_gyro.GetAngle()) * kP;
          // Invert the direction of the turn if we are going backwards
          turningValue = std::copysign(turningValue, m_joystick.GetY());
          m_robotDrive.ArcadeDrive(m_joystick.GetY(), turningValue);
      }

  private:
      static constexpr double kAngleSetpoint = 0.0;
      static constexpr double kP = 0.005;  // Proportional turning constant

      // Gyro calibration constant, may need to be adjusted
      // Gyro value of 360 is set to correspond to one full revolution
      static constexpr double kVoltsPerDegreePerSecond = 0.0128;

      static constexpr int kLeftMotorPort = 0;
      static constexpr int kRightMotorPort = 1;
      static constexpr int kGyroPort = 0;
      static constexpr int kJoystickPort = 0;

      frc::Spark m_left{kLeftMotorPort};
      frc::Spark m_right{kRightMotorPort};
      frc::DifferentialDrive m_robotDrive{m_left, m_right};

      frc::AnalogGyro m_gyro{kGyroPort};
      frc::Joystick m_joystick{kJoystickPort};
  };

  START_ROBOT_CLASS(Robot)`` First, we need to tell the program to include the right header file for the ADI gyro. Change AnalogGyro.h to ADXRS450_Gyro.h at the top of the page.
| ``#include <cmath>

  #include <AnalogGyro.h>
  #include <Drive/DifferentialDrive.h>
  #include <IterativeRobot.h>
  #include <Joystick.h>
  #include <Spark.h>``

::

   #include <cmath>

   #include <ADXRS450_Gyro.h>
   #include <Drive/DifferentialDrive.h>
   #include <IterativeRobot.h>
   #include <Joystick.h>
   #include <Spark.h>

| Now you'll need to change the method that's being called within RobotInit(), since SetSensitivity() doesn't apply to our gyro. You can replace the text "SetSensitivity" with "Calibrate" so that we can perform the required calibration sequence. You should also delete the kVoltsPerDegreePerSecond argument, since Calibrate does not accept any arguments.
| ``class Robot : public frc::IterativeRobot {
  public:
      void RobotInit() override {
          m_gyro.SetSensitivity(kVoltsPerDegreePerSecond);
      }

      /**
       * The motor speed is set from the joystick while the DifferentialDrive
       * turning value is assigned from the error between the setpoint and the
       * gyro angle.
       */
      void TeleopPeriodic() override {
          double turningValue = (kAngleSetpoint - m_gyro.GetAngle()) * kP;
          // Invert the direction of the turn if we are going backwards
          turningValue = std::copysign(turningValue, m_joystick.GetY());
          m_robotDrive.ArcadeDrive(m_joystick.GetY(), turningValue);
      }``

::

   class Robot : public frc::IterativeRobot {
   public:
       void RobotInit() override {
           m_gyro.Calibrate();
       }

       /**
        * The motor speed is set from the joystick while the DifferentialDrive
        * turning value is assigned from the error between the setpoint and the
        * gyro angle.
        */
       void TeleopPeriodic() override {
           double turningValue = (kAngleSetpoint - m_gyro.GetAngle()) * kP;
           // Invert the direction of the turn if we are going backwards
           turningValue = std::copysign(turningValue, m_joystick.GetY());
           m_robotDrive.ArcadeDrive(m_joystick.GetY(), turningValue);
       }

| TeleopPeriodic can be left alone, since GetAngle() is the same for both gyro types. Now we get to the private definitions of the Robot class for this example. First you can delete the definition for kVoltsPerDegreePerSecond, since this variable is no longer needed and we don't want it consuming memory. You can also delete the two comments above it since they don't apply to the ADXRS450 gyro. You also need to change the class on your gyro definition from AnalogGyro to ADXRS450_Gyro in the instantiation. You can also delete the argument if your gyro is in the default configuration. Otherwise, change it to the port you will be using. I've configured mine by explicitly defining the C0 port below.
| ``private:
      static constexpr double kAngleSetpoint = 0.0;
      static constexpr double kP = 0.005;  // Proportional turning constant

      // Gyro calibration constant, may need to be adjusted
      // Gyro value of 360 is set to correspond to one full revolution
      static constexpr double kVoltsPerDegreePerSecond = 0.0128;

      static constexpr int kLeftMotorPort = 0;
      static constexpr int kRightMotorPort = 1;
      static constexpr int kGyroPort = 0;
      static constexpr int kJoystickPort = 0;

      frc::Spark m_left{kLeftMotorPort};
      frc::Spark m_right{kRightMotorPort};
      frc::DifferentialDrive m_robotDrive{m_left, m_right};

      frc::AnalogGyro m_gyro{kGyroPort};
      frc::Joystick m_joystick{kJoystickPort};
  };``

::

   private:
       static constexpr double kAngleSetpoint = 0.0;
       static constexpr double kP = 0.005;  // Proportional turning constant

       static constexpr int kLeftMotorPort = 0;
       static constexpr int kRightMotorPort = 1;
       static constexpr SPI::Port kGyroPort = 0;
       static constexpr int kJoystickPort = 0;

       frc::Spark m_left{kLeftMotorPort};
       frc::Spark m_right{kRightMotorPort};
       frc::DifferentialDrive m_robotDrive{m_left, m_right};

       frc::ADXRS450_Gyro m_gyro{kGyroPort};
       frc::Joystick m_joystick{kJoystickPort};
   };

| Go ahead and build your code to ensure there are no errors. This is what you should have once you're done.
| ``/*----------------------------------------------------------------------------*/
  /* Copyright (c) 2017-2018 FIRST. All Rights Reserved.                        */
  /* Open Source Software - may be modified and shared by FRC teams. The code   */
  /* must be accompanied by the FIRST BSD license file in the root directory of */
  /* the project.                                                               */
  /*----------------------------------------------------------------------------*/

  #include <cmath>

  #include <ADXRS450_Gyro.h>
  #include <Drive/DifferentialDrive.h>
  #include <IterativeRobot.h>
  #include <Joystick.h>
  #include <Spark.h>

  /**
    * This is a sample program to demonstrate how to use a gyro sensor to make a
    * robot drive straight. This program uses a joystick to drive forwards and
    * backwards while the gyro is used for direction keeping.
   */
  class Robot : public frc::IterativeRobot {
  public:
      void RobotInit() override {
          m_gyro.Calibrate();
      }

      /**
       * The motor speed is set from the joystick while the DifferentialDrive
       * turning value is assigned from the error between the setpoint and the
       * gyro angle.
       */
      void TeleopPeriodic() override {
          double turningValue = (kAngleSetpoint - m_gyro.GetAngle()) * kP;
          // Invert the direction of the turn if we are going backwards
          turningValue = std::copysign(turningValue, m_joystick.GetY());
          m_robotDrive.ArcadeDrive(m_joystick.GetY(), turningValue);
      }

  private:
      static constexpr double kAngleSetpoint = 0.0;
      static constexpr double kP = 0.005;  // Proportional turning constant

      static constexpr int kLeftMotorPort = 0;
      static constexpr int kRightMotorPort = 1;
      static constexpr SPI::Port kGyroPort = 0;
      static constexpr int kJoystickPort = 0;

      frc::Spark m_left{kLeftMotorPort};
      frc::Spark m_right{kRightMotorPort};
      frc::DifferentialDrive m_robotDrive{m_left, m_right};

      frc::ADXRS450_Gyro m_gyro{kGyroPort};
      frc::Joystick m_joystick{kJoystickPort};
  };

  START_ROBOT_CLASS(Robot)``
