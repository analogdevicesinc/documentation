ALICE User’s Guide for using Equivalent Time Sampling (ETS)
===========================================================

Objective:
----------

This document serves as the advanced User’s Guide for using Equivalent Time Sampling (ETS) in the ALICE 1.3 Desktop software interface written for use with the ADALM1000 active learning kit hardware.

Background
----------

Bandwidth vs Sample Rate and the ADALM1000
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The meaning of "bandwidth vs sample rate", especially in relation to a low cost USB based digital oscilloscope like the ADALM1000 is something that can cause a lot of confusion at times. For those familiar with the Nyquist-Shannon Sampling Theorem, it seems strange that an analog to digital convertor (ADC) that has a maximum sample rate of 100 KSPS is able to measure signals beyond the Nyquist limit of one half the sample rate let alone see waveforms that are at even higher frequencies. However, given the right circumstances it is possible to do this and much more. The 1.3 version of the ALICE desktop software suite for ADALM1000 includes an optional user interface that implements a form of equivalent time sampling or ETS.

Periodic waveforms
~~~~~~~~~~~~~~~~~~

The key to understanding how this "magic" works is to realize that many of the kinds of signals that an oscilloscope user might like to measure are periodic. That is, they have a fixed pattern or shape that repeats periodically. Indeed it is almost impossible to see any other type of signal with an ordinary (non-sampling) analog oscilloscope. A digital oscilloscope like ALM1000 can of course capture and store any non-periodic waveform at the base real time sample rate. If we are interested in measuring waveforms with frequency content higher than half the sample rate, as the specification of many ADCs suggest we can, then we will be limited to periodic waveforms. The successive approximation ADC used in the ALM1000 is designed to exploit this ability by sampling the analog input for a much shorter period of time than a full sample period. That is, it has a very short acquisition time (i.e. time to capture the input signal) but it requires additional time to convert the sampled analog value to its encoded digital value. This short time aperture is what enables the ADC to see frequencies much higher than the sample rate alone might suggest, but there is some work to be done first in order to properly display the waveform.

Sub-sampled waveform capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you display a buffer of raw data captured from a signal with a higher frequency than even one tenth the sample rate (10 samples per cycle), you will still see a waveform; just not much detail. The following screen shot, in figure1, is taken with the ALM1000 sampling a 20.10 KHz square wave. As we can see there are only five sample points per cycle and the waveform does not look much like a square wave. The sampled data is drawn two different ways. The light green trace is drawn with lines connecting the sampled values. The dark green trace is drawn with horizontal and vertical lines or stair-steps connecting the sampled values. This is sometimes a better way to visualize the sampling process.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Real time sampling 20.1 KHz square wave at 100 KSPS


The 2.17 version of the ALM1000 board firmware allows it to be reconfigured from sampling the four measurement channels (2 voltage and 2 current) at 100 KSPS to sampling two measurement channels (2 voltage, 2 current or 1 voltage / 1 current) at 200 KSPS. This mode offers better time resolution but still often not enough. The following screen shot, figure 2, is taken with the ALM1000 sampling the same square wave at 200 KSPS.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Real time sampling 20.1 KHz square wave at 200 KSPS


Looking closely at these traces we can see that the sampled values are slightly different for each subsequent cycle. This happens because the time between samples, or sample rate is not an exact integer multiple (or fraction) of the input signal’s frequency. In this example the sample rate is100/200 KSPS vs the 20.1 KHz of the input signal.

If there are less than 2 samples per cycle you will see an "alias", or frequency shifted version of the waveform.

If certain conditions are met where the samples fall at different points in each cycle of the input signal, the alias is unique, meaning you can "unwrap" or re-sequence the raw data to reveal the true waveform. This process is known as sub-sampling or equivalent time sampling and is a technique used by many digital oscilloscopes to display high frequency signals. It is similar to a radio receiver where two frequencies are "mixed" to produce the "sum and difference" frequencies to shift from a high frequency to a lower one. Indeed, many ADCs (and DACs) in the Analog Devices catalog are often used to perform this frequency translation function in systems like cell phone towers and WiFi networks. The next screen shot, figure 3, is taken again with a 20.10 KHz as the input but now using ETS techniques. The approximately 20.1 KHz input frequency is now down converted or shifted to a much lower frequency around 333 Hz or a factor of 60:1. This multiplies the 100 KSPS to an effective sample rate of about 6 MSPS. So there are now 60 X 5 or 300 samples per cycle (or you can think of it as the new lower frequency signal has been sampled at 100 KSPS). The software scales the horizontal time scale based on the new effective sample rate. The time per Div is the same 20 uSec/Div as in the previous two screens but now we can see much more detail in the waveform including the single pole response of the analog inputs.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Equivalent time sampling 20.1 KHz square wave at 6 MSPS


