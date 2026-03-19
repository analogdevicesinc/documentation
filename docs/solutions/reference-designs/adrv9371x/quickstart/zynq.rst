ADRV9371/PCBZ Zynq Quick Start Guide
====================================

This guide provides some quick instructions (still takes awhile to download, and
set things up) on how to setup the ADRV9371/PCBZ:

-  `ZC706 <https://www.xilinx.com/ZC706>`_

Requirements
------------

-  You need a Host PC (Windows or Linux).
-  You need a SD card writer connected to above PC (Supported USB SD readers/writers are OK).
-  USB keyboard/mouse for the Zynq or ZED Device
-  HDMI Display (monitor or TV) (FULL HD only!)
-  Antenna, or SMA cable for crossing Tx to Rx.
-  Reference clock source

Creating / Configuring the SD Card
----------------------------------

`Create SD Image for Zynq boards. (it is a single image for all boards) <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

.. esd-warning::

Setting up the hardware (ZC706)
-------------------------------

You will need to:

-  Get the `ZC706 <https://www.xilinx.com/ZC706>`_:

   -

   |http---www.xilinx.com-images-product-images-zc706-base-board.jpg|

-  Insert the SD-CARD into the SD Card Interface Connector (J30)
-  Plug the ADRV9371/PCBZ into the HPC FMC Connector
-  Plug your HDMI display device into the HDMI Video Connector (P1)
-  Plug your USB mouse/keyboard into the USB 2.0 ULPI Controller, w/Micro-B Connector (J49)
-  Plug the Power Supply into 12V Power input connector (J22) (DO NOT turn the device on).
-  Set the jumpers: The main one is: SW11 - Big Blue Switch in the middle, which
   controls the Boot Mode, it needs to be set: 1: Down, 2: Down, 3: Up, 4: Up,
   5: Down. Other Jumpers can be checked via looking at the picture. (click the
   picture to make it bigger)

.. image:: ../images/zc706plusfmcjesdadc1.png
   :alt: zc706plusfmcjesdadc1.png
   :align: right
   :width: 200

-  Turn it on.
-  Wait ~30 seconds for the "DONE" LED to turn green. This is above the power switch.
-  Wait another ~30 seconds for the HDMI display device to start showing signs of life.
-  The follow the instructions for the type of demo that you want to do.

.. image:: ../images/mykonos_system_overview.png
   :align: center
   :width: 600

Booting the SD Card
-------------------

-  Ignore your PC, and now interact on the USB mouse/keyboard on the Zynq device
-  You should see the following screen:

   -  IIO Scope tool:

   |image1|

   -  Learn more about the `IIO Scope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_.

-  You are done. You can interact with the GUI either over the network, or with
   the HDMI monitor/USB keyboard mouse.

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``

   |image2|

.. |http---www.xilinx.com-images-product-images-zc706-base-board.jpg| image:: http://www.xilinx.com/images/product-images/zc706-base-board.jpg
.. |image1| image:: ../images/s56mc2_3.png
   :width: 200
.. |image2| image:: ../images/shutdown.png
   :width: 300

.. |http---www.xilinx.com-images-product-images-zc706-base-board.jpg| image:: https://wiki.analog.com/_media/http///www.xilinx.com/images/product-images/zc706-base-board.jpg
