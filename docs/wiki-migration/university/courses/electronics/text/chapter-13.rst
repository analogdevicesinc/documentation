Chapter 13: Transimpedance (Transresistance) frontends
======================================================

The differential pair we studied in chapter 12, in Bipolar or FET form, is the most popular input stage for what are most often referred to as voltage feedback amplifiers (VFB). They are characterized by having a relatively high input impedance at both the inverting and non-inverting input terminals. There is a second, alternate, type of input structure which is characterized by having a relatively low input impedance at the inverting input terminal and a high input impedance at the non-inverting input terminal. These amplifiers are often called transimpedance or transresistance amplifiers because they are inherently current to voltage converters (like a resistor or impedance). This low impedance current input stage leads to current feedback amplifiers (CFB). These amplifiers can be considered current controlled voltage sources (CCVS) in an ideal sense.

13.1 Current Feedback Amplifier Basics
--------------------------------------

The basic current feedback amplifier topology is shown in figure 13.1. Notice that within the model, a unity gain buffer connects the non-inverting input to the inverting input. In the ideal case, the output impedance of this buffer is zero (R\ :sub:`O` = 0), and the error signal is a small current, i, which flows into the inverting input. The error current, i, is mirrored into a high impedance, T(s), and the voltage developed across T(s) is equal to T(s)·i. (The quantity T(s) is generally referred to as the open-loop transimpedance gain.)

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr13-f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 13.1 Current Feedback (CFB) Op Amp Topology


.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr13-e1.png
   :align: center
   :width: 300px

Assume R\ :sub:`0` << R\ :sub:`1` and R\ :sub:`1`\ <= R\ :sub:`2` then:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr13-e2.png
   :align: center
   :width: 300px

At this point we are reminded that current feedback op amps are often called transimpedance op amps, because the open-loop transfer function is in fact an impedance as described above. However, the term transimpedance amplifier is often more correctly applied to more general circuits such as current-to-voltage (I/V) converters, where either CFB or VFB op amps can be used. Therefore, some caution is warranted when the term transimpedance is encountered in a given situation. On the other hand, the term current feedback op amp is rarely confused and is the preferred nomenclature when referring to this op amp topology.

From this simple model, several important CFB op amp characteristics can be deduced.

• Unlike VFB op amps, CFB op amps do not have balanced inputs. Instead, the non-inverting input is high impedance, and the inverting input is low impedance.

• The open-loop gain of CFB op amps is measured in units of O (transimpedance gain) rather than V/V as for VFB op amps.

• For a fixed value feedback resistor R\ :sub:`2`, the closed-loop gain of a CFB can be varied by changing R\ :sub:`1`, without significantly affecting the closed-loop bandwidth. This can be seen by examining the simplified equation in figure 13.1. The denominator determines the overall frequency response; and if R\ :sub:`2` is constant, then R\ :sub:`1` of the numerator can be changed (thereby changing the gain) without affecting the denominator-hence the bandwidth remains relatively constant.

The CFB topology is primarily used where the ultimate in high speed and low distortion is required. The fundamental concept is based on the fact that in bipolar transistor circuits currents can be switched faster than voltages, all other things being equal.

Figure 13.2 shows a simplified schematic of an example of an early IC CFB op amp, the AD846-introduced by Analog Devices in 1988. Notice that full advantage is taken of a complementary bipolar (CB) process which provides well matched PNP and NPN transistors.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr13-f2.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 13.2: Current Feedback Op Amp (AD846 Cir. 1988)


Transistors Q\ :sub:`1`-Q\ :sub:`2` buffer the non-inverting input (pin 3) and drive the inverting input (pin 2). Q\ :sub:`5`-Q\ :sub:`6` and Q\ :sub:`7`-Q\ :sub:`8` act as current mirrors that drive the high impedance node. The C\ :sub:`COMP` capacitor provides the dominant pole compensation; and Q\ :sub:`9`, Q\ :sub:`10`, Q\ :sub:`11`, and Q\ :sub:`12` comprise the output buffer. In order to take full advantage of the CFB architecture, a high speed complementary bipolar (CB) IC process is generally required. With modern IC processes, this is readily achievable, allowing direct coupling in the signal path of the amplifier.

13.2 Differences Between CFB And VFB Op Amps
--------------------------------------------

