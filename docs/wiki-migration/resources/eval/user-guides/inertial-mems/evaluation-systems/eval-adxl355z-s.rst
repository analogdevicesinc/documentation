ADXL355Z EVALUATION ON A PERSONAL COMPUTER
==========================================

The :adi:`ADXL355 <en/products/adxl355.html>` EVB GUI enables PC-based evaluation of the :adi:`ADXL355 <en/products/adxl355.html>` , using the following hardware: :adi:`EVAL-ADXL355Z-S <en/products/adxl355.html#product-overview>` satellite board and :adi:`EVAL-ADXL345Z-M <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-MST-ISEB.html>` mother board. Please see the figure below for an example on how to use these two devices together for this purpose.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/adxl355z-ssetup.png
   :align: center
   :width: 900px

PART NUMBERS TO ORDER
=====================

:adi:`Click here to start the online ordering process <en/products/adxl355.html>` for the following two parts, or contact your ADI distributor to place the order.

:adi:`EVAL-ADXL355Z-S <en/products/adxl355.html#product-overview>`

:adi:`EVAL-ADXL345Z-M <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-MST-ISEB.html>`

SOFTWARE TO DOWNLOAD
====================

-  ADI ISEB USB Driver (ftp://ftp.analog.com/pub/iMEMS_Sensor_Eval/ISEB_USB_Driver/ )
-  ISEB Firmware (ftp://ftp.analog.com/pub/iMEMS_Sensor_Eval/EVAL-ADXL345Z-M/)
-  ADXL355 EVB GUI

PC SYSTEM REQUIREMENTS
======================

Windows 7, 8, 8.1, 10

EVAL-ADXL355Z-S CONTENTS & SETUP
================================

The `EVAL-ADXL355Z-S <https://www.analog.com/>`__ kit comes with the following materials: (1) EVAL-ADXL355Z-S, (2) ADXL355Z, (3) 4 board feet and (4) 4 head screws.

Verify that the jumpers located in the center of :adi:`EVAL-ADXL355Z-S <en/products/adxl355.html#product-overview>` are configured as shown:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/adxl355zjumper.png
   :align: center
   :width: 300px

Place the :adi:`ADXL355 <en/products/adxl355.html>` accelerometer into the socket on the :adi:`EVAL-ADXL355Z-S <en/products/adxl355.html#product-overview>` board. The socket indicator should match the Pin 1 indicator of :adi:`ADXL355 <en/products/adxl355.html>`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/adxl355socket.png
   :align: center
   :width: 400px

Connect one end of the 20-pin ribbon cable to P1 of :adi:`EVAL-ADXL355Z-S <en/products/adxl355.html#product-overview>`.


|image1|

onnect the other end of the 20-pin ribbon cable to P1 of :adi:`EVAL-ADXL345Z-M <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-MST-ISEB.html>`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/step4wiki.png
   :align: center
   :width: 400px

Connect the USB cable (mini-B) to the USB port of the EVAL-ADXL355Z-M. |image2| Connect the USB cable (type A) to the USB port of the PC.

USB DRIVER INSTALLATION
-----------------------

Extract the ADI ISEB USB Driver and execute the *ADI_ISEB_USB_Drivers.exe* file.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/extractiseb.png
   :align: center

Follow the on-screen instructions.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/on-screeniseb.png
   :align: center

If prompted that the drivers are not tested, click Continue Anyway.

The ISEB main board (:adi:`EVAL-ADXL345Z-M <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-MST-ISEB.html>`) can now be connected to the computer via USB. In cases where previously installed drivers are not automatically associated with the device continue with the next step (for older versions of Windows).

Connect the USB (mini-B) to the ISEB and the USB (Type-A) to the PC. The :adi:`EVAL-ADXL355Z-S <en/products/adxl355.html#product-overview>` does not need to be connected in this step.

If prompted to install drivers again, click Install from a list or specific location (Advanced); then click Next.


|image3|

Select Don’t search. I will choose the driver to install, and click Next.


|image4|

Select ADI Inertial Sensor Evaluation System from the model list, and click Next to complete the process.


|image5|

COM PORT VERIFICATION
---------------------

For older version of windows, open My Computer and select Properties then click the Hardware tab of System Properties. Select Device Manager.


|image6|

Expand the Ports(COM & LTP) menu item. ADI Inertial Sensor Evaluation System should be listed with an assigned COM port number in parenthesis. Note the COM Port number for future use.


|image7|

For later version of windows, go to This PC, right click on a blank area on the windows then select Properties.

Select Device Manager from the left-pane.


|image8|

Confirm that the ISEB is connected by expanding the Ports(COM & LPT) menu item. ADI Inertial Sensor Evaluation System should be listed. Note the assigned COM Port number for future use.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/wiki_comlpt_menu.png
   :align: center
   :width: 650px

INSTALLING THE LATEST ISEB FIRMWARE
-----------------------------------

After verifying that the ISEB is connected and with an assigned COM port number, extract the ZIP file downloaded from ftp://ftp.analog.com/pub/iMEMS_Sensor_Eval/EVAL-ADXL345Z-M/ . Go to the EVAL-ADXL345Z-M folder then to ARMWSD folder. Run *ARMWSD.exe* .


|image9|

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/armwsdopen.png
   :align: center

Click *Browse...* and select ADXL355-S.hex from the ADXL Source Code folder.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/adxl355shex.png
   :align: center

Click the *Configure* button of ARMWSD. Click the *Parts* tab of the window that will appear and ensure that the selected part is (:adi:`ADuC7026 <en/products/aduc7026.html>`). Click the *Comms* tab and confirm that the correct Serial Port number is selected. Click *OK*. In cases where the .hex file cannot be downloaded correctly, try to make the Baudrate lower and retry. Program and Verify are suggested to be checked at the same time in the *Commands* tab.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/configure_parts.png
   :align: center

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/commscommand.png
   :align: center

Click *Start* in the ARMWSD to initiate the flashing process. After clicking Start, push the two buttons on the ISEB in the following order to flash the firmware. |image10|


|image11|

-  Press and hold down SW1 (*Serial Download*)
-  With SW1 held down, press and release SW2 (*Reset*)
-  Release SW1

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/buttons.png
   :align: center

If the downloading process fails, attempt the download again by clicking *Start* and pressing the appropriate switch combinations. It may take a few attempts to reprogram the board with no errors. You can also try to lower the download Baudrate to increase success rate. After download has completed , click the *Reset* button to run the new firmware. When this step is complete, the board is updated correctly.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/resetbut.png
   :align: center

INSTALLING THE ADXL355 EVB GUI
------------------------------

The software GUI installation did not include National Instruments drivers and run-time engines that are necessary for proper operation. If there is no such run-time engines in your computer, please also install it before installing the :adi:`ADXL355 <en/products/adxl355.html>` software evaluation GUI. The run-time engine installer also can be found on the ADI FTP.

To run the software GUI installation routine, double-click the setup.exe file located in the :adi:`ADXL355 <en/products/adxl355.html>` EVB GUI folder then follow the on-screen instructions.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/install1.png
   :align: center
   :width: 400px

Click Finish to complete the installation.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/install2.png
   :align: center
   :width: 400px

ADXL355 EVB GUI OVERVIEW
========================

This part gives a basic overview of the functions included in the GUI.

LAUNCH SOFTWARE
---------------

Connect the Evaluation System to the PC. Push SW2 (Reset) on :adi:`EVAL-ADXL345Z-M <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-MST-ISEB.html>`. |image12| Run the :adi:`ADXL355 <en/products/adxl355.html>` EVB GUI from the Start Menu.


|image13|

INITIAL SETUP
-------------

Click *Check Devices* from the GUI.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/checkdevices.png
   :align: center

With the Evaluation System connected to the PC, the COM port of the connected device should appear below the *Check Devices* button. Click on the text and wait for the software to initialize.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/selectcomport.png
   :align: center

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/waitforinit.png
   :align: center

After initialization, the GUI should display current accelerometer reading and its FFT.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/afterinit.png
   :align: center

ADXL355 EVB GUI FUNCTIONS
=========================

This part digs deeper into the functionality of :adi:`ADXL355 <en/products/adxl355.html>` through the GUI functions.

ACCELEROMETER DATA AND FFT
--------------------------

The accelerometer data and its FFT are readily viewed in the home tab of the GUI.

|image14| Legend:

-  <fc #ff0000>Accelerometer Time Domain Plot</fc>
-  <fc #ffC000>Accelerometer FFT Plot</fc>
-  <fc #4682b4>Statistics</fc>
-  <fc #008000>Axis Toggle Buttons</fc> - This toggles which axis/axes you would want to view.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/guizaxistoggle.png
   :align: center

-  <fc #ffa500>Amplitude/Logarithm Button</fc> - This changes the FFT plot view in Amplitude or Logarithmic Form
-  <fc #800080>Noise/Acceleration Button</fc> - This switches the FFT plot from the acceleration FFT or Noise FFT.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/guilognoise.png
   :align: center

BOARD ORIENTATION
~~~~~~~~~~~~~~~~~

The board orientation is situated below. The following markings present the positive axes (with the Z-axis out of the page, towards the viewer)


|image15|

TEMPERATURE
-----------

The plot of the current temperature reading from the board can be accessed by clicking the right arrow as shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/guitemp.png
   :align: center

INCLINOMETER
------------

The GUI has an Inclinometer function. It is accessed by clicking the Inclinometer tab.


|image16|

Offset calibration must be first done (while the board is placed on a flat surface) by clicking the button shown below.


|image17|

Please wait for the process to finish before moving the board.


|image18|

Press *Start Sensing* to start the inclinometer function.


|image19|

The tilt angle of the board appears as a text in the upper right corner and also visualized through the dial on the window. The current acceleration reading of the three axes are displayed at the bottom.


|image20|

The Inclinometer has 4 plane selections which are the:

-  XY Plane
-  YZ Plane
-  XZ Plane
-  XYZ Plane

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/adxl355z_s/inclinometer_plane_selection.png
   :align: center

As an example, with the XY plane selected, the Z-axis must be parallel to the ground (facing the user). Tilting the board clockwise/counter-clockwise would produce the same tilt in the dial.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/adxl355z_s/incwith_setup.png
   :align: center

SELF TEST
---------

The self test feature of the ADXL355 can be accessed by clicking the Self Test Tab.


|image21|

The SelfTest window will appear. By clicking *Start Test*, the self test values will then appear in the blank boxes.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/adxl355z_s/selftestwindw.png
   :align: center

The measured self test values should be around of the typical values found in the data sheet.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/selftestvalues.png
   :align: center

FIFO
----

SETTINGS
--------

The Settings tab gives you an option to vary the current configuration of the accelerometer.


|image22|

Upon clicking the Settings tab, the Settings window will appear.


|image23|

-  <fc #ffc000>Range</fc> - Configures the current range of the accelerometer
-  <fc #ff0000>ODR/LPF</fc> - Sets the Output Data Rate and the Low-Pass Filter corner frequency
-  <fc #ff9933>HPF</fc> - Configures the programmable corner frequency of the digital high-pass filter.
-  <fc #00b050>Update Filter</fc> - Writes the current filter settings to register.
-  <fc #0070c0>User Offset</fc> - Displays the User Offset option.
-  <fc #7030a0>Configure Activity</fc> - Shows the Configure Activity option.
-  <fc #000000>Accelerometer/Temperature data</fc> - Toggles the display of read data from the accelerometer. Pauses the graphing of the selected data turned off.
-  <fc #CC9900>Reset</fc> - Resets the settings of the accelerometer.
-  <fc #00b0f0>Register</fc> - This tab gives you the option to read/write registers of the accelerometer.
-  <fc #ff66ff>Logging</fc> - Contains the options for data logging

ODR/LPF
~~~~~~~

Here are the available pairs of Output Data Rate and Low Pass Filter Frequencies:

-  4 kHz / 1 kHz
-  2 kHz / 500 Hz
-  1 kHz / 250 Hz
-  500 Hz / 125 Hz
-  250 Hz / 62.5 Hz
-  125 Hz/ 31.5 Hz
-  31.25 Hz / 7.813 Hz
-  15.625 Hz / 3.906 Hz
-  7.813 Hz / 1.953 Hz
-  3.906 Hz / 0.977 Hz

HPF
~~~

The corner frequencies available for the High Pass Filter are:

-  24.7E-4 × ODR
-  6.2084 × ODR
-  1.5545 × ODR
-  0.3862 × ODR
-  0.0954 × ODR
-  0.0238 × ODR

USER OFFSET
~~~~~~~~~~~

The user offset is enabled and set by clicking the button corresponding to it. After that, a window with options will appear. Clicking the *OFF* button would enable the typing of values to the text boxes. The *Update* button is clicked afterwards.


|image24|

CONFIGURE ACTIVITY
~~~~~~~~~~~~~~~~~~

The configuration of activity detection is started by clicking the button next to it. Just like the user offset, a window with options will also appear. By clicking the *ON/OFF* buttons, the user has an option to select which axis to detect activity. The threshold for this is set by moving the slider to the left or right.


|image25|

REGISTER
~~~~~~~~

In the register tab, a user can read/write from/to a single address in the Single Read/Write Value tab by entering the hexadecimal register address and clicking the *Read* or *Write* button.


|image26|

In the All Registers tab, all the current values of the registers could be read by pressing the *Read All* button.


|image27|

The register address and values are then displayed in Hexadecimal form.


|image28|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/step3wiki.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/step5wiki.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/oldiseb1.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/oldiseb2.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/oldiseb3.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/comportold1.png
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/comportold2.png
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/devicemanager.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/runarmwsd.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/click_start.png
   :width: 450px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/sw1sw2.png
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/push_sw2.png
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/evbstart.png
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/guihometab.png
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/boardorient.png
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/guiinctab.png
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/guiincloffset.png
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/gui_inc_wait.png
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/guistartsensing.png
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/adxl355z_s/guiinctilt.png
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/adxl355z_s/selftest.png
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/settingstab.png
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/settingstabexplained.png
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/gui_user_offset.png
.. |image25| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/inactivty.png
.. |image26| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/regisetr.png
.. |image27| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/readallreg.png
.. |image28| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/hexaddr_hex_val.png
