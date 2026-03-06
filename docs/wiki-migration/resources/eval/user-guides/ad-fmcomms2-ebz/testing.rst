Production testing of the AD-FMCOMMS2 / AD-FMCOMMS3 / AD-FMCOMMS4 / AD-FMCOMMS5
===============================================================================

Overview
--------

The production testing is quite simple. Since each board has been completely characterized, and we know the layout is good, we can just look for gross errors.

There are multiple test files for the different boards. (all in GitHub)

-  test_fmcomms2-3_prod : used to test AD-FMCOMMS2-EBZ and AD-FMCOMMS3-EBZ
-  test_fmcomms4_prod: used to test AD-FMCOMMS4-EBZ
-  test_fmcomms5_prod : used to test AD-FMCOMMS5-EBZ

The tests and test parameters are in in the "**pyadi-iio/tests/test_fmcomms2-3_prod.py**" file. This is broken down into the following sections:

::

   -Temperature
   -Voltage
   * RF
   * Peaks
   * DCXO
   * Loopback

Required hardware
-----------------

-  Zynq ZC706
-  Raspberry Pi4
-  :adi:`AD-FMCOMMS2-EBZ` or :adi:`AD-FMCOMMS3-EBZ` or :adi:`AD-FMCOMMS4-EBZ` or :adi:`AD-FMCOMMS5-EBZ` card
-  RF loopback cables (2x for FMCOMMS2/3/4, 4x for FMCOMMS5)
-  External monitor connected to the Raspberry Pi via micro HDMI
-  Keyboard and mouse (with USB hub if they aren't part of a combo device)
-  Ethernet cable (needs to be plugged into the internet)
-  QR code scanner
-  For the FMCOMMS2/3/4: Frequency counter with a USB-GPIB port (tested with an HAMEG Instruments, HM8123,5.12) and with a probe and grounding clip attachment

Required software
-----------------

**Creating a ZY706 carrier SD test card**

-  First, write the latest available SD card image found to a spare card and prepare the card to boot into Linux.

.. admonition:: Download
   :class: download

   
   -  \**18 January 2022 release \*\*
   -   `Actual file for FMCOMMS4 <https://swdownloads.analog.com/cse/prod_test_rel/fmcomms4_test/zc706_fmcomms4_prod_test_2022.zip>`__
   


.. admonition:: Download
   :class: download

   
   -  \**27 June 2022 release \*\*
   -   `Actual file for FMCOMMS2-3 <https://swdownloads.analog.com/cse/prod_test_rel/fmcomms2-3_test/fmcomms2-3_carrier_production.zip>`__
   


.. admonition:: Download
   :class: download

   
   -  \**13 June 2023 release \*\*
   -   `Image for FMCOMMS5 <https://swdownloads.analog.com/cse/prod_test_rel/fmcomms5_test/fmcomms5_production.zip>`__
   -  md5sum for zip file: 9c26146636e2e59a7f7e02f89508663d
   


**Note that different board use different test scripts as seen in the following mapping:**

-  test_fmcomms2-3_prod.py - FMCOMMS2/FMCOMMS3
-  test_fmcomms4_prod.py - FMCOMMS4
-  test_fmcomms5_prod.py - FMCOMMS5

**Creating a Raspberry Pi SD test card**

-  The SD image used is based on Raspbian with desktop.

.. admonition:: Download
   :class: download

   
   -  \**18 January 2022 release \*\*
   -   `Actual Raspberry Pi file for FMCOMMS4 <https://swdownloads.analog.com/cse/prod_test_rel/fmcomms4_test/rpi_fmcomms4_production_mongo.zip>`__
   -  `Actual Raspberry Pi file for FMCOMMS2-3 <https://swdownloads.analog.com/cse/prod_test_rel/fmcomms2-3_test/rpi_fmcomss2-3_production_fast.zip>`__
   -  `Raspberry Pi image file for FMCOMMS5 <https://swdownloads.analog.com/cse/prod_test_rel/fmcomms5_test/rpi_fmcomms5_prod.zip>`__
   


.. tip::

   To write an image on a SD card you can follow the instructions `Installing Pi Images <https://www.raspberrypi.com/documentation/computers/getting-started.html>`__\


Required setup
--------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/setup_1.1.png
   :align: right

-  Attach the RF loopback cables to the board. The images at the bottom of the page show the correct placement for each type of AD-FMCOMMS board.
-  Insert the SD card into the carrier board.
-  Insert the FMCOMMS board onto the carrier
-  Connect the HDMI cable to Raspberry Pi
-  Connect USB keyboard to Raspberry Pi
-  Insert SD card into Raspberry Pi
-  Connect Ethernet cable between Raspberry Pi and the carrier
-  Connect the scanner to Raspberry Pi
-  Connect the frequency counter to Raspberry Pi
-  Power the carrier board and Raspberry Pi

|image1| |image2|

.. note::

   Before testing the board, please make sure to add a QR code sticker with the serial number as shown below.


   |image3|

Make sure to connect to your WIFI Network before testing. You can exit the test window by pressing CTRL+C in order to access the connection. Reboot the system in order to return to the test window.


|image4|

Test process
------------

Firstly, make sure all the required steps from the setup explained above are completed. Once the setup is ready, testing should be done using the following steps:

-   Power the carrier board and the Raspberry Pi. The following screen will appear once the system has booted.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/test_1.png
   :align: center

-  The testing sequence can be started by selecting one of the menu items. **In order to start testing, an Ethernet cable should be connected between Raspberry Pi and DUT**.
-  Start the DCXO test by writing the following command in the terminal: 1
-  At the beginning of every test, the connection with DUT is checked. If the connection is correctly established, the following message will be printed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/test_2.png
   :align: right

-  Use the scanner to scan the QR code on the board
-  If the DCXO test has been completed, the PASSED message will appear on the screen

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/test_4.png
   :align: center

-  Secondly, start the FMCOMMS4 test by writing the following command in the terminal: 2

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/test_5.png
   :align: center

-  In the beginning, scan the QR code on the board
-  If connections are OK, the test will begin. Below is an example of a test running:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/test_6.png
   :align: right

-  If the FMCOMMS test has been completed, the PASSED message will be printed on the screen. This means that the DUT passed all the assigned tests.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/test_7.png
   :align: center

-  If one of the tests failed, the FAILED message will be printed as in the screen capture below:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/test_8.png
   :align: center

-  In case of a failed test, the tester can repeat the test immediately. The test can be repeated an undefined number of times.
-  After completing the test, power off the carrier by typing 4. After several seconds, power off the carrier board using the physical switch.
-  In order to power off Linux, please type 3 and enter.
-  Remove the FMCOMMS card and previously used board. Return to step 1 with the next board.

.. important::

   When testing is finished, ZC706 and the Raspberry Pi should always be powered off from terminal before power is unplugged, otherwise the SD cards can be corrupted. First select item 4 to power off the carrier. After a few seconds, turn off the switch. After the ZC706 is off, the Raspberry Pi can be turned off selecting item 3.


+-----------------------------+-------------------------+-------------------------+
| RF loopback cable placement |                         |                         |
+=============================+=========================+=========================+
| |fmcomms3-loopback.jpg|     | |fmcomms4-loopback.jpg| | |fmcomms5-loopback.jpg| |
+-----------------------------+-------------------------+-------------------------+
| FMCOMMS2/3                  | FMCOMMS4                | FMCOMMS5                |
+-----------------------------+-------------------------+-------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/picture2.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/frequency_counter.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/qr_code.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/wifi_connection.png
   :width: 600px
.. |fmcomms3-loopback.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/fmcomms3-loopback.jpg
.. |fmcomms4-loopback.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/fmcomms4-loopback.jpg
.. |fmcomms5-loopback.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/fmcomms5-loopback.jpg
