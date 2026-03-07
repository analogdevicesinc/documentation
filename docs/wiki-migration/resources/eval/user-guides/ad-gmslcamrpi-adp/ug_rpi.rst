Raspberry Pi User Guide
=======================

Required hardware
-----------------

**Development Kits**

-  :adi:`AD-GMSLCAMRPI-ADP# GMSL EV Kit Adapter Board <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ad-gmslcamrpi-adp.html>`
-  :adi:`MAX96724 GMSL Deserializer Evaluation Kit (EVK) <en/products/max96724.html>`
-  :adi:`MAX96717 GMSL Serializer Evaluation Kit (EVK) <en/products/max96717.html>` or *GMSL camera*
-  `Raspberry Pi 4 Model B <https://www.raspberrypi.com/products/raspberry-pi-4-model-b/>`_ *(2GB of RAM or more preferred)*

**Supported image sensors & cameras**

-  `IMX219 Raspberry Pi Camera Module 2 <https://www.raspberrypi.com/products/camera-module-v2/>`_

**Cables**

.. warning::

   Do not use the 15-pin ribbon cable included with the Raspberry Pi camera since that is an opposite sided cable.


-  15 Pin Type A (**

.. container:: hi

   same side


**) Flexible Ribbon Cable, P/N: MP-FFCA10152003A or `Similar <https://www.amazon.com/dp/B07RVD2MZV>`_
-  22 Pin Type B (**

.. container:: hi

   opposite side


**) Flexible Ribbon Cable, P/N: MP-FFCA05222002B or `Similar <https://www.amazon.com/dp/B07S1BSPYD>`_
-  FAKRA Jack to FAKRA Jack coaxial cable, provided in EV kits

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/adaptor_block_diagram.png
   :align: center
   :width: 800px

--------------

Board modifications
-------------------

Using the procedure to :doc:`Set CFG Pin Levels </wiki-migration/products/gmsl/gui/tools/set_cfg_pin_levels>`, configure the serdes pair as follows:

==== ========================== ==========================
\    MAX96717                   MAX96724
==== ========================== ==========================
CFG0 **0** – I2C, ROR, 0x80     **0** – I2C, 0x4E
CFG1 **7** – Coax, 6Gbps, Pixel **0** – Coax, GMSL2, 6Gbps
==== ========================== ==========================

.. important::

   It is required to set the CFG pins to the indicated levels for this setup.


| For more information about the default CFG configuration of each evaluation board, please visit the respective datasheet documentation: :adi:`MAX96717EVKIT Datasheet <media/en/technical-documentation/data-sheets/max96717ev.pdf>`
| :adi:`MAX96724EVKIT Datasheet <media/en/technical-documentation/data-sheets/max96724-bak-evk-max96724r-bak-evk.pdf>`

**GMSL Deserializer Evaluation Kit**

-  Slide the **SW5** switches to the ON position - enables I2C communication over the CSI bus
-  Remove the **J18** and **J19** jumpers to allow the Rpi to become the Main host controller for the I2C lines.
-  Make sure the **J3** is set as default **2-3** position to enable POC.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/gmsl_deserializer_sw5.jpg
   :width: 300px

-  Bridge **R88** - provides VDDIO to the adapter

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/deserializer_resistors.jpg
   :width: 300px

**GMSL Serializer Evaluation Kit**

-  Place a jumper on the **J10** connector - enables power over the coaxial cable

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/serializer_mods_j10.png
   :width: 400px

-  Bridge **R70** - provides 12V to the adapter
-  Bridge **R80** - connects MFP2 to the adapter for IMX219
-  Bridge **R66** - provides VDDIO to the adapter

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/serializer_mods_samtec_res.png
   :width: 400px

**AD-GMSLCAMRPI-ADP# Adapter**

-  Configure the switch **S2** on the GMSL Serializer adapter for CAM1 on connector **P9**.
-  Configure the switch **S1** on the GMSL Deserializer adapter for CAM2 on connector **P6** and slide switch **S3** towards connector **P6**.

====================== ========================
**Serializer adapter** **Deserializer adapter**
|image1|               |image2|
====================== ========================

--------------

System setup
------------

MAX96717 Serializer EV kit Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the following setup, please ensure ribbon cables and boards are oriented to match the diagrams.

Connect the 15 pin ribbon cable to the camera board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/step0.png
   :align: center
   :width: 200px

Connect the other end of the 15 pin ribbon cable into the 15-to-22 pin adaptor board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/step1.png
   :align: center
   :width: 300px

On the other side of the 15-to-22 pin adaptor board, connect the 22-pin ribbon cable. **Note:** This is an opposite sided flex cable, please ensure it matches the orientation in the picture.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/step2.png
   :align: center
   :width: 400px

Connect the other end of the 22 pin ribbon cable into the EV kit adaptor board **P9** connector.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/step3.png
   :align: center
   :width: 500px

Lastly, connect the EV kit adaptor board to the MAX96717 EV kit.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/step4.png
   :align: center
   :width: 700px

MAX96724 Deserializer EV kit Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting with the Raspberry Pi 4 B, connect the 15 pin ribbon cable to the CSI input connector.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/step5.png
   :align: center
   :width: 400px

Connect the other end of the 15 pin ribbon cable into the 15-to-22 pin adaptor board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/step6.png
   :align: center
   :width: 400px

