Activity: Delta - Sigma Modulator
=================================

Objective:
----------

The objective of this exercise is to explore the concepts of Delta-Sigma modulation through a simple continuous time first order modulator.

Background:
-----------

The delta sigma modulator is the central part of delta sigma analog to digital converters which are also often referred to as over-sampling converters. In its simplest form, which features a single bit quantizer, it produces a bit stream. The digital average of this bit stream represents the input signal level. A simple continuous time first order delta sigma modulator block diagram is shown here:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a17_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 Delta-Sigma modulator block diagram


The difference between the analog input and the analog feedback DAC ( delta ) is integrated by the integrator ( sigma ). The output of the integrator is quantized by comparing it to a threshold. The results of the comparison is sampled by the clocked latch and the digital output of the latch becomes the data output stream. A more in-depth explanation can be found in this mini-tutorial:

:adi:`ADC Architectures III: Sigma-Delta ADC Basics <static/imported-files/tutorials/MT-022.pdf>`

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - AD8541 CMOS rail-to-rail Op-Amp
| 1 - 74HC74 Dual D-type flip flop
| 2 - 10 KΩ Resistors
| 2 - 20 KΩ Resistors
| 1 - 2.2 KΩ Resistor
| 1 - 0.1 uF capacitor
| 1 - 0.02 uF capacitor
| 1 - 10 uF capacitor

Directions:
-----------

The breadboard connections are as shown in figure 2. The scope inputs should be connected to measure the digital and analog output waveforms at D out (1+) and A out (2+). The circuit will operate from the positive Vp supply provided from the ADALM2000 board but better performance will be observed if a +5V bench power supply is used. The digital pulse source output drives the clock input of the flip flop at pin 3. The waveform generator output is connected to resistor R\ :sub:`4` to provide the analog input test signals. Resistors R\ :sub:`1` and R\ :sub:`2` serve to split the supply voltage in half which provides a common mode bias point at the positive input of the opamp. Ground and Vp can now be considered as -Vref and +Vref respectively.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a17_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 First Order Delta Modulator


Referring back to the block diagram, the AD8541 op-amp along with capacitor C\ :sub:`1` are the integrator function. The difference function takes place at the summing junction which is the negative input of the op-amp. The analog input voltage is converted into a current by resistor R\ :sub:`4`. The 1 bit digital to analog function (DAC) is performed by the Q output of the flip-flop and resistor R\ :sub:`3`. The flip-flop output can have two values, 0 Volts ( -Vref ) and +5 Volts ( +Vref ).

Feedback resistor R\ :sub:`3` converts these two voltage levels into current which is also summed at the op-amp summing junction. The difference in the current in R\ :sub:`3` and R\ :sub:`4` is integrated on capacitor C\ :sub:`1`.

The D input of the CMOS flip-flop will have a threshold voltage of approximately one half the power supply voltage and thus can serve as the comparator function. The digital bit steam can be observed at the Qbar output of the flip-flop. The single pole RC low pass filter R\ :sub:`5` C\ :sub:`2` will serve as an analog reconstruction filter.

Hardware Setup:
---------------

The digital pulse source from AWG2 should be configured for a frequency of 100 KHz with a 50% duty cycle. The amplitude should be set to 5 V peak-to-peak with a 2.5 V offset which will produce a 0 to 5 V swing. Waveform generator AWG1 should be set as a sine wave and to a frequency of 1 KHz with an offset of 0.7 volts and a 0 V amplitude for the first measurement.

Procedure:
----------

With the above settings save the observed oscilloscope waveforms for both the digital (Dout) and filtered analog output (Aout) as plot number 1 in your lab report. The digital output waveform should be low most of the time with narrow pulses. The reconstructed analog output after the RC low pass filter should have a DC average value approximately the same as the value that the DC offset of the waveform generator is set to. Now set the offset of waveform generator to 2.7 volts. Again save the observed oscilloscope waveforms as plot number 2 in your lab report. The digital output should be high much more of the time and the average value of the analog output should be close to 2.7 volts.

Now set the offset of the waveform generator to 1.75V and the amplitude to 1.6V peak-to-peak. Now save the waveforms as plot number 3 in your lab report. Open the spectrum analyzer window. The frequency spectrum of the digital waveform and analog waveforms can now be measured and saved as plot number 4 in your lab report.

Questions:
----------

| What is the effect of changing the DC value of the analog input?
| What is the effect of changing the frequency of analog input?
| What is the maximum analog input frequency?
| Looking at the spectrum of the digital output, why does the noise level increase with frequency?
| What is the effect of changing the value of integrator capacitor C\ :sub:`1`?
| Does the spectrum change? Is there a minimum value for C\ :sub:`1`? Is there a maximum value for C\ :sub:`1`?
| What is the effect of changing the frequency of the digital pulse?
| How is the spectrum of the digital output changed? Is there a minimum? or a maximum?
| The simple single pole RC low pass filter R\ :sub:`5` C\ :sub:`2` removes some of high frequency the noise in the analog output spectrum. What would be the effect of a higher order ( active ) filter on the analog output spectrum?

**For Further Reading:**

| :adi:`ADC Architectures IV: Sigma-Del ta ADC Advanced Concepts and Applications <static/imported-files/tutorials/MT-023.pdf>`
| `Delta Sigma Toolbox <https://www.mathworks.com/matlabcentral/fileexchange/19-delta-sigma-toolbox>`_
| http://en.wikipedia.org/wiki/Delta-sigma_modulation

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**
