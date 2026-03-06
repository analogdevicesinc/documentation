Techniques To Increase Signal Generator Output Voltage, Part 1:
===============================================================

Objective:
----------

The objective of this document is to present various techniques that can be used to increase the output voltage available from a Personal Test Instrument signal generator or AWG.

Cautionary Note:
----------------

Performing tests on circuits that generate, operate at, or use high voltages present a significant shock hazard and great care should be taken while working with such systems.

Motivation:
-----------

Even the most well equipped labs with large budgets may not have the exact right instrument for a particular test or measurement. What do you do in this situation if there isn’t money or time to obtain the right equipment? There are a number of things that can contribute to a buy, adapt or make trade-off.

Background:
-----------

While one can investigate most fundamental principles in Electrical Engineering with circuits / components that only need 5V to operate, there are times where certain components and IC's require higher voltages. Can this be done only using USB powered personal instruments like ADALM1000 (M1k) / ADALM2000 (M2k)?

Personal test instruments (USB based data acquisition systems) generally support voltages in the +5 V to -5 V range for signal generation, signal measurement and power supplies. Some may provide built-in resistor dividers that extend the input voltage measurement range to as much as +/- 25V for the M2k. However, an external resistor voltage divider can be used to extend any instrument’s input voltage measurement capability beyond its specified design range such as using a 10X passive scope probe. Note this document on :doc:`how to extend the voltage range </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>` of the M1k. On the signal generation side it is not so simple. AC testing of electronic systems often requires a low-distortion signal source to excite a DUT (device under test) from a signal generator to produce a large enough low-distortion AC signal.

The Step-Up Transformer
-----------------------

A very simple, yet often overlooked, way to increase the voltage of an AC signal is by using a step-up transformer. While the voltage seen on the output (secondary) side of the transformer is indeed higher than the input (primary) side there is no free lunch. Transformers are passive devices in that they are not powered by an external power source. The power delivered to the load cannot exceed the power supplied at the primary. That is if the voltage is stepped up the current is stepped down. Power out equals the power in only in an ideal transformer. In a real transformer the output power will be less than the input power due to resistive losses in the windings.

Transformer Limitations
~~~~~~~~~~~~~~~~~~~~~~~

There are a number of things to keep in mind when considering the use of a transformer to step-up the output voltage of a signal generator.

-  Transformers only pass AC signals while blocking any DC component of the signal. This is a high pass filter function and the minimum usable frequency is highly dependent on the construction of the transformer. Generally, the lower the minimum frequency the larger the transformer.
-  Transformers have an upper frequency limit. Transformers have mainly a band-pass frequency response. The width of the usable pass band again largely depends on the construction of the magnetic core and the windings. The limited band-pass nature of the transformer frequency response can distort more complex waveform shapes.
-  Transformers have a maximum power rating. The size of the magnetic core and the diameter of the wire used in the coils generally determine the maximum power rating. Transformers with higher power ratings will have lower DC winding resistance (DCR).

::

   * 

We now take a look at some candidate transformers that might be used in a voltage step-up mode for increasing the voltage swing.

Audio Transformers
~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/hv-awg-part1-fig1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1, Typical Audio Signal Transformers


A selection of typical audio transformers is listed in table 1. The DC resistance of the two windings is listed along with the voltage step up ratio. Lastly the open circuit peek-to-peek voltage in a step up configuration is listed for an input p-p voltage of 5 V.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/hv-awg-part1-tab1.png
   :align: center
   :width: 800px

Even a 1:1 transformer can be used to double the voltage swing of a signal when connected in the auto-transformer configuration. Note how the secondary winding is connected to stack its voltage on top of the signal on the primary paying particular attention the winding polarity dots in figure 2..

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/hv-awg-part1-fig2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2, Auto Transformer Configuration


AC Power Transformers
~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-2.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 3, Typical AC-AC Wall Transformer


A selection of AC power transformers is listed in table 2. The DC resistance of the two windings is listed along with the voltage step down (up) ratio. Lastly the open circuit peek-to-peek voltage in a step up configuration is listed for an input p-p voltage of 5 V.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/hv-awg-part1-tab2.png
   :align: center
   :width: 800px

