Activity: The Emitter follower (BJT)
====================================

Objective:
----------

To investigate the simple NPN emitter follower amplifier also sometimes referred to as the common collector configuration.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 – 2.2KΩ Resistor ( RL )
| 1 – small signal NPN transistor ( 2N3904 Q\ :sub:`1` )

Directions:
-----------

The breadboard connections are shown in the diagram below. The output of the arbitrary waveform generator, W1, is connected to the base terminal of Q\ :sub:`1`. Scope input 1+ (Single Ended) is also connected to W1 output. The collector terminal is connected to the positive (Vp) supply. The emitter terminal is connected to both the 2.2 KΩ load resistor and Scope input 2+ (Single Ended). The other end of the load resistor is connected to the negative (Vn) supply. To measure the input to output error, channel 2 of the scope can be used differentially by connecting 2+ to the base of Q\ :sub:`1` and 2- to the emitter.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f1.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 1 Emitter Follower


Hardware Setup:
---------------

The waveform generator should be configured for a 1 KHz Sine wave with 4 volt amplitude peak-to-peak and 0 offset. The Single ended input of scope channel 2 (2+) is used to measure the voltage at the emitter. The Scope configured with channel 1+ connected to display the AWG generator output. When measuring the input to output error, channel 2 of the scope should be connected to display 2+ and 2- differential.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/emit_flw-bb.png

.. container:: centeralign

   Figure 2 Emitter Follower Breadboard Circuit


Procedure:
----------

|image1|

.. container:: centeralign

   Figure 3 Emitter Follower Waveforms


The incremental Gain (Vout / Vin) of the emitter follower should ideally be 1 but will always be slightly less than 1. The gain is generally given by the following equation:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_e1.png
   :align: center
   :width: 100px

From the equation we can see that in order to obtain a gain close to one we can either increase R\ :sub:`L` or decrease r\ :sub:`e`. We also know that r\ :sub:`e` is a function of I\ :sub:`E` and that as I\ :sub:`E` increases r\ :sub:`e` decreases. Also from the circuit we can see that I\ :sub:`E` is related to R\ :sub:`L` and that as R\ :sub:`L` increases I\ :sub:`E` decreases. These two effects work counter to each other in the simple resistive loaded emitter follower. Thus to optimize the gain of the follower we need to explore ways to either decrease r\ :sub:`e` or increase R\ :sub:`L` without effecting the other. Looking at the follower in another way, because of the inherent DC shift due to the transistor’s V\ :sub:`BE`, the difference between input and output should be constant over the intended swing. Due to the simple resistive load R\ :sub:`L`, the emitter current I\ :sub:`E` increases and decreases as the output swings up and down. We know that V\ :sub:`BE` is a (exponential) function of I\ :sub:`E` and will change approximately 18 mV (at room temperature) for a factor of 2 change in I\ :sub:`E`. In this +2V to -2V swing example the minimum I\ :sub:`E` = 2V/ 2.2KΩ or 0.91 mA to a maximum I\ :sub:`E` = 6V / 2.2KΩ or 2.7mA. This results in a 28 mV change in V\ :sub:`BE`. This observation leads us to the first possible improvement in the emitter follower. The current mirror from activity 5 is now substituted for the emitter load resistor to fix the amplifier transistor emitter current. A current mirror will sink a more or less constant current over a wide range of voltages. This more or less constant current flowing in the transistor will result in a more or less constant V\ :sub:`BE`. Viewed another way, the very high output resistance of the current source has effectively increased R\ :sub:`L` while r\ :sub:`e` remains at a low value set by the current.

Additional Materials:
---------------------

| 1 – 3.2KΩ Resistor ( use a 1KΩ in series with a 2.2KΩ )
| 1 – small signal NPN transistor ( Q\ :sub:`1` 2N3904)
| 2 – small signal NPN transistors ( Q\ :sub:`2`, Q\ :sub:`3` SSM2212) selected for best Vbe matching

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f3.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 4 Improved Emitter Follower


