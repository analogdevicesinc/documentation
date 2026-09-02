.. _ad-synchrona14-ebz production_testing:

Production Testing
==================

Overview
--------

The purpose of this test procedure is to identify connectivity issues, poor
soldering, and potential manufacturing defects in the :adi:`AD-SYNCHRONA14-EBZ`
board. Some issues are directly identified by explicit part-targeted tests,
while others are detected implicitly by running adjacent tests.

Test Duration
-------------

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Step Description
     - Estimated Time (minutes)
   * - Test bench setup
     - 10 min
   * - Software test
     - 15 min
   * - **Total time**
     - **25 min**

Test Requirements
-----------------

Required Hardware
~~~~~~~~~~~~~~~~~

* :adi:`AD-SYNCHRONA14-EBZ` board
* Raspberry Pi 4, power cable (USB-C), HDMI cable
* :adi:`ADALM2000` with BNC adapter
* BR-068851 connector board with ribbon cable
* Twinax cable assembly
* Micro-USB cable
* Ethernet cable
* QR code scanner
* Mouse and keyboard
* Dymo LabelWriter450 printer
* Front panel SMA cable
* Back panel SMA cable
* 50 Ohm terminator

Required Software
~~~~~~~~~~~~~~~~~

* SD card with the test image

Required Setup
~~~~~~~~~~~~~~

.. figure:: images/test_setup_s.png

   Test setup overview

* Insert the SD card into the Raspberry Pi.

* Connect the ADALM2000's BNC adapter to both the front and back panel SMA
  cables, with USB connection to the Synchrona board.

* Connect the Raspberry Pi's GPIO pins via ribbon cable to the BR-068851
  adapter board, which connects via USB.

  .. figure:: images/picture3.jpg

     BR-068851 connection

* Add a wire to the V_IO select pin, and configure the EN pins with a jumper.

  .. figure:: images/picture2.png

     V_IO select and EN pins configuration

* Connect an Ethernet cable between the Raspberry Pi and the Synchrona board.

* Connect the QR code scanner, keyboard, and display to the Raspberry Pi.

* Connect the Dymo LabelWriter450 printer via USB to the Raspberry Pi.

* Power on the Raspberry Pi via USB-C.

* Power on the Synchrona board by pressing the front panel power button.
  Allow approximately 30 seconds for initialization.

Test Process
------------

Starting the Test
~~~~~~~~~~~~~~~~~

* After the Raspberry Pi boots, the test screen will appear on the monitor.

  .. figure:: images/test_1.png

     Initial test screen

* Type **1** and press **ENTER** to start the **Production Testing**.

* Scan the board's serial number QR code when prompted.

  .. figure:: images/test_2.png

     QR code scanning prompt

Front Panel Output Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Test channels 1-10 by sequentially connecting the front panel SMA cable to
  each port's P and N connectors.

  .. figure:: images/channel1_test.png

     Channel 1 test

  .. figure:: images/test_4.png

     Front panel channel testing

* For channels 11-14, use the Twinax-to-SMA adapter with a probe connection.

  .. figure:: images/channel11.jpg

     Twinax adapter for channels 11-14

  .. figure:: images/testt_5.png

     Channels 11-14 testing

Back Panel Input Testing
~~~~~~~~~~~~~~~~~~~~~~~~

* Attach the back panel SMA cable to **REF IN**, **PPS**, **CH2**, and **CH3**
  inputs sequentially.

* When testing CH2 and CH3, connect to only one connector (P or N) and place
  a 50 Ohm terminator on the unconnected port.

  .. figure:: images/50ohm.jpg

     50 Ohm terminator placement

  .. figure:: images/backpanel.jpg

     Back panel connections

Communication Testing
~~~~~~~~~~~~~~~~~~~~~

* Attach the BR-068851 adapter to the GPIO port.

  .. figure:: images/gpio.jpg

     BR-068851 attached to GPIO port

* Verify UART COMM 01, UART COMM 02, and SPI communication functionality.

  .. figure:: images/test_6.png

     Communication test screen

Visual Inspection
~~~~~~~~~~~~~~~~~

* Verify that LED STAT1 displays yellow and STAT2 displays red.

* Confirm fan operation.

  .. figure:: images/test_8.png

     LED and fan verification

Cleanup
~~~~~~~

* Power off the board.

* Remove the BR-068851 adapter.

* Reboot the Raspberry Pi for cleanup operations.

  .. figure:: images/synchrona_clean_up.jpg

     Cleanup prompt

  .. important::

     Make sure to reboot the board in order to perform clean-up.

Final Steps
~~~~~~~~~~~

* The printer generates a label for placement on the board's rear.

  .. figure:: images/label_synchrona.jpg

     Label placement reference

* The test concludes with a **PASSED** or **FAILED** message displayed
  on screen.

  .. figure:: images/passed_final.png

     Test passed screen

* If all tests pass, you can move onto the next D.U.T.

* When you are done testing, press **2** and hit **ENTER** to power off the
  Raspberry Pi.
