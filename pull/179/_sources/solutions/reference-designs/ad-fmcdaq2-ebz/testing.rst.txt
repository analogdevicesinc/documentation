.. _ad-fmcdaq2-ebz testing:

Production Testing of the AD-FMCDAQ2 / AD-FMCDAQ3
==================================================

Overview
--------

The production testing is quite simple. Since each board has been completely
characterized, and we know the layout is good, we can just look for gross
errors.

The test is broken down into the following sections:

Temperature
~~~~~~~~~~~

The ``ad7291.in_temp0_raw`` is the raw results from the AD7291 - which is
0.25 deg C. 80 refers to 80 steps of 0.25 deg C or 20 deg C, and 160 refers to 40 deg C. This
allows the tests to be done in a normal lab setting.

Voltage
~~~~~~~

This section requires checking the schematics.
Specifically, sheet 7 shows how the AD7291 is connected. 1% resistors connect
various voltages, and things are divided down to ensure that the voltage levels
don't exceed full scale.

The explanation of how the valid ranges are calculated is similar to the same
tests for the FMComms boards.

Signals
~~~~~~~

First the noise floor is checked when no input is supplied to make sure it is
within a certain threshold. Then tones of approximately 97 MHz, 185 MHz, and 233
MHz are input against each channel individually and the fundamental frequency as
well as the 2nd through 7th harmonics are checked to make sure they are within
set bounds.

Required Software
-----------------

**Creating a ZY706 carrier SD test card** - First, write the latest available SD
card image found to a spare card and prepare the card to boot into Linux.

- **15 December 2022 release**
- `Actual file for
  FMCDAQ3 <https://swdownloads.analog.com/cse/prod_test_rel/fmcdaq3_test/fmcdaq3_carrier.zip>`__
- Checksum ``57ade50f1add6596c1501e0388f7fcfa``

**Creating a Raspberry Pi SD test card** - The SD image used is based on
Raspbian with Desktop.

- **15 December 2022 release**
- `Actual file for
  FMCDAQ3 <https://swdownloads.analog.com/cse/prod_test_rel/fmcdaq3_test/rpi_daq3_prod.zip>`__
- Checksum ``7b49ab20b2f9d28afdb8703e6f19b498``

Required hardware
-----------------

- Zynq ZC706
- Raspberry Pi4
- FMCDAQ2/3
- RF loopback cables (2x)
- External monitor connected to the Raspberry Pi via micro HDMI
- Keyboard and mouse (with USB hub if they aren't part of a combo device)
- Ethernet cable (needs to be plugged between Raspberry Pi and carrier)
- QR code scanner
- DAQ2/DAQ3 test SD Card
- Raspberry Pi SD Card

Required setup
--------------

.. figure:: daq3-setup.png
   :alt: Test Setup
   :width: 600

   Test setup overview

1. Attach the RF loopback cables to the board. The images at the bottom of the
   page show the correct placement for each type of AD-FMCDAQ board.
2. Insert the SD card into the carrier board.
3. Insert the AD-FMCDAQ2/3 board onto the carrier
4. Connect the HDMI cable to Raspberry Pi
5. Connect USB keyboard to Raspberry Pi
6. Insert SD card into Raspberry Pi
7. Connect Ethernet cable between Raspberry Pi and the carrier
8. Connect the scanner to Raspberry Pi
9. Power the carrier board and Raspberry Pi

Make sure to connect to your WIFI Network before testing. You can exit the test
window by pressing CTRL+C in order to access the connection. Reboot the system
in order to return to the test window.

Test process
------------

Firstly, make sure all the required steps from the setup explained above are
completed. Once the setup is ready, testing should be done using the following
steps:

- Power the carrier board and the Raspberry Pi. The following screen will
  appear once the system has booted.

  .. image:: fmcdaq3-startup-screen.png

- The testing sequence can be started by selecting one of the menu items. **In
  order to start testing, an Ethernet cable should be connected between
  Raspberry Pi and DUT**.

  - **Test 1** for FMCDAQ3
  - **Test 2** for FMCDAQ2

- At the beginning of every test, the connection with DUT is checked. If the
  connection is correctly established, the following message will be printed.

  .. image:: fmcdaq3-eth-err.png

- Use the scanner to scan the QR code on the board.

- If one of the tests failed, the FAILED message will be printed as in the
  screen capture below:

  .. image:: fmcdaq3-failed.png

- In case of a failed test, the tester can repeat the test immediately. The test
  can be repeated an undefined number of times.

- After completing the test, power off the carrier by typing 4. After several
  seconds, power off the carrier board using the physical switch.

- Remove the DAQ2/3 card and place the heatsink according to the pictures below.

- In order to power off the Raspberry Pi, please type 3 and enter.

When testing is finished, ZC706 and the Raspberry Pi should always be powered
off from terminal before power is unplugged, otherwise the SD cards can be
corrupted. First select item 4 to power off the carrier. After a few seconds,
turn off the switch. After the ZC706 is off, the Raspberry Pi can be turned off
selecting item 3.

Cable placement
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 0

   * - .. image:: daq2_connection.png
          :width: 400
     - .. image:: daq3_connection.png
          :width: 400
   * - FMCDAQ2
     - FMCDAQ3

Heatsink placement
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 0

   * - .. image:: daq2_heatsink.png
          :width: 250
     - .. image:: daq3_heatsink_top.png
          :width: 250
     - .. image:: daq3_heatsink_bottom.png
          :width: 250
   * - FMCDAQ2
     - FMCDAQ3 top
     - FMCDAQ3 bottom
