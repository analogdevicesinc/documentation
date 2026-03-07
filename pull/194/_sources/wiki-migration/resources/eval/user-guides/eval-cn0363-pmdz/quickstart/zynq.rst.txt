EVAL-CN0363-PMDZ ZED Quick Start Guide
======================================

This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the EVAL-CN0363-PMDZ ZED on the `ZED Board <http://zedboard.org/product/zedboard>`_.

Creating / Configuring the SD card
----------------------------------

.. tip::

   The EVAL-CN0363-PMDZ comes with a pre-populated SD card. When using the pre-polpulated SD card this step can be skipped. It is still recommended to run the :doc:`update procedure </wiki-migration/resources/tools-software/linux-software/zynq_images>` to get the latest software updates.


The first step is to create and configure the SD card. Follow the instructions to `download the image and populate the SD card <https://wiki.analog.com/[[resources/tools-software/linux-software/zynq_images>`_. Make sure the you configure the BOOT partition for the SD card for the EVAL-CN0363-PMDZ + ZED board.

Setting up the Hardware
-----------------------

Follow the `hardware setup instructions <https://wiki.analog.com/../prerequisites>`_ and setup the system.

Starting the System
-------------------

After the hardware has been setup the system can be started. Turn on the main power switch on the ZED board (SW8). After a few seconds the blue DONE LED (LD12) will turn on. It takes a while for the system to be completed booted, after around 30 second you will see the following screen on the HDMI monitor. The system is now ready to use and you should see the following screen.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cn0363-pmdz/quickstart/cn0363_zed_startup_1.png
   :align: center

The "ADI IIO Oscilloscope" can be closed since it is not required for the EVAL-CN0363-PMDZ. To start the EVAL-CN0363-PMDZ colorimeter application go to the top-left **"Applications Menu"** and to the **"Other"** section and click on **"ADI CN0363 Colorimeter"**. Now you should see the following screen and you can use the EVAL-CN0363-PDMZ to perform measurements.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cn0363-pmdz/quickstart/cn0363_zed_startup_2.png
   :align: center

For more information on how to use the application see the :doc:`EVAL-CN0363-PMDZ Colorimeter Application User Guide </wiki-migration/resources/tools-software/linux-software/colorimeter>`.

More Information
----------------

-  `EVAL-CN0363-PMDZ User Guide <https://wiki.analog.com/resources/eval/user-guides/eval-cn0363-pmdz/quickstart/..>`_
