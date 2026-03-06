AD5933 LTSpice Model
====================

The :adi:`AD5933` is an impedance analyzer that works from 1 kHz to 100 kHz using a 16MHz system clock. The circuit incorporates the complete signal chain to generate, amplify, acquire and analyze the signals to measure an unknown impedance. A DDS with a single-ended, 10-bit, voltage output DAC, similar to the :adi:`AD9833`, provides the stimulus for the impedance under test. The device incorporates an amplifier with 4 output ranges to provide a suitable driving level for the impedance under test. On the receiving side, a Transimpedance Amplifier (TIA) converts the current across the unknown impedance into voltage. The TIA is followed by a Programmable-Gain Amplifier (PGA) to accommodate the signal to the range of the 12-bit ADC. The signal is windowed with a 1024-sample Hann window and then the DFT is computed using the phase and quadrature signals of the DDS. The result is provided in two 16-bit signed registers containing and real and imaginary part of the admittance.


|AD5933 Block Diagram|

The simulation model is represented with the following symbol. The use of the ports is explained below.


|AD5933 Model Symbol|

Pin Description
---------------

-  **MCLK**: master clock input. The DDS and the DAC run at 1/4 of this frequency and the ADC runs at 1/16 of it. If this pin is left floating, the model lets the simulator choose a suitable time step, which results in faster but less accurate simulation.
-  **RFB**: this pin provides the connection for an external RFB resistor that sets the conversion gain between current and voltage in the internal TIA. The resistor must be connected between VIN and RFB. As a rule of thumb, RFB must be 75% to 150% of the modulus of the impedance under test.
-  **VIN**: this pin provides access to the inverting input of the TIA. It must be connected to the low-side terminal of the impedance. Check the application diagrams to see how to connect this pin in a 4-wire configuration.
-  **AVDD**: analog supply of the AD5933. Connect a DC source from 2.7V to 5.5V.
-  **AGND**: analog ground.
-  **VADC**: this is a fictitious pin that does not exist in the real device. The purpose of this pin is allowing the user to see how the signal looks like at the output of the ADC, so as to avoid under quantization or overflow. The signal is expressed in actual volts, although sampled and quantized.
-  **VOUT**: this pin provides the excitation for the impedance under test. It is advisable to add an AC-coupled voltage follower to re-bias the signal and minimize signal attenuation, as seen in the application example.
-  **MEAS**: this is a fictitious pin that does not exist in the real device. This pin is set high (1V) when the AD5933 is performing the impedance measurement, that is when the number of settling cycles is achieved. The pin remains high until the chip has acquired 1024 samples. The impedance measurement is available when this signal goes low (0V).
-  **RE**: this is a fictitious pin that does not exist in the real device. This pin is intended to provide the value of the Real register (the result of the in-phase accumulator), as this is the only way to return a value from inside a model.
-  **IM**: this is a fictitious pin that does not exist in the real device. This pin is intended to provide the value of the Imaginary register (the result of the quadrature accumulator), as this is the only way to return a value from inside a model.

Model Parameters
----------------

-  **RANGE**: this parameter specifies the output range of the VOUT signal. Valid values are 1 to 4, according to the specifications of datasheet Table 1.
-  **RXG**: this parameter specifies the gain of the PGA. Valid values are 1 or 5 exclusively.
-  **NSET**: this parameter specifies the number of cycles of the excitation signal that the AD5933 waits before starting the measurement. This time is intended for the signal chain and impedance under test to reach steady state. The use of IC parameter is recommended to reduce simulation time, as shown in the application example.
-  **FCODE**: this parameter contains the frequency tuning word of the DDS. The value of this parameter is calculated according to datasheet Equation 1:

<m 11> FCODE = {f_t*2^{29}}/{f_MCLK} </m> where f\ :sub:`t` is the frequency of the tone used for measurement.

-  **fMCLK**: this parameter specifies the frequency of the system clock in Hz. It is required in AC analysis or when the transient simulation is performed without the MCLK signal.

Modeled Features
----------------

