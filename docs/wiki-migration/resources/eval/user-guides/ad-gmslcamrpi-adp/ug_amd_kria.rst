AMD Kria KV260 User Guide
=========================

Required hardware
-----------------

**Development kits**

-  :adi:`MAX96724-BAK-EVK GMSL Deserializer evaluation kit <en/products/max96724.html>`
-  `AMD Kria KV260 <https://www.xilinx.com/products/som/kria/kv260-vision-starter-kit.html>`_

**Supported image sensors & cameras**

-  `C1 TIER-IV camera with integrated GMSL serializer <https://sensor.tier4.jp/automotive-camera/#C1>`_

**Cables**

-  15 pin same-side ribbon cable, P/N: MP-FFCA10152003A or similar

--------------

Hardware changes
----------------

**GMSL Deserializer Evaluation Kit (MAX96724)**

-  Flip the SW5 switches to the ON position - enables I2C communication over the CSI bus

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/gmsl_deserializer_sw5.jpg
   :width: 300px

-  Bridge R88 - provides VDDIO to the adapter

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/deserializer_resistors.jpg
   :width: 300px

.. note::

   Make sure you have all the PoC-related jumpers set to the corresponding **VPOC_x** point (ref. :adi:`datasheet <media/en/technical-documentation/data-sheets/max96724-bak-evk-max96724r-bak-evk.pdf>` p. 15/22) (1 to 4 for the possible serializer inputs to the quad deserializer).


-  Example from the datasheet - J3 for SIOA input:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/vpoc1_sioa_max96724.png
   :align: center

--------------

GMSL SerDes Evaluation Kits Validation and Switch Setup
-------------------------------------------------------

**MAX96724 Deserializer Evaluation Kit**

-  Please make sure that the **CFG** pins of the MAX96724 deserializer are set to low (0) - indicating a COAX - GMSL 2 connection between serializers and deserializer. The levels can be seen and changed by using the GMSL SerDes GUI :adi:`software <en/resources/evaluation-hardware-and-software/embedded-development-software/software-download.html?swpart=SFW0019760I>`. You need to connect the MAX96724 kit to a host PC by using an USB cable and then refresh the application to see the added device.

**AD-GMSLCAMRPI-ADP# Adapter**

-  Configure the switches on the GMSL Deserializer adapter for **CAM2**.

====================== ========================
**Serializer adapter** **Deserializer adapter**
|image1|               |image2|
====================== ========================

--------------

System setup
------------

-  Write the :git-gmsl#platforms-user-guides-sd-card-images-and-build-instructions>`__ on a 8GB (or more) SD card
-  Plug the SD card into the KV260 SD card slot
-  Connect the HDMI cable from the monitor to the HDMI connector of the KV260 evaluation kit
-  Connect the 2 Tier 4 C1 cameras to INA and INB of the deserializer kit (if you have only one camera, connect it to the INA port of the deserializer)
-  Connect the 15 pins camera cable between the Kria and the P1 connector of the interposer. **Make sure to use the cable with contacts on the same sides.**
-  Connect the 22 pin flex cable
-  Connect the **KV260 evaluation kit** to the power supply
-  Connect the **MAX96724 evaluation kit** to the power supply and put the corresponding switch in the **"ON"** position
-  KV260 will boot by default from QSPI. It must be forced to boot from SD card to correctly load the custom BOOT.BIN. For this please follow the guide `here <https::`AMD KV260-based latest SD card image </xilinx.github.io/kria-apps-docs/creating_applications/2022.1/build/html/docs/bootmodes.html>` and run **boot_sd** boot mode
-  Connect a USB mouse and keyboard to the KV260 evaluation kit. It's possible to use either a mouse & keyboard combo or a separate mouse and keyboard

.. note::

   Ubuntu credentials user:analog/pass:analog


.. note::

   To change the number of cameras that would be used in the setup, you would need to change the default devicetree binary that is located in the boot partition of the SD card to the corresponding number of cameras (between 1 and 2), by overwriting the system.dtb to an one from the corresponding directory. The devicetree binary options are located in the bootfs partiiton (in **nr_cams/1cam or 2cams directory/system.dtb**). The **bootfs** partition can be mounted by using the mount utility: e.g. **mount /dev/mmcblk1p1 /mnt**.


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/kria_adapter.jpg
   :align: left
   :width: 1000px

.. note::

   The setup from the attached figure contains the two SWs of the GMSL Deserializer RPi adapter as follows: the **SW1** set to the left side and the **SW3** oriented to the connected flex cable, in the upper part in this case, oriented to the P6 flex cable connector. In addition to the connections from the figure, please make sure that the **Kria KV260 and MAX96724 evaluation kits** are powered up using their corresponding power-related **barrel jack connectors**.


--------------

Running the evaluation application
----------------------------------

Once Linux boots you'll see on the HDMI monitor the Linux desktop and on the top left corner a shortcut to the script named **video_cfg.sh**. Double clicking on the icon will start the media-ctl configuration script. The script is running in background without any pop ups.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/kria_video_cfg.png
   :width: 600px

After the script was executed once, one should double click on Qt V4L2 test Utility icon to start the video capture application. A window like bellow should open. First the user must select **video0** device by clicking the open icon.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/qv4l2_select_video_dev.png
   :width: 600px

A new instance of Qt V4L2 test Utility should be started and selected **video1** this time. After this step the play button should be pressed on both Qt V4L2 test Utility instances. Video should be visible on the 2 windows.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmslcamrpi-adp/qv4l2_video.jpg
   :width: 600px

OpenGL rendering is recommended to be disabled by accessing Qt V4L2 test Utility capture menu. Capture will start only if both Qt V4L2 test Utility instances are on play state. This is a current HDL limitation.

RTP-based Streaming
~~~~~~~~~~~~~~~~~~~

-  In order to do a streaming of the data that is captured from the cameras to an external machine, you can use the 1G Ethernet-based transmission available through the attached port of the KV260 evaluation kit and a streaming-related application such as the one available in the GStreamer framework (an e.g. would be the RTP-based streaming support for uncompressed data available in the GStreamer).

Power off sequence
~~~~~~~~~~~~~~~~~~

-  Open a terminal and type **sudo poweroff**. This will safely power off the Kria and ensure that the SD card is properly unmounted

--------------

Getting the software
--------------------

The GMSL Linux kernel drivers, the complete Linux distributions for the supported processing platforms, and software user guides can be found on the :git-gmsl>`__.

HDL Project
-----------

The project and the project's overview can be found at the following links: `project's link <https::`Analog Devices GMSL github repository </github.com/analogdevicesinc/hdl/tree/main/projects/max96724/kv260>` :doc:`overview's link </wiki-migration/resources/eval/user-guides/ad-gmslcamrpi-adp/ug_amd_kria/hdl>`.

--------------

.. image:: https://wiki.analog.com/_media/navigation ad-gmslcamrpi-adp#none#./
   :alt: Overview#none#

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ser_interposer.jpg
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/deser_interposer.jpg
   :width: 300px
