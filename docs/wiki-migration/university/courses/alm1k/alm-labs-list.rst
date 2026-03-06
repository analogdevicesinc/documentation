ADALM1000 Based Lab Activity Material, Electronics I and II
===========================================================

Analog Devices is as passionate about educating the next generation of young circuit design engineers as it is about pioneering the next technological breakthrough. The Active Learning Program is a platform where Analog Devices, working with leading educational institutions has created and deployed new hands on learning tools for the next generation of analog circuit design engineers. This University Program brings the analog signal processing technology the company has developed to the academic community in a way that is open and accessible to faculty and students in the form of analog design kits and analog component kits, online and downloadable software and teaching materials, online support, textbooks, reference designs and lab projects to enrich students’ education about analog circuits and their application to core engineering and physical science curricula.

The laboratory activities provided on these wiki pages are considered open source and available for free use in non-commercial educational and academic settings. **The only requirement is that they continue to retain the attribution to Analog Devices Inc.** Supplying them on the ADI wiki allows registered users to login and contribute to the materials posted here improving the content and keeping them up to date.

In general these example labs are based on the :doc:`ADALM1000 </wiki-migration/university/tools/m1k>` (M1K) entry level design hardware and the accompanying :doc:`ALICE Desk-Top </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` software package. It is also possible to perform these lab activities using the ADALM2000 (M2K) hardware module with minor adjustments to the circuits. :doc:`This document </wiki-migration/university/courses/alm1k/m2k-convert-labs>` outlines how the labs might be altered for use with M2K.

They are generally written to be performed using just the components provided in the Analog Parts Kit, :doc:`ADALP2000 </wiki-migration/university/tools/adalp2000/parts-index>`, supplied through ADI distribution channels, however additional devices are sometimes needed. Other sources of components can of course be used and there is additional information on that further down on this page.

Pre-Lab Circuit Simulation
--------------------------

| Notes on :doc:`circuit simulation </wiki-migration/university/courses/electronics/circuitsimulationnotes>`.
| Links to an archive of example simulation schematic files are provided below.

General Lab materials
---------------------

-  Background Lab Notes: :doc:`Solder-less Breadboards </wiki-migration/university/courses/electronics/electronics-lab-breadboards>`
-  Background Lab Notes: :doc:`Resistors </wiki-migration/university/courses/electronics/electronics-lab-resistors>` (including color code)
-  Background Lab Notes: :doc:`Capacitors </wiki-migration/university/courses/electronics/electronics-lab-capacitors>` (including color code)
-  Review Activity: :doc:`Rechargeable Batteries </wiki-migration/university/courses/alm1k/alm-lab-e1>`
-  :doc:`Measuring voltages beyond 0 to 5V with the ADALM1000 (M1K) </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>`
-  :doc:`How to Generate External Signal Sources </wiki-migration/university/courses/alm1k/circuits1/alm-cir-signal-generators>`
-  :doc:`Battery Voltage "Rail-Splitter" </wiki-migration/university/courses/alm1k/circuits1/alm_cir_lab-rail-splitter>`

Electronics I
~~~~~~~~~~~~~

Electronics I pre-lab simulation `schematic files <https://wiki.analog.com/_media/university/courses/electronics/electronics-lab-i.zip>`__.

