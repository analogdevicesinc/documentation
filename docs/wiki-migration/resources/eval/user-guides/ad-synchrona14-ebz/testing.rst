Production testing of the AD-SYNCHRONA14-EBZ
============================================

Overview
--------

The production testing is quite simple. Since each board has been completely characterized, and we know the layout is good, we can just look for gross errors.

There are multiple test files for the different boards. (all in GitHub)

-  synchrona_test_name_prod

The tests and test parameters are in the production testing file. This is broken down into the following sections:

::

   -Front panel output channels
   -Back panel input channels
   -UART ports and SPI communication
   -Miscellaneous

Required hardware
-----------------

-  AD-SYNCHRONA14-EBZ
-  Raspberry Pi4
-  ADALM2000
-  ADALM2000 BNC Adapter
-  BR-068851 with ribbon cable and a single wire
-  Twinax Cable Assembly
-  Micro-USB
-  Ethernet cable
-  QR code scanner
-  Mouse and Keyboard
-  Dymo LabelWriter450

Required software
-----------------

**Creating an AD-SYNCHRONA14-EBZ SD test card**

Firstly, write the latest available SD card image found to a spare card to boot into Linux.

.. admonition:: Download
   :class: download

   
   -  \**22 June 2022 release \*\*
   -   `Actual file <https://swdownloads.analog.com/cse/prod_test_rel/synchrona_test/synchrona_production_small.zip>`_
   


\*\* Creating a Raspberry Pi SD test card \*\*

The SD image used is based on Raspbian with Desktop.

.. admonition:: Download
   :class: download

   
   -  \**22 June 2022 release \*\*
   -   `Actual file <http://swdownloads.analog.com/cse/prod_test_rel/synchrona_test/rpi_synchrona_production.zip>`_
   


.. tip::

   To write an image on a SD card you can follow the instructions `Installing Pi Images <https://www.raspberrypi.com/documentation/computers/getting-started.html>`_\


Required setup
--------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/test_setup_s.png
   :align: center

-  Connect the BNC adapter to the ADALM2000 and attach the Back Panel and Front Panel SMA cables.
-  Connect the ADALM2000 USB cable to one of the SYNCHRONA14 USB ports
-  Connect the Raspberry Pi pins via ribbon cable to the BR-068851 and connect the two using a USB cable.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/picture3.jpg
   :align: right

-  Make sure you have added a wire to V_IO select on the BR-068851 and also a jumper on EN pins. See below photo for reference.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/picture2.png
   :align: right

-  Connect an Ethernet cable between the Pi and Synchrona
-  Add the scanner and keyboard USBs to the Raspberry Pi, and also an external display
-  Connect the Dymo LabelWriter450 label printer to the Raspberry Pi via USB.
-  Power on the Raspberry Pi by plugging in the USB-C power supply
-  Power on the Synchrona board by pressing the power button on the front panel an wait ~30sec

Test process
------------

Firstly, make sure all the required steps from the setup explained above are completed. Once the setup is ready, testing should be done using the following steps:

-  Once you have powered on both Synchrona and the Raspberry Pi, you should be prompted with the following test window on your display.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/test_1.png
   :align: right

-  Type '1' in order to start the production testing
-  Start by scanning the serial number QR code on Synchrona

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/test_2.png
   :align: center

-  Firstly, we will test the outputs on the front panel of Synchrona. Attach the front panel SMA cable to Channel 01, port P and press 'Enter' when ready.\


|image1|

-  Proceed doing the same process for each 'P' and 'N' ports of the channels.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/test_4.png
   :align: right

-  For channels 11-14, attach the front panel cable to the Twinax to SMA adapter. Use the new probe to test.\


|image2|

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/testt_5.png
   :align: right

-  The next step is testing the inputs, on the back panel. Use the SMA cable for back panel and attach it one at a time to REF IN, PPS, CH2 and CH3. \**For CH2 and CH3 inputs you only need to connect to one of the SMA connectors, P or N. On the input (P or N) you are not connecting the SMA cable place a SMA 50 Ohm terminator. \*\*

::

   * 

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/50ohm.jpg
   :align: center
   :width: 300px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/backpanel.jpg
   :align: right

-  In order to test the UART COMM 01, 02 and the SPI Communication, attach a BR-068851 to the GPIO port on the back panel.

|image3| |image4|

-  Next, check if the LED STAT1 is yellow and STAT2 red, check if the Synchrona fan is working.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/test_8.png
   :align: right

-  After these steps, the board will power-off and display a message asking you to power up Synchrona in order to perform clean-up. Remove the BR-068851 board from the Synchrona before powering it back on.


|image5|

.. important::

   Make sure to reboot the board in order to perform clean-up.


-  Make sure you have connected the Dymo LabelWriter 450 printer via USB to the Rasperry Pi. A label will be printed that must be placed on the back of the board. See below image for reference.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/label_synchrona.jpg
   :align: right

-  A 'PASSED' or 'FAILED' message should appear on the screen at the end of the test.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/passed_final.png
   :align: center

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/channel1_test.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/channel11.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/gpio.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/test_6.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-synchrona14-ebz/synchrona_clean_up.jpg
