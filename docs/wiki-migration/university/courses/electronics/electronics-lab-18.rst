Activity: The CMOS Analog Switch - ADALM2000
============================================

Objective:
----------

The objective of this exercise is to explore the use of complementary MOS transistors as an analog voltage switch.

Concept:
--------

The ideal analog switch has no on-resistance, infinite off-impedance and zero time delay, and can handle large signal and common-mode voltages. Real analog switches made with MOS transistors meet none of these criteria, but if we understand the limitations of analog switches, most of these limitations can be overcome. The on-resistance is one of these limitations and this lab activity will attempt to characterize this switch specification.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - CD4007 CMOS transistor array
| 2 - NPN transistors (2N3904 or equivalent)
| 1 - 4.7 KΩ resistor
| |image1|

.. container:: centeralign

   CD4007 CMOS transistor array pinout


NMOS Directions:
----------------

Construct the test circuit shown in figure 1. The green boxes indicate connections to the connector on ADALM2000. NMOS and PMOS devices M\ :sub:`1` and M\ :sub:`2` are contained in the CD4007 package. All un-used pins can be left floating. To measure the resistance (Ron) of the MOS transistors we first need to force a known current through the resistance and then measure the voltage across the resistance. The two NPN devices Q\ :sub:`1` and Q\ :sub:`2` along with resistor R\ :sub:`1` form a current source with an output current of approximately 1 mA. The exact magnitude of this current is not important in that we are mainly interested in the change in the Ron of the MOS devices as the voltage at their source/drain varies over the range of between the plus and minus power supplies.

In this first test only NMOS device M\ :sub:`1` is turned on and PMOS device M\ :sub:`2` is turned off.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a18_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 NMOS Ron test circuit


Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a18_nmos_bb.JPG
   :align: center

.. container:: centeralign

   Figure 2 NMOS Ron test circuit Breadboard Connections


Procedure:
----------

Configure waveform generator 1 as a 100 Hz triangle wave with an amplitude of 9 volts peak-to-peak and an offset of +500 mV. This will swing the voltage on the NMOS switch transistor from +5 volts to -4 volts. We can not swing the voltage all the way to -5 volts because of the NPN current source Q\ :sub:`2`. Be sure to turn on the external user power supplies (Vp and Vn) before running the waveform generator. Configure the scope screen in XY mode with C1 on the X axis, and C2 (the voltage across the switch) on the Y axis. Use the math function to calculate the resistance (C2 / 1mA). Note: You can get a more precise estimate of the current source by measuring the voltage across R\ :sub:`1` and its actual resistance.


|image2|

.. container:: centeralign

   Figure 3 NMOS Ron X-Y trace


Questions:
----------

At what voltage does the NMOS devices turn off?

What happens to the source to drain voltage as the NMOS transistor turns off?

How does this affect the display on the scope screen?

PMOS Directions:
----------------

Now modify your circuit to look like figure 2 by connecting the gates of both M\ :sub:`1` and M\ :sub:`2` to the negative power supply Vn. In this second test only PMOS device M\ :sub:`2` is turned on and NMOS device M\ :sub:`1` is turned off.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a18_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 PMOS Ron test circuit


.. _hardware-setup-1:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a18_pmos_bb.JPG
   :align: center

.. container:: centeralign

   Figure 5 PMOS Ron test circuit Breadboard Connections


.. _procedure-1:

Procedure:
----------

Repeat the sweep of the voltage from waveform generator W1 and plot the on-resistance of just the PMOS transistor.


|image3|

.. container:: centeralign

   Figure 6 PMOS Ron X-Y trace


.. _questions-1:

Questions:
----------

At what voltage does the PMOS devices turn off?

What happens to the source to drain voltage as the PMOS transistor turns off?

How does this affect the display on the scope screen?

CMOS Directions:
----------------

Now modify your circuit to look like figure 3 by connecting the gate of M\ :sub:`1` to the positive power supply Vp and the gate of M\ :sub:`2` to the negative power supply Vn. In this last test both NMOS device M\ :sub:`1` and PMOS device M\ :sub:`2` is turned on.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a18_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 7 CMOS Ron test circuit


.. _hardware-setup-2:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a18_cmos_bb.JPG
   :align: center

.. container:: centeralign

   Figure 8 CMOS Ron test circuit Breadboard Connections


.. _procedure-2:

Procedure:
----------

Repeat the sweep of the voltage and plot the on resistance of the combined NMOS and PMOS transistors.


|image4|

.. container:: centeralign

   Figure 9 CMOS Ron X-Y trace


.. _questions-2:

Questions:
----------

Do either the NMOS or PMOS transistors ever turn off?

Are both the NMOS and PMOS ever off at the same time?

If an NMOS switch is used to connect two signal nodes that can have analog voltages that vary from 0 to 1V, what must be the value of the bulk and gate voltages for the switch to work properly?

What are the conditions for a PMOS switch?

For Further Study:
~~~~~~~~~~~~~~~~~~

| ADI Mini Tutorial on :adi:`Analog Switches <static/imported-files/tutorials/MT-088.pdf>`
| R\ :sub:`ON` Modulation in CMOS :adi:`Switches and Multiplexers <static/imported-files/tech_articles/99941520Ron_Modulati_Whitepaper.pdf>`
| :adi:`Switches and Multiplexers <library/analogdialogue/archives/45-05/switch_mux.html>`
| :adi:`On Building Physically Accurate Analog Switch Macromodels <media/en/analog-dialogue/raqs/raq-issue-173.pdf>`

Extra Challenge Activity:
=========================

Try measuring the Ron vs input voltage for other CMOS analog switches such as the CD4016, CD4066 quad switches or the CD4051, CD4052, and CD4053 analog multiplexers or the ADG419 SPDT analog switch or ADG333 quad SPDT switch. Compare your results to the Ron specified in the manufacturer product datasheets.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/cmos_analog_sw_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/cmos_analog_sw_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/a18_nmos_ss.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/a18_pmos_ss.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/a18_cmos_ss.png
   :width: 300px