On the other side of the 15-to-22 pin adaptor board, connect the 22-pin ribbon cable. **Note:** This is an opposite sided flex cable, please ensure it matches the orientation in the picture.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/step7.png
   :align: center
   :width: 500px

Connect the other end of the 22 pin ribbon cable into the EV kit adaptor board **P8** connector.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/step8.png
   :align: center
   :width: 600px

Lastly, connect the EV kit adaptor board to the MAX96724 EV kit.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/step9.png
   :align: center
   :width: 700px

With both sides of the SerDes devices connected up, the last step it to connect the two sides together with the coax cable. The MAX96717 serializer only has one connection. The MAX96724 deserializer has 4 inputs so connect the coax cable to link A (INA) on **J7**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/gmsl_full_system_config.png
   :align: center
   :width: 800px

Connect power to the 12V barrel jack **J1** of the MAX96724 deserializer. If utilizing the GMSL GUI, also connect the micro USB cable to **J6** of the MAX96724 deserializer EV kit.

Raspberry Pi 4 Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Connect the USB-C power supply to the Raspberry Pi 4 connector.
-  Connect the HDMI cable from the monitor to the Raspberry Pi micro HDMI connector.
-  Write the :git-gmsl#platforms-user-guides-sd-card-images-and-build-instructions>`__ on a 8GB (or more) SD card.
-  Plug the SD card into the Raspberry Pi 4 SD card slot.
-  Connect a USB mouse and keyboard to the Raspberry Pi 4. It's possible to use either a mouse & keyboard combo or a separate mouse and keyboard.

--------------

Running the evaluation application
----------------------------------

Once Linux boots you'll see on the HDMI monitor the Linux desktop and on the top left corner a shortcut to the script named **video_cfg.sh**. Double-clicking on the icon will start the media-ctl configuration script to connect to the V4L2 media pipeline. It may not appear that anything happens but the script runs in background without any pop ups.

.. image:: https://wiki.analog.com/_media/:`Raspberry Pi latest SD card image <resources/eval/user-guides/ad-gmslcamrpi-adp/rpi_video_cfg.png
   :align: center
   :width: 600px

After the script runs, double-click on the Qt V4L2 test Utility icon to start the video capture application. A window will open then press the green play button to start video capturing.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/rpi_qv4l2.png
   :align: center
   :width: 600px

The capture window will look like below.

|image3| *Note*: some displays may have vertical/horizontal lines. This is typically an artifact caused on HDMI monitors and unrelated to the evaluation setup.

Power off sequence
~~~~~~~~~~~~~~~~~~

-  Open a terminal and type **sudo poweroff**. This will safely power off the Raspberry Pi 4 and ensure that the SD card is properly unmounted.
-  Remove the power supply from the Raspberry Pi 4.
-  Remove the power supply from the MAX96724 EV kit.

--------------

Getting the software
--------------------

The GMSL Linux kernel drivers, the complete Linux distributions for the supported processing platforms, and software user guides can be found on the `Analog Devices GMSL github repository <https://github.com/analogdevicesinc/gmsl>`.

--------------

Tips for Troubleshooting
------------------------

There are a few key commands in the Linux environment that can help identify if the expected connections and communications have been made.

-  In the Linux environment, you can check to see if the Rpi I2C is detecting the GMSL boards by sending a I2C detect command  [1]_ as follows: ``$ sudo i2cdetect -y 10``\ The Result should look as follows in the terminal:``analog@kuiper-gmsl:~$ sudo i2cdetect -y 10
   [sudo] password for analog: 
        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
   00:                         -- -- -- -- -- -- -- -- 
   10: UU -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
   20: -- -- -- -- -- -- -- UU -- -- -- -- -- -- -- -- 
   30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
   40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
   50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
   60: -- -- -- -- 64 -- -- -- -- -- -- -- -- -- -- -- 
   70: -- -- -- -- -- -- -- --``
-  You can also confirm that the video for Linux application is detecting the camera and GMSL devices by using the following command:``$ v4l2-ctl --list-devices``\ The response should look like the following:``analog@kuiper-gmsl:~$ v4l2-ctl --list-devices
   bcm2835-codec-decode (platform:bcm2835-codec):
       /dev/video10
       /dev/video11
       /dev/video12
       /dev/video18
       /dev/video31
       /dev/media2

   bcm2835-isp (platform:bcm2835-isp):
       /dev/video13
       /dev/video14
       /dev/video15
       /dev/video16
       /dev/video20
       /dev/video21
       /dev/video22
       /dev/video23
       /dev/media1
       /dev/media3

   unicam (platform:fe801000.csi):
       /dev/video0
       /dev/video1
       /dev/media4

   rpivid (platform:rpivid):
       /dev/video19
       /dev/media0``\ The key is to identify the **unicam** output, which correspond to the Rpi camera setup.

--------------

.. image:: https://wiki.analog.com/_media/navigation ad-gmslcamrpi-adp#none#./
   :alt: Overview#none#

.. [1]
   More information about these commands found here `i2c-tools - i2cdetect <https://www.mankier.com/8/i2cdetect>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/serializer_interposer_cfg.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/deserializer_interposer_cfg.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/rpi_running_qv4l2.png
   :width: 600px
