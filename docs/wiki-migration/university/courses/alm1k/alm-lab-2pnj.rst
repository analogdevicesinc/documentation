Activity: The voltage dependent capacitance of the PN junction
==============================================================

Objective:
----------

The objective of this lab activity is to measure the voltage dependent capacitance of a reverse biased PN junction.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The analog I/O channel pins are referred to as CHA and CHB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Background:
-----------

\**PN junction capacitance \*\*

Increasing the reverse bias voltage, V\ :sub:`J`, across a PN junction leads to the redistribution of charge away from the interface leaving a depleted region or layer, W in figure 1. This depleted layer acts like the insulator between the two conducting plates of a capacitor. The thickness, W, of this layer is a function of the applied electric field and the doping concentration. The PN junction capacitance is divided into two components, the barrier capacitance and the diffusion capacitance. Under the conditions of reverse bias free carrier injection does not occur therefore, the diffusion capacitance is equal to zero. The barrier capacitance is the dominant source of capacitance for reverse and small positive bias voltages less than the diode turn on voltage (0.6V for Si). In practice, the barrier capacitance can be as small as a fraction of a picofarad to hundreds of picofarads depending on the area of the junction and the doping concentration. The dependence of the junction capacitance to the applied bias voltage called the capacitance-voltage (CV) characteristic of the junction. In this lab you will measure and plot this characteristic for various PN junctions (diodes).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-pn-cap_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 PN junction depletion region


| For further reading on PN junction depletion region:
| http://en.wikipedia.org/wiki/Depletion_region

Materials:
~~~~~~~~~~

| ALM1000 Module
| Solder-less Breadboard
| 1 – AD8541 single op-amp
| 1 – 100 KΩ resistor
| 1 – 39 pF capacitor
| 1 – 1N4001 diode
| 1 - 1N3064 diode
| 1 – 1N914 diode
| Red, yellow and green LEDs
| 1 – NPN transistor, 2N3904 or TIP31
| 1 – PNP transistor, 2N3906 or TIP32

Hardware Setup:
~~~~~~~~~~~~~~~

Build the test setup as shown in figures 2 and 3 on your solder-less bread board. Keep the jumper wires as short and neat as possible. Each row of contacts on the breadboard has a small stray capacitance to the adjacent rows on either side. In this setup we want to minimize these stray capacitances. One way to cancel out the effect of the row to row capacitance is to drive or boot-strap the adjacent rows with the output of a buffer amplifier. Now the stay capacitance will see the same signal on both sides and will thus not have any current through it.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-pn-cap_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Step 1 setup to cancel C\ :sub:`stray`\


In figure 3 we can see that the amplifier input on pin 3 has pins 2 and 4 adjacent to it. Pin 2 is connected to the output and is inherently boot-strapped. Pin 4 is connected to ground and there is not anything we can do about that. We have shown a jumper wire from pin 3 to another row of pins to provide a place to connect the test devices. The two adjacent rows on either side are connected to the amplifier output and their stay capacitance will be boot-strapped out.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-pn-cap_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Step 1 setup to cancel C\ :sub:`stray`\


Directions Step 1:
~~~~~~~~~~~~~~~~~~

Using the Impedance Analyzer display in the :doc:`ALICE desktop software </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` obtain a capacitance measurement. Set the Ext Res equal to the 100000 ohms of R\ :sub:`1`. The number of FFT samples does not affect the measurement very much but 4096 or 8192 samples is a good place to start. The FFT Window function likewise does not matter too much but Nuttall or Flat-top are good choices. Scope channel A is the input stimulus and scope channel B measures the output. In the AWG window set CHA to SVMI mode and Shape to Sine. Set the Freq to 12500 Hz. Be sure CHB mode is set to Hi-Z. Set CHA Min to 0V and the CHA Max to 0.7V. The offset value is not important at this point when measuring a simple real capacitor but will be used as the reverse bias voltage when we measure diodes in later steps.

With no capacitor installed click the run button. When the readings have stabilized click the stop button to pause the program. Note the Gain and Phase values at the top of the display area. Enter the displayed gain value in the Gain Cor entry slot and the displayed phase value in the Phase Cor entry slot. Enter a positive value if a negative number is displayed to cancel out the value. Click on run again. The display should change such that the gain and phase values are nearly zero and the calculated capacitance at the bottom is approximately zero as well.

