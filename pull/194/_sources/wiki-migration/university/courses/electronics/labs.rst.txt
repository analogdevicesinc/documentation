ADALM2000 Based Lab Activity Material, Electronics I and II
===========================================================

Analog Devices is as passionate about educating the next generation of young circuit design engineers as it is about pioneering the next technological breakthrough. The University Program is a platform where Analog Devices, working with leading educational institutions has created and deployed new hands on learning tools for the next generation of analog circuit design engineers. The University Program brings the analog signal processing technology the company has developed to the academic community in a way that is open and accessible to faculty and students in the form of analog design kits and analog components, online and downloadable software and teaching materials, online support, textbooks, reference designs and lab projects to enrich students’ education about analog circuits and their application to core engineering and physical science curricula.

The laboratory activities provided on this wiki are considered open source and available for free use in non-commercial educational and academic settings. **The only requirement is that they continue to retain the attribution to Analog Devices Inc.** Supplying them on the ADI wiki allows registered users to contribute to the materials posted here improving the content and keeping them up to date.

In general these labs can be performed using the :doc:`ADALM2000 </wiki-migration/university/tools/m2k>` (M2K) Active Learning Module and :doc:`Scopy </wiki-migration/university/tools/m2k/scopy>` software. It is also possible to perform these lab activities using the ADALM1000 (M1K) hardware module with minor adjustments to the circuits. :doc:`This document </wiki-migration/university/courses/alm1k/m2k-convert-labs>` outlines how the labs might be altered for use with M1K and the ALICE desktop software.

They are generally written to be performed with just the components provided in the :doc:`ADALP2000 </wiki-migration/university/tools/adalp2000/parts-index>` Analog Parts Kit, however additional devices are sometimes needed. Other sources of components can of course be used and there is additional information on that further down on this page. If you are looking for Lab Activity material written specifically for use with the :doc:`ADALM1000 look here </wiki-migration/university/courses/alm1k/alm-labs-list>`.

Most of the labs are populated with :adi:`LTSpice <en/design-center/design-tools-and-calculators/ltspice-simulator.html>` resource files which contain the schematics of the circuits discussed at a specific topic. An file containing the ADALM2000 connections for the schematics can be found here: :git-education_tools:`m2k/ltspice/m2k_conn_ltspice`.

Pre-Lab Circuit Simulation
--------------------------

| Notes on :doc:`circuit simulation </wiki-migration/university/courses/electronics/circuitsimulationnotes>`.
| Links to an archive of example simulation schematic files are provided below.

General Lab materials
---------------------

-  Background Lab Notes: :doc:`Solder-less Breadboards </wiki-migration/university/courses/electronics/electronics-lab-breadboards>`
-  Background Lab Activity: :doc:`Solder-less Breadboard Parasitic Capacitance </wiki-migration/university/courses/electronics/electronics-lab-breadboard-coupling>`
-  Background Lab Notes: :doc:`Resistors </wiki-migration/university/courses/electronics/electronics-lab-resistors>` (including color code)
-  Background Lab Notes: :doc:`Capacitors </wiki-migration/university/courses/electronics/electronics-lab-capacitors>` (including color code)
-  Review Activity: :doc:`Real voltage sources </wiki-migration/university/courses/electronics/electronics-lab-0>`
-  Basic Activity: :doc:`Energy Harvesting </wiki-migration/university/courses/electronics/electronics-lab-eh>`

Electronics I
-------------

Electronics I pre-lab simulation :git-education_tools:`schematic files <m2k/adisimpe/electronics-lab-i>`.

