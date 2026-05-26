.. _ad-rpi-t1lpse-sl production_testing:

Production Testing
==================

Overview
--------

The purpose of the test procedure is to identify connectivity issues, poor
soldering, and potential manufacturing defects. Some of the issues are directly
identified by explicit part-targeted tests, others are implicit, by running
adjacent tests.

.. note::

   Before production testing the AD-RPI-T1LPSE-SL board, the FTDI chip needs to
   be programmed. See the :ref:`rpit1lpse_ftdi_programming` section below.

.. _rpit1lpse_ftdi_programming:

FTDI Programming
----------------

Programming the board is done using the MAX77958_2S3 software, which can only
be installed on Windows.

Required Hardware
~~~~~~~~~~~~~~~~~

* Raspberry Pi used for production testing
* 1 x PC with Windows 10
* MAX77958EVKIT-2S3 V1.0.0
* Usb Type-C cable
* :adi:`MAX32625PICO` (Daplink programmer)
* Usb to I2C adapter board

Required Software
~~~~~~~~~~~~~~~~~

* ``secure_update_BC58_verD005.bin`` - binary file containing the firmware
* MAX77958EVKIT-2S3 V1.0.0 installed on Windows 10 - available from the
  `ADI Software Download page <https://www.analog.com/en/design-center/evaluation-hardware-and-software/software/software-download.html?swpart=SFW0011130G>`__

Required Setup
~~~~~~~~~~~~~~

.. figure:: images/ftdi_programming_required_setup.png
   :width: 45em

   FTDI programming required setup

Programming Procedure
~~~~~~~~~~~~~~~~~~~~~

#. Power the device under test and make sure S2 switch is in position as shown
   in the image above.

#. Connect the mini programmer to the PC and open the MAX77958EVKIT-2S3 V1.0.0
   application. This step can be done only once and the app can be kept open
   for programming the next board.

   .. figure:: images/ftdi_programming_connection_setup.png
      :width: 45em

      Connection setup

#. In the opened app, connect to the test board by clicking on
   **Device -> Connect -> Yes -> Read and Close**.

#. In the opened MAX77958_2S3 app, click on **Tools -> Firmware Update... ->
   Open** -> select ``secure_update_BC58_verD005.bin`` in the folder where it
   is saved -> **Open -> Start**.

   .. figure:: images/ftdi_programming_firmware_programming_commands.png
      :width: 45em

      Commands to program the firmware

#. Wait for the board to be programmed until the "...Completed" message is
   displayed.

   .. figure:: images/ftdi_programming_firmware_programming_completion_message.png
      :width: 45em

      Completion message for writing the firmware

#. Disconnect the board from MAX77958_2S3 application by clicking
   **Device -> Disconnect**.

   .. figure:: images/ftdi_programming_board_disconnection.png
      :width: 45em

      How to disconnect the board from MAX77958_2S3 application

After disconnecting the board from the PC, follow the instructions in the
testing procedure below.

Test Duration
-------------

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Step Description
     - Estimate Time (minutes)
   * - Test bench setup
     - 3 min
   * - Software test
     - 5 min
   * - **Total time**
     - **8 min**

Test Requirements
-----------------

Required Hardware
~~~~~~~~~~~~~~~~~

* Raspberry Pi 4
* HDMI cable
* Mouse and keyboard
* :adi:`AD-RPI-T1LPSE-SL` (Device Under Test)
* T1L cable and :adi:`AD-SWIOT1L-SL` board
* 12V power supply Usb Type-C

Required Software
~~~~~~~~~~~~~~~~~

The test image is provided on a pre-configured SD card.

Required Setup
~~~~~~~~~~~~~~

#. Insert the SD card into the Raspberry Pi.

#. Connect the Raspberry Pi to a monitor, keyboard, and mouse.

#. Insert the AD-RPI-T1LPSE-SL on top of the Raspberry Pi.

#. Connect the T1L cable to AD-RPI-T1LPSE-SL and the AD-SWIOT1L-SL board.

#. Power the AD-RPI-T1LPSE-SL using a Type-C power supply (12V).

.. figure:: images/rpi_setup.png
   :width: 45em

   Raspberry Pi setup

.. figure:: images/system_setup.png
   :width: 45em

   Complete system setup

Test Process
------------

Wi-Fi Setup
~~~~~~~~~~~

Make sure the Raspberry Pi is connected to Wi-Fi before starting the tests.

#. Power the Raspberry Pi.

#. Press **CONTROL+C** to exit the test screen.

#. Click on the network and type in the password.

   .. figure:: images/wifi_connection.png
      :width: 45em

      Wi-Fi connection

#. After successfully connecting, reboot the Raspberry Pi by following the
   instructions below.

   .. figure:: images/reboot1.png
      :width: 45em

      Reboot instructions

Running the Tests
~~~~~~~~~~~~~~~~~

After the Raspberry Pi reboots, the test screen will appear on the monitor.

.. figure:: images/test_monitor.png
   :width: 45em

   Test menu

1) System Test
^^^^^^^^^^^^^^

Type **1** into the terminal then press **ENTER** to start "1) System Test".

.. figure:: images/test_command_1.png
   :width: 45em

   Starting the System test

Connect the T1L cable to port 1.

.. figure:: images/test_command_1_board.png
   :width: 45em

   T1L cable connection to port 1

If the test is **PASSED**, the DUT is functional. Continue testing the other
boards.

.. figure:: images/test_command_1_passed.png
   :width: 45em

   System test passed