.. _hardware-setup-1:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/imp_emit_flw-bb.png

.. container:: centeralign

   Figure 5 Improved Emitter Follower Breadboard Circuit


.. _procedure-1:

Procedure:
----------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/imp_emit_flw-wave.png

.. container:: centeralign

   Figure 6 Improved Emitter Follower Waveforms


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 7 Input vs output error for resistor and current source load


Emitter follower output impedance
=================================

.. _objective-1:

Objective:
----------

An important aspect of the emitter follower is to provide power or current gain. That is to say drive a lower resistance (impedance) load from a higher resistance (impedance) source. Thus it is instructive to measure the emitter follower output impedance.

.. _materials-1:

Materials:
----------

| 1 – 4.7KΩ Resistor
| 1 – 10KΩ Resistor
| 1 – small signal NPN transistor ( Q\ :sub:`1` 2N3904)

.. _directions-1:

Directions:
-----------

The circuit configuration below adds a resistor R\ :sub:`2` to inject a test signal from AWG1 into the emitter (output) of Q\ :sub:`1`. The input, base of Q\ :sub:`1`, is grounded.


|image2|

.. container:: centeralign

   Figure 8 Output impedance test


.. _hardware-setup-2:

Hardware Setup:
---------------

The waveform generator should be configured for a 1 KHz Sine wave with 2 volt amplitude peak-to-peak with the offset set equal to minus the V\ :sub:`BE` of Q\ :sub:`1` ( approximately -0.65V ). This injects a +/- 0.1mA (1V/10KΩ) current into Q\ :sub:`1`\ ‘s emitter. Scope input 2+ measures the change in voltage seen at the emitter.


|image3|

.. container:: centeralign

   Figure 9 Output impedance test Breadboard Circuit


.. _procedure-2:

Procedure:
----------

|image4|

.. container:: centeralign

   Figure 10 Output impedance test Waveforms


Plot the change in voltage measured at the emitter. The nominal emitter current in Q\ :sub:`1` is (5V – 0.65) / 4.7KΩ or 925uA. We can calculate r\ :sub:`e`\ from this current as 26mV/925uA or 28Ω. How does this r\ :sub:`e` compare to the value measured from the test data? Change the value of R\ :sub:`1` from 4.7 KΩ to 2.2 KΩ and re-measure the output impedance of the circuit. How has it changed and why??

Low Offset Follower
===================

All the follower circuits we have investigated so far have a built in offset of –V\ :sub:`BE`. The circuit shown next uses the V\ :sub:`BE` shift up of a PNP emitter follower to partially cancel the V\ :sub:`BE` shift down of an NPN emitter follower.

.. _materials-2:

Materials:
----------

| 1 – 6.8KΩ Resistor
| 1 – 10KΩ Resistor
| 1 – 0.01uF Capacitor
| 1 – small signal PNP transistor ( Q\ :sub:`1` 2N3906)
| 3 – small signal NPN transistors ( Q\ :sub:`2`, Q\ :sub:`3`, Q\ :sub:`4` 2N3904 or SSM2212)

.. _directions-2:

Directions:
-----------

The breadboard connections are shown in the diagram below. The output of the function generator is connected to the base terminal of PNP transistor Q\ :sub:`1`. The collector terminal of Q\ :sub:`1` is connected to diode connected NPN Q\ :sub:`3` which is the input of a current mirror. The emitter terminal is connected to both resistor R\ :sub:`1`\ and the base terminal of NPN transistor Q\ :sub:`2`. Scope input 2+ is connected to both the emitter of Q\ :sub:`2` and the Collector of Q\ :sub:`4`. The emitters of both Q\ :sub:`3` and Q\ :sub:`4` are connected to the negative ( Vn ) supply. For best matching use the SSM2212 matched NPN pair for Q\ :sub:`3` and Q\ :sub:`4`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f7.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 11 Low offset follower