-  :doc:`An Ohm's Law Experiment </wiki-migration/university/courses/electronics/ohm_law>`
-  :doc:`Transient Response of an RC Circuit </wiki-migration/university/courses/electronics/rc_transient_response>`
-  :doc:`Transient Response of an RL Circuit </wiki-migration/university/courses/electronics/rl_transient_response>`
-  :doc:`Low Pass and High Pass Filters </wiki-migration/university/courses/electronics/lp_hp_filters>`
-  :doc:`Band Pass Filters </wiki-migration/university/labs/band_pass_filters_adalm200>`
-  :doc:`Band Stop Filters </wiki-migration/university/labs/band_stop_filters_adalm2000>`
-  :doc:`Resonance in RLC Circuits </wiki-migration/university/courses/electronics/rlc_resonance>`
-  :doc:`Cascaded RC low pass filters </wiki-migration/university/labs/cascaded_rc_adalm2000>`
-  :doc:`Simple Op Amps </wiki-migration/university/courses/electronics/electronics-lab-1>`,\ :doc:`Op Amp as Comparator </wiki-migration/university/courses/electronics/electronics-lab-opamp-comparator>`,\ :doc:`Op Amp Settling Time </wiki-migration/university/courses/electronics/electronics-lab-1st>`, :doc:`Measuring Loop Gain </wiki-migration/university/courses/electronics/electronics-lab-loop-gain>`
-  :doc:`PN Diode I/V curves </wiki-migration/university/courses/electronics/electronics-lab-2>`
-  :doc:`Voltage dependent capacitance of the PN junction </wiki-migration/university/courses/electronics/electronics-lab-pn-junction-cap>`
-  :doc:`Differential Temperature Sensor </wiki-migration/university/courses/electronics/electronics-lab-25>`
-  :doc:`Zener diode regulator </wiki-migration/university/courses/electronics/electronics-lab-26>`
-  :doc:`BJT as a diode </wiki-migration/university/courses/electronics/electronics-lab-3>`, :doc:`MOS as a diode </wiki-migration/university/courses/electronics/electronics-lab-3m>`
-  Device I/V curves, :doc:`BJT </wiki-migration/university/courses/electronics/electronics-lab-4>` and :doc:`MOS </wiki-migration/university/courses/electronics/electronics-lab-4m>`
-  :doc:`Common emitter amplifier </wiki-migration/university/courses/electronics/electronics-lab-5>`, :doc:`Common source amplifier </wiki-migration/university/courses/electronics/electronics-lab-5m>`, :doc:`Amplifier Frequency Response </wiki-migration/university/courses/electronics/electronics-lab-5fr>`, :doc:`CE amplifier loop gain </wiki-migration/university/courses/electronics/electronics-lab-ce-loop-gain>`
-  :doc:`BJT Current Mirror </wiki-migration/university/courses/electronics/electronics-lab-6>`, :doc:`MOS Current Mirror </wiki-migration/university/courses/electronics/electronics-lab-6m>`
-  :doc:`BJT Zero gain amplifier </wiki-migration/university/courses/electronics/electronics-lab-7>`, :doc:`MOS Zero gain amplifier </wiki-migration/university/courses/electronics/electronics-lab-7m>`
-  :doc:`BJT Stabilized current source </wiki-migration/university/courses/electronics/electronics-lab-8>`, :doc:`MOS Stabilized current source </wiki-migration/university/courses/electronics/electronics-lab-8m>`
-  :doc:`Floating (two terminal) Current Source / Sink </wiki-migration/university/courses/electronics/electronics-lab-8a>`
-  :doc:`Regulated Voltage Reference </wiki-migration/university/courses/electronics/electronics-lab-9>`
-  :doc:`Shunt voltage regulator </wiki-migration/university/courses/electronics/electronics-lab-10>`
-  :doc:`BJT Emitter follower </wiki-migration/university/courses/electronics/electronics-lab-11>`, :doc:`MOS source follower </wiki-migration/university/courses/electronics/electronics-lab-11m>`
-  :doc:`BJT Differential Pair </wiki-migration/university/courses/electronics/electronics-lab-12>`, :doc:`MOS Differential Pair </wiki-migration/university/courses/electronics/electronics-lab-12m>`, :doc:`Transresistance input stage </wiki-migration/university/courses/electronics/electronics-lab-12a>`
-  :doc:`Differential pair triangle to sine converter </wiki-migration/university/courses/electronics/electronics-lab-12sg>`
-  :doc:`Making a full Amplifier from circuit blocks </wiki-migration/university/courses/electronics/electronics-lab-13>`. :doc:`Output Stages </wiki-migration/university/courses/electronics/electronics-lab-13a>`

Electronics II
--------------

