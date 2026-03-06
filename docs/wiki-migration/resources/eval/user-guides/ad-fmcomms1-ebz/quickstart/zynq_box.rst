FMComms1 Demo System
====================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



Congratulations, you are about to assemble a demo system, which should have everything you need to properly demo the FMComms1 system and the Xilinx Zynq-7000 All Programmable SoC.

If you don't have a box, and you need to self assemble your kit, please refer to the standard `zynq <https://wiki.analog.com/zynq>`__ documents.

Contents:

-  1 x :adi:`AD-FMCOMMS1-EBZ` (Rev B)
-  1 x `ZedBoard <http://www.zedboard.org>`__ (Rev C)

   -  1 x USB OTG Adapter
   -  1 x AC Adapter (120V or 220V)
   -  1 x 8 Gig SD Card, with Linux image on it.

-  2 x `Pulse 4G LTE blade antennas <http://productfinder.pulseeng.com/product/SPDA24700/2700>`__
-  1 x SMA Cable
-  1 x `Logitech Keyboard (400R) <http://www.logitech.com/en-us/product/wireless-touch-keyboard-k400r>`__

Required external equipment:

-  HDMI Display device (Monitor, projector, HDMI capture card, etc) and HDMI cable.

Instructions:

-  Reseat the SD Card in the Zedboard (on bottom – J12). To ensure it didn’t come loose during shipping.
-  Plug the FMComms1-EBZ into the ZedBoard via the FMC connector (J1). Ensure that the VADJ SELECT is set to 2.5V (J18).
-  Attach either (it doesn’t matter which).

   -  Pulse Antennas to the FMComms1-EBZ Rx and Tx connectors (RF_OUT and RF_IN)
   -  SMA cable between the FMComms1-EBZ Rx and Tx connectors (RF_OUT and RF_IN)

-  Plug the USB Keyboard/Mouse into the mini USB cable, and then the USB cable into the USB OTG connector (J13). If the mouse/keyboard are wireless make sure they are turned on.
-  Connect the HDMI Display device to the Zed Board HDMI OUT connector (J9)
-  Plug the power cable into the Zed Board (J20)
-  Plug the power cable into the AC power source. You may need to swap the ends to plug in the wall.
-  Turn the Zed Board on (SW8).
-  Wait 90 seconds for the IIOscope to come up.
-  Follow the instructions on the `IIO Scope <https://wiki.analog.com/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/iio_scope>`__ page

Here are some pictures showing the FMComms1 board connected to the Zedboard:

|image1| |image2|

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/20130808_154634.jpg
   :width: 400px

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/20130808_153759.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/20130808_154712.jpg
   :width: 415px
