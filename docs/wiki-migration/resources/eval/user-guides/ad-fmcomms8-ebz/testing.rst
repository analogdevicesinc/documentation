AD-FMCOMMS8-EBZ Production Testing
==================================

Overview
--------

Production tests for AD-FMCOMMS8 are composed of a series of Bash scripts that run both on Raspberry Pi and DUT (Device Under Test). The test procedure requires a Raspberry Pi 4 board (host) connected via Ethernet cable to the DUT. The Raspberry Pi board requires to have a HDMI monitor and USB keyboard connected. All test sequences are selected and started from the GUI interface displayed by Raspberry Pi on the monitor. Please find the required equipment list below:

Required Hardware
-----------------

-  Raspberry Pi4: Is strictly required to be version 4 or newer. USB 3.0 connection is required during testing.
-  HDMI monitor: monitor should be connected to Raspberry Pi to display the testing sequence and the testing results
-  USB keyboard: keyboard should be connected to Raspberry Pi USB 2.0 port (black). It is required to interact with the testing SW.
-  Raspberry Pi microSD card: A minimum 8GB Class 10 microSD card prepared for testing sequence as presented bellow should be inserted in Raspberry Pi.
-  DUT SD card: A minimum 8GB Class 10 SD card prepared for testing sequence as presented bellow should be inserted in ADRV2CRR-FMC P15 slot.
-  CAT5 ethernet cable: Using ethernet cable communication between Raspberry Pi and DUT is performed. On DUT side the ethernet cable should be connected on M2 port (Ethernet RGMII)
-  USB-C power supply is required for powering up the Raspberry Pi
-  ADRV2CRR-FMC
-  ADRV9009-ZU11EG RF-SOM
-  AD-FMCOMMS8-EBZ: can be tested selecting item 7 from test menu. It can be tested with ADRV2CRR-FMC.
-  4 U.FL loopback cables: required for RF testing of AD-FMCOMMS8-EBZ RF (U.FL-2LPHF6-068N1T-A-100)
-  12V power supply: connected to P11 on ADRV2CRR-FMC.

The complete test jig should look like:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms8-ebz/fmcomms8-prod-test-complete-setup-fan.png
   :align: center
   :width: 900px

Required Software
~~~~~~~~~~~~~~~~~

AD-FMCOMMS8-EBZ SD card
^^^^^^^^^^^^^^^^^^^^^^^

The SD card image used for production testing is based on official release of Zynq images and can be downloaded from :

.. admonition:: Download
   :class: download

   
   -  \**28 May 2020 release \*\*
   -   `Actual file <https://swdownloads.analog.com/cse/prod_test_rel/talise_test/adrv9009_fmcomms8_test_card_28_05.img.tar.xz>`_
   -  Checksum ``9d3455a071f4151b9c320282abcb2f04``
   


.. admonition:: Download
   :class: download

   
   -  \**27 May 2020 release \*\*
   -   `Actual file <https://swdownloads.analog.com/cse/prod_test_rel/talise_test/adrv9009_som_test_card_27_05.img.tar.xz>`_
   -  Checksum ``4efbaa39928f2f36b7b462156e6d00f6``
   


.. note::

   To write it on SD card can follow the instructions for: :doc:`linux hosts </wiki-migration/resources/tools-software/linux-software/zynq_images/linux_hosts>` or :doc:`windows hosts </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>`


Raspberry PI SD card
^^^^^^^^^^^^^^^^^^^^

The SD image used is based on Raspbian with desktop. On top of that are installed the testing scripts. The image can be created starting from vanilla Raspbian or downloaded from:

.. admonition:: Download
   :class: download

   
   -  \**02 Nov 2021 release \*\*
   -  `Actual file <https://swdownloads.analog.com/cse/prod_test_rel/talise_test/adrv9009_pi_test_card_02_11.tar.xz>`_
   -  Checksum ``080fb8771e12195eba7196f9de05ec1c``
   


.. admonition:: Download
   :class: download

   
   -  **27 May 2020 release - outdated, do not use!**
   -  `Actual file <https://swdownloads.analog.com/cse/prod_test_rel/talise_test/adrv9009_pi_test_card_27_05.img.tar.xz>`_
   -  Checksum ``cf5b55f2a874ef43e47f269b4c534c9d``
   


.. note::

   To write it on SD card can follow the instructions: `Installing PI images <https://www.raspberrypi.org/documentation/installation/installing-images/>`_


Required setup steps
~~~~~~~~~~~~~~~~~~~~

-  Connect HDMI cable to Raspberry Pi
-  Connect USB keyboard to Raspberry Pi
-  Insert Raspberry Pi microSD card
-  Connect power supply to Raspberry Pi
-  Connect all loopbacks to DUT

   -


   |image1|

-  Connect Ethernet cable between Raspberry Pi and DUT
-  Insert SD card in DUT
-  Power on DUT

Test process
~~~~~~~~~~~~

First make sure all the required setup explained above is completed. Once the test setup is ready, SOM testing should be done using the following steps:

-  Power on both DUT and Raspberry Pi
-  The following screen should be visible after Raspberry Pi booted:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009-zu11eg/boot-pi-screen.png
   :align: center
   :width: 800px

-  Before starting the test place the label containing the serial number on the RF shielding top cover.

|

.. warning::

   After this step, DO NOT SWAP the RF shielding top cover between boards.


.. important::

   When testing the AD-FMCOMMS8-EBZ run the following test:


   | \* **Test 7**
   |

-  Testing sequence can be started by selecting one of the menu items. In order to start testing an Ethernet cable should be connected between Raspberry Pi and DUT. At the beginning of every test the correct connection with DUT is checked. If the connection cannot be established the following error message will be printed:


|image2|

.. tip::

   Make sure that Ethernet cable is connected, DUT is powered up, DUT SD card is inserted and boot mode switches (S13-S16) are configured for SD boot.


-  If test completed successfully the PASSED message will be printed in green like in the screen bellow. This means that DUT passed all the assigned tests.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009-zu11eg/test_passed_screen.jpg
   :align: center
   :width: 600px

-  If one of the tests failed, the FAIL message will be printed like in the screen capture bellow:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009-zu11eg/test_failed_screen.jpg
   :align: center
   :width: 600px

-  In case of a failed test the program will ask if the tester wants to repeat that test immediately. The test can be repeated by an undefined number of times.
-  If the problem is persistent and the test failing continuously the test engineer can decide to not repeat it anymore.

.. important::

   When testing is finished ADRV and Raspberry PI should always be powered off before power is unplugged otherwise the SD cards can be corrupted. First should be selected item 9 to power off ADRV. The test engineer should wait until LEDs DS6 and DS7 are off. Now the power can be disconnected from ADRV. After ADRV is off the Raspberry PI can be turned off by selecting item 8.


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms8-ebz/fmcomms8-ufl-complete.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009-zu11eg/boot-pi-eth-conn.png
   :width: 800px