Electronics II pre-lab simulation :git-education_tools:`schematic files <m2k/adisimpe/electronics-lab-ii>`.

-  :doc:`CMOS Amplifier </wiki-migration/university/courses/electronics/electronics-lab-20>` (with chopping / auto zero)
-  :doc:`CMOS Analog Switches </wiki-migration/university/courses/electronics/electronics-lab-18>`
-  :doc:`Switched Capacitor circuits </wiki-migration/university/courses/electronics/electronics-lab-19>`
-  :doc:`Analog to Digital </wiki-migration/university/courses/electronics/electronics-lab-adc>` and :doc:`Digital to Analog </wiki-migration/university/courses/electronics/electronics-lab-14>` Conversion
-  :doc:`Delta – Sigma Modulator </wiki-migration/university/courses/electronics/electronics-lab-17>`
-  :doc:`CMOS LC Oscillator </wiki-migration/university/courses/electronics/electronics-lab-21>`
-  :doc:`Light Controlled RC Oscillator </wiki-migration/university/courses/electronics/electronics-lab-lco>`
-  :doc:`Optocouplers </wiki-migration/university/courses/electronics/electronics-lab-22>` ( analog isolation amplifier )
-  :doc:`Silicon Controlled Rectifiers </wiki-migration/university/courses/electronics/electronics-lab-scr>`
-  :doc:`Active Rectifiers </wiki-migration/university/courses/electronics/electronics-lab-32>`
-  :doc:`DC-DC Converters I </wiki-migration/university/courses/electronics/electronics-lab-15>` ( inductors )
-  :doc:`DC-DC Converters II </wiki-migration/university/courses/electronics/electronics-lab-16>` ( capacitors )
-  Multivibrators, :doc:`NPN </wiki-migration/university/courses/electronics/electronics-lab-24>` and :doc:`NMOS </wiki-migration/university/courses/electronics/electronics-lab-24m>`
-  :doc:`TTL inverter and NAND gate </wiki-migration/university/courses/electronics/electronics-lab-27>`
-  :doc:`Build CMOS Logic Functions Using CD4007 Array </wiki-migration/university/courses/electronics/electronics-lab-28>`
-  :doc:`CMOS Logic Circuits, Transmission Gate XOR </wiki-migration/university/courses/electronics/electronics-lab-30>`
-  :doc:`CMOS Logic Circuits, D Type Latch </wiki-migration/university/courses/electronics/electronics-lab-29>`
-  :doc:`Logic Voltage Level Shifting </wiki-migration/university/courses/electronics/electronics-lab-voltage-level-shifter>`
-  :doc:`Phase locked loops </wiki-migration/university/courses/electronics/electronics-lab-31>`

Miscellaneous Lab Activities
----------------------------

-  :doc:`LED as light sensor </wiki-migration/university/courses/electronics/electronics-lab-led-sensor>`
-  :doc:`Characteristics of Photovoltaic Solar Cells </wiki-migration/university/courses/eps/photovoltaic>`
-  :doc:`Negative voltage reference from positive reference </wiki-migration/university/courses/electronics/electronics-lab-nr>`
-  :doc:`Measuring a Loudspeaker Impedance Profile </wiki-migration/university/courses/electronics/electronics-lab-speaker>`
-  :doc:`Adjustable External Triggering Circuit </wiki-migration/university/courses/electronics/electronics-lab-external-trigger>`
-  :doc:`Heartbeat Measurement Circuit </wiki-migration/university/courses/electronics/electronics-lab-heartbeat>`
-  :doc:`Temperature Control using Window Comparator </wiki-migration/university/courses/electronics/electronics-lab-window-comp-tmp01>`
-  :doc:`Magnetic proximity sensor </wiki-migration/university/courses/electronics/magnetic_proximity_sensor>`
-  :doc:`2-Axis Tilt Sensor </wiki-migration/university/labs/2_axis_tilt_sensor_adalm2000>`
-  :doc:`IC temperature sensors </wiki-migration/university/courses/electronics/temperature_measuring>`
-  :doc:`Audio Amplifier with Electret Microphone </wiki-migration/university/courses/electronics/electronics-lab-electret_microphone>`

Communications Circuits
-----------------------