**What's the catch?**

A minor digression at this point is in order. Why 20.1 KHz and not exactly 20.000 KHz? 20.000 KHz is a rational fraction of the fixed 100 KSPS sample rate and the sample points will fall at exactly the same point in each cycle so no additional waveform details would be obtained. With a fixed real time sample rate there are certain frequencies that fall in nulls or no-go zones and can't be used with the ETS as implemented for the ALM1000. This limitation is not so great for a general purpose piece of test equipment but is perfectly acceptable for using the ALM1000 in a teaching situation where the experiments can be tailored to the fixed frequencies allowed due to the fixed real time sample rate.

Another point to note here is that the scheme used in ALICE will down convert the input frequency to the frequency "offset" (or integer multiple of the offset) chosen in the software. These screen shots were taken with the input frequency offset adjusted to about but not exactly 100 Hz thus the signal displayed is the actual offset.

So, when you read a specification that says "Oscilloscope Y has a 100 MHz bandwidth but a 20 MHz sample rate" you know it means that it is using sub-sampling and the scope can display a periodic waveform with frequency components up to 100 MHz.

In the case of ALM1000, it has an analog bandwidth of slightly more than 100 KHz and a real time sample rate of up to 100 KHz (200 KHz for 2 channels). Using ETS the apparent sample rate could be much higher even into the 10's of MHz depending on how small the frequency offset is.

Sub-Sampling does not free you from the constraints of the Nyquist theorem: the bandwidth of the signal must still be less than half the sample rate to avoid destructive aliasing. However, the signal may appear anywhere in the analog bandwidth of the ADC so long as the bandwidth of the signal remains less than half the sample rate.

For example, if you have a 125 KHz analog capture bandwidth and a up to 100 KSPS sample rate you can measure a signal with a fundamental frequency of 65 KHz and bandwidth of 50 KHz (i.e. you can see any frequencies between 65 KHz and 115 KHz) which might be especially useful if the software has a build-in spectrum analyzer like ALICE. If the signal is not sufficiently band limited, it must be filtered to prevent aliased components in the result. The ALM1000 has a single pole RC filter ahead of the ADC input with a cut-off frequency a little more than 100 KHz.

There is one important exception that frees you from this constraint: if the signal is harmonic (i.e. there are no frequency components that are not integer related to the fundamental frequency) and the sample rate is different to and unrelated to the fundamental, it is possible to unwrap all signal harmonics up to the physical analog bandwidth of the analog input signal chain.

This is how ALICE, and any other digital scope software that can perform equivalent-time sampling, can see waveforms at frequencies much higher than the Nyquist-Shannon Sampling Theorem would otherwise imply.

Using Equivalent Time Sampling with the ADALM1000
-------------------------------------------------

The ALICE 1.3 desktop software suite for ADALM1000 includes an option that implements a form of equivalent time sampling or ETS.

.. _periodic-waveforms-1:

Periodic waveforms
~~~~~~~~~~~~~~~~~~

Many of the kinds of signals that an oscilloscope user might like to measure are periodic. That is, they have a fixed pattern or shape that repeats periodically. Indeed it is almost impossible to see any other type of signal with an ordinary (non-sampling) analog oscilloscope. A digital oscilloscope like ALM1000 can of course capture and store any non-periodic waveform at the base real time sample rate. Often the analog signal chain and the ADC used in a scope like the ALM1000 have more usable bandwidth than some fraction of the sample rate.

.. _sub-sampled-waveform-capture-1:

