Production Testing
==================

Overview
--------

The purpose of the test procedure is to identify connectivity issues, poor
soldering, and potential manufacturing defects. Some of the issues are directly
identified by explicit part-targeted tests, others are implicit, by running
adjacent tests.

.. figure:: images/adrd5161_board_image.png
   :width: 30em

   ADRD5161-01Z BMS board

.. attention::

   Before running the production tests, the boards need FTDI programming.
   See :ref:`ftdi-programming` section below.

.. _ftdi-programming:

FTDI Programming
----------------

Before running the production tests, the boards need FTDI programming. Follow
the steps below to program the FTDI.

Required Hardware
^^^^^^^^^^^^^^^^^

* FTDI programming fixture (resistor board with programming area)
* ADRD5161 board (D.U.T)
* Load resistors
* USB cable for connection to PC

Required Software
^^^^^^^^^^^^^^^^^

* MAX77958 TypeC/PD & MAX77962 Charger EV Kit application
* Firmware binary file (``.bin``)

Programming Steps
^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - No.
     - Steps
   * - 1
     - Set up the jumper positions on the programming fixture:

       * Both jumpers on I2C position
       * Jumper on 3V3 position

       .. figure:: images/ftdi_programming/jumper_positions.png
          :width: 30em

          Jumper positions for FTDI programming
   * - 2
     - Connect the ADRD5161 board to the load as shown below:

       .. figure:: images/ftdi_programming/load_connection.png
          :width: 30em

          ADRD5161 and load connection
   * - 3
     - Connect the fixture to the PC via USB cable
   * - 4
     - Open the **MAX77958 TypeC/PD & MAX77962 Charger EV Kit** application
   * - 5
     - Go to **Device > Connect** to connect to the device. If scanning fails,
       a dialog will appear asking "Could not confirm existence of devices.
       Do you want to continue?" - click **Yes** to proceed

       .. figure:: images/ftdi_programming/device_scanning.png
          :width: 40em

          Device scanning and connection
   * - 6
     - Once connected, go to **Tools > Firmware Update...**

       .. figure:: images/ftdi_programming/firmware_programming_commands.png
          :width: 40em

          Firmware update menu navigation
   * - 7
     - In the Firmware Update window:

       * Click **Open** to select the firmware file
       * Navigate to the firmware location and select the appropriate
         ``.bin`` file
       * Click **Start** to begin programming
   * - 8
     - Wait for the firmware to be written. A completion message will appear:
       "Write firmware data to the device...Completed."

       .. figure:: images/ftdi_programming/firmware_writing_completion_message.png
          :width: 30em

          Firmware writing completion message
   * - 9
     - Verify the programming was successful by checking the LED feedback on
       the resistor board. Once the FTDI is programmed, the red LED must be ON

       .. figure:: images/ftdi_programming/led_feedback_ftdi_programming.png
          :width: 30em

          LED feedback after FTDI programming
   * - 10
     - Disconnect the board from the application by going to
       **Device > Disconnect**

       .. figure:: images/ftdi_programming/board_disconnection_from_app.png
          :width: 30em

          Board disconnection from application
   * - 11
     - Remove the board from the fixture and proceed with production testing

Test Procedure
--------------

Test Duration
^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Step Description
     - Estimated Time (minutes)
   * - Test bench setup
     - 5 min
   * - Software test
     - 6 min
   * - **Total time**
     - **11 min**

Required Hardware
^^^^^^^^^^^^^^^^^

* ADRD5161 board as Device Under Test
* Raspberry Pi, HDMI cable, power supply, mouse and keyboard
* Power supply USB C (20V, 5A)
* MAXPICO 32650 programmer (Daplink)
* CAN2USB cable
* Battery
* Resistor board

Required Software
^^^^^^^^^^^^^^^^^

The test image will be provided as a SD test card that goes into the Raspberry
Pi.

