Activity: NMOS FET characteristic curves, For ADALM1000
=======================================================

Objective:
----------

The purpose of this activity is to investigate the drain current vs. gate voltage characteristics of an NMOS and PMOS FET transistors. The ADALP2000 kit of parts will contain a number of transistors, both NMOS and PMOS enhancement mode devices of various types, that can be used.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

NMOS ID> vs. VGS curves
-----------------------

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 1 - Small signal NMOS transistor (CD4007 or ZVN2110A)

NMOS device Directions:
~~~~~~~~~~~~~~~~~~~~~~~

The drain current vs. gate voltage characteristics of an NMOS transistor can be measured using the ALM1000 hardware and the following connections as shown in figure 1. Set up the breadboard with the channel A generator output attached to the gate terminal of M\ :sub:`1`. Connect the drain terminal of M\ :sub:`1` to the channel B generator output. Connect the source terminal of M\ :sub:`1` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4m_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 NMOS I\ :sub:`D` vs V\ :sub:`GS` setup


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz triangle wave with 4.5 volt Max and 1.0 volt Min. The channel B DC voltage source can be adjusted from 0 V to 5 V. The measurement channel CB-I measures the current in the drain of transistor.

Procedure:
~~~~~~~~~~

Load the captured data in to spreadsheet or other analysis software. Plot the drain current vs. the gate voltage of the transistor (V\ :sub:`GS`) for various DC voltages on the drain. No drain current should flow when V\ :sub:`GS` is less than V\ :sub:`TH`\ the threshold voltage of the transistor. The threshold voltage, V\ :sub:`TH`, can be both positive, for an enhancement mode, and negative, for a depletion mode device. When V\ :sub:`GS` is greater than V\ :sub:`TH`, the gate voltage to drain current relationship is quadratic. Now plot the drain current vs. the square of the gate voltage. The line should be approximately straight.

Future activities will rely on matching of the threshold voltage, V\ :sub:`TH`, of at least two FETs. You should record the V\ :sub:`TH`\ for each device you have available and sort them by their threshold voltages.

Questions:
~~~~~~~~~~

Insert further questions here.

NMOS ID vs. VDS curves
----------------------

.. _objective-1:

Objective:
~~~~~~~~~~

The purpose of this activity is to investigate the drain current I\ :sub:`D` vs. drain to source voltage V\ :sub:`DS` characteristic curves of an NMOS FET transistor.

.. _materials-1:

Materials:
~~~~~~~~~~

1 - Small signal NMOS transistor (CD4007 or ZVN2110A)

NMOS Directions:
~~~~~~~~~~~~~~~~

Starting with the previous breadboard setup, Move the CA-V triangle wave generator drain of the transistor. Now place CV-B generator on the gate terminal.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4m_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 NMOS I\ :sub:`D` vs V\ :sub:`DS` setup


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

The setup is the same as the previous experiment except now measurement channel CA-I is set to display the transistor I\ :sub:`DS`. The drain voltage is swept using a 5 volt Max, 0 V Min triangle wave. V\ :sub:`DS` is measured by CA-V.

A stair-step waveform will be needed to drive the gate of the transistor. Set the Channel B generator output to the 10 level stair-step waveform. Set the frequency to 20Hz, the Max to 4.25 V and the Min to 1.25 V. The extra 1.25 volts is an initial estimate of V\ :sub:`TH`. The waveform in the display should start at 1.25 V and increase in 0.3 V increments to 4.25 V. Set the channel A generator to a triangle wave with a Max of 5.0 V and a Min of 0 V (wave should swing from 0 to 5V). Set the frequency to 200 Hz ( 10 times the 20 Hz of channel B). Comparing the waveforms in channel A and channel B, the triangle wave in channel A should go through one cycle from 0 to 5 V and back to zero during the time of one step in the waveform in channel B. Adjust the phases of channel A and/or channel B to make them line up in this way if they do not.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Once the V\ :sub:`TH` of the device is known from the previous measurement, the starting offset for the stair step waveform used on the gate, from generator CB-V, can be established. The height of the steps should be set, or adjusted according to the gain (mA/V\ :sup:`2`) of the transistor being measured. This can also be gotten from the previous I\ :sub:`D` vs. V\ :sub:`GS` data.

.. _questions-1:

Questions:
~~~~~~~~~~

Insert further questions here.

PMOS ID vs. VGS curves
----------------------

.. _materials-2:

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 1 - Small signal PMOS transistor (CD4007 or ZVP2110A)

PMOS device Directions:
~~~~~~~~~~~~~~~~~~~~~~~