.. _hardware-setup-3:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/low_off_flw-bb.png

.. container:: centeralign

   Figure 12 Low offset follower Breadboard Circuit


The waveform generator should be configured for a 1 KHz Sine wave with 2 volt amplitude peak-to-peak with the offset set equal to 0. Scope input channel 2 is set to 500mV / Div.

.. _procedure-3:

Procedure:
----------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/low_off_flw-wav.png

.. container:: centeralign

   Figure 13 Low offset follower Waveforms


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 14


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 15


Driving a Capacitor
~~~~~~~~~~~~~~~~~~~

A problem suffered by the simple emitter follower can be seen when it drives a capacitive load. The rise time of the output can be relative fast as the emitter current is limited only by beta times the base current that can be supplied by the signal source driving the base. The fall time can be much slower and is limited by either the emitter resistor or current source.

.. _materials-3:

Materials:
----------

| 2 – 2.2KΩ Resistor
| 1 – 10KΩ Resistor
| 1 – 0.01uF Capacitor
| 3 – small signal PNP transistor (Q\ :sub:`2`, Q\ :sub:`3`, Q\ :sub:`4` 2N3906 SSM2220)
| 3 – small signal NPN transistors ( Q\ :sub:`1`, Q\ :sub:`5`, Q\ :sub:`6` 2N2904 SSM2212)
| The circuit shown here in figure 10 uses feedback to adjust the current in the emitter follower as the current in the load changes. The current to pull the output negative can be as much as N times (the gain of the NPN mirror) the current in PNP Q\ :sub:`3`. For best matching use the SSM2220 matched PNP pair for Q\ :sub:`3` and Q\ :sub:`4`\ and the SSM2212 matched NPN pair for Q\ :sub:`5` and Q\ :sub:`6`\ (NPN mirror gain will be 1, add a second SSM2212 in parallel with Q\ :sub:`5` to increase the mirror gain).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f10.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 16 Balanced slew rate follower


.. _hardware-setup-4:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/balanced_sr_flw-bb.png

.. container:: centeralign

   Figure 17 Balanced slew rate follower Breadboard Circuit


.. _procedure-4:

Procedure:
----------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/balanced_sr_flw-wav1.png

.. container:: centeralign

   Figure 18 Balanced slew rate follower Waveforms


.. image:: https://wiki.analog.com/_media/university/courses/electronics/balanced_sr_flw-wav2.png

.. container:: centeralign

   Figure 19 Balanced slew rate follower Waveforms


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f11.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 20


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f12.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 21


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f13.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 22


An alternate approach to improving the emitter follower is to reduce the effective r\ :sub:`e` through negative feedback. Reducing r\ :sub:`e` can be addressed by adding a second transistor to increase the negative feedback factor by increasing the open-loop-gain. The single transistor is replaced by a pair with 100% voltage feedback to the emitter of the first transistor. This is often referred to as a complementary feedback pair. The value of R\ :sub:`2` is crucial to good linearity, as it sets the I\ :sub:`C` of transistor Q\ :sub:`1`, and also determines its collector loading.

.. _materials-4:

Materials:
----------

| 1 – 2.2KΩ Resistor
| 1 – 10KΩ Resistor
| 1 – small signal NPN transistor ( 2N3904 Q\ :sub:`1` )
| 1 – small signal PNP transistor ( 2N3906 Q\ :sub:`2` )
| |image5|

.. container:: centeralign

   Figure 23 Complementary Feedback Pair Emitter Follower


.. _hardware-setup-5:

Hardware Setup:
---------------

|image6|

.. container:: centeralign

   Figure 24 Complementary Feedback Pair Emitter Follower Breadboard Circuit


.. _procedure-5:

Procedure:
----------

|image7|

.. container:: centeralign

   Figure 25 Complementary Feedback Pair Emitter Follower Waveforms


