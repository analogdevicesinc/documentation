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

This user guide describes the inclinometer design software for digital ADXL accelerometer. This user guide provides an overview of how to use the application software to simulate inclinometer using ADXL Devices. The step-by-step instructions on how to use the software

User Guide
----------

Installation
~~~~~~~~~~~~

**PC System Requirements** - Windows 10

- Download the Inclinometer Design Desktop Application Installer link below

.. admonition:: Download
   :class: download

   `Inclinometer Design Desktop Application Installer <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/inclinometer_design_desktop_application_installer.zip>`__

   


- Extract the Installer from the Zipped folder.

- Double-click on the Inclinometer Design Desktop Application Installer.


|image1|

.. container:: center lo

   **Figure 1:** Inclinometer Design Desktop Application Installer


- Run the Installer and Click Next



|image2|

.. container:: center lo

   **Figure 2:** Inclinometer Design Desktop Application Installer Wizard


- Accept The License Agreement and click Next



|image3|

.. container:: center lo

   **Figure 3:** License Agreement


- Select the placement of shortcut for the software and click Next



|image4|

.. container:: center lo

   **Figure 4:** Shortcut creation


- Wait until installation is done and click finish



|image5|

.. container:: center lo

   **Figure 5:** Completed Installation


- Open the Inclinometer Design Desktop Application



|image6|

.. container:: center lo

   **Figure 6:** The Inclinometer Design Desktop Application GUI


- Select the number of axis to be used as inclinometer. Provided with two options (1-axis or 2-axis)



|image7|

.. container:: center lo

   **Figure 7:** The Inclinometer Design Desktop Application GUI (Axis Selection)


1 Axis Option
~~~~~~~~~~~~~

- Upon selection of the 1 axis option the GUI will display the Incremental Inclination Sensitivity window


|image8|

.. container:: center lo

   **Figure 8:** The Inclinometer Design Desktop Application GUI (1-Axis Selected)


- Select the ADXL to be simulated as an inclinometer



|image9|

.. container:: center lo

   **Figure 9:** The Inclinometer Design Desktop Application GUI (Device Selection)


- Select the g settings (g settings are dependent on the device selected)



|image10|

.. container:: center lo

   **Figure 10:** The Inclinometer Design Desktop Application GUI (g Selection)


- Select the resolution of the device

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda7.jpg
   :align: center
   :width: 600px

.. container:: center lo

   **Figure 11:** The Inclinometer Design Desktop Application GUI (Resolution Selection)


- Inclinometer Resolution in degrees will be provided and plot the inclination based on the increment of the device's output acceleration. Refer to Figure 12.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda8.jpg
   :align: center
   :width: 600px

.. container:: center lo

   **Figure 12:** The Inclinometer Design Desktop Application GUI (Output Acceleration vs. Inclination Plot)


Incremental Sensitivity
~~~~~~~~~~~~~~~~~~~~~~~

- For 1 Axis inclinometer, minimum sensitivity can be determined by providing the step size and the range of inclination

- Select the Step size

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda9.jpg
   :align: center
   :width: 600px

.. container:: center lo

   **Figure 13:** The Inclinometer Design Desktop Application GUI (Step Size Selection)


- Input the Angle Range (from 1-90 degrees)



|image11|

.. container:: center lo

   **Figure 14:** The Inclinometer Design Desktop Application GUI (Step Size Selection)


- The Resolution in mg will be provided and the plot of the minimum sensitivity based on the angle of inclination. Refer to Figure 15.



|image12|

.. container:: center lo

   **Figure 15:** The Inclinometer Design Desktop Application GUI (Minimum Sensitivity vs. Inclination)


.. _axis-option-1:

2 Axis Option
~~~~~~~~~~~~~

- Upon selection of the 2 axis option the GUI will display the Calculated Angle Error Due to Accelerometer Offset window


|image13|

.. container:: center lo

   **Figure 16:** The Inclinometer Design Desktop Application GUI (2-Axis Selected)


- Select the ADXL to be simulated as an inclinometer



|image14|

.. container:: center lo

   **Figure 17:** The Inclinometer Design Desktop Application GUI (Device Selection)


- Select the g settings (g settings are dependent on the device selected)



|image15|

.. container:: center lo

   **Figure 18:** The Inclinometer Design Desktop Application GUI (g Selection)


- Select the resolution of the device

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda15.jpg
   :align: center
   :width: 600px

.. container:: center lo

   **Figure 19:** The Inclinometer Design Desktop Application GUI (Resolution Selection)


- Inclinometer Resolution in degrees will be provided and plot the inclination based on the increment of the device's output acceleration for x-axis, y-axis and 2 axis. Refer to Figure 20.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda16.jpg
   :align: center
   :width: 600px

.. container:: center lo

   **Figure 20:** The Inclinometer Design Desktop Application GUI (Output Acceleration vs. Inclination Plot)


Effects of Offset Error in Either of the Axis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Select the Axis to where the offset will be added and input the offset value in mg. Calculated angle error due to offset will be plotted from -90 to +90 degrees. Refer to Figure 21

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda17.jpg
   :align: center
   :width: 600px

.. container:: center lo

   **Figure 21:** The Inclinometer Design Desktop Application GUI (Calculated Angle Error Due to Accelerometer Offset)


**Reference:** Fisher, C.(2010).Using an accelerometer for inclination sensing. AN-1057, Application note, Analog Devices

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/installer1.jpg
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/installer2.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/installer3.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/installer4.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/installer5.jpg
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda2.jpg
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda3.jpg
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda4.jpg
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda5.jpg
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda6.jpg
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda10.jpg
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda11.jpg
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda12.jpg
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda13.jpg
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/idda14.jpg
   :width: 600px
