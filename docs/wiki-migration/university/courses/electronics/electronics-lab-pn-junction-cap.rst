Activity: The voltage dependent capacitance of the PN junction
==============================================================

Objective:
----------

The objective of this lab activity is to measure the voltage dependent capacitance of a reverse biased PN junction.

Background:
-----------

**PN junction capacitance**

Increasing the reverse bias voltage, V\ :sub:`J`, across a PN junction leads to the redistribution of charge away from the interface leaving a depleted region or layer, W in figure 1. This depleted layer acts like the insulator between the two conducting plates of a capacitor. The thickness, W, of this layer is a function of the applied electric field and the doping concentration. The PN junction capacitance is divided into two components, the barrier capacitance and the diffusion capacitance. Under the conditions of reverse bias free carrier injection does not occur therefore, the diffusion capacitance is equal to zero. The barrier capacitance is the dominant source of capacitance for reverse and small positive bias voltages less than the diode turn on voltage (0.6V for Si). In practice, the barrier capacitance can be as small as a fraction of a picofarad to hundreds of picofarads depending on the area of the junction and the doping concentration. The dependence of the junction capacitance to the applied bias voltage called the capacitance-voltage (CV) characteristic of the junction. In this lab you will measure and plot this characteristic for various PN junctions (diodes).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/apn_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 PN junction depletion region


For further reading on PN junction depletion region:

`Depletion Region <https://en.wikipedia.org/wiki/Depletion_region>`__

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less Breadboard
| 1 - 10 KΩ resistor
| 1 - 39 pF capacitor
| 1 - 1N4001 diode
| 1 - 1N3064 diode
| 1 - 1N914 diode
| Red, yellow and green LEDs
| 1 - 2N3904 NPN transistor
| 1 - 2N3906 PNP transistor

Directions Step 1:
------------------

Build the test setup as shown in figures 2 and 3 on your solder-less bread board. The first step is to measure the unknown capacitance C\ :sub:`m` with the known C\ :sub:`1`, we connected between the AWG output and Scope input. The two scope minus inputs 1- and 2- are both grounded. The Scope channel 1+ input is tied to the AWG 1 output, W1, using one row on breadboard. Scope channel 2+ is inserted into a bread board row 8 to 10 rows away from the row that the AWG output is inserted in. The row adjacent to scope channel 2+ and towards the AWG1 row is grounded. This is to minimize any unwanted stray coupling between AWG1 and Scope channel 2. Because the Fly-Wires are not shielded, try to keep the W1 and 1+ wires as far away from the 2+ wire as possible.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/apn_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 Step 1 setup to measure C\ :sub:`m`


Hardware Setup:
---------------

Using the Network Analyzer instrument in the Scopy software obtain a gain (attenuation) vs. frequency plot from 5 kHz to 10 MHz. Scope channel 1 is the "filter" input and scope channel 2 is the "filter" output. Set AWG offset to 1V and the Amplitude to 200mV peak-to-peak . The offset value is not important at this point when measuring a simple real capacitor but will be used as the reverse bias voltage when we measure diodes in later steps. Set the vertical scale to start at 1dB to -50 dB range. Run a single sweep and export the data to a .csv file. You should notice a high pass characteristic that has a high attenuation at very low frequencies where the impedance of the capacitor is large compared to R\ :sub:`1`. At the very high end of the frequency sweep there should be a relatively flat region where the impedance of the C\ :sub:`1`, C\ :sub:`m`\ capacitive voltage divider is much lower than R\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/apn_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3 Step 1 setup to measure C\ :sub:`m`


Procedure Step 1:
-----------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/apn_f3_ss.png
   :align: center

.. container:: centeralign

   Figure 4 Scopy shot


We chose C\ :sub:`1` to be sufficiently larger than C\ :sub:`stray` such that we can ignore C\ :sub:`stray` in our calculations but still have a similar value to our unknown C\ :sub:`m`.

Open the saved data file in a spreadsheet program (Excel) and scroll to near the end of the data at high frequencies (>1MHz) where the attenuation level is essentially flat. Write down the channel 2 amplitude, this is G\ :sub:`HF1`\ (in dB). Since we now know G\ :sub:`HF1` and C\ :sub:`1` we can use the following equation to calculate C\ :sub:`m`. Write down your C\ :sub:`m`\ value which we will need when we move to the next step and measure the capacitance of various diode PN junctions. Be sure to include your calculations and the value for C\ :sub:`m` in your lab report.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/apn_e1.png
   :align: center
   :width: 220px

