.. _ad_fmcmotcon1_ebz zedboard_quickstart:

AD-FMCMOTCON1-EBZ Linux on Zynq Quick Start Guide
===============================================================================

.. warning::

   The :adi:`AD-FMCMOTCON1-EBZ` is a **legacy product** and is no longer
   actively supported. This documentation is provided for reference only.

This guide provides some quick instructions (still takes awhile to download, and
set things up) on how to setup the AD-FMCMOTCON1-EBZ on either:

-  `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`_, Rev C or later

Requirements
-------------------------------------------------------------------------------

-  You need a Host PC (Windows or Linux).
-  You need a SD card writer connected to above PC (Supported USB SD readers/writers are OK).
-  USB keyboard/mouse for the Zynq Device
-  HDMI Display (monitor or TV)

Creating the SD Card
-------------------------------------------------------------------------------

:external+kuiper:doc:`Create SD Image for Zynq Boards <index>`

The carrier setup requires power, UART connection (115200 baud, 8N1), and
Ethernet (for Linux) connections. The ZedBoard programs the FPGA and boots
Linux from the SD card.

Connecting the hardware together
-------------------------------------------------------------------------------

.. figure:: ../images/mc_system.jpg
   :alt: AD-FMCMOTCON1-EBZ connected to ZedBoard
   :align: center
   :width: 600

   AD-FMCMOTCON1-EBZ connected to ZedBoard

Connect the hardware as follows:

- Connect the Low Voltage Drive Board (AD-DRVLV1-EBZ) to the Controller
  Board (AD-FMCMOTCON1-EBZ).
- Connect the Controller + Drive board assembly to the FMC connector of the
  ZedBoard.
- Insert the 6-pin Hall connector into P7 - pin 1 is the empty slot of the
  Hall connector. For an encoder, connect encoder pins one-to-one to P7.

.. figure:: ../images/hall_connector.jpg
   :alt: Hall sensor connector (P7)
   :align: center
   :width: 300

   Hall sensor connector (P7)

- Insert the 5 V supply into the left side of the Dynamometer Drive System
  (AD-DYNO1-EBZ), if used.

.. figure:: ../images/dyno_supply.jpg
   :alt: Dynamometer power supply connection
   :align: center
   :width: 300

   Dynamometer power supply connection

- Ensure that the Emergency Stop button (P2) is **pressed** before powering
  on (see :ref:`AD-DRVLV1-EBZ connectors and switches
  <ad_fmcmotcon1_ebz lv-board>` for more details).

.. figure:: ../images/emergency_stop.jpg
   :alt: Emergency Stop button (P2)
   :align: center
   :width: 300

   Emergency Stop button (P2)

- Insert the 3-pin motor connector into P1 and connect the lab power supply
  to P4 (24 V, 3 A minimum; see :ref:`AD-DRVLV1-EBZ connectors
  <ad_fmcmotcon1_ebz lv-board>` for connector pinout).

.. figure:: ../images/motor_power_connections.jpg
   :alt: Motor (P1) and power supply (P4) connections
   :align: center
   :width: 300

   Motor (P1) and power supply (P4) connections

- Power on the ZedBoard.
- After the board is programmed, to start the motor release the Emergency
  Stop button (P2) and then press the Reset switch (S1) for a few seconds.

Booting the SD Card
-------------------------------------------------------------------------------

-  Ignore your PC, and now interact on the USB mouse/keyboard on the Zynq device.
-  You should see two screens:

   -  Firefox:

      .. figure:: ../images/firefox.jpg
         :alt: Firefox browser on the Zynq device
         :align: center
         :width: 300

         Firefox browser on the Zynq device

   -  IIO Scope tool:

      .. figure:: ../images/iio_scope.jpg
         :alt: IIO Scope tool on the Zynq device
         :align: center
         :width: 300

         IIO Scope tool on the Zynq device

-  You are now done with booting from the SD card. You can interact with the GUI
   either over the network, or with the HDMI monitor/USB keyboard mouse.

Using IIO SCOPE for AD-FMCMOTCON1-EBZ
-------------------------------------------------------------------------------

For instructions on how to use the IIO Oscilloscope with this system, refer to
the :ref:`iio-oscilloscope` documentation.

.. important::

   Even thought this is Linux, this is a persistent file system. Care should be taken
   not to corrupt the file system -- please shut down things, don't just turn off the
   power switch. Depending on your monitor, the standard power off could be hiding.
   You can do this from the terminal as well with: ``sudo shutdown -h now``

   .. figure:: ../images/shutdown.jpg
      :alt: Shutdown dialog
      :align: center
      :width: 300

      Shutdown dialog
