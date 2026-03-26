ADRD3161-01Z Production Testing
===============================

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
     - 8 min
   * - Software test
     - 6 min
   * - **Total time**
     - **14 min**

Test Requirements
-----------------

Required Hardware
^^^^^^^^^^^^^^^^^

* Raspberry Pi 5, power supply
* HDMI cable, mouse, keyboard
* 1x USB to CAN adapter
* 1x CAN cable
* 1x motor :adi:`QSH5718-76-28-101-10k <qsh5718>`
* 1x encoder cable
* 1x :adi:`MAX32650` (Daplink programmer)
* 1x Power supply for device under test, crimped power cable
* :adi:`ADRD3161-01Z` as device under test (D.U.T.)
* SD card with the test image

Required Software
^^^^^^^^^^^^^^^^^

The test image will be provided as a SD test card that goes into the Raspberry Pi.

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
     - Connect the Raspberry Pi to a monitor and power it
   * - 3
     - Put jumpers on D.U.T. P12, P15 in position
   * - 5
     - Connect the CAN cable to P9 and the USB into the Raspberry Pi
   * - 6
     - Connect the encoder cable between P16 and the motor
   * - 7
     - Connect the motor cable to P3 header (see picture below)
   * - 8
     - Connect power supply to P10 on D.U.T. board
   * - 9
     - S2 switch in configuration shown in picture below
   * - 10
     - Connect the Daplink cable to P7 connector
   * - 11
     - Run 1) TMC bootstrapping
   * - 12
     - Move the Daplink to P6 connector
   * - 13
     - Run 2) Microcontroller Flash
   * - 14
     - Run 3) System test

.. note::

   * When running test **1) Bootstrapping TMC**, the Daplink should be connected to **P7 connector**
   * When running test **2) Microcontroller Flash** and **3) System Test**, the Daplink should be connected to **P6 connector**

Jumper Positions
""""""""""""""""

.. figure:: images/production_tests/p12_jumper_position.png
   :width: 45em

   P12 jumper connected

.. figure:: images/production_tests/p15_jumper_position.png
   :width: 45em

   P15 jumper connected

S2 Switch Configuration
"""""""""""""""""""""""

.. figure:: images/production_tests/s2_switch_config.png
   :width: 45em

   S2 switch configuration

Motor and Encoder Connections
"""""""""""""""""""""""""""""

When connecting the motor cable to P3, ensure the correct color order:

* UX1 = **black**
* VX2 = **green**
* WY1 = **red**
* Y2 = **blue**

.. figure:: images/production_tests/encoder_and_motor_cable_conn.png
   :width: 45em

   Encoder cable and motor cable connections

.. figure:: images/production_tests/motor_connections.png
   :width: 45em

   Motor connections

Daplink Connections
"""""""""""""""""""

.. figure:: images/production_tests/p7_connection.png
   :width: 45em

   Daplink on P7 for 1) TMC bootstrapping

.. figure:: images/production_tests/p6_connection.png
   :width: 45em

   Daplink on P6 for 2) Microcontroller flash

Power Connections
"""""""""""""""""

.. figure:: images/production_tests/power_connections.png
   :width: 45em

   Power connections

Complete Test Bench
"""""""""""""""""""

.. figure:: images/production_tests/system_connection.png
   :width: 45em

   Full system connection overview

Test Process
------------

Before starting the testing procedure, make sure the Raspberry Pi is connected
to Wi-Fi.

Enabling Wi-Fi
^^^^^^^^^^^^^^

#. After the RPi boots, press CONTROL+C to exit the test screen.
#. Click on the Wi-Fi network you want to connect to.

   .. figure:: images/production_tests/test_process_1_wifi_connection.png
      :width: 45em

      Wi-Fi network selection

#. Type in the password. After connecting successfully, reboot the Raspberry Pi.

   .. figure:: images/production_tests/test_process_2_reboot_conn.png
      :width: 45em

      Raspberry Pi menu

   .. figure:: images/production_tests/test_process_3_reboot_conn.png
      :width: 45em

      Shutdown options - select Reboot

Running the Tests
^^^^^^^^^^^^^^^^^

The following test menu should appear after reboot:

.. code-block:: text

   Please enter your choice:
   1) TMC Bootstrapping
   2) Firmware Flash
   3) System Test
   4) Power-Off Pi

1) TMC Bootstrapping
""""""""""""""""""""

Type "1" and press ENTER to run **1) TMC9660 Bootstrapping**. This step may fail
once, in which case try it again. If it fails twice then either:

* The board has already been through this test (check if any LEDs light up on
  the board)
* The board is defective

.. figure:: images/production_tests/test_menu_command_1.png
   :width: 45em

   TMC Bootstrapping process

When prompted ``Proceed with OTP burn? (y/n):``, press ``y`` then ENTER.

.. figure:: images/production_tests/test_menu_command_1_result.png
   :width: 45em

   TMC Bootstrapping passed

.. attention::

   **1) TMC Bootstrapping** test is a **one-time step**. It might fail if you run
   it multiple times. Thus, an error may be acceptable if the step was already
   run and passed in the past.

   To diagnose whether an error in this test is an actual fault, or just a
   result of running the step multiple times, do the following:

   * Press TMC_RST -> check DS1 lights up
   * Press MCU_RST -> check DS1 turns off

   .. list-table::
      :header-rows: 1
      :widths: 30 30 40

      * - After pressing RST_TMC
        - After pressing RST_MCU
        - Diagnosis
      * - DS1 lights up
        - DS1 turns off
        - OK! Both TMC and MCU are functional.
      * - DS1 lights up
        - DS1 stays on
        - TMC bootstrapped, MCU not functional (could be because step 2 didn't run yet)
      * - DS1 LED does not turn on
        - /
        - TMC fault/TMC not bootstrapped

After TMC Bootstrapping:

* Press RST_TMC button
* Press RST_MCU button

.. figure:: images/production_tests/reset_TMC_reset_MCU.png
   :width: 45em

   RST_TMC and RST_MCU buttons

2) Firmware Flash
"""""""""""""""""

Type "2" in order to run **2) Firmware Flash**. Connect the Daplink cable to
**P6 connector**.

.. figure:: images/production_tests/test_menu_command_2.png
   :width: 45em

   Firmware Flash process

When prompted, verify that the programmer is connected to header P6, then press
Enter.

.. figure:: images/production_tests/test_menu_command_2_result.png
   :width: 45em

   Firmware Flash passed

3) System Test
""""""""""""""

Type "3" to run **3) System Test**.

.. warning::

   THE MOTOR WILL MOVE during this test.

.. figure:: images/production_tests/test_menu_command_3.png
   :width: 45em

   System Test passed

If test 3) fails, it will display:

.. figure:: images/production_tests/test_menu_command_3_failure.png
   :width: 45em

   System Test failed