Sub-sampled waveform capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you display a buffer of raw data captured from a signal with a higher frequency than even one tenth the sample rate (10 samples per cycle), you will still see a waveform; just not much detail. If the sampling frequency is not exactly an integer fraction (or multiple) of the input frequency each sample represents a unique point somewhere along the repeating waveform. For example if we look at figure 4 we see a case where the sample frequency is slightly slower than the input frequency, by a factor of 19/20. So from the top graph we see that 20 unique points are obtained from 20 different cycles of the input signal. If these sample points are then assembled in the proper order we get the graph on the bottom.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Sub-sampling with a ratio of 19/20.


In this simple example the points are just plotted in the order they are taken. If, on the other hand, the ratio of the input frequency and the sample rate were the other way around, 20/19, then each sample would come earlier in each cycle and it would look like time was going backward if the points were plotted in the same order. To make time increase the order of the points would need to be reversed. This sub-sampling has the same effect as a down conversion mixer shifting the input to a lower frequency, even DC for certain ratios like 1, or 2 or 3 etc. This technique assumes that either the sample rate or the input frequency or both are adjustable such that a known ratio can be achieved. In the case of the ALM1000 we have only certain fixed sample rates, to work with. The maximum base sample rate is 100 KSPS for 4 channel measurements and 200 KSPS for 2 channels measurements. Other lower sample rates are possible but are limited to certain fractions of the sampling timer clock in the microcontroller. To calculate the actual sample rate we need to know the minimum number of clock cycles per sample, which is 240. The ALM1000 sample timer clock is 48 MHz. We know that the time per sample is 1 over the requested new Sample Rate.

m_sam_per = round(48 MHz / (2.0 \* Sample Rate))

To convert this back to the actual sample time:

sample_time = m_sam_per / 48 MHz

To convert back to the actual sample rate:

Actual Sample Rate = int(round( (1.0/sample_time)/2.0) )

The first possible sample rate lower than the 100 KSPS maximum is 99585. The next below that is 99174, and below that is 98765, 98361 etc. These values are doubled of course when sampling just 2 channels. These are small but still finite steps in the available sample rates.

Fortunately it is possible to use a different approach. Instead of trying to set the exact ratio, the fixed sampling rate is used and if we know the frequency of the input signal an actual ratio is then calculated. With this known ratio it is very easy to find out which sample within the record has what delay (or its position) within the input waveform period.

As an example we can use a simple ratio where the input frequency is 39/20 times the sample rate or there are 1.95 cycles per sample. It means than every following sample is delayed by 1 full cycle and 0.95*T, where T is the time index in the record, relative to the current one. If we do the calculations shown in the following table where we multiply the cycles per sample by the time index and then take just the fraction part in the last column. If we multiple this fraction of a cycle by the length of the record we have the position to place that sample in a new re-sorted sample record.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-t1.png
   :align: center
   :width: 500px

To implement this technique in ALICE we use two variables. One is the dividend of the fraction of the sample rate we are targeting. For example if we want to observe input frequencies just above (or below) 1/6 of the sample rate (multiples of 16,666.67 Hz), we use 6. Another is what is called an offset for lack of a better term. A number of possible values can be used for this, ALICE starts at -25 and adjusts this factor to get a record length based on the time/Div setting. But never using a record length larger than a 95,000 sample limit (0.95 seconds at 100 KSPS).

First we need to calculate how many samples (length of the record) will be needed to capture the right number of input waveform cycles. As we have already pointed out there are only certain fractions of the fixed sample rate that we can use.

Record Length = (Dividend \* Sample Rate) / (10,000 \* Offset)

For example for a divide factor of 6 and an Offset of -25 we get a record length of 24,000 samples or 240 mSec. This means that the lowest frequency we can shift an input waveform to and see one complete cycle would be 1/240 mSec or slightly more than 4 Hz. The idea is to shift the input to somewhere between 100 Hz and 5 KHz for optimal display, the lower the frequency the higher the effective sample rate will be.

Now we need to calculate the factor we need to multiply the fractions of a cycle or each time index (right hand column in the table) by.

Index multiplier = int(Record Length \* (Sample Rate + Offset ) / (Sample Rate))

This may seem all very complicated and it is. That is why the software does all the calculations and plots the results for you.

Divide factors from 1 to 75 are allowed in the program.

The ETS controls in ALICE 1.3
-----------------------------

Unlike in a bench digital oscilloscope with an equivalent time sampling mode feature, the ETS mode controls in ALICE 1.3 require some manual settings by the user. By default access to the ETS feature is disabled. To enable access to the ETS controls add the following lines to your alice_init.ini file:

