ADRV936X_RFSOM production testing
=================================

Overview
--------

The production test of the SOM has several built-in tests that run and return a pass or failed status. See the following list for summaries of the current tests:

-  USB media: Data is saved to an attached USB media drive, read back, and verified. If the data is different or there are other USB issues (device not attached, enumeration problems, etc) the test will fail.
-  Ethernet: The breakout board give itself a static IP address and tries to ping the computer's static address that it's directly connected to. The test passes if a response is received, otherwise it fails.
-  FPGA loopback: Electrical connectivity is tested using the test fixture attached to the breakout board by writing, reading and verifying data in the GPIO registers.
-  AD9361: The RF performance and related factors for the ad9361 part are tested via a python script. Note that all the TX<->RX loopbacks are required otherwise the tests will fail.

The script also proceeds to write required files to QSPI flash in order to allow booting from it, querying a connected frequency counter to store the actual AD9361 reference clock out frequency, as well as allowing the user to enter in the remaining suffix for the board's MAC address. These values are saved as variables and stored in the flash memory.

Power Sequencer
---------------

-  The first step towards production testing of the ADRV936x RF SOM is programming the ADM1166 Power Sequencer.
-  The instructions regarding the setup and how to program the sequencer can be found by clicking on the link below.
-  After opening the link, follow the steps that use the **USB-SDP-CABLEZ serial I/O Interface**.

.. important::

   :doc:`Sequencer programming steps </wiki-migration/resources/eval/user-guides/pzsdr/power-and-sequencing>`\


Test image
----------

The production test software running on the target device is available as a prebuilt image that can be written to an SD card in the same fashion as the ADI Zynq images. Instructions are available for writing images from :doc:`Windows </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>` or :doc:`Linux </wiki-migration/resources/tools-software/linux-software/zynq_images/linux_hosts>`.

.. admonition:: Download
   :class: download

   \* \**22 June 2022 release \*\*

   
   -  `Actual file for SOM2 Testing <https://swdownloads.analog.com/cse/prod_test_rel/adrv9361_bob/adrv9361_brk_production.zip>`__
   -  \**22 January 2016 release \*\*
   -  `Actual file for SOM2 Testing <http://swdownloads.analog.com/cse/picozed/picozed-sdr2-brk-test-2016_01_05.img.xz>`__
   -  Checksum picozed-sdr2-brk-test-2016_01_05.img.xz ``f070bb467a23d42f3bebe25f70876ed2``
   -  Checksum picozed-sdr2-brk-test-2016_01_05.img ``9fefaa3910f3d6103704978b848fbfd6``
   -  \**14 August 2020 release \*\*
   -  `Actual file for SOM2 Testing <https://swdownloads.analog.com/cse/prod_test_rel/picozed_test/picozed-sdr2-brk-test-2020_14_08.img.tar.xz>`__
   


.. important::

   It is also possible to manually create one using :doc:`these instructions </wiki-migration/resources/eval/user-guides/pzsdr/testing/sd-cards>`.


.. admonition:: Download
   :class: download

   
   -  \**27 July 2022 release \*\*
   -  `Actual file for SOM1 Testing <https://swdownloads.analog.com/cse/prod_test_rel/adrv9364_bob/adrv9364_bob_production.zip>`__
   -  \**14 August 2020 release \*\*
   -  `Actual file for SOM1 Testing <https://swdownloads.analog.com/cse/prod_test_rel/picozed_test/picozed-sdr1-brk-test-2020_14_08.img.tar.xz>`__
   


.. admonition:: Download
   :class: download

   
   -  \**27 July 2022 release \*\*
   -  `Raspberry Pi file for SOM1 Testing <https://swdownloads.analog.com/cse/prod_test_rel/adrv9364_bob/rpi_adrv9364_production.zip>`__
   -  \**22 June 2022 release \*\*
   -  `Raspberry Pi file for SOM2 Testing <https://swdownloads.analog.com/cse/prod_test_rel/adrv9361_bob/raspberry_pi_som2_test.zip>`__
   


