Activity: Optocouplers.
=======================

Objective:
----------

In this activity you will construct an optocoupler from an infra-red LED and an NPN photo transistor. You will investigate the operation of an optocoupler based analog isolation amplifier and floating current source using integrated optocouplers.

The NPN transistor Optocoupler
------------------------------

Background:
~~~~~~~~~~~

An optocoupler, or optical isolator, is an electronic device designed to transfer electrical signals by light across an electrical isolation barrier between its input and output. The main purpose of an optocoupler is to prevent high voltages or voltage spikes on one side of the barrier from damaging components or interfering with the transmission of signals to the other side. Commercially available optocouplers can withstand input-to-output voltages from 3kV to 10 kV and voltage transients with speeds up to 10 kV/µs. The device consists generally of an infrared LED on one side as the input and a photo-detector such as a photo diode or photo transistor on the other with an electrical isolation barrier in between as shown in figure 1. When the LED is off, that is producing no light, there is no photo current into the base of the transistor and it is off. When the LED has current flowing through it producing light and there is sufficient photo current into the base of the transistor it will turn on.

For more in-depth reading on optocouplers see: http://en.wikipedia.org/wiki/Opto-isolator

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a22_f1.gif
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1 NPN transistor Optocoupler


Construction Directions:
~~~~~~~~~~~~~~~~~~~~~~~~

The first step in this activity is to construct your own optocoupler using the infra-red LED and NPN photo transistor supplied with the ADALP2000 Analog Parts Kit. If you are not using the Parts Kit for these lab activities similar devices may be substituted but your results may vary depending on the components used.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a22_g1.jpg
   :align: center
   :width: 250px

.. container:: centeralign

   **QED-123 Infrared LED**


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a22_g2.jpg
   :align: center
   :width: 250px

.. container:: centeralign

   **QSD123 Infrared Transistor**


First bend the leads of both the LED and photo transistor 90 degrees so that when inserted into the solder-less breadboard they are facing each other and are at the same level. Too keep them properly aligned and to keep out stray ambient light it is best to use a short length of tubing or black electrical tape cut to the approprate width to wrap around the combined LED and photo transistor as indicated below.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a22_g3.gif
   :align: center
   :width: 450px

.. container:: centeralign

   **Completed coupler**


Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 2 - 2.2 KΩ resistors
| 1 - single op-amp such as OP27

Directions:
~~~~~~~~~~~

On your solder-less breadboard construct the circuit shown in figure 2. Notice that the NPN photo transistor is configured as a current sink with its emitter connected to ground. Note that the longer of the two leads on the photo transistor is the collector. Note that the shorter of the two LED leads is connected to ground. Double check the component datasheets to make sure you have made the correct connections.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a22_f2.gif
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 Optocoupler Input to Output characteristics


Hardware Setup:
~~~~~~~~~~~~~~~

Configure the waveform generator for a 100 Hz triangle wave with 3V amplitude peak-to-peak and 2.5V offset. Both scope channels should be set to 1V/Div.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a22_oc_bb.JPG
   :align: center

.. container:: centeralign

   Figure 3 Optocoupler Breadboard Connections


Procedure:
~~~~~~~~~~

Scope channel 1 measures the voltage across resistor R\ :sub:`1`. and thus the input current in the LED. Scope channel 2 measures the voltage across resistor R\ :sub:`2` and thus the output collector current in the NPN transistor. The Current Transfer Ratio or CTR is simply the ratio of these to currents. The CTR is a measure of the gain or efficiency or sensitivity of the device.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a22_oc_wv.JPG
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4 Optocoupler Scopy Waveforms


Questions:
~~~~~~~~~~

What is the Current Transfer Ratio of the device you constructed and tested? Is it constant over a range of input currents?

.. _directions-1:

Directions:
~~~~~~~~~~~

Now move the 1- input of scope channel 1 to ground and move the 2+ input of scope channel 2 to the collector the photo transistor and scope input 2- to ground.

.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

Configure the waveform generator for a 5 KHz square wave with 5V amplitude peak-to-peak and 2.5V offset. Both scope channels should be set to 1V/Div.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Scope channel 1 now measures the input signal and scope channel 2 measures the output signal. The speed of the optocoupler can be characterized by the delay between the input and output waveforms. Another measure of the device speed is the rise and fall times of the output waveform. Another method of testing the frequency response of the optocoupler is to use the Network Analyzer instrument in the Scopy software. Set the frequency sweep from 10 Hz to 100 KHz. Set the AWG amplitude to 2V peak-to-peak and the AWG offset to 3V or whatever DC offset centers the output signal for your coupler circuit.

.. _questions-1:

Questions:
~~~~~~~~~~

| What is the input to output delay of the device you tested?
| Is it the same for the rising and falling edges?
| What is the rise and fall times of the output signal?
| What is the -3dB bandwidth of the coupler?

.. _hardware-setup-2:

Hardware setup:
~~~~~~~~~~~~~~~

Now configure the waveform generator for a 1 KHz sine wave with 1.2V amplitude peak-to-peak and 2.2V offset. Both scope channels should be set to 1V/Div. The offset might need to be adjusted slightly to make sure the output signal is relatively centered within the 0 to 5V range of the output. You want to make sure that the peaks of the sine wave are not too close to either 0V or 5V.

.. _procedure-2:

Procedure:
~~~~~~~~~~

In this simple circuit the conversion of the input voltage to current in the LED is nonlinear because the current vs voltage characteristic of the LED is exponential like a conventional diode. There are additional nonlinearities in the photo transistor when converting the light from the LED to current in the collector. The best way to measure these nonlinearities is by measuring the harmonic distortion seen in the output signal when the input is driven by a relatively pure sine wave.

