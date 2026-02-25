.. _eval-cn0566-rpiz:

EVAL-CN0566-RPIZ
================

ADALM-PHASER: Phased Array Beamforming Exploration Platform.

Overview
--------

Phased array communications and radar systems are finding increased use in a
variety of applications. This places a greater importance on training engineers
and rapidly prototyping new phased array concepts. However, both those
imperatives have historically been difficult and expensive. That is why Analog
Devices launched the ADALM-PHASER. It is a low cost, simplified phased array
radar which allows real beamforming hardware to be used for education, project
proposals, and even software development.

Most of the labs are run on a Python GUI, with several helper scripts. These can
be run on a remote host computer, or directly on the phaser's Raspberry Pi
computer with the addition of a keyboard, mouse, and display. For more advanced
application development, the Phaser is also supported in the MATLAB RF Microwave
Toolbox.

.. figure:: cn0566_hardware.png
   :align: center

   EVAL-CN0566-RPIZ Hardware

The :adi:`CN0566` is a phased-array beamforming antenna demonstration platform
that allows the user to experience the principles and applications of phased
array antennas. The RF input signal is received from an onboard 8-element patch
antenna that operates from 10 GHz to 10.5 GHz. Each antenna element is input to
an :adi:`ADL8107`, a low noise amplifier (LNA) that operates from 6 GHz to
18 GHz with 1.3 dB NF and 24 dB gain. The output of these amplifiers is fed
into the main core of the design, two :adi:`ADAR1000` 4-channel beamformers.
The :adi:`ADAR1000` operates from 8 GHz to 16 GHz, providing per-channel 360
degree phase adjustment with 2.8 degree resolution, and 31 dB gain adjustment
with 0.5 dB resolution.

The ADAR1000 RFIO output passes through a low pass filter before entering the
:adi:`LTC5548` mixer. The low pass filter removes the high side image of the
mixer as well as any re-radiation of the high side LO. The :adi:`LTC5548`
outputs an IF of approximately 2.2 GHz which passes through a low pass filter
(LPF) to remove mixer spurs and attenuate any RF or LO leakage. The LPF output,
at Rx1 and Rx2, can then be mixed down and sampled by an external 2-channel SDR
receiver, such as the ADALM-Pluto.

Features
~~~~~~~~

- Provides CN0566 software control via Raspberry Pi with Kuiper Linux
- Includes a 10 GHz to 10.5 GHz onboard antenna array design with the option
  to connect an external antenna
- Supports applications running GNURadio, Python, or MATLAB

Equipment Required
------------------

**Hardware**

- EVAL-CN0566-RPIZ Board
- Raspberry Pi 4
- ADALM-Pluto Rev. C
- 5 V, 3 A, USB-C wall adapter
- HB100 microwave source
- Micro HDMI to HDMI adapter
- HDMI cable
- 16 GB or larger SD card
- USB keyboard and mouse
- Monitor with HDMI display
- Tripod

**Software**

- :external+adi-kuiper-gen:doc:`index`

Hardware Overview
-----------------

.. figure:: cn0566_block_assignment.png
   :align: center
   :width: 500

   EVAL-CN0566-RPIZ Block Assignment

Connector assignments:

- **P1** -- 14-pin header for connection to ADALM-Pluto
- **P16** -- USB-C port for power supply
- **RX1** -- SMA connector for RX1 output
- **RX2** -- SMA connector for RX2 output
- **TX_IN** -- SMA connector for TX input
- **TX_OUT_1** -- SMA connector for the first TX output
- **TX_OUT_2** -- SMA connector for the second TX output
- **LO_OUT** -- SMA connector for the LO output
- **EXT_LO** -- SMA connector for external LO input
- **J3 to J10** -- SMP connector footprints for external antenna connections

System Setup
------------

.. figure:: cn0566_test_setup.png
   :align: center

   Test Setup Functional Block Diagram

#. Connect ADALM-Pluto's center micro-USB port to Raspberry Pi via a
   micro-USB to USB cable.
#. Carefully thread the tripod into the tripod mount. Minimize stress on the
   mount while plugging in cables, as it is screwed directly to the PCB.
