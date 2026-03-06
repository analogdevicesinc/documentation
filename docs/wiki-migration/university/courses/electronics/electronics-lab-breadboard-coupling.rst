Solder-less Breadboard Stray Capacitance
========================================

Objective:
----------

The objective of this Lab Activity is to measure the stray coupling capacitance between adjacent rows on a solder-less breadboard under various arrangements of connections.

Background:
-----------

When building an experiment on a solder-less breadboard, you add the small (stray) capacitor between adjacent rows of connection points to the circuit. This is because the way the solder-less breadboard is built, it has rows of metal connection strips laid side by side (0.1 inch apart) separated by plastic dividers. Because the strips are fairly long and they are in parallel, they have a significant capacitance between them. Figure 1 shows a cut away of the inside of a typical breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abc_f1.jpg
   :align: center
   :width: 350px

.. container:: centeralign

   **Figure 1 Breadboard cut away**


The goal of this activity is to measure your solder-less breadboard and find the capacitance each row has to the next row. Not only that, but from a row to the alternate row (second one over) and to each second alternate and so on.

When there are unintended hidden capacitors in the structure of the circuit being tested, we refer to these as parasitic capacitance. The solder-less breadboard has a lot of these unwanted parasitic capacitances. These stray paths can lead to unwanted coupling between inputs and outputs in the breadboarded circuit. Take the standard single op-amp in an 8 pin DIP package for example. The inverting and non-inverting inputs are right next to each other on pins 2 and 3. Another example would be the standard dual op-amp in an 8 pin DIP where the output of one of the amplifiers is on pin 1 and its inverting input is on the adjacent pin 2. When inserted in the breadboard a small stray capacitance will be present between these two pins which can adversely affect the circuit characteristics at high frequencies.

Schematically we can view the breadboard and our measurement setup as shown in figure 2. In the figure we depict three typical rows of pins on the breadboard. The row to row capacitance, C\ :sub:`row`, is shown. Since all the rows are more or less identical, all the C\ :sub:`row`\ s have the same value. To measure C\ :sub:`row` we will excite one row with the AWG sine source and measure the amount of signal coupled onto another row (an adjacent row in this schematic) using the oscilloscope. We will model the oscilloscope channel as a 1 megaohm resistance, R\ :sub:`m`, to ground in parallel with some as yet unknown capacitance C\ :sub:`m`. The 1 megaohm value for R\ :sub:`m` is only an approximation. If you have a digital ohm meter use it to get the actual R\ :sub:`m` for your ADALM2000 module. The wiring that connects the AWG and Scope inputs to the breadboard also introduce some stray coupling capacitance which is included as C\ :sub:`stray` in the schematic.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abc_f2.png
   :align: center
   :width: 575px

.. container:: centeralign

   **Figure 2 Schematic model of breadboard.**


The parallel combination of C\ :sub:`stray` and C\ :sub:`row` form a capacitor AC voltage divider with C\ :sub:`m` (and R\ :sub:`m`) of the scope input. The circuit has a high pass characteristic with resistance R\ :sub:`m` and the total capacitance (C\ :sub:`m` + C\ :sub:`stray` + C\ :sub:`row`) setting the 3 dB corner frequency F\ :sub:`3dB` given by:

|image1|\ (E1)

At frequencies well above F\ :sub:`3dB` the response is flat with a zero degree phase shift. The relative attenuation, G\ :sub:`HF`, in dB is simply the capacitance divider ratio given by:

|image2|\ (E2)

By sweeping the frequency of AWG1 and measuring F\ :sub:`3dB` and G\ :sub:`HF` for various configurations we can obtain values for the three unknown capacitances. At this point it is important to point out that it is likely that C\ :sub:`m` will be much larger than either C\ :sub:`stray` or C\ :sub:`row`. So the attenuation factor will be large in this case.

Materials:
----------

| ADALM2000 Lab Module
| Solder-less Breadboard
| Fly-Wire connector

Step 1 Directions:
------------------

The first step is to measure just the stray capacitance, C\ :sub:`stray`, between the AWG output and Scope input due to the Fly-Wire connector. Connect the wires from the ADALM2000 module to your solder-less breadboard using the fly-wire connector that came with the Kit as shown in figure 3. The two scope minus inputs 1- and 2- are both grounded. Scope channel 1+ input is tied to the AWG 1 output, W1, using one row on breadboard. Scope channel 2+ is inserted into a bread board row at least 10 rows away from the row that the AWG output is inserted in. The row adjacent to scope channel 2+ and towards the AWG1 row is grounded. Because the Fly-Wires are not shielded, try to keep the W1 and 1+ wires as far away from the 2+ wire as possible.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abc_bb1.png
   :align: center
   :width: 600px

