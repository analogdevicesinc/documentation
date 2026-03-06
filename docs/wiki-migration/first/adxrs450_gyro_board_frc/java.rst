Using the ADXRS450 Gyro for FRC in Java
=======================================

| This guide will walk you through the various features of the WPI Library for the ADXRS450 FRC Gyro Board and how to use it in your Java robot code. If you're looking for a guide in another language, :doc:`click here </wiki-migration/first/adxrs450_gyro_board_frc/cpp>` for C++ or :doc:`here </wiki-migration/first/adxrs450_gyro_board_frc/labview>` for LabVIEW.
| If you need help getting started with the basics of programming your robot in java, you may want to check out the WPI Screensteps documentation, which can be found `here <https://wpilib.screenstepslive.com/s/currentCS/m/java>`__. Another useful resource can be found `here <https://media.readthedocs.org/pdf/frc-pdr/latest/frc-pdr.pdf>`__.
| ===== Definition and Instantiation ===== Before you can read data from the gyro, you'll need to define and instantiate an ADXRS450_Gyro object in your code as part of the Robot class. Where exactly you decide to put it will depend on how your team organizes your robot code, but as long as it is accessible by the Robot class, you will be able to use it.
| When you instantiate your gyro, you will need to define which SPI port the device will be using. Depending on how you have set up your gyro (see notes on the general FRC Gyro page), this will vary, but should usually be set to CS0. Alternatively, you can leave the port out of the instantiation and the robot will default to CS0.
| ===== Sensor Initialization and Calibration with calibrate() ===== Once your gyro is defined and instantiated, you will need to initialize it with a calibration where it will execute as soon as the robot is powered on, typically robotInit(). To do this, you will need to call the calibrate() method. Calibration is necessary for proper operation and **MUST** be performed before the gyro can be used. For more information, please see the :doc:`general FRC Gyro page </wiki-migration/first/adxrs450_gyro_board_frc>`.
| ===== Using getAngle() and getRate() ===== Now that your sensor is calibrated you can start reading data from the gyro. You can use getAngle() to obtain the robot's current heading as a double. If you ever need it you can also request the current rotation rate using getRate(), though this is typically very rare. You'll typically use these in either autonomousPeriodic() and teleopPeriodic().
|

.. tip::

   As a general note, the getAngle() method will count continuously, meaning when it reaches 360 degrees, it will continue to 361, not zero. This is to make any functionality in your code using the gyro angle easier to implement without having to keep track of where in the 0-360 range your robot is or how many rotations have happened.


| ===== Re-Zeroing the Gyro with reset() ===== Sometimes it may be necessary to reset the gyro's "zero degrees" position. All gyros will have some amount of drift over time and it's physically impossible to calibrate out all sources of drift. In this case, you can use reset() to reset the current gyro heading to 0 degrees. When doing this, your robot should be facing the direction you want zero degrees to be, particularly if you are driving with field-oriented drive using an omnidirectional drive base. Otherwise, your robot may begin to behave incorrectly. For this reason, you should never automate this routine. Note that this **does not** recalibrate the gyro, so you don't have to be sitting still to perform this method properly.
| ===== Drive Straight Example ===== To show you how you would use the gyro in your code, we'll take a look at the gyro example that comes packaged in the WPI library and modify it to use the ADXRS450 gyro instead of the analog gyro. When you open the example, it should look like this.
| ``/*----------------------------------------------------------------------------*/
  /* Copyright (c) 2017-2018 FIRST. All Rights Reserved.                        */
  /* Open Source Software - may be modified and shared by FRC teams. The code   */
  /* must be accompanied by the FIRST BSD license file in the root directory of */
  /* the project.                                                               */
  /*----------------------------------------------------------------------------*/

  package org.usfirst.frc.team2655.robot;

  import edu.wpi.first.wpilibj.AnalogGyro;
  import edu.wpi.first.wpilibj.IterativeRobot;
  import edu.wpi.first.wpilibj.Joystick;
  import edu.wpi.first.wpilibj.Spark;
  import edu.wpi.first.wpilibj.drive.DifferentialDrive;

  /**
    * This is a sample program to demonstrate how to use a gyro sensor to make a
    * robot drive straight. This program uses a joystick to drive forwards and
    * backwards while the gyro is used for direction keeping.
   */
  public class Robot extends IterativeRobot {
      private static final double kAngleSetpoint = 0.0;
      private static final double kP = 0.005; // propotional turning constant

      // gyro calibration constant, may need to be adjusted;
      // gyro value of 360 is set to correspond to one full revolution
      private static final double kVoltsPerDegreePerSecond = 0.0128;

      private static final int kLeftMotorPort = 0;
      private static final int kRightMotorPort = 1;
      private static final int kGyroPort = 0;
      private static final int kJoystickPort = 0;

      private DifferentialDrive m_myRobot
              = new DifferentialDrive(new Spark(kLeftMotorPort),
              new Spark(kRightMotorPort));
      private AnalogGyro m_gyro = new AnalogGyro(kGyroPort);
      private Joystick m_joystick = new Joystick(kJoystickPort);

      @Override
      public void robotInit() {
          m_gyro.setSensitivity(kVoltsPerDegreePerSecond);
      }

      /**
       * The motor speed is set from the joystick while the RobotDrive turning
       * value is assigned from the error between the setpoint and the gyro angle.
       */
      @Override
      public void teleopPeriodic() {
          double turningValue = (kAngleSetpoint - m_gyro.getAngle()) * kP;
          // Invert the direction of the turn if we are going backwards
          turningValue = Math.copySign(turningValue, m_joystick.getY());
          m_myRobot.arcadeDrive(m_joystick.getY(), turningValue);
      }
  }`` First we will need to tell the program to import the correct library for using the ADXRS450. Change your import statement from AnalogGyro to ADXRS450_Gyro like below. You'll also need to import the SPI library so you can use the SPI port in your code, which is required for the gyro to communicate with the RoboRIO.
