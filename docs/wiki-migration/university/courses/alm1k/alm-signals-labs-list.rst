ADALM1000 Active Learning Module Lab Activities for Signals and Systems
=======================================================================

Analog Devices is as passionate about educating the next generation of young electrical engineers as it is about pioneering the next technological breakthrough. The Active Learning Program is a platform where Analog Devices, working with leading educational institutions has created and deployed new hands on learning tools for the next generation of analog circuit design engineers. This University Program brings the analog signal processing technology the company has developed to the academic community in a way that is open and accessible to faculty and students in the form of analog design kits and analog component kits, online and downloadable software and teaching materials, online support, textbooks, reference designs and lab projects to enrich students’ education in electrical engineering and the application to core engineering and physical science curricula.

The laboratory activities provided on these wiki pages are considered open source and available for free use in non-commercial educational and academic settings. **The only requirement is that they continue to retain the attribution to Analog Devices Inc.** Supplying them on the ADI wiki allows registered users to login and contribute to the materials posted here improving the content and keeping them up to date.

In general these example lab activities are based on the :doc:`ADALM1000 </wiki-migration/university/tools/m1k>` (M1K) low cost design hardware platform and the accompanying :doc:`ALICE Desk-Top </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` software package. It is also possible to perform these lab activities using the ADALM2000 (M2K) hardware module with minor adjustments to the circuits. :doc:`This document </wiki-migration/university/courses/alm1k/m2k-convert-labs>` outlines how the labs might be altered for use with M2K.

They are generally written to be performed using principally the components provided in the Analog Parts Kit, ADALP2000, supplied through ADI distribution channels, however additional devices are sometimes needed. Other sources of these or similar components can of course be used.

Pre-Lab Circuit Simulation
--------------------------

| Notes on :doc:`circuit simulation </wiki-migration/university/courses/electronics/circuitsimulationnotes>`.
| Links to an archive of example simulation schematic files are provided below.

General Lab materials
---------------------

-  Background Lab Notes: :doc:`Solder-less Breadboards </wiki-migration/university/courses/electronics/electronics-lab-breadboards>`
-  Background Lab Notes: :doc:`Resistors </wiki-migration/university/courses/electronics/electronics-lab-resistors>` (including color code)
-  Background Lab Notes: :doc:`Capacitors </wiki-migration/university/courses/electronics/electronics-lab-capacitors>` (including color code)
-  :doc:`Measuring voltages beyond 0 to 5V with the ADALM1000 (M1K) </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>`
-  :doc:`How to Generate External Signal Sources </wiki-migration/university/courses/alm1k/circuits1/alm-cir-signal-generators>`
-  :doc:`Battery Voltage "Rail-Splitter" </wiki-migration/university/courses/alm1k/circuits1/alm_cir_lab-rail-splitter>`
-  :doc:`Bipolar power supplies for active learning labs </wiki-migration/university/courses/alm1k/circuits1/alm-bipolar-step-up-dc-dc>`

Continuous Time Filters
~~~~~~~~~~~~~~~~~~~~~~~

Passive and Active filter pre-lab simulation `schematic files <https://wiki.analog.com/_media/university/courses/electronics/continuous-time-filter-sims.zip>`_.

Filter Tutorial Pages:
^^^^^^^^^^^^^^^^^^^^^^

-   F\ :sub:`O` and Q in Filters :adi:`MT-210`
-   The Bessel Response :adi:`MT-204`
-   The Butterworth Response :adi:`MT-224`
-   The Chebyshev Response :adi:`MT-206`
-   Biquadratic (Biquad) Filters :adi:`MT-205`
-   Sallen-Key Filters :adi:`MT-222`
-   Multiple Feedback Filters :adi:`MT-220`
-   Multiple Feedback Band-Pass Design Example :adi:`MT-218`
-   State Variable Filters :adi:`MT-223`
-   Digitally Programmed State Variable Filter :adi:`MT-208`
-   Allpass Filters :adi:`MT-202`
-   Dual Amplifier Band-Pass (DABP) Filter :adi:`MT-209`
-   Bainter Notch Filters :adi:`MT-203`
-   Twin T Notch Filter :adi:`MT-225`
-   Low-Pass to Band-Pass Filter Transformation :adi:`MT-215`
-   Low-Pass to Band-Reject (Notch) Filter Transformation :adi:`MT-216`
-   Low-Pass to High-Pass Filter Transformation :adi:`MT-217`

Filter Lab Activities
^^^^^^^^^^^^^^^^^^^^^

-  Passive R-L-C filters
-  Active Filters, Low Pass, High Pass, :doc:`Band Pass </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-band-pass-step-response-lab>`
-  Descrete Time Filters
-  :doc:`Switched Capacitor Filters </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-switched-cap-filter-lab>`
-  :doc:`Semi-digital FIR Filter </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-semi-dig-filter-lab>`

Sampled Data Systems
~~~~~~~~~~~~~~~~~~~~

Sampled Data Systems pre-lab simulation `schematic files <https://wiki.analog.com/_media/university/courses/electronics/sampled-data-sims.zip>`_.

Sampling Systems Tutorial Pages:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-   Quantization Noise :adi:`MT-001`

   -   An Expanded Derivation of the Equation, SNR=6.02N+1.76 dB :adi:`MT-229`

