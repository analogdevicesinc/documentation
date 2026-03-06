AD-FMCOMMS2/3/4/5-EBZ Zynq and ZED Quick Start Guide
====================================================

This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the AD-FMCOMMS2-EBZ or AD-FMCOMMS3-EBZ or AD-FMCOMMS4-EBZ or AD-FMCOMMS5-EBZ on either:

-  `ZC702 <https://www.xilinx.com/ZC702>`__ (FMCOMMS2/3/4/5)
-  `ZC706 <https://www.xilinx.com/ZC706>`__ (FMCOMMS2/3/4/5)
-  `ZED Board <http://zedboard.org/product/zedboard/>`__ (FMCOMMS2/3/4)

Which board you want to use is completely up to you. There isn't much of a difference from evaluation of the transceiver standpoint - the difference is really up to you, and how much you want to add into the FPGA for your specific/custom design. (The ZC706 [1]_ includes a much larger FPGA , which includes for your custom design than what exists on the ZC702 [2]_, or ZED Board [3]_).

The base functionality (play, and record RF waveforms) is the same on any platform.

Requirements
------------

-  You need a Host PC (Windows or Linux).
-  You need a SD card writer connected to above PC (Supported USB SD readers/writers are OK).
-  USB keyboard/mouse for the Zynq or ZED Device
-  HDMI Display (monitor or TV) (FULL HD only!)
-  Antenna, or SMA cable for crossing Tx to Rx.

Creating / Configuring the SD Card
----------------------------------

Create the :doc:`SD Image </wiki-migration/resources/tools-software/linux-software/zynq_images>` for Zynq/ZED Boards. (it is a single image for all boards)

.. esd-warning::


Setting up the hardware (ZC706)
-------------------------------

You will need to:

-  Get the `ZC706 <https://www.xilinx.com/ZC706>`__

   -


   |http://www.xilinx.com/images/product-images/zc706-base-board.jpg|

-  Prepare the SD card with the proper Linux image (from :doc:`here </wiki-migration/resources/tools-software/linux-software/zynq_images>` and pay attention to the Linux/Windows setup).
-  Insert the SD-CARD into the SD Card Interface Connector (J30)
-  Plug the AD-FMCOMMS2-EBZ into the LPC LPC Connector (J5)
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

-  Ignore your PC, and now interact on the USB mouse/keyboard on the Zynq device
-  You should see the following screen:

   -  IIO Scope tool:
      |image1|\ |image2|

      -  Learn more about the :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`.

-  You are done. You can interact with the GUI either over the network, or with the HDMI monitor/USB keyboard mouse.

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``


   |image3|

Setting up the hardware (ZED)
-----------------------------

You will need to:

-  Get the `ZED Board <http://zedboard.org/product/zedboard>`__
-  Set the Jumpers and Switches accordingly like shown on the picture. (click on the picture to enlarge)\ |ZED Board prepared|\ Boot (JP7-JP11) and MIO0 (JP6) jumpers are set to SD card mode. To use USB peripheral devices with ZedBoard, install jumpers JP2 and JP3. The FMC interface spans over two PL I/O banks, banks 34 and 35. To meet the FMC spec, these banks are powered from an adjustable voltage set by jumper, J18. Selectable voltages include 1.8V, default, and 2.5V.
-  Prepare the SD card with the proper Linux image (see :doc:`here </wiki-migration/resources/tools-software/linux-software/zynq_images>` and pay attention to the Linux/Windows setup)
-  Insert the SD-CARD into the SD Card Interface Connector (J12)
-  Plug the AD-FMCOMMS2-EBZ or AD-FMCOMMS3-EBZ into the LPC Connector (J1)
-  Plug your HDMI display device into the HDMI Video Connector (J9)
-  Plug your USB hub into the USB 2.0 socket w/Micro-B Connector (J13)
-  Connect mouse and keyboard to your USB hub.
-  Power up the USB-HUB
-  Plug the Power Supply into 12V Power input connector (J20) (DO NOT turn the device on).
-  Turn on the TV/Monitor, verify "Overscan" is on (visualizing the entire picture till to the edge), verify the HDMI channel.
-  Turn on the power to the ZED Board
-  1 green LED on the ZED, 1 green on the AD-FMCOMMS2 shall turn on immediately
-  Wait ~15 seconds for the blue and another green LED on the ZED Board.
-  Wait another ~30 seconds for the HDMI display device to start showing signs of life. (Linux TUX top left)
-  Follow the instructions for the type of demo that you want to do on screen.

**Note:** For more detailed information on the ZedBoard jumper settings, check out the *ZedBoard Hardware User Guide*, available on the `ZedBoard doc page <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard>`__, the *Jumper Settings* chapter.

.. tip::

   If you want to manually build the HDL project and make the BOOT.BIN, see :doc:`this tutorial </wiki-migration/resources/fpga/docs/build>`. For the Zynq Linux kernel and the devicetree, check :doc:`this tutorial </wiki-migration/resources/tools-software/linux-build/generic/zynq>`.


Setup/Wiring. (click to enlarge):

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zed_setup.jpg
   :width: 300px

**Note:** For proper robustness shield the ZED board with a plexi-glass cover. Add a "Touch-Screw" (A2, stainless steel) and connect it via a 270kOhm resistor to a GND pin. Touch this screw prior any handling of any board. It ensures proper and painless ESD discharge.

.. [1]
   XC7Z045-FFG900-2, 350K Logic Cells

.. [2]
   XC7Z020-CLG484 -1, 85K Logic Cells

.. [3]
   XC7Z020-CLG484 -1, 85K Logic Cells

.. |http://www.xilinx.com/images/product-images/zc706-base-board.jpg| image:: http://www.xilinx.com/images/product-images/zc706-base-board.jpg
.. |zc706plusfmcjesdadc1.png| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/zc706plusfmcjesdadc1.png
   :width: 200px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/fmcomms2-iio-osc.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/fmcomms2-osc-plugin.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
   :width: 300px
.. |ZED Board prepared| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zed_sw.png
   :width: 400px
