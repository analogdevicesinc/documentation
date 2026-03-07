Activity: Optocouplers:
=======================

Objective:
----------

In this activity you will construct an optocoupler from an infra-red LED and an NPN photo transistor. You will investigate the operation of an optocoupler based analog isolation amplifier

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

The NPN transistor Optocoupler
------------------------------

Background:
~~~~~~~~~~~

An optocoupler, or optical isolator, is an electronic device designed to transfer electrical signals by light across an electrical isolation barrier between its input and output. The main purpose of an optocoupler is to prevent high voltages or voltage spikes on one side of the barrier from damaging components or interfering with the transmission of signals to the other side. Commercially available optocouplers can withstand input-to-output voltages from 3kV to 10 kV and voltage transients with speeds up to 10 kV/μs. The device consists generally of an infrared LED on one side as the input and a photo-detector such as a photo diode or photo transistor on the other with an electrical isolation barrier in between as shown in figure 1. When the LED is off, that is producing no light, there is no photo current into the base of the transistor and it is off. When the LED has current flowing through it producing light and there is sufficient photo current into the base of the transistor it will turn on. For more in-depth reading on optocouplers see: http://en.wikipedia.org/wiki/Opto-isolator

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab22_f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1 NPN transistor Optocoupler


Note that in all of the experiments you will do with the ALM1000 hardware the emitter ( or collector ) of the photo transistor will be connected ( or referenced ) to the ground and power terminals. This is done for measurement convenience but the photo transistor terminals can in fact be connected anywhere providing many hundreds or even thousands of volts of isolation.

Directions:
~~~~~~~~~~~

The first step in this activity is to construct your own optocoupler using the infra-red LED and NPN photo transistor supplied with the ADALP2000 Analog Parts Kit. There are two black plastic devices in the kit that look almost exactly the same. One is the photo transistor and the other is a photo diode. The one with the slightly shorter leads should be the photo transistor. If you have a DMM with a diode test function handy you can verify which is the photo diode and which is the photo transistor ( the photo diode will conduct in one direction and the photo transistor will not conduct in either direction ). If you are not using the Parts Kit for these lab activities similar devices may be substituted but your results may vary depending on the components used.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab22_p1.png
   :align: center
   :width: 250px

.. container:: centeralign

   QED-123 Infrared LED


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab22_p2.png
   :align: center
   :width: 250px

.. container:: centeralign

   QSD123 Infrared Transistor


First bend the leads of both the LED and photo transistor 90 degrees so that when inserted into the solder-less breadboard they are facing each other and are at the same level. Too keep them properly aligned and to keep out stray ambient light it is best to use a short length of tubing ( a half inch length cut from a ball point pen barrel is a good option ) or black electrical tape cut to the appropriate width to wrap around the combined LED and photo transistor as indicated below.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab22_p3.png
   :align: center
   :width: 400px

Materials:
~~~~~~~~~~

| ADALM1000 hardware module ( with ALICE desktop software )
| Solder-less breadboard
| Jumper wires
| 2 – 2.2 KΩ resistors
| 1 – single rail-to-rail op-amp AD8541 ( or AD8542 dual )

.. _directions-1:

Directions:
~~~~~~~~~~~

On your solder-less breadboard construct the circuit shown in figure 2. Notice that the NPN photo transistor is configured as a current sink with its emitter connected to ground. Note that the longer of the two leads on the photo transistor is the collector. Note that the shorter of the two LED leads is connected to ground. Double check the component datasheets to make sure you have made the correct connections. As a way to check if you have the LED polarity correct you can use channel B (in Hi-Z mode) to observe the voltage across the LED. It should only swing to less than 1 V and not follow channel A exactly.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab22_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 Optocoupler Input to Output characteristics


Hardware Setup:
~~~~~~~~~~~~~~~

Configure the channel A AWG output for a 100 Hz triangle wave with 0V Min value and 5V Max value. Both scope channels should be set to 0.5V/Div.

Procedure:
~~~~~~~~~~

