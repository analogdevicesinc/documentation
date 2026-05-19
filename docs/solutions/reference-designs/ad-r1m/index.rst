.. _ad-r1m:

AD-R1M
======

Open Mobile Robot Platform Reference Design
""""""""""""""""""""""""""""""""""""""""""""

.. toctree::
   :hidden:

   hardware-assembly

Introduction
------------

.. figure:: res/robot-hardware.png
   :width: 25em
   :align: right

   AD-R1M Open Mobile Robot Platform

The AD-R1M Open Mobile Robot Platform Reference Design is a modular, extensible,
and fully open-source framework developed to accelerate the design, prototyping,
and deployment of autonomous mobile robots.

This reference design integrates key hardware and software components including
motor control, sensor fusion, localization, navigation, and communication into a
cohesive platform that supports rapid development and experimentation.

The platform supports two processing configurations:

- **Raspberry Pi 5** with ADI Kuiper2 for standard deployments
- **NVIDIA Jetson AGX Orin** for GPU-accelerated workloads and visual SLAM

Features
--------

- Open-source hardware and software design
- ROS 2 Humble compatible with modular node architecture
- Differential drive mobile base with encoder feedback
- Integrated ADI IMU (:adi:`ADIS16470`) for precision localization
- ADI Time-of-Flight camera (:adi:`EVAL-ADTF3175`) for 2D/3D perception
- Battery Management System with CAN-based monitoring
- Support for NVIDIA Jetson AGX Orin for GPU-accelerated workloads
- Zephyr RTOS firmware on embedded motor and BMS controllers
- CRSF/ELRS remote control with safety killswitch
- Gazebo simulation environment included

Applications
------------

- Mobile robotics research and development
- Autonomous navigation and SLAM algorithm development
- Warehouse and logistics automation prototyping
- Educational robotics platforms
- Multi-robot setup management research

Hardware Components
-------------------

The AD-R1M platform is built from modular ADI reference design boards:

.. list-table::
   :header-rows: 1
   :widths: 15 25 40 20

   * - Component
     - Board
     - Description
     - Documentation
   * - Motor Control
     - .. image:: res/adrd3161.jpg
          :width: 120px

       :adi:`ADRD3161-01Z`
     - CAN-based motor driver with encoder interface (x2)
     - :doc:`ADRD3161-01Z </solutions/reference-designs/adrd3161-01z/index>`
   * - Power Distribution
     - .. image:: res/adrd4161_board.jpg
          :width: 120px

       :adi:`ADRD4161-01Z`
     - Robotics perception compute carrier for Raspberry Pi
     - :doc:`ADRD4161-01Z </solutions/reference-designs/adrd4161-01z/index>`
   * - Battery Management
     - .. image:: res/adrd5161.png
          :width: 120px

       :adi:`ADRD5161-01Z`
     - BMS board with CAN interface (3S or 12S variants)
     - :doc:`ADRD5161-01Z </solutions/reference-designs/adrd5161-01z/index>`
   * - IMU
     - :adi:`ADIS16470`
     - High-precision 6-axis IMU for localization
     - `imu_ros2 docs <https://analogdevicesinc.github.io/imu_ros2/>`__
   * - ToF Camera
     - .. image:: res/eval_adtf3175.png
          :width: 120px

       :adi:`EVAL-ADTF3175`
     - Time-of-Flight depth camera for perception
     - `adi_3dtof <https://analogdevicesinc.github.io/adi_ros2/humble/adi_3dtof_adtf31xx/index.html>`_


System Applications
-------------------

SLAM Mapping
~~~~~~~~~~~~

The AD-R1M uses the ADIS16470 IMU and EVAL-ADTF3175 ToF camera for real-time
Simultaneous Localization and Mapping (SLAM). The platform can supports multiple
SLAM algorithms.

.. figure:: res/do_mapping.gif
   :width: 500px
   :align: center

   SLAM mapping with AD-R1M

