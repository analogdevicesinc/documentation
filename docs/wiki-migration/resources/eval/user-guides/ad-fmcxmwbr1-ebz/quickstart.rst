AD-FMCXMWBR1-EBZ Setup Guide
============================

The :adi:`AD-FMCXMWBR1-EBZ` is a kit of two boards connected with ribbon cables. The customer needs to plug the AD-FMCXMWBR1-EBZ module in an FMC slot on a carrier. The Protoplate Interface board should be mounted on a `32x32 X-microwave Prototype plate <https://www.xmicrowave.com/product/xm-pp2-3232-01/>`_, then connected by ribbon cables. At this point, the carrier board can be turned on and the setup can be used accordingly.

The advantage of this board is that it has a pin header compatible with the Raspberry Pi based `X-MW controller <https://www.xmicrowave.com/documentation/x-mwcontroller-touch-interface/>`_ . It uses the communication protocol pins and some GPIO pins of the Raspberry Pi. Here is the link to our wiki page where customers can find all the info they need for this board:

.. important::

   The adjustable supplies are set by default to the maximum value.


You have to plug the :adi:`AD-FMCXMWBR1-EBZ` FMC card into a carrier board. Then to have access to all the signals and power rails, build the entire setup using the cables included in the package. The board can be powered both by the FMC 12V supply or with an external supply. The external power supply is prioritized, so when this is connected the FMC 12V supply is not used.

Supported Carriers
------------------

The AD-FMCXMWBR1-EBZ is, by definition a “FPGA mezzanine card” (FMC), that means it needs a carrier to plug into. In most carriers, the AD-FMCXMWBR1-EBZ board connects to the FMC LPC connector. The carrier setup requires power, ethernet (Linux), HDMI or display port connections.

In addition to this, the AD-FMCXMWBR1-EBZ has a RaspberryPi compatible pin header that allows connection to any RaspberryPi development system.

Hardware Setup
==============

| 
| ==== FMC carrier ==== A typical setup with **ADRV9009-ZU11EG RF-SOM Complete Prototyping System** is shown below. |image1|

.. container:: centeralign

   Figure 1. AD-FMCXMWBR1-EBZ on carrier


-  First, the ADRV9009-zu11eg setup should be built. Please refer to the :doc:`ADRV9009-ZU11EG Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/quick-start-guide>`.
-  ADRV2CRR-FMC should be powered and connected to a network with the ethernet cable.
-  The screen is connected to ADRV2CRR-FMC through a display port cable. If there is no image shown on the screen at the first boot, please refer to the :doc:`guide </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`.
-  Connect the USB OTG adapter and plug the USB Port Hub. In the Port hub will be connected the keyboard and the QR code scanner.
-  Plug the AD-FMCXMWBR1-EBZ into the FMC connector of the ADRV2CRR-FMC.
-  Use the cables provided in the kit to connect the AD-FMCXMWBR1-EBZ to the desired setup.

| 

X-MW controller
---------------

|

| AD-FMCXMWBR1-EBZ has a pin header compatible with both the X-MW controller and the Raspberry Pi. It can be connected with a 40pin Ribbon cable to the controller, and with the cables in the kit is connected to the X-microwave setup.

| |image2|

.. container:: centeralign

   Figure 2. Diagram of AD-FMCXMWBR1-EBZ with a X-MW controller


| ====Raspberry Pi====
| The AD-FMCXMWBR1-EBZ can be used with a standalone Raspberry Pi. It doesn't have as many benefits as the setup with a FPGA board, but it can simplify the wiring and power supplies needed in an X-microwave prototype.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/phaser_proto_xmw_bridge.jpg
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 3. AD-FMCXMWBR1-EBZ in a test setup with RaspberryPi


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/adrv9009-adfmcxmwsetup.png
   :width: 700px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz/xmwcontrollersetup.png
   :width: 800px
