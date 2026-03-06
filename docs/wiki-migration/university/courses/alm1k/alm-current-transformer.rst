Activity: The Current Transformer
=================================

Objective:
----------

Transformers have three uses or, more precisely, can provide three types of transformation: Voltage, Current and Impedance. Of course, these are related, but, ideally, they have different frequency dependence. In this lab activity the transformer will be explored as a means to scale or transform (AC) current.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

The ALM1000's SMU channels can measure DC currents from -200mA to +200mA. Because of the 100 KSPS sampling rate it can actually measure AC currents as well. But the current to be measured has to be flowing into or out of the SMU channel. This limits the range of voltages that the current must be "referenced" to, 0 to +5V. To measure current over a wider range of voltages a current shunt monitor IC like the AD8210 from the ADALP2000 Analog Parts kit can be used.

The ALM1000 SMU channels use this same integrated circuit to measure the current. The operating input common-mode voltage range of the AD8210 is −2 V to +65 V with respect to the ground pin of the IC. A larger voltage range but still not enough to safely measure the current of a household appliance or lighting fixture operating from 120 V AC. So what can we use to do that? Enter the Current Sense Transformer, CST.

Transformers have three uses or, more precisely, can provide three types of transformation: Voltage, Current and Impedance. Of course, these are related, but, ideally, they have different frequency dependence. Current transformers only work when the secondary is behaving like an inductor, with little loss.

The current sense transformer is specifically optimized or designed to produce an alternating current in the secondary winding which is proportional to the alternating current being "sensed" or measured in the primary winding. Like any transformer, current transformers isolate the measuring of currents in high voltage circuits to a much lower voltage and provide a convenient way of safely monitoring the actual electrical current flowing in a high voltage AC power line. In our case the monitoring equipment could be the SMU of the ALM1000.

The principal of operation of a basic current transformer is slightly different from that of an ordinary voltage transformer. Unlike a power transformer used to step up or down voltages, the current transformer often consists of only one or a few turns as the primary winding. The secondary winding supplies a current into either a short circuit, in the form of an ammeter, or into a low value resistive load until the voltage induced in the secondary is big enough to saturate the core. The secondary load of a current transformer is termed the "burden" to distinguish it from the primary load. Unlike a voltage transformer application the goal is to have the primary current of a current sense transformer not depend on the secondary current but instead is determined by an external load.

This primary winding can be of either a single flat turn, a coil of heavy duty wire wrapped around the core or just a wire inserted through a central hole like that shown in the photo of a clamp-on current probe transformer, (model LCTC-0250) figure 1. With this current "probe" the jaws open so that it can be clamped around the conductor carrying the current to be measured without having to disconnect the conductor. Current probes such as this are designed for use in 50/60 Hz AC power applications. The LCTC-0250 probe has a current measuring range up to 100 Amps and a built-in current to voltage (burden) resistor so the output voltage is specified as 15mV/A.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-fig1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1, Clamp-on Current Transformer, model LCTC-0250


Phase shift:
~~~~~~~~~~~~

Ideally we want the primary and secondary currents of a current transformer to be in phase. In practice, this is not possible, but, at normal power line frequencies, phase shifts of a few tenths of a degree are achievable, at high frequencies CTs may have phase shifts up to six degrees. For average and RMS current measurements the phase shift does not factor in the measurement as ammeters only display the magnitude of the current. However, for power, energy, and power factor (real power vs reactive power) measurements, phase shift produces errors. For power and energy measurements, the errors can be considered to be negligible at unity power factor but become more significant as the power factor approaches zero. At zero power-factor, any indicated power is entirely due to the current transformer's phase error. The introduction of electronic power and energy meters has allowed current phase error to be calibrated out.

Testing the concept:
--------------------

We can use the 6 winding coils from the ADALP2000 Parts kit to examine the basic concepts of using a transformer as a current sensor. Normally we would like the turns ratio to be some large number like 100 or 200 but we can still see the relationship of the primary and secondary current with a smaller ratio like 1:5 available using these 6 winding coils.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less Breadboard
| Jumper wires
| 1 - HPH1-1400L 202 uH 6 winding coil
| 1 - HPH1-0190L 27 uH 6 winding coil
| 1 – 6.2 ohm power resistor

Directions:
~~~~~~~~~~~

