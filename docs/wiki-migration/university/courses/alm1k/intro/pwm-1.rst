Activity: Pulse Width Modulation - ADALM1000
============================================

Objective:
----------

In this lab activity the concept of pulse width modulation is explored. Pulse width modulation is used in a variety of applications including sophisticated power control circuitry. PWM will be used to adjust the brightness of an LED. Simple RC low pass filtering techniques will be investigated as a way to produce a "DC" average output from the PWM signals.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background
----------

Pulse width modulation (PWM), is a method of adjusting the average power delivered by an electrical signal, by effectively chopping it up into discrete parts. The average value of voltage (and current) fed to the load is controlled by turning the switch between supply and load on and off at a fast rate. The longer the switch is on compared to the off periods (so called duty cycle), the higher the total power delivered to the load.

Rather than adjust a constant voltage (or current) to an LED circuit, we will change the voltage applied to the LED using pulse width modulation (PWM). This method has some significant advantages over the constant voltage method.

For additional background, read the online tutorials on pulse width modulation listed in the **"For Further Reading"** section at the end of this Activity. Do not expect to understand everything. Rather, focus on the main idea, that the duty cycle translates to signal average.

Experiment
----------

Pulse Width Modulation with ADALM1000

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Jumper Wires
| 1 - 470Ω resistor
| 1 - LED, any color is fine
| 1 – 10 kΩ resistor
| 1 – 1 uF capacitor

Connect the 470Ω and the LED to the channel A waveform generator (AWG1) and ground. Measure the input voltage waveform with the CA-V scope trace. It is not necessary to measure the voltage across the LED in this experiment. CH A is connected to the left end of the resistor and GND is connected to the bottom (-) end of the LED. The circuit is shown in figure 1.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-pwm-fig-1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1 PWM LED circuit


Set up the CH A waveform generator in SVMI mode and so that it produces a square shape waveform at a frequency of 2 Hz, with Max voltage = 5V and Min voltage = 0V. That is, the pulses go from 0 to 5 V. Be sure that the Sync AWG box is not checked. The waveform generator window should look like the one in figure 2. The AWG CH B settings do not matter except that it should be in Hi-Z mode.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-pwm-fig-2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2 AWG controls


Click on the green Run button to start the function generator and describe what you see as you observe the

Note the entry box next to the "%". This will allow you to adjust the duty cycle. Vary the duty cycle throughout its range from 0% to 100% in steps of 10% and describe what you observe.

Set the duty cycle back to 50%. Now adjust the frequency to 100 Hz (see Figure below). Describe what you see now. Again vary the duty cycle from 0% to 100% in steps of 10% and describe what you see. While you are varying the duty cycle, measure the average voltage that is being produced by the waveform generator by displaying the Avg value under Meas CA.

Record the measurement for each duty cycle setting in your lab report.

Finally, at 50% duty cycle, lower the frequency of the square wave until you can just start to see the LED flash. Observe the LED both directly and to the side using your peripheral vision. Record the value of the highest frequency that you are able to sense flashing looking in both directions. Are they the same? How does this frequency relate to the refresh rate of televisions and computer monitors?

Low Pass Filtering to Average PWM Output
----------------------------------------

In this part of the activity you will use a simple RC low pass filter to measure the apparent "DC" average of a PWM signal. Configure the circuit on your solderless as shown in figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-pwm-fig-3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, PWM low pass filter schematic


The nominal voltage observed at the output of the low-pass filter is determined by just two parameters, the duty cycle and the PWM signal's low and high voltages which can be thought of as the peak-to-peak amplitude plus a DC offset. The relationship between duty cycle, amplitude, offset and the filtered output voltage is fairly intuitive. In the frequency domain, a low-pass filter removes (suppresses) higher-frequency components of an input signal. The time-domain equivalent of this effect is smoothing, or averaging, thus, by low-pass filtering a PWM signal we are extracting its average value. Let's assume the duty cycle is 50% and our PWM signal low and high voltage is 0 and 5. You can probably guess what the nominal output of the filter will be: 2.5 V, because the signal spends half of its time at 0 V and half at 5 V, and thus the smoothed-out version will end up right in the middle.

Procedure:
~~~~~~~~~~

Start with the Min and Max values of 0 and 5, a frequency of 100 Hz and 50% duty cycle. Select the CB-V trace from the Curves menu. Add the average channel B voltage by displaying the Avg value under Meas CB. The filter does not remove all the high frequency parts of the PWM signal so the residual frequency part is call e the ripple. To measure the ripple, add the P-P measurement for CB as well.

Again vary the duty cycle from 0% to 100% in steps of 10% and describe what you see. How does the average value and the amplitude and shape of the ripple change? Set the duty cycle back to 50%. Now adjust the frequency from 100 Hz to 2000 Hz in 100 Hz steps. How does the amplitude and shape of the ripple change?

Pulse Width Modulated Sine wave
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the built-in arbitrary waveforms in ALICE is a pulse width modulated sine wave. From the AWG CH A Shapes drop down, select the PWM Sine shape (figure 4). The Min and Max entries set the low and high voltages as with the simple square wave. The Freq entry sets the frequency of the sine wave. What was the duty cycle entry now sets the width of the PWM signal (should now be labeled PWidth). The number entered sets the number of master clock (100KSPS) samples per pulse, X 100. This effectively sets the PWM carrier frequency. 50 is a good place to start.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-pwm-fig-4.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 4, AWG CH A settings for PWM Sine


