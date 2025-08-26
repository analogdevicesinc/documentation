ADRD8012-01Z
============

FPGA-based 8x GMSL to 10 Gb Ethernet Adapter
""""""""""""""""""""""""""""""""""""""""""""

Overview
---------

.. figure:: ADRD8012-01Z_ANGLE-evaluation-board.jpg
   :width: 600 px

   ADRD8012-01Z GMSL Board

The **ADRD8012-01Z** is an edge compute platform enabling low latency data
transfer from eight :adi:`Gigabit Multimedia Serial Link™ (GMSL) </product-category/gigabit-multimedia-serial-link.html>`
interfaces on to a 10 Gb Ethernet link. The target applications include
autonomous robots and vehicles where machine vision and real-time sensor fusion
is critical. Some of the main features and benefits include:

-  8x GMSL2 camera interfaces with up to 6 Gbps/channel
-  10 Gbps SFP+ Ethernet interface
-  Precision Time Protocol for synchronization with host systems and other edge devices
-  Embedded processing capabilities using the on-board 
   `AMD Kria K26 System-on-Module <https://www.amd.com/en/products/system-on-modules/kria/k26/k26i-industrial.html>`__
-  ROS2 compliant
-  Open-source embedded Linux software and FPGA design
-  Advanced camera triggering functions and control features

.. figure:: ADRD8012-01Z_01-block-diagram.png
   :width: 800 px

   ADRD8012-01Z Simplified Block Diagram

Specifications
--------------

+-----------------------+-----------------------------------------------------+
| Interfaces            |                                                     |
+=======================+=====================================================+
| SFP+                  | Supports 10 Gb Ethernet with IEEE 1588 hardware     |
|                       | timestamping                                        |
+-----------------------+-----------------------------------------------------+
| RS-232                | Serial interface for connecting UART peripherals,   |
|                       | e.g., GNSS devices                                  |
+-----------------------+-----------------------------------------------------+
| I/O                   | 16 general purpose I/O pins with software           |
|                       | configurable functionality, 3.3V voltage level      |
+-----------------------+-----------------------------------------------------+
| GMSL                  | 2x Quad Fakra connectors supporting 8 x GMSL        |
|                       | camera interfaces                                   |
+-----------------------+-----------------------------------------------------+
| Processing            |                                                     |
+-----------------------+-----------------------------------------------------+
| AMD K26               | Industrial grade AMD K26 SoM                        |
+-----------------------+-----------------------------------------------------+
| Power & Thermal       |                                                     |
+-----------------------+-----------------------------------------------------+
| Power Supply          | Input voltage: 9V to 48V DC at 24W max              |
+-----------------------+-----------------------------------------------------+
| Operating Temperature | -40°C to 60°C                                       |
+-----------------------+-----------------------------------------------------+
| Software              |                                                     |
+-----------------------+-----------------------------------------------------+
| Operating System      | Linux OS                                            |
+-----------------------+-----------------------------------------------------+
| Network data protocol | RTP over UDP with software implementation and       |
|                       | option for licensable FPGA accelerated RTP & UDP    |
|                       | stack                                               |
+-----------------------+-----------------------------------------------------+


System Setup & Evaluation
-------------------------

Required Hardware
~~~~~~~~~~~~~~~~~~

- 1 x :adi:`ADRD8012-01Z </resources/evaluation-hardware-and-software/evaluation-boards-kits/ADRD8012-01Z.html>`
- 8 x `Tier IV C1 cameras <https://edge.auto/automotive-camera/#C1>`__
- 8 x Fakra cables
- 2 x Quad-based mini-Fakra cables
- 1 x 16 GB SD card
- 1 x PC with 10G ethernet card
- 1 x SFP+ Ethernet cable

FPGA SD Card Image
~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   `SD card image <https://swdownloads.analog.com/cse/gmsl/10G/gmsl-10g-fsync.tar.xz>`__

After downloading the file, extract the compressed image and write it to the SD
card using `Balena Etcher <https://www.balena.io/etcher>`__ or
`Win32-Disk-Imager <https://sourceforge.net/projects/win32diskimager/files/Archive/>`__.