.. important::

   It is also possible to manually create one using :doc:`these instructions </wiki-migration/resources/eval/user-guides/pzsdr/testing/sd-cards>`.


Test script
-----------

A series of bash and python scripts are used to test aforementioned functionalities and to automate post-test functions. They are used to save the board model and check AD9361 reference clock frequency in addition to writing all the required boot files to QSPI flash in order to support booting Linux directly from it.

Required hardware
-----------------

-  Frequency counter with a USB-GPIB port (tested with an `Hameg HM8123 <https://www.rohde-schwarz.com/fi/product/hm8123-productstartpage_63493-44102.html>`__) with BNC to dual-probe minigraber;
-  Raspberry Pi 4 with provided Linux image, keyboard, mouse, micro-HDMI cable, and a monitor with HDMI input;
-  1 adrv936x_rfsom breakout board and loopback test fixture;
-  1 adrv936x_rfsom module (adrv9361 or adrv9364);
-  1 microSD card with the latest Raspberry test image;
-  1 microSD card with the latest board test image;
-  1 Ethernet cable: either regular patch cable or crossover works fine;
-  1 USB media drive with type A to micro OTG adapter;
-  2 USB cables: one type A to micro to attach from the Raspberry Pi to the board's UART port and one type A to type B to attach from Raspberry Pi to the GPIB-USB controller on the frequency counter;
-  4 RF/Coaxial Cable Assembly, 90° U.FL Plug to 90° U.FL Plug (loopbacks for SOM2)
-  U.FL-LP-N2 Extraction Tool, HRS U.FL Series SMT Ultra-Miniature Coaxial Connectors, U.FL (to safely remove loopbacks)
-  QR code scanner

Required setup
--------------

-  Raspberry Pi 4 with attached mouse and keyboard running the provided scripts and an Ethernet cable plugged into both the breakout board and the Raspberry Pi. In addition, two USB cables should be plugged into the Raspberry Pi board: the first goes to the UART port on the breakout board and the second goes to the USB-GPIB module on the frequency counter.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/raspberry_pi_4_setup.jpg
   :alt: raspberry_pi_4_setup.jpg
   :align: center
   :width: 600px

-  Insert the SOM onto the breakout board.
-  Make sure the boot select switches are set to boot off the SOM's SD card and that the SD card containing the production test software is inserted. See the image below for proper boot select switch positions.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/pzsdr-som-bootselect.jpg
   :align: center

-  Connect the Ethernet cable between the Raspberry Pi and the breakout board
-  Insert the USB cable into the UART port and into the Raspberry
-  Insert the flash drive into the OTG port on the breakout board. Make sure the USB jumper is set to OTG mode on the breakout board, see the image below for confirmation of correct positioning.
-  Insert the frequency counter USB into the Raspberry Pi.
-  The "INPUT A" of the frequency counter should be attached to the pin on the fan plugin nearest to the power switch on the breakout board and to a ground location such as the pin accessible through the cutout on the side of the JTAG header. Below there's a view of the probe locations. Also, note the labels on the USB ports in order to plug them in the right locations for the media drive and UART connection to the Raspberry Pi.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/pzsdr2-test-setup.jpg
   :align: center
   :width: 600px

-  SOM2 has loopbacks placed between TX1A↔RX1A, TX1B↔RX1B, TX2A↔RX2A, and TX2B↔RX2B as seen in the first image below. SOM1 has loopbacks placed between TXA↔RXA and TXB→RXB as seen in the second image.

|image1| |image2|

.. warning::

   Careful while attaching and removing the loopback cables since they are fragil. Make sure they aren't broken before the test because this may lead to test fails.


Test process
------------

-  Before starting the testing, ensure you have added the MAC Address sticker on the board similarly to the photo below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/mac_address.png
   :alt: &400
   :align: center