Nav2 Navigation
~~~~~~~~~~~~~~~

Autonomous navigation is powered by the ROS 2 Nav2 stack, providing path planning,
obstacle avoidance, and waypoint following. The platform integrates sensor fusion
from the IMU and depth camera.

.. figure:: res/navigate.gif
   :width: 500px
   :align: center

   Nav2 stack navigation with AD-R1M

.. figure:: res/amr_elevator.gif
   :width: 500px
   :align: center

   AD-R1M demo navigation with elevator payload

Multi-robot Fleet
~~~~~~~~~~~~~~~~~

The AD-R1M supports multi-robot deployments using `ROS 2 Zenoh middleware
<https://docs.ros.org/en/humble/Installation/RMW-Implementations/Non-DDS-Implementations/Working-with-Zenoh.html>`_
and namespacing for swarm robotics management. Fleet coordination enables
sensor data aquisition, task distribution, and control across multiple
robots operating in shared environments.

.. figure:: res/amr_multi_robot.gif
   :width: 500px
   :align: center

   Multi-robot control with ROS 2 Zenoh middleware

Gazebo Simulation
~~~~~~~~~~~~~~~~~

Full simulation environment for development and testing without hardware.
The Gazebo models include sensor simulation for the ToF camera
and IMU, enabling algorithm development and validation before deployment.


Capability Expansion
--------------------

NVIDIA Jetson AGX Orin + cuVSLAM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For GPU-accelerated workloads and visual SLAM, the AD-R1M supports NVIDIA Jetson
AGX Orin integration with NVIDIA Isaac ROS cuVSLAM and Intel RealSense cameras.

**Key Components:**

- **NVIDIA Jetson AGX Orin** - High-performance edge AI compute
- **NVIDIA Isaac ROS** - GPU-accelerated ROS 2 packages
- **cuVSLAM** - CUDA-accelerated visual SLAM
- **Intel RealSense D455** - RGB-D camera for visual odometry

.. figure:: res/ad_r1m_and_cuvslam_demo.gif
   :width: 500px
   :align: center

   AD-R1M with NVIDIA cuVSLAM visual odometry

.. figure:: res/simulation_demo.gif
   :width: 500px
   :align: center

   Gazebo simulation with cuVSLAM

The Jetson AGX Orin is powered by the ADRD5161 BMS and communicates with the
AD-R1M via Ethernet using ROS 2 middleware wrappers.

.. list-table::
   :widths: 33 33 33

   * - .. image:: res/robot_power_connection.jpg
          :width: 200px

       BMS power connection
     - .. image:: res/robot_ethernet_connection.jpg
          :width: 200px

       RPi Ethernet
     - .. image:: res/orin_ethernet_and_power.jpg
          :width: 200px

       AGX Orin power & Ethernet

See the `AGX Orin cuVSLAM Guide <https://analogdevicesinc.github.io/ad_r1m_ros2/agx-orin-cuvslam/index.html>`__
for full setup instructions.

GMSL Camera Integration
~~~~~~~~~~~~~~~~~~~~~~~

The AD-R1M platform can be extended with ADI GMSL camera boards for enhanced
perception capabilities in robotics and autonomous systems:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Board
     - Description
   * - :doc:`AD-GMSL716MIPI-EVK </solutions/reference-designs/ad-gmsl716mipi-evk/index>`
     - GMSL2-to-MIPI deserializer for multi-camera vision systems
   * - :doc:`AD-GMSL717MIPI-EVK </solutions/reference-designs/ad-gmsl717mipi-evk/index>`
     - GMSL2 serializer for Raspberry Pi cameras
   * - :doc:`AD-GMSL792MIPI-EVK </solutions/reference-designs/ad-gmsl792mipi-evk/index>`
     - GMSL3/2 quad deserializer for surround-view applications
   * - :doc:`AD-GMSL793MIPI-EVK </solutions/reference-designs/ad-gmsl793mipi-evk/index>`
     - GMSL3/2 octal deserializer for advanced multi-camera systems

