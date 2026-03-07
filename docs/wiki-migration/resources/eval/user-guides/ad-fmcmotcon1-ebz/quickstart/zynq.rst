AD-FMCMOTCON1-EBZ Linux on Zynq Quick Start Guide
=================================================


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#retired>`_
 This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the AD-FMCMOTCON1-EBZ on either:

-  `ZED Board <http://www.zedboard.org/>`_, Rev C or later

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
