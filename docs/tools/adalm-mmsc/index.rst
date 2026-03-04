ADALM-MMSC
==========

Advanced Active Learning Module for Signal Chain Exploration and Design.

A concise version of this document is available in portable document format.
Click on the file below to download:

.. admonition:: Download

   :download:`ADALM-MMSC QuickStart Guide (pdf) <ad-bmse2e3w-sl-ug-2245.pdf>`

Overview
--------

.. figure:: adalm-mmsc_angle.jpg
   :align: left

   ADALM-MMSC

The :adi:`ADALM-MMSC (Analog Devices Active Learning Module - Mixed-Mode Signal Chain)` is an educational board that facilitates hands-on exploration of fundamental signal chain concepts.

The core of the circuit is the AD4080, 40-Msps oversampling SAR analog to digital converter (ADC) with configurable digital filter and internal data capture memory (single-port FIFO).

The board includes a highly configurable 2nd order analog filter with adjustable cutoff frequencies, input attenuation, and filter gain.

An onboard selectable clock source provides sample rates from 5 Msps to 40 Msps. A MAX32666FTHR microcontroller runs an IIO server over a serial backend, allowing the use of standard tools such as Scopy, IIO Oscilloscope, Pyadi-iio, and ADI's MATLAB precision toolbox.

The Libiio library provides language bindings for C, C#, MATLAB, Python, and other languages.

Concepts demonstrated include:

- Digital filtering
- Analog vs. digital anti alias filtering
- Properties of different digital filters
- Noise Analysis
- Reference noise

Features
++++++++

- Multiple input connections
   - 100-mil posts compatible with the ADALM2000
   - SMA connections for benchtop signal generators
   - 1/8-inch phono jack for connection to sound cards and other audio sources
- Selectable input attenuator
   - 3:5 attenuation allows +/-5 V input swing
   - 3:50, 3:500 allows testing with low-amplitude signals for dynamic range measurements
- Configurable Sallen-Key filter with low-noise amplifier
   - Cutoff frequencies between XX kHz and YY kHz
   - Gains of unity, 2, and 5 for exploring noise optimization
- Onboard fully-differential amplifier
   - Allows arbitrary input signals
   - Input and output test connections for monitoring of all critical points
- Onboard low-noise reference
   - Flagship LTC6655 for optimal performance
   - "Reference Corruption" input allows noise and interfering tones to be introduced and their effects observed
- Selectable conversion rates from 5 Msps to 40 Msps allows observation of aliasing, ADC noise density vs. sample rate

Applications
++++++++++++

- Mixed Signal and Digital Signal Processing experiments, workshops, and lab exercises
- Precision data acquisition

System Architecture
+++++++++++++++++++

.. figure:: updated_block_diagram_72vto96v.png

   ADALM-MMSC Simplified Block Diagram

.. csv-table:: Specifications
   :file: specifications.csv
   :widths: 20, 10, 10, 10, 10, 40
   :header-rows: 1

What's Inside the Box?
++++++++++++++++++++++

Upon purchase of the ADALM-MMSC kit, the package comes with the following boards and accessories:

.. figure:: ad-bmse2e3w-sl_package_contents.png

   ADALM-MMSC Kit Contents

Components and Connections
++++++++++++++++++++++++++

.. figure:: revised_ad-bmse2e3w-sl_board_with_pin_labels.png

   Hardware Components and Connections

.. csv-table:: Hardware Part Functions
   :file: components.csv
   :widths: 5, 25, 60
   :header-rows: 1

System Evaluation
+++++++++++++++++

Follow the setup shown in the diagram below to get the board up and running. Ensure that the hardware parts and equipment are complete based on list of Equipment Needed. The banana plug cables used in this setup only have a maximum rating of 10A. Cables suitable for higher current rating must be used if the intended application operates at range higher than 10A. Note that the AD-BMSE2E3W-SL board can only accommodate up to 100A.

.. figure:: system_evaluation_set-up.png

   Evaluation Setup

Equipment Needed
^^^^^^^^^^^^^^^^

- 1x ADALM-MMSC Board (as DUT)
- Windows, Mac, or Linux host computer with available USB port
- Signal generator, :adi:`ADALM2000 <https://analogdevicesinc.github.io/documentation/tools/m2k/index.html>` or similar.
   - Generators in the audio range work great
   - PC sound card with Audacity is another option

.. warning::

   This reference design has not undergone compliant testing for EMI/ EMC standards for automotive. It is up for the user to do its qualification as the requirements vary depending on its end application or use cases.


.. esd-warning::

.. note::

   For high current applications requiring greater than 50 A, it is advisable to install a heat sink to protect the pre-charge, charge, and discharge MOSFETs from overheating.


   - The AD-BMSE2E3W-SL Kit has 7 available HEATSINK PIN-FIN W/TAPE (375424B00034G) easy-to-install, adhesive type, aluminum top mount heat sink than can be installed directly on top of the board.

   - Peel off the protective film from the bottom of each heat sink and firmly press each one on top of the following FETs:

   (1) Attach the 5 heat sinks on the top layer of the board (Q4, Q5, Q6, Q7, and Q9),
   (2) the remaining 2 heat sinks on the bottom layer of the board (Q3 and Q8).