While the AC voltage on the secondary is often used directly with one of the secondary terminals referenced to ground or common, a DC offset can be introduced, as in figure 4, by connecting the secondary to a DC voltage source or power supply. Another option would be to rectify the AC output voltage using a diode bridge as shown in figure 5.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/hv-awg-part1-fig4.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 4, DC Offset Introduced.


.. image:: https://wiki.analog.com/_media/university/courses/tutorials/hv-awg-part1-fig5.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 5, Using a Bridge Rectifier


Example Use Case
~~~~~~~~~~~~~~~~

Can you light a small neon lamp, which generally requires more than 100 V to turn on, using only a USB powered personal instrument, like M1k or M2k, and passive (i.e. unpowered) components?

The experimental configuration using the M1k hardware is shown in figure 6, where a 1:15 step-up transformer (Audio #4 from Table 1) is used to magnify the 10 p-p differential signal generated by using the two AWG channels in a bridged push-pull configuration. The magnified secondary voltage is then applied to the first half of a single Dickson voltage doubler consisting of a 1N4006 high voltage rectifier diode and three 0.56 uF high voltage capacitors in parallel (1.5uF) to shift (DC restore) the voltage waveform to only positive values of approximately 0 to 145 V. A 41:1 voltage divider consisting of two 220 K resistors in series (440 K) and two 22 K resistors in parallel (11 K) attenuates the waveform so it can be monitored by the 0-5 V input range of the M1k.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/hv-awg-part1-fig6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, M1k connections


Figure 7 is an ALICE screen shot showing the current and voltage waveforms driving a single neon lamp. The green trace is the CH A drive voltage (500 Hz tri wave) used for triggering and reference. The brown and darker cyan reference traces show the high voltage and AWG drive current without the neon lamp in circuit. The orange and cyan traces are with the lamp in circuit. You can see clearly in the voltage and current traces where the lamp turns on (around 113 V) and the current jumps above the reference base line and where it extinguishes (around 70 V). The big negative current spike is when the diode turns on and recharges the capacitor.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/hv-awg-part1-fig7.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 7, M1k test waveforms


Performing the same experiment using the M2k hardware is shown next in figure 8. Both AWG channels are used in parallel to drive the primary side of the transformer. The two 50Ω resistors inside the blue dashed box represent the internal series resistors in the M2k AWG channels. Both channels are configured with identical waveforms, shape, frequency, amplitude, offset and phase. This effectively lowers the source resistance to 25Ω and boosts the effective voltage and current that is applied to the transformer. Otherwise the experimental setup is the same. (Inputs 1- and 2- assumed to be grounded). The maximum voltage swing achievable is about 15V lower due to losses in the 25Ω source resistance.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/hv-awg-part1-fig8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, M2k connections


The same 41:1 voltage divider is used to attenuate the high voltage waveform. With the M2k input dividers set in the “high gain” mode (0.5V/div) the input voltage range is +/- 2.5 V which can be offset to 0 to +5V in the software by setting the vertical position controls.

Figure 9 is a Scopy screen shot showing the voltage waveforms driving a single neon lamp. The orange trace is the drive voltage (500 Hz tri wave) seen on the transformer primary and is used for triggering and reference. The purple trace is the raw voltage seen at the 41:1 resistor divider and the green math trace is the scaled high voltage waveform. The M2k lacks a current measurement channel so it is more difficult to see where the lamp turns on and where it extinguishes. There is a noticeable jump in the voltage trace when the lamp turns on.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/hv-awg-part1-fig9.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 9, M2k test waveforms


Appendix:
---------

Audio Transformer Specs 42TL Series Transformers, Maximum output 75 mW.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/hv-awg-part1-tab3.png
   :width: 400px

42TM Series, Maximum output: 200mW

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/hv-awg-part1-tab5.png
   :width: 700px

42TU Series, Maximum output: 460mW

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/hv-awg-part1-tab6.png
   :width: 400px

**For Further Reading:**

`LT3080 power oscillator <https://www.edn.com/test-ideas-produce-ac-test-signals/>`__