-   Data Converter Codes :adi:`MT-009`
-   Data Converter Static Specifications :adi:`MT-010`
-   What the Nyquist Criterion Means to Sampled Data System Design :adi:`MT-002`
-   Understanding SINAD, ENOB, SNR, THD, THD+N, and SFDR :adi:`MT-003`
-   Aspects of ADC Input Noise :adi:`MT-004`
-   Aperture Time, Aperture Jitter, Aperture Delay Time :adi:`MT-007`

   -  The Effect of Clock Noise on Sampled Data Systems :adi:`(ppt, 655,360 bytes) <static/imported-files/rarely_asked_questions/clockNoise.ppt>`

-   Converting Oscillator Phase Noise to Time Jitter :adi:`MT-008`
-  The Power Spectral Density of Phase Noise and Jitter: Theory, Data Analysis, and Experimental Results :adi:`(AN-1067) <media/en/technical-documentation/application-notes/AN-1067.pdf>`
-   ADC Sparkle Codes and Metastable States :adi:`MT-011`

Digital to Analog Converter Tutorial pages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-   String DACs, Thermometer (Fully Decoded) DACs :adi:`MT-014`
-   Binary DACs :adi:`MT-015`
-   Segmented DACs :adi:`MT-016`
-   Oversampling Interpolating DACs) :adi:`MT-017`
-   Intentionally Nonlinear DACs :adi:`MT-018`
-   DAC Interface Fundamentals :adi:`MT-019`
-   Fundamentals of Direct Digital Synthesis (DDS) :adi:`MT-085`
-   Digital Potentiometers :adi:`MT-091`

Analog to Digital Converter Tutorial pages:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-   The Flash Converter :adi:`MT-020`
-   Successive Approximation ADCs :adi:`MT-021`
-   Sigma-Delta ADC Basics :adi:`MT-022`
-   Sigma-Delta ADC Advanced Concepts and Applications :adi:`MT-023`
-   Pipelined Subranging ADCs :adi:`MT-024`
-   Folding ADCs :adi:`MT-025`
-   Counting ADCs :adi:`MT-026`
-   Integrating ADCs :adi:`MT-027`
-   Voltage-to-Frequency Converters :adi:`MT-028`

Sampled Data Systems Lab Activities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :doc:`CMOS Analog Switches </wiki-migration/university/courses/alm1k/alm-lab-18>`
-  :doc:`Auto-Zeroing Amplifier </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-auto-zero-amp-lab>`
-  :doc:`Linear Feedback Shift Register </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-lfsr-lab>`
-  :doc:`Semi-digital Filter </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-semi-dig-filter-lab>`
-  :doc:`Switched Capacitor Filters </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-switched-cap-filter-lab>`
-  Switched Cap Analog Delay line (bucket brigade)
-  :doc:`Digital to Analog Conversion </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-adc-dac-lab>`
-  :doc:`The Track Hold Amplifier </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-tha-lab>`
-  :doc:`Analog to Digital Conversion </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-sar-adc-1>`
-  :doc:`Delta – Sigma Modulator </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-delta-sigma-lab>`

Communications Systems
~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`Amplitude Modulation (AM) </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-am-modulatior-lab>`
-  Pulse Amplitude Modulation
-  :doc:`Pulse Width Modulation </wiki-migration/university/courses/alm1k/alm-lab-pwm>`
-  Pulse Frequency Modulation
-  Frequency Shift Keying
-  Time Division Multiplexing
-  Optocouplers ( analog isolation amplifier )

Communications Circuits
-----------------------

-  Inductor Self Resonance
-  :doc:`Transformers </wiki-migration/university/courses/alm1k/alm-lab-transformers>`
-  :doc:`Artificial Transmission Lines </wiki-migration/university/courses/alm1k/alm-lc-atline>`
-  Tuned Amplifiers,part I, Tuned Amplifiers,part II
-  Transformer Coupled Amplifiers
-  Active Filters, :doc:`Polyphase Filters </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-poly-phase-filter-lab>`
-  :doc:`AM modulation and Envelop Detectors </wiki-migration/university/courses/alm1k/circuits1/alm-cir-envelope-detector>`
-  FM Detectors
-  Variable Gain Amplifiers
-  :doc:`Pulse Width Modulation </wiki-migration/university/courses/alm1k/alm-lab-pwm>`
-  Frequency Synthesizers, :doc:`Hartley oscillator </wiki-migration/university/courses/alm1k/alm-lab-hartley-osc>`, Colpitts oscillator, Clapp oscillator, Peltz Oscillator
-  :doc:`The Wien bridge oscillator </wiki-migration/university/courses/alm1k/alm-lab-wien-bridge-osc>`
-  :doc:`Pulsed Oscillators </wiki-migration/university/courses/alm1k/alm-lab-pulsed-osc>`
-  :doc:`Phase Locked Loops </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-phase-locked-loop-lab>`
-  Diode Ring Modulators
-  Active Mixers
-  Pseudo-Random Sequence Generators

Miscellaneous Lab Activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`Electret microphone preamplifier </wiki-migration/university/courses/alm1k/alm-lab-s1>`
-  :doc:`Heart Rate Monitor Circuit </wiki-migration/university/courses/alm1k/alm-lab-heart-rate-mon>`

General background Information.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The assumption is made that the reader has some familiarity with the ADALM1000 Lab hardware and ALICE software system before starting these lab activities. It is also assumed that for certain of the data presented here, the data waveforms from the lab hardware were saved to disk and post processed and plotted in Microsoft Excel.

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

**Return to ALM1000** :doc:`Overview </wiki-migration/university/tools/m1k>`
