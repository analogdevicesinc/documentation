Activity: NMOS FET characteristic curves - ADALM2000
====================================================

ID vs. VGS curves
=================

Objective:
----------

The purpose of this activity is to investigate the drain current vs. gate voltage characteristics of an NMOS FET transistor.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - 100Ω resistor
| 1 - Small signal NMOS transistor (CD4007 or ZVN2110A)

Directions:
-----------

The drain current vs. gate voltage characteristics of an NMOS transistor can be measure using the ADALM2000 Lab hardware and the following connections as shown in figure 1. Set up the breadboard with the arbitrary waveform generator output W1 attached to the gate terminal of M\ :sub:`1`. Connect one end of resistor R\ :sub:`1` to both the positive Vp supply and the 2+ scope input. Connect the opposite end of resistor R\ :sub:`1` to both the drain of M\ :sub:`1` and scope inputs 2- and 1+. The source of M\ :sub:`1` is connected to ground.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4m_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 NMOS I\ :sub:`D` vs V\ :sub:`GS` setup


Hardware Setup:
---------------

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 2 NMOS I\ :sub:`D` vs V\ :sub:`GS` breadboard circuit


The arbitrary waveform generator should be configured for a 100 Hz triangle wave with 2.5 volt amplitude peak-to-peak and 1.25 volt offset. The differential scope channel 2 (2+/-) measures the current in the resistor (and in the transistor). Scope channel 1 should be connected to display the output of the waveform generator. The current flowing through the transistor is the voltage difference 2+ and 2- divided by the resistor value (100Ω).

Procedure:
----------

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 3 NMOS I\ :sub:`D` vs V\ :sub:`GS` XY plot


Load the captured data in to Excel and calculate the current. Plot the drain current vs. the gate voltage of the transistor (V\ :sub:`GS`). No drain current should flow when V\ :sub:`GS` is less than V\ :sub:`TH`\ the threshold voltage of the transistor. The threshold voltage, V\ :sub:`TH`, can be both positive, for an enhancement mode, and negative, for a depletion mode device. When V\ :sub:`GS` is greater than V\ :sub:`TH`, the gate voltage to drain current relationship is quadratic. Now plot the drain current vs. the square of the gate voltage. The line should be straight as seen in the second plot.

Future activities will rely on matching of the threshold voltage, V\ :sub:`TH`, of at least two FETs. You should record the V\ :sub:`TH`\ for each device you have available and sort them by their threshold voltages.

Questions:
----------

Add Questions here:

ID vs. VDS curves
=================

.. _objective-1:

Objective:
----------

The purpose of this activity is to investigate the drain current I\ :sub:`D` vs. drain to source voltage V\ :sub:`DS` characteristic curves of an NMOS FET transistor.

.. _materials-1:

Materials:
----------

| 1 - 100Ω resistor
| 1 - Small signal NMOS transistor (CD4007 or ZVN2110A)

.. _directions-1:

Directions:
-----------

Starting with the previous breadboard setup, Remove the Vp supply connection and replace it with W1 taken from the gate terminal. Now place W2 on the gate terminal (in place of W1).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4m_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 NMOS I\ :sub:`D` vs V\ :sub:`DS` setup


.. _hardware-setup-1:

Hardware Setup:
---------------

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   Figure 5 NMOS I\ :sub:`D` vs V\ :sub:`DS` breadboard circuit


The setup is the same as the previous experiment except now Scope channel 1 is set to display the transistor V\ :sub:`DS`. The drain voltage is swept using a 3 volt peak to peak ramp with an offset equal to 1.5V from the arbitrary waveform generator. V\ :sub:`DS` is measured by single ended scope input 1+. The drain current is measured by differential scope input 2+/- across the 100Ω resistor R\ :sub:`1`.

A stair-step waveform will be needed to drive the gate of the transistor. Using the buffer in the Scopy Signal Generator tool, construct a stair-step waveform with 5 levels on channel 2 (W2). Load the following csv file (extract from archive): `stair-step.zip <https://wiki.analog.com/_media/university/courses/electronics/stair-step.zip>`_. Set the amplitude to 3V peak-to-peak and sampleRate to 100Hz.

.. _procedure-1:

Procedure:
----------

.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   Figure 6 NMOS I\ :sub:`D` vs V\ :sub:`DS` waveforms


Once the V\ :sub:`TH` of the device is known from the previous measurement, the starting offset for the stair step waveform used on the gate, from waveform generator 2, can be established. The height of the steps should be set, or adjusted according to the gain (mA/V\ :sup:`2`) of the transistor being measured. This can also be gotten from the previous I\ :sub:`D` vs. V\ :sub:`GS` data.

.. _questions-1:

Questions:
----------

Add questions here:

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/nmos_i_vs_v_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/nmos_curve_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/nmos_id_vs_vgs-bb.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/nmos_id_vs_vgs-xy.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/nmos_id_vs_vgs-bb2.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/nmos_id_vs_vgs-wav.png
