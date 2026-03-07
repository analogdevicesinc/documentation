AD9834 LTSpice Model
====================

The :adi:`AD9834` is a low-frequency DDS that can generate sinusoidal, triangular and square waves with a sampling rate up to 75 MHz. The simulation model is represented with the following symbol.


|image1|

The circuit incorporates a 10-bit current-steering DAC with differential output (IOUT and IOUTB) that requires two termination resistors to ground. These outputs produce sinusoidal and triangular waveforms.

The circuit can also produce digital square waveforms on the SBO pin. To generate this signal, the circuit can use the sign bit of the DAC or use an integrated comparator on the filtered sinewave signal connected to VIN. The first method is more convenient at low frequency and the second method is more accurate at high frequency.

The DDS can be used as a modulator if a binary stream is connected to the FSEL or PSEL pins. The first one generates a binary FSK modulation, and the second one generates a binary PSK modulation.

The AD9834 allows adjusting the full-scale current of the DAC, and therefore the amplitude of the signal, by changing the resistor connected to the FSADJ pin.

Pin Description
---------------

-  **MCLK**: master clock input. This is the clock used for the DDS logic and the DAC.
-  **FSEL**: frequency selection pin. A low level selects the frequency value assigned to FREQ0 parameter and a high value selects the frequency value assigned to FREQ1 parameter.
-  **PSEL**: phase selection pin. A low level selects the phase value assigned to PHASE0 parameter and a high value selects the phase value assigned to PHASE1 parameter.
-  **VIN**: comparator input. Connect the filtered sinewave from IOUT or IOUTB to generate a square signal of the same frequency. This input is AC coupled.
-  **AVDD**: analog supply of the DAC and the comparator.
-  **AGND**: analog ground.
-  **FSADJ**: full-scale adjustment pin. Connect an external resistor to ground to set the reference current of the DAC.
-  **IOUT**: non-inverted current output. Connect a termination resistor to ground.
-  **IOUTB**: inverted current output. Connect a termination resistor to ground.
-  **SBO**: digital output pin, used for square waves.

Model Parameters
----------------

-  **TYPE**: type of waveform. 0 for sinewave, 1 for triangular, 2 for DC (test option).
-  **COMP**: function on SBO output. 0 uses the sign bit of the DAC (the MSB), 1 uses the output of the internal comparator.
-  **FREQ0**, **FREQ1**: value of the frequency register. It is a decimal number from 0 to 2\ :sup:`28`-1, where 0 represents DC and 2\ :sup:`28` represents f\ :sub:`MCLK`. Values higher than 2\ :sup:`27` cause frequency aliasing. The value of this parameter is calculated as: *FREQ_reg = f\ 0\ \*2\ 28/fMCLK*, where f\ :sub:`0` is the desired tone frequency.
-  **PHASE0**, **PHASE1**: value of the phase register. It is a decimal number from 0 to 2\ :sup:`12`-1, where 0 represents 0° and 2\ :sup:`12` represents 360°. The value of this parameter is calculated as: *PHASE_reg = φ\*2\ 12/360*, where φ is the desired phase in degrees.
-  **fMCLK**: frequency of the MCLK signal. This parameter is required for autonomous operation when the MCLK pin is floating or grounded.

Modeled Features
----------------

-  DAC full-scale current and output voltage as a function of FS current and load resistor
-  10-bit quantization of DAC
-  28-bit quantization of frequency resolution
-  12-bit quantization of phase resolution
-  Sinusoidal output (AC and Tran with or without MCLK)
-  Triangular output (Tran with or without MCLK)
-  VIH and VIL for FSELECT, PSELECT and MCLK
-  Set-up time for FSELECT and PSELECT
-  Digital latency of FSELECT and PSELECT signals (with and without MCLK)
-  Internal comparator (phase and cutoff frequency)
-  Digital output (rise and fall time with comparator or sign bit sources)
-  Harmonic distortion
-  Thermal noise of DAC current sources
-  AVDD (analog) current consumption

Supported Analysis
------------------

-  DC Operating point (.DC)
-  Transient analysis (.TRAN). The model can operate with or without MCLK. If MCLK is provided, the model produces a new sample for every clock cycle. Digital delays and set-up times are referred to the clock. If MCLK is not connected or grounded, the model takes a time step that ensures convergence, which results in a faster execution but less accurate in spectral content. This mode requires setting the correct value of the fMCLK parameter to calculate frequencies and delays.
-  AC Analysis (.AC). The model supports AC analysis to easily tune the signal chain at the output of the DDS. The amplitude of the signal is nominally full scale.
-  Noise (.noise). The model supports noise analysis to see the thermal noise produced by resistors and reference. The output is set to mid-scale when this analysis is run.

Circuit Example
---------------

The example provided with the circuit aims at demonstrating the main features of the AD9834:

-  Sinewave generation
-  Phase and Frequency modulation
-  Internal Comparator

.. image:: https://wiki.analog.com/_media/resources/quick-start/ad469x-ltspice-user-guide/ad9834_example.png
   :align: center
   :width: 600px

In addition, the example provides the formulas to compute the register values from the phase and frequency values. Shown under the Register Encoding section. The user is expected to edit the values in the User Parameters section. The output of the simulation looks like this:

.. image:: https://wiki.analog.com/_media/resources/quick-start/ad469x-ltspice-user-guide/ad9834_waveforms.png

For long simulations, the MCLK pin can grounded or floated. In this case the simulator adjusts the time step to ensure convergence. Simulation is faster but spectral and timing fidelity is reduced.

.. |image1| image:: https://wiki.analog.com/_media/resources/quick-start/ad469x-ltspice-user-guide/ad9834_symbol.png
   :width: 400px