The drain current vs. gate voltage characteristics of a PMOS transistor can be measured using the ALM1000 hardware. To measure the PMOS device, alter the characteristic curve measurement circuit as shown in figure 3. The connections are not very different from those in figure 1 but the polarity of the voltage waveforms generated by channel A and channel B must now be negative with respect to the PMOS source. To accommodate this the source is now connected to +5 V. Set up the breadboard with the channel A generator output attached to the gate terminal of M\ :sub:`1`. Connect the drain terminal of M\ :sub:`1` to the channel B generator output.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4m_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 PMOS I\ :sub:`D` vs V\ :sub:`GS` setup


You can use the same step staircase waveform you used for the NMOS device to drive the gate voltage for the PMOS device. However, you will need to set the Max to +5 V - V\ :sub:`TH` or 3.8 V and set the Min to 0.8 V. The waveform in the display should now start at 3.8 V and decrease in 0.3 V increments to 0.8 V.

.. _hardware-setup-2:

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz triangle wave with 3.5 volt Max and 1.0 volt Min. The channel B DC voltage source can be adjusted from 0 V to 5 V. The measurement channel CB-I measures the current in the drain of transistor.

.. _procedure-2:

Procedure:
~~~~~~~~~~

Load the captured data in to spreadsheet or other analysis software. Plot the drain current vs. the gate voltage of the transistor (V\ :sub:`GS`) for various DC voltages on the drain. No drain current should flow when V\ :sub:`GS` is less than V\ :sub:`TH`\ the threshold voltage of the transistor. The threshold voltage, V\ :sub:`TH`, can be both positive, for an enhancement mode, and negative, for a depletion mode device. When V\ :sub:`GS` is greater than V\ :sub:`TH`, the gate voltage to drain current relationship is quadratic. Now plot the drain current vs. the square of the gate voltage. The line should be approximately straight.

Future activities will rely on matching of the threshold voltage, V\ :sub:`TH`, of at least two FETs. You should record the V\ :sub:`TH`\ for each device you have available and sort them by their threshold voltages.

.. _questions-2:

Questions:
~~~~~~~~~~

Insert further questions here.

PMOS ID vs. VDS curves
----------------------

.. _objective-2:

Objective:
~~~~~~~~~~

The purpose of this activity is to investigate the drain current I\ :sub:`D` vs. drain to source voltage V\ :sub:`DS` characteristic curves of an PMOS FET transistor.

.. _materials-3:

Materials:
~~~~~~~~~~

1 - Small signal PMOS transistor (CD4007 or ZVP2110A)

PMOS Directions:
~~~~~~~~~~~~~~~~

Starting with the previous breadboard setup, Move the CA-V triangle wave generator drain of the transistor. Now place CV-B generator on the gate terminal.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab4m_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 PMOS I\ :sub:`D` vs V\ :sub:`DS` setup


.. _hardware-setup-3:

Hardware Setup:
~~~~~~~~~~~~~~~

The setup is the same as the previous experiment except now measurement channel CA-I is set to display the transistor I\ :sub:`DS`. The drain voltage is swept using a 5 volt Max, 0 V Min triangle wave channel B generator. V\ :sub:`DS` is measured by CA-V.

A stair-step waveform will be needed to drive the gate of the transistor. Set the Channel B generator output to the 10 level stair-step waveform. Set the frequency to 20Hz, the Max to 4.25 V and the Min to 1.25 V. The extra 1.25 volts is an initial estimate of V\ :sub:`TH`. The waveform in the display should start at 1.25 V and increase in 0.3 V increments to 4.25 V. Set the channel A generator to a triangle wave with a Max of 5.0 V and a Min of 0 V (wave should swing from 0 to 5V). Set the frequency to 200 Hz ( 10 times the 20 Hz of channel B). Comparing the waveforms in channel A and channel B, the triangle wave in channel A should go through one cycle from 0 to 5 V and back to zero during the time of one step in the waveform in channel B. Adjust the phases of channel A and/or channel B to make them line up in this way if they do not.

.. _procedure-3:

Procedure:
~~~~~~~~~~

Once the V\ :sub:`TH` of the device is known from the previous measurement, the starting offset for the stair step waveform used on the gate, from generator CB-V, can be established. The height of the steps should be set, or adjusted according to the gain (mA/V\ :sup:`2`) of the transistor being measured. This can also be gotten from the previous I\ :sub:`D` vs. V\ :sub:`GS` data.

.. _questions-3:

Questions:
~~~~~~~~~~

Insert further questions here.

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/nmos_fet_char_curves_ltspice`
-  Fritzing files: :git-education_tools:`m1k/fritzing/nmos_fet_char_curves_bb`

**For Further Reading:**

http://en.wikipedia.org/wiki/MOSFET

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
