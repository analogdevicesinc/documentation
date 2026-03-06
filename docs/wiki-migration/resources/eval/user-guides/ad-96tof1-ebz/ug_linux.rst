Linux User Guide
================

.. include:: ug_host_system_setup.rst

Enable the USB connection to the host PC
----------------------------------------

-  After the DragonBoard boots up press the S3 button on the camera board. This will start on the DragonBoard the application that manages the USB host interface
-  Once the USB connection is active the DS4 LED will light up on the camera board and the USB camera driver will be loaded on the PC enabling the communication between the host PC and the camera system
-  To check if the camera has been recognized by the host PC, open up a terminal and run the *dmesg* command. The ADI TOF DEPTH SENSOR name should come up in the list displayed by *dmesg*.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/linux_db410c_usb.png
   :alt: Linux driver
   :align: center
   :width: 800px

Troubleshooting
---------------

-  The PC does not load the USB driver after pressing the S3 button on the camera board

   -  Press S3 so that DS4 turns off, reconnect the USB cable to the PC into a different USB port, press S3 again so that DS4 turns on
   -  Restart the DragonBoard410c while the USB cable is still connected to the host PC

--------------

Ethernet connection
-------------------

-  The IP address of the target is needed in order to use the ethernet connection. To find the IP address, connect a keyboard, a mouse and a monitor to the camera. After booting open a terminal and type either sudo ifconfig or ip addr command.
-  There are two examples that show how to use the ethernet connection: **aditof-demo** and **first-frame-ethernet**.
-  For **first-frame-ethernet** example, if the IP address of the target is *192.168.1.110* the run command should be: ``./first-frame-ethernet "192.168.1.110"``
-  In the **aditof-demo** example, choose to connect via ethernet from the UI. After the *Ethernet* checkbox is selected input the IP and press the button *Connect*.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/aditof-demo_ethernet.png
   :alt: aditof-demo connect through ethernet
   :align: center
   :width: 300px

--------------

Running the evaluation application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can build the evaluation application from source as part of the SDK build process described on github.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/aditof_demo.png
   :alt: aditof-demo
   :align: center
   :width: 800px

When starting the application, a terminal window will open to display status messages (also warning and error messages, in case there are any issues). Shorty the main window will show up.

The evaluation application allows to do live streaming of depth and IR data as well as recording the depth and IR data and playing back from a file. The depth data is displayed as a color map ranging from warm to cold colors as the distance from the camera increases. A point in the middle of the depth image shows the distance in mm to the target.

There are 3 operating modes that determine the range of the system:

-  Near - 25cm to 80cm
-  Medium - 30cm to 4.5m (Rev.B: 80cm to 3m)
-  Far - 300cm to 600cm

When in a certain operating mode the system will measure distances outside of the mode's range but those will not be accurate.

The system is factory calibrated to achieve high accuracy in all the operating modes for indoor environments. It is possible to recalibrate the system for your specific operating conditions by using the calibration procedure and tools provided :doc:`here </wiki-migration/resources/eval/user-guides/ad-96tof1-ebz/calibration>`.

The evaluation application also displays the temperature in deg C of the camera (AFE) and laser boards as read from the temperature sensors installed on each board.

The framerate at which data is acquired from the system is constantly updated on the GUI. The camera board outputs data at 30 frames per second (fps), but due to USB connection limitations, the host PC acquires the frames at a lower rate.

Enabling the point cloud display in aditof-demo
-----------------------------------------------

-  The demo application has the capability to display a point cloud image if it detects an OpenCV module called viz.

Unfortunately OpenCV does not provide binaries for this module so a manual build is needed. The steps required to install OpenCV and include it in the project are presented here: :git-aditof_sdk:`Windows <doc/windows/build_instructions.md#enabling-the-point-cloud-display-in-aditof-demo>` :git-aditof_sdk:`Linux <doc/linux/build_instructions.md#enabling-the-point-cloud-display-in-aditof-demo>`

-  If aditof-demo finds all the OpenCV required modules a button in the interface will allow you to display the point cloud. By toggling the button a separate window will appear.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/aditof_demo_pointCloud.png
   :alt: aditof-demo
   :align: center
   :width: 800px

.. important::

   Due to the limited computation speed of DragonBoard410c it is recomended to enable the point cloud only in the desktop sdk


Troubleshooting
---------------

-  The demo application hangs after closing the main window

   -  Due to some limitations the application always hangs if it is closed using the regular X button from the window top bar (title bar). To avoid this unpleasant hang, we've made available a second X button in the top right corner right above the title bar that can be used to safely close the demo application. We hope this to be a temporary workaround.


.. image:: https://wiki.analog.com/_media/navigation AD-96TOF1-EBZ#none#./
   :alt: Overview#none#
