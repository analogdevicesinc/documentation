AD-FMCDAQ3-EBZ Zynq ZC706 Quick Start Guide
===========================================

This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the AD-FMCDAQ3-EBZ on:

-  `ZC706 <https://www.xilinx.com/ZC706>`__ (rev 1.1 or higher)

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq3-ebz/software/linux/ad-fmcdaq3-ebz_zc706.png
   :width: 600px

.. important::

   The ZC706 is build around a XC7Z045 FFG900 – 2 FPGA, which means the design will be overclocked when configured for 1233MSPS. In a production design a XC7Z045 FFG900 –3 FPGA should be used or the lane rate should be within the supported range for the specific FPGA.


Requirements
------------

-  You need a Host PC (Windows or Linux).
-  You need a SD card writer connected to above PC (Supported USB SD readers/writers are OK).
-  USB keyboard/mouse for the Zynq or ZED Device
-  HDMI Display (monitor or TV) (FULL HD only!)

Creating / Configuring the SD Card
----------------------------------

:doc:`Create SD Image for Zynq Boards. (it is a single image for all boards) </wiki-migration/resources/tools-software/linux-software/zynq_images>`

.. esd-warning::


Setting up the hardware (ZC706)
-------------------------------

You will need to:

-  Get the `ZC706 <https://www.xilinx.com/ZC706>`__:

   -


   |http://www.xilinx.com/images/product-images/zc706-base-board.jpg|

-  Insert the SD-CARD into the SD Card Interface Connector (J30)
-  Plug the AD-FMCDAQ3-EBZ into the HPC Connector
-  Plug your HDMI display device into the HDMI Video Connector (P1)
-  Plug your USB mouse/keyboard into the USB 2.0 ULPI Controller, w/Micro-B Connector (J49)
-  Plug the Power Supply into 12V Power input connector (J22) (DO NOT turn the device on).
-  Set the jumpers: The main one is: SW11 - Big Blue Switch in the middle, which controls the Boot Mode, it needs to be set: 1: Down, 2: Down, 3: Up, 4: Up, 5: Down. Other Jumpers can be checked via looking at the picture. (click the picture to make it bigger)

|zc706plusfmcjesdadc1.png|

-  Turn it on.
-  Wait ~30 seconds for the "DONE" LED to turn green. This is above the power switch.
-  Wait another ~30 seconds for the HDMI display device to start showing signs of life.
-  The follow the instructions for the type of demo that you want to do.

Booting the SD Card
-------------------

-  ignore your PC, and now interact on the USB mouse/keyboard on the Zynq device
-  You should see two screens:

   -  IIO Scope tool:
      |image1|\ |image2|

      -  Learn more about the :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`.

-  You are done. You can interact with the GUI either over the network, or with the HDMI monitor/USB keyboard mouse.

|

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with

   | ``sudo shutdown -h now``
   
   |image3|


.. |http://www.xilinx.com/images/product-images/zc706-base-board.jpg| image:: http://www.xilinx.com/images/product-images/zc706-base-board.jpg
.. |zc706plusfmcjesdadc1.png| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/zc706plusfmcjesdadc1.png
   :width: 200px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq3-ebz/quickstart/plot_window.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq3-ebz/quickstart/daq3_plugin.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
   :width: 300px
