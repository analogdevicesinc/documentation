ZCU102 GMSL User Guide
======================

Development kit contents
------------------------

2 x FPGA Carrier boards: `ZCU102 eval kit <https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g.html>`__

1 x GMSL Deserializer: :adi:`MAX96724-BAK-EVK <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max96724f-bak-evk.html#eb-overview>`

1 x GMSL FMC adapter

2 x 16GB SD cards

1 x SFP+ Ethernet cable

FPGA SD Card Image
------------------

The SD-card Image for the Xilinx ZCU102 board can be found here: `gmsl_driver.img.xz <https://swdownloads.analog.com/cse/kuiper/gmsl_driver.img.xz>`__

After downloading the file, extract the compressed image and write it to the SD-card using `Balena Ethcher <https://www.balena.io/etcher>`__ or `Win32-Disk-Imager <https://sourceforge.net/projects/win32diskimager/files/Archive/>`__.

More details on how to extract a compressed image and write it on the SD card on Linux and Windows can be found here: `Writing an image onto the SD card <http://github.com/analogdevicesinc/aditof_sdk/blob/master/doc/sdcard_burn.md>`__

--------------

System Setup
------------

.. important::

   The default FMC Vadj on ZCU102 is 1.8V and the MIPI D-PHY requires 1.2V

   
   The following `tutorial <https://www.xilinx.com/member/forms/download/design-license.html?cid=cd76e6f1-932f-454e-a8aa-04114f041b1f&filename=xtp433-zcu102-system-controller-c-2019-1.pdf>`__ explains how to use the `ZCU102 system controller GUI <https://www.xilinx.com/member/forms/download/design-license.html?cid=35da7fb5-614f-4f7f-a9df-11e76c05a717&filename=rdf0382-zcu102-system-controller-c-2019-1.zip>`__ and configure the Vadj to 1.2V.
   


Solder a pcb connector on the FMC adapter's J5 and configure the jumpers as the following.

|image1| |image2|

Place a 0 OHM resistor on R88.

.. image:: https://wiki.analog.com/_media/playground/gmsl-deserializer-bridge.png
   :width: 600px



.. raw:: html

   <details><summary>GMSL Deserializer Board Setup (outdated)</summary>

Connect the FMC adapter to the EVAL board and place it on the ZCU102's HPC0 port. With a jumper wire (blue wire in the image below) connect the GMSL deserializer board MFP8 pin to the PMOD 0, PIN 1.

.. image:: https://wiki.analog.com/_media/playground/20230802_131214.jpg
   :width: 600px

Insert the SD-card into the Xilinx ZCU102 board and connect the GMSL deserializer board USB cable to a PC.

.. image:: https://wiki.analog.com/_media/playground/deserializer-cable.png
   :width: 600px

--------------

Move the i2c switch in the OFF position on the GMSL deserializer board.

.. image:: https://wiki.analog.com/_media/playground/serdes-i2c.png
   :width: 800px

Power-up the ZCU102 and check if a new COM port appears in Device Manager.

.. image:: https://wiki.analog.com/_media/playground/gmsl-dev-man-serdes.png
   :width: 600px

Configure the GMSL video pipeline using the :adi:`GMSL GUI tool <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max96717f-aak-evk.html#eb-tools>` and the `GMSL config files <https://swdownloads.analog.com/cse/kuiper/GMSL-config.zip>`__

.. image:: https://wiki.analog.com/_media/playground/serdes1.png
   :width: 800px

In the uC information area, press on "Release Port" and "Connect port"

|image3| |image4|

The corresponding COM port should appear in the dropdown bar. Now load the config files from the "File" tab -> Load (.cpp) file.

.. image:: https://wiki.analog.com/_media/playground/serdes-load.png
   :width: 400px

Now load the files in the following order:

-  Tier4-ISX021-4CH-pipe.cpp
-  Tier4-ISX021-MAX9295_80.cpp
-  Tier4-ISX021-MAX9295_84.cpp
-  Tier4-ISX021-MAX9295_C0.cpp
-  Tier4-ISX021-MAX9295_C4.cpp

.. image:: https://wiki.analog.com/_media/playground/serdes-files.png
   :width: 600px

Move back the i2c switches in the ON state


|image5|

.. raw:: html

   </details>


--------------

ZCU102 FPGA Board Setup
~~~~~~~~~~~~~~~~~~~~~~~

Connect the Deserializer and the FMC adapter to ZCU102 FMC HPC1 connector.

.. image:: https://wiki.analog.com/_media/playground/gmsl_des_on.png
   :alt: Status of the Adapter and D-Phy (still LEDs)
   :width: 400px

Attach to the serial terminal using the first USB com port that appears after connecting the ZCU102's USB, with a baud rate of 115200.

Connect an ethernet cable to the ZCU102 RJ45 port

.. image:: https://wiki.analog.com/_media/playground/zcu102-cables.png
   :width: 600px

Or connect the cable to the SFP0 port

.. image:: https://wiki.analog.com/_media/playground/zcu102_sfp0.jpg
   :width: 600px

