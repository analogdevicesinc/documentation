DragonBoard410C User Guide
==========================

Setting up the system
---------------------

Required hardware
~~~~~~~~~~~~~~~~~

-  :adi:`AD-96TOF1-EBZ development kit <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ad-96tof1-ebz.html>`
-  `DragonBoard410c <https://www.96boards.org/product/dragonboard410c/>`__
-  DragonBoard410c 12V power supply (e.g. AK-ND-49)
-  To run the system in standalone mode, besides the accessories that are provided in the AD-96TOF1-EBZ box you'll need an additional HDMI cable to connect to a monitor and a USB keyboard and mouse

Power on sequence
~~~~~~~~~~~~~~~~~

-  Plug the SD card that came in the AD-96TOF1-EBZ box into the DragonBoard410c SD card slot. To benefit from the most recent software updates it is highly recommended to update the SD card with the `latest SD card image <https://github.com/analogdevicesinc/aditof_sdk#supported-embedded-platforms>`__
-  Make sure that switch S6 on the DragonBoard410C is set to SD BOOT (position 2 ON, all others OFF)
-  connect the HDMI cable from the monitor to the DragonBoard410c HDMI connector
-  connect a USB mouse and keyboard to the DragonBoard410c. It's possible to use either a mouse & keyboard combo or a separate mouse and keyboard
-  connect the 5V power supply to the camera board and set the camera power switch S2 to on. Once the camera board is powered up the DS1 LED will turn on
-  connect the 12V power supply to the DragonBoard 410c. Once power is connected to the DragonBoard the system will boot the Linux OS from the SD card.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/db410c_standalone.jpg
   :alt: DB410C connections
   :align: center
   :width: 400px

Power off sequence
~~~~~~~~~~~~~~~~~~

-  Open a terminal and type **sudo halt**. This will safely turn off the OS on DragonBoard410c and ensure that the SD card is properly unmounted
-  Remove the 12V supply from the DragonBoard410c
-  Set the camera board power switch to off

Troubleshooting
~~~~~~~~~~~~~~~

-  Linux does not boot

   -  Sometimes the SD card is not read correctly and this prevents the system to boot. Reset the system by removing and reapplying power to the DragonBoard410c
   -  The SD card is corrupted and this prevents the system from booting. Reflash the SD card with the SD card image.

--------------

Running the evaluation application
----------------------------------

Once Linux boots you'll see on the HDMI monitor the Linux desktop and on the top left corner a shortcut to the evaluation application. Double clicking on the icon will start the evaluation application. A console window will open to show the application's status and, after a few seconds, the evaluation application GUI will be displayed.

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~

-  The demo application hangs after closing the main window

   -  Due to some limitations the application always hangs if it is closed using the regular X button from the window top bar (title bar). To avoid this unpleasant hang, we've made available a second X button in the top right corner right above the title bar that can be used to safely close the demo application. We hope this to be a temporary workaround.


.. image:: https://wiki.analog.com/_media/navigation AD-96TOF1-EBZ#none#./
   :alt: Overview#none#
