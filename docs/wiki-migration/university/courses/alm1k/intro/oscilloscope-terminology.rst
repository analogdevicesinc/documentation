Oscilloscope Terminology
========================

**Volts/div:**

Sets how many volts the signal at the input must increase or decrease for the trace to move one division.

**Time/div:**

Sets the time the trace needs to scan from the left hand side to the right hand side of a division.

**Division:**

The visible grid of lines on the oscilloscope screen, shown as number 3 below. It is used in estimating signal amplitude and period. Also called Graticule,

**Trace:**

The ‘line’ that is drawn on the screen (grid), which represents the signal at the input, shown as number 6 below.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-terminology-f1.png
   :align: center
   :width: 600px

\*\* Example Grid with Trace*\*

**Period (T):**

Duration of one cycle of an AC waveform, shown as number 4 above. Equal to 1/f.

**Frequency (f):**

The number cycles of the AC waveform per second. Equal to 1/T (4).

**Amplitude:**

| How far does the signal swings in a direction. Expressed in mV or V. For repetitive signals: Vpeak, shown as number 7 above.
| The magnitude of a quantity or strength of a signal. In electronics, amplitude usually refers to either voltage, current or power.

**Peak-to-peak:**

Difference between most positive and most negative swing of the signal. Two times Vpeak for sinusoidal signals, shown as number 8 above.

**Phase:**

The amount of time that passes from the beginning of a cycle to the beginning of the next cycle, measured in degrees.

**Phase Shift:**

The difference in time between two otherwise similar signals.

**AC coupling:**

Mode where the oscilloscope will only display the AC component of a signal, any DC level or offset is ignored.

**Analog Oscilloscope:**

An instrument that creates a waveform display by applying the input signal (conditioned and amplified) to the vertical axis of an electron beam moving across a cathode-ray tube (CRT) screen horizontally from left to right. A chemical phosphor coated on the CRT create a glowing trace wherever the beam hits. Analog signals are continuously variable. See also ‘Digital’.

**Analog-to-Digital Converter (ADC):**

A mixed signal electronic component that converts an electrical signal into discrete binary values.

**Attenuation:**

A decrease in signal amplitude during its transmission from one point to another.

**Averaging:**

A signal processing technique used in digital oscilloscopes to reduce noise in a displayed signal.

**‘Auto-setup’ mode:**

The oscilloscope automatically selects a setting for Volts/div and Time/div in such a way that one or more periods of the signal are displayed correctly.

**Clipping:**

When the ‘top’ or ‘bottom’ or both extremes of a signal are cut-off (‘clipped’), e.g. because the signal cannot swing any further due to power supply limitations. An undesired property of amplifiers that are driven beyond their specs.

**DC coupling:**

Mode where the oscilloscope displays both the AC and the DC component of a signal.

**Digital:**

| Digital (sampling) scopes perform an analog to digital conversion on the incoming signal and handle all the calculations and plotting in the digital domain.
| Digital signals feature only two fixed levels, usually 0V and +5V. See also ‘Analog’.

**Distortion:**

Undesired alteration of a signal due to external causes such as overloaded circuits, badly designed circuits, etc…

**Duty cycle**

Duty cycle is the fraction of one period in which a signal or system is active. Duty cycle is commonly expressed as a percentage or a ratio. A period is the time it takes for a signal to complete an on-and-off cycle.

**Noise:**

Undesired random addition to a signal.

**Ripple:**

Unwanted periodic variation of a DC voltage.

**Signal:**

Voltage applied to the input of the oscilloscope. The subject of your measurement.

**Sine wave:**

Mathematical function that represents a single oscillation frequency. The waveform shown at the start of this glossary is a sine wave.

**Pulse wave:**

A common waveform shape that has a fast rising edge, a width, and a fast falling edge.

**Pulse Width:**

The amount of time the pulse takes to go from low to high and back to low again, conventionally measured at 50% of full voltage.

**Rise Time:**

The time taken for the leading edge of a pulse to rise from its low to its high values, typically measured from the 10% to 90% levels.

