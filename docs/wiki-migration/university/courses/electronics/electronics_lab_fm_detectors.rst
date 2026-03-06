FM Detectors
============

Objective
---------

To know the basic principles of FM demodulation as well as the different circuits used to detect information from a received FM signal.

Background
----------

For communication to work, both the sender and the receiver must agree on what communication channel to use. After which, the sender encodes the message and transmits it to the receiver. Then, the receiver receives the message and decodes it. This holds true to FM: the transmitted FM signal is received and must be demodulated to take the information. This is what FM detectors do.


|FM Demodulation Detection|

.. container:: centeralign

   //Figure 1. FM Demodulation Detection //


FM detectors are circuits that instantaneously convert the frequency changes from the carrier signal to its output voltage counterpart. They are also known as frequency demodulators or discriminators. An FM detector’s transfer function is nonlinear, however, when operated in its linear range is:

.. container:: centeralign

   :math:`K_d = V_out/f_input`


where:

-  V\ :sub:`out` = output voltage (information), V
-  f\ :sub:`input` = input FM signal, Hz
-  K\ :sub:`d` = transfer function, V/Hz

The input to the circuits is a frequency-varying signal with a constant amplitude. The circuits then transform these instantaneous frequency variations to amplitude variations, thus each voltage level in the output corresponds to its instantaneous frequency variation counterpart in the input. Therefore, the FM demodulator’s transfer function unit is in volts per Hertz.

Just like AM, FM also has a modulation index. It is equal to the ratio of the frequency deviation to the modulating frequency. The frequency deviation is the amount of change or swing in carrier frequency produced by the modulating signal. FM’s modulation index is defined by:

.. container:: centeralign

   :math:`\displaystyle m = \frac{\Delta f}{f_m}`


where:

-  Delta f = frequency deviation
-  f\ :sub:`m` = modulating frequency

Like AM, FM’s modulation index, m, is a measure of the peak frequency deviation. This is a way to express the peak deviation frequency as a multiple of the maximum modulating frequency. To illustrate this, refer to the figure below:


|Sample FM Signal|

.. container:: centeralign

   //Figure 2. Sample FM Signal //


The carrier signal frequency is 1kHz, the modulating frequency 100Hz, and the modulation index is 3. Taking note of the modulation index, this makes the peak frequency deviation 300Hz. The frequency will swing between 700 and 1300 Hz. On the other hand, the function of the modulating frequency is to know how fast the cycle is completed.

| There are different types of FM demodulators including:

-  Slope Detector
   \* Foster-Seeley Discriminator
   \* Ratio Detector
   \* Pulse-Averaging Discriminators
   \* Quadrature Detectors
   \* Phase-Locked Loops

| For the sake of simplicity, we will dive in to the Slope Detector to know the basic function of an FM demodulator.
| ===== Slope Detector ===== The slope-detector, otherwise known as a single-ended slope detector, is the simplest form of an FM demodulator. It is a Tuned-circuit frequency demodulator type wherein it converts FM signals to AM using tuned (LC) circuits and extract the information from the AM envelope using a series connection of a diode and a capacitor (conventional peak detector.) It can be used with any radio even if it does not have an FM capability. The slope detector relies on the selectivity of the receiver and its circuit operation is basic to all tuned-circuit discriminator. It is composed of a tuned circuit and a diode peak detector – the basic components of a typical tuned-circuit frequency discriminators. Figures 2 and 3 shows its traditional and simplified schematic diagram.

|Slope Detector|

.. container:: centeralign

   //Figure 3. Slope Detector //


   |Simplified Slope Detector|

.. container:: centeralign

   //Figure 4. Transformerless Slope Detector //


Despite its simplicity, the slope-detector has the most nonlinear voltage-versus-frequency characteristics, thus, it is rarely used. Figure 4 illustrates its voltage versus frequency characteristic.



|Voltage vs Frequency Characteristic|

.. container:: centeralign

   *Figure 5. Slope Detector’s Voltage vs Frequency Characteristic*


Another variation of a slope detector is a balanced slope detector. It is composed of two single-ended slope detectors connected in parallel and fed 180 degrees out of phase.

| 
| ===Procedure===

Open the simulation file. In the circuit, an FM signal with a 1kHz modulating frequency, 5V-20kHz carrier signal, and a modulating index of 5 is fed to the input. The tuned circuit formed by C\ :sub:`1` and L\ :sub:`1` performs the FM-to-AM conversion and the peak detector formed by D\ :sub:`1`, R\ :sub:`2`, and C\ :sub:`2` extract the information from the AM envelope. Run the simulation file and observe the waveforms.


|Slope Detector Simulation|

.. container:: centeralign

   //Figure 6. Slope Detector Simulation //


The waveforms observed should be similar to that of Figure 5b.

| |Slope Detector Waveforms|

.. container:: centeralign

   //Figure 7. Slope Detector Waveforms //


| ===== Other Circuits =====

Foster-Seeley Discriminator and Ratio Detectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Foster-Seeley Discriminator and Ratio Detector were widely used FM demodulators demodulation for radio receivers that typically used discrete components. Figure 6 shows a schematic of a Foster-Seely Discriminator and Figure 7 a Ratio Detector. At first look, the two circuits are similar. They both have an RF transformer and a pair of diodes, but the Foster-Seeley has no third winding unlike the Ratio Detector. It has a choke instead.


|Foster-Seeley Discriminator|

.. container:: centeralign

   //Figure 8. Foster-Seeley Discriminator //


   |Ratio Detector|

.. container:: centeralign

   //Figure 9. Ratio Detector //


