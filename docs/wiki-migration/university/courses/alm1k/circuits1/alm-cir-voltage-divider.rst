Activity: Frequency Compensated Voltage Dividers, For ADALM1000
===============================================================

Objective:
----------

The goal of this lab activity is to examine the issues of capacitive loading of resistive voltage dividers and the resulting effects on frequency response.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V, CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

A frequency compensated voltage divider or attenuator is a simple two-port RC network providing a fixed voltage division ratio or attenuation over a wide frequency range and not just at DC. Such networks are used where the part of the circuit loading the voltage divider output is capacitive. This particularly important when the signal has a wide bandwidth, that is, it is not sinusoidal. The simplest voltage attenuator is a purely resistive voltage divider with transfer function: H(jω) = V\ :sub:`2`/V\ :sub:`S` = R\ :sub:`2`/(R\ :sub:`1`\ +R\ :sub:`2`) where the input is V\ :sub:`S` = V\ :sub:`1`\ +V\ :sub:`2`, and the output is V\ :sub:`2`, as in figure 1. The transfer function of a resistive voltage divider is independent of frequency only if the resistors are ideal and any parasitic capacitances associated with the circuit are negligibly small.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-vdiv-f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1, simple resistor voltage divider


A problem seen at high frequencies is that stray (parasitic) capacitance effects with the overall response of a resistive voltage divider. The simplest way to correct for this problem is to introduce capacitors in parallel to the resistors. Consider the divider circuit in figure 2. Capacitor C\ :sub:`2` which is across the output, V\ :sub:`2`, can be thought of as any stray parasitic capacitance at the output of the divider that might be part of the system. We can see that this circuit, known as a frequency compensated divider, works like a resistive voltage divider at DC or low frequencies and like a capacitive voltage divider at high frequencies. Voltage dividers can be constructed from reactive components just as they can be constructed from resistors. Also as with resistor dividers, the divider ratio of a capacitive voltage divider is not affected by changes in the signal frequency even though the capacitor reactance is frequency dependent.

The divider ratio V\ :sub:`2`/V\ :sub:`S` = X\ :sub:`C2`/(X\ :sub:`C1`\ +X\ :sub:`C2`). The capacitive reactance X\ :sub:`C` is proportional to 1/C so V\ :sub:`2`/V\ :sub:`S` = C\ :sub:`1`/(C\ :sub:`1`\ +C\ :sub:`2`) is similar to the formula for the resistor divider. For the simple case where R\ :sub:`1` = R\ :sub:`2` we have a divider ratio of 1/2 for the resistors. To have the same 1/2 divider ratio for the capacitors C\ :sub:`1` = C\ :sub:`2`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-vdiv-f2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2, Frequency Compensated Divider


The compensated divider employs pole-zero cancellation to suppress undesired frequency dependence caused by any stray capacitance on the output side of the network. If the resistor and capacitor values are adjusted so that the pole and the zero of H(s) are superimposed, \|H(jω)\| becomes independent of frequency.

An instructive way to learn about the conditions for pole-zero cancellation is to write down the limiting, low and high frequency expressions for \|H(jω)\| and then to set them equal to each other. The result is a simple relationship between R\ :sub:`1`, R\ :sub:`2`, C\ :sub:`1`, and C\ :sub:`2`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-vdiv-f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, Showing (a) proper adjustment, (b) under compensation, (c) over compensation on the edges of a square wave.


Experiment to compensate for the input capacitance of the ALM1000
-----------------------------------------------------------------

.. note::

   The ADALM1000 (Rev. F version) has the ability to separate the voltage measurement connection from the voltage / current output pin, the Split I/O mode control in the AWG settings. The size of the parasitic capacitance is significantly different when using the CH A/B pins in Hi-Z mode vs using the AIN/BIN pins. The required external compensation capacitor value will be very different between the two pins.


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 – 1 MΩ resistor
| 1 – Capacitor, value to be determined

Directions:
~~~~~~~~~~~

Referring back to figure 2 we can consider R\ :sub:`2` to represent the 1 MΩ input resistance of the ALM1000 channels when in Hi-Z mode. Likewise, C\ :sub:`2` can be considered to represent the stray parasitic capacitance of the inputs. The resistor and capacitor inside the green box shown in figure 4. Use another 1 MΩ as R\ :sub:`1` to make a 1/2 divider ratio. Start without including C\ :sub:`1` to measure the effect on the frequency response due to C\ :sub:`2`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-vdiv-f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4, Voltage divider setup.


Procedure:
~~~~~~~~~~

Set AWG A to SVMI mode with the Min value set to 1.0 and Max value to 4.0. Set Shape to Square and the Frequency to 500 Hz. Set AWG B to Hi-Z mode. Under Curves select CA-V and CB-V to be displayed. Hit Run and adjust the horizontal time scale such that about 3 cycles are visible. You should see a sharp square wave on channel A and the waveform on channels B should look like the red curve (b) in figure 3. This is because C\ :sub:`1` has not yet been included. Estimate the RC time constant and the value of C\ :sub:`2` from the channel B waveform.

Open the Bode Plotting window. You can disable the time plot if you would like while generating the frequency response curves. Set AWG A Min value to 1.082 and the Max value to 3.92 (1 VRMS or 0 dBV). Check that the shape has been changed to Sine. Set the start frequency to 100 and the stop frequency to 20000. Select CH-A as the sweep source. Under curves select the CA-dBV, CB-dBV and CA-dB – CB-dB traces to be displayed. Under FFT Window using the Flat-top window works the best. Set the number of sweep point to 300 and Single sweep. Hit the Run button.

