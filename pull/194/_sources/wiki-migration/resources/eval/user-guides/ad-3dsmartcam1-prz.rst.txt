AD-3DSMARTCAM1-PRZ
==================

.. important::

   This system has reached its end of life and cannot be purchased anymore.


Introduction
------------

| The :adi:`AD-3DSMARTCAM1-PRZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/AD-SMARTCAM1-PRZ.html>` is a 2D & 3D machine vision solution with AI edge processing capabilities. It can be used for implementing advance machine vision applications for different industry segments including logistics, robotics, agriculture and people activity monitoring.
| |3D Smart Camera|

--------------

What's inside
-------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fxtof1-ebz/exploded_view.png
   :alt: 3D Smart Camera Exploded View
   :width: 600px

--------------

Specifications
--------------

+--------------------------------+---------------------------------------------------------------------------------------------+
| Vision sensors                 |                                                                                             |
+================================+=============================================================================================+
| 3D ToF sensor                  | FoV 90x60, Range 3m, Resolution 640x480 @ 30fps                                             |
+--------------------------------+---------------------------------------------------------------------------------------------+
| RGB sensor                     | FoV 128x68, Range 6m, Resolution 1920x1080 @ 30fps                                          |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Connectivity                   |                                                                                             |
+--------------------------------+---------------------------------------------------------------------------------------------+
| WiFi                           | 802.11a/b/g/n/ac, 867Mbps with dual stream in 802.11n, 2x2 Access Points with MIMO standard |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Ethernet (optional)            | 1xRJ45 10M/100M/1G self-adaptive Ethernet port                                              |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Bluetooth 5.0                  | Bluetooth Class 1 and Class 2 transmitter operation, Adaptive frequency hopping             |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Power supply                   |                                                                                             |
+--------------------------------+---------------------------------------------------------------------------------------------+
| External power                 | 12V DC @ 2A                                                                                 |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Power over Ethernet (optional) | PoE+ IEEE802.3-2012, max 20W                                                                |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Operating Conditions           |                                                                                             |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Temperature Range              | -25\ :sup:`o`\ C to 60\ :sup:`o`\ C                                                         |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Operating Class                | IP66                                                                                        |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Computing Resources            |                                                                                             |
+--------------------------------+---------------------------------------------------------------------------------------------+
| CPU                            | Quad-core ARM A57 @ 1.43 GHz                                                                |
+--------------------------------+---------------------------------------------------------------------------------------------+
| GPU                            | 128-core Maxwell                                                                            |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Memory                         | 4 GB 64-bit LPDDR4 25.6 GB/s                                                                |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Storage                        | 16GB eMMC                                                                                   |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Certifications                 |                                                                                             |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Safety, EMC, Environment       | Eye safe and conforms to necessary regional standards                                       |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Mechanical Specs               |                                                                                             |
+--------------------------------+---------------------------------------------------------------------------------------------+
| Dimensions                     | |image2|                                                                                    |
+--------------------------------+---------------------------------------------------------------------------------------------+

--------------

Development
-----------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/sdk_stack.png
   :alt: SDK Architecture
   :align: right
   :width: 300px

An open-source SDK that accompanies the hardware platform enables you to configure the system and extract depth and RGB data from the camera on the system of your choice. Windows and Linux support are built into the SDK as well as sample code and wrappers for various languages including Python, C/C++ and MATLAB. The SDK also integrates with 3rd party technologies like OpenCV and RoS.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fxtof1-ebz/logos.png
   :alt: Bindings
   :width: 500px

.. admonition:: Download
   :class: download

   :git-aditof_sdk>`__


--------------

Applications
------------

A set of applications have been developed for the 3D Smart Camera to showcase the system's capabilities but also to be used as a starting point for custom development.

Box dimensioning
~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/youtube>G-9UfaZXUCk
   :alt: youtube>G-9UfaZXUCk
   :align: right

Detecting and measuring the size of boxes is the base of many use cases for logistics, industrial and commercial applications. By combining the information received for the 3D and 2D sensors, the 3D Smart Camera can reliably measure boxes of various sizes with an accuracy between 0.5cm and 2cm per each dimension, depending on the operating conditions and box characteristics.

|

.. note::

   `Box dimensioning app <https::`Access the open source ADI 3D ToF SDK to get started </github.com/robotics-ai/tof_process_public/tree/main/box_measure>`


People detection and tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|youtube>-CErH6ROli8| Knowing the precise position of people in a space has many use cases for robotics, building management, healthcare and AV applications. The 3D Smart Camera enables precise detection and tracking of people in the 3D space as well as detecting the objects people are touching, carrying or sitting on and the boundaries of the space such as the floor, walls and ceiling.

|

.. note::

   `People detection and tracking app <https://github.com/robotics-ai/tof_process_public/tree/main/door_sense>`_


Robot navigation
~~~~~~~~~~~~~~~~

|youtube>XKTGsVNyvrg| Autonomous robots need to be able to "see" the objects and people which are around them to be able to move inside a space and accomplish their tasks without bumping into things or injuring people. By combining the people and objects detection with real time objects dimensioning and positioning is space, the 3D Smart Camera can enable an autonomous robot to navigate safely in an environment.

|

.. note::

   `Robot navigation app <https://github.com/robotics-ai/tof_process_public/tree/main/slam>`_


Space mapping
~~~~~~~~~~~~~

|youtube>mL542eUw_dg| This application shows how the 3D and IR data can be used to create a 3D map of a space using the ROS RTAB-Map (Real-Time Appearance-Based Mapping), a RGB-D SLAM approach based on a global loop closure detector with real-time constraints. Applications include robot autonomous navigation and 3D space reconstruction.

|

.. note::

   `Space mapping app <https://github.com/robotics-ai/tof_process_public/tree/main/3d_mapping>`_


--------------

Getting your system up and running
----------------------------------

|Smart Camera Desktop| The 3D Smart Camera provides Gb Ethernet and 2.4GHz / 5GHz WiFi connectivity for interfacing with the outside world. Connecting to the camera from your PC is just as easy as hooking it up to your local wired or WiFi network or connecting to the camera's WiFi access point. Once the connection is alive the camera can be accessed via ssh for command line style interfacing or VNC to get access to the camera's Linux UI.

.. note::

   :doc:`3D Smart Camera User Guide </wiki-migration/resources/eval/user-guides/ad-3dsmartcam1-prz/ug_system_setup>`


--------------

Laser Safety
------------

.. important::

   This device complies with International Standards IEC 60825-1:2014 & 2007 for a Class 1 laser product. This device also complies with 21 CFR 1040.10 and 1040.11 except for deviations pursuant to Laser Notice No. 50, dated June 24, 2007. Only use Software and Firmware updates that are specifically provided for this solution.


--------------

Help and Support
----------------

For questions and more information please contact us on the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone 3D ToF Depth Sensing <depth-perception-ranging-technologies/lidar-solutions/3d-tof-depth-sensing>`


.. |3D Smart Camera| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-3dsmartcam1-prz/ad-3dsmartcam1-przangle1-web.gif
   :width: 400px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-3dsmartcam1-prz/samxl.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-3dsmartcam1-prz/samxl.png
   :width: 400px
.. |youtube>-CErH6ROli8| image:: https://wiki.analog.com/_media/youtube>-CErH6ROli8
.. |youtube>XKTGsVNyvrg| image:: https://wiki.analog.com/_media/youtube>XKTGsVNyvrg
.. |youtube>mL542eUw_dg| image:: https://wiki.analog.com/_media/youtube>mL542eUw_dg
.. |Smart Camera Desktop| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fxtof1-ebz/jetson_desktop.png
   :width: 300px
