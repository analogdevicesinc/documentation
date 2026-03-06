GMSL with Raspberry Pi Adapters
===============================

Create a full GMSL Camera System with off the shelf parts.


|image1|

Overview
--------

Developing quick proof of concept GMSL Camera systems can be achieved with the :adi:`AD-GMSLCAMRPI-ADP# <design-center/evaluation-hardware-and-software/evaluation-boards-kits/AD-GMSLCAMRPI-ADP.html>`\ kit. The kit includes four adapter boards which can be broken apart into a GMSL CSI-Serializer EVKIT adapter, a GMSL CSI-2 Deserializer EVKIT adapter, and two 15-pin to 22-pin adapters. For more information about this adapter see the :doc:`AD-GMSLCAMRPI-ADP# User Guide </wiki-migration/resources/eval/user-guides/ad-gmslcamrpi-adp>`

By creating an RPi camera adapter for the GMSL CSI-2 EVKIT, GMSL CSI-2 camera SerDes can be quickly connected to the existing ecosystem of RPi camera connectivity. Beyond Raspberry Pi there are many other available camera and SoC platforms which interface to this RPi connector. In addition to the standard 15-pin RPi connector there is also the 22-pin connector. The 15-pin connector is typically a 2-lane CSI-2 interface whereas the 22-pin a 4-Lane interface. To fully utilize the bandwidth of GMSL SerDes of 2x4-Lane ports a dual 22-pin connector was placed on the adapter boards.

.. image:: https://wiki.analog.com/_media/playground/wikigmsladptop.png
   :width: 400px

--------------

Camera Connections
------------------

Connect RPi 15-pin cameras to GMSL Serializer EVKIT's with the 15-22 pin adapter or use a single MAXCAM2 camera module.

|image2|-OR-|image3|

--------------

SoC Connections
---------------

The same configuration is used for the SoC side where the 22-pin adapter can be directly connect to a Jetson Orin Development kit or use the 22-15 pin adapter to connect to an Raspberry Pi.

|image4| -OR - |image5|

.. |image1| image:: https://wiki.analog.com/_media/playground/wikigmslblock.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/playground/wikigmslcamadpser.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/playground/wikigmslmaxcam2cs.png
   :width: 200px
.. |image4| image:: https://wiki.analog.com/_media/playground/wikigmsladpdesjeto.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/playground/wikigmsladpdesrpi4.png
   :width: 400px