-  :doc:`Inductor Self Resonance </wiki-migration/university/labs/comms_lab_isr_adalm2000>`
-  :doc:`Transformers </wiki-migration/university/labs/comms_lab_transformers_adalm2000>`
-  :doc:`Tuned Amplifiers,part I </wiki-migration/university/labs/comms_lab_tuned_amplifiers_1_adalm2000>`, :doc:`Tuned Amplifiers,part II </wiki-migration/university/labs/comms_lab_tuned_amplifiers_2_adalm2000>`
-  :doc:`Transformer Coupled Amplifier </wiki-migration/university/labs/electronics_lab_transformer_coupled_amp_adalm2000>`
-  :doc:`Active Filters </wiki-migration/university/courses/electronics/electronics-lab-active-filter>`, :doc:`Polyphase Filters </wiki-migration/university/courses/electronics/comms-lab-polyphase-filter>`
-  :doc:`Envelope Detectors </wiki-migration/university/courses/electronics/electronics-lab-envelope-detector>`
-  :doc:`FM Detectors </wiki-migration/university/courses/electronics/electronics_lab_fm_detectors>`
-  :doc:`Variable Gain Amplifiers </wiki-migration/university/courses/electronics/electronics-lab-variable-gain-amplifier>`
-  :doc:`Pulse Width Modulation </wiki-migration/university/courses/electronics/electronics-lab-pulse-width-modulation>`
-  Frequency Synthesizers, :doc:`Hartley oscillator </wiki-migration/university/courses/electronics/comms-lab-hartley-osc>`, :doc:`Colpitts oscillator </wiki-migration/university/courses/electronics/comms-lab-colpitts-osc>`, :doc:`Clapp oscillator </wiki-migration/university/courses/electronics/comms-lab-clapp-osc>`, :doc:`Peltz Oscillator </wiki-migration/university/courses/electronics/comms-lab-peltz-osc>`
-  :doc:`The Wien Bridge Oscillator </wiki-migration/university/labs/wien_bridge_osc_adalm2000>`
-  :doc:`Pulsed Oscillators </wiki-migration/university/courses/electronics/comms-lab-pulse-osc>`
-  :doc:`Diode Ring Modulators </wiki-migration/university/courses/electronics/electronics_lab_diode_ring_modulator>`
-  :doc:`Active Mixers </wiki-migration/university/courses/electronics/electronics-lab-active-mixer>`
-  :doc:`Pseudo-Random Sequence Generators </wiki-migration/university/courses/electronics/comms-lab-lfsr>`
-  :doc:`Transmission Lines and Standing Waves </wiki-migration/university/labs/tlines_standing_waves_adalm2000>`

Power Management Circuits
-------------------------

-  :doc:`Switched Capacitor Power Supplies </wiki-migration/university/courses/electronics/switched-cap-power-supplies>`
-  :doc:`Buck Converter Basics </wiki-migration/university/courses/electronics/buck_converter_basics>`
-  :doc:`Efficiency, Power Loss, and Thermal Management </wiki-migration/university/courses/electronics/efficiency_power_loss>`
-  :doc:`Boost and Buck converter elements and open-loop operation </wiki-migration/university/labs/open_loop_boost_and_buck_adalm2000>`
-  :doc:`Buck Converters: closed loop operation </wiki-migration/university/labs/closed_loop_buck_adalm2000>`
-  :doc:`Boost Converters: closed loop operation </wiki-migration/university/labs/closed_loop_boost_adalm2000>`

Tutorials
---------

-  :doc:`ADALM2000 Tutorials </wiki-migration/university/courses/electronics/tutorials>` *(temporary link)*

General background Information.
===============================

The assumption is made that the reader has some familiarity with the ADALM2000 Lab hardware and Scopy software system before starting these lab activities. It is also assumed that for the data presented here, the measurement data waveforms from the lab hardware were saved to disk and manipulated and plotted in Microsoft Excel.