-  Make sure the sequencer is programmed before starting the production testing.
-  Make sure all the required setup explained above is completed and the frequency counter is turned on in addition to the Raspberry Pi running the test script. Once the test setup is ready, SOM testing should be done using the following steps:

.. important::

   If it is the first time you run a test on your setup, there will be a prompt asking you to input the password for uploading test logs remotely. Type in the password provided and press enter. The password is then stored locally and there will be no need to this further.


-  Place a new SOM module onto the breakout board

-  Insert an SD card with the production test software into the SOM card slot

-  Power on the breakout board

-  Select from the menu on the screen the test option by pressing 1

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/test_1.png
   :align: center

-  Scan the serial number on the board using the scanner
-  When prompted on the Raspberry Pi monitor, enter in the remaining suffix characters to set the MAC address for the board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/2_test.png
   :align: center

-  Once the test has been completed, the 'PASSED' message will be prompted on the screen.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/test_7.png
   :align: center

-  When the test process is over, power-off the breakout board by selecting option 3, before powering it off manually. Then, insert the next module for testing.

FMC Carrier
~~~~~~~~~~~

.. _overview-1:

Overview
--------

The carrier tests run on boot up on Raspberry Pi via a script in a terminal window. See the following list for summaries of the current tests:

-  USB device mode: Micro USB cable is connected between raspberry pi and carrier, the test checks that the carrier is listed as usb gadget device
-  USB host mode: a Micro USB (male) an adapter to type A (female) is used to connect a usb flash, lsusb linux command is run on carrier to see if host mode is enabled and flash is detected, check speed with hdparm, check that partition is mounted
-  Ethernet: A cable is connected between the board's Ethernet ports and a ping between them is forced over the wire. The test passes if a response is received, otherwise it fails
-  Audio: Audio loopback cables plugged into horizontal sets of output/input jacks. Using Advanced Linux Sound Architecture (ALSA) commands like speaker-test and arecord, a sine signal is sent, recorded back. Then the recorded file is analyzed to determine the frequency of the recorded tone matches the input frequency
-  HDMI: Monitor connectivity is checked through physical displaying output on the attached monitor
-  Clocks: he clock monitor IP (axi_clock_monitor) is used to test several clock signal paths. The IP features a mechanism which measures the input clock frequency relative to the system clock and stores the result in an internal register. By checking if the measured clock signal is within an expected range the path is validated. 4 clock signals are measured, 3 of them generated by the FMC loopback at the same frequency of 156MHz and one is generated by the AD9517 PLL
-  SFP+, FMC loopback test. This is an instance of the axi_adxcvr_lb which is used to test 2 transceiver lanes. One transceiver lane (lane 0) is used for the FMC connector P2 and the other one (lane 1) for the SFP peripheral on the P1 connector. The test is performed continuously inside the IP core and the result is written to an internal status register. Each lane will have a corresponding status bit. Data is generated and verified by the core for each lane individually. The software must read the register to get the result.
-  FMC, Camera, Pmod gpio test.There are 3 instances of the axi_gpio IP core used to test general purpose signal paths for the FMC connector (P2), the camera connector (P9) and the (P11) PMOD connector. The FMC connector has the most signals (68) out of the three peripherals requiring three GPIO channels (GPIO_LB_0 ch1, ch2 and GPIO_LB_1 ch1), the CAM connector uses 2 channels and the PMOD uses 1. The test is performed by walking 0 across the signals of each channel, reading back the signals and checking for expected behaviour.

.. _test-image-1:

Test image
----------

Carrier SD Card
^^^^^^^^^^^^^^^

The production test software running on the target device is available as a prebuilt image that can be written to an SD card in the same fashion as the ADI Zynq images. Instructions are available for writing images from :doc:`Windows </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>` or :doc:`Linux </wiki-migration/resources/tools-software/linux-software/zynq_images/linux_hosts>`.

