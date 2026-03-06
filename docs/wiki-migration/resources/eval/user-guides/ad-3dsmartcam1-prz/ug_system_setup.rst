AD-3DSMARTCAM1-PRZ User Guide
=============================

To get your new camera up and running there are a few steps to go through in order to connect the camera to your PC, update the camera's software and then start receiving data and using the installed applications.

| |image1| After powering up the camera the blue LED on the top right corner of the camera's front will light up and the system will start booting the installed Linux OS. The boot process takes about 30 seconds, after which the camera will expose a WiFi access point named **ADI_Smart_Camera** and having the password *ADI_Smart_Camera*.
| There are two ways to connect to the camera from a PC:

-  Connect the PC to the camera's WiFi access point. In this case the camera will always have the **172.16.1.1** IP address.
-  Connect the camera to the local Ethernet network. In this case the camera will use DHCP to obtain a dynamic IP address.

The camera can now be accessed via *ssh* using the camera's IP address and **username** *analog* and **password** *analog*.


|image2|

Once connected to the camera it's time to start updating the installed software package. For this please make sure the camera is connected to the internet using the wired Ethernet connection, **the system date is correct** and then follow the steps below. These will get the latest Analog Devices ToF SDK from github and build it, and then it will install VNC server and a few demo applications. Please monitor the process since there will be a few places where user input is required.

::

   analog@adi-smart-camera:~$ cd Workspace/aditof_sdk
   analog@adi-smart-camera:~/Workspace/aditof_sdk/$ git checkout .
   analog@adi-smart-camera:~/Workspace/aditof_sdk/$ git fetch
   analog@adi-smart-camera:~/Workspace/aditof_sdk/$ git pull
   analog@adi-smart-camera:~/Workspace/aditof_sdk$ cd scripts/3dsmartcam1/
   analog@adi-smart-camera:~/Workspace/aditof_sdk/scripts/3dsmartcam1$ ./sdk_update.sh
   analog@adi-smart-camera:~/Workspace/aditof_sdk/scripts/3dsmartcam1$ sh ./apps_update.sh
   analog@adi-smart-camera:~/Workspace/aditof_sdk/scripts/3dsmartcam1$ sudo reboot

After the system restarts the easiest way to interact with the camera is via VNC. For this the `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`__ application needs to be installed on your PC.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-3dsmartcam1-prz/vnc_viewer.png
   :alt: VNC Viewer
   :width: 400px

Once VNC Viewer is connected the camera's Linux Desktop will be displayed and you can start interacting with it. On the desktop there are a few shortcuts to the aditof-demo evaluation application and to the box dimensioning, people detection and robot navigation applications.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-3dsmartcam1-prz/jetson_desktop.png
   :alt: Linux Desktop
   :width: 600px

--------------

.. image:: https://wiki.analog.com/_media/navigation AD-3DSMARTCAM1-PRZ#none#./
   :alt: Overview#none#

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fxtof1-ebz/smart_camera_wifi.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-3dsmartcam1-prz/ssh_connect.png
   :width: 500px