#. Verify that the SD card is properly inserted into the Raspberry Pi slot.
#. Either connect an HDMI display, USB keyboard, and USB mouse to the
   Raspberry Pi, or for remote login, connect the Raspberry Pi Ethernet
   jack to a wired network or directly to a host computer Ethernet jack.
#. Power up the setup through the USB-C port of the CN0566. Do **not**
   connect a separate supply to the Raspberry Pi.
#. Wait for Raspberry Pi to boot (this may take a minute or two, as the
   filesystem is expanded on first boot).

Software Setup
--------------

SD Card and Image Preparation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order for the Raspberry Pi to control the Phaser devices, write the ADI
Kuiper Linux image to an SD card and configure it. The SD card that ships with
the phaser kit must be updated with a new image.

Download the image from:

- `Kuiper Linux 2021_R2 (April 2, 2023 release)
  <https://swdownloads.analog.com/cse/kuiper/image_2023-04-02-ADI-Kuiper-full.zip>`__

Complete instructions for how to write the image to the SD card and configure an
example system are provided in the
:external+adi-kuiper-gen:doc:`index` guide.

After writing the image, if a window pops up stating the card needs to be
formatted, select **No**. Eject the card and insert it into the Raspberry Pi SD
card slot.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

The easiest way to configure the SD card is by running a setup script. This
requires a wired or wireless internet connection. Once connected to a network,
run the following commands:

.. code-block:: bash

   wget https://github.com/thorenscientific/rpi_setup_stuff/raw/main/phaser/phaser_sdcard_setup.sh
   sudo chmod +x phaser_sdcard_setup.sh
   ./phaser_sdcard_setup.sh
   sudo reboot

After running the script, the hostname will be **phaser.local**.

If running scripts and software directly on the Raspberry Pi, set locale,
keyboard, timezone, and Wi-Fi country using:

.. code-block:: bash

   sudo raspi-config

ADALM-Pluto Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Pluto that ships with the phaser kit has been pre-configured. In case
reconfiguration is needed, the TDD engine and additional control signals are
required for some configurations (added in Pluto firmware 0.38). The latest
firmware is available from the
`PlutoSDR firmware releases
<https://github.com/analogdevicesinc/plutosdr-fw/releases>`__.

To enable the AD9361 second channel, configure the Pluto for 2r2t mode:

.. code-block:: bash

   fw_setenv attr_name compatible
   fw_setenv attr_val ad9361
   fw_setenv compatible ad9361
   fw_setenv mode 2r2t
   reboot

Basic Beamforming Example
-------------------------

Finding the Source Frequency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two distinct ways to use the Phaser setup:

- With a source of unknown frequency, such as an HB100 microwave motion sensor.
  This tends to give the sharpest nulls in the measured pattern.
- With the CN0566 itself providing the signal on one of the TX outputs, fed to
  an antenna. This is required for FMCW RADAR applications.

Most of the scripts only examine a few MHz of bandwidth at a time, while the
HB100 frequency can vary by several tens of MHz. Thus it is essential to know
the frequency of the source. Run the find HB100 script:

.. code-block:: bash

   cd ~/pyadi-iio/examples/phaser
   python phaser_find_hb100.py

Ideally, there should be a single, sharp peak. If there is a single prominent
peak, enter ``y``. If there are several peaks or no visible peak, close the plot
and enter ``n`` at the prompt. Reposition the HB100 and re-run the script.

Running the GUI
~~~~~~~~~~~~~~~

After finding the HB100 frequency, launch the GUI:

.. code-block:: bash

   cd ~/pyadi-iio/examples/phaser
   python phaser_gui.py

The GUI will load and begin displaying the beam pattern.

.. figure:: cn0566_phaser_gui.png
   :align: center
   :width: 600

   Phaser GUI

Calibration
-----------

The phaser board is initially uncalibrated; each element will have a slightly
different gain and slight phase error due to manufacturing tolerances.

**Gain Calibration:** The array is illuminated with the HB100 held far away at
mechanical boresight (zero degrees). One element at a time is set to its maximum
gain. The resulting signal level for each element is measured, and the element
with the minimum gain is chosen as a reference. A correction factor is then
calculated for all other elements.