.. container:: centeralign

   **Figure 3 Connection to measure stray coupling due to Fly-Wire connector.**


Hardware Setup:
---------------

Using the Network Analyzer instrument in the Scopy software obtain a gain (attenuation) vs. frequency plot from 10 Hz to 10 MHz. Scope channel 1 is the "filter" input and scope channel 2 is the "filter" output. Set AWG offset to 0 and the Amplitude to 2V with the Max-Gain set to 0.1X. Set the vertical scale to start at 1dB with an 80 dB range. Run a single sweep and export the data to a .csv file.

Procedure:
----------

Open the saved data file in a spreadsheet program (Excel) and first scroll to near the end of the data at high frequencies where the attenuation level is essentially flat. Write down the channel 2 amplitude, this is G\ :sub:`HF1`. Now subtract 3 dB from this value. This is the -3 dB amplitude G\ :sub:`3dB1`. Now scroll back up the data looking for the entry in the channel 2 column that most closely matches G\ :sub:`3dB1`. Write down the frequency value that corresponds to this amplitude. This will be the F\ :sub:`3dB1` value.

Using the equations we presented earlier calculate the values for C\ :sub:`m` and C\ :sub:`stray`.

Step 2 Directions:
------------------

The second step is to measure just the single row capacitance, C\ :sub:`row`, between adjacent rows with the second adjacent row floating. Remember that C\ :sub:`stray` is still present in this measurement. Connect the wires from the ADALM2000 module to your solder-less breadboard using the fly-wire connector that came with the Kit as shown in figure 4. Starting from the figure 3 configuration all you need to do is move the blue 2+ scope input wire to the row next to where AWG1 and scope 1+ wires are connected. The second black ground wire can be connected with the rest of the grounds tied to the bus strip.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abc_bb2.png
   :align: center
   :width: 600px

.. container:: centeralign

   **Figure 4 Measure single row coupling, opposite side floating**


.. _hardware-setup-1:

Hardware Setup:
---------------

Leave all the settings the same as in step 1. Using the Network Analyzer instrument in the Scopy software obtain a gain (attenuation) vs. frequency plot from 10 Hz to 10 MHz by running a single sweep and export the data to a second .csv file with a different name.

.. _procedure-1:

Procedure:
----------

Open the second saved data file in a spreadsheet program (Excel) and again scroll to near the end of the data at high frequencies where the attenuation level is essentially flat. Write down the channel 2 amplitude, this is G\ :sub:`HF2`. Now subtract 3 dB from this value. This is the -3 dB amplitude G\ :sub:`3dB2`. Now scroll back up the data looking for the entry in the channel 2 column that most closely matches G\ :sub:`3dB2`. Write down the frequency value that corresponds to this amplitude. This will be the F\ :sub:`3dB2` value.

Using the equations we presented earlier calculate the values for C\ :sub:`m` and C\ :sub:`stray` + C\ :sub:`row`. Using the measurements from step 1 for C\ :sub:`m` and C\ :sub:`stray` calculate C\ :sub:`row`. Compare the C\ :sub:`m` value you obtained from step 1 to what you calculated in step 2.

Step 3 Directions:
------------------

The third step is to measure the single row capacitance, C\ :sub:`row`, between adjacent rows with the second adjacent row grounded. This places a C\ :sub:`row` in parallel with C\ :sub:`m`. Remember that C\ :sub:`stray` is still present in this measurement. Connect the wires from the ADALM2000 module to your solder-less breadboard using the fly-wire connector that came with the Kit as shown in figure 5. Starting from the figure 4 configuration all you need to do is move the second black ground wire from the ground bus to the row to the left (opposite side) of the row that the blue 2+ scope wire is plugged into.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abc_bb3.png
   :align: center
   :width: 600px

.. container:: centeralign

   **Figure 5 Measure single row coupling, opposite side grounded**


.. _hardware-setup-2:

Hardware Setup:
---------------