**Spikes:**

Fast, short duration transients in a signal. Also sometimes referred to as a Glitch - An intermittent, high-speed error in a circuit.

**AC voltage: (AC: Alternating Current)**

With AC, the flow of the current periodically reverses, as opposed to DC, where the current flows in one direction. An AC source does not have a polarity.

**Bandwidth:**

Usually expressed in Hertz (Hz, kHz, MHz etc.). It is the frequency at which an applied sine wave will be displayed at an amplitude of around 70% (1 over the square root of 2) of its original amplitude. This amplitude expressed in dB is -3 dB. More expensive scopes feature higher bandwidths. Rule of thumb: the bandwidth of an oscilloscope needs to be at least 5 times higher than the frequency of the signal applied to the input of the scope. The ADALM1000 bandwidth goes up to 100KHz. The ADALM2000 bandwidth goes up to 30 MHz, depending on the time scale setting.

**Circuit Loading:**

The interaction of the oscilloscope input circuitry with the circuit being tested, distorting the signal. This is mostly due to the capacitance of the input but the input resistance can also be a factor in some cases. Loading – The unintentional interaction of the oscilloscope channel input impedance (resistance and capacitance) with the circuit being tested which distorts a signal.

**Input Compensation:**

An adjustment for passive attenuation scope frontends that balances the capacitance of the attenuator with the capacitance of the input circuitry. The ADALM2000 hardware includes trimmer capacitors internal on the circuit board. The ALICE desktop software for the ADALM1000 does this frequency compensation using digital filters.

**DC reference:**

A DC measurement is always performed with respect to a ground or common level, so we need to define this level. If you do not set the DC reference, the readout might not be correct. In most cases, this ground level will be the center of the screen, however this is not mandatory.

\**DC voltage: (DC:Direct Current) \*\*

With DC, the current flows in a single direction, it does not reverse. A DC source has a polarity, (+) and (-).

**Input coupling:**

The drawing shows typical oscilloscope input circuit. There are 3 possible settings: AC-coupling, DC coupling and GND.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-terminology-f2.png
   :align: center
   :width: 400px

With AC-coupling, a capacitor is put in series with the input signal. This capacitor blocks any DC component of the signal and passes only AC.

With DC coupling, the capacitor is bypassed and both the AC and DC component of the signal are passed. Low frequency signals (<20Hz) should always be displayed using DC coupling. Should AC coupling be used, the high pass nature of the coupling capacitor will interfere with the signal and the displayed signal will not be correct.

**Cursor:**

One or more on–screen markers that you can align with a waveform to make more accurate measurements.

**Digital Oscilloscope:**

A type of oscilloscope that uses an analog–to–digital converter (ADC) to convert the measured voltage into digital information. Three types: digital storage, digital phosphor, and digital sampling oscilloscopes.

**Digital Phosphor Oscilloscope (DPO):**

A type of digital oscilloscope that models the display characteristics of an analog oscilloscope while providing digital oscilloscope benefits such as waveform storage. The DPO oscilloscope provides intensity-graded viewing of signal characteristics in real time, and displays signals in three dimensions: amplitude, time and the distribution of amplitude over time.

**Digital Sampling Oscilloscope:**

A type of digital oscilloscope that employs equivalent-time sampling method to capture and display samples of a signal, ideal for accurately capturing signals whose frequency components are much higher than the oscilloscope’s sample rate.

**Digital Storage Oscilloscope (DSO):**

A digital oscilloscope that acquires signals with digital sampling using an analog-to-digital converter (ADC). It uses a serial-processing architecture to control acquisition, user interface, and the raster display.

**Mixed-Signal Oscilloscope (MSO):**

Digital oscilloscopes that have a larger number of channels for viewing both analog and digital signals together. MSO scopes typically have two to four analog channels and at least 8 bits of vertical resolution. There are usually 16 digital channels but they typically have only 1 bit of vertical resolution. For example the ADALM2000 module.

**Effective Bits:**