More details on how to extract a compressed image and write it on the SD card on
Linux and Windows can be found here:
`Writing an image onto the SD card <http://github.com/analogdevicesinc/aditof_sdk/blob/master/doc/sdcard_burn.md>`__

System Setup
~~~~~~~~~~~~~

In order to boot using SD card, you will need to set the boot mode’s switches to
the corresponding position, as indicated in the following image:

.. figure:: img_1242_1_.jpg
   :width: 400 px

   Boot Mode Switches Position

Connect the Quad-based mini-Fakra cables to the corresponding connectors on the
board. These will connect the cameras to the corresponding deserializers.

.. figure:: img_1247_1_.jpg
   :width: 400 px

   Connecting the Fakra Cables

Connect a SFP+ cable to the corresponding SFP port on the board.

.. figure:: img_1244_1_.jpg
   :width: 400 px

   Connecting the SFP Cable

Finally, you will need to connect a USB/micro-USB cable to the micro-USB port
located on the board. After that, you will be able to connect to the first USB
COM port that appears on the serial terminal, with a baud rate of **115200**.

.. note::

   Ubuntu credentials

   * username:analog
   * password:analog

.. shell::

   #eth0 - 10G ethernet interface
   $ls -l /sys/class/net/
    total 0
    lrwxrwxrwx 1 root root 0 Mar 20 16:32 eth0 -> ../../devices/platform/axi/a0000000.ethernet/net/eth0
    lrwxrwxrwx 1 root root 0 Mar 20 16:32 lo -> ../../devices/virtual/net/lo
    lrwxrwxrwx 1 root root 0 Mar 20 16:32 sit0 -> ../../devices/virtual/net/sit0

.. important::

   Both server and client should have the same MTU

.. shell::

   #Set the eth0's MTU and IP address
   $sudo ip link set mtu 9000 dev eth0 up
   $sudo ifconfig eth0 10.42.0.1
   $ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
            valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
            valid_lft forever preferred_lft forever
    2: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
        link/sit 0.0.0.0 brd 0.0.0.0
    3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc mq state UP group default qlen 1000
        link/ether a2:78:c4:14:da:c2 brd ff:ff:ff:ff:ff:ff
        inet 10.42.0.1/8 brd 10.255.255.255 scope global eth0
            valid_lft forever preferred_lft forever
        inet6 fe80::a078::c4ff:fe14:dac2/64 scope link
            valid_lft forever preferred_lft forever

.. shell::

   #Configure the video pipeline and the cameras
   $cd /home/analog/Workspace/K26
   $./media_cfg_des1/2/12.sh
   #(depending on the desired deserializer or 12 for the case when there are two deserializers with 4 cameras)

   #Start streaming to another host
   $cd /home/analog/Workspace/gstreamer
   #(depending on the number of cameras - 4 or 8 cameras - 1 or 2 deserializers)
   $./stream_1des_4cams/2des_8cams.sh [HOST_IP_ADDRESS of the x86-based workstation can be modified/by default is set to 10.42.0.106 in this script]

.. note::

    In order to stop all this processes generated by the streaming-related
    scripts, you can use the Linux pidof command to see what are the IDs of this
    gstreamer-related instaces, and after that kill these ones by using Linux kill
    command, in the following way:

.. shell::

   #That is the command to show the ID numbers of the opened processes and will show you 8 numbers - like in the following line
   $pidof gst-launch-1.0
   $800 799 798 797 796 795 794 793
   $sudo kill 800 799 797 796 795 794 793


Now the streams are running on ports 5004 to 5007, depending on the configured number of cameras.

Install Gstreamer on x86
~~~~~~~~~~~~~~~~~~~~~~~~

Depending on the Linux distribution of your x86 workstation, you can install
Gstreamer by using the corresponding package manager. For example, on Ubuntu
you can use the following command:

.. shell::

   $sudo apt-get install gstreamer1.0-tools gstreamer1.0-plugins-base
    gstreamer1.0-plugins-good gstreamer1.0-plugins-bad
    gstreamer1.0-plugins-ugly gstreamer1.0-libav

