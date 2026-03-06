Activity: Pulse Width Modulation - ADALM1000
============================================

Objective:
----------

The objective of this activity is to explore pulse width modulation (PWM ). The pulse width modulator takes a relatively lower frequency analog input signal and converts it to a much higher square wave signal where the duty-cycle ( pulse width ) of the square wave varies in proportion to the analog input signal.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

There are many uses for pulse width modulation. In this activity we will be concentrating on its use for analog signal transmission. PWM can be used to first modulate then transmit over some distance and finally demodulate analog signals. The PWM signal may be sent across some sort of isolation barrier by optical or magnetic means.

The modulation is done in a mostly analog fashion using a method called intersective PWM. In this technique, the analog signal and a high frequency ( modulation or carrier frequency ) sawtooth or triangular waveform, each drive one of the inputs of a comparator. The output of the comparator is a digital signal that is driven high and low each time the triangular waveform voltage and the analog input waveform cross each other. The percentage of the carrier frequency period ( time ) the output is high encodes the value of the analog input at that point in time.

**PWM sampling theory**

Conventional Nyquist Sampling Theory states that: "A bandlimited signal can be reconstructed exactly if it is sampled at a rate at least twice the maximum frequency component in it." But how does this relate to sampling a signal using a pulse width modulator?

The process of modulating the output pulse width of an oscillator by some analog ( continuous ) signal is non-linear and it is generally believed that using a low pass filter to recover the original input signal is imperfect for PWM. The PWM sampling theorem states that PWM can be perfect. The theorem states that "Any bandlimited baseband signal within ±0.637 ( where +1 is 100% on and -1 is 100% off ) can be represented by a PWM waveform with unit amplitude. The number of pulses in the waveform used to represent the input value is equal to the number of Nyquist samples." This makes intuitive sense when considered against conventional Nyquist sampling. In theory you would need only one PWM pulse to decode the corresponding analog input but that would require an perfect ideal analog reconstruction filter. Given a finite real analog filter multiple PWM pulses will be needed to reconstruct the analog output. How many PWM pulses, called over sampling, will depend on the order of the analog filter. Simple first order or second order filters will require many PWM pulses to adequately remove or suppress the high frequency carrier from the output.

**The basic pulse width modulator**

In this previous activity on :doc:`voltage comparators </wiki-migration/university/courses/alm1k/alm-lab-comp>` we investigated a circuit which generated both triangle wave and square wave outputs. One variation of the circuit included a means to vary the symmetry of the waveforms ( pulse width ) by changing the relative charging / discharging resistance in the integrator section of the circuit. The resistance was changed by moving the wiper of a potentiometer ( variable resistor ). We can modify that circuit to allow the pulse width to be varied though a voltage input rather than a mechanical potentiometer.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wire kit
| 1 – OP484 quad rail-to-rail op-amp
| 1 – 4.7 KΩ resistor
| 2 – 10 KΩ resistor
| 1 – 20 KΩ resistor
| 1 – 100 KΩ resistor
| 1 – 4.7 nF capacitor
| 1 – 10 nF capacitor
| 1 – 47 nF capacitor
| 1 – 100 nF capacitor

Directions:
~~~~~~~~~~~

Construct the PWM test circuit as shown in figure 1 on your solder-less breadboard. Start with integrator capacitor C\ :sub:`I` equal to 100 nF ( 0.1 uF ). The oscillator should run at around 1 KHz.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-pwm_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, analog Pulse Width Modulator


Hardware Setup:
~~~~~~~~~~~~~~~

Start with both scope channels in Hi-Z mode to check that the circuit oscillates. You will later use Channel A as the input signal source.

Procedure:
~~~~~~~~~~

With Channel B in Hi-Z mode first connect it to the output of A\ :sub:`2` at pin 7. Set the trigger to CH-B, rising edge ( setting Auto Level to on is also useful ). Adjust the time base so that between 2 and 5 cycles of the output are displayed. Both scope channels should be set to 0.5V/Div. With Channel A also in Hi-Z mode the non-inverting input of A\ :sub:`1` will be at 2.5 V through R\ :sub:`3` and the oscillator square wave output should have a 50 % duty-cycle i.e. high half the time and low half the time. You can also observe the triangle waveform at the output of A\ :sub:`1`, on pin 1.

