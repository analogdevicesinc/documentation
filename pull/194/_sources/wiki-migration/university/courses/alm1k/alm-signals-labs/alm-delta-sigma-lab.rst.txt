Activity: Delta – Sigma Modulator
=================================

Objective:
----------

The objective of this Lab activity is to explore the concepts of Delta-Sigma modulation through a simple continuous time first order modulator.

Background:
-----------

The delta sigma modulator is the central part of delta sigma analog to digital converters which are also often referred to as over-sampling converters. In its simplest form, which features a single bit quantizer, it produces a bit stream. The digital average of this bit stream represents the input signal level. A simple continuous time first order delta sigma modulator block diagram is shown here:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-delta-sigma-fig_1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 Delta-Sigma modulator block diagram


The difference between the analog input and the analog feedback DAC (delta) is integrated by the integrator (sigma). The output of the integrator is quantized by comparing it to a threshold. The result of the comparison is sampled by the clocked latch and the digital output of the latch becomes the data output stream. A more in-depth explanation can be found in this :adi:`mini-tutorial <media/en/training-seminars/tutorials/MT-022.pdf>` and the other links available at the end of this document.

Materials:
~~~~~~~~~~

| ADALM1000 Lab hardware
| Solder-less breadboard
| Jumper wires
| 1 – AD8541 CMOS rail-to-rail Op-Amp (1/2 AD8542 dual) or OP97
| 1 – 74HC273 Octal D-type flip flop (or 74HC74 Dual D-type flip flop)
| 1 – 74HC04 Hex inverter
| 2 – 10KΩ Resistors
| 2 – 20KΩ Resistors
| 1 – 2.2KΩ Resistor
| 1 – 0.1uF capacitor (104)
| 1 – 10 nF capacitor (103)
| 1 – 10uF capacitor

Directions:
~~~~~~~~~~~

The breadboard connections are as shown in figure 2. The circuit is powered from the fixed +5V supply. The digital pulse source output drives the clock input of the flip flop at pin 11. The channel A AWG output is connected to resistor R\ :sub:`1` to provide the analog input test signals. The fixed +2.5 V source provides a common mode bias point at the positive input of the opamp. Ground and +5V can now be considered as –Vref and +Vref respectively. The amplifier and capacitor C\ :sub:`1` form the integrator function. Feedback resistor R\ :sub:`2` serves as the one bit feedback DAC. The Channel B input should be connected to alternately measure the digital and analog output waveforms at Dout and Aout. C\ :sub:`2` and R\ :sub:`3` form a simple RC low pass analog reconstruction filter.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-delta-sigma-fig_2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 First Order Delta Modulator


Referring back to the block diagram, the AD8541 op-amp along with capacitor C\ :sub:`1` are the integrator function. The difference function takes place at the summing junction which is the negative input of the op-amp. The analog input voltage is converted into a current by resistor R\ :sub:`1`. The 1 bit digital to analog function (DAC) is performed by the Q output of the flip-flop and resistor R\ :sub:`2`. The flip-flop output can have two values, 0 Volts (-Vref) and +5 Volts (+Vref). Feedback resistor R\ :sub:`2` converts these two voltage levels into current which is also summed at the op-amp summing junction. The difference in the current in R\ :sub:`2` and R\ :sub:`1` is integrated on capacitor C\ :sub:`1`. The D input of the CMOS flip-flop will have a threshold voltage of approximately one half the power supply voltage and thus can serve as the comparator function. The digital bit steam can be observed at either the Q output of the flip-flop. The single pole RC low pass filter R\ :sub:`3` and C\ :sub:`2` serve as an analog reconstruction filter. Higher order active filters can be constructed based on this earlier lab activity.

Clock source:
-------------

This experiment needs a square wave clock source for the D-type FF. A variable frequency square wave source can be built using the AD654 voltage-to-frequency converter IC, as shown in figure 3.

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

Alongside the other circuit from figure 2 construct the AD645 based digital clock source generator shown in figure 3. Refer to the AD654 datasheet for more details on the operation of the circuit. The output frequency is determined by the values of C\ :sub:`2` and R\ :sub:`5` and the voltage applied to pin 4 (V\ :sub:`REF`). A variable voltage divider consisting of R\ :sub:`1`, R\ :sub:`3` and potentiometer R\ :sub:`2`, across the 2.5 V supply creates V\ :sub:`REF`. The square wave output at pin 1 of the AD654 drives the clock input of the 74HC273 at pin 11.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-delta-sigma-fig_3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Voltage-to-frequency Converter square wave source


Check the output frequency of the clock source with scope cannel B. It should be at least 10 KHz and be able to be adjusted up to 25 KHz or as much as 35 or 40 KHz.

Hardware Setup:
~~~~~~~~~~~~~~~

Procedure:
~~~~~~~~~~