You should now have the gain (attenuation) ratio vs frequency response for the uncompensated divider. From the -3 dB point of the gain plot estimate the RC time constant and the value of C\ :sub:`2`. How do these values compare to what you calculated using the time domain response? Based on your best estimates for the value of C\ :sub:`2`, calculate a value for C\ :sub:`1` that will exactly compensate for C\ :sub:`2`. The value you come up with will probably not be close to a standard capacitor value. Find a parallel combination (or series combination) of two or more capacitors which closely adds up to the required value for C\ :sub:`1`.

Add your new C\ :sub:`1` combination across R\ :sub:`1` on the breadboard.

Repeat the Time domain and Frequency domain tests on this new circuit. Does the time domain response of the output of the divider now more closely resemble the blue waveform of (a) in figure 3? If not, why not? Compare the frequency response of the circuit before and after C\ :sub:`1` is added. What is the -3 dB frequency now?

Capacitor Divider path response:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's now take a look at just the capacitor divider path. Disconnect R\ :sub:`1` from the end of C\ :sub:`1` and connect it to the 2.5 V fixed supply as shown in figure 5. The path through just C\ :sub:`1` blocks the DC path from channel A. Connecting R\ :sub:`1` to the fixed 2.5 V supply restores the DC voltage level at the channel B input.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-vdiv-f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5, Just Capacitor Divider path


Repeat the Time domain and Frequency domain tests on this version of the circuit. Compare the time and frequency domain response of the circuit to what you obtained with just R\ :sub:`1` and with R\ :sub:`1` and C\ :sub:`1` connected in parallel (figure 4). What is the -3 dB frequency now? Is the frequency response flat, low pass or high pass? Explain why.

Using your divider to measure a 9 V battery:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We will now use the voltage divider to measure voltages larger than the 0 to +5 V allowed by the ALM1000 hardware. But first we need to calibrate the divider offset and gain.

Disconnect the end of R\ :sub:`1`,C\ :sub:`1` from channel A, figure 4, and connect them to ground. Set the value for the channel B gain to 2.0, the approximate divider ratio, for the moment. While monitoring the DC average of channel B, adjust the value entered in the channel B offset entry window.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-vdiv-s1.png
   :align: center
   :width: 300px

Now reconnect R\ :sub:`1`/C\ :sub:`1` back to channel A output. The channels A and B waveforms should now more closely align on top of each other. Adjust the gain value up or down slightly as needed such that the flat portions of the top and bottom of the square waves are right on top of each other. You might need to tweak the offset slightly as well to get perfect alignment. The software is now calibrated to the voltage divider.

Disconnect R\ :sub:`1`/C\ :sub:`1` from channel A. Connect the negative ( - ) terminal of the 9 V battery to ground and connect the positive (+) terminal to R\ :sub:`1`/C\ :sub:`1`. The DC average read by channel B should now be the DC voltage of the 9 V battery. You will need to change the channel B vertical range to 1 V/Div and the position to 5.0 to see the 9 volts on the scope grid.

Oscilloscope Probes:
~~~~~~~~~~~~~~~~~~~~

A 10X passive oscilloscope probe uses a series resistor (9 MΩ) to provide a 10:1 attenuation when it is used with the 1 MΩ input impedance of the scope itself. A 1 MΩ impedance is standard for most oscilloscope inputs This enables scope probes to be interchanged between oscilloscopes from different manufacturers. Figure 6 is the schematic for a typical 10X probe. 10X oscilloscope probes also include some amount of frequency compensation adjustment to allow for variations in the scope channel input capacitance. A capacitor divider network is designed into the probe as shown. The adjustable capacitor connected to ground can then be used to equalize the frequency response of the probe.

You can find more information on how to connect the scope probe BNC connector to your breadboard circuit or the inputs of the ALM1000: :ez:`Connect BNC Cables to Active Learning modules <adieducation/university-program/b/blogs/posts/simple-way-to-connect-bnc-cables-to-active-learning-modules>`

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-vdiv-f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6, Typical oscilloscope probe schematic


The input channels of the ALM1000 have a 1 MΩ input resistance but the input capacitance is much larger than the roughly 10 pF to 50pF adjustment range of most 10X probes. The capacitor in parallel with the 9 MΩ resistor is typically 10 pF and the parallel combination of the scope input capacitance and the adjustable compensation capacitor in the probe needs to be close to 90 pF. This means that if a standard probe were connected directly to the ALM1000 input it is not possible to compensate the frequency response.

A unity gain buffer amplifier (AD8541 or AD8542) can be inserted between the probe circuit and the ALM1000 input as shown in figure 7. R\ :sub:`1` and C\ :sub:`1` complete the resistor / capacitor divider circuit of the 10 X probe.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-cir-vdiv-f7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Insert a unit gain buffer to lower input capacitance.


With resistor R\ :sub:`1` connected to ground only positive voltages can be measured. If R\ :sub:`1` is connected to 2.5 V, middle of the 0 – 5V input range of the amplifier, an offset is injected and both positive and negative voltages can be measured.

\**For Further Reading: \*\*

| `Capacitive voltage divider <https://en.wikipedia.org/wiki/Voltage_divider#Capacitive_divider>`__
| `Oscilloscope Probes <http://www.radio-electronics.com/info/t_and_m/oscilloscope/oscilloscope-probes.php>`__
| `Building Your Own Oscilloscope Probes <http://cromwell-intl.com/radio/probes.html>`__
| :ez:`New Feature in ALICE Adds Input Divider Frequency Compensation <adieducation/university-program/b/blogs/posts/new-feature-in-alice-adds-input-divider-frequency-compensation>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