Now set Channel A to SVMI mode and the shape to DC. Set the Max value to different voltages between 1.0 and 4.0 volts and measure the resultant duty-cycle seen at the output for each DC value. Report these values in your lab report. Also note any changes in the frequency of the output square wave as the DC level is changed. Explain what you observe.

Now configure the channel A voltage generator CA-V for a 100 Hz sine wave with a 1 V Min value and 4 V Max value. Channel B should remain set in the Hi-Z mode. Set the trigger to none. The input sine wave should be displayed on the Channel A voltage trace and the pulse width modulated output waveform should be displayed on the Channel B voltage trace. The input sine wave should be stable on the screen and the PWM output will be jumping around with different width pulses.

The oscillator is running a little too slow to be properly modulated by the 100 Hz input signal. Replace the 100 nF C\ :sub:`I` capacitor with a 10 nF ( 0.01 uF ) capacitor. Now the oscillator should be running about 10 times faster. This will make the square wave output much harder to see on the Channel B trace. Move the Channel B input to the output of the RC reconstruction filter ( at top of C\ :sub:`F` ). Try different values of C\ :sub:`F` from 4.7 nF, 10 nF, 47 nF and 100 nF. The Channel B trace should look like the input sine wave with different amounts of fuzz depending on the value of C\ :sub:`F`. The fuzz is a result of some of the high frequency PWM carrier leaking through the simple first order RC filter. The reconstructed output will also be delayed with respect to the input and be slightly attenuated, again based on the value of C\ :sub:`F`. Save screen shots of the output trace and include them in your lab report. Also note the amplitude of the fuzz and the delay and amplitude of the overall sinewave.

Repeat the above measurements with C\ :sub:`I` equal to 4.7 nF ( 0.0047 uF ). This should make the oscillation frequency even higher and the amplitude of the fuzz on the reconstructed output even smaller. Explain the results you observe.

Try extending the Min and Max values of the input sine wave all the way to 0.0 and 5.0 volts. What are the Min and Max values where the modulator saturates or stops making an accurate version of the input?

**Second order low pass filter**

We can get slightly better attenuation of the carrier frequency by adding a second pole to the simple RC filter on the output. Normally there would be a buffer amplifier between the filter sections but if we make the impedance of the second stage 10 times larger ( i.e. 10 KΩ vs 1 KΩ but with the same RC time constant ) then the loading of the second stage is minimal and we get most of the benefit of the second filter stage. You can experiment with different values for C\ :sub:`F1` and C\ :sub:`F2`.

Add the second filter stage to your breadboard as shown in figure 2 and compare the amount of the carrier frequency feeding through to the output now vs with just the single filter stage as in figure 1. Also note the amount of attenuation and phase shift of the input ( 100 Hz ) you observe now vs with the single filter stage. Explain the differences you see.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-pwm_f2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2, second order low pass filter


Applying A Digital filter to the PWM output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ALICE desk-top software has an optional interface that allows you to apply a digital filter to the scope waveforms. Add the following line to your alice_init.ini file if it does not already have it:

-  global EnableDigitalFilter; EnableDigitalFilter = 1

Close and restart ALICE if needed. There should be a button in the right side menu panel labeled Digital Filter. Click on the button to open the digital filter interface.

From the :doc:`ALICE desk-top user guide </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` Wiki page down load the `example digital filters <https://wiki.analog.com/_media/university/tools/m1k/alice/example-filters.zip>`__ archive. Un-zip the archive into your working directory. There should be a number of .csv files.

In the Digital Filter interface, click on the Load CH-B Filter Coef button. Find the filter file named 1khz-low-pass-3khz.csv and click on that file and load it. The interface should now display that file name and a Length = 93. The 1khz-low-pass-3khz.csv file contains the filter coefficients for a low pass filter with a pass band up to 1 KHz and a transition band from 1 KHz to 3 KHz ( assuming the 100 KSPS of the ALM1000 input channels ).

You will need to set the Hold Off time to 5 mS to not display the first part of the waveform where the digital filter has not yet settled. Click on the Filter CH-B check box. You should now see a smooth trace of the sine wave on Channel B. Try different values of C\ :sub:`F` including no cap ( leave open ). How does the value of C\ :sub:`F` effect the digital filtered trace and the not digital filtered trace? Try different values for C\ :sub:`I`, which changes the modulator frequency. How does that effect the output?

If you have time try some of the other filter files.

**For Further Reading:**

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