AWG output CA-V should start out set as a DC shape with an Max value of 0.5 volts for the first measurement. With the above settings save the observed waveforms for both the digital (Dout) and filtered analog output (Aout) as plot number 1 in your lab report. The digital output waveform should be low most of the time with narrow pulses. The reconstructed analog output after the RC low pass filter should have a DC average value approximately the same as the value that the DC output of the waveform generator is set to. Now set the DC value of channel A to 2.5 volts. Again save the observed oscilloscope waveforms as plot number 2 in your lab report. The digital output should be about half of the time and the average value of the analog output should be close to 2.5 volts. Again set the DC value of channel A to 4.5 volts. Again save the observed oscilloscope waveforms as plot number 3 in your lab report. The digital output should be high most of the time and the average value of the analog output should be close to 4.5 volts.

Change the shape of AWG channel A to Sine. Change the Min value to 1.5 and the Max value to 3.5 (amplitude equal to 1 V). Now save the waveforms as plot number 4 in your lab report. Open the spectrum analyzer window. The frequency spectrum of the digital waveform and analog waveforms can now be measured and saved as plot number 4 in your lab report.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-delta-sigma-fig_4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Dout waveform for 200 Hz input sinewave


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-delta-sigma-fig_5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Aout waveform for 200 Hz input sinewave


Questions:
~~~~~~~~~~

| What is the effect of changing the DC value of the analog input?
| What is the effect of changing the frequency of analog input?
| What is the maximum analog input frequency?
| Looking at the spectrum of the digital output, why does the noise level increase with frequency?
| What is the effect of changing the value of integrator capacitor C\ :sub:`1`?
| Does the spectrum change? Is there a minimum value for C\ :sub:`1`? Is there a maximum value for C\ :sub:`1`?
| What is the effect of changing the frequency of the digital pulse?
| How is the spectrum of the digital output changed? Is there a minimum? or a maximum?
| The simple single pole RC low pass filter R\ :sub:`5` C\ :sub:`2` removes some of high frequency the noise in the analog output spectrum. What would be the effect of a higher order (active) filter on the analog output spectrum?

Using Semi-Digital FIR Reconstruction Filter:
---------------------------------------------

The remaining 7 stages in the 74HC273 can be configured as a Semi-digital FIR filter as in this Lab Activity. Connect the remaining 7 FF stages in the 74HC273 as a shift register as shown in figure 6.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-delta-sigma-fig_6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, Shift register FIR reconstruction filter


Observe the FIR reconstructed analog output as shown in figure 7. How does it compare to the digital and analog outputs without the FIR filter as in figure 2?

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-delta-sigma-fig_7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, FIR filter output w/o capacitor


Further analog smoothing/filtering can be done by adding a 0.1 uF capacitor from the output to ground as we see in the next screen shot, figure 8. Higher order active filters can be constructed based on this earlier lab activity. Be sure to include waveform plots of the analog output for both cases in your lab report.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-delta-sigma-fig_8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, FIR filter output with capacitor


Again use the frequency spectrum analyzer to observe of the FIR output without the capacitor and with a capacitor and save them as plots in your lab report. Explain any difference you see compared to the spectrum plots you got without using the FIR filter.

Appendix:
---------

\**74HC273 functional block diagram \*\*

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-lfsr-fig_6.png
   :align: center
   :width: 250px

.. container:: centeralign

   74HC273 Pinout


D-type Flip-Flop from Transistors:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Analog Parts Kit includes the 74HC273 Octal D-type flip-flop but a functional equivalent can be built using the individual transistors, resistors and capacitors from the kit. In the Lab Activity on NPN Multivibrators we built a falling edge triggered D-type flip-flop from three NPN transistors. Here will flip the circuit over and use PNP transistors to build a rising edge triggered D-type flip-flop. We can add CMOS inverter buffers from the 74HC04 hex inverter (or CD4007) to the D and Clock inputs and the Q and QB outputs to more closely emulate a CMOS D-type FF such as a 74HC74 device.

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

| 3 – 1 KΩ resistors
| 3 – 100 KΩ resistors
| 2 – 47 KΩ resistors
| 3 – small signal PNP transistors (2N3906)
| 2 – small signal diodes (1N914)
| 2 – 39 pF capacitors
| 2 – 100 pF capacitors

.. _directions-2:

Directions:
~~~~~~~~~~~

Construct the D type flip-flop circuit as shown in figure A1 on your solder-less breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-lab-delta-sigma-fig_10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A1 Transistor D-type FF


**For Further Pre-Lab Reading:**

| http:*www.analog.com/media/en/training-seminars/tutorials/MT-023.pdf
  http:*\ www.analog.com/en/analog-dialogue/articles/using-sigma-delta-converters-1.html
| http:*www.analog.com/en/analog-dialogue/articles/using-sigma-delta-converters-2.html
  http:*\ www.analog.com/en/design-center/interactive-design-tools/sigma-delta-adc-tutorial.html
| http://www.mathworks.com/matlabcentral/fileexchange/19-delta-sigma-toolbox
| http://en.wikipedia.org/wiki/Delta-sigma_modulation]]
| http://www2.ece.rochester.edu/~zduan/teaching/ece472/reading/Aziz_1996.pdf

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-signals-labs-list>`\ **.**
