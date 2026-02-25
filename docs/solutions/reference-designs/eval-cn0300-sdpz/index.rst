.. _eval-cn0300-sdpz:

EVAL-CN0300-SDPZ
=================

Closed-Loop Thermocouple Measurement System with 4--20 mA Output.

Overview
--------

:adi:`CN0300` is a complete closed-loop precision analog microcontroller
thermocouple measurement system with 4 mA to 20 mA output. This circuit uses
the :adi:`ADuCM360 <ADUCM360>` to show how a thermocouple and RTD can be
amplified and sampled using the internal programmable gain amplifier (PGA) and
high-performance ADC. The DAC output is then set to control the 4--20 mA
transmitter interface. :adi:`CN0300` demonstrates the high performance and
circuit integration of the :adi:`ADuCM360 <ADUCM360>` -- amplifier, ADC, CPU,
DAC, and op-amp all in one chip.

Required Equipment
------------------

- :adi:`EVAL-CN0300-EB1Z <CN0300>` evaluation board
- CN0300 Evaluation Software
- USB-SWD/UART board
- USB cable
- T-type thermocouple
- Current meter (connected in series with 12 V supply)
- 12 V DC power supply
- PC or laptop

Minimum PC/System Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Windows XP SP2, Windows Vista, or Windows 7
  Business/Enterprise/Ultimate editions
- Intel Pentium processor (x86 compatible), 1 GHz or faster
- 512 MB RAM and 1 GB available hard disk space
- USB port

Driver Installation
--------------------

#. Ensure your PC has the USB drivers for the USB-SWD/UART board.
#. To install the drivers for the USB-SWD/UART board, unzip the
   **CDM 2.04.06** file for Windows XP drivers.
#. For other operating systems, download the drivers from the
   `FTDI website <https://ftdichip.com/drivers/>`__.

Hardware Setup
--------------

#. Connect the EVAL-CN0300-EB1Z board to the USB-SWD/UART board.
#. Connect a 12 V power supply to **J3**. Make sure to connect a current
   meter in series with the 12 V terminal. Short the inputs at **J2**
   together.

   .. figure:: cn0300-hardware-test-setup.jpg
      :width: 500px
      :align: center

      Hardware test setup

#. Connect the USB-SWD/UART board to your PC via a USB cable (ensure the
   driver is installed correctly).

Verifying Operation
--------------------

#. Determine the COM port your PC has allocated to the USB-SWD/UART board.
   Go to **Settings > Control Panel > System > Hardware > Device Manager**
   to find the allocated COM port.

   .. figure:: cn0300-pc-device-manager.jpg
      :align: center

      Device Manager showing the allocated COM port

#. Press the reset button on the EVAL-CN0300-EB1Z board. The following should
   appear on the HyperTerminal window. The current reading on the current
   meter should match the value **Expected DAC Current** on the screen.

   Configure HyperTerminal for the appropriate COM port with the following
   settings: 9600 baud rate, 8 data bits, no parity, 1 stop bit, no flow
   control.

   .. figure:: cn0300-software-hyperterminal4.jpg
      :align: center

      HyperTerminal output after reset

Calibrating the DAC (Optional)
-------------------------------

This procedure is only needed if a recalibration is desired.

#. Open the application **CM3WSD.exe**.

   .. figure:: cn0300-software-wsd.jpg
      :align: center

      CM3WSD application

#. Using the **Browse** tab, select the file **CN0300_test.hex**.

#. Select the **Configure** tab and select the :adi:`ADuCM360 <ADUCM360>` in
   the **Parts** tab.

   .. figure:: cn0300-software-wsd1.jpg
      :align: center

      Selecting the ADuCM360 in the Parts tab

#. Select the **Comms** tab. Select the appropriate COM port as determined
   previously. A baud rate of 9600 is fine.

   .. figure:: cn0300-software-wsd2.jpg
      :align: center

      Comms tab with COM port and baud rate settings

#. Select the **Command** tab. Enable the **Program and Verify** tabs.

   .. figure:: cn0300-software-wsd3.jpg
      :align: center

      Command tab with Program and Verify enabled

#. Force the part into download mode: hold the **SD** button on the
   EVAL-CN0300-EB1Z board while pressing and releasing the **RESET** button.

#. Click the **Start** button on CM3WSD.

   .. figure:: cn0300-software-wsd4.jpg
      :align: center

      CM3WSD download progress

#. Close CM3WSD and open **HyperTerminal** on your PC.

#. Set HyperTerminal for the appropriate COM port: 9600 baud rate, 8 data
   bits, no parity, 1 stop bit, no flow control.

#. Press reset. The calibration interface should appear on the terminal.

   .. figure:: cn0300-software-hyperterminal.jpg
      :align: center

      HyperTerminal calibration interface after reset

#. Your current meter should report a value close to 4 mA. If it does not,
   follow the instructions on the HyperTerminal screen to calibrate the DAC
   output to 4 mA by pressing the ``1`` or ``0`` keys accordingly. Ensure
   you select the HyperTerminal screen before pressing 1 or 0.

#. Press Return when the current meter reports 4 mA.

#. Repeat the previous step for the 20 mA calibration.

   .. figure:: cn0300-software-hyperterminal1.jpg
      :align: center

      HyperTerminal 20 mA calibration

#. After calibration, the program will continuously output temperature and
   current data. The final temperature reported should be within a few
   degrees C of the expected ambient temperature (+/-5 C is acceptable since
   the ADC is not fully calibrated).

   .. figure:: cn0300-software-hyperterminal2.jpg
      :align: center

      Continuous temperature and current output

#. Temporarily disconnect the COM port from HyperTerminal by pressing the
   phone icon.

   .. figure:: cn0300-software-hyperterminal3.jpg
      :align: center

      Disconnecting the COM port in HyperTerminal

#. Repeat steps 2 through 10, except this time select the file
   **CN0300_Final.hex**. This file is very similar to the test program except
   it does not call the DAC calibration function.

   .. figure:: cn0300-software-wsd5.jpg
      :align: center

      Loading CN0300_Final.hex in CM3WSD

#. Close CM3WSD. Return to HyperTerminal and select **Connect** by pressing
   the phone icon.

Documents
---------

- :adi:`CN0300 Circuit Note <CN0300>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0300-EB1Z Design & Integration Files
   <https://www.analog.com/cn0300-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`ADuCM360 Product Page <ADUCM360>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
