Activity: The MOS transistor connected as a diode
=================================================

Objective:
----------

The purpose of this activity is to investigate the forward and reverse current vs. voltage characteristics of a MOS field effect transistor (NMOS and PMOS) connected as a diode.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less Breadboard
| 1 - 100Ω Resistor
| 1 - ZVN2110A NMOS transistor
| 1 - ZVP2110A PMOS transistor

NMOS Directions:
----------------

The current vs. voltage characteristics of the gate source of an enhancement mode NMOS transistor can be measured using the ADALM2000 Lab hardware and the following connections. Set up the breadboard with the waveform generator, W1, attached to one end of resistor R\ :sub:`1`. Also connect scope input 2+ here. Connect the Gate and Drain of M\ :sub:`1` to the opposite end of R\ :sub:`1` as shown in the diagram. The Source of M\ :sub:`1` is connected to Vn. Connect scope input 2- and scope input 1+ to the gate - drain node of M\ :sub:`1`. (Scope input 1- is best grounded as well to reduce noise pickup). Be sure that the power supply (Vn) is turned off while you build your circuit. Once you are sure all your connections are correct then turn on the supply.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a3m_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 NMOS diode connection diagram


Hardware Setup:
---------------

The waveform generator should be configured for a 100 Hz triangle wave with 10 volt amplitude peak-to-peak and 0 offset. The differential scope channel 2 (2+, 2-) measures the current in the resistor (and in the transistor). The Single ended input of scope channel 1 (1+) is connected to measure the voltage across the transistor. The current flowing through the transistor is the voltage difference 2+ and 2- divided by the resistor value (100Ω).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/nmos_diode-bb.png

.. container:: centeralign

   Figure 2 NMOS diode Breadboard Circuit


Procedure:
----------

Load the captured data in to Excel and calculate the current. Calculate and plot the current vs. the voltage across the transistor (V\ :sub:`GS`). No current should flow in the reverse direction. In the forward conduction region, the voltage, current relationship should be quadratic. Also calculate and plot the square root of the current vs. the voltage across the transistor (V\ :sub:`GS`). Compare the shape of the two plots and comment.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 3 NMOS diode XY plot


Questions:
----------

By plotting the data measured for I\ :sub:`D` vs V\ :sub:`GS`, find and report values of V\ :sub:`TH` and K (W/L).

PMOS Directions:
----------------

Repeat the experiment using the PMOS device. The connections are similar and as shown on figure 4 below. You may notice that the polarity of the scope inputs has been reversed in this case. This is so that the direction of the voltage and currents on the scope screen will be similar to the NMOS case. The Source of M\ :sub:`1` is connected to Vp. Connect scope input 2+ and scope input 1- to the gate - drain node of M1. Be sure that the power supply (Vp) is turned off while you build your circuit. Once you are sure all your connections are correct then turn on the supplies.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a3m_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 PMOS diode connection diagram


.. _hardware-setup-1:

Hardware Setup:
---------------

The waveform generator should be configured for a 100 Hz triangle wave with 10 volt amplitude peak-to-peak and 0 offset. The differential scope channel 2 (2+, 2-) measures the current in the resistor (and in the transistor). The Single ended input of scope channel 1 (1-) is connected to measure the voltage across the transistor. The current flowing through the transistor is the voltage difference 2+ and 2- divided by the resistor value (100Ω).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/pmos_diode-bb.png

.. container:: centeralign

   Figure 5 PMOS diode Breadboard Circuit


.. _procedure-1:

Procedure:
----------

Load the captured data in to Excel and calculate the current. Calculate and plot the current vs. the voltage across the transistor (V\ :sub:`GS`). No current should flow in the reverse direction. In the forward conduction region, the voltage, current relationship should be quadratic. Also calculate and plot the square root of the current (I\ :sub:`D`) vs. the voltage across the transistor (V\ :sub:`GS`). Compare the shape of the two plots and comment.

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 6 PMOS diode XY plot


.. _questions-1:

Questions:
----------

By plotting the data measured for I\ :sub:`D` vs V\ :sub:`GS`, find and report values of V\ :sub:`TH` and K (W/L).

How do the V\ :sub:`TH` and K (W/L) values for the NMOS and PMOS compare?

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/mos_diode_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/mos_diode_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/nmos_diode_c_vs_v-wav.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/pmos_diode_c_vs_v-wav.png
   :width: 600px