| Both demodulators are simple to construct using discrete components and offer good levels of performance and linearity. However, the Foster-Seeley provides a higher output and has a lower distortion than the ratio detector, and the ratio detector provides a good level of immunity to amplitude noise and has a wider bandwidth compared to the Foster-Seeley. The downsides to these demodulators are the high cost of their transformers and they are difficult to incorporate with an integrated circuit; thus, they are not widely used these days.
| ==== Pulse-Averaging Discriminators ==== A Pulse-Averaging discriminator uses a zero-crossing detector, a one shot multivibrator and a low-pass filter to recover the original modulating signal. Figure 10 shows a block diagram of the pulse-averaging discriminator.

|Block Diagram of Pulse-Averaging Discriminator|

.. container:: centeralign

   //Figure 10. \| Block Diagram of Pulse-Averaging Discriminator //


This is a very high-quality frequency demodulator and was limited to expensive telemetry and industrial control applications. But due to the availability of low-cost ICs, the pulse-averaging discriminator is easily implemented and is now used in many electronic products.



|Pulse-Averaging Discriminator’s Waveforms|

.. container:: centeralign

   //Figure 11. \| Pulse-Averaging Discriminator’s Waveforms: (a) FM input, (b) Output of zero-crossing detector, (c) Output of one shot, (d) Output of discriminator (original modulating signal). //


| 
| ==== Quadrature Detectors ==== |Quadrature Detector|

.. container:: centeralign

   *Figure 12. Block Diagram of Quadrature Detector*


| The quadrature detector is probably the single most widely used FM demodulator. It uses a phase-shift circuit to produce a phase shift of 90° at the unmodulated carrier frequency. This detector is primarily used in TV demodulation and is used in some FM radio stations.
| ==== Phase-Locked Loops ==== The phase-locked loop (PLL) is a frequency- or phase-sensitive feedback control circuit. All PLLs have the three basic elements: Phase detector, low-pass filter, and voltage-controlled oscillator. Phase-locked loops are used in frequency demodulation, frequency synthesizers, and various filtering and signal detection applications. Figure 17 shows the block diagram of a PLL.

|Phase-Locked Loop|

.. container:: centeralign

   //Figure 13. Block Diagram of Phase-Locked Loop //


| The phase-locked loop used as an FM demodulator, though the operation of a PLL is involved, is probably the simplest and easiest to understand. The ability of a phase-locked loop to provide frequency selectivity and filtering gives it a signal-to noise ratio superior to that of any other type of FM detector. For a more in-depth study of its operation, check the :doc:`Phase-Locked Loop Laboratory Activity </wiki-migration/university/courses/electronics/electronics-lab-31>`.
| ===== Question ===== 1. In the slope detector, what happens to the output signal if C2 is changed to 0.001uF? 0.1uF? Change R2 while retaining C2 as 0.01uF and again, observe the output waveform.
|

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  LTSpice files: :git-education_tools:`m2k/ltspice/fm_demodulators_ltspice`
   


Further Reading
===============

Some additional resources:

-  `NTSC Transmission through Optic Fiber <http://web.mit.edu/6.101/www/s2015/projects/hmalpica_Project_Final_Report.pdf>`__ Malpica, et. al. (2015) Massachusetts Institute of Technology
-  `Frequency Modulation <https://fas.org/man/dod-101/navy/docs/es310/FM.htm>`__
-  `Demodulation <https://www-elec.inaoep.mx/~rogerio/DemodulationGeneral.pdf>`__
-  `Slope Detector <https://www.usna.edu/EE/ee334/documents/EE334%20Supplementary%20Notes.pdf>`__ US Naval Academy (2012-2013) p. 85

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |FM Demodulation Detection| image:: https://wiki.analog.com/_media/university/courses/electronics/fmd_f1.png
   :width: 700px
.. |Sample FM Signal| image:: https://wiki.analog.com/_media/university/courses/electronics/fmd_1.png
   :width: 700px
.. |Slope Detector| image:: https://wiki.analog.com/_media/university/courses/electronics/fmd_slope_det.png
   :width: 500px
.. |Simplified Slope Detector| image:: https://wiki.analog.com/_media/university/courses/electronics/fmd_slope_det2.png
   :width: 600px
.. |Voltage vs Frequency Characteristic| image:: https://wiki.analog.com/_media/university/courses/electronics/fmd_f3.png
   :width: 700px
.. |Slope Detector Simulation| image:: https://wiki.analog.com/_media/university/courses/electronics/fmd_f5.png
   :width: 700px
.. |Slope Detector Waveforms| image:: https://wiki.analog.com/_media/university/courses/electronics/fmd_f5_3.png
   :width: 800px
.. |Foster-Seeley Discriminator| image:: https://wiki.analog.com/_media/university/courses/electronics/fmd_foster_seeley.png
   :width: 600px
.. |Ratio Detector| image:: https://wiki.analog.com/_media/university/courses/electronics/fmd_ratio_det.png
   :width: 600px
.. |Block Diagram of Pulse-Averaging Discriminator| image:: https://wiki.analog.com/_media/university/courses/electronics/fmd_f10.png
   :width: 700px
.. |Pulse-Averaging Discriminator’s Waveforms| image:: https://wiki.analog.com/_media/university/courses/electronics/fmd_f11.png
   :width: 800px
.. |Quadrature Detector| image:: https://wiki.analog.com/_media/university/courses/electronics/fmd_f14.png
   :width: 700px
.. |Phase-Locked Loop| image:: https://wiki.analog.com/_media/university/courses/electronics/fmd_f17.png
   :width: 700px
