EVAL-ADTF3175D-NXZ Startup Guide
================================

Kit Contents
------------

-  ADTF3175-NXZ Evaluation Module

   -  ADTF3175 Imager Module
   -  i.MX8 M Plus SOM (SolidRun)
   -  Camera Interface Board
   -  ADSD3500 Interposer board

-  16GB flashed microSD card (Inserted in module sd card slot)
-  USB-C to USB-C cable. Supports PD 2.0, and USB 3.1
-  Tripod

.. image:: https://wiki.analog.com/_media/adtf_eval_whatsinthebox.jpg
   :align: center
   :width: 400px

Software Download
-----------------

-  GUI Install Guide: :doc:`Link </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-software-installation>`

Startup
-------

-  Remove camera from packaging
-  Mount camera. Orientation shown in image below

.. image:: https://wiki.analog.com/_media/img_01812.jpg
   :align: center
   :width: 400px

-  Connect USB-C cable to module

.. image:: https://wiki.analog.com/_media/capture33.png
   :align: center
   :width: 400px

-  Connect USB-C to laptop (for additional connection options please check "Connectivity" section)
-  The following leds must turn on before moving to next steps:

   -  Green led under USB-C connector
   -  Blinking led on NXP SOM
   -  Blue led on ADSD3500 interposer board

-  Look at available network connections, an 'Unidentified Network' with no internet access must show up, as shown in the image below

.. image:: https://wiki.analog.com/_media/blurrednetworks.png
   :align: center

-  Run :doc:`GUI </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-gui>`

.. image:: https://wiki.analog.com/_media/img_0186.jpg
   :align: center
   :width: 400px

Using the wall adaptor to power up camera
-----------------------------------------

It is possible to power up the camera by using an external wall adaptor. As long as the cable has USB-C on one side and the wall adaptor can support at least 5W.

In this case the USB-C cable cannot be used to transfer data over to the PC. The user will have to communicate through an IX ethernet cable as the one shown below: - https://www.digikey.com/en/products/detail/harting/33480147826020/14556483

Setup as follows:

-  Connect wall adaptor with USB-C cable to power outlet and camera
-  Connect IX ethernet cable to router and camera

.. image:: https://wiki.analog.com/_media/wiki-adtf3175d-side-connectors.png
   :align: center
   :width: 400px

-  Ensure your laptop is connected to router (WIFI or Ethernet is okay)

   -  Please note there will be frame drops by using WIFI or Ethernet in comparison to USB-C

-  Find IP address of camera (Multiple options)

   -  Connect to router and find IP address of camera (192.168.0.1 can usually take you to your router menu)
   -  Connect to NXP via micro-USB cable and get ip address

      -  For instructions please check :doc:`Connecting to adtf-3175x </wiki-migration/resources/eval/user-guides/eval-adtf3175x-access>`
      -  Once logged in run 'ip addr' command and find IP address as shown in red below. In this case the IP address is 192.168.0.101

.. image:: https://wiki.analog.com/_media/get_ip_from_nxp.png
   :align: center
   :width: 600px

-  To run the GUI change 'camera_ip' parameter to IP found above in the tof-tools.config file in "TOF_Evaluation_ADTF3175D-RelX.X.X\\bin" folder (Open with notepad)

.. image:: https://wiki.analog.com/_media/tof_tools_modification.png
   :align: center
   :width: 300px

-  Run GUI

Troubleshooting
---------------

-  Visit :doc:`Troubleshooting Guide </wiki-migration/resources/eval/user-guides/aditofgui_ts>`
