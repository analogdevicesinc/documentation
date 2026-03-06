:doc:`Link to parent page </wiki-migration/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end>`

2-24 GHz Reference Design Hardware Prototyping
==============================================

This page will detail the prototype hardware that ADI is developing to prove out and prototype this reference design. The hardware is composed of 2 main platforms:

-  2 to 24 GHz RX Engineering Platform
-  2 to 24 GHz TX Engineering Platform

Each platform is composed of 4 primary pieces of hardware:

-  X-Microwave RF Signal Chain (`X-Microwave Reference Design Kits <https://quanticxmw.com/reference-design-kits/>`__)
-  AD9082 Evaluation Board (:adi:`AD9082-FMCA-EBZ <eval-ad9082>`)
-  ZCU102 Evaluation Board (`EK-U1-ZCU102-G <https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g.html>`__)
-  ADI's X-Microwave Bridge Board (:adi:`AD-FMCXMWBR1-EBZ`)

Additional pieces of hardware will be needed, such as cables, test equipment and power supplies.

With these 4 key pieces of hardware, the full signal chain (including Digitizer) can be evaluated for functionality and performance. Additionally, all control of the signal chain is conducted from a central location (FPGA on the ZCU102), which allows for coordinated control system prototyping.

| Below is a diagram showing how these pieces will fit together to complete the prototyping system. |image1|
| Once the hardware is connected as pictured above, the pinouts for the XMW bridge board can be distributed to the components in the signal chain to interface with the hardware platform. The following block diagram shows the receiver signal chain with LO circuits and XMW bridge board pinouts connected: |image2|
| The following block diagram shows the transmit signal chain with LO circuits and XMW bridge board pinouts connected: |image3|
|

.. important::

   This Hardware is currently in development. We expect to have results of our prototyping posted soon.


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/prototypingplatformhw.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/updatedrxcontrol.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/updatedtxcontrol.png