A measure of a digital oscilloscope's ability to accurately reconstruct a sine wave signal’s shape. This measurement compares the oscilloscope's actual error to that of a theoretical “ideal” digitizer.

**Envelope:**

The outline of a signal’s highest and lowest points acquired over many displayed waveform repetitions.

**Interpolation:**

A “connect–the–dots” plotting technique to estimate what a fast waveform looks like based on only a few sampled points. Two types: linear and splines.

**Sampling:**

The conversion of a portion of an input signal into a number of discrete electrical values for the purpose of storage, processing and/or display by an oscilloscope. Two types: real-time sampling and equivalent time sampling

**Sample rate:**

Usually expressed in samples or kilo-samples/second (KSPS), sometimes in mega-samples/sec (MSPS). It is the number of times per second the digital oscilloscope converts the analog signal at the input to a digital number. The more often it converts, the better it is able to recreate a faithful image of the waveform on the screen. Theoretically the sample rate needs to be twice the maximum frequency of the applied signal, however, for best results a sample rate of 10 times the maximum frequency is recommended. The ADALM1000 max sample rate can be either 100 KSPS or 200 KSPS. The ADALM2000 max sample rate can be up to 100 MSPS depending on the time scale setting.

**Record or Sample Buffer Length:**

The number of waveform points used to create a record of a signal waveform.

**Equivalent-time Sampling**

A sampling mode in which the oscilloscope constructs a picture of a repetitive signal by capturing a little bit of information from each repetition or cycle. There are two types of equivalent-time sampling: random and sequential.

**Real-time Sampling:**

A sampling mode in which the oscilloscope collects as many samples as possible from one triggered acquisition. Ideal for signals whose frequency range is less than half the oscilloscope’s maximum sample rate.

**Sensitivity:**

Indicates the smallest change of the input signal that makes the trace move up or down on the screen. Usually expressed in mV. The ADALM1000 16 bit ADC can resolve inputs down to 100uV. The ADALM2000 12 bit ADC can resolve inputs down to 1.5mV.

**Single Shot:**

A signal measured by an oscilloscope that only occurs once (also called a transient event).

**Single Sweep:**

A trigger mode to display one triggered screen of a signal and then stop.

**Sweep:**

One horizontal pass of an oscilloscope’s electron beam from left to right across the CRT screen.

**Sweep Speed:**

Same as the time base.

**Time Base:**

Oscilloscope circuitry that controls the timing of the sweep. The time base is set by the seconds/division control.

**Trace:**

The shapes drawn on an analog oscilloscope cathode-ray tube (CRT) by the movement of the electron beam.

**Transient:**

A signal measured by an oscilloscope that only occurs once (also called a single–shot event).

**Trigger Level:**

The voltage level that a trigger source signal must reach before the trigger circuit initiates a sweep.

**Trigger Mode:**

A mode that determines whether or not the oscilloscope draws a waveform if it does not detect a trigger. Common trigger modes include normal and auto.

**Trigger Slope or Edge:**

It determines where in the input signal the scope will trigger. This can be on the rising or on the falling slope or edge of the signal.

**Vrms:**

The true rms voltage of signal waveform represents the equivalent DC voltage that would generate the same amount of heat (energy) in a resistor as the signal would. For sinusoidal signals with a DC average of zero, Vrms = Vpeak / sqrt(2)/

**Wave:**

A signal that repeats regularly over time. Common types include: sine, square, rectangular, saw-tooth, triangle, step, pulse, periodic, non-periodic, synchronous, asynchronous.

**Waveform:**

A graphic representation of a voltage varying over time.

**Waveform Capture Rate:**

How quickly an oscilloscope acquires waveforms, expressed as waveforms per second (wfms/s).

**Waveform Point:**

A digital value that represents the voltage of a signal at a specific point in time. Waveform points are calculated from sample points and stored in memory.

**Writing Speed:**

The ability of an analog oscilloscope to provide a visible trace of the movement of a signal from one point to another. This ability is restrictive for low-repetition signals that have fast-moving details, such as digital logic signals.
