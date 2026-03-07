AARDVARK
========

Totalphase's `AARDVARK <https://www.totalphase.com/products/aardvark-i2cspi>`_ can be used as a replacement for USBi board.

AARDVARK channel can be found under communication channel as shown below.


|image1|

AARDVARK can be connected to ICs same way as the USBi.


|image2|

Multiple AARDVARKs can be connected to the same SigmaStudio instance and each AARDVARK can be connected to a different ICs. Serial ID printed on the AARDVARK device will be displayed along with the I2C address/SPI select options. This feature is supported only from SigmaStudio 4.0.

Please note that `AARDVARK USB driver <https://www.totalphase.com/products/usb-drivers-windows/>`_ should be installed separately before using the AARDVARK with the sigmastudio.

Example
-------

The below example shows how to connect 2 AARDVARKs with the 2 different boards/ICs. The example below takes uses 2 ADAU1701 Evaluation boards (:adi:`EVAL-ADAU1701MINIZ <media/en/technical-documentation/evaluation-documentation/EVAL-ADAU1701MINIZ.pdf>`)

| 
| 1. First, install the recent AARDVARK USB driver from TotalPhase.
| 2. Connect both the AARDVARK devices to the same Laptop/Machine using different USB ports.
| 3. Create a schematic and drag and drop 2 AARDVARKs from the 'Communication Channels'
| 4. Connect first AARDVARK to IC1 in the schematic. And connect the second AARDVARK to IC2. If you select the combo-box both the AARDVARKs should be listed for each I2C/SPI configuration. |image3| Please note that 2 AARDVARK devices are listed as Serial Number #1 (2238405722) and Serial Number #2 (2238289772). These serial number will be printed on top of the AARDVARK device as well.
| 5. Connect the AARDVARK device with Serial number #1 to first AUAU1701 MINZ. And the select the same AARDVARK in the schematic as well for the AUAU1701 IC1.

6. Connect the AARDVARK device with Serial number #2 to second AUAU1701 MINZ. And the select the same AARDVARK in the schematic as well for the AUAU1701 IC2.

7. Create the signal chain and Link compile download. Both the boards should play audio.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/gettingstarted/usbinterfaces/aardvark2.jpg
   :align: center

You can download the `attached schematic <https://wiki.analog.com/_media/resources/tools-software/sigmastudio/gettingstarted/usbinterfaces/aardvark_test.zip>`_ as an example.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/gettingstarted/usbinterfaces/aardvark1.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/gettingstarted/usbinterfaces/aardvark3.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/gettingstarted/usbinterfaces/aardvark1.jpg