`Capacitive Dividers <https://en.wikipedia.org/wiki/Voltage_divider#Capacitive_divider>`__

Directions Step 2:
------------------

Now we will measure the capacitance of the various diodes from the ADALP2000 Analog Parts Kit under a range of reverse bias conditions. Build the test setup as shown in figures 4 and 5 on your solder-less bread board. Simply replace C\ :sub:`1` with D\ :sub:`1`, a 1N4001. Be sure to insert the diode with the correct polarity such that a positive offset in AWG1 will reverse bias the diode.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/apn_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5 Step 2 setup to measure diode capacitance


.. _hardware-setup-1:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/apn_f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6 Step 2 setup to measure diode capacitance


Using the Network Analyzer instrument in the Scopy software obtain a gain (attenuation) vs. frequency plot from 5 kHz to 10 MHz for each AWG 1 DC offset value in table 1. Export the data for each sweep to a different .csv file.

Procedure:
----------

Fill in the rest of Table 1 with the G\ :sub:`HF` value for each offset voltage value and using the value for C\ :sub:`m` and the equation from step 1, calculate the value for C\ :sub:`diode`.

============== ============ ===============
Offset Voltage G\ :sub:`HF` C\ :sub:`diode`
============== ============ ===============
0V                          
1V                          
2V                          
3V                          
4V                          
============== ============ ===============

Table 1 Capacitance vs. voltage data


|image1|

.. container:: centeralign

   Figure 7 Scopy shot with offset at 0V


Replace the 1N4001 diode with the 1N3064 diode from the Kit and repeat the same set of sweeps you just did for the first diode. Fill out another table with your measured data and calculated C\ :sub:`diode` values. How do the 1N3064 values compare to those for the 1N4001 diode? You should include a plot of the diode capacitance vs. reverse bias voltage for each diode you measure in your lab report.

Next replace the 1N3064 diode with one of the 1N914 diodes from the kit. Again repeat the same set of sweeps you just did for the other diodes. Fill out another table with your measured data and calculated C\ :sub:`diode` values. How do the 1N914 values compare to those for the 1N4001 and 1N3064 diodes?

The capacitance you measure for the 1N914 diode should be much smaller than the other two diodes. It might be small enough to be comparable in size to C\ :sub:`stray`. If you haven't already gone through the lab on measuring the :doc:`parasitic capacitance of solder-less breadboards </wiki-migration/university/courses/electronics/electronics-lab-breadboard-coupling>` you might want to go back and do that at this point to confirm the value of C\ :sub:`stray` in the setup..

Extra Credit measurements:
--------------------------

Light emitting diodes or LEDs are also PN junctions. They are fabricated from materials other than Silicon so their turn on voltage is much different from normal diodes. However, they still have a depletion layer and capacitance. As extra credit measure the red, yellow and green LEDs supplied in the ADALP2000 Analog Parts Kits as you did the normal diodes. Be sure to insert the LEDs into the test setup with the proper polarity for reverse bias. If you did it wrong you will probably see the LED light up at some point. Include your calculations, a table and plot of your measured capacitance vs. voltage for each LED in your lab report.

Advanced Credit measurements:
-----------------------------

Bipolar transistors (NPN, PNP) also contain PN junctions. The Base - Collector junction is reversed biased under most conditions of operation, This Base - Collector junction capacitance appears from input to output in the :doc:`common emitter amplifier </wiki-migration/university/courses/electronics/electronics-lab-5>` configuration and can be the ultimate limiting factor in the high frequency bandwidth of such an amplifier. You can measure this capacitance vs. the amount of reverse bias by connecting the base and collector leads of the 2N3904 (NPN) and 2N3906 (PNP) transistors to your test setup. Remember to connect the transistor with the correct polarity such that the C-B is reversed biased.

Include your calculations, a table and plot of your measured capacitance vs. voltage for each transistor in your lab report. Compare your measured C-B capacitance to the manufacturer's data sheet for these transistors. Note, data sheets don't often list the C-B capacitance directly. It is often included as part of the output capacitance or something similar.

.. admonition:: Download
   :class: download

   \*\* Lab Resources \*\*

   
   -  Fritzing files: :git-education_tools:`v_dep_pn_bb <m2k/fritzing/volt_dep_cap_pn_junc_bb>`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/v_dep_pn_ltspice`
   


For Further Reading:
~~~~~~~~~~~~~~~~~~~~

`The Varactor Diode, Varicaps <https://en.wikipedia.org/wiki/Varicap>`__

**Return to the Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/apn_f7_ss.png