| ``package org.usfirst.frc.team9999.robot;

  import edu.wpi.first.wpilibj.AnalogGyro;
  import edu.wpi.first.wpilibj.IterativeRobot;
  import edu.wpi.first.wpilibj.Joystick;
  import edu.wpi.first.wpilibj.Spark;
  import edu.wpi.first.wpilibj.drive.DifferentialDrive;``

::

   package org.usfirst.frc.team9999.robot;

   import edu.wpi.first.wpilibj.ADXRS450_Gyro;
   import edu.wpi.first.wpilibj.SPI;
   import edu.wpi.first.wpilibj.IterativeRobot;
   import edu.wpi.first.wpilibj.Joystick;
   import edu.wpi.first.wpilibj.Spark;
   import edu.wpi.first.wpilibj.drive.DifferentialDrive;

| Now we need to fix all of the variable definitions. You'll need to fix the gyro port variable as well as the gyro itself, and delete the kVoltsPerDegrePerSecond variable and its related comments. In case you're using a port other than CS0, I've explicitly defined my gyro port below. If you're using CS0, you don't have to include the port.
| ``public class Robot extends IterativeRobot {
      private static final double kAngleSetpoint = 0.0;
      private static final double kP = 0.005; // propotional turning constant

      // gyro calibration constant, may need to be adjusted;
      // gyro value of 360 is set to correspond to one full revolution
      private static final double kVoltsPerDegreePerSecond = 0.0128;

      private static final int kLeftMotorPort = 0;
      private static final int kRightMotorPort = 1;
      private static final int kGyroPort = 0;
      private static final int kJoystickPort = 0;

      private DifferentialDrive m_myRobot
              = new DifferentialDrive(new Spark(kLeftMotorPort),
              new Spark(kRightMotorPort));
      private AnalogGyro m_gyro = new AnalogGyro(kGyroPort);
      private Joystick m_joystick = new Joystick(kJoystickPort);``

::

   public class Robot extends IterativeRobot {
       private static final double kAngleSetpoint = 0.0;
       private static final double kP = 0.005; // propotional turning constant

       private static final int kLeftMotorPort = 0;
       private static final int kRightMotorPort = 1;
       private static final SPI.Port kGyroPort = SPI.Port.kOnboardCS0;
       private static final int kJoystickPort = 0;

       private DifferentialDrive m_myRobot
               = new DifferentialDrive(new Spark(kLeftMotorPort),
               new Spark(kRightMotorPort));
       private ADXRS450_Gyro m_gyro = new ADXRS450_Gyro(kGyroPort);
       private Joystick m_joystick = new Joystick(kJoystickPort);

| Next you'll need to fix the method called in robotInit() to be calibrate() instead of setSensitivity(). You can also delete the argument from setSensitivity(), since calibrate does not take any arguments.
| ``@Override
      public void robotInit() {
          m_gyro.setSensitivity(kVoltsPerDegreePerSecond);
      }``

::

       @Override
       public void robotInit() {
           m_gyro.calibrate();
       }

| You can leave teleopPeriodic() alone since nothing is different here between using data from an analog gyro and the ADXRS450. When you're done, your code should now look like this.
| ``/*----------------------------------------------------------------------------*/
  /* Copyright (c) 2017-2018 FIRST. All Rights Reserved.                        */
  /* Open Source Software - may be modified and shared by FRC teams. The code   */
  /* must be accompanied by the FIRST BSD license file in the root directory of */
  /* the project.                                                               */
  /*----------------------------------------------------------------------------*/

  package org.usfirst.frc.team2655.robot;

  import edu.wpi.first.wpilibj.ADXRS450_Gyro;
  import edu.wpi.first.wpilibj.SPI;
  import edu.wpi.first.wpilibj.IterativeRobot;
  import edu.wpi.first.wpilibj.Joystick;
  import edu.wpi.first.wpilibj.Spark;
  import edu.wpi.first.wpilibj.drive.DifferentialDrive;

  /**
    * This is a sample program to demonstrate how to use a gyro sensor to make a
    * robot drive straight. This program uses a joystick to drive forwards and
    * backwards while the gyro is used for direction keeping.
   */
  public class Robot extends IterativeRobot {
      private static final double kAngleSetpoint = 0.0;
      private static final double kP = 0.005; // propotional turning constant

      private static final int kLeftMotorPort = 0;
      private static final int kRightMotorPort = 1;
      private static final SPI.Port kGyroPort = SPI.Port.kOnboardCS0;
      private static final int kJoystickPort = 0;

      private DifferentialDrive m_myRobot
              = new DifferentialDrive(new Spark(kLeftMotorPort),
              new Spark(kRightMotorPort));
      private ADXRS450_Gyro m_gyro = new ADXRS450_Gyro(kGyroPort);
      private Joystick m_joystick = new Joystick(kJoystickPort);

      @Override
      public void robotInit() {
          m_gyro.calibrate();
      }

      /**
       * The motor speed is set from the joystick while the RobotDrive turning
       * value is assigned from the error between the setpoint and the gyro angle.
       */
      @Override
      public void teleopPeriodic() {
          double turningValue = (kAngleSetpoint - m_gyro.getAngle()) * kP;
          // Invert the direction of the turn if we are going backwards
          turningValue = Math.copySign(turningValue, m_joystick.getY());
          m_myRobot.arcadeDrive(m_joystick.getY(), turningValue);
      }
  }``