.. admonition:: Download
   :class: download

   
   -  \**20 Dec 2021 release \*\*
   -   `Actual file <https://swdownloads.analog.com/cse/prod_test_rel/adrv1crr_test/adrv1_carrier_14_02_2023.zip>`__
   -  Checksum ``d2c1ad4dfd4d91c5601be28a7d227c9c``
   


Raspberry microSD Card
^^^^^^^^^^^^^^^^^^^^^^

The SD image used is based on Raspbian with desktop. On top of that are installed the testing scripts. The image can be created starting from vanilla Raspbian.

.. admonition:: Download
   :class: download

   
   -  \**20 Dec 2021 release \*\*
   -   `Actual file <https://swdownloads.analog.com/cse/prod_test_rel/adrv1crr_test/adrv1crr_rpi_production_image.zip>`__
   -  Checksum ``d15c432f121141fc9cede87c0576e312``
   


.. note::

   To write it on SD card can follow the instructions: `Installing PI images <https://www.raspberrypi.org/documentation/installation/installing-images/>`__


.. _required-hardware-1:

Required hardware
-----------------

-  1 Raspberry Pi
-  2 Ethernet cables
-  1 SFP+ loopback module
-  2 1/8" audio loopback cables
-  1 FMC loopback card (`Whizz FMC loopback card <https://www.whizzsystems.com/loopback-card/>`__)
-  1 Camera loopback module
-  1 PMOD loopback module
-  1 USB media drive
-  1 type A to micro OTG adapter
-  1 USB hub
-  1 type A to micro USB cable to attach from Pi to the board's UART port
-  1 type A to micro USB cable to attach from Pi to the board's OTG port
-  1 adrv9361_rfsom module
-  1 adrv9361_rfsom FMC carrier board (ADRV1CRR)
-  1 microSD card and SD adapter with the latest test image (:doc:`or manually create one </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`)
-  1 External monitor with HDMI input
-  1 Scanner
-  Keyboard and mouse to be connected to the RaspberryPi board

.. _required-setup-1:

Required setup
--------------

-  SOM board plugged into a carrier board with the card and boot select switches set to boot from the carrier SD card slot (as seen in the image below).


|pzsdr-ccfmc-bootselect.jpg|

-  SD card with tests inserted into carrier slot.
-  RaspberryPi microSD card inserted.
-  1 Ethernet cable between the carrier port Ethernet1 and Pi, and one connected to the second Ethernet port on the carrier.
-  Audio loopback cables plugged into horizontal sets of output/input jacks.
-  SFP+, FMC, camera, and PMOD loopback modules plugged in.
-  Micro USB cable between Pi and carrier in USB OTG port or media drive inserted into the USB hub that plugs into the OTG adapter.
-  Mouse and keyboard also plugged into the RaspberryPi.
-  USB cable plugged into Pi and the micro USB UART port on the carrier board.
-  HDMI cable plugged from the carrier board into the external monitor.

.. important::

   Before starting the test process, please make sure to place the sticker with the QR code and the serial number **on top of the board**, as pictured below.


   |image3|

See the following image of a board set up to run the production tests.


|image4|

Make sure to connect to your WIFI Network before testing. You can exit the test window by pressing CTRL+C in order to access the connection. Reboot the system in order to return to the test window.


|image5|

.. _test-process-1:

Test process
------------

First make sure all the required setup explained above is ready. Once that is done, testing carrier boards should be done using the following steps:

-  Insert an SD card with the production test software into the carrier slot.
-  Insert card in Raspberry and power it on.
-  Power on the ADRV1CRR-FMC board.
-  The Pi should display the test interface once it booted, as presented in the image below

|image6|

-  Using option number 3 in the menu, the carrier test starts. In order to test the device, an ethernet cable must be connected between Pi and carrier. Connection is verified at the beginning of the test.
-  After connection is verified, the QR code with the board's serial number must be scanned in order to continue. The serial number may also be entered from the keyboard.
-  Tests should start automatically and begin with USB-gadget and UART testing. These tests run on the Raspberry.

|adr1crr_test_begin.png|

