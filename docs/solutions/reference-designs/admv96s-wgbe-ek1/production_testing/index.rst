.. _admv96s-wgbe-ek1 production_testing:

Production Testing
==================

Overview
--------

This document describes the production test procedure for the
:adi:`ADMV96S-WGBE-EK1` multi board kit. The procedure focuses on firmware
programming and testing the two BR-073235 boards included in the kit.

Pre-Required Setup
------------------

Board Assembly
~~~~~~~~~~~~~~

The disassembled boards must be assembled as a DUT (Device Under Test) before
proceeding with the testing steps.

.. figure:: images/disassembled_board.png
   :width: 45em

   Disassembled boards overview

.. figure:: images/disassembled_board_1.png
   :width: 45em

   Disassembled board components - view 1

.. figure:: images/disassembled_board_2.png
   :width: 45em

   Disassembled board components - view 2

#. Attach the right-angle connectors with the screws to the support PCB and the
   BR-073235.

#. Populate the ADMV96x5 module on the board and read the label to identify
   whether it is an ADMV9615 or ADMV9625.

   .. figure:: images/populated_board_module.png
      :width: 45em

      Populated board with module

   .. list-table::
      :widths: 50 50
      :header-rows: 1

      * - ADMV9615 Label
        - ADMV9625 Label
      * - .. figure:: images/admv9615_label.png

        - .. figure:: images/admv9625_label.png

#. With a small tool like a screwdriver, move the S1 switch into ADMV9615 or
   ADMV9625 position depending on which module was installed.

   .. list-table::
      :widths: 50 50
      :header-rows: 1

      * - ADMV9615 Switch Position
        - ADMV9625 Switch Position
      * - .. figure:: images/admv9615_switch_position.png

        - .. figure:: images/admv9625_switch_position.png

#. Mount the board on the test-jig in the correct position:

   * If the newly assembled board has an **ADMV9615** module, mount it in front
     of the **REFERENCE ADMV9625**.
   * If the newly assembled board has an **ADMV9625** module, mount it in front
     of the **REFERENCE ADMV9615**.

   .. list-table::
      :widths: 50 50
      :header-rows: 0

      * - .. figure:: images/test_jig_mount.jpg

        - .. figure:: images/test_jig_mount_2.jpg.png

Heatsink Assembly
~~~~~~~~~~~~~~~~~

Mount a heatsink (S08ERQ0J-D) on each BR-073235 before packaging.

Steps for assembling the heatsink:

#. Make sure the S08ERQ0J-D heatsink has the thermal pad in the approximate
   position shown in the datasheet.

   .. figure:: images/heatsink_assembly_schematic.png
      :width: 45em

      Heatsink assembly schematic

#. Peel the liner from the thermal pad and make sure it sticks to the
   highlighted area of the board.

   .. figure:: images/heatskin_position.png
      :width: 45em

      Heatsink position on the board

#. Two aluminum unthreaded spacers (94669A101) must be placed between the
   BR-073235 and heatsink on the pins that go in the corners of the board.

   .. list-table::
      :widths: 50 50
      :header-rows: 0

      * - .. figure:: images/aluminium_spacers_schematic.png

        - .. figure:: images/aluminium_spacers_position.png

Test Process
------------

Required Hardware
~~~~~~~~~~~~~~~~~

* Raspberry Pi 4
* Mouse and keyboard
* Ethernet to Usb3 adapter
* :adi:`MAX32625PICO` (Daplink programmer) x2
* Ethernet cable
* Raspberry Pi power supply
* Raspberry Pi HDMI cable
* Display
* 2 Power supplies for the ADMV96S-WGBE
* 2 Reference ADMVs mounted to a support

Required Software
~~~~~~~~~~~~~~~~~

SD card with the test image.

Required Setup
~~~~~~~~~~~~~~

#. Insert the SD card into the Raspberry Pi.

#. Connect an Ethernet cable from the Pi Ethernet port to the D.U.T Ethernet
   port.

#. Connect an Ethernet cable to the reference ADMV and via an Ethernet to Usb3
   adapter, connect it to the Pi Usb3.0 hub.

#. Connect the Daplink cable to the Raspberry Pi Usb on one side and to the
   jtag swd connector of the D.U.T. on the other side.

#. Connect the HDMI cable to the Pi and a Display.

#. Connect the keyboard and mouse dongle into the Raspberry Pi.

#. Connect the Raspberry Pi power adapter.

#. Power the DUT and the reference ADMV.

.. figure:: images/system_setup.jpg
   :width: 45em

   Complete system setup

Testing Procedure
-----------------

Wi-Fi Setup
~~~~~~~~~~~

Make sure the Raspberry Pi is connected to Wi-Fi before starting the tests.

#. Power the Raspberry Pi.

#. Press **CONTROL+C** to exit the test screen.

#. Click on the network and type in the password.

   .. list-table::
      :widths: 50 50
      :header-rows: 0

      * - .. figure:: images/wifi_connection.png

        - .. figure:: images/wifi_password.jpg

#. Reboot the Raspberry Pi to reinitialize the test screen by following the
   screen instructions.

   .. list-table::
      :widths: 50 50
      :header-rows: 0

      * - .. figure:: images/reboot.png

        - .. figure:: images/logout.jpg

Running the Tests
~~~~~~~~~~~~~~~~~

After rebooting the Raspberry Pi, the test screen will appear. Make sure the
DUT and the reference board are perfectly parallel, facing each other.

.. figure:: images/dut_and_ref_board_setup.jpg
   :width: 45em

   DUT and reference board setup

1) Provisioning Test
^^^^^^^^^^^^^^^^^^^^

Type **1** from the keyboard to start the Provisioning test.

.. figure:: images/test_command_1.jpg
   :width: 45em

   Starting the Provisioning test

The test has two parts: writing the firmware and checking that it is the
"Production firmware", and writing attributes.

.. figure:: images/test_command_1_wip.jpg
   :width: 45em

   Provisioning test in progress

If the test is successful, a **PASSED** message will appear.

.. figure:: images/test_command_1_passed.jpg
   :width: 45em

   Provisioning test passed

2) ADMV96x5 Test
^^^^^^^^^^^^^^^^

Type **2** to run the ADMV96x5 Test.

.. figure:: images/test_command_2.jpg
   :width: 45em

   Starting the ADMV96x5 test

If the test is successful, the **PASSED** message will appear.

.. figure:: images/test_command_2_passed.jpg
   :width: 45em

   ADMV96x5 test passed

3) Network Test
^^^^^^^^^^^^^^^

Type **3** to run the Network Test.

.. figure:: images/test_command_3.jpg
   :width: 45em

   Starting the Network test

If the test is successful, the **PASSED** message will appear.

.. figure:: images/test_command_3_passed.jpg
   :width: 45em

   Network test passed

.. attention::

   If the networking test fails, unplug and plug again the Usb3 to Ethernet
   adapter into the Raspberry Pi.

After all tests are completed, proceed to the next untested DUT and repeat the
testing procedure.

When done testing, type **4** to power off the Raspberry Pi.