Use channel A current trace to measure the current through resistor R\ :sub:`1` and the current in the LED. Turn on trace averaging to smooth out the noise in the current trace. Channel B measures the voltage across the photo transistor. Configure a Math trace to display the voltage across resistor R\ :sub:`2` by subtracting the channel B waveform from value of the fixed 5 V supply ( 5 – VBuffB[t] ). You can also calculate the current in the photo transistor ( in mA ) by dividing by the resistance ( (5 – VBuffB[t]) / 2.2 ) The Current Transfer Ratio or CTR is simply the ratio of these to currents. The CTR is a measure of the gain or efficiency or sensitivity of the device.

Questions:
~~~~~~~~~~

What is the Current Transfer Ratio of the device you constructed and tested? Is it constant over a range of input currents?

.. _hardware-setup-1:

Hardware setup:
~~~~~~~~~~~~~~~

Now configure the waveform generator for a 1 KHz sine wave with 1.4V Min and 2.8 V Max ( 1.2 V P-P swing centered on 2.2V. Both scope channels should be set to 0.5V/Div. The Min and Max settings might need to be adjusted slightly to make sure the output signal is relatively centered within the 0 to 5V range of the output. You want to make sure that the peaks of the sine wave are not too close to either 0V or 5V.

.. _procedure-1:

Procedure:
~~~~~~~~~~

In this simple circuit the conversion of the input voltage to current in the LED is nonlinear because the current vs voltage characteristic of the LED is exponential like a conventional diode. There are additional nonlinearities in the photo transistor when converting the light from the LED to current in the collector. The best way to measure these nonlinearities is by measuring the harmonic distortion seen in the output signal when the input is driven by a relatively pure sine wave.

Open the Spectrum display within the main ALICE window. Adjust the time base such that the fundamental and the first 5 or 6 harmonics are displayed. Write down and save the magnitudes of the fundamental and up to at least the 4\ :sup:`th` harmonic for future reference.

Driving the LED with a voltage to current converter
---------------------------------------------------

By putting the LED in the feedback loop of an op amp configured as a voltage to current converter we can greatly reduce the effect of the nonlinearity of the LED.

.. _directions-2:

Directions:
~~~~~~~~~~~

On your solder-less breadboard modify your circuit to look like the one shown in figure 3. Notice that the NPN photo transistor is now configured as a current source with its collector connected to the fixed positive 5V power supply. This was done to show that it indeed does not matter how the voltages on the transistor terminals are configured.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab22_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3 V to I LED drive


.. _hardware-setup-2:

Hardware Setup:
~~~~~~~~~~~~~~~

Configure the channel A AWG for a 100 Hz triangle wave with 2.5 Min and 5V Max values. Both scope channels should be set to 0.5V/Div.

.. _procedure-2:

Procedure:
~~~~~~~~~~

Repeat the same measurements you did on the simple resistor driver version on this circuit. Switch the AWG to a sine wave ( same 1KHz frequency as before ) and again measure the harmonic distortion. Remember to adjust the AWG amplitude and offset to get a similar output waveform as you had in the previous circuit.

.. _questions-1:

Questions:
~~~~~~~~~~

What would happen if the input signal were to go negative with respect to the fixed 2.5 V rail (below the common mode voltage)?

Compare your distortion measurements for this circuit to what you measured for the previous circuit. How much have the harmonics improved?

**For Further Reading:**

`Designing Linear Amplifiers Using the IL300 Optocoupler <https://www.vishay.com/docs/83708/appnote50.pdf>`_

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`

Appendix:
~~~~~~~~~

Integrated optocouplers.

Some models are in 6 pin packages and include a connection to the base terminal of the photo transistor. Others are in 4 pin packages and do not have base connections. FOD817 Series 4 pin photo transistor optocoupler from Fairchild Semi.

| Lite-On, Optocoupler DC-IN 1-CH Transistor DC-OUT 4-Pin PDIP (Avnet Part #:LTV-817)
| 4N25, 6 pin DIP package with Base terminal (Jameco Part no. 40985)
| 4N26, 6 pin DIP package with Base terminal (Jameco Part no. 41005)
| 4N28, 6 pin DIP package with Base terminal (Jameco Part no. 41013)
| 4N35, 6 pin DIP package with Base terminal (Jameco Part no. 41056)
| MCT6, MCT61,MCT62 dual photo transistor optocoupler from Fairchild Semi.