Click on the green Run button to start the AWG generator and describe what you see as you observe the PWM signal in the channel A trace and the filtered output in the channel B trace. You may need to adjust the Horizontal time/Div settings to display a couple of cycles of the sine wave. You should see something like figure 5.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-pwm-fig-5.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 5, PWM sine wave


| Try increasing and decreasing the number of samples per pulse effectively changing the PWM frequency.
| How does the filtered output change?

For Further Reading:
~~~~~~~~~~~~~~~~~~~~

| `Wikipedia - Pulse Width Modulation <https://en.wikipedia.org/wiki/Pulse-width_modulation>`__
| `Sparkfun PWM tutorial <https://learn.sparkfun.com/tutorials/pulse-width-modulation>`__
| `All About Circuits: PWM <http://www.allaboutcircuits.com/textbook/semiconductors/chpt-11/pulse-width-modulation/>`__
| `Low Pass Filter PWM signal <https://www.allaboutcircuits.com/technical-articles/low-pass-filter-a-pwm-signal-into-an-analog-voltage/>`__

Going further with PWM - flickering LEDs.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most of flameless LED candles are quite simple circuits. They consist of nothing more than an on/off switch, a 3V coin cell battery and the special flickering LED. The flickering effect is produced by an integrated pulse width modulation (PWM) circuit, inside the special LED as shown in figure 6. These flickering LEDs are a perfect way to demonstrate PWM in action both visually and with the ADALM1000 scope.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-pwm-fig-6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6, inside a flickering LED


After extracting the LED from the plastic candle housing insert the LED in your solder-less breadboard along with a 220 Ω current limiting resistor as shown in figure 7. Each time that the LED circuit turns on, current is drawn from the power supply, channel A set to DC 5 V, and through the 220 Ω resistor R\ :sub:`1` to ground. To observe the voltage across R\ :sub:`1` we can connect scope channel B, in Hi-Z mode to the resistor as shown.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-pwm-fig-7.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 7, LED test circuit


The LED is on most of the time and is switched off in a pulse width modulated fashion in bursts that make it appear dimmer or to flicker. When the LED is on the current through the LED causes a voltage drop across R\ :sub:`1` raising the voltage to about 2.5 V in the case of the LED that was used in this example and the 220 Ω resistor. Your particular LED may work slightly different. The current through the LED is much smaller when it is off thus the voltage across R\ :sub:`1` goes down to nearly 0 V. So the PWM current through the LED will appear as a PWM voltage that swings from 0 to 2.5V as we see for the channel B voltage trace in figure 8. In the figure we also displayed the Channel A current trace which as expected looks much like the voltage across the resistor. From this we measure the current to be a little over 10 mA when the LED is on and zero as we would expect when off.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-pwm-fig-8.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 8, Example PWM voltage waveform


From this screen shot we can see one of the PWM bursts. It is 32 pulses long for a total of about 100 mS or 10 Hz. So it is possible for the duty cycle to change every 100 mS and the LED will seem to flicker at 10 Hz.

The next two screen shots, figures 9 and 10, are close-ups of the beginning and end of a burst. From figure 9 we can measure the pulse width and period. For this burst the pulses are low (LED off) for 0.944 mS and high (LED on) for 2.278 mS for a total period of 3.222 mS or 310 Hz. The duty cycle comes out to be about a 70%.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-pwm-fig-9.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 9, Beginning of a burst


The end of a different burst shown in figure 10 has a lower duty cycle but the same 310 Hz frequency.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-pwm-fig-10.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 10, End of a burst


Figure 11 is another close up screen shot showing the chip transitioning from one pulse width to another. We can also see that the frequency (310 Hz) does not change as the pulse width changes.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-pwm-fig-11.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 11, Changing the pulse width


Another way to observe, hear actually, the PWM signal is to replace the 220 Ω R\ :sub:`1` with the series connected combination of a 100 Ω resistor and the speaker from the ALP2000 parts kit.

Not very musical but still interesting.

`You Tube Video <https://www.youtube.com/watch?v=753-lkao8l0>`__

Extra related links:

| `Does this LED sound funny to you? <https://www.evilmadscientist.com/2011/does-this-led-sound-funny-to-you/>`__
| `Reverse Engineering a candle flicker LED <https://hackaday.com/2013/12/16/reverse-engineering-a-candle-flicker-led/>`__
| `Hacking a Candle flicker LED <https://cpldcpu.wordpress.com/2013/12/08/hacking-a-candleflicker-led/>`__

Another thing you can do is make another normal LED flicker in sync with the special LED. Connect a regular Red LED from the kit in series with the flicker LED as shown in figure 12. Be sure to note the proper polarity for the second LED. A lower value resistor will be needed because of the larger total voltage drop of the series combination of the two LEDs.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-pwm-fig-12.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 12, Flickering a second LED


| Why does the second LED flicker as well?
| Does it matter what order the LEDs and resistor are connected?

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**
