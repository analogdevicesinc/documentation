Activity: Bipolar Power Supplies for Active Learning Labs
=========================================================

Objective:
----------

The objective of this document is to explore a DC-DC converter topology for the generation of external bipolar power supply voltages to be used in conjunction with the ADALM1000 (M1k) or ADALM2000 (M2k) while performing Active Learning Lab activities where the built-in supplies (fixed 2.5 V and 5 V for M1k and +/-5V for M2k) may not provide the required supply voltage(s). The LT1054 Switched-Capacitor Voltage Converter in combination with an HPH1-1400L 6 winding transformer is used to generate up to +/- 10 V power supplies.

Note: Measuring Voltages Outside 0 to 5 V Range:
------------------------------------------------

To keep production cost of the ADALM1000 board low, certain tradeoffs were made. One was to forego programmable input gain ranges that use resistor dividers and perhaps adjustable frequency compensation capacitors. This is a problematic limitation of the ADALM1000 limiting the input voltage range from 0 to +5 V. Users will come up against this restriction when testing circuits powered by (generally larger) supply voltages other than the built in supplies.

.. important::

   \ **One quick note of caution before proceeding!**\


Before building any circuits that generate or operate from power supplies outside the native 0 to 5 V range of the ADALM1000 you need to protect the analog inputs when in Hi-Z or Split I/O modes and extend the usable range of voltages. There are large protection diodes connected between the analog I/O pins and ground and the internal +5 volt power supply which are generally reverse biased when the voltage on the pins is in the range of 0 to 5 V. If the voltage on the pin were to go more than a forward diode voltage beyond this range the diodes will possibly conduct large currents.

Full details on how to construct and calibrate external voltage dividers can be found in this document: :doc:`Measuring voltages beyond 0 to 5V with the ADALM1000 (M1K) </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>` **It is highly recommended that you read and follow this document before attempting any experiments on circuits powered by voltage outside 0 to 5 V.**

Background:
-----------

Forward mode DC-DC converters are used to provide galvanic isolation and voltage transformation. The Half-Bridge Forward configuration, shown in figure 1, converts a positive input voltage to a higher or lower, positive and negative output voltage. Energy from the input source is transferred to the output when the switch transistors are conducting. Note that in figure 1 the Input ground reference node need not be connected to the Output ground reference node providing galvanic isolation between the two sides of the transformer.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/bipolar-step-up-dc-dc-fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Half-Bridge Forward Converter


The LT1054 (supplied in the ADALP2000 Analog Parts kit) can provide the needed components of the half-bridge driver. Figure 2 show the internal block diagram. It contains the oscillator, non-overlapping switch drive circuit and upper and lower switch transistors at the CAP+ pin. The rest of the circuit components can be ignored for now.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/bipolar-step-up-dc-dc-fig2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2, LT1054 Internals


What is a forward-mode transformer?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a forward-mode transformer the core is not used for energy storage. The primary and secondary conduct simultaneously (and directly) when the switch is on, and energy is transferred directly through the transformer. This is different from a fly-back topology, in which energy is stored in the magnetic field of the transformer (inductor) during the first half of the conduction cycle and then released to the secondary winding(s) connected to the load in the second half of the cycle. Fly-back transformers require a specific magnetizing inductance and have a gapped-core construction, which allows high energy storage without saturating the core. Ideally, the forward-mode transformer has high (primary) magnetizing inductance, which serves to minimize the magnetizing current.

The HPH1-1400L (supplied in the ADALP2000 Analog Parts kit) is designed exclusively for use as a forward converter transformer.

Construction:
-------------

The internal oscillator of the LT1054 runs at a nominal frequency of 25 kHz. CAP+ (Pin 2) is alternately driven between V+ and ground. When driven to V+, Pin 2 sources current from V+. When driven to ground Pin 2 sinks current to ground. The relatively simple circuit for a forward mode DC-DC converter is shown in figure 3.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 - HPH1-1400L 6 winding transformer
| 1 - LT1054
| 2 - 1N4001 Diodes (D\ :sub:`1` and D\ :sub:`2`)
| 2 – 47 uF Capacitors (C\ :sub:`1` and C\ :sub:`2`)
| 1 – 220 uF Capacitor (C\ :sub:`3`)
| 1 – Optional +5 V DC output AC wall adapter (USB charger)

As shown in figure 3, the HPH1-1400L is wired as a 1:5 step-up transformer with one winding serving as the primary and the other 5 connected in series as the secondary. The CAP+ pin of the LT1054 drives one end of the primary with the other end of the primary connected to DC blocking capacitor C\ :sub:`3`. This single capacitor represents the parallel combination of C\ :sub:`1` and C\ :sub:`2` in figure 1. This insures that there will be no DC current in the transformer primary.

One end of the secondary is connected to ground. The other end is connected to D\ :sub:`1` and D\ :sub:`2` which half wave rectify the AC waveform to positive and negative DC output voltages. Caps C\ :sub:`1` and C\ :sub:`2` filter the half wave rectified outputs.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/bipolar-step-up-dc-dc-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, 1:5 Step-Up circuit.


