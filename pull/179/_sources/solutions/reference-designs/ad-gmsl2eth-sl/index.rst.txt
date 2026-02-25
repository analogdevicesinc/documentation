.. _ad-gmsl2eth-sl:

AD-GMSL2ETH-SL
===============

GMSL2 to 10G Ethernet Edge Compute Platform.

Overview
--------

.. figure:: ad-gmsl2eth-sl.jpg
   :width: 400 px
   :align: left

   AD-GMSL2ETH-SL Evaluation Board

The :adi:`AD-GMSL2ETH-SL` is an edge compute platform enabling low latency
data transfer from eight
:adi:`Gigabit Multimedia Serial Link (GMSL) <en/solutions/gigabit-mulitimedia-serial-link.html>`
interfaces onto a 10 Gb Ethernet link. It targets applications such as
autonomous robots and vehicles that require machine vision and real-time
sensor fusion.

The platform combines the AMD Kria K26 Industrial SoM for embedded processing
with open-source Linux software and FPGA designs, offering a complete
development environment for GMSL-based systems.

Features
--------

- 8 GMSL2 camera interfaces with up to 6 Gbps per channel
- 10 Gbps SFP+ Ethernet interface with IEEE 1588 hardware timestamping
- Embedded processing via AMD Kria K26 Industrial System-on-Module
- Precision Time Protocol (PTP) synchronization capability
- ROS2 compliant
- Open-source Linux software and FPGA design
- Advanced camera triggering and control functions

Applications
------------

- Autonomous vehicles
- Machine vision
- Real-time sensor fusion
- Robotic systems

System Architecture
-------------------

.. figure:: ad-gmsl2eth-sl-block-diagram.png
   :width: 600 px
   :align: center

   AD-GMSL2ETH-SL Simplified Block Diagram

Specifications
--------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Parameter
     - Specification
   * - GMSL Interfaces
     - 2 x Quad Fakra connectors (8 camera interfaces)
   * - Ethernet
     - SFP+ 10 Gb with IEEE 1588 hardware timestamping
   * - Serial
     - RS232 UART interface (e.g., for GNSS devices)
   * - General I/O
     - 16 pins, 3.3 V, software configurable
   * - Processing
     - AMD Kria K26 Industrial SoM
   * - Power Supply
     - 9 V to 48 V DC, 24 W maximum
   * - Operating Temperature
     - -40 C to +60 C
   * - Software
     - Linux OS; RTP over UDP (software or FPGA-accelerated)

Hardware Requirements
---------------------

- AD-GMSL2ETH-SL evaluation board
- Up to 8 Tier IV C1 cameras (or compatible GMSL2 cameras)
- 8 Fakra cables and 2 quad-based mini-Fakra cables
- 16 GB SD card
- PC with 10G Ethernet capability
- SFP+ Ethernet cable

System Setup
------------

SD Card Preparation
~~~~~~~~~~~~~~~~~~~

Download the SD card image and write it to a 16 GB (or larger) SD card using
Balena Etcher or Win32 Disk Imager.

Boot Configuration
~~~~~~~~~~~~~~~~~~

Set the boot mode DIP switches to the SD card boot position as shown below.

.. figure:: boot_mode_switches.jpg
   :width: 500 px
   :align: center

   Boot mode switch configuration for SD card boot

Hardware Connections
~~~~~~~~~~~~~~~~~~~~

Connect the quad-based mini-Fakra cables from the cameras to the evaluation
board and attach the SFP+ Ethernet cable to the host PC.

.. figure:: fakra_connections.jpg
   :width: 500 px
   :align: center

   Quad-based mini-Fakra cable connections

.. figure:: sfp_connection.jpg
   :width: 500 px
   :align: center

   SFP+ cable connection

Network Configuration
~~~~~~~~~~~~~~~~~~~~~

After powering on the board (login credentials: ``analog`` / ``analog``),
configure the Ethernet interface:

.. code-block:: bash

   sudo ip link set mtu 9000 dev eth0 up
   sudo ifconfig eth0 10.42.0.1

Verify the configuration:

.. code-block:: bash

   ip a
   ls -l /sys/class/net/

Video Streaming
~~~~~~~~~~~~~~~

On the AD-GMSL2ETH-SL board, navigate to the workspace directory and run
the media configuration script:

.. code-block:: bash

   cd /home/analog/Workspace/K26
   # For 1 deserializer (4 cameras):
   ./media_cfg_des1.sh
   # For 2 deserializers (8 cameras):
   ./media_cfg_des12.sh

Start the GStreamer streaming pipeline:

.. code-block:: bash

   cd /home/analog/Workspace/gstreamer
   # For 4 cameras:
   ./stream_1des_4cams.sh
   # For 8 cameras:
   ./stream_2des_8cams.sh

The default target IP address is ``10.42.0.106`` and can be modified in the
streaming script.

Video Reception
~~~~~~~~~~~~~~~

On the receiving PC, use GStreamer to display the incoming video streams.
Each camera stream is available on a separate UDP port (5004--5011):

.. code-block:: bash

   gst-launch-1.0 udpsrc \
       caps="application/x-rtp, sampling=YCbCr-4:2:2, \
       depth=(string)8, width=(string)1920, height=(string)1080" \
       port="5004" \
       ! rtpvrawdepay ! videoconvert \
       ! fpsdisplaysink video-sink=xvimagesink

.. figure:: video_display.jpg
   :width: 500 px
   :align: center

   Video display with four cameras streaming

To stop streaming, identify and terminate the GStreamer processes:

.. code-block:: bash

   pidof gst-launch-1.0
   sudo kill <PID_NUMBERS>

Resources
---------

- :adi:`AD-GMSL2ETH-SL Product Page <AD-GMSL2ETH-SL>`

Support
-------

For questions and more information, please contact us on the :ez:`/`.

- :ez:`EngineerZone Reference Designs <reference-designs>`