Image Processing
~~~~~~~~~~~~~~~~

The ``ad_r1m_image_processing`` ROS 2 package provides real-time image processing
capabilities for GMSL camera streams:

**Floor Segmentation** - Uses FastSAM (Fast Segment Anything Model) to identify
traversable floor regions, enabling safe navigation path planning.

.. figure:: res/segmentation_result.gif
   :width: 500px
   :align: center

   Floor segmentation with FastSAM

**Object Detection** - YOLO-based real-time obstacle detection with bounding boxes
and class labels for obstacle avoidance.

.. figure:: res/detection_result.gif
   :width: 500px
   :align: center

   Object detection with YOLO

See the `ad_r1m_image_processing package <https://github.com/analogdevicesinc/ad_r1m_ros2/tree/image_processing_pkg/ad_r1m_image_processing>`_
for setup and configuration.


Getting Started
---------------

Full documentation and guides are available in the project repository:

- :doc:`Hardware Assembly Guide <hardware-assembly>`
- `Quick Start Guide <https://analogdevicesinc.github.io/ad_r1m_ros2/quick-start-guide.html>`__
- `Hardware Setup Guide <https://analogdevicesinc.github.io/ad_r1m_ros2/hardware-guide.html>`__
- `Software Guide (ROS 2, Docker) <https://analogdevicesinc.github.io/ad_r1m_ros2/software-guide.html>`__
- `Use Cases and Examples <https://analogdevicesinc.github.io/ad_r1m_ros2/use-cases.html>`__

ADI ROS 2 Ecosystem
-------------------

The `adi_ros2 <https://github.com/analogdevicesinc/adi_ros2>`_ meta-repository
streamlines the use of ADI packages within ROS 2 by providing a single entry point
for all ADI-supported packages. It includes CI scripts for building system
dependencies from source, centralized within a Docker wrapper for reproducible
builds. See the `official documentation <https://analogdevicesinc.github.io/adi_ros2/>`_
for getting started.

**Related ROS 2 Packages:**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Package
     - Description
   * - `imu_ros2 (GitHub) <https://github.com/analogdevicesinc/imu_ros2>`__
     - ROS 2 driver for ADI IMUs (ADIS16470, ADIS16475, etc.)
   * - `adi_3dtof_adtf31xx <https://github.com/analogdevicesinc/adi_3dtof_adtf31xx>`__
     - ROS 2 driver for ADI Time-of-Flight cameras (ADTF3175D)
   * - `ad_r1m_ros2 <https://github.com/analogdevicesinc/ad_r1m_ros2>`__
     - AD-R1M platform packages and documentation

Resources
---------

- AD-R1M Repository: `ad_r1m_ros2 <https://github.com/analogdevicesinc/ad_r1m_ros2>`__
- ADI ROS 2 Meta-repo: `adi_ros2 <https://github.com/analogdevicesinc/adi_ros2>`_

Related Products
----------------

**Hardware Modules:**

- :adi:`ADRD3161-01Z` - Motor control board
- :adi:`ADRD4161-01Z` - Robotics perception compute carrier
- :adi:`ADRD5161-01Z` - Battery management system

**Sensors:**

- :adi:`ADIS16470` - High-precision 6-axis IMU
- :adi:`ADTF3175D` - Time-of-Flight depth camera

**GMSL Camera Boards:**

- :adi:`AD-GMSL716MIPI-EVK` - GMSL2-to-MIPI deserializer
- :adi:`AD-GMSL717MIPI-EVK` - GMSL2 serializer
- :adi:`AD-GMSL792MIPI-EVK` - GMSL3/2 quad deserializer

**Supporting ICs:**

- :adi:`MAX32662` - Microcontroller (ADRD4161)
- :adi:`MAX96716A` - GMSL2 deserializer (AD-GMSL716MIPI-EVK)

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`sw-interface-tools/robot-operating-system-ros-sdk`.
