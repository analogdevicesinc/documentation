Production Testing
==================

Overview
--------

The purpose of the test procedure is to identify connectivity issues, poor
soldering, and potential manufacturing defects. Some of the issues are directly
identified by explicit part-targeted tests, others are implicit, by running
adjacent tests.

There is only one test fixture that will be used to test three different hardware
platforms:

#. Jupiter Main Board
#. Jupiter Add-on Board
#. Jupiter System

Once the initial setup for one of the hardware platforms is done, it is highly
recommended that all the hardware platforms of the same type be tested before
changing the setup to test another hardware platform. It is mandatory to run the
Main Board and Add-on Board tests before System testing because the Jupiter
System should include only boards that previously passed the manufacturing
testing.

Test Duration
-------------

Sequence 1 - Main Board
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Step Description
     - Estimated Time (minutes)
   * - Test bench setup
     - 3 min
   * - Software test
     - 10 min
   * - **Total time**
     - **13 min**

Sequence 2 - Add-on Board
^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Step Description
     - Estimated Time (minutes)
   * - Test bench setup
     - 3 min
   * - Software test
     - 4 min
   * - **Total time**
     - **7 min**

Sequence 3 - System Test
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Step Description
     - Estimated Time (minutes)
   * - Test bench setup
     - 2 min
   * - Software test
     - 4 min
   * - **Total time**
     - **6 min**

Test Requirements
-----------------

.. note::

   Please test all main boards first, then perform the add-on boards testing,
   and last, test the entire system in the enclosure.

Required Hardware
^^^^^^^^^^^^^^^^^

Initial Setup
"""""""""""""

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - 1x Raspberry Pi 4 + Power supply
     - .. figure:: images/rpi5.jpg

   * - 1x Micro HDMI cable for Raspberry Pi
     - .. figure:: images/micro_hdmi.jpg

   * - 1x Mouse and keyboard for Raspberry Pi
     - .. figure:: images/mouse_keyboard.png

   * - 1x Test SD card for Raspberry Pi
     - .. figure:: images/sd_card.jpg

   * - 1x Portable Display + Power Supply
     - .. figure:: images/portable_display.png

   * - 1x QR code reader
     - .. figure:: images/qr_reader.jpg

   * - RPI PWR shield connection
     - .. figure:: images/rpi_pwr_shield_conn.png

   * - External Reference Clock and MCS cables
     - .. figure:: images/external_ref_clock_mcs_cable.jpg

.. note::

   * 1x 4 Port Ethernet Switch + Ethernet cables (3 pieces: 1x 20cm, 1x 50cm, 1 for main switch)
   * Ethernet switch must be connected to the internet.
   * 1x USB Type A to USB Type C cable