Procedure Step 2:
~~~~~~~~~~~~~~~~~

Now we can measure a small value capacitor to verify the set up. From the Analog Parts Kit insert a 39 pF capacitor from pin 3 of the amplifier to ground as shown in figures 4 and 5. The display should change and the calculated capacitance at the bottom should read a value very close to 39 pF.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-pn-cap_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Schematic to measure small fixed capacitor


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-pn-cap_f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Breadboard setup to measure small fixed capacitor


Directions Step 3:
~~~~~~~~~~~~~~~~~~

Now we are ready to measure the capacitance of the various diodes from the Analog Parts Kit under a range of reverse bias conditions. Modify the test setup as shown in figures 6 and 7 on your solder-less breadboard. Simply replace C\ :sub:`1` with D\ :sub:`1`, a 1N4001. Be sure to insert the diode with the correct polarity such that a positive offset in CHA will reverse bias the diode.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-pn-cap_f6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, Step 3 setup to measure diode capacitance


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-pn-cap_f7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Step 3 setup to measure diode capacitance


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

Using the Impedance Analyzer display in the ALICE desktop software obtain a capacitance measurement for each CHA DC offset value in table 1.

Procedure:
~~~~~~~~~~

Fill in the rest of Table 1 with the Capacitance value for each offset voltage value.

======= ======= ===============
CHA Min CHA Max C\ :sub:`diode`
======= ======= ===============
0V      0.7     
1V      1.7     
2V      2.7     
3V      3.7     
4V      4.7     
======= ======= ===============

Table 1 Capacitance vs. voltage data

Replace the 1N4001 diode with the 1N3064 diode from the Kit and repeat the same set of DC offsets you just did for the first diode. Fill out another table with your measured data C\ :sub:`diode` values. How do the 1N3064 values compare to those for the 1N4001 diode? Explain what might make the capacitance of the two diodes different. You should include a plot of the diode capacitance vs. reverse bias voltage for each diode you measure in your lab report.

Next replace the 1N3064 diode with one of the 1N914 diodes from the kit. Again repeat the same set of DC offset measurements you just did for the other diodes. Fill out another table with your measured data and calculated C\ :sub:`diode` values. How do the 1N914 values compare to those for the 1N4001 and 1N3064 diodes?

The capacitance you measure for the 1N914 diode should be much smaller than the other two diodes. It might be small enough to be comparable in size to C\ :sub:`stray`. You could place the other three 1N914 diodes from the kit in parallel ( remember proper polarity ) with the first diode to increase the total. Remember to divide the measured capacitance by 4 to get the average capacitance per diode.

Extra Credit measurements:
~~~~~~~~~~~~~~~~~~~~~~~~~~

Light emitting diodes or LEDs are also PN junctions. They are fabricated from materials other than Silicon so their forward turn on voltage is much different than normal diodes. However, they still have a depletion layer and capacitance. As extra credit measure the red, yellow and green LEDs supplied in the Analog Parts Kits as you did the normal diodes. Be sure to insert the LEDs into the test setup with the proper polarity for reverse bias. If you did it wrong you will probably see the LED light up at some point. Include your calculations, a table and plot of your measured capacitance vs. voltage for each LED in your lab report.

Advanced Credit measurements:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bipolar transistors (NPN, PNP) also contain PN junctions. The Base – Collector junction is reversed biased under most conditions of operation, This Base – Collector junction capacitance appears from input to output in the common emitter amplifier configuration and can be the ultimate limiting factor in the high frequency bandwidth of such an amplifier. You can measure this capacitance vs. the amount of reverse bias by connecting the base and collector leads of the 2N3904 or TIP31 (NPN) and 2N3906 or TIP32 (PNP) transistors to your test setup. Remember to connect the transistor with the correct polarity such that the C-B is reversed biased.

Include your calculations, a table and plot of your measured capacitance vs. voltage for each transistor in your lab report. Compare your measured C-B capacitance to the manufacturer’s data sheet for these transistors. Note, data sheets don’t often list the C-B capacitance directly. It is often included as part of the output capacitance or something similar.

**Return to the ALM Lab Activity** :doc:`table of contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
