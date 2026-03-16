.. _ad9213 evb quickstart ads8-v1ebz_ad9213_ad9217:

Quick Start Guide for Testing the AD9213/9217 ADC Evaluation Board (AD9213-10GEBZ, AD9213-6GEBZ, AD9217-10GEBZ, AD9217-6GEBZ) Using the ADS8-V1EBZ FPGA-Based Capture Board
===================================================================================================================================================================================

For AD9213-10GEBZ-B refer to
:doc:`AD9213-10GEBZ-B QuickStart Guide <ads8-v1ebz_ad9213-10gebz-b>`

Typical Setup
~~~~~~~~~~~~~

.. figure:: ../images/ad9213_ads8v1_setup.jpeg
   :alt: Typical hardware setup with AD9213/9217 evaluation board and ADS8-V1EBZ
   :width: 1200

   AD9213/9217 Evaluation Board and ADS8-V1EBZ Data Capture Board

Equipment Needed
~~~~~~~~~~~~~~~~

-  Signal Generators

   -  Analog signal source: The frequency and power requirements depend
      on the tests to be performed. A bandpass filter is typically used
      for single tone tests.
   -  Analog clock source: The clock signal generator should have very
      low phase-noise and be capable of supplying a 10Ghz clock signal
      (or 6 GHz clock signal for the the 6Gsps speed grade of AD9213)
      at approximately 10dBm.
   -  Reference clock source: For AD9213-10GEBZ with 16 output lanes (at
      10Gsps), the frequency of REFCLK is 625MHz. For AD9213-6EBZ configured for
      8 output lanes (at 6Gsps), the frequency of REFCLK is 750MHz. For AD9213,
      the frequency of REFCLK is the digital output lane rate divided by 20. For
      AD9217, the frequency of REFCLK is the sample rate divided by 16, which is
      the same as digital output data rate divided by 16.

-  PC running Windows®
-  USB port and cable to connect to a PC
-  AD9213/9217 Evaluation Board
-  AD9213/9217 Regulator Board (supplies power to the ADC Board)
-  ADS8-V1EBZ FPGA Based Data Capture Board with a power supply

Helpful Documents
~~~~~~~~~~~~~~~~~

-  :adi:`AD9213` Data Sheet
-  ACE Manual: http://swdownloads.analog.com/ACE/ACE_User_Manual_rev3.pdf

Software Needed
~~~~~~~~~~~~~~~

-  Analysis Control Evaluation (ACE) software: available at
   :adi:`/en/resources/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html`

Board Design and Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 60 40
   :header-rows: 1

   * - Description
     - Download
   * - Schematics for ADC board and regulator board
     - :download:`ad9213_evalbrd_regboard_schems.zip <../files/ad9213_evalbrd_regboard_schems.zip>`
   * - Gerber Layout files for ADC board
     - :download:`ad9213_evalbrd_revc_gerbers.zip <../files/ad9213_evalbrd_revc_gerbers.zip>`
   * - Gerber Layout files for regulator board
     - :download:`ad9213_regboard_reva_gerbers.zip <../files/ad9213_regboard_reva_gerbers.zip>`
   * - Bill of materials for ADC board
     - :download:`2020-05-15_ad9213_evalbrd_revc_bom_w_dut.xlsx <../files/2020-05-15_ad9213_evalbrd_revc_bom_w_dut.xlsx>`
   * - Bill of Materials for regulator board
     - :download:`ad9213_regulator_board_bom.xlsx <../files/ad9213_regulator_board_bom.xlsx>`

Testing
~~~~~~~

-  Install the ACE software. The installer is located at
   https://swdownloads.analog.com/ACE/ACEInstall_1.30.3369.1491.exe.
   The Start page appears after you complete the installation and open
   ACE. The Start page displays released plugins. Ensure that the
   AD9213/9217 plugin appears in the pre-installed list of released
   plugins.
-  If the AD9213/9217 plugin does not appear in the pre-installed list,
   it is also available here:
   :adi:`en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9213.html#eb-relatedsoftware`
-  Close ACE.
-  Install jumpers on P3, P8, P9, P10 as shown below.

.. figure:: ../images/ad9213_standoffs_screw_locations.jpeg
   :alt: AD9213 evaluation board showing standoff and screw positions
   :align: center

   Standoff and screw locations

-  You can install standoffs at the locations (marked with an \*) if
   needed. Alternatively, you can use foam sheets to support the board.
-  Connect the AD9213 evaluation board to the regulator board. The
   connectors mate as shown below. With the boards parallel to each
   other, carefully align the connectors.
-  Press the boards together applying even pressure over the connectors to avoid
   stressing and flexing the boards. The connectors are keyed; therefore, you
   cannot insert the board with the incorrect orientation.

.. figure:: ../images/ad9213_connect_eval_board_to_regulator_board.jpeg
   :alt: AD9213 evaluation board mated with the regulator board
   :align: center

   Evaluation board connected to regulator board

-  Connect the AD9213/9217 evaluation/regulator board combo to the
   ADS8-V1EBZ board together as shown in the following figure.
-  Align the FMC+ connectors and apply even pressure across the
   connector and press the FMC connector on to its counterpart on the
   FPGA board.