| global EnableETSScreen; EnableETSScreen = 1
| global EnableHSsampling; EnableHSsampling = 1

Three new control widgets will now appear in the main ALICE scope window, figure 5. Two will appear along the top next to the Time per division entry. The one on the right is where the User will enter the target minimum input frequency that is to be displayed. More later in this guide on how to determine this frequency. Next to that is where the time (horizontal X) multiplication factor will appear. The program will attempt to calculate this vale based on the target minimum input frequency entered and the chosen sample rate. This “guess” can be very off from the actual multiplication factor based on how accurate the User guessed at the entered target minimum input frequency. Either the Fmin or MulX values can be adjusted to more accurately “calibrate” the horizontal time scale. More on doing that adjustment later in the guide as well. The third button added will appear along the right hand column of buttons below the other instrument enable buttons. Where in the list it appears will depend on what other optional feature controls are enabled in the alice_init.ini file.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, New widgets on main oscilloscope window


To control all this ALICE 1.3 has the ETS Controls window, figure 6. The current real time sample rate (starting default is 100000) is shown at the top as a reminder. The calculated equivalent time sample rate is displayed based on the time multiplier factor. Next there is a check box to turn on and off ETS. Next is an entry space to enter the Divide factor, in the case below 5 was used. From the divide factor entered ALICE picks an offset and record length to best display the input signal (values are only displayed when in Debug mode). The base or minimum frequency is shown, 1/5 of the sample rate or 20,000 Hz. This is the frequency that will be shifted to DC. The user can enter a frequency multiplier. Multiply factors from 1 to 75 are allowed in the program. The multiplied value is displayed. This does not really change anything in how ALICE displays the signal. It is handy to use this value when setting or selecting the sample rate with respect to frequency of the input signal.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f6.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 6, ETS controls


As was pointed out earlier if the input frequency is above or below the Base frequency (the frequency that will be shifted to DC), in other words the frequency offset is positive or negative, the order of the samples will be either forward or reversed in time. This is generally set correctly based on the Frequency value entered as the “guess” for Fmin. Control buttons allow the user to select which way to order the data displayed if the waveform looks backward.

There is a major complication in the case of the ALM1000 and how the A and B channels are sampled. The A channel samples first every 10 uSec (at 100KSPS) and channel B samples second, 5 uSec later, between the channel A samples. This is not so big a deal in real time sample mode and ALICE handles this when drawing the traces. But in ETS mode this 5 uSec difference causes the channel B data to shift all over with respect to channel A depending on the frequency of the input and to what frequency it is down shifted to. Think of this 5 uSec difference with respect to the equivalent time sampling rate which might be many MHz. If the time scale multiplication factor, Mul X is set properly such that the horizontal time scale is “calibrated” to the shifted input frequency then the CHB Time Shift should be set correctly automatically by the software.

A good way to adjust or “calibrate” the Mul X horizontal time scale factor is to connect both Channel A and B inputs to the same signal and adjust Mul X (or Fmin) until both traces are aligned on top of each other. You can then move channel B to the other signal you wish to observe.

There is a place to manually enter a shift factor for channel B but the software generally changes the value based on the entered Mul X value automatically. This shift factor is in sample points. A positive number shifts the trace to the right and a negative one shifts it to the left. Either might be necessary depending on the Forward or Reverse data order.

This time shift is only required when the ALM1000 is set to sample all four measurement channels simultaneously. If the Double Sample Rate button in the Set Sample Rate controls is checked, see figure 7, the channel B time shift factor will always be 0.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f7.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 7, Base Sample Rate controls


Advanced Signal Processing Techniques
-------------------------------------

Input Frequency Compensation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The software frequency compensation for each channel consists of a cascade of two adjustable `first order high pass filters <https://en.wikipedia.org/wiki/High-pass_filter#Algorithmic_implementation>`__. The time constant and the gain of each stage can be adjusted. Normal first order high pass filters do not pass DC so a DC gain of 1 path is added to the overall second order high pass software compensation filter. This structure is often called a shelving filter because of the shape of its frequency response.

This functionality is generally used to compensate for a low pass response that might be introduced when using external resistor dividers and the internal input capacitance of the ALM1000 AIN and BIN pins. These software frequency compensation filters can also be used to compensate for the internal 100 KHz anti-alias filter in the ETS mode. Based on the time scale multiplication factor appropriate time constant and gain factors can be calculated from fixed values for any given multiplier.

