ADRD4161-01Z Production Testing
================================

Overview
--------

The purpose of the test procedure is to identify connectivity issues, poor
soldering, and potential manufacturing defects. Some of the issues are directly
identified by explicit part-targeted tests, others are implicit, by running
adjacent tests.

Test Duration
-------------

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Step Description
     - Estimated Time (minutes)
   * - Test bench setup
     - 5 min
   * - Software test
     - 5 min
   * - **Total time**
     - **10 min**

Test Requirements
-----------------

Required Hardware
^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - 1x
     - Raspberry Pi 5
   * - 1x
     - Micro HDMI cable
   * - 1x
     - USB-A to USB-C data cable
   * - 1x
     - Mouse and keyboard
   * - 1x
     - Device-Under-Test (DUT) ADRD4161
   * - 1x
     - CAN to USB adapter
   * - 1x
     - ADIS167X board
   * - 1x
     - 12V power supply
   * - 1x
     - LED connector

Required Software
^^^^^^^^^^^^^^^^^

The test image will be provided as a SD test card that goes into the Raspberry
Pi.

Required Setup
^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - No.
     - Steps
   * - 1
     - Insert the SD card into the Raspberry Pi
   * - 2
     - Connect the Raspberry Pi to a monitor using a micro-HDMI cable
   * - 3
     - Connect the mouse and keyboard to the Raspberry Pi
   * - 4
     - Connect the ADRD4161 (DUT) to the Raspberry Pi using the ribbon cable
   * - 5
     - Connect the ADIS167X board on the back of the ADRD4161 (DUT)
   * - 6
     - Connect the CAN to USB adapter to the ADRD4161 (DUT) and to the
       Raspberry Pi using the USB-A to USB-C cable
   * - 7
     - Connect the LED connector to the ADRD4161 (DUT)
   * - 8
     - Connect the 12V power supply into the ADRD4161 (DUT)

.. figure:: images/system_connections.png
   :width: 30em

   System connections

.. figure:: images/adrd4161_connections.png
   :width: 30em

   ADRD4161 (DUT) connections

.. figure:: images/adis167x_connection.png
   :width: 30em

   ADIS167X to DUT connection

.. figure:: images/led_connection.png
   :width: 30em

   LED connector connection

Test Process
------------

Enabling Wifi
^^^^^^^^^^^^^

Before starting the testing procedure, make sure the Raspberry Pi is connected
to Wifi.

#. After the RPi boots, press ``CONTROL+C`` to exit the test screen.
#. Click on the Wifi network you want to connect to.

.. figure:: images/wifi_conn_1.png
   :width: 30em

   Wifi connection

3. Type in the password. After successfully connected, reboot the Raspberry Pi
   by following the below instructions.

.. figure:: images/logout.png
   :width: 20em

   Logout menu

.. figure:: images/reboot.png
   :width: 15em

   Reboot option

Running the Test Software
^^^^^^^^^^^^^^^^^^^^^^^^^

After the Raspberry Pi reboots, the test screen will appear on the monitor as
shown below.

.. figure:: images/test_screen.png
   :width: 30em

   Test screen

The following test menu should appear:

.. code-block:: text

   [ADRD4161] Please enter your choice:
   1) CAN Test
   2) IMU Test
   3) GPIO Test
   4) Power-Off Pi

1) CAN Test
"""""""""""

Type "1" into the terminal and press ``ENTER`` to start the **1) CAN Test**
test suite.

Make sure the CAN to USB adapter is connected to the ADRD4161 (DUT) and
Raspberry Pi boards as shown in the system connections figure.

.. figure:: images/can_test_screen.png
   :width: 40em

   CAN Test screen

Visually check if the DS1 and DS2 LEDs are blinking. Type "y" if yes or "n"
for not when prompted. You can see their position in the ADRD4161 connections
and LED connector figures above.

.. warning::

   If a "FAILED" message appears, check the USB connection to the CAN to USB
   adapter (found on port P7) and re-run the test for up to 3 times.

If the test runs with no failures, a green "PASSED" message will appear on the
screen.

.. figure:: images/passing_can_test_screen.png
   :width: 40em

   Passing CAN Test screen

2) IMU Test
"""""""""""

Type "2" into the terminal and press ``ENTER`` to start the **2) IMU Test**.

Make sure the ADIS167X (IMU) board is properly connected to the ADRD4161 (DUT)
board, as shown in the ADIS167X connection figure.

.. warning::

   In case a failure occurs, a "FAILED" message appears. Check the presence of
   the ADIS167X board and its connections and re-run the test for up to 3 times.

If the second test runs with no failures, a green "PASSED" message will appear
on the screen.

.. figure:: images/passing_imu_test_screen.png
   :width: 30em

   Passing IMU test screen

3) GPIO Test
""""""""""""

Type "3" into the terminal and press ``ENTER`` to start the **3) GPIO Test**.

Make sure the LED connector is connected to the ADRD4161 (DUT) board as shown
in the LED connector figure.

Visually check if the LED connector connected to the GPIO header is on. Type
"y" if yes or "n" for no.

.. warning::

   In case a failure occurs, a "FAILED" message appears. Check that the LED
   connector is properly connected and re-run the test for up to 3 times.

If the third test runs with no failures, a green "PASSED" message will appear
on the screen.

.. figure:: images/passing_gpio_test_screen.png
   :width: 30em

   Passing GPIO test screen

Pass Criteria
"""""""""""""

After the tests **1)**, **2)** and **3)** have successfully passed, you can
consider the DUT as being functional.

4) Power-Off Pi
"""""""""""""""

Type "4" and press ``ENTER`` in the terminal to power off the RPi. Disconnect
the LED connector and CAN to USB adapter from the last tested DUT. Disconnect
the last tested DUT from the RPi by removing the ribbon cable.

Repeat the testing procedure for the next DUT.

.. note::

   If at any point a test fails, you should retry the test suite for up to 3
   times.
