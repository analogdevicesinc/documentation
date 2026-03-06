Activity: Semi-Digital FIR Filter
=================================

Objective:
----------

The objective of this Lab activity is to examine the Finite Impulse Filter (FIR) structure where the single-bit digital signal to be filtered is fed into a digital shift register with an analog reconstruction output stage. This digital/analog hybrid arrangement is most often referred to as a semi-digital filter.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

When converting a digital audio signal or other type of band-limited digital signal into analog form, it is desirable to preserve a given frequency band of the signal content, while filtering out unwanted frequencies in other bands (typically higher in frequency than the desired band). For example, the digital to analog conversion process generally includes a low pass filtering stage, which removes out of band noise in the resulting output analog signal.

When the raw unfiltered analog output of a digital to analog converter is fed to an analog circuit such as an amplifier, out of band noise can have a negative interaction with the linear amplification process, and can alias back into the desired frequency band, distorting the output signal. One means of low pass filtering for removing the out of band noise during the digital to analog conversion may be through the use of a semi-digital finite impulse response (FIR) filter. The input to the filter could be pulse width modulated (PWM) or pulse density modulated (PDM). The semi-digital FIR filter uses the digital input value delayed in time to switch voltage mode summation switches on and off to generate an analog output reconstruction of the digital input signal that is inherently low-pass filtered. In a conventional design, the coefficients of the semi-digital FIR filter are computed using classical digital filter design techniques in which the filter is constrained to be a linear phase filter, which results in a symmetrical set of FIR filter coefficients.

The Semi-digital FIR filter principle is shown in figure 1, where the single-bit digital signal to be filtered is fed into a shift register. An analog summing node is coupled to the contents of the shift register though a weighting network. In the simple form we are looking at in this activity, the unit delay (Z\ :sup:`-1`) taps have associated resistances which are the coefficients of the filter (B\ :sub:`0` – B\ :sub:`N`). The analog sum at the output produces a filtered analog version of the digital input signal that was fed to the input of the shift register delay line.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-sdf-fig_1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Semi-digital FIR filter


The D-type latches used in the shift register produce unit delays (Z\ :sup:`-1`) equal to one single clock cycle. Notice that the signal flow is strictly feed-forward, since all paths connecting the input to the output flow in the forward direction.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 - 74HC273 Octal D-type FF register
| 1 – 20 KΩ resistor
| 5 – 6.8 KΩ resistors
| 4 – 10 KΩ resistors
| Filter caps as needed

Directions:
~~~~~~~~~~~

Build the semi-digital FIR low pass filter using a 74HC273 Octal D-type register on your solderless breadboard. An 8 stage shift register is constructed by connecting the Q output of one FF to the D input of the next as shown in figure 2. The digital input signal to be filtered is connected to the first FF D input. A delayed version of the digital input appears at each Q output. The delay is equal to one clock period per stage in the register. So the first Q output is delayed by one clock period and the eighth (or last) Q output is delayed by 8 clock periods.

The analog output representation of the digital input signal is created as a weighted summation of the digital input and all 8 Q outputs. In this first example, using resistor values from the ADALP2000 parts kit, all the coefficients are similar in weight with the first two and last two of equal value (10 KΩ) an the middle 5 slightly higher weight equal to 6.8 KΩ.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-sdf-fig_2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Shift register FIR filter


Clock source:
~~~~~~~~~~~~~

This experiment needs a square wave clock source for the shift register. A variable frequency square wave source can be built using the AD654 voltage-to-frequency converter IC, as shown in figure 3.

.. _materials-1:

Materials:
~~~~~~~~~~

| 1 – 10Ω resistor
| 2 – 220 Ω resistors
| 1 – 1.5 KΩ resistor
| 1 – 4.7 KΩ resistor
| 1 – 5 KΩ potentiometer
| 1 – 2.2 nF capacitor (222)
| 1 – 0.56 uF capacitor (564)
| 1 – 10 uF capacitor
| 1 – AD654 Voltage-to-frequency Converter

.. _directions-1:

Directions:
~~~~~~~~~~~