-  :doc:`Basic OP Amp Configurations </wiki-migration/university/courses/alm1k/alm-lab-1>`
-  :doc:`Op-Amp Open-Loop Gain </wiki-migration/university/courses/alm1k/alm-lab-olg>`
-  :doc:`Op-Amp Gain Bandwidth Product </wiki-migration/university/courses/alm1k/alm-lab-gbw>`
-  :doc:`The Voltage Comparator </wiki-migration/university/courses/alm1k/alm-lab-comp>`
-  :doc:`PN Diode </wiki-migration/university/courses/alm1k/alm-lab-2>` and :doc:`Zener Diode </wiki-migration/university/courses/alm1k/alm-lab-zener-diode>` I/V curves
-  :doc:`Diode Rectifiers </wiki-migration/university/courses/alm1k/circuits1/alm-cir-diode-rectifier>`
-  :doc:`Precision Rectifiers, Absolute value circuits </wiki-migration/university/courses/alm1k/circuits1/alm-cir-precision-rectifier>`
-  :doc:`The voltage dependent capacitance of the PN junction </wiki-migration/university/courses/alm1k/alm-lab-2pnj>`
-  :doc:`BJT as a diode </wiki-migration/university/courses/alm1k/alm-lab-3>`, :doc:`MOS as a diode </wiki-migration/university/courses/alm1k/alm-lab-3m>`
-  Device I/V curves, :doc:`BJT </wiki-migration/university/courses/alm1k/alm-lab-4>` and :doc:`MOS </wiki-migration/university/courses/alm1k/alm-lab-4m>`
-  Transistor as a switch, :doc:`BJT </wiki-migration/university/courses/alm1k/alm-lab-4s>` and :doc:`MOS </wiki-migration/university/courses/alm1k/alm-lab-4ms>`
-  :doc:`Common Emitter Amplifier </wiki-migration/university/courses/alm1k/alm-lab-5>`, :doc:`Common Source Amplifier </wiki-migration/university/courses/alm1k/alm-lab-5m>`, :doc:`Frequency Response of CE amplifier </wiki-migration/university/courses/alm1k/alm-lab-ce-freq-resp>`
-  :doc:`Common Base Amplifier </wiki-migration/university/courses/alm1k/alm-lab-cb>`, :doc:`Common Gate Amplifier </wiki-migration/university/courses/alm1k/alm-lab-cg>`
-  :doc:`Folded Cascode Amplifier </wiki-migration/university/courses/alm1k/alm-lab-fca>`
-  :doc:`BJT Current Mirror </wiki-migration/university/courses/alm1k/alm-lab-6>`, :doc:`MOS Current Mirror </wiki-migration/university/courses/alm1k/alm-lab-6m>`
-  :doc:`BJT Zero Gain Amplifier </wiki-migration/university/courses/alm1k/alm-lab-7>`, :doc:`MOS Zero Gain Amplifier </wiki-migration/university/courses/alm1k/alm-lab-7m>`
-  :doc:`BJT Stabilized current source </wiki-migration/university/courses/alm1k/alm-lab-8>`, :doc:`MOS Stabilized current source </wiki-migration/university/courses/alm1k/alm-lab-8m>`
-  :doc:`Regulated Voltage Reference </wiki-migration/university/courses/alm1k/alm-lab-9>`
-  :doc:`Shunt Voltage Regulator </wiki-migration/university/courses/alm1k/alm-lab-10>`
-  :doc:`BJT Emitter Follower </wiki-migration/university/courses/alm1k/alm-lab-11>`, :doc:`MOS Source Follower </wiki-migration/university/courses/alm1k/alm-lab-11m>`
-  :doc:`Phase Splitter Amplifier </wiki-migration/university/courses/alm1k/alm-lab-phase-split>`
-  :doc:`BJT Differential Pair </wiki-migration/university/courses/alm1k/alm-lab-12>`, :doc:`MOS Differential Pair </wiki-migration/university/courses/alm1k/alm-lab-12m>`
-  :doc:`Multi Stage Amplifier </wiki-migration/university/courses/alm1k/alm-lab-mstageamp>`.
-  :doc:`Making a full Amplifier from circuit blocks </wiki-migration/university/courses/alm1k/alm-lab-13>`. :doc:`Output Stages </wiki-migration/university/courses/alm1k/alm-lab-13a>`

Electronics II
~~~~~~~~~~~~~~

Electronics II pre-lab simulation `schematic files <https://wiki.analog.com/_media/university/courses/electronics/electroincs-lab-ii.zip>`__.