.. code:: c


   #Configure the interface
   #In this case we use ZCU102's SFP0
   $ ls -l /sys/class/net/
   total 0
   lrwxrwxrwx 1 root root 0 Mar 20 16:32 can0 -> ../../devices/platform/axi/ff070000.can/net/can0
   lrwxrwxrwx 1 root root 0 Mar 20 16:32 eth0 -> ../../devices/platform/axi/a0000000.ethernet/net/eth0
   lrwxrwxrwx 1 root root 0 Mar 20 16:32 eth1 -> ../../devices/platform/axi/a0000000.ethernet/net/eth1
   lrwxrwxrwx 1 root root 0 Mar 20 16:32 eth2 -> ../../devices/platform/axi/ff0e0000.ethernet/net/eth2
   lrwxrwxrwx 1 root root 0 Mar 20 16:32 lo -> ../../devices/virtual/net/lo
   lrwxrwxrwx 1 root root 0 Mar 20 16:32 sit0 -> ../../devices/virtual/net/sit0

.. important::

   Both server and client should have the same MTU


::


   #Set the MTU and ip
   $ sudo ip link set mtu 9000 dev eth1 up
   $ sudo ip addr add 192.168.5.1/24 dev eth1
   $ ip a
   1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
       link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
       inet 127.0.0.1/8 scope host lo
          valid_lft forever preferred_lft forever
       inet6 ::1/128 scope host 
          valid_lft forever preferred_lft forever
   2: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
       link/sit 0.0.0.0 brd 0.0.0.0
   3: can0: <NOARP,ECHO> mtu 16 qdisc noop state DOWN group default qlen 10
       link/can 
   5: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
       link/ether 96:e8:9a:83:fc:f6 brd ff:ff:ff:ff:ff:ff
   6: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc mq state UP group default qlen 1000
       link/ether 8e:2e:6e:7d:a8:f2 brd ff:ff:ff:ff:ff:ff
       inet 192.168.5.1/24 scope global eth1
          valid_lft forever preferred_lft forever
       inet6 fe80::8c2e:6eff:fe7d:a8f2/64 scope link 
          valid_lft forever preferred_lft forever
   7: eth2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
       link/ether e2:43:6c:e2:ae:42 brd ff:ff:ff:ff:ff:ff

.. note::

   Ubuntu credentials user:analog/pass:analog


.. code:: c


   #Configure the video pipeline and the cameras (invalid argument messages can be ignored)
   $ cd /home/analog/Workspace/ZCU102
   $ ./media_cfg.sh

   #Start streaming to another host
   $ cd /home/analog/Workspace/gstreamer
   $ ./server.sh **[IP of the viewing station]**
   $ ./server.sh 192.168.5.2

Now the streams are running on ports 5004 to 5007, depending on the configured number of cameras

--------------

Displaying the Video
--------------------

On the receiving side, `G-streamer <https://gstreamer.freedesktop.org/documentation/installing/index.html?gi-language=c>`__ must be installed

Now open 4 instances of g-streamer for each port(5004-5007) 

.. raw:: html

   <details><summary>(Click) On another ZCU102</summary>

$ gst-launch-1.0 udpsrc caps="application/x-rtp, sampling=YCbCr-4:2:2, depth=(string)8, width=(string)1920, height=(string )1080" port="5004" ! rtpvrawdepay ! videoconvert ! autovideosink

$ gst-launch-1.0 udpsrc caps="application/x-rtp, sampling=YCbCr-4:2:2, depth=(string)8, width=(string)1920, height=(string )1080" port="5005" ! rtpvrawdepay ! videoconvert ! autovideosink

$ gst-launch-1.0 udpsrc caps="application/x-rtp, sampling=YCbCr-4:2:2, depth=(string)8, width=(string)1920, height=(string )1080" port="5006" ! rtpvrawdepay ! videoconvert ! autovideosink

$ gst-launch-1.0 udpsrc caps="application/x-rtp, sampling=YCbCr-4:2:2, depth=(string)8, width=(string)1920, height=(string )1080" port="5007" ! rtpvrawdepay ! videoconvert ! autovideosink

.. raw:: html

   </details>




.. raw:: html

   <details><summary>(Click) On x86 workstation</summary>

$ gst-launch-1.0 udpsrc caps="application/x-rtp, sampling=YCbCr-4:2:2, depth=(string)8, width=(string)1920, height=(string )1080" port="5004" ! rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink text-overlay=true sync=false

$ gst-launch-1.0 udpsrc caps="application/x-rtp, sampling=YCbCr-4:2:2, depth=(string)8, width=(string)1920, height=(string )1080" port="5005" ! rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink text-overlay=true sync=false

$ gst-launch-1.0 udpsrc caps="application/x-rtp, sampling=YCbCr-4:2:2, depth=(string)8, width=(string)1920, height=(string )1080" port="5006" ! rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink text-overlay=true sync=false

$ gst-launch-1.0 udpsrc caps="application/x-rtp, sampling=YCbCr-4:2:2, depth=(string)8, width=(string)1920, height=(string )1080" port="5007" ! rtpvrawdepay ! videoconvert ! fpsdisplaysink video-sink=xvimagesink text-overlay=true sync=false

.. raw:: html

   </details>


--------------

Configure the system for a different number of cameras
------------------------------------------------------

Copy the devicetree from the folder that matches the number of connected cameras

::

   $ sudo mount /dev/mmcblk0p1 /mnt
   $ cd /mnt
   $ ls ZCU102/device_tree/
      tier4_1cam  tier4_2cam  tier4_3cam  tier4_4cam
   $ sudo cp ZCU102/device_tree/tier4_2cam/system.dtb .
   $ sudo reboot

.. |image1| image:: https://wiki.analog.com/_media/playground/fmc-adp-conn.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/playground/fmc-adp-conn-jumper.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/playground/serdes2.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/playground/serdes3.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/playground/serdes-i2c2.png
   :width: 800px