More details about Gstreamer installation can be found
`here <https://gstreamer.freedesktop.org/documentation/installing/index.html?gi-language=c>`__.

Displaying the Video
--------------------

On the receiving side, `Gstreamer <https://gstreamer.freedesktop.org/documentation/installing/index.html?gi-language=c>`__
must be installed.


Single Deserializer (4 cameras)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now open 4 instances of Gstreamer for each port(5004-5007).

**On x86 workstation**

.. shell::

   $gst-launch-1.0 udpsrc caps=“application/x-rtp, sampling=YCbCr-4:2:2,
    depth=(string)8, width=(string)1920, height=(string )1080” port=“5004” !
    rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink
    text-overlay=true sync=false

   $gst-launch-1.0 udpsrc caps=“application/x-rtp, sampling=YCbCr-4:2:2,
    depth=(string)8, width=(string)1920, height=(string )1080” port=“5005” !
    rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink
    text-overlay=true sync=false

   $gst-launch-1.0 udpsrc caps=“application/x-rtp, sampling=YCbCr-4:2:2,
    depth=(string)8, width=(string)1920, height=(string )1080” port=“5006” !
    rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink
    text-overlay=true sync=false

   $gst-launch-1.0 udpsrc caps=“application/x-rtp, sampling=YCbCr-4:2:2,
    depth=(string)8, width=(string)1920, height=(string )1080” port=“5007” !
    rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink
    text-overlay=true sync=false

.. figure:: img_1252_1_.jpg

   Gstreamer Video Display for Single Deserializer (4 Cameras)

2 x Deserializers (8 cameras)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now open 8 instances of Gstreamer for each port(5004-5011).

**On x86 workstation**

.. shell::

   $gst-launch-1.0 udpsrc caps=“application/x-rtp, sampling=YCbCr-4:2:2,
    depth=(string)8, width=(string)1920, height=(string )1080” port=“5004” !
    rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink
    text-overlay=true sync=false

   $gst-launch-1.0 udpsrc caps=“application/x-rtp, sampling=YCbCr-4:2:2,
    depth=(string)8, width=(string)1920, height=(string )1080” port=“5005” !
    rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink
    text-overlay=true sync=false

   $gst-launch-1.0 udpsrc caps=“application/x-rtp, sampling=YCbCr-4:2:2,
    depth=(string)8, width=(string)1920, height=(string )1080” port=“5006” !
    rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink
    text-overlay=true sync=false

   $gst-launch-1.0 udpsrc caps=“application/x-rtp, sampling=YCbCr-4:2:2,
    depth=(string)8, width=(string)1920, height=(string )1080” port=“5007” !
    rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink
    text-overlay=true sync=false

   $gst-launch-1.0 udpsrc caps=“application/x-rtp, sampling=YCbCr-4:2:2,
    depth=(string)8, width=(string)1920, height=(string )1080” port=“5008” !
    rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink
    text-overlay=true sync=false

   $gst-launch-1.0 udpsrc caps=“application/x-rtp, sampling=YCbCr-4:2:2,
    depth=(string)8, width=(string)1920, height=(string )1080” port=“5009” !
    rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink
    text-overlay=true sync=false

   $ gst-launch-1.0 udpsrc caps=“application/x-rtp, sampling=YCbCr-4:2:2,
    depth=(string)8, width=(string)1920, height=(string )1080” port=“5010” !
    rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink
    text-overlay=true sync=false

   $gst-launch-1.0 udpsrc caps=“application/x-rtp, sampling=YCbCr-4:2:2,
    depth=(string)8, width=(string)1920, height=(string )1080” port=“5011” !
    rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink
    text-overlay=true sync=false

..
   Enable after adding new content

   User Guides
   -----------

   .. toctree::
      :titlesonly:
      :maxdepth: 1
      :glob:

      */index

Help and Support
----------------

For questions and more information, please visit the :ez:`/`.