-  Connect signal, clocks, power, and USB cables to the boards as shown in
   Figure 1.

   -   Signal (J3): The frequency and amplitude of the test signal
       depend on the type of test you are performing. Full scale is
       typically achieved at 9dBm – 12dBm signal power at the signal
       generator (depending on the frequency). If in doubt about which
       amplitude to use, start with a lower amplitude (for example,
       4dBm at the signal generator) and work up or down from there.

      -   Note: In Figure 1 the input signal is shown being applied to RF
          connector J3. The trace from J3 goes to the balun where the
          single-ended signal is converted to differential. On some board
          revisions the trace to the balun comes from RF connector J2. In these
          cases, the input signal must be applied to J2.

.. figure:: ../images/ad9213_input_signal.jpeg
   :alt: Input signal cable connected to RF connector J3 on the evaluation board
   :align: center

   Input signal connection at RF connector J3

-  Sample clock (J13): The sample clock works well across a wide range
   of amplitudes (1dBm – 10dBm at the signal generator). Because jitter
   performance is likely to improve as the slew rate increases, choose
   an amplitude towards the upper end of the stated range.
-  Reference Clock (ADS8-V1EBZ J1): Similar to the sample clock, the
   reference clock works well across a wide range of amplitudes
   (1dBm – 10dBm at the signal generator). Unlike the sample clock, the
   reference clock is not sensitive to jitter/phase noise. Any signal
   generator that meets the frequency and power requirements works. For
   AD9213, the frequency of the reference clock is the (output digital
   data rate)/20. For AD9217, the frequency of the reference clock is
   the (output digital data rate)/16.
-  Example: For the default JESD204B output configuration of
   AD9213-10GEBZ (L = 16, N' = 16, M = 1) at 10Gsps, the output data
   rate is 12.5Gbps. Reference clock frequency =12.5G/20 = 625MHz.
-  Example: For AD9213-6GEBZ, ACE brings the part up in 8-Lane mode.
   In this case (L = 8, N' = 16, M = 1) at 6Gsps, the output data rate
   is 15Gbps. Reference clock frequency = 15G/20 = 750MHz.
-  Connect the USB cable from the ADS8-V1EBZ FPGA board to the Windows
   PC that has ACE installed.
-  Power on the ADS8-V1EBZ FPGA board using the switch S4. Wait several
   seconds after powering on the ADS8-V1EBZ, until DS17 flashes and the
   FPGA fan has stopped spinning.
-  Start ACE from Start->Programs->Analog Devices->ACE.
-  ACE will auto-detect the AD9213 or AD9217 board and bring up the
   correct ACE plugin, which will appear in the upper left portion of
   the GUI. If the plugin does not appear in the upper left, select
   Plug-in Marketplace and select AD9213-10GEBZ, AD9213-6GEBZ or
   AD9217, and add the selected plugin.

.. figure:: ../images/ad9213_ace_screen.jpeg
   :alt: ACE software start page with AD9213/AD9217 plugin listed
   :align: center

   AD9213/AD9217 ACE Plugin Screen

-  Double click on the AD9213 or AD9217 part number in the plugin icon
   in the upper left of the GUI.
-  "Unknown" initially appears in the lower left corner. Wait until "Unknown"
   changes to "Good."

.. figure:: ../images/ad9213_board_view.jpeg
   :alt: ACE board view showing AD9213/9217 with status indicators
   :align: center

   AD9213/AD9217 board view

-  After "State=Good" appears in the lower left, turn on the signal
   generators for the clock, reference clock, and signal.
-  Double-click the AD9213/AD9217 icon to display the chip view.

.. figure:: ../images/ad9213_state_good.jpeg
   :alt: ACE board view showing "State=Good" in the lower left corner
   :align: center

   AD9213/AD9217 Board View with "State=Good"

-  Click the Apply button to configure AD9213 in its default configuration.

.. figure:: ../images/ad9213_apply_default_config.jpeg
   :alt: ACE chip view for AD9213/9217 with default configuration options
   :align: center

   AD9213 Chip View

.. figure:: ../images/ad9213_after_apply.jpeg
   :alt: AD9213/AD9217 chip view in ACE after applying the default configuration
   :align: center

   After Applying the Default Configuration

-  AD9213 DDC and NCO controls are added to the configuration wizard. The
   following image shows a summary of the settings.

.. figure:: ../images/ad9213_config_settings.jpeg
   :alt: AD9213/AD9217 DDC and NCO configuration summary in ACE
   :align: center

   AD9213/AD9217 configuration settings in ACE

-  Click the "Proceed to Analysis" button. The Analysis page appears.
-  Click "Run Once" to get a time domain view at the converted data.

.. figure:: ../images/ad9213_click_run_once.jpeg
   :alt: ACE analysis page after clicking Run Once, showing time domain data
   :align: center

   AD9213/AD9217 analysis page with time domain data

-  Click on the FFT icon to display the frequency domain view (FFT).

.. figure:: ../images/ad9213_click_fft.jpeg
   :alt: ACE analysis page showing the frequency domain FFT view
   :align: center

   Analysis page with FFT

-  Click "Run Continuously" to view repetitive FFTs.

.. figure:: ../images/ad9213_run_continuously.jpeg
   :alt: ACE analysis page showing repetitive FFT running continuously
   :align: center

   FFT running continuously

.. note::

   If the ACE startup procedure does not proceed as described or expected
   (assuming you properly setup the hardware):

   -  Close the ACE software.
   -  Power down the ADS8-V1EBZ using switch S4 (you might need to repeat this
      step several times).

   If after repeated attempts the ACE startup procedure is not successful:

   -  Check that the jumpers are placed on the AD9213/9217 evaluation
      board as shown in step 4.
   -  Check that all signal generators are on and at the correct
      frequencies and power levels.
   -  Check that 3.3V appears at TP5 on the Regulator Board.