Wire the HPH1-1400L 6 winding coil as a 1:5 transformer as shown in figure 2 taking careful note of the winding polarity indicated by the dots. The single winding primary winding is driven by AWG channel A through the 6.2 Ω power resistor, RL. SMU channel B is used as a ground referenced ammeter to load the five winding secondary while measuring the current.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, 1:5 current transformer


Hardware Settings:
~~~~~~~~~~~~~~~~~~

Set AWG channel A Shape to sine with the Min value set to 1.5 and the Max value set to 3.5. The Min setting should not set lower or the Max value set higher than these values to insure that the current sourced by the output does not exceed +/- 200 mA (1.3 V / 6.2 ohms). Set the frequency initially to 1000 Hz. AWG channel B should be set to Shape DC with the Max value set to 0. Select the CA-V, CA-I CB-V and CB-I traces to be displayed.

Procedure:
~~~~~~~~~~

Figure 3 is a screen capture of the current and voltage waveforms. We can see that the primary current, CHA-I, is 301 mA p-p, 106 mA RMS and the secondary current, CHB-I, is 60 mA p-p, 21 mA RMS. The ratio of the primary current to the secondary current is 5:1 as we would expect.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, 1:5 current transformer waveforms


Now replace the HPH1-1400L 202 uH six winding coil with the HPH1-0190L 27 uH six winding coil. How has the secondary current ratio changed? Increase the Channel A frequency to 10000 Hz. Does the higher frequency affect the secondary current?

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-fig4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, HPH1-0190L current transformer waveforms at 1KHz


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-fig5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, HPH1-0190L current transformer waveforms at 10KHz


How does the coil inductance factor into the phase error between the primary and secondary currents?

Testing a higher turns ratio:
-----------------------------

We can potentially make a higher turns ratio CT by wrapping a single turn of wire around one of the inductors from the Parts Kit. In figure 6 we show the LTspice simulation schematic of this using a 10 mH coil as the secondary winding. In the simulation we can adjust the primary inductance and the mutual inductance coupling factor to model the real circuit from figure 7

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-fig6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6 Simulation schematic


.. _materials-1:

Materials:
~~~~~~~~~~

| 2.5 inches of solid core jumper wire
| 1 – 10 mH inductor
| 1 – 10 uH inductor
| 1 – 1 uH inductor
| 1 – AC coupling capacitor, any combination greater than 2200 uF
| 1 – 1 KΩ resistor
| 1 – AD8542 dual R-R op-amp (or AD8541 single op-amp)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-fig7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, breadboard connections


In this circuit we use the op-amp to create a virtual short across the secondary coil and us a relatively higher value resistor in the feedback of the amplifier to convert the coil current into a voltage. Other inductors from the Parts Kit can be used to produce other possible turns ratios.

Appendix:
---------

Commercial current sense transformers:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many manufacturers make a range of current sense inductors that are a toroidal coil with a hole in the center that the user passes a wire (or loops of wire) through to sense the AC current, figure A1. Depending on the particular model and the specification these types of current transformers are designed for use in switch mode power supply control systems and operate over a frequency range from 20 kHz to 200 kHz. The PE-51718 center tapped 100 turn 20 mH version is shown. The size, excluding the leads, is 20mm tall x 11mm wide x 10mm deep which is small enough to fit on a solder-less breadboard.

The nice thing about using coil like this as a sense transformer is that you can choose any number of turns you want for the primary. Up to when the center hole is filled based on the gauge of the wire used.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-figa1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure A1, Pulse Engineering Center tapped 100:1 20 mH example


A current transformer with a built-in primary winding from CoilCraft is shown in figure A2. Since it is totally encapsulated, we can't tell how it is constructed. The design frequency range for this 200:1, 80 mH example is from 1 KHz to 1 MHz.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-figa2.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure A2, CoilCraft 200:1 80 mH example CS4200V-01


In figure A3 we have a surface mount current sense transformer from Würth Elektronik. In this example the primary winding is simply the wide metal strap that goes up and around the central secondary winding. The manufacturer specifies the inductance for this 200:1, 20 mH example at 10 KHz so it probably is also not designed for lower frequency power line applications.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-figa3.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure A3, Würth Elektronik 200:1 20 mH example from MID-SNS Family