-  :doc:`Pulse Width Modulator </wiki-migration/university/courses/alm1k/alm-lab-pwm>`
-  :doc:`CMOS Amplifier </wiki-migration/university/courses/alm1k/alm-lab-20>`
-  :doc:`Two stage CMOS OTA </wiki-migration/university/courses/alm1k/alm-lab-ota>`
-  :doc:`CMOS Analog Switches </wiki-migration/university/courses/alm1k/alm-lab-18>`
-  :doc:`CMOS LC Oscillator </wiki-migration/university/courses/alm1k/alm-lab-21>`
-  :doc:`Light Controlled RC Oscillator </wiki-migration/university/courses/alm1k/alm-lab-lco>`
-  :doc:`Voltage Controlled RC Oscillator </wiki-migration/university/courses/alm1k/alm-lab-vco>`
-  :doc:`Optocouplers </wiki-migration/university/courses/alm1k/alm-lab-22>` ( analog isolation amplifier )
-  :doc:`Silicon Controlled Rectifiers </wiki-migration/university/courses/alm1k/alm-lab-scr>`
-  :doc:`Low Drop out Linear Voltage Regulators </wiki-migration/university/courses/alm1k/alm-ldo-lab>`
-  :doc:`DC-DC Converters I </wiki-migration/university/courses/alm1k/alm-lab-15>` ( inductors )
-  :doc:`DC-DC Converters II </wiki-migration/university/courses/alm1k/alm-lab-16>` ( capacitors )

Digital Electronics
-------------------

-  Multivibrators, :doc:`NPN </wiki-migration/university/courses/alm1k/alm-lab-24>` and :doc:`NMOS </wiki-migration/university/courses/alm1k/alm-lab-24m>`
-  :doc:`TTL inverter and NAND gate </wiki-migration/university/courses/alm1k/alm-lab-27>`
-  :doc:`Build CMOS Logic Functions Using CD4007 Array </wiki-migration/university/courses/alm1k/alm-lab-28>`
-  :doc:`CMOS Ring Oscillator </wiki-migration/university/courses/alm1k/alm-lab-ring-osc>`
-  :doc:`CMOS Ring Oscillator Frequency Multiplier </wiki-migration/university/courses/alm1k/alm-lab-ring-3x>`
-  :doc:`CMOS Logic Circuits, Transmission Gate XOR </wiki-migration/university/courses/alm1k/alm-lab-30>`
-  :doc:`CMOS Logic Circuits, D Type Latch </wiki-migration/university/courses/alm1k/alm-lab-29>`
-  :doc:`Logic Voltage Level Shifting </wiki-migration/university/courses/alm1k/alm-lab-voltage-level-shifter>`

Miscellaneous Lab Activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`LED as light sensor </wiki-migration/university/courses/alm1k/alm-lab-led-sensor>`
-  :doc:`Photo Voltaic Solar Cells </wiki-migration/university/courses/alm1k/alm-lab-pv>`
-  :doc:`Electret microphone preamplifier </wiki-migration/university/courses/alm1k/alm-lab-s1>`
-  :doc:`Heart Rate Monitor Circuit </wiki-migration/university/courses/alm1k/alm-lab-heart-rate-mon>`

Power Management Lab Activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`Low Drop out Linear Voltage Regulators </wiki-migration/university/courses/alm1k/alm-ldo-lab>`
-  :doc:`Efficiency, Power Loss, and Thermal Management </wiki-migration/university/courses/alm1k/alm-power-efficiency>`
-  :doc:`Inductor DC-DC Converters I </wiki-migration/university/courses/alm1k/alm-lab-15>`
-  :doc:`DC-DC Boost Converters </wiki-migration/university/courses/alm1k/circuits1/alm-cir-15a>`
-  :doc:`Switched Capacitor Power Supplies </wiki-migration/university/courses/electronics/switched-cap-power-supplies>`
-  :doc:`Capacitor DC-DC Converters II </wiki-migration/university/courses/alm1k/alm-lab-16>`
-  :doc:`Buck Converter Basics </wiki-migration/university/courses/electronics/buck_converter_basics>`
-  :doc:`Simple "Joule Thief" DC/DC Converter </wiki-migration/university/courses/alm1k/circuits1/alm-joule-thief>`
-  :doc:`Active Rectifiers </wiki-migration/university/courses/alm1k/alm-active-rectifiers>`
-  :doc:`Electronic Circuit Breakers </wiki-migration/university/courses/alm1k/alm-circuit-breaker>`

Communications Circuits
~~~~~~~~~~~~~~~~~~~~~~~

