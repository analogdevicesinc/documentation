.. _eval-ad7124-x quickstart sdp_b:

SDP-B Quick Start (Eval+ Software)
===============================================================================

.. esd-warning::

This guide describes how to use the AD7124 evaluation boards with the
:adi:`SDP-B` controller board and the AD7124 Eval+ Software.

This quickstart applies to the following evaluation boards:

- :adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>` and
  :adi:`EVAL-AD7124-8SDZ <EVAL-AD7124-8>` (7--9 V external supply
  required)
- :adi:`EVAL-AD7124-4ASDZ <EVAL-AD7124-8>` and
  :adi:`EVAL-AD7124-8ASDZ <EVAL-AD7124-8>` (USB-powered, no
  external supply required)

Prerequisites
-------------------------------------------------------------------------------

See :ref:`eval-ad7124-x prerequisites` for the full list.

**Hardware:**

- AD7124 evaluation board (one of the four boards listed above)
- :adi:`SDP-B` controller board
- USB cable
- DC signal source
- PC running Windows with a USB 2.0 port
- 7--9 V DC power supply (for EVAL-AD7124-4SDZ / EVAL-AD7124-8SDZ only)

**Software:**

- - AD7124 Eval+ Software (included on CD or :download:`downloadable <https://www.analog.com/media/en/evaluation-boards-kits/evaluation-software/ad7124-eval-plus-installer.zip>`)

Software installation
-------------------------------------------------------------------------------

.. warning::

   The evaluation software and drivers must be installed **before** connecting
   the evaluation board and controller board to the USB port of the PC, to
   ensure the system is correctly recognized.

Installing the AD7124 Eval+ Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. With the :adi:`SDP-B` disconnected from the PC, run the Eval+ Software
   installer (``setup.exe`` from the CD or downloaded package).
#. Select the installation location (default:
   ``C:\Program Files\Analog Devices\AD7124 EVAL+``).
#. Accept the license agreement and click **Next** to complete the
   installation.

Installing the SDP-B drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SDP-B driver installation begins automatically after the Eval+ Software
installation completes.

#. With the :adi:`SDP-B` still disconnected, select the driver installation
   location (default:
   ``C:\Program Files\Analog Devices\SDP\Drivers``).
#. Click **Install** to install the drivers.
#. Click **Finish** and restart the PC before using the evaluation board.

Setting up the hardware
-------------------------------------------------------------------------------

#. Connect the :adi:`SDP-B` to the evaluation board via the 120-pin SDP
   connector. Screw the two boards together using the plastic screw and washer
   set included in the evaluation board kit.

#. For the **EVAL-AD7124-4SDZ / EVAL-AD7124-8SDZ**: apply 7--9 V DC to
   connector J3 (bench top) or J5 (wall wart/DC plug). No external supply is
   needed for the
   :adi:`EVAL-AD7124-4ASDZ <EVAL-AD7124-8>` /
   :adi:`EVAL-AD7124-8ASDZ <EVAL-AD7124-8>`.

#. Connect the :adi:`SDP-B` to the PC using a USB cable.

#. Verify the board is recognized: open **Device Manager** on the PC and check
   that the :adi:`SDP-B` appears under **ADI Development Tools**.

Launching the software
-------------------------------------------------------------------------------

#. From the Start menu, navigate to **Programs > Analog Devices > AD7124
   Eval+ > AD7124 Eval+**.
#. Select your evaluation board from the interface selection dialog:

   - **EVAL-AD7124-4SDZ** or **EVAL-AD7124-8SDZ** for the SDZ boards
   - **EVAL-AD7124-4ASDZ** or **EVAL-AD7124-8ASDZ** for the ASDZ boards

#. If the evaluation system is not detected, a connectivity error appears.
   Connect the board, wait a few seconds, and click **Rescan**. Press the
   **RESET** button on the SDP-B board if needed.

Using the Eval+ Software
-------------------------------------------------------------------------------

The main window contains four tabs:

Configuration tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Shows a functional block diagram of the AD7124. Clicking a configuration button
on the diagram opens a pop-up window to configure that functional block.

Key features:

- **ADC RESET** -- performs a software reset of the AD7124 (no hardware reset
  pin; remove power for a hard reset)
- **External Reference** -- set the Refin1(+/-) field to match the reference
  voltage being used (default: 2.5 V from the on-board ADR4525)
- **CONFIG SUMMARY** -- displays channel configuration, setup information, and
  any errors present
- **DEMO MODES** -- pre-configured modes for Thermocouple, 3-Wire RTD, 4-Wire
  RTD, and Noise Test. Each includes a help file.
- **TUTORIAL** -- opens a tutorial on using the software

Waveform tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Graphs the ADC conversions and performs noise analysis:

- **Waveform graph** showing each successive ADC sample
- **Noise analysis** displaying: number of samples, mean, max, min, peak-to-
  peak noise, RMS noise, peak-to-peak resolution, and RMS resolution
- **Channel selection** to choose which channels to display
- **Display units** toggle between volts and codes
- **Batch control** for single run or continuous capture

Histogram tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generates a histogram of gathered samples with the same noise analysis
metrics as the Waveform tab.

Register Map tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Direct access to all AD7124 registers. Individual bit fields can be modified
through drop-down menus. Register configurations can be saved and loaded.

Noise test demonstration
-------------------------------------------------------------------------------

#. On the **Configuration** tab, click the **NOISE TEST** demo button.
#. The device is configured with: output data rate = 9.38 SPS, sinc4 digital
   filter, full power mode, external reference REFIN1(+/-).
#. Switch to the **Waveform** tab, set the desired number of samples, and
   click **SAMPLE**.
#. View the noise analysis results below the waveform graph.

To save conversion data, use **File** at the top of the window. To export as
Excel, right-click the waveform graph and select **Export Data**.
