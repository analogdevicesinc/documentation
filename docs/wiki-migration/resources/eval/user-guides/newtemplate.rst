**\*BOARD_NAME**\ \*
====================

Introduction
------------

| The `board_name <https://wiki.analog.com/board_name>`__ is an 18-bit, 15 MSPS, 2 ppm linear data acquisition system with an easy to drive input impedance of 1.1 kΩ. The analog input range is 8.096 V peak-to-peak and can be driven in either single-ended or differential mode, providing flexibility for many different applications.
| The circuit is in field programmable gate array (FPGA) mezzanine card (FMC) form factor, powered with 12 V either from the FMC connector or an external supply. The digital interface uses serial low voltage differential signaling (LVDS), minimizing the input/output requirements and enabling easy integration with other FPGA designs.
| A separate data clock eases the timing requirements of the host FPGA. An on-board 120 MHz clock is forwarded to the FPGA and a CONVERT retiming flip-flop reduces jitter from the convert signal of the FPGA.
| |image1|

--------------

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/newtemplate/mock_diagram.png
   :align: center
   :width: 600px

--------------

What's Inside
-------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/newtemplate/kit_contents.png
   :align: center
   :width: 600px

--------------

Specifications
--------------

======================== ========================================
Power supply             
======================== ========================================
External power           12 V\ :sub:`DC` @ 2 A
Operating Conditions     
Temperature Range        -25\ :sup:`o`\ C to 60\ :sup:`o`\ C
Certifications           
Safety, EMC, Environment conforms to necessary regional standards
Mechanical Specs         
Dimensions

|image2|

======================== ========================================

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

A set of applications have been developed for the `board_name <https::`Access the open source ADI 3D ToF SDK to get started </wiki.analog.com/board_name>` to showcase the system's capabilities, but also to be used as a starting point for custom development.

Application # 1
~~~~~~~~~~~~~~~

|youtube>G-9UfaZXUCk| Knowing the precise position of people in a space has many use cases for robotics, building management, healthcare and AV applications. The 3D Smart Camera enables precise detection and tracking of people in the 3D space as well as detecting the objects people are touching, carrying or sitting on and the boundaries of the space such as the floor, walls and ceiling.

|

.. note::

   `Box dimensioning app <https://github.com/robotics-ai/tof_process_public/tree/main/box_measure>`__


Application # 2
~~~~~~~~~~~~~~~

|youtube>-CErH6ROli8| Knowing the precise position of people in a space has many use cases for robotics, building management, healthcare and AV applications. The 3D Smart Camera enables precise detection and tracking of people in the 3D space as well as detecting the objects people are touching, carrying or sitting on and the boundaries of the space such as the floor, walls and ceiling.

|

.. note::

   `People detection and tracking app <https://github.com/robotics-ai/tof_process_public/tree/main/door_sense>`__


Application # 3
~~~~~~~~~~~~~~~

|youtube>XKTGsVNyvrg| Autonomous robots need to be able to "see" the objects and people which are around them to be able to move inside a space and accomplish their tasks without bumping into things or injuring people. By combining the people and objects detection with real time objects dimensioning and positioning is space, the 3D Smart Camera can enable an autonomous robot to navigate safely in an environment.

|

.. note::

   `Robot navigation app <https://github.com/robotics-ai/tof_process_public/tree/main/slam>`__


Application # 4
~~~~~~~~~~~~~~~

|youtube>mL542eUw_dg| This application shows how the 3D and IR data can be used to create a 3D map of a space using the ROS RTAB-Map (Real-Time Appearance-Based Mapping), an RGB-D SLAM approach based on a global loop closure detector with real-time constraints. Applications include robot autonomous navigation and 3D space reconstruction.

|

.. note::

   `Space mapping app <https://github.com/robotics-ai/tof_process_public/tree/main/3d_mapping>`__


--------------

Getting your system up and running
----------------------------------

.. tip::

   The complete instructions for setting up the `board_name <https://wiki.analog.com/board_name>`__ for circuit evaluation can be found here: :doc:`BOARD NAME User Guide </wiki-migration/resources/eval/user-guides/newtemplate/hardware>`


--------------

Compliance
----------

.. important::

   This device complies with International Standards IEC 60825-1:2014 & 2007 for a Class 1 laser product. This device also complies with 21 CFR 1040.10 and 1040.11 except for deviations pursuant to Laser Notice No. 50, dated June 24, 2007. Only use Software and Firmware updates that are specifically provided for this solution.


--------------

Help and Support
----------------

For questions and more information, please contact us on the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone 3D ToF Depth Sensing <depth-perception-ranging-technologies/lidar-solutions/3d-tof-depth-sensing>`


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0577/cn0577_1.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-3dsmartcam1-prz/samxl.png
   :width: 400px
.. |youtube>G-9UfaZXUCk| image:: https://wiki.analog.com/_media/youtube>G-9UfaZXUCk
.. |youtube>-CErH6ROli8| image:: https://wiki.analog.com/_media/youtube>-CErH6ROli8
.. |youtube>XKTGsVNyvrg| image:: https://wiki.analog.com/_media/youtube>XKTGsVNyvrg
.. |youtube>mL542eUw_dg| image:: https://wiki.analog.com/_media/youtube>mL542eUw_dg