DUT Setup
"""""""""

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - 1x HDMI to Display Port adapter
     - .. figure:: images/hdmi_display_port_adapter.png

   * - 1x Mini HDMI to HDMI cable
     - .. figure:: images/mini_hdmi_to_hdmi.png

   * - 10x SMA quick connect adapters
     - .. figure:: images/sma_quick_connect_adapters.png

   * - 4x 50 Ohm terminators
     - .. figure:: images/50_ohm_terminator.png

   * - 4x uFL cables
     - .. figure:: images/ufi_cable.jpg

   * - 1x uFL cable remover key
     - .. figure:: images/cable_remover_key.jpg

   * - 2x Spacers (12 mm)
     - .. figure:: images/spacer.jpg

Additional DUT items (no image):

* 1x Portable Display + Power Supply
* 1x SATA III SSD
* 1x SATA to eSATA cable
* 1x USB 3 stick + USB Type C adapter
* 1x Micro USB cable
* 1x Test SD card for the DUT
* 1x BR-048139 Jupiter SDR Main Board (DUT)
* 1x GPIO loopback cable
* 1x Add-on Interface test board
* 2x RF loopback cables
* 1x Reference Clock cable
* 1x MCS cable
* 1x Jupiter USB Type C supply + USB Type C cable

.. warning::

   * uFL cables must always be replaced after testing a batch of 30 Add-on boards
   * Known good Main Board must always be replaced after testing a batch of ~900
     tested Add-on boards
   * SMA quick connect adapters must be replaced after testing a batch of 500 DUTs
     or they could be replaced every time you start a new production LOT

.. note::

   DUT is any of the following:

   * Main Board
   * RF Add-on Board
   * Assembled System

.. note::

   The test setup needs to be connected to the internet during testing process
   to allow the test logs to be uploaded to the server.

   To complete the test setup, you need to have 5 Power Outlets available:

   * 2x Monitor supply
   * 1x RPI supply
   * 1x Ethernet Switch supply
   * 1x DUT USB power supply

Required Software
^^^^^^^^^^^^^^^^^

The test image is provided on a pre-configured SD card.

Required Setup
^^^^^^^^^^^^^^

Initial Setup
"""""""""""""

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - No.
     - Steps
   * - 1
     - Insert the SD card into the Raspberry Pi
   * - 2
     - Make the following connections to the RPI:

       * HDMI micro cable - RPI HDMI port and monitor
       * Mouse and keyboard dongle - to RPI's USB port
       * A to micro-USB cable - to RPI's USB port
       * USB C - power supply
       * USB Type A to USB Type C cable (it will be connected to the DUT during
         test procedure)
       * Ethernet cable PI ETH - 20cm length
   * - 3
     - Connect QR code reader to RPI's USB port (labeled QR READER)

       **OR**

       During System test, instead of QR code reader, connect the Dymo
       LabelWriter 450 Turbo printer
   * - 4
     - The RPI comes with the PWR shield connected
   * - 5
     - Connect External Reference clock SMA cable and MCS SMA cable (CLK OUT and
       MCS OUT)
   * - 6
     - Power up the Ethernet switch (label ETH PWR)
   * - 7
     - Power up RPI - power supply to power outlet

.. figure:: images/rpi_connection_1.jpg
   :width: 25em

   Raspberry Pi connections

Labeling
""""""""

The label stuck on the boards will be scanned during testing and the information
will be stored into the board's EEPROM. Also, the test logs will contain the
info on the labels so that we can track the logs.

The label stuck on the enclosure will allow us to identify the hardware our
customer is referring to and we can always check the testing logs to check how
the device was performing during testing.

Test Sequence 1 - Main Board Test
---------------------------------

Main Board Labeling
^^^^^^^^^^^^^^^^^^^

The label contains the board ID and its QR code:

* Manufacturing Date in the format yyyymmdd
* Board ID: a 5 digit decimal number

The label will be printed by the manufacturing company on their available
printer. The label needs to be stuck to the PCB before production testing since
it needs to be scanned during testing.

Label size: 13.81 x 6.35 mm

Example: ``2023110600018``

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - Main board label position
     - .. figure:: images/label_position.png

   * - Main board labeling example
     - .. figure:: images/main_board_labeling_example.png

Main Board Test Setup
^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - No.
     - Steps
   * - 1
     - Place BR-048139 Jupiter SDR Main Board (DUT) into the fixture
   * - 2
     - Insert the following cables into the DUT:

       * Insert SD card into DUT
       * Ethernet cable coming from the Ethernet Switch (DUT ETH - 50cm)
       * eSATA cable coming from SSD
       * HDMI to Display Port adapter + Mini HDMI to HDMI cable coming from DUT
         Display
       * Connect GPIO loopback cable into the GPIO connector
       * Connect micro USB cable from RPI
       * Add-on Interface test board
       * Connect RF loopback cables using SMA Quick connect adapters (push and
         click connection)
       * Power on the monitor from DUT
   * - 3
     - Connect External Reference clock cable and MCS cable (CLK OUT and MCS OUT)
       to SMA connectors of the DUT board
   * - 4
     - Before testing another board, or at the work day end, make sure to remove
       all the cables from the DUT
   * - 5
     - After disconnecting the DUT, place a new one and repeat testing steps 2
       and 3

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - Placing DUT into the fixture
     - .. figure:: images/fixture_placing.png

   * - DUT cable insertion
     - .. figure:: images/dut_cable_insertion.jpg

   * - External Reference clock SMA cable connection
     - .. figure:: images/external_ref_clock_sma_cable_conn.jpg

   * - DUT cable removal
     - .. figure:: images/dut_cable_removal.jpg

.. figure:: images/test_system_setup.png
   :width: 25em

   Test system setup overview

Test Sequence 2 - Add-on Board Test
-----------------------------------

Add-on Board Labeling
^^^^^^^^^^^^^^^^^^^^^

The label will be identical with the one from the main board. The label needs
to be stuck to the PCB before production testing since it needs to be scanned
during testing.

Info: Manufacturing Date and Board ID

Example: ``2023110600018``

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - Add-on board label position
     - .. figure:: images/label_position_test_seq_2.png

Add-on Board Test Setup
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - No.
     - Steps
   * - 1
     - Perform the steps from initial setup / make sure the initial setup is
       prepared
   * - 2
     - Insert the SD card into the main board (known good)
   * - 3
     - Known good main board and Add-on board (DUT) connections:

       Fix down the main board using 12 mm spacers
   * - 4
     - Stick the QR code label to the add-on board
   * - 5
     - Connect uFL cables to the main board (known as good)
   * - 6
     - Connect add-on board using uFL cables and add-on interface connector
   * - 7
     - Connect the Ethernet cable coming from the Ethernet Switch (DUT ETH - 50cm)
   * - 8
     - Connect the USB Type C power supply to USB_POWER port
   * - 9
     - Press the Power button to power on the board. The LED should turn blue
   * - 10
     - Wait for the test to finish. Make sure the power LED is RED, then:

       * Unplug the loopback cables (make sure you hold the add-on board)
       * Using uFL Cable Remover Key, disconnect the uFL cables from the DUT
       * Leave uFLs on the main board connected
   * - 11
     - Connect the next add-on board
   * - 12
     - Repeat testing steps 4 to 10

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - Main board and add-on board connection
     - .. figure:: images/manandaddonboardconnection.png

   * - DUT connections for add-on board test
     - .. figure:: images/dut_conn_test_seq_2.png

   * - uFL cable connection to main board
     - .. figure:: images/ufl_cable_main_board_conn_test_seq_2.jpg

   * - Add-on board connection
     - .. figure:: images/add_on_board_conn_test_seq_2.jpg

   * - RF loopback cable connection
     - .. figure:: images/rf_loopback_cable_conn_test_seq_2.jpg

   * - RF loopback cable (labeled B)
     - .. figure:: images/rf_loopback_label_b.jpg

   * - Power button press
     - .. figure:: images/power_button_test_seq_2.png

   * - Unplug loopback cables
     - .. figure:: images/unplug_loopback_cable_test_seq_2.jpg

   * - Remove uFL cables using key
     - .. figure:: images/remove_ufl_cables_w_key_test_seq_2.jpg

Test Sequence 3 - System Test
-----------------------------

.. attention::

   When the system is assembled, make sure the Main Board and Add-on Board
   placed in the same enclosure have the same IDs.

System Labeling
^^^^^^^^^^^^^^^

The label will be printed by the testing application only if it PASSes the test.

Label size: 46 x 78 mm (Dymo 99016-2)

Printer: Dymo LabelWriter 450 Turbo

The System label has the following format shown below. Stick the label on the
bottom of the enclosure.

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - Dymo LabelWriter 450 Turbo
     - .. figure:: images/label_writer.jpg

   * - System label example
     - .. figure:: images/main_board_labeling_example_test_seq_3.png

System Test Setup
^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - No.
     - Steps
   * - 1
     - Perform the steps from initial setup / make sure the initial setup is
       prepared
   * - 2
     - Place the support board along with protective foam on DUT place
   * - 3
     - Insert the SD card into the SD Card Slot of the enclosure
   * - 4
     - Connect RF loopback cables using SMA Quick connect adapters on the add-on
       board ports (labeled B)
   * - 5
     - Connect the RF terminators on the MAIN BOARD ports using quick connect
       (labeled A)
   * - 6
     - Connect the Ethernet cable coming from the Ethernet Switch (DUT ETH - 50cm)
   * - 7
     - Press the Power button to power on the board. The LED should turn blue,
       press Enter
   * - 8
     - Wait for the test to finish
   * - 9
     - Unplug the loopback cables and terminators. Unplug ETH cable
   * - 10
     - Connect another DUT and perform testing steps 3-8

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - Support board with protective foam
     - .. figure:: images/protective_foam_test_seq_3.jpg

   * - SD card slot on enclosure
     - .. figure:: images/sd_card_slot.png

   * - Power button press for system test
     - .. figure:: images/power_button_test_seq_3.png

Test Process
------------

Running the Test Software
^^^^^^^^^^^^^^^^^^^^^^^^^

After the Raspberry Pi boots up, the test screen will appear on the monitor as
shown below.

.. figure:: images/test_screen.png
   :width: 45em

   Test screen

The following test menu should appear:

.. code-block:: text

   Please enter your choice:
   1) TEST MAIN BOARD
   2) Add-ON test
   3) System Test
   4) Power-Off Pi
   5) Repair SD card

1) Test Main Board
""""""""""""""""""

Type "1" into the terminal then press ENTER to start **1) TEST MAIN BOARD**.

.. figure:: images/test_main_board.png
   :width: 45em

   Test Main Board option

**Test USB_DATA boot:**

During this test, perform the following:

#. Press shortly on the power button and wait for the LED to turn RED
#. Unplug the ETH cable (DUT ETH)
#. Plug the USB-C power cable in USB_DATA port of the DUT

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - Power cable connection to DUT
     - .. figure:: images/test_command_1_power_cable_conn_to_dut.png

   * - USB-C connection to USB_DATA port
     - .. figure:: images/test_command_1_usb_power_boot_usb_c_conn.jpg

#. Press the button again to power up the board
#. Wait for the board to boot (LED should turn blue); it will take about 30
   seconds to fully boot the board

.. figure:: images/test_command_1_short_power_bttn_press.png
   :width: 45em

   Short power button press

**Test USB_POWER boot:**

During this test, perform the following:

#. Plug in the DUT ETH cable
#. Plug the USB-C power cable in USB_POWER port of the DUT

.. figure:: images/test_command_1_usb_power_boot.png
   :width: 45em

   USB_POWER boot test

**USB_DATA port testing - Host mode:**

Plug OTG cable with a connected USB3 flash device (OTG cable labeled USB DONGLE)
in the DATA USB C port.

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - OTG cable connection
     - .. figure:: images/otg_cable_conn.png

   * - Host mode test
     - .. figure:: images/test_command_1_host_mode.png

Replug OTG cable but rotated 180 degrees:

.. figure:: images/replug_rotated_otg_cable.png
   :width: 45em

   Replug OTG cable rotated 180 degrees

**USB_DATA port testing - Device mode:**

Plug in USB_DATA Type C cable between Pi and DUT:

.. figure:: images/usb_data_type_c_between_pi_and_dut_plug.png
   :width: 45em

   USB_DATA Type C cable between Pi and DUT

Replug cable but rotated 180 degrees:

.. figure:: images/usb_data_type_c_between_pi_and_dut_replug.png
   :width: 45em

   Replug USB_DATA Type C cable rotated 180 degrees

After the test suite passed, a green "PASSED" message will appear on the screen.

.. figure:: images/test_command_1_passed.png
   :width: 45em

   Test Main Board passed

When at least one test is failing, at the end of the test suite a "FAILED"
message will be displayed.

.. note::

   In case a failure occurred, a "FAILED" message will be displayed and you will
   be prompted to enter a new command.

   If at any point a test fails, you are prompted with a message saying:
   "Do you want to repeat test?". In case the test failed due to an unconnected
   cable, or some exceptional reason, you can opt to repeat the last test as
   shown below:

   .. figure:: images/test_command_1_repeat_test.png
      :width: 45em

      Repeat test option

   Alternatively, if you realize that there is something wrong with the board
   and you do not wish to continue with the rest of the procedure, you can press
   "n" + "ENTER" and stop the test, which will also prompt a test failure:

   .. figure:: images/test_command_1_stop_test.png
      :width: 45em

      Stop test option

2) Add-on Test
""""""""""""""

Type "2" into the terminal and press ENTER to start **2) Add-ON test**.

.. figure:: images/test_command_2_addon_test.png
   :width: 45em

   Add-on test option

In case a failure occurred, a "FAILED" message will be displayed.

After the test is passed, a green "PASSED" message will appear on the screen.

.. figure:: images/test_command_2_addon_test_passed.png
   :width: 45em

   Add-on test passed

3) System Test
""""""""""""""

Type "3" and press ENTER to start **3) System Test**.

Make sure:

* SD card inserted in slot
* Ethernet cable connected
* RF Loopback cables on the ADD-ON ports
* RF terminators on the MAIN BOARD ports
* Dymo Label printer is inserted into Raspberry Pi USB port (instead of QR code
  reader)

Press ENTER to continue.

.. figure:: images/test_command_3_system_test.png
   :width: 45em

   System test

After the system test PASSes, a QR code label will be printed and should be
stuck on the bottom of the enclosure.

**Test Status LED:**

Is Status LED blinking?

.. figure:: images/test_command_3_test_status_led.jpg
   :width: 45em

   Test status LED

Pass Criteria
"""""""""""""

* **Main boards test:** Test 1) has successfully passed
* **Add-on boards:** Test 2) has successfully passed
* **System:** Test 3) has successfully passed

5) Repair SD Card
"""""""""""""""""

.. note::

   In the unlikely case the board is not behaving as expected, run the
   **5) Repair SD card** option in order to repair the boot image. Please be
   aware that you will be required to input the password ``analog`` three times
   during the repair steps.

.. figure:: images/test_command_5_repair_sd_card.png
   :width: 45em

   Repair SD card option

4) Power-Off Pi
"""""""""""""""

When you are done testing, press "4" and press ENTER to power-off the
Raspberry Pi.
