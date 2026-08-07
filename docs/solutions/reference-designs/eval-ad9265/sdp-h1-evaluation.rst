.. _eval_ad9265 sdp-h1-evaluation:

Evaluating the AD9265 Analog-to-Digital Converter
===============================================================================

.. warning::

   Support for the AD9265-FMC with the SDP-H1 board was discontinued starting
   with the 2022_R2 Kuiper Linux release and will not be supported in future
   releases. The last release with pre-built files is 2021_R2. See all
   :external+kuiper:doc:`Kuiper releases <index>`.

This page describes how to evaluate the :adi:`AD9265-FMC-125EBZ <AD9265>`
using the :adi:`EVAL-SDP-CH1Z` (SDP-H1) High Speed Controller Board, together
with the VisualAnalog® and SPI Controller software. The evaluation board
provides all of the support circuitry required to operate the
:adi:`AD9265` in its various modes and configurations.

For additional information, consult the :adi:`AD9265` data sheet and the
:adi:`UG-074 User Guide <media/en/technical-documentation/user-guides/UG-074.pdf>`.

Typical Measurement Setup
-------------------------------------------------------------------------------

.. figure:: images/ad9265_fmc_125ebz_typical_setup.jpg
   :width: 600

   Figure 1. Evaluation Board Connection — AD9265-FMC-125EBZ (on Left) and
   EVAL-SDP-CH1Z SDP-H1 (on Right)

Features
-------------------------------------------------------------------------------

- Full featured evaluation board for the :adi:`AD9265`
- SPI interface for setup and control
- External, on-board oscillator, and :adi:`AD9517 <ad9517>` clocking options
- Balun/transformer or amplifier input drive option
- LDO regulator or switching power supply options
- VisualAnalog® and SPI Controller software interfaces

Helpful Documents
-------------------------------------------------------------------------------

- :adi:`AD9265` data sheet
- :adi:`EVAL-SDP-CH1Z`, SDP-H1 High Speed Controller Board for System
  Development Platform
- :adi:`AN-905 Application Note <an-905>`, *VisualAnalog Converter Evaluation
  Tool Version 1.0 User Manual*
- :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control
  Software*
- :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs
  via SPI*
- :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and
  Evaluation*
- :adi:`UG-074 User Guide <media/en/technical-documentation/user-guides/UG-074.pdf>`,
  *User Guide for FIFO5 AD9265 Evaluation Board*

Software Needed
-------------------------------------------------------------------------------

- :adi:`SPI Controller <en/design-center/interactive-design-tools/spicontroller.html>`
- :adi:`VisualAnalog <en/design-center/interactive-design-tools/visualanalog.html>`

Equipment Needed
-------------------------------------------------------------------------------

- Analog signal source (preferably SMA 100A Signal Generator)
- Antialiasing filter
- Sample clock source (if not using the on-board oscillator)
- 12 V power supply
- 1-meter SMA cable
- PC running Windows®
- USB-Mini-B cable
- :adi:`AD9265-FMC-125EBZ <AD9265>` board
- :adi:`EVAL-SDP-CH1Z` System Development Platform Kit

Getting Started
-------------------------------------------------------------------------------

Configuring the Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before using the software for testing, configure the evaluation board as
follows:

#. Connect the evaluation board to the data capture board, as shown in
   Figure 1.
#. Connect one 12 V switching power supply to the :adi:`EVAL-SDP-CH1Z`
   SDP-H1 board.
#. Connect the :adi:`EVAL-SDP-CH1Z` SDP-H1 board to the PC with a USB cable
   (connect to J1).
#. When using the on-board clock, connect Pin 1 and Pin 3 of P2.
#. On the ADC evaluation board, use a clean, low-phase-noise signal generator
   to provide an input signal to the input channel (J100). Use a 1 m,
   shielded, RG-58, 50 Ω coaxial cable. For best results, use a narrow-band
   band-pass filter with 50 Ω terminations and an appropriate center
   frequency.
#. If using an external clock signal, remove the connector from P2 and connect
   a clean signal generator to J201.

Using the Software for Testing
-------------------------------------------------------------------------------

Setting Up the ADC Data Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After configuring the board, set up the ADC data capture using the following
steps:

#. Start VisualAnalog.

   .. figure:: images/ad9265_va_start_button.png
      :width: 100

      Figure 2. VisualAnalog Start Button

#. Select AD9265 and double-click **FFT**.

   .. figure:: images/ad9265_va_new_canvas.png
      :width: 600

      Figure 3. VisualAnalog New Canvas Window