Leave all the settings the same as in steps 1,2. Using the Network Analyzer instrument in the Scopy software obtain a gain (attenuation) vs. frequency plot from 10 Hz to 10 MHz by running a single sweep and export the data to a third .csv file with a different name.

.. _procedure-2:

Procedure:
----------

Open the third saved data file in a spreadsheet program (Excel) and again scroll to near the end of the data at high frequencies where the attenuation level is essentially flat. Write down the channel 2 amplitude, this is G\ :sub:`HF3`. Now subtract 3 dB from this value. This is the -3 dB amplitude G\ :sub:`3dB3`. Now scroll back up the data looking for the entry in the channel 2 column that most closely matches G\ :sub:`3dB3`. Write down the frequency value that corresponds to this amplitude. This will be the F\ :sub:`3dB3` value.

Using the equations we presented earlier calculate the values for C\ :sub:`m` + C\ :sub:`row` and C\ :sub:`stray` + C\ :sub:`row`. Using the measurements from steps 1,2 for C\ :sub:`m` and C\ :sub:`stray` calculate C\ :sub:`row` again. Compare the C\ :sub:`row` value you obtained from step 2 to what you calculated in step 3.

Step 4 Directions:
------------------

The fourth step is to measure the combined capacitance, C\ :sub:`row`, with adjacent rows on both sides of a row driven by AWG1. This places two C\ :sub:`row` in parallel so the coupling capacitance is now 2C\ :sub:`row`. Remember that C\ :sub:`stray` is still present in this measurement. Connect the wires from the ADALM2000 module to your solder-less breadboard using the fly-wire connector that came with the Kit as shown in figure 6. Starting from the figure 5 configuration all you need to do is to remove the second black ground wire and return it to the ground bus and add a short jumper wire from the row to the left of the row that the blue 2+ scope wire is plugged into to the row that AWG1 and Scope 1+ are connected.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abc_bb4.png
   :align: center
   :width: 600px

.. container:: centeralign

   **Figure 6 Measure two rows coupling from both sides.**


.. _hardware-setup-3:

Hardware Setup:
---------------

Leave all the settings the same as in steps 1,2,3. Using the Network Analyzer instrument in the Scopy software obtain a gain ( attenuation ) vs. frequency plot from 10 Hz to 10 MHz by running a single sweep and export the data to a fourth .csv file with a different name.

.. _procedure-3:

Procedure:
----------

Open the fourth saved data file in a spreadsheet program ( Excel ) and again scroll to near the end of the data at high frequencies where the attenuation level is essentially flat. Write down the channel 2 amplitude, this is G\ :sub:`HF4`. Now subtract 3 dB from this value. This is the -3 dB amplitude G\ :sub:`3dB4`. Now scroll back up the data looking for the entry in the channel 2 column that most closely matches G\ :sub:`3dB4`. Write down the frequency value that corresponds to this amplitude. This will be the F\ :sub:`3dB4` value.

Using the equations we presented earlier calculate the values for C\ :sub:`m` and C\ :sub:`stray` + 2C\ :sub:`row`. Using the measurements from steps 1,2,3 for C\ :sub:`m` and C\ :sub:`stray` calculate 2C\ :sub:`row`. Compare the value for C\ :sub:`row` and the value for C\ :sub:`m` you obtained from steps 2,3 to what you calculated in step 4.

Report all your measurements and show all your calculations in your lab report. Also be sure to include your measured gain vs. frequency plot for each step. Include any changes or improvements you might recommend to the measurement setup and / or technique used.

Extra Credit work:
------------------

For extra credit, verify your results by using your favorite circuit simulation software to simulate the model circuit using your measured values for C\ :sub:`m`, R\ :sub:`m`, C\ :sub:`stray` and C\ :sub:`row`. Figure 7 is a simulation schematic (SIMetrix or ADsimPE) that you can use as a guide for your simulations. Just change the values for Cm (Scope input capacitance) Crow (breadboard row to row capacitance) and Cstray (stray wiring capacitance).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/breadboard-stray-capacitance.png
   :align: center
   :width: 600px

.. container:: centeralign

   **Figure 7 Simulation schematic**


The SIMetrix schematic file can be sound in the Miscellaneous-Schematics folder.

Do the simulated F\ :sub:`3dB` and G\ :sub:`HF` agree with your Lab measured value?

**Return to Lab Activities** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/abc_e1.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/abc_e2.png
   :width: 300px
