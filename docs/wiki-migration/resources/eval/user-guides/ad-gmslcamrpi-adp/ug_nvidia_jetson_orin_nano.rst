Nvidia Jetson Orin Nano User Guide
==================================

Required hardware
-----------------

**Development kits**

-  :adi:`MAX96724 GMSL Deserializer Evaluation Kit (EVK) <en/products/max96724.html>`
-  :adi:`MAX96717 GMSL Serializer Evaluation Kit (EVK) <en/products/max96717.html>` or **GMSL camera**
-  `Nvidia Orin Nano Developer Kit <https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/>`__

**Supported image sensors & cameras**

-  `Raspberry Pi Camera Module 2 <https://www.raspberrypi.com/products/camera-module-v2/>`__

**Cables**

-  15 pin same-side ribbon cable, P/N: MP-FFCA10152003A or similar
-  22 pin opposite-side ribbon cable, P/N: MP-FFCA05222002B or similar
-  22 pin same-side ribbon cable, P/N: MP-FFCA05222002A or similar
-  FAKRA Jack to FAKRA Jack coaxial cable

--------------

Hardware changes
----------------

**GMSL Deserializer Evaluation Kit**

-  Flip the SW5 switches to the ON position - enables I2C communication over the CSI bus

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/gmsl_deserializer_sw5.jpg
   :width: 300px

-  Bridge R88 - provides VDDIO to the adapter

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/deserializer_resistors.jpg
   :width: 300px

**GMSL Serializer Evaluation Kit**

-  Place a jumper on the J10 connector - enables power over the coaxial cable

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/gmsl_serializer_j10.jpg
   :width: 300px

-  Bridge R70 - provides 12V to the adapter
-  Bridge R80 - connects MFP2 to the adapter for IMX219
-  Bridge R66 - provides VDDIO to the adapter

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/serializer_resistors.jpg
   :width: 300px

**AD-GMSLCAMRPI-ADP# Adapter**

-  Configure the switches on the GMSL Serializer and the GMSL Deserializer adapters for **CAM1**.

====================== ========================
**Serializer adapter** **Deserializer adapter**
|image1|               |image2|
====================== ========================

--------------

System setup
------------

-  Write the :git-gmsl#platforms-user-guides-sd-card-images-and-build-instructions>`__ on a 64GB SD card
-  Plug the SD card into the Nvidia Orin Nano Developer Kit SD card slot
-  Connect a USB mouse and keyboard to the Nvidia Orin Nano Developer Kit
-  Connect a Display Port (DP) cable from the monitor to the Nvidia Orin Nano Developer Kit DP connector
-  Connect a **15 pins same-side** flex cable between the camera and the ribbon cable adapter
-  Connect a **22 pins opposite-side** flex cable between the ribbon cable adapter and the GMSL Serializer EVK Adapter on port P9
-  Connect the GMSL Serializer EVK Adapter to the GMSL Serializer EVK using the FAKRA coaxial cable
-  Connect a Coaxial cable between the GMSL Serializer EVK and the GMSL Deserializer EVK
-  Connect the GMSL Deserializer EVK Adapter to the GMSL Deserializer EVK
-  Connect a **22 pins same-side** flex cable between the GMSL Deserializer EVK Adapter on port P8 and the Nvidia Orin Nano Developer Kit on port CAM0
-  Connect the power supply to the GMSL Deserializer EVK
-  Flip the power switch labeled S1 to the ON position on the GMSL Serializer EVK
-  Flip the power switch labeled S4 to the ON position on the GMSL Deserializer EVK
-  Connect the power supply to the Nvidia Orin Nano Developer Kit

.. image:: https://wiki.analog.com/_media/:`Nvidia Orin Nano latest SD card image <resources/eval/user-guides/ad-gmslcamrpi-adp/nvidia_jetson_orin_system.jpg
   :align: left
   :width: 350px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/jetson_orin_nano_rpi_camera_connection.jpg
   :width: 350px

--------------

Running the evaluation application
----------------------------------

Once Linux boots you'll see on the DP monitor the Linux desktop and a shortcut named **run_demo.sh**. Double clicking on the icon will start the evaluation application. The evaluation application GUI will be displayed like in the picture bellow.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/nvidia_screen1.png
   :width: 600px

Power off sequence
~~~~~~~~~~~~~~~~~~

-  Open a terminal and type **sudo poweroff**. This will safely power off the Nvidia Orin Nano Developer Kit and ensure that the SD card is properly unmounted
-  Remove the power supply from the Nvidia Orin Nano Developer Kit
-  Flip the power switch labeled S1 to the OFF position on the GMSL Serializer Evaluation Kit
-  Flip the power switch labeled S4 to the OFF position on the GMSL Deserializer Evaluation Kit
-  Remove the power supply from the GMSL Deserializer Evaluation Kit

--------------

Getting the software
--------------------

The GMSL Linux kernel drivers, the complete Linux distributions for the supported processing platforms, and software user guides can be found on the `Analog Devices GMSL github repository <https://github.com/analogdevicesinc/gmsl>`.

--------------

.. image:: https://wiki.analog.com/_media/navigation ad-gmslcamrpi-adp#none#./
   :alt: Overview#none#

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ser_interposer.jpg
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/deser_interposer.jpg
   :width: 300px