#. Click **Settings** under the **ADC Data Capture** section.

   .. figure:: images/ad9265_va_adc_data_capture_2.png
      :width: 300

      Figure 4. VisualAnalog ADC Data Capture Section

#. Set the device to AD9265.
#. Navigate to **Capture Board** and browse to the FPGA image file
   ``ad9265_sdph1.bin``.
#. Click **Program** and verify that LED0 on the SDP-H1 illuminates. Then
   click **OK**.

   .. figure:: images/ad9265_va_adc_data_capture_setting_fpga.png
      :width: 600

      Figure 5. VisualAnalog ADC Data Capture Settings

Evaluation and Test
-------------------------------------------------------------------------------

Setting Up the SPI Controller Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Start SPI Controller.

   .. figure:: images/ad9265_spicontroller_start_button.png
      :width: 100

      Figure 6. SPIController Start Button

#. If a "Read Test Failure" message appears, click **Ignore**.

   .. figure:: images/ad9265_spicontroller_msg_ignore.png
      :width: 400

      Figure 7. First Ignore Test Failure

#. Click **File > Cfg Open**, find the file ``ad9265_16bit_125MSspiR03.cfg``,
   and double-click it.

   .. figure:: images/ad9265_spicontroller_cfg_open.png
      :width: 400

      Figure 8. Configuration Settings

#. If a "Read Test Failure" message appears again, click **Ignore**.

   .. figure:: images/ad9265_spicontroller_msg_ignore.png
      :width: 400

      Figure 9. Second Ignore Test Failure

#. Click **Config > Controller Dialog**.

   .. figure:: images/ad9265_spicontroller_controller_dialog.png
      :width: 400

      Figure 10. Controller Dialog Guide

#. Clear the **SDO Active** checkbox and click **OK**.

   .. figure:: images/ad9265_spicontroller_unselect_sdo_2.png
      :width: 400

      Figure 11. Controller Dialog Setting

#. Click **Read Chip ID** and **Read Chip Grade**.

   .. figure:: images/ad9265_spicontroller_read_chip_id_grade.png
      :width: 300

      Figure 12. Read Chip ID and Read Chip Grade Section

#. Return to VisualAnalog and click the **Play** button.

Adjusting the Amplitude of the Input Signal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Adjust the amplitude of the input signal so that the fundamental is at
   −1.0 dBFS. Verify the **Fund Power** reading in the left panel of the
   **VisualAnalog Graph - AD9265 Average FFT** window.

   .. figure:: images/ad9265_typical_window_2.png
      :width: 500

      Figure 13. Graph Window of VisualAnalog

#. Click the disk icon in the **Graph** window to save the performance plot
   data as a ``.csv`` file.

   .. figure:: images/ad9265_va_disk_icon.png
      :width: 500

      Figure 14. VisualAnalog Disk Icon

When testing additional AD9265 boards, power down the :adi:`EVAL-SDP-CH1Z`
SDP-H1 board first before swapping evaluation boards.

Troubleshooting
-------------------------------------------------------------------------------

**FFT plot appears abnormal:**

- If the noise floor looks normal when the signal generator is disconnected,
  the ADC may be overdriven — reduce the input level.
- In VisualAnalog, click **Settings** in the **Input Formatter** block and
  verify that **Number Format** is set to the correct encoding (offset binary
  by default).

**FFT appears normal but performance is poor:**

- Ensure an appropriate band-pass filter is used on the analog input.
- Use low-phase-noise signal generators for both the clock and the analog
  input.
- If non-coherent sampling is used, change the analog input frequency
  slightly, or switch to coherent frequencies.
- Verify that the SPI configuration file matches the product being evaluated.
- Check for mechanical stress or torque on the clock and analog input
  connectors.

**FFT window remains blank after Run is clicked:**

- Confirm the evaluation board is securely connected to the
  :adi:`EVAL-SDP-CH1Z` SDP-H1 board.
- Verify the FPGA has been programmed by checking that the **FPGA_DONE** LED
  is illuminated on the SDP-H1. If not, reprogram via VisualAnalog. If the
  LED still does not illuminate, disconnect USB and power for 15 seconds,
  reconnect, and repeat the SDP-H1 setup process.
- Confirm the correct FPGA ``.bin`` file was used.
- In the **ADC Data Capture** block in VisualAnalog, click **Settings** and
  verify that **Clock Frequency** is set correctly.
- Ensure the ADC has a valid clock input.