First, here are a few words about components that might be suitable for use in these lab experiments. Transistors that can be used are general purpose NPN types like 2SC1815 and the 2SA1015 PNP complement. Similar type devices can be used such as the popular 2N3904 NPN and 2N3906 PNP devices which are also considered comparable complements of each other. A supply of various diodes, resistors, capacitors and inductors should also be available. Another potential source of transistors for use in these lab exercises are transistor arrays such as the LM3045 / LM3046 / LM3086 NPN Arrays from National Semiconductor. Similar NPN arrays from Intersil are, CA3045 / CA3046 / CA3083. Arrays of two or four 2N2222, 2N3904, 2N3906 and other types are available from some manufacturers like Fairchild and ON Semiconductor. A readily available enhancement mode NMOS transistor is the 2N7000. Advanced Linear Devices Inc. offers dual and quad N and P channel MOS arrays (ALD1106 and ALD1107) as well. The CD4007C CMOS logic package consists of three complementary pairs of N and P-channel enhancement mode MOS transistors. The N and P type pairs share either a common gate or common drain terminal which limits their use as six individual devices but these devices can still be useful for Lab experiments.

Remember, not all transistors share the same terminal designations, or pinouts, even if they share the same physical appearance. The order of some types is CBE (base is center lead) and BCE (collector is center lead) for others. This is very important when you connect the transistors together and to other components. Be careful to check the manufacturer's specifications (component datasheet). These can be easily found on various websites. Double-checking pin identities with a multi-meter's "diode check" function is highly recommended.

Extra stuff:
============

Learning to mathematically analyze circuits requires much study and practice. Typically, students practice by working through lots of sample problems and checking their answers against those provided by the textbook or the instructor. While this is good, there is a much better way. You will learn much more by actually building and analyzing real circuits, letting your test equipment provide the "answers" instead of a book or another person. For successful circuit-building exercises, follow these steps:

1. Carefully measure and record all component values prior to circuit construction, choosing resistor values high enough to make damage to any active components unlikely.

2. Draw the schematic diagram for the circuit to be analyzed. Or perhaps print out the schematics shown in these lab activities.

3. Carefully build this circuit on your breadboard.

4. Before applying power to your circuit check the accuracy of the circuit's construction, following each wire to each connection point, and verifying these elements one-by-one on the diagram.

5. Mathematically analyze the circuit, solving for all voltage and current values.

6. Carefully measure all voltages and currents, to verify the accuracy of your analysis.

7. If there are any substantial errors (greater than a few percent), carefully check your circuit's construction against the diagram, then carefully re-calculate the values and re-measure.

One way you can save time and reduce the possibility of error is to begin with a very simple circuit and incrementally add components to increase its complexity after each analysis, rather than building a whole new circuit for each practice activity. Another time-saving technique is to re-use the same components in a variety of different circuit configurations. This way, you won't have to measure any component's value more than once.

Note about diodes and bandgap conventions:
==========================================

The common convention is that a typical silicon BJT base–emitter diode drop, ``VBE``, is 0.65V and a standard general purpose silicon diode drop is 0.6V. Other conventions use 0.6V or 0.7V for one or both. These are highly dependent on the manufacturing process used and the physical size of the components. The results you measure in the laboratory will most likely be between these values. Diodes and BJTs implemented on the same integrated circuit (i.e., on the same silicon die) may have equivalent characteristics. That is, the diodes and transistors will be more closely matched. Matched components are convenient to use in many circuit designs. We use discrete elements in most of these activities, and so it is not possible to match components unless they are all fabricated on the same silicon die. In the laboratory, a diode-connected transistor, with its base shorted to its collector may match the base–emitter characteristics of another transistor of the same type better than a simple diode.

Diode drops are strongly temperature dependent. Room-temperature transistors (~27ºC or 300ºK) have base–emitter drops around 0.65V, but as the temperature of the transistors increases, ``VBE`` drops near 0.5V. So temperature matching is just as important as component matching. Internal temperature compensation in bandgap voltage references lets them provide a temperature-independent voltage reference. Their output reference of ∼1.22V is the extrapolated ``VBE`` at absolute zero (i.e., 0ºK or −273.15ºC). It is not a coincidence that the Silicon bandgap (i.e., the energy separating valence and conduction electron bands) is ∼1.22 eV.

Temperature dependence and manufacturing variations (and the Early effect) are always a concern.

**Return to Electronics Text** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`