In figure 8 we show the controls for the input compensation when the ETS feature is enabled. To turn on and off the compensation for Channels A and B there are check boxes under the Curves drop down menu. Turning on compensation applies to both the Scope and Spectrum tools (time and frequency measurements). The filter time constant and gain settings can be set using entry slots in the Settings Controls screen. The DC gain and offset adjust controls are unchanged.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f8.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 8, Settings controls with ETS turned on


The software also includes the option to process the waveform buffers with digital filters. For completeness the digital filter controls are shown in figure 9.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f9.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 9, Digital Filter controls


Example Use Case
================

As an example of how to apply the ETS functionality to measure high frequency signals we will use the ADALM-BUCK-ARDZ switch mode buck regulator experiment Arduino shield board plugged into an Arduino running the script from the lab exercise. The photo of the board in figure 10 shows the connection points we will be using.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 10, ADALM-BUCK-ARDZ test board


The first signal that will be measured will be the Arduino PWM output signal. Both channels will be connected to the same node. Any of the ground connection points will serve as the common ground reference for the ADALM1000. The PWM output signal will be a 0 to 5 V digital square wave signal. We will be using a resistor input divider to attenuate the signals before applying them to the AIN and BIN pins on the ALM1000 as shown in figure 11. The nominal gain factor for the resistors shown is 19.5/1.5 or 13. This is done to reduce the 5 V PWM signal to an amplitude that is low enough such that the limited large signal slew rate of the ADA4661 buffer does not affect the high speed digital edges as much. The wide dynamic range of the 16 bit ADC allows us to do this and still have at least 12 bits of resolution. Higher value resistors could be used but eventually the R2, C1 time constant becomes an issue that limits the frequency response. In this case the 19.5 K ohm total resistance does not present too large of a load on the Arduino digital output.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11, AIN and BIN Input voltage dividers


The first thing to do in the ALICE software is to “calibrate” the A and B channel DC gain and offset adjustment values. Connect the input end of the 18 K resistors (R1) for channels A and B both to ground (GND). It is best to enter the approximate Gain value, 13 in this example, first. Now adjust the CA-V and CB-V Offset Adjust values, as shown in figure 12, so that the CHA AvgV and CHB AvgV measure as close to 0 volts as possible (+/- a few mV is good enough). Now connect the divider inputs to the fixed +5.0V output pin. Adjust the Gain values so that the CHA AvgV and CHB AvgV measure as close to 5 volts as possible. (For better accuracy you can measure the fixed 5 V output directly without the voltage divider first and use that value as your target measurement when using the dividers).

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f12.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 12, A and B Input voltage divider Adjustments


Now go back and connect the input dividers to ground and recheck the Offset values. Changes to the Gain values can have small effects on the Offset so it is a good idea to iterate back and forth a couple of times between measuring +5 and GND until you have the values dialed in. Notice that the actual values for the gain in this example were slightly different than the calculated value due to the tolerance in the actual resistor values. Now we are ready to measure the Arduino PWM output signal. With both the channel A and B input dividers connected to the ADALM-BUCK-ARDZ test board PWM signal, jumper in upper left corner of the board and the ADALM1000 ground connected to the ADALM-BUCK-ARDZ ground, set the channel input ranges and positons along with the Time/Div such that you get a display something like shown in figure 13. The Fmin and Mul X entries could be anything at this point. Select the CA Freq value to be displayed. To get the best measurement of the input frequency the Real Time sample rate should be 200000. This should happen automatically when the time scale is set to 0.1 mS/Div.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f13.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 13, PWM signal Real Time Sampling display


The Arduino PWM frequency should be 31.250 KHz. The measured value (to one decimal place) is 31.3 KHz. This is very close to the expected value and any small difference is likely due to the frequency tolerance of the crystal oscillator on the Arduino board and the master crystal oscillator on the ALM1000 board. This value for the PWM input frequency will be the target Fmin value. You can transfer the CA Freq reading (to 3 decimal places) to the Fmin entry spot by clicking on Fmin (raised button), Figure 14. You can of course always manually enter the Fmin value. This may be needed in cases where the input signal is not a nice neat square wave and the software can’t get a correct reading of its frequency.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f14.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 14, Transfer CA Freq reading to Fmin entry