Open the frequency display within the scope window. Adjust the time base such that the fundamental and the first 5 or 6 harmonics are displayed. Write down and save the magnitudes of the fundamental and up to at least the 4\ :sup:`th` harmonic for future reference.

Driving the LED with a voltage to current converter
---------------------------------------------------

By putting the LED in the feedback loop of an op amp configured as a voltage to current converter we can greatly reduce the effect of the nonlinearity of the LED.

.. _directions-2:

Directions:
~~~~~~~~~~~

On your solder-less breadboard modify what you have to look like the circuit shown in figure 3. Notice that the NPN photo transistor is now configured as a current source with its collector connected to the positive 5V power supply, Vp. This was done to show that it indeed does not matter how the voltages on the transistor terminals are configured.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a22_f3.gif
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5 V to I LED drive


.. _hardware-setup-3:

Hardware Setup:
~~~~~~~~~~~~~~~

Configure the waveform generator for a 100 Hz triangle wave with 3V amplitude peak-to-peak and 2.5V offset. Both scope channels should be set to 1V/Div.


|image1|

.. container:: centeralign

   Figure 6 V to I LED drive Breadboard Connections


.. _procedure-3:

Procedure:
~~~~~~~~~~

Repeat the same measurements you did on the simple resistor diver version on this circuit. Switch the AWG waveform to a square wave and remeasure the delay, rise and fall times for inclusion in your lab report. Switch the AWG to a sine wave ( same 1KHz frequency as before ) and again measure the harmonic distortion. Remember to adjust the AWG amplitude and offset to get a similar output waveform as you had in the previous circuit.


|image2|

.. container:: centeralign

   Figure 7 V to I LED drive Scopy Waveforms


.. _questions-2:

Questions:
~~~~~~~~~~

| What happens if the input signal W1 from the waveform generator goes negative (below ground)?
| Compare your distortion measurements for this circuit to what you measured for the previous circuit. How much have the harmonics improved?

Analog Isolation amplifier.
---------------------------

To make a more linear amplifier two matching optocouplers can be used. It is best to use integrated versions for this circuit.

The previous V to I configuration reduced the nonlinearity of the LED. If we also include a photo transistor inside the feedback loop we can also reduce the nonlinear effect of the light to current conversion characteristic of the photo transistor.

.. _materials-1:

Materials:
~~~~~~~~~~

| 2 - NPN optocouplers see Appendix below for specific device options
| 1 - 0.0047uF capacitor (472)
| 1 - 470Ω resistor

.. _directions-3:

Directions:
~~~~~~~~~~~

Build the circuit shown in figure 4 on your solder-less breadboard. The exact wiring of the optocouplers might be different depending on which kind you use (4 pin packages or 6 pin packages etc.). The pin numbers shown are generally standard for 4 pin packages. Be sure to consult the manufacturer's datasheet for how to properly connect your specific device.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a22_f4.gif
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8 Unipolar voltage input


.. _hardware-setup-4:

Hardware Setup:
~~~~~~~~~~~~~~~

Start with the waveform generator set for a 100 Hz triangle wave with 4.8V amplitude peak-to-peak and 2.5V offset as you have done for the previous two configurations. Both scope channels should be set to 1V/Div.

.. _procedure-4:

Procedure:
~~~~~~~~~~

Repeat the same measurements you did on the previous two versions of the circuit. Switch the AWG waveform to a square wave and remeasure the delay, rise and fall times for inclusion in your lab report. Switch the AWG to a sine wave ( same 1KHz frequency as before ) and again measure the harmonic distortion. Remember to adjust the AWG amplitude and offset to get a similar output waveform as you had in the previous circuits.

.. _questions-3:

Questions:
~~~~~~~~~~

| Does it matter which order LEDs D\ :sub:`1` and D\ :sub:`2` are connected?
| Does it matter which photo transistor Q\ :sub:`1` or Q\ :sub:`2` is used for the feedback path?
| What purpose does C\ :sub:`1`\ serve and what will happen if it were removed and why?
| Compare your distortion measurements for this circuit to what you measure for the previous two circuits. How much have the harmonics improved?
| |image3|

.. container:: centeralign

   Figure 9 Bipolar voltage input


**Return to the Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **:**

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/optocouplers_bb`
   


For Further Reading
~~~~~~~~~~~~~~~~~~~

| :adi:`MT-071 Analog Isolation Amplifiers <static/imported-files/tutorials/MT-071.pdf>`
| `Designing Linear Amplifiers Using the IL300 Optocoupler <https://www.vishay.com/docs/83708/appnote50.pdf>`_

**Return to Lab Activity:** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

Appendix:
---------

**Integrated optocouplers.**

Some models are in 6 pin packages and include a connection to the base terminal of the photo transistor. Others are in 4 pin packages and do not have base connections.

| FOD817 Series 4 pin photo transistor optocoupler from Fairchild Semi.
| Lite-On, Optocoupler DC-IN 1-CH Transistor DC-OUT 4-Pin PDIP (Avnet Part #:LTV-817)
| 4N25, 6 pin DIP package with Base terminal (Jameco Part no. 40985)
| 4N26, 6 pin DIP package with Base terminal (Jameco Part no. 41005)
| 4N28, 6 pin DIP package with Base terminal (Jameco Part no. 41013)
| 4N35, 6 pin DIP package with Base terminal (Jameco Part no. 41056)
| MCT6, MCT61,MCT62 dual photo transistor optocoupler from Fairchild Semi.

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/a22_drv_bb.JPG
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/a22_drv_wv.JPG
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/a22_f5.gif
   :width: 600px
