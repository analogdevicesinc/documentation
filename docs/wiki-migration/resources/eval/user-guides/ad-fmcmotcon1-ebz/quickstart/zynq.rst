AD-FMCMOTCON1-EBZ Linux on Zynq Quick Start Guide
=================================================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.

 This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the AD-FMCMOTCON1-EBZ on either:

-  `ZED Board <http://www.zedboard.org/>`__, Rev C or later

Requirements
------------

-  You need a Host PC (Windows or Linux).
-  You need a SD card writer connected to above PC (Supported USB SD readers/writers are OK).
-  USB keyboard/mouse for the Zynq Device
-  HDMI Display (monitor or TV)

Creating the SD Card
--------------------

:doc:`Create SD Image for Zynq Boards </wiki-migration/resources/tools-software/linux-software/zynq_images>`

Connecting the hardware together
--------------------------------

| Instruction regarding the hardware connection can be found at:
| :doc:`Hardware connection user guide ZED board </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/quickstart/lv_setup_guide>`

Booting the SD Card
-------------------

-  ignore your PC, and now interact on the USB mouse/keyboard on the Zynq device
-  You should see two screens:

   -  firefox:


   |image1|

   -  IIO Scope tool:

   |image2|

      -  Learn more about the :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`.

-  You are now done with booting from the SD card. You can interact with the GUI either over the network, or with the HDMI monitor/USB keyboard mouse.

Using IIO SCOPE for AD-FMCMOTCON1-EBZ
-------------------------------------

:doc:`Software user guide </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/software/iio_scope>`

|

.. important::

   Even thought this is Linux, this is a persistent file system. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with:

   | ``sudo shutdown -h now``
   | |image3|


.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#none#../
   :alt: Overview#chipscope|ISE Project with Chipscope

.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/firefox.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/iio_scope.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
   :width: 300px