The frequency that Fmin was set to is 31.338 KHz, which is just a 0.2784 % difference from the expected 31.250 KHz from the Arduino PWM timer output.

Now that we know the target input frequency we can choose a real time sample rate and divider factor that is close but just below this frequency. If we select the allowed RT sample rate value of 93385 and divide by 3 we get 31128.33 Hz. So the Frequency Offset will be 31338 – 31128 or 210 Hz. Which is a good frequency range to convert down to. Another way to pick a RT sample rate is to manually enter a value in the Base Sample Rate spin box that you calculate by multiplying Fmin by some integer factor that is less than the 100000 max limit. When you hit return on the entered value the software will automatically pick the closest allowed rate.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f15.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 15, Select Real Time Sample rate and Divide Factor


Now we can Enable the ETS and after adjusting the horizontal time scale you should see something like what is shown in figure 16. To check that the proper MulX value is being used you can enable the Gated Measurement cursors. Clicking the left mouse button on the first rising edge and a second left click on the next rising edge will display the delta time (period) and frequency of the waveform. Note that the ET Sample rate is calculated and displayed in the EST controls. In this example the ET sample rate is 4.575865 MSPS, or 50 times (Mul X) the 93.385 KSPS RT sample rate.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f16.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 16, Traces with EST enabled


Since both input channels are connected to the same signal, both channels should be aligned exactly on top of each other as they are in the screen shot. If they are not then the Mul X factor is not adjusted correctly, i.e. the Fmin value was incorrect. To properly align the B channel to the A channel you can either adjust Fmin or Mul X.

Now we can set up the software input frequency compensation to correct for the 100 KHz low pass anti-alias filter. Open the Change Settings controls, figure 17. Make sure the Auto Set ETS Comp box is checked. The built in default Time constant and gain values should be correct for the 100 KHz filter in most boards but can be tweaked as necessary. The CHA and CHB values are automatically scaled by the ETS multiplication factor as it changes so the correct compensation should be applied for whatever the real time sample rate, Fmin and Mul X are set to.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f17.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 17, EST frequency compensation settings


From the Curves Drop down Menu we turn on the Frequency compensation. Now as we see in this next screen shot, figure 18, the RC setting of the 100 KHz anti-alias filter is compensated.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f18.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 18, Traces with EST and Frequency compensation enabled


We can now move channel B to look at other nodes on the ADALM-BUCK-ARDZ test board. In the next screen shot, figure 19, we show the waveforms for the PWM signal on channel A and the Inductor Switch node on channel B.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f19.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 19, PWM signal and Switch node traces


Another Example
~~~~~~~~~~~~~~~

Signal sources generated from crystal oscillators are prime candidates for using ETS. Direct Digital Synthesizers (DDS) such as the AD983x class function generators are good examples. Below in figure 20 are two examples of AD983x DDS boards. The one on the left is the SparkFun MiniGen, and the one on the right is one of the commonly available variants from multiple sources in China.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f20.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 20, AD983x DDS Function Generators


ALICE has a simple set of controls to program the registers in the AD983x shown in figure 21. To enable access to the AD983X DDS function generator controls add the following line to your alice_init.ini file:

global EnableMinigenMode; EnableMinigenMode = 1

The board on the right was used in this example. There is no output buffer amplifier so the analog output signal for sine and triangle waveforms is only about 600 mV p-p. For this small signal amplitude no input resistor dividers are needed. The serial interface pins on the board need to be mapped to the appropriate digital I/O pins on the ALM1000.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f21.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 21, AD983X DDS function generator controls


As in the first example we need to select a RT sample rate that along with the Divide factor results in a base frequency just below the frequency we set the DDS function generator to.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f22.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 22, Select Real Time Sample rate and Divide Factor


For the 97959 RT sample rate, with Fmin set to 32.768 KHz, Mul X is 94, the ET Sample rate will be 9.208146 MSPS. The screen shot below in figure 23 shows the output of the DDS function generator with the software frequency compensation turned on connected directly to both the AIN and BIN input pins.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f23.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 23, DDS function generator triangle waveform output


As the ETS part of the ALICE project progresses, the controls may become more automatic.