A minor addition to the complementary feedback pair emitter follower can provide a gain greater than 1. Resistor R\ :sub:`3` is added between the collector of PNP Q\ :sub:`2` and the emitter of NPN Q\ :sub:`1`. The output is now taken at the collector of Q\ :sub:`2`. The gain is approximated by the ratio of R\ :sub:`3` to R\ :sub:`1`, Gain = (R\ :sub:`1`\ +R\ :sub:`3`)/R\ :sub:`1`. In this example it is about 3.2.

.. _materials-5:

Materials:
----------

| 2 – 1KΩ Resistors
| 1 – 2,2KΩ Resistor
| 1 – small signal NPN transistor ( 2N3904 Q\ :sub:`1` )
| 1 – small signal PNP transistor ( 2N3906 Q\ :sub:`2` )

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f15.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 26 Follower with gain greater than 1


.. _hardware-setup-6:

Hardware Setup:
---------------

|image8|

.. container:: centeralign

   Figure 27 Follower with gain greater than 1 Breadboard Circuit


.. _procedure-6:

Procedure:
----------

|image9|

.. container:: centeralign

   Figure 28 Follower with gain greater than 1 Waveforms


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f16.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 29


In addition to the gain (or as a result of it) the DC level of the output is shifted positive as compared to the gain of 1 version. This limits the range of input voltage where the circuit can operate as shown by the negative shift in the input DC level. The next plot normalizes out the DC offset.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f17.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 30


To confirm that the gain is indeed about 3.2 the next plot divides the output by the gain and compares that to the input. In this example the actual gain is 3.16, most likely due to the resistor values not being exact.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f18.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 31


Questions:
----------

What limits the amount of gain greater than one that this circuit can produce?

What could be added to the circuit to remove / restore the DC levels at the input and output of this circuit?

What would happen if a diode connected NPN transistor were substituted for resistor R\ :sub:`2` (2.2KΩ)?

Current Limit or Constant Current (Transistor Based)
====================================================

This is a modification of the emitter follower to limit the current output. If the output stage of an amplifier is an emitter follower it may be necessary to limit the maximum current that can be supplied to the output load. Circuit:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f19.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 32 Emitter Current Limit


.. _hardware-setup-7:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/emit_curr_limit-bb.png

.. container:: centeralign

   Figure 33 Emitter Current Limit Breadboard Circuit


.. _procedure-7:

Procedure:
----------

|image10|

.. container:: centeralign

   Figure 34 Emitter Current Limit Waveforms


Where:

-   R\ :sub:`1` base resistor limits base current to transistor Q1.
-   R\ :sub:`2` current sense resistor used to sense the current and turn on transistor Q2.
-   R\ :sub:`3` Output Load.
-   Q\ :sub:`1` main transistor supplying the load current.
-   Q\ :sub:`2` current sense transistor.

Discussion:
-----------

The concept in this circuit is that R\ :sub:`2` acts as current sense resistor. When the load current times R\ :sub:`2`, the sense voltage, reaches about 0.6 (for silicon transistors ) Q\ :sub:`2` begins to conduct and increases current in R\ :sub:`1` which limits the base drive to Q\ :sub:`1`\ reducing its output current. The maximum current from the circuit is reached when I\ :sub:`L`\ \*R\ :sub:`2` = 0.6. This circuit can be used to protect amplifiers (including push pull amplifiers.), power supplies and other circuits; or it can be used as a constant current circuit. This is not a precision circuit; however it is a simple and effective circuit.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/bjt_emitter_ff_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/bjt_emitter_ff_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/emit_flw-wav.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f5.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/out_imp_test-bb.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/out_imp_test-wav.png
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/a11_f14.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/compl_fb_flw-bb.png
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/compl_fb_flw-wav.png
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/flw_gain_gr_one-bb.png
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/flw_gain_gr_one-wav.png
.. |image10| image:: https://wiki.analog.com/_media/university/courses/electronics/emit_curr_limit-wav.png