For demonstration purposes here the circuit is powered from the internal fixed +5 V supply of the M1k. Optionally it could be powered from a +5 V DC output AC wall adapter (USB charger). The supply voltage operating range of the LT1054 is 3.5V to 15V (LT1054) and 3.5V to 7V (LT1054L) so other input supply voltages could be used.

**How much output voltage can we expect?**

We can expect the LT1054 switches, while un-loaded, to supply a maximum p-p voltage swing on the primary of 5 V. The step-up ratio of 1:5 should result in a maximum (un-loaded) p-p swing on the secondary of 25 V or a +12.5 V positive peak and -12.5 V negative peak. The forward voltage drop of the diodes will reduce each output voltage by 0.7 V to +11.8 V positive peak and -11.8 V negative peak.

The measured Vout using a DMM is 10.4 V when loaded with 2.7 kΩ resistors on both positive and negative outputs. The total load current is slightly less than 8 mA. Taking in to account the 1:5 step-up ratio, the average current in the primary supplied by the LT1054 is 40 mA. Looking at the voltage loss characteristics from the LT1054 datasheet, shown in figure 4, we can estimate that the potential 5 V p-p voltage swing will likely be reduced by 0.6 V at 25° C. The voltage swing loss seen in the secondary will be 5 X larger or 3.0 V (+1.5 and -1.5). Adding this extra voltage loss to the un-loaded peak outputs of +11.8 V and -11.8 V we get an estimated output voltage of +10.3 V and -10.3 V. These estimated voltages are consistent with the measured values.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/bipolar-step-up-dc-dc-fig4.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 4, Output Voltage Loss.


Example Use Case:
~~~~~~~~~~~~~~~~~

The ADTL082 Dual JFET Input Op-Amp (from the ADALP2000 Analog Parts Kit) requires a minimum of 8 V for its power supply. This minimum supply voltage is greater than the internal +5 V supplied by the M1k. While the full +/-5V range of the M2k internal user power supplies is large enough to turn on the ADTL082 the 10 V supply, minus the 3 V of total supply headroom required, may not be large enough for some experiments.

In order to use op-amps such as the ADTL082 in lab experiments with the M1k, higher supply voltages will be needed. The typical total supply current is only 2.4 mA (3.8 mA Max) and is well within the capabilities of this DC-DC converter.

Additional Materials:
^^^^^^^^^^^^^^^^^^^^^

| 1 – ADTL082 Dual Op-Amp
| 3 – 20 kΩ resistors
| 2 – 4.7 kΩ resistors
| 1 – 4.7 uF capacitor

Construct the example circuit shown in figure 5 on the breadboard next to the DC-DC converter in figure 3. The ADTL082 is powered from the generated +/- Vout voltages. The first of the two amplifiers is configured with a non-inverting gain greater than 1 (approx. 5) and the second amplifier is configured with an inverting gain of 1 with its input connect to the output of the first amplifier.

In order to measure the higher voltage outputs, two 470 K / 100 K voltage dividers are used. After :doc:`calibrating </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>` the software gain and offset settings for these dividers (gain will be approx. 6.12) we can test the circuit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/bipolar-step-up-dc-dc-fig5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Example test case.


To test the maximum available output swing using the generated +/- 10 V supplies a 4 V p-p 500 Hz sine wave from the channel A AWG output was applied to AC input coupling cap C\ :sub:`1`. The amplitude of the sine wave can be adjusted until the output signals just begin to clip (saturate). According to the ADTL082 datasheet the outputs should be able to swing to within 1.5 V of the power supply rails. The screen shot shown in figure 6 shows the amplifier outputs swinging to within less than 1.5 V of the generated +/- 10 V power rails.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/bipolar-step-up-dc-dc-fig6.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 6, Example test case.


Appendix: Alternate IC’s
========================

The ADM660 and MAX660 CMOS Switched Capacitor DC-DC converters share a similar pin out to the LT1054. The MOS switches in the ADM660 provide less voltage loss (0.3 V drop at 30 mA load) than the LT1054 and the higher 120 kHz switching frequency (80 KHz for MAX660) provides higher efficiency while allowing the use of smaller output filter capacitors.

Other pin compatible parts such as ICL7660 switch at much lower frequencies and are not suitable for use with the HPH1-1400L transformer but other lower frequency transformers could be substituted.

**Transformer Driver Integrated Circuits**

| :adi:`LT3439 DC/DC Transformer Driver <media/en/technical-documentation/data-sheets/3439fs.pdf>`
| `MAX253 DC/DC Transformer Driver <https://datasheets.maximintegrated.com/en/ds/MAX253.pdf>`__

**For Further Reading:**

| `Forward Mode Converters <https://en.wikipedia.org/wiki/Forward_converter>`__
| :adi:`ADM660 Datasheet <media/en/technical-documentation/data-sheets/ADM660_8660.pdf>`
| :adi:`LT1054 Datasheet <media/en/technical-documentation/data-sheets/1054lfh.pdf>`

**Return to Lab Activity Table of Contents**