To test these current transformers the ALM1000 and the test circuit shown in figure A4. A 4 V peak-peak sine wave signal is generated by the channel A AWG. The signal is then AC coupled through a large capacitor to the 10 ohm load resistor which converts the voltage into a 400 mA peak to peak current. The current is sensed by the primary winding which is connected to ground. On the secondary side the 100 ohm burden resistor is connected across the coil winding and the resulting voltage is measured by channel B in Hi-Z mode. The other end of the coil is referenced to the fixed 2.5 V rail to center it in channel B's input range.

For the clamp-on probe and the PE coil one of the longer wire jumpers from the Analog Parts kit is inserted through the center hole to use as the primary.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-figa4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A4, Frequency Bandwidth test circuit using M1K


The input frequency is swept from 20 Hz to 1 KHz in all the following tests. The first bode plot is for the LCTC clamp probe with a single wire through the clamp. Remember that the clamp has a built-in burden so the 100 ohm external resistor was not included for this test case. The magnitude response is very flat, within a dB down to 20 Hz.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-figa5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A5, LCTC current probe bode plot


Next up is the PE-51718. As we see the response below 1 KHz is not at all flat which is to be expected given the 20 KHz minimum frequency specification. The lighter set of curves are for one wire as primary and the darker set is for 4 turns as the primary.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-figa6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A6, PE-51718 bode plot


Next we have the CoilCraft CS4200V-01 and Würth Elektronik 750316796 examples. Both are 200:1 turns ratio. The darker curves are for the 80 mH CoilCraft device and the lighter curves are for the 20 mH Würth device. As expected the higher inductance of the CoilCraft device gives the better low frequency response. The CoilCraft device meets and exceeds its 1 KHz minimum frequency specification and the Würth device is probably only flat above a few KHz using this value of burden resistor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-figa7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A7, CoilCraft CS4200V-01 and Würth Elektronik 750316796 bode plot


Electronic Burden, I to V converter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One way to improve the frequency response of any current transformer is to replace the resistive burden with an electronic solution, i.e. an op-amp I to V conversion circuit. The single supply rail-rail AD8541 CMOS op-amp is used as an I to V converter as shown in figure A8. The virtual ground at the summing junction, pin 2, presents a very low impedance load on the secondary. The 1K feedback resistor converts the current into a voltage that is measured by channel B at pin 6.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-figa8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A8, Op-amp I to V converter circuit


To test the frequency response using the op-amp the CoilCraft CS4200V-01 (dark trace) and Würth 750316796 (light trace) are again compared in figure A9. Note the vertical scale is now 3 dB/div. There is a huge improvement in the flatness of the response compared to figure A7 with less than a dB of roll off at 60 Hz. The CoilCraft response is now about as flat as the LCTC current probe in figure A5.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-figa9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A9, CoilCraft CS4200V-01 and Würth 750316796 op-amp I to V bode plot


Making real world measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a real world example let's use the model LCTC-0250 clamp-on current sensor we saw in the first figure and the M1k to measure the current waveform of an LED Holiday light string. The LCTC-0250 probe has a built-in current to voltage (burden) resistor so the output voltage is specified as 15mV/A. The string consists of 35 white LEDs in series. About a foot of the wire was untwisted and one leg was wrapped about 5 times around the clamp. The sensitivity should be about 75 mV/A ( 5 \* 15 mV/A ).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-figa12.png
   :align: center
   :width: 600px

The probe is connected directly to the input of an M1k without any additional amplification or filtering. As you can see in figure A10 the current is simple 1/2 wave rectification and the peak current is between 35 and 45 mA. Hard to see exactly with the noise and the signal is too small to trigger on properly and apply trace averaging.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-figa10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A10, Current waveform without any signal processing


By applying some mathematical wizardry we are able to clean up the noise and make the "signal" big enough (by 10X) to trigger on and use trace averaging. A simple 20 tap box car digital filter with an overall gain of 10 is applied to the captured waveform trace and trace averaging is used (set to average 8). The waveform is nice and clean now and the p-p current is 42 mA.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-current-transformer-figa11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A11, filtered current waveform


\*\* For Further Reading:\*\*

`Simulating Non-linear Transformers in LTspice <https://www.allaboutcircuits.com/technical-articles/simulating-non-linear-transformers-in-ltspice/>`__

**Return to Power Lab Activity** :doc:`Table of Contents </wiki-migration/university/labs/power>`
