AD-FMCOMMS11-EBZ Zynq Quick Start Guide
=======================================

This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the AD-FMCOMMS11-EBZ on:

-  `ZC706 <https://www.xilinx.com/ZC706>`__

Requirements
------------

-  You need a Host PC (Windows or Linux).
-  You need a SD card writer connected to above PC (Supported USB SD readers/writers are OK).
-  USB keyboard/mouse for the Zynq
-  HDMI Display (monitor or TV) (FULL HD only!)
-  Antenna, or SMA cable for crossing Tx to Rx.

Creating / Configuring the SD Card
----------------------------------

:doc:`Create SD Image for Zynq/ZED Boards. (it is a single image for all boards) </wiki-migration/resources/tools-software/linux-software/zynq_images>`

.. esd-warning::


Setting up the hardware (ZC706)
-------------------------------

You will need to:

-  Get the `ZC706 <https://www.xilinx.com/ZC706>`__:

   -


   |http://www.xilinx.com/images/product-images/zc706-base-board.jpg|

-  Insert the SD-CARD into the SD Card Interface Connector (J30)
-  Plug the AD-FMCOMMS11-EBZ into the HPC Connector (J37)
-  Plug your HDMI display device into the HDMI Video Connector (P1)
-  Plug your USB mouse/keyboard into the USB 2.0 ULPI Controller, w/ Micro-B Connector (J49). You will have to use a USB hub to connect both mouse and keyboard. Some keyboards have a mouse or touch pad sharing the same USB connection or wireless dongle. This can be used to eliminate the use of a USB hub.
-  Plug the Power Supply into 12V Power input connector (J22) (DO NOT turn the device on yet).
-  Set the jumpers: The main one is: SW11 - Big Blue Switch in the middle, which controls the Boot Mode, it needs to be set: 1: Down, 2: Down, 3: Up, 4: Up, 5: Down. Refer to the image below.\

|image1|

-  Turn it on.
-  Wait ~30 seconds for the "DONE" LED to turn green. This is above the power switch.
-  Wait another ~30 seconds for the HDMI display device to start showing signs of life.
-  The follow the instructions for the type of demo that you want to do.

Booting the SD Card
-------------------

-  Ignore your PC, and now interact on the USB mouse/keyboard on the Zynq device
-  You should see the following screen:

   -  IIO Scope tool:
      |image2|\ |image3|

      -  Learn more about the :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`.

-  You are done. You can interact with the GUI either over the network, or with the HDMI monitor/USB keyboard mouse.

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``


   |image4|

.. |http://www.xilinx.com/images/product-images/zc706-base-board.jpg| image:: http://www.xilinx.com/images/product-images/zc706-base-board.jpg
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/zilynx_switch_settings.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/fmcomms2-iio-osc.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/fmcomms2-osc-plugin.png
   :width: 200px
.. |image4| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
   :width: 300px