-  The following tests run directly on the carrier via SSH. When prompted, you should insert the password for the carrier, like in the image above. The default password is analog. If all the tests completed appropriately, a 'PASSED' message will be displayed on the screen.

|image7|

-  In case a test fails, a message is prompted asking whether the test should be repeated. A test can be re-run any number of times. If the test keeps failing, the user can opt to close the test, which leads to a 'FAILED' message in red being displayed on the screen. However, the test can be continued for the rest of the components. In this case, the number of failing tests will be displayed along with the 'FAILED' message at the end. |image8|

|image9|

-  At completion, the menu of the testing interface appears again. Option 5 can be used to power off the ADRV. After that, it is safe to physically toggle the power switch on the board.

The regular test process can be observed below.


|image10|

Breakout board
~~~~~~~~~~~~~~

Raspberry Pi test suite
-----------------------

.. _overview-2:

Overview
^^^^^^^^

The breakout board tests run via the U-Boot post testing framework while an attached Raspberry Pi automates the pass/fail mechanism via a looped expect script reading the breakout board's output over a serial connection. See the following list for summaries of the current tests:

-  USB media: Data is saved to an attached USB media drive, read back, and verified. If the data is different or there are other USB issues (device not attached, enumeration problems, etc) the test will fail.
-  Ethernet: The breakout board give itself a static IP address and tries to ping the computer's static address that it's directly connected to. The test passes if a response is received, otherwise it fails.
-  Buttons: The user running the test must interactively toggle the buttons which triggers a LED to blink. Note that when using adrv9364_rfsom boards only buttons S7, S8, and S9 are tested due to pin count limitations.

.. _required-hardware-2:

Required hardware
^^^^^^^^^^^^^^^^^

-  1 Ethernet cable
-  1 USB media drive
-  1 type A to micro OTG adapter
-  1 type A to micro USB cable to attach from the computer to the board's UART port
-  1 two pin jumper to set the USB mode
-  1 adrv9364_rfsom module
-  1 adrv9364_rfsom breakout board and power adapter
-  1 microSD card using the latest test image
-  1 Raspberry Pi 2/3 with attached screen using the related test image

.. _required-setup-2:

Required setup
^^^^^^^^^^^^^^

-  Raspberry Pi 2/3 with SD card for the test suite inserted.
-  ADRV9364 board plugged into a breakout board with SD card for test suite inserted.
-  Ethernet cable plugged in between the breakout board and the Raspberry Pi.
-  USB media drive inserted into the USB hub that plugs into the OTG adapter and then into the breakout board's USB OTG port.
-  Two pin jumper inserted to enable USB OTG mode.
-  USB cable plugged into Raspberry Pi and the micro USB UART port on the breakout board.

See the following images of a Raspberry Pi and breakout board set up to run the production tests. |brkout-setup.jpg|


|rpi-setup.jpg|

.. _test-process-2:

Test process
^^^^^^^^^^^^

First make sure all the required setup explained above is ready. Once that is done, testing breakout boards should be done using the following steps:

-  Insert the adrv9364_rfsom board with test suite SD card into the breakout board.
-  Make sure the power, USB, and Ethernet cables are plugged in and then power on the board. Confirm the green power LED and blue FPGA LED are both lit after a few seconds have passed (see the picture below). If two green LEDs are lit on the SOM without the blue FPGA LED being lit this means that the FPGA isn't getting configured properly which means there is an issue during early bring up such as the board's power sequence not running correctly.

|pzsdr-som-poweron-leds.jpg|

-  The board will start U-Boot which will run the tests after initialization.
-  Tests should start automatically and be shown on the serial terminal.
-  When prompted on screen as seen in the following image, toggle the buttons (S7 through S9) on the board. Note that the DS3 LED should light up when the buttons are in the on state. In order to pass the test the buttons must be toggled on and off within a minute of starting the test, otherwise the test will timeout and fail.

|rpi-button.jpg|