-  VOUT AC and DC voltage levels
-  DDS operation and 10-bit quantization of the DAC
-  Bandwidth and impedance of output amplifier
-  Gain, bandwidth and phase of the Rx signal path
-  Signal clipping at ADC input and 12-bit quantization
-  Hann windowing and DFT calculation
-  Timing and resolution of digital processing and registers
-  Counter for settling time cycles
-  Total current consumption of the AD5933

Supported Analysis
------------------

-  **DC Operating point (.DC)**
-  **Transient analysis (.TRAN)**. The model can operate with or without MCLK. If MCLK is provided, the model produces a new sample for every clock cycle. If MCLK is not connected or connected to VDD, the model takes a time step that ensures convergence, which results in a faster execution, but only the analog signals are calculated. This mode is used to simulate the settling time of the impedance under test without running the DSP engine.
-  **AC Analysis (.AC)**. The model supports AC analysis to easily tune the signal chain at the output and the input of the model. This mode is used to evaluate the phase shift introduced by additional filters and amplifiers. The model also estimates the magnitude of the binary value of the real and imaginary registers to facilitate the detection of numerical overflow across the frequency range. Note that the magnitude is unsigned and that clipping is not enforced and must be evaluated based on the simulation values.

Circuit Example
---------------

The example provided with the circuit aims at demonstrating the use of the AD5933 model and explaining how to calculate admittance and impedance from the value of the real and imaginary registers. The contents of these registers do not correspond to the real and imaginary part of the admittance; they represent the amount of energy of signal in phase and in quadrature in relation to the transmitted signal. |image1|


|image2|

.. tip::

   The imaginary register is not zero despite measuring a resistor because the AD5933 has an intrinsic phase shift due to the filters of the signal chain and the ADC conversion delay. This shift must be measured in calibration and discounted from subsequent measurements.


-  **Admittance Y** is calculated as:

<m 11> delim{\|}Y{\|} = GF*sqrt{RE^2+IM^2} </m> <m 11> phi=tan^{-1}(IM/RE) </m> where GF is the gain factor, RE and IM are the decimal values of the real and imaginary registers and φ is the argument of the admittance.

-  **Gain Factor GF**. This is a correction of the admittance magnitude that accounts for gain of the analog and digital signal chain. The theoretical GF value can be calculated as:

<m 11> GF_th = {V_DD/{V_AC*R_FB*RXG*2^14}} </m>

where V\ :sub:`DD` is the analog supply voltage, V\ :sub:`AC` is the peak-to-peak value of the measurement signal, R\ :sub:`FB` is the value of the I/V conversion resistor and RXG is the value of the reception gain. This theoretical value does not include the roll-off of internal filters or the effect of additional elements in the signal chain. It is therefore advisable to use the value obtained from a calibration with a known impedance.

-  **Argument φ**. The AD5933 has an approximately linear variation of phase with frequency, with the following theoretical expression:

:math:`phi_th=0.000653 \times f_t-0.65` where f\ :sub:`t` is the frequency of the measurement signal. This theoretical value does not include the phase shift introduced by additional or parasitic elements in the signal chain. It is therefore advisable to use the value obtained from a calibration with a known impedance.

-  **Impedance Z**. Impedance can be calculated as the inverse of the admittance:

:math:`|Z|=1/|Y|`

-  \*\* Resistance R*\*. Resistance can be calculated from impedance as:

:math:`R=|Z| \times cos(\phi)`

-  **Capacitance C**. Parallel capacitance can be calculated from admittance as:

:math:`C=|Y| \times sin(\phi)`

-  **Inductance L**. Series inductance can be calculated from impedance as:

:math:`L=|Z| \times sin(\phi)`

.. |AD5933 Block Diagram| image:: https://wiki.analog.com/_media/resources/quick-start/ad5933_block_diagram.png
.. |AD5933 Model Symbol| image:: https://wiki.analog.com/_media/resources/quick-start/ad5933_symbol.png
   :width: 400px
.. |image1| image:: https://wiki.analog.com/_media/resources/quick-start/ad5933_application_example.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/quick-start/ad5933_simulation_result.png
   :width: 600px
