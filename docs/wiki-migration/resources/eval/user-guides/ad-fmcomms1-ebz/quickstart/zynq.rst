AD-FMCOMMS1-EBZ Zynq Quick Start Guide
======================================


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#retired>`_


This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the AD-FMCOMMS1-EBZ on either:

-  `ZC702 <https://www.xilinx.com/ZC702>`_
-  `ZC706 <https://www.xilinx.com/ZC706>`_
-  `ZED Board <http://zedboard.org/product/zedboard/>`_, Rev C or later

Requirements
------------

-  You need a Host PC (Windows or Linux).
-  You need a SD card writer connected to above PC (Supported USB SD readers/writers are OK).
-  USB keyboard/mouse for the Zynq Device
-  HDMI Display (monitor or TV)
-  Antenna, or SMA cable for crossing Tx to Rx.

Creating the SD Card
--------------------

:doc:`Create SD Image for Zynq Boards </wiki-migration/resources/tools-software/linux-software/zynq_images>`

Booting the SD Card
-------------------

-  ignore your PC, and now interact on the USB mouse/keyboard on the Zynq device
-  You should see the following screen:

   -  IIO Scope tool:


   |image1|

      -  Learn more about the :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`.

-  You are done. You can interact with the GUI either over the network, or with the HDMI monitor/USB keyboard mouse.

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``


   |image2|

.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/iio_scope.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
   :width: 300px