-  When the tests pass, a related message will be shown on screen in green. If any test fails, a message will shown in red instead. The following images show what the screen should look like in these cases. |rpi-pass.jpg|

|rpi-fail.jpg|

-  Once the tests are complete, keep the Raspberry Pi running and turn off the breakout board. Then unplug the power, USB, and Ethernet cables from the breakout board in addition to removing the adrv9364_rfsom. Plug all the cables back into the next breakout board and repeat the process from the beginning.

When done testing, hit button #23 on the Raspberry Pi to power down the system and give the system a few seconds before pulling the power cable. The screen should display a bunch of service stopping messages before finally stating "Starting Power-off" (as seen below) at which point it's safe to pull the power cable.


|rpi-poweroff.jpg|

Linux test suite
----------------

.. _overview-3:

Overview
^^^^^^^^

The breakout board tests run on boot up into Linux via a script. See the following list for summaries of the current tests:

-  USB media: Data is saved to an attached USB media drive, read back, and verified. If the data is different or there are other USB issues (device not attached, enumeration problems, etc) the test will fail.
-  Ethernet: A loopback module is used to perform a simple loopback test.
-  Switches/buttons: The user running the test must interactively toggle the switches and buttons which trigger the related LEDs.

.. _test-image-2:

Test image
^^^^^^^^^^

The production test software running on the target device is the :doc:`standard ADI Zynq image </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` modified slightly to run the :git-board-tests:`test suite <picozed-brk>`.

.. _required-hardware-3:

Required hardware
^^^^^^^^^^^^^^^^^

-  1 Ethernet loopback module
-  1 USB media drive
-  1 type A to micro OTG adapter
-  1 type A to micro USB cable to attach from the computer to the board's UART port
-  1 two pin jumper to set the USB mode
-  1 adrv9361_rfsom module
-  1 adrv936x_rfsom breakout board and power adapter
-  1 microSD card using the latest :doc:`ADI Zynq image </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` configured to run the :git-board-tests:`test suite <picozed-brk>`
-  1 External computer set up to monitor the serial connection

.. _required-setup-3:

Required setup
^^^^^^^^^^^^^^

-  SOM board plugged into a breakout board with SD card for test suite inserted.
-  Ethernet loopback module plugged in.
-  USB media drive inserted into the USB hub that plugs into the OTG adapter and then into the carrier's USB OTG port.
-  Two pin jumper inserted to enable USB OTG mode.
-  `Cypress USB driver <http://www.cypress.com/documentation/other-resources/usb-serial-drivers>`__ installed for connecting to the UART on Windows (or the cp210x module loaded on Linux)
-  USB cable plugged into computer and the micro USB UART port on the breakout board and the computer running your favorite terminal emulator (e.g. TeraTerm, PuTTY, minicom, picocom, etc) connected to the related serial port.

See the following image of a board set up to run the production tests.


|pzsdr-ccbrk-setup.jpg|

.. _test-process-3:

Test process
^^^^^^^^^^^^

First make sure all the required setup explained above is ready. Once that is done, testing breakout boards should be done using the following steps:

-  Insert the arv9361_rf SOM board with test suite SD card into the breakout board.
-  Make sure all the switches (S1 through S4) are set to the off position (they should all be toggled towards the label side as seen in the image above).
-  Make sure the power cable is plugged in and then power on the board. Confirm the green power LED and blue FPGA LED are both lit after a few seconds have passed (see the picture below). If two green LEDs are lit on the SOM without the blue FPGA LED being lit this means that the FPGA isn't getting configured properly which means there is an issue during early bring up such as the board's power sequence not running correctly.

|pzsdr-som-poweron-leds.jpg|

