AD-GMSL-MIPI-ADP#
=================

Overview
--------

The GMSL2 SerDes Adapter Board is a versatile interface solution designed to streamline the integration of MIPI-CSI camera modules with MAX96717 serializers and MAX96724 deserializers. Supporting both MINI-SAS and FPC/FFC connectors, it enables seamless connectivity with NXP processors. The adapter includes a built-in MIPI switch for dynamic data lane selection, a robust power management system with Power over Coax (PoC) support, and high-speed data transmission up to 6Gbps—ideal for automotive, industrial, and high-resolution imaging applications.

Features
--------

::

   *Dual-interface support (MINI-SAS and FFC) for camera module flexibility
   *Integrated MIPI switch for data lane routes between SerDes and processor/camera
   *Support for GMSL2 up to 6Gbps, enabling transmission of high-resolution video (up to 4K)
   *Robust automotive-grade performance with low-latency, ECC, and EMI mitigation features

Applications
------------

::

   *Automotive Surround View and Driver Monitoring Systems
   *Industrial Machine Vision
   *Smart Surveillance and Security Cameras
   *High-Resolution Display Interfaces
   *AI/ML Edge Processing with Vision Sensors

System Architecture
-------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmsl-mipi-adp/max96717_gmsl_serializer_16_.png
   :align: center
   :width: 1500px

General Setup
-------------

Equipment Needed
~~~~~~~~~~~~~~~~

::

   *MAX96717 EVK
   *MAX96724 EVK
   *Mouse and Keyboard
   *Monitor with HDMI connector
   *USB Hub (type-c)
   *Coax Cable
   *Camera modules
     *Setup A: MINISASTOCSI
     *Setup B: RPI-CAM-MIPI
   *MIPI-DSI to HDMI adapter such as IMX-MIPI-HDMI
   *Processors either
     *Setup A: 8MNANOLPD4-EVK or
     *Setup B: MCIMX93-EVK
   *Mini-SAS Cable (additional connector for i.MX8M EVK)
   *Flat Flexible Cable (FCC) (additional connector for i.MX93 EVK)

Hardware Settings
~~~~~~~~~~~~~~~~~

GMSL adaptor configuration and setup:

============== =================== ===
**Processor**  **Shunt** (J10/J20) 
============== =================== ===
8MNANOLPD4-EVK GND_S               SEL
MCIMX93-EVK    3v3                 SEL
============== =================== ===

Hardware Setup
--------------

Setup A:8MNANOLPD4-EVK
~~~~~~~~~~~~~~~~~~~~~~

-  The GMSL Serializer MAX96717-AAK-EVK# should have the following jumper settings: populate R67, R68, and R70 are populated with 0-ohm resistors to power the camera module.


|image1|

-  Ordered List Item The GMSL Deserializer MAX96724 should have the following jumper settings: populate R88 and R91 with 0-ohm resistors and leave R98 unpopulated.\

|image2|

-  Connect MINISASTOCSI camera module to J17 Ser Adapter using MINISAS cable as shown in this figure below.\

|image3|

-  Connect Serializer Adaptor to MAX96717 EVK using an on-board Samtec connector as shown in the figure below.\

|image4|

-  Connect GMSL SerDes using coax cable.

|image5|

-  Connect deserializer Adapter to MAX96724 using an onboard Samtec connector. And then connect the Des Adaptor to i.MX8M Nano EVK using MINISAS cables, as shown below.\

|image6|

-  Power on the MAX96724 using a 12V power supply and switch SW4 to the ON position. The PoC on the MAX96724 will also power the MAX96717 and the +camera module through the Ser Adapter.
-  Power the processor using a type-c power cord and turn ON the power switch.

Software Setup
--------------

-  After booting up, run the command i2cdetect -y 2 to check the I²C connection from the processor. Expected device addresses:

::

     *MAX96717: 0x40 
     *MAX96724: 0x4E
   * Transfer the script from your computer to the processor:\
     *Download and install WinSCP on your computer.
     *Connect an Ethernet cable to the processor, and check the IP address using the command: ip a.
     *Open WinSCP and use the IP address to connect your computer to the processor.
     *Transfer the required files from your computer to the processor.
   * Run the script using the command: ./.sh
   * Re-run the command i2cdetect -y 2 to verify if the camera module is now being detected by the processor.
     *MINISASTOCSI - 0x3c
     *RPI-CAM-MIPI - 0x67
   * Reboot the i.MX8M/i.MX93 with the command: reboot
   * After rebooting, start the GStreamer pipeline with the command:

.. container:: code bash

   
   .. code:: bash
   
            gst-launch-1.0 v4l2src ! 'video/x-raw, framerate=60/2, width=1280, height=720' ! autovideosink
   
   ::
   


* Once the pipeline is running, open a new terminal window and re-run the script: ./FileName.sh This will start the video feed.
   * To stop the video feed, press CTRL+C.

Support
-------

Analog Devices will provide **limited** online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone FPGA reference designs <community/fpga>` forum.

It should be noted, that the older the tools' versions and release branches are, the lower the chances to receive support from ADI engineers.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/max96717_setup.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/max96724_setup.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/serializer_setup.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/7171toadapter.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/7171tocoax.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/724toprocessor.png
   :width: 600px