One primary difference between the CFB and VFB amps is that the CFB amplifier does not have a constant gain-bandwidth product. While there is a small change in bandwidth with gain, it is much less than the 6 dB/octave we see with a VFB op amp. This is shown in figure 13.4. As previously mentioned, the bandwidth of a CFB op amp is proportional to the feedback resistor. For every CFB op amp there is a recommended value of feedback resistor for maximum bandwidth. If you increase the value of the resistor beyond this value, you reduce the bandwidth. If you use a lower value of resistor below this value, the phase margin is reduced, and the amplifier may become unstable.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr13-f3.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 13.4 Current Feedback Amplifier Frequency Response


Gain is manipulated in a CFB op amp application by choosing the correct feedback resistor for the device (R\ :sub:`2`), and then selecting the bottom resistor (R\ :sub:`1`) to yield the desired closed loop gain. The gain relationship of R\ :sub:`2` and R\ :sub:`1` is identical to the case of a VFB op amp. The optimum feedback resistor may be different for different operational conditions. For instance, the value will change for different package types because of the variation in parasitic capacitances. Figure 13.5 shows the optimum feedback resistor for the AD8001 op amp for various gains for the PDIP, SOIC, and SOT-23 packages.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr13-f4.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure 13.5: AD8001 Optimum Feedback Resistor vs. Package


Also, a CFB amplifier should not have a capacitor in the feedback loop. If a capacitor is used in the feedback loop, it reduces the net feedback impedance at higher frequencies, which will cause the op amp to oscillate. Stray capacitance on the inverting input will cause a similar effect and should be minimized by etching away the ground plane around this terminal.

A common error in using a current feedback op amp is to connect the inverting input directly to the output in an attempt to build a unity gain voltage follower (buffer). This circuit will oscillate because the equivalent feedback resistor value is zero. The follower circuit can be stabilized by simply connecting the inverting input to the output using the recommended feedback resistor value.

Another difference between the VFB and CFB amplifiers is that the inverting input impedance of the CFB amp is low (typically 50 O to 100 O), while the non-inverting input impedance is high (typically several hundred kO). Therefore, the inputs of the CFB amp are not balanced, as is the case with VFB amps.

Slew rate performance is also enhanced by the CFB topology. The current that is available to charge and discharge the internal compensation capacitor is available on demand. It is not limited to a fixed value as is often the case in VFB topologies. With a step input, the current is increased (current-on-demand) until the feedback loop is stabilized. The basic current feedback amplifier has no fundamental slew-rate limit. Limits only come about from parasitic internal capacitances, and many strides have been made to reduce their effects.

The combination of higher bandwidths and slew rate allows CFB devices to have good distortion performance, while doing so at a lower power.

The distortion of an amplifier is affected by the open loop distortion of the amplifier and the loop gain of the closed-loop circuit. The amount of open-loop distortion contributed by a CFB amplifier is small due to the basic symmetry of the internal topology. High bandwidth is the other main contributor to low distortion. In most configurations, a CFB amplifier has a greater bandwidth than its VFB counterpart. So at a given signal frequency, the faster part has greater loop-gain and therefore lower distortion. There are, however, certain voltage feedback structures (often referred to as "quad core" or "H-Bridge") which approach the performance levels of CFB and provide "current on demand" when designed on similar processes.

Section Summary: Current Feedback (CFB) VS. Voltage Feedback (VFB)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The application advantages of current feedback and voltage feedback differ. In many applications, the differences between CFB and VFB are not readily apparent. Today's CFB and VFB amplifiers have comparable performance, but there are certain unique advantages associated with each topology. Voltage feedback allows freedom of choice of the feedback resistor (or network) at the expense of sacrificing bandwidth for gain. Current feedback maintains high bandwidth over a wide range of gains at the cost of limiting the choices in the feedback impedance.

| In general, VFB amplifiers offer:
| • Lower Noise
| • Better dc Performance
| • Feedback Component Freedom

| while CFB amplifiers offer:
| • Faster Slew Rates
| • Lower Distortion
| • Feedback Component Restrictions

**ADALM2000 Lab Activity 12A,** :doc:`Transimpedance input stage </wiki-migration/university/courses/electronics/electronics-lab-12a>`

**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/chapter-12>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-14>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`