Preparing the MCU
+++++++++++++++++

By JGEALON default (upon purchase), the AD+BMSE2E3W+SL board comes with a MAX32625PICO programmer adapter that is loaded with firmware image.

Otherwise, if you are using a new MAX32625PICO programmer (that is not part of the original kit), make sure to flash it first with the correct firmware image before connecting it to the AD-BMSE2E3W-SL board. If you do not know how to load the image, follow the instructions below:

#. Download the firmware image:
   :downgit-max32625pico-firmware-images:`MAX32625PICO Firmware Image for MAX32690 <master:bin/max32625_max32690evkit_if_crc_swd_v1.0.7.bin>`

#. Do not connect the MAX32625PICO to the AD-BMSE2E3W-SL Board yet.

#. Connect the MAX32625PICO to the Host PC using the micro USB to USB cable.

#. Press the button on the MAX32625PICO. (Do not release the button until the MAINTENANCE drive is mounted)

#. Release the button once the MAINTENANCE drive is mounted.

#. Drag and drop (to the MAINTENANCE drive) the firmware image.

#. After a few seconds, the MAINTENANCE drive will disappear and be replaced by a drive named DAPLINK. This indicates that the process is complete, and the MAX32625PICO can now be used to flash the firmware of the AD-BMSE2E3W-SL Board.

Hardware Setup
++++++++++++++
The board utilizes the DC2472A battery emulator as input for cell voltage measurement. The DC2472A allows a cell voltage of 1.4 V (min) to 4.2 V (max). Follow below steps to set up the board for cell measurement:

#. Screw the two cell connector blocks to the two DC2472A battery emulators. Note that the first two terminals and the last terminal of each DC2472A cell connector must be left hanging (refer to below figure). Make sure to also set the last two terminals' input to low voltage or equivalent range of roughly 1.4V per cell.

   .. figure:: battery_emulator_pins.png

      DC2472A Battery Emulator Pins

#. Connect the DC2472A battery emulators to the ADBMSE2E3W-SL board through the cell connector blocks. Then, connect a micro-USB Type B cable to each DC2472A battery emulator and power the boards by connecting the other end of the cables to the Host PC.

   .. figure:: usb_emulator.png

      Connecting the DC2472A Battery Emulator

#. Set the DC2472A battery emulators to the lowest voltage by fully turning the Cell Voltage Adjustment Potentiometer counterclockwise.

#. Attach the MAX32625PICO programmer to the AD-BMSE2E3W-SL board using the 10-pin ribbon SWD cable. Power the MAX32625PICO using a micro-USB to USB cable connected to the Host PC.

   .. figure:: max32625_power_usb_pc.png

      Connecting the MAX32625PICO Programmer

#. Connect the alligator clip cable (red) to the VBATTP Pin or the 3rd of Pin 17 header of the DC2472A battery emulator. Then, insert the other end of the cable (banana jack plug) to TP16 (VBAT+ terminal) of the AD-BMSE2E3W-SL board.

   .. figure:: connector_supply_vbattp.png

      DC2472A's VBATT+ Supply Connector to AD-BMSE2E3W-SL's VBAT+ Terminal

#. Connect the alligator clip cable (black) to the GND (VBAT-) supply of the DC2472A battery emulator. Then, connect the other end of the cable to the Rsense (top side) of the AD-BMSE2E3W-SL.

   .. figure:: gnd_vbat-_to_gnd_sense.png

      DC2472A's VBAT- Supply Connector to AD-BMSE2E3W-SL's Rsense


#. Set the DC2472A battery emulators to HIGH voltage or equivalent to 4.1 V per cell by turning the Cell Voltage Adjustment Potentiometer clockwise.

#. Check the supply for the following test points as described in the diagram and table below. Make sure that the voltage levels are within the specified range.

   .. figure:: quick_test_points.png

      AD-BMSE2E3W-SL Test Points

   .. csv-table:: Hardware Supply Quick Test Point
     :file: test-points.csv
     :widths: 15, 30, 35, 20
     :header-rows: 1

#. Once all steps are completed, you are now ready to use this reference design and run the accompanying software found in the link below:

   .. note::

      The AD-BMSE2E3W-SL comes complete with firmware examples and easy-to-use application GUI. Access the software resources and see the setup procedure in the AD-BMSE2E3W-SL Software User Guide.

Resources
++++++++++++

- :adi:`ADBMS6830`
- :adi:`ADBMS2950`
- :adi:`ADBMS6822`
- :adi:`MAX32690`
- :adi:`LLT8303`
- :adi:`ADUM225N`
- :adi:`LTC7001`
- :adi:`LTC3639`

Design & Integration Files
++++++++++++++++++++++++++

.. admonition:: Download

   `AD-BMSE2E3W-SL Design Support Package <ad-bmse2e3w-sl-designsupport.zip>`_

   * Schematic
   * PCB Layout
   * Bill of Materials
   * Allegro Project

Guides&Sample Software
----------------------

A software user-guide and sample application for :adi:`AD-BMSE2E3W-SL` are available:

.. toctree::
   :titlesonly:
   :glob:

   */index

Help and Support
----------------

For questions and more information, please visit the :ez:`EngineerZone Support Community </>`.