-  The board will boot into Linux to run the tests.
-  Tests should start automatically and be shown on the serial terminal.
-  When prompted, toggle the switches (S1 through S4) and buttons (S6 through S9) on the board. Note that the related LEDs should light up when the switches or buttons are in the on state (e.g. LED DS3 should light up when switch S1 or button S6 are enabled). In order to pass the test all switches and buttons must be toggled on and off. If this is not done within a minute of starting the test, it will timeout and fail.
-  The others tests will run without requiring user input once the switch and button tests are finished.
-  When the tests pass, the DS3 through DS6 LEDs will be solid. See the picture below for an example of LEDs lit after a successful test run. |pzsdr-ccbrk-passed.jpg| If any test fails LEDs DS3 through DS6 will be blinking and the script output will note the failure.
-  Finally hit the Enter key to power down the system. The message "System halted" should be shown on the serial output when it's safe to physically toggle the power switch on the board.

Breakout board Raspberry Pi test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _overview-4:

Overview
--------

The breakout board tests run via the U-Boot post testing framework while an attached Raspberry Pi automates the pass/fail mechanism via a looped expect script reading the breakout board's output over a serial connection. See the following list for summaries of the current tests:

-   **Buttons**: The user running the test must interactively toggle the buttons which trigger a LED to blink. Note that when using SOM1 boards only buttons S7, S8, and S9 are tested due to pin count limitations.
-   **USB media**: Data is saved to an attached USB media drive, read back and verified. If the data is different or there are other USB issues (device not attached, enumeration problems, etc) the test will fail.
-   **Ethernet**: A loopback module is used to perform a simple loopback test. The test passes if a response is received, otherwise, it fails.

Test images
-----------

The production test software running on the target device is available as a prebuilt image that can be written to an SD card in the same fashion as the ADI Zynq images. Instructions are available for writing images from :doc:`Windows </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>` or :doc:`Linux </wiki-migration/resources/tools-software/linux-software/zynq_images/linux_hosts>`.

.. admonition:: Download
   :class: download

   
   -  \**5 January 2016 release \*\*
   
   ::
   
      * 
      * Checksum ''''
      * Checksum ''''
   


.. admonition:: Download
   :class: download

   
   -  \**Raspberry Pi image \*\*
   
   ::
   
      * 
      * Checksum ''''
      * Checksum ''''
   


.. important::

   It is also possible to manually create one using :doc:`these instructions </wiki-migration/resources/eval/user-guides/pzsdr/testing/sd-cards>`.


.. _required-hardware-4:

Required hardware
-----------------

-   1 Ethernet loopback module
-   1 USB media drive
-   1 type A to micro USB OTG adapter
-   1 type A to micro USB cable to attach from the Raspberry Pi computer to the board's UART port
-   1 two pin jumper to set the USB mode
-   1 adrv9361_rfsom module
-   1 adrv936x_rfsom breakout board and power adapter
-   1 microSD card using the latest ADI Zynq image configured to run the test suite

.. _required-setup-4:

Required setup
--------------

.. tip::

   This setup needs to be done only once.


| **1. SDR2 SOM** board **with SD card inserted** configurated to run the test suite and **S1** dip switch on the **"SDSOM"** position. |image11|
| **2. USB** media drive into the **OTG** adapter. |image12|
| **3. Raspberry Pi powered on** configurated to run the breakout board test with a **USB cable attached**. After about a couple seconds the following message will be printed on the screen “POWER ON BRK”. At this point, the Raspberry Pi is ready to test the breakout board. |image13|

.. _test-process-4:

Test process
------------