**Phase Calibration:** Two adjacent elements are set to the maximum calibrated
gain. The phase of one element is swept from 0 to 360 degrees. The phase that
produces the minimum null is 180 degrees away from the matched phase. Each
adjacent pair is measured and an array of phase compensation values is generated.

To run calibration, place the HB100 directly in front of the array at mechanical
boresight, approximately 1.5 m away:

.. code-block:: bash

   cd ~/pyadi-iio/examples/phaser
   python phaser_examples.py cal

The script provides debug information and plots as it runs. Close each plot for
the script to proceed. Plots from an acceptable calibration run will show:

- Gain plots with eight impulses; the lowest should be no lower than about 70%
  of the highest.
- Phase plots with seven arcs centered around zero degrees, with nulls between
  -180 and -135 degrees or between 135 and 180 degrees.

.. figure:: cn0566_gain_phase_cal.png
   :align: center

   Gain and Phase Calibration Plots

After running the script, files ``gain_cal_val.pkl`` and
``phase_cal_val.pkl`` are placed in the working directory. The GUI program
loads these files automatically.

Labs and Lectures
-----------------

The ADALM-PHASER includes a series of short lectures followed by hands-on labs
covering the following topics:

#. **Phaser Hardware Overview and Software Setup**

   Overview of the hardware, software setup, and frequency plan.

#. **Basics of SDR and Beamforming Control**

   Getting acquainted with software control and data capture. Run the minimal
   example script and perform gain/phase calibration.

#. **Phased Array Beam Steering**

   Explore the relationship between the element-to-element phase shift and the
   resulting electrical steering angle using the GUI steering angle slider.

#. **Phased Array Antenna Patterns**

   Directly observe the array factor equation. Measure the Half Power Beam
   Width (HPBW), First Null Beam Width (FNBW), and first sidelobe amplitude.
   Compare with theoretical values for different numbers of active elements.

#. **Sidelobes and Beam Tapering**

   Observe sidelobe amplitudes while reducing the gain of antenna elements at
   the edge of the array. Experiment with different windowing/tapering profiles
   such as Hamming, Hann, and custom tapers.

#. **Grating Lobes**

   Vary the effective element-to-element spacing by disabling selected elements
   to observe grating lobe formation. Compare measured grating lobe positions
   with calculated values.

#. **Beam Squint**

   Observe the change in steering angle as a function of signal frequency. Set
   different signal bandwidths and steering angles to measure beam deviation.

#. **Quantization Sidelobes**

#. **Analog, Digital, and Hybrid Beamforming**

#. **Monopulse Tracking**

#. **Radar: Simple FMCW**

#. **Radar: CFAR, Range Normalization, Clutter Suppression, and
   Range/Velocity**

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0566-RPIZ Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/cn0566-designsupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Assembly Drawing
   - Allegro Project

Additional Resources
--------------------

- `Phased Array Antenna Patterns -- Part 1: Linear Array Beam Characteristics
  and Array Factor
  <https://www.analog.com/en/analog-dialogue/articles/phased-array-antenna-patterns-part1.html>`__
- `Phased Array Antenna Patterns -- Part 2: Grating Lobes and Beam Squint
  <https://www.analog.com/en/analog-dialogue/articles/phased-array-antenna-patterns-part2.html>`__
- `Phased Array Antenna Patterns -- Part 3: Sidelobes and Tapering
  <https://www.analog.com/en/analog-dialogue/articles/phased-array-antenna-patterns-part3.html>`__

More Information and Useful Links
---------------------------------

- :adi:`CN0566 Product Page <CN0566>`
- :adi:`ADAR1000 Product Page <ADAR1000>`
- :adi:`ADF4159 Product Page <ADF4159>`
- :adi:`ADRF5019 Product Page <ADRF5019>`
- :adi:`ADL8107 Product Page <ADL8107>`
- :adi:`LTC5548 Product Page <LTC5548>`
- :adi:`AD7291 Product Page <AD7291>`
- :adi:`ADM7170 Product Page <ADM7170>`
- :adi:`ADM7150 Product Page <ADM7150>`
- `PyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the :ez:`/`.
