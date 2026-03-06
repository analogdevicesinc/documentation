ADRV-PACKRF Production Testing
==============================

Overview
--------

Production tests for ADRV-PACKRF BOX are composed of a series of Bash scripts that run both on Raspberry Pi and DUT (Device under test). The tester only interacts with the Raspberry Pi through a keyboard and monitor. Connected to the Raspberry PI should be an HDMI display where information about tests, required tester actions and results are displayed.

Assembling of the box is split in two phases (Partial Assembly and Full Assembly). After each assembly phase the corresponding testing batch must be run.

If one of the test fails the testing sequence will stop and "FAILED" message will be printed. Tester can get information related to what component failed. After that he can either try to test again or mark the tested device as defective.

A set of log files is created and stored on Raspberry PI SD card. These logs can be used to supervise the testing process.

The complete test jig should look like:


|image1|

Required Hardware
-----------------

-  1 PACKRF box

   -  1 MicroSD card prepared for PACKRF

-  1 Raspberry PI

   -  1 MicroSD card prepared for Raspberry PI

-  1 5V-Micro USB power supply for Raspberry PI
-  1 DC Wallwart (12V, 3A)
-  1 POE Injector BOX
-  2 Ethernet cables

   -  One connected Raspberry PI <-> POE Injector Data IN
   -  One connected POE Injector Data OUT <-> PACKRF

-  1 USB media drive with type A to micro OTG adapter
-  1 SMA <-> SMA loopback cable
-  1 pair of headphones CTIA standard with media buttons
-  1 loopback TRRS jack
-  1 ADALM PLUTO used for GPS spoofing
-  1 SMA DC blocker

Test Setup
----------

-  Complete :doc:`Partial Assembly </wiki-migration/resources/eval/user-guides/pzsdr/carriers/portable-radio-reference-design/assembly-instructions>` of the radio.
-  Connect an HDMI monitor to the Raspberry Pi.
-  Connect a USB keyboard to the Raspberry PI.
-  Connect an Ethernet cable to the Raspberry Pi and Radio.

   -  The Ethernet port of the Raspberry PI is configured with static IP and a DHCP server is running on it. So is not recommended to connect anything other than the POE-Injector or the RFSOM-BOX.

-  Connect a 5V Power Supply to the "PWR IN" port of the Raspberry PI.
-  Turn on the Raspberry Pi. After it powers on it should boot up Linux and the testing screen should be visible on the monitor.
-  Connect DC Wall wart adapter and POE Injector to SOM-BOX PCB.

PACKRF SD card
~~~~~~~~~~~~~~

The SD card image used for production testing has no differences compared to the one prepared for shipping of the PackRF. To create it please follow the instructions presented here: :doc:`Zynq & Altera SoC Quick Start Guide </wiki-migration/resources/tools-software/linux-software/zynq_images>` and here: :doc:`SD card update </wiki-migration/resources/tools-software/linux-software/zynq_images>` sub-section "User Space Tools"

Raspberry PI SD card
~~~~~~~~~~~~~~~~~~~~

The SD image used is based on Raspbian Stretch with desktop. On top of that the "setup_env.sh" script should be run to prepare the testing framework.

To set the PI SD card please follow the steps:

-  Write a clean Raspbian Stretch with desktop image to a minimum 8GB SD card.

   -  Download the following zip file: `Raspbian latest <https://downloads.raspberrypi.org/raspbian_latest>`__.
   -  Write it to the SD card following the instructions presented here: `Installing PI images <https://www.raspberrypi.org/documentation/installation/installing-images/>`__.

-  Boot Raspberry PI with newly created card and establish internet connection on PI through Ethernet or WiFi
-  Download the test frame repository from git: "placeholder_path" and save the whole folder in /home/pi/
-  open a terminal on Raspberry, change directory to /home/pi/rfsom-box-production-test
-  run the setup_env.sh script "./setup_env.sh rfsom-box jig"
-  after script execution ended, disconnect Ethernet cable from PI and reboot it
-  The PI should display after boot the test screen

Step 1 - Partial Assembly Test
==============================

This test sequence can only be started once :doc:`Partial Assembly </wiki-migration/resources/eval/user-guides/pzsdr/carriers/portable-radio-reference-design/assembly-instructions>` is complete.

The following items will be tested:

-  Power supply voltage output
-  Charging, Battery
-  Ethernet
-  USB
-  Real Time Clock
-  UART communication with GPS module
-  Audio CODEC and Audio Connector

Test Procedure
~~~~~~~~~~~~~~

-  Insert the PACK-RF SD card in the carrier card slot
-  Connect the DC adapter barrel power connector
-  Connect the Ethernet cable that exit POE injector
-  Press and release the power button.
-  Wait for the system to boot up.
-  On test station display the following image should be visible:
-

|guides:pzsdr:carriers:packrf:start_screen.jpg|

-  Select option 1 to begin "Pre Assembly Test"
-  Communication with device under test is established and test should start.
-  If connection can't be established "Check Ethernet connection to DUT" warning will be displayed
-  While test is running a log is printed on display.
-  In picture bellow is presented a case where POE supply testing failed.
-

|image2|

-  If all required tests are passed the following message should be visible:
-

|image3|

-  Either previous test set passed or failed the selection menu will be printed on screen
-  Now RFSOM-BOX should be powered off by entering "4" in the selection menu
-  Continue with :doc:`Full Assembly </wiki-migration/resources/eval/user-guides/pzsdr/carriers/portable-radio-reference-design/assembly-instructions>`

Step 2 - Full Assembly Test
===========================

This test sequence can only be started once :doc:`Full Assembly </wiki-migration/resources/eval/user-guides/pzsdr/carriers/portable-radio-reference-design/assembly-instructions>` is complete.

The following items will be tested:

-  RF front-end (Transmit and Receive with SMA connectors)
-  Inertial Measurement Unit
-  GPS Satelite Locking (PLUTO GPS spoofer required)
-  Display
-  Navigation Switch / Rotary Encoder

.. _test-procedure-1:

Test Procedure
~~~~~~~~~~~~~~

-  Press and release the BOX power button.
-  Wait for the system to boot up. "Analog Devices" screen should be visible on box screen.
-  From the test selection screen now select option “2”
-  Full assembly testing should start
-  RF testing requires making connections between different SMA connectors using SMA <-> SMA loop-back cable
-

|image4|

-  Image below shows how the result of RF testing should look after all nine connections were tested
-

|image5|

-  If one of the pairs failed it can be because cables are bad, connections are bad or cables are swapped between them
-  IMU testing requires physical movement of the RFSOM-BOX
-  GPS module testing requires an ADALM PLUTO connected through a DC BLOCK and SMA <-> SMA cable to the GPS port of DUT. The PLUTO board will generate GPS signals and DUT should acquire location, speed and time. Locking has a timeout of 120 seconds. If no locking is acquired in this time interval the test is failed.
-  After testing is finished and PASSED/FAIL state displayed the RFSOM-BOX should be turned off selecting option "4"
-  :doc:`PackRF assembly </wiki-migration/resources/eval/user-guides/pzsdr/carriers/portable-radio-reference-design/assembly-instructions>` and testing is complete.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/packrf_test_jig.jpg
   :width: 600px
.. |guides:pzsdr:carriers:packrf:start_screen.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/start_screen.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/pre_assemb_fail.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/partial_assemb_pass.jpg
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/sma_loopback.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/packrf/rf_test.png
   :width: 600px
