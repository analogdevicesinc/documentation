Inclinometer Design Desktop Application
=======================================

Features
--------

-  PC-based graphical user interface (GUI)
-  Fast, easy installation
-  Can simulate Single Axis or Dual Axis Inclinometer
-  Includes different ADXL Devices with digital interface
-   \* :adi:`ADXL312` , :adi:`ADXL313` , :adi:`ADXL343` ,
-   \* :adi:`ADXL344` , :adi:`ADXL345` , :adi:`ADXL346` ,
-   \* :adi:`ADXL350` , :adi:`ADXL355` , :adi:`ADXL362` ,
-   \* :adi:`ADXL363` , :adi:`ADXL367`

General Description
-------------------

This user guide describes the inclinometer design software for digital ADXL
accelerometer. This user guide provides an overview of how to use the
application software to simulate inclinometer using ADXL Devices. The
step-by-step instructions on how to use the software

User Guide
----------

Installation
~~~~~~~~~~~~

**PC System Requirements** - Windows 10

- Download the Inclinometer Design Desktop Application Installer link below

.. admonition:: Download
   :class: download

   `Inclinometer Design Desktop Application Installer <../resources/inclinometer_design_desktop_application_installer.zip>`_

   

- Extract the Installer from the Zipped folder.

- Double-click on the Inclinometer Design Desktop Application Installer.

.. image:: ../images/installer1.jpg
   :align: center
   :width: 200

**Figure 1:** Inclinometer Design Desktop Application Installer

- Run the Installer and Click Next

.. image:: ../images/installer2.jpg
   :align: center
   :width: 400

**Figure 2:** Inclinometer Design Desktop Application Installer Wizard

- Accept The License Agreement and click Next

.. image:: ../images/installer3.jpg
   :align: center
   :width: 400

**Figure 3:** License Agreement

- Select the placement of shortcut for the software and click Next

.. image:: ../images/installer4.jpg
   :align: center
   :width: 400

**Figure 4:** Shortcut creation

- Wait until installation is done and click finish

.. image:: ../images/installer5.jpg
   :align: center
   :width: 400

**Figure 5:** Completed Installation

- Open the Inclinometer Design Desktop Application

.. image:: ../images/idda2.jpg
   :align: center
   :width: 600

**Figure 6:** The Inclinometer Design Desktop Application GUI

- Select the number of axis to be used as inclinometer. Provided with two
  options (1-axis or 2-axis)

.. image:: ../images/idda3.jpg
   :align: center
   :width: 600

**Figure 7:** The Inclinometer Design Desktop Application GUI (Axis Selection)

1 Axis Option
~~~~~~~~~~~~~

- Upon selection of the 1 axis option the GUI will display the Incremental
  Inclination Sensitivity window

.. image:: ../images/idda4.jpg
   :align: center
   :width: 600

**Figure 8:** The Inclinometer Design Desktop Application GUI (1-Axis Selected)

- Select the ADXL to be simulated as an inclinometer

.. image:: ../images/idda5.jpg
   :align: center
   :width: 600

**Figure 9:** The Inclinometer Design Desktop Application GUI (Device Selection)

- Select the g settings (g settings are dependent on the device selected)

.. image:: ../images/idda6.jpg
   :align: center
   :width: 600

**Figure 10:** The Inclinometer Design Desktop Application GUI (g Selection)

- Select the resolution of the device

.. image:: ../images/idda7.jpg
   :align: center
   :width: 600

**Figure 11:** The Inclinometer Design Desktop Application GUI (Resolution Selection)

- Inclinometer Resolution in degrees will be provided and plot the inclination
  based on the increment of the device's output acceleration. Refer to Figure
  12.

.. image:: ../images/idda8.jpg
   :align: center
   :width: 600

**Figure 12:** The Inclinometer Design Desktop Application GUI (Output Acceleration vs. Inclination Plot)

Incremental Sensitivity
~~~~~~~~~~~~~~~~~~~~~~~

- For 1 Axis inclinometer, minimum sensitivity can be determined by providing
  the step size and the range of inclination

- Select the Step size

.. image:: ../images/idda9.jpg
   :align: center
   :width: 600

**Figure 13:** The Inclinometer Design Desktop Application GUI (Step Size Selection)

- Input the Angle Range (from 1-90 degrees)

|image1|

**Figure 14:** The Inclinometer Design Desktop Application GUI (Step Size Selection)

- The Resolution in mg will be provided and the plot of the minimum sensitivity
  based on the angle of inclination. Refer to Figure 15.

|image2|

**Figure 15:** The Inclinometer Design Desktop Application GUI (Minimum Sensitivity vs. Inclination)

2 Axis Option
~~~~~~~~~~~~~

- Upon selection of the 2 axis option the GUI will display the Calculated Angle
  Error Due to Accelerometer Offset window

.. image:: ../images/idda12.jpg
   :align: center
   :width: 600

**Figure 16:** The Inclinometer Design Desktop Application GUI (2-Axis Selected)

- Select the ADXL to be simulated as an inclinometer

.. image:: ../images/idda13.jpg
   :align: center
   :width: 600

**Figure 17:** The Inclinometer Design Desktop Application GUI (Device Selection)

- Select the g settings (g settings are dependent on the device selected)

.. image:: ../images/idda14.jpg
   :align: center
   :width: 600

**Figure 18:** The Inclinometer Design Desktop Application GUI (g Selection)

- Select the resolution of the device

.. image:: ../images/idda15.jpg
   :align: center
   :width: 600

**Figure 19:** The Inclinometer Design Desktop Application GUI (Resolution Selection)

- Inclinometer Resolution in degrees will be provided and plot the inclination
  based on the increment of the device's output acceleration for x-axis, y-axis
  and 2 axis. Refer to Figure 20.

.. image:: ../images/idda16.jpg
   :align: center
   :width: 600

**Figure 20:** The Inclinometer Design Desktop Application GUI (Output Acceleration vs. Inclination Plot)

Effects of Offset Error in Either of the Axis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Select the Axis to where the offset will be added and input the offset value
  in mg. Calculated angle error due to offset will be plotted from -90 to +90
  degrees. Refer to Figure 21

.. image:: ../images/idda17.jpg
   :align: center
   :width: 600

**Figure 21:** The Inclinometer Design Desktop Application GUI (Calculated Angle Error Due to Accelerometer Offset)

**Reference:** Fisher, C.(2010).Using an accelerometer for inclination sensing. AN-1057, Application note, Analog Devices

.. |image1| image:: ../images/idda10.jpg
   :width: 600

.. |image2| image:: ../images/idda11.jpg
   :width: 600
