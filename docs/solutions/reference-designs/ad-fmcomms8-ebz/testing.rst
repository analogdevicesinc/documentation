.. _ad-fmcomms8-ebz-testing:

Production Testing
===================

Overview
--------

Production tests for the AD-FMCOMMS8-EBZ are composed of a series of Bash
scripts that run both on the Raspberry Pi (host) and the DUT (Device Under
Test). The test procedure requires a Raspberry Pi 4 board connected via
Ethernet cable to the DUT. The Raspberry Pi requires an HDMI monitor and USB
keyboard connected. All test sequences are selected and started from the GUI
interface displayed by the Raspberry Pi on the monitor.

.. figure:: testing/fmcomms8-prod-test-complete-setup-fan.png
   :align: center

   Complete test setup

Required Hardware
-----------------

- **Raspberry Pi 4** (version 4 or newer required; USB 3.0 connection is used
  during testing)
- **HDMI monitor** connected to the Raspberry Pi
- **USB keyboard** connected to a Raspberry Pi USB 2.0 port (black)
- **Raspberry Pi microSD card** (minimum 8 GB, Class 10)
- **DUT SD card** (minimum 8 GB, Class 10) inserted in ADRV2CRR-FMC P15 slot
- **CAT5 Ethernet cable** — connect between the Raspberry Pi and the DUT
  (use the M2 port / Ethernet RGMII on the DUT side)
- **USB-C power supply** for the Raspberry Pi
- **ADRV2CRR-FMC** carrier board
- **ADRV9009-ZU11EG** RF-SOM
- **AD-FMCOMMS8-EBZ** evaluation board
- **4x U.FL loopback cables** (U.FL-2LPHF6-068N1T-A-100) for RF testing
- **12 V power supply** connected to P11 on the ADRV2CRR-FMC

.. figure:: testing/fmcomms8-ufl-complete.png
   :align: center

   U.FL loopback cable connections

Setup
-----

#. Connect HDMI cable to the Raspberry Pi.
#. Connect USB keyboard to the Raspberry Pi.
#. Insert the Raspberry Pi microSD card.
#. Connect the USB-C power supply to the Raspberry Pi.
#. Connect all loopback cables to the DUT (see figure above).
#. Connect the Ethernet cable between the Raspberry Pi and the DUT.
#. Insert the SD card into the DUT.
#. Power on the DUT.

Test Process
------------

#. Power on both the DUT and the Raspberry Pi.

   .. figure:: testing/boot-pi-screen.png
      :align: center

      Raspberry Pi test menu

#. Before starting the test, place the label containing the serial number on
   the RF shielding top cover. After this step, do **not** swap the RF
   shielding top cover between boards.

#. When testing the AD-FMCOMMS8-EBZ, select **Test 7** from the menu.

#. The testing sequence checks the Ethernet connection with the DUT first. If
   the connection cannot be established, an error message is displayed:

   .. figure:: testing/boot-pi-eth-conn.png
      :align: center

      Ethernet connection error

   Ensure the Ethernet cable is connected, the DUT is powered up, the DUT SD
   card is inserted, and boot mode switches (S13-S16) are configured for SD
   boot.

#. If the test completes successfully, the **PASSED** message is displayed:

   .. figure:: testing/test_passed_screen.jpg
      :align: center

      All tests passed

#. If a test fails, the **FAIL** message is displayed. The failing test can be
   repeated immediately:

   .. figure:: testing/test_failed_screen.jpg
      :align: center

      Test failed

.. warning::

   When testing is finished, always power off the DUT and Raspberry Pi from
   the terminal before disconnecting power, otherwise the SD cards can be
   corrupted.

   #. Select item **9** to power off the DUT. Wait until LEDs DS6 and DS7 are
      off, then disconnect power from the DUT.
   #. Select item **8** to power off the Raspberry Pi.