| **1.** Insert the SDR2 SOM board with test suite SD card into the breakout board.
| **2.** Make sure all the switches (S1 through S4) are set to the off position.
| **3.** Plug the micro USB on the UART port (P14) on the breakout board.
| **4.** Plug the OTG adapter into the breakout board USB OTG port (P11).
| **5.** Plug the Ethernet loopback module into breakout board Ethernet connector (M1).
| **6.** Insert a jumper on the P9 header, between pin 1 & 2, to enable USB OTG mode.
| |image14|
| **7.** Make sure the power cable is plugged in and then power on the board. Confirm the green power LED and blue FPGA LED are both lit after a few seconds have passed (see the picture below). If two green LEDs are lit on the SOM without the blue FPGA LED being lit this means that the FPGA isn't getting configured properly which means there is an issue during early bring up such as the board's power sequence not running correctly.
| **8.** The board will boot into Linux to run the tests.
| **9.** Tests should start automatically and be shown on the Raspberry Pi display.
| |image15|
| **10.** When prompted, toggle the switches (S1 through S4) and buttons (S6 through S9) on the board. Note that the related LEDs should light up when the switches or buttons are in the on the state (e.g. LED DS3 should light up when switch S1 or button S6 are enabled). In order to pass the test, all switches and buttons must be toggled on and off. If this is not done within a minute of starting the test, it will timeout and fail.
| |image16|
| **11.** Wait for the test result. The other tests will run without requiring user input once the switch and button tests are finished. When the tests pass, the DS3 through DS6 LEDs will be solid.

========= =========
|image17| |image18|
========= =========

| If any test fails LEDs DS3 through DS6 will be blinking and the script output will note the failure.
| \| |image19| \| |image20| \| |image21| \|
| **12.** Finally wait for "TURN OFF BOARD! CONNECT NEXT BOARD TO BE TESTED!" to power down the system.
| \| |image22| \| |image23| \|
| **13.** Once the test is complete turn off the breakout board, unplug the power, USB cables and Ethernet loopback module from the breakout board in addition to removing the SDR2 SOM. Plug all the cables back into the next breakout board and repeat the process from the beginning. If you want to start the test again, for the same breakout board, power off and then power on the breakout board or reset the SDR2 SOM board to repeat the test automaticaly.
| **When done testing**, hit **button #27 on the Raspberry Pi display** to **power down** the system and give the system a few seconds before pulling the power cable.
| |image24|
| If necessary, hit **button #23 on the Raspberry Pi display to restart** or hit **button #22 to display the Raspberry Pi IP addresses**.
| \| |image25| \| |image26| \| \|

Demo Test process
-----------------

| |image27|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/pzsdr-rf-loopback.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/pzsdr1-rf-loopback.jpg
   :width: 400px
.. |pzsdr-ccfmc-bootselect.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/pzsdr-ccfmc-bootselect.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/img_1735_qr.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/img_1736.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/wifi_connection.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/initial_screen.png
.. |adr1crr_test_begin.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/adr1crr_test_begin.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/test_pass_adrv1crr.png
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/camera_test_fail_adrv1crr.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/adrv1crr_test_failed.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/211213_gif_adrvtest_passed_1_5sec.gif
.. |brkout-setup.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/brkout-setup.jpg
.. |rpi-setup.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/rpi-setup.jpg
.. |pzsdr-som-poweron-leds.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/pzsdr-som-poweron-leds.jpg
.. |rpi-button.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/rpi-button.jpg
.. |rpi-pass.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/rpi-pass.jpg
.. |rpi-fail.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/rpi-fail.jpg
.. |rpi-poweroff.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/rpi-poweroff.jpg
.. |pzsdr-ccbrk-setup.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/pzsdr-ccbrk-setup.jpg
.. |pzsdr-ccbrk-passed.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/pzsdr-ccbrk-passed.jpg
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/sdr2_som.jpg
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/usb_drive_otg.jpg
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/raspberry_pi_setup.jpg
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/breakout_board_setup.jpg
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/pzsdr-som-poweron-leds.jpg
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/start_toggle.png
   :width: 250px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/test_pass.png
   :width: 250px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/pzsdr-ccbrk-passed.jpg
   :width: 370px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/test_fail_toggle.png
   :width: 250px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/test_fail_usb.png
   :width: 250px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/test_fail_ethernet.png
   :width: 250px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/test_pass_end.png
   :width: 250px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/test_fail_end.png
   :width: 250px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/power_off_pi.png
   :width: 250px
.. |image25| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/reboot_pi.png
   :width: 250px
.. |image26| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/get_all_ip.png
   :width: 250px
.. |image27| image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/breakout_board_test.gif