Test Setup
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - No.
     - Steps
   * - 1
     - Insert the SD card into the Raspberry Pi
   * - 2
     - Connect the Raspberry Pi to a monitor and power it
   * - 3
     - Connect the Daplink programmer to the D.U.T and the Raspberry Pi

       .. figure:: images/daplink_programmer_connection.png
          :width: 30em

          Daplink programmer connection
   * - 4
     - Connect the CAN to USB cable to the D.U.T and the Raspberry Pi

       .. figure:: images/can_to_usb_adaptor_connection.png
          :width: 30em

          CAN to USB adaptor connection
   * - 5
     - Connect the resistor board to -/+ on the DUT as seen in the picture below

       .. figure:: images/resistor_board_and_connections.png
          :width: 30em

          Resistor board and connections
   * - 6
     - Connect the battery to XT60 connector on the D.U.T and the balancing
       connector (picture below)

       .. figure:: images/adrd5161_battery_connections.png
          :width: 30em

          Battery connections
   * - 7
     - Connect the power supply USB C into the D.U.T

       .. figure:: images/usb_power_supply_connection.png
          :width: 20em

          USB power supply connection

Enabling Wifi
^^^^^^^^^^^^^

Before starting the testing procedure, make sure the Raspberry Pi is connected
to Wifi.

#. After the RPi boots, press **CONTROL+C** to exit the test screen
#. Click on the Wifi network you want to connect to

   .. figure:: images/wifi_connection_1.png
      :width: 30em

      Wifi network selection

#. Type in the password
#. After connecting successfully, reboot the Raspberry Pi by following the
   instructions below:

   .. figure:: images/logout.png
      :width: 20em

      Logout menu

   .. figure:: images/reboot.png
      :width: 15em

      Reboot option

Running the Test Software
^^^^^^^^^^^^^^^^^^^^^^^^^

After reboot, the following test menu should appear:

.. figure:: images/test_menu.png
   :width: 25em

   Test menu

.. code-block:: text

   Please enter your choice:
   1) MAX17320 Ini Flash
   2) Firmware Flash
   3) System Test
   4) Power-Off Pi

1) MAX17320 Ini Flash
"""""""""""""""""""""

Type "1" into the terminal and press **ENTER** to start **1) MAX17320 Ini
Flash**.

Please verify that the programmer is connected to header P7, then press Enter.

.. figure:: images/ini_flash_test_passed.png
   :width: 35em

   MAX17320 Ini Flash test passed

After the first test is passed, move on by writing "2" in the terminal.

2) Firmware Flash
"""""""""""""""""

Type "2" into the terminal and press **ENTER** to start **2) Firmware Flash**.

Please verify that the programmer is connected to header P7, then press Enter.

.. figure:: images/firmware_flash_test_menu.png
   :width: 25em

   Firmware Flash menu selection

.. figure:: images/firmware_flash_test_menu_passed.png
   :width: 35em

   Firmware Flash test passed

3) System Test
""""""""""""""

Type "3" in the terminal in order to run **3) System Test**.

.. figure:: images/system_test_screen_1.png
   :width: 30em

   System Test - CAN network connection and readings

.. figure:: images/system_test_screen_2.png
   :width: 30em

   System Test - Object Dictionary values

If no errors are found, the message "No Errors. System test passed." will be
displayed.

.. figure:: images/system_test_screen_passed.png
   :width: 30em

   System Test passed

Next, you will need to unplug the USB C power supply from the D.U.T. When
prompted, check if the red LED is on (see picture below) and type **y** or
**n**.

For the current test, read the display on the board. The value should be
approximately 500 mA. If around that value, type **y**.

.. figure:: images/screen_output.png
   :width: 35em

   LED and current verification

After all tests pass, a green **PASSED** message will appear on the screen.

.. warning::

   If a **FAILED** message appears, check the connections and verify that all
   cables are properly connected. You may repeat the failed test if it was due
   to a connection issue.

4) Power-Off Pi
"""""""""""""""

When you are done testing, press "4" and press **ENTER** to power-off the
Raspberry Pi.

Pass Criteria
^^^^^^^^^^^^^

* **MAX17320 Ini Flash:** Test 1) has successfully passed
* **Firmware Flash:** Test 2) has successfully passed
* **System Test:** Test 3) has successfully passed with LED verification and
  current reading approximately 500 mA