Alongside the shift register construct the AD645 based digital clock source generator shown in figure 3. Refer to the AD654 datasheet for more details on the operation of the circuit. The output frequency is determined by the values of C\ :sub:`2` and R\ :sub:`5` and the voltage applied to pin 4 (V\ :sub:`REF`). A variable voltage divider consisting of R\ :sub:`1`, R\ :sub:`3` and potentiometer R\ :sub:`2`, across the 2.5 V supply creates V\ :sub:`REF`. The square wave output at pin 1 of the AD654 drives the clock input of the 74HC273 at pin 11.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-delta-sigma-fig_3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Voltage-to-frequency Converter square wave source


Check the output frequency of the clock source with scope cannel B. It should be at least 10 KHz and be able to be adjusted up to 25 KHz or as much as 35 or 40 KHz.

Procedure:
~~~~~~~~~~

The first step is to test the step response of the filter. Set the AWG channel A Min value to 0 and Max vale to 5. Set the Freq to 500 Hz. From the AWG channel A Shape menu select Square. Using scope channel B, observe the response at the output to the rising and falling edge of the input. As you change the clock frequency generated by the AD654 (adjust pot R\ :sub:`2`) you should see the slope of the output change. You should see 9 or 10 distinct levels as the output transitions. To further smooth these intermediate steps a filter capacitor can be connected from the output to ground.

To observe the impulse response of the filter adjust the Freq of channel A to a lower number say 200 Hz and reduce the duty cycle value to produce a narrow pulse. The width of the pulse needs to be at least one clock cycle wide but not more than 2 clock cycles wide.

Generating digital signals to filter:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We would now like to test the response of the filter with more complex digital waveforms. One way to do that is to load the waveform from a .csv file. Download the waveform file containing a pulse width modulated waveform (pwm-sine-5.zip) and extract the .csv file. This file was generated using 128 Master 100 KHz clock pulses for the base pulse width and 128 "samples" of a sine wave. It is 128 \* 128 or 16384 samples long and the sinewave output frequency is about 6 Hz. From the AWG channel A Shape menu select Read CSV to load the waveform into the AWG A waveform buffer. (Be sure that Repeat is checked to produce a continuous output.) To actually see the modulating sine wave you can use the simple RC filter shown in figure 4.

The ALICE software can also generate Pulse Width Modulated sine waves. From the Shape drop-down menu select the PWM sine option. The Min and Max values are used to set the low and high values of the pulse. The Freq entry is used to set the frequency of the modulation sine wave. The number in the duty cycle entry set the number of master clock cycles (100 KHz) used for the pulse width that will be modulated by the sine wave. The more master clock cycles used the higher the resolution, but also the lower the sine wave frequency has to be.

Try generating a few different PWM sinewaves and observe the filter response.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-sdf-fig_4.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 4, Simple first order RC reconstruction filter.


Another option is to build the analog PWM circuit from this Lab, :doc:`Pulse Width Modulation </wiki-migration/university/courses/alm1k/alm-lab-pwm>`. Using the pulse output of this circuit as the input to the digital filter observe the response as you adjust the frequency and amplitude of the sine wave input to the PWM circuit.

Appendix:
~~~~~~~~~

**74HC273 functional block diagram**

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-lfsr-fig_6.png
   :align: center
   :width: 250px

.. container:: centeralign

   74HC273 Pinout


Moving Average Filter (Boxcar filter):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The moving average filter is a simple Low Pass FIR (Finite Impulse Response) filter commonly used for smoothing an array of sampled data/signal values. It takes the last M samples of the input at a time and takes the average of those M-samples and produces a single output point. It is a very simple LPF (Low Pass Filter) structure that comes in handy for scientists and engineers to filter unwanted noisy or higher frequency components from the sampled data.

As the filter length increases (the parameter M) the smoothness of the output increases, whereas the sharp transitions in the data are made increasingly blunt. This implies that this filter has excellent time domain response but a poor frequency response.

| The Moving Average filter performs three important functions:
| 1) It takes M input points, computes the average of those M-points and produces a single output point
| 2) Due to the computation/calculations involved, the filter introduces a definite amount of delay
| 3) The filter acts as a Low Pass Filter (with poor frequency domain response and a good time domain response).

**For Further Reading:**

| :adi:`AD654 datasheet <media/en/technical-documentation/data-sheets/AD654.pdf>`
| `Finite impulse response <https://en.wikipedia.org/wiki/Finite_impulse_response>`__
| `Frequency Response of the Running Average Filter <https://ptolemy.berkeley.edu/eecs20/week12/freqResponseRA.html>`__

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-signals-labs-list>`\ **.**