-  Inductor Self Resonance
-  :doc:`Transformers </wiki-migration/university/courses/alm1k/alm-lab-transformers>`
-  Tuned Amplifiers,part I, Tuned Amplifiers,part II
-  Transformer Coupled Amplifiers
-  Active Filters, Polyphase Filters
-  :doc:`AM modulation and Envelop Detectors </wiki-migration/university/courses/alm1k/circuits1/alm-cir-envelope-detector>`
-  FM Detectors
-  Variable Gain Amplifiers
-  :doc:`Pulse Width Modulation </wiki-migration/university/courses/alm1k/alm-lab-pwm>`
-  Frequency Synthesizers, :doc:`Hartley oscillator </wiki-migration/university/courses/alm1k/alm-lab-hartley-osc>`, Colpitts oscillator, Clapp oscillator, Peltz Oscillator
-  Pulsed Oscillators
-  Phase Locked Loops
-  Diode Ring Modulators
-  Active Mixers
-  Pseudo-Random Sequence Generators

General background Information.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The assumption is made that the reader has some familiarity with the ADALM1000 Lab hardware and ALICE software system before starting these lab activities. It is also assumed that for the data presented here, the measurement data waveforms from the lab hardware were saved to disk and manipulated and plotted in Microsoft Excel.

First, here are a few words about components that might be suitable for use in these lab experiments. Transistors that can be used are general purpose NPN types like 2SC1815 and the 2SA1015 PNP complement. Similar type devices can be used such as the popular 2N3904 NPN and 2N3906 PNP devices which are also considered comparable complements of each other. A supply of various diodes, resistors, capacitors and inductors should also be available. Another potential source of transistors for use in these lab exercises are transistor arrays such as the LM3045 / LM3046 / LM3086 NPN Arrays from National Semiconductor. Similar NPN arrays from Intersil are, CA3045 / CA3046 / CA3083. Arrays of two or four 2N2222, 2N3904, 2N3906 and other types are available from some manufacturers like Fairchild and ON Semiconductor. A readily available enhancement mode NMOS transistor is the 2N7000. Advanced Linear Devices Inc. offers dual and quad N and P channel MOS arrays (ALD1106 and ALD1107) as well. The CD4007C CMOS logic package consists of three complementary pairs of N and P-channel enhancement mode MOS transistors. The N and P type pairs share either a common gate or common drain terminal which limits their use as six individual devices but these devices can still be useful for Lab experiments.

Remember, not all transistors share the same terminal designations, or pinouts, even if they share the same physical appearance. The order of some types is CBE (base is center lead) and BCE (collector is center lead) for others. This is very important when you connect the transistors together and to other components. Be careful to check the manufacturer's specifications (component datasheet). These can be easily found on various websites. Double-checking pin identities with a multi-meter's "diode check" function is highly recommended.

Extra stuff:
^^^^^^^^^^^^

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The common convention is that a typical silicon BJT base–emitter diode drop, ``VBE``, is 0.65V and a standard general purpose silicon diode drop is 0.6V. Other conventions use 0.6V or 0.7V for one or both. These are highly dependent on the manufacturing process used and the physical size of the components. The results you measure in the laboratory will most likely be between these values. Diodes and BJTs implemented on the same integrated circuit (i.e., on the same silicon die) may have equivalent characteristics. That is, the diodes and transistors will be more closely matched. Matched components are convenient to use in many circuit designs. We use discrete elements in most of these activities, and so it is not possible to match components unless they are all fabricated on the same silicon die. In the laboratory, a diode-connected transistor, with its base shorted to its collector may match the base–emitter characteristics of another transistor of the same type better than a simple diode.

Diode drops are strongly temperature dependent. Room-temperature transistors (~27ºC or 300ºK) have base–emitter drops around 0.65V, but as the temperature of the transistors increases, ``VBE`` drops near 0.5V. So temperature matching is just as important as component matching. Internal temperature compensation in bandgap voltage references lets them provide a temperature-independent voltage reference. Their output reference of ∼1.22V is the extrapolated ``VBE`` at absolute zero (i.e., 0ºK or −273.15ºC). It is not a coincidence that the Silicon bandgap (i.e., the energy separating valence and conduction electron bands) is ∼1.22 eV.

Temperature dependence and manufacturing variations (and the Early effect) are always a concern.

**Return to Electronics Text** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`
