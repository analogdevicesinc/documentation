Activity: BJT Current Mirror
============================

Objective:
----------

The goal of this activity is to study the BJT current source or current mirror. Important attributes for current sources include high output resistance with a wide range of voltage compliance and rejection of external variations such as power supply or temperature.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 2 - 1KΩ Resistors (values matched as close as possible, or measured to 3 digits or better)
| 2 - small signal NPN transistors (2N3904 or SSM2212)
| 1 - Dual Op AMP ( such as ADTL082 )
| 2 - 4.7uF decoupling capacitors

Directions:
-----------

The good way to measure the characteristics of the current mirror is to reuse the same basic configuration that was used in the common emitter BJT curve tracer experiments. The input and output resistors R\ :sub:`1` and R\ :sub:`2` are now both 1KΩ. Be sure to accurately measure (with the most significant figures possible) the actual values of R\ :sub:`1` and R\ :sub:`2`. This is to insure accurate measurement of the input and output current of the mirror. I\ :sub:`in` will be equal to the AWG2 output voltage at W1 divided by the value of R\ :sub:`1`. Iout will be the voltage measured by scope channel 2 divided by the value of R\ :sub:`2`. Diode connected Q\ :sub:`1` is connected across the base and emitter terminals of Q\ :sub:`2`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Current mirror test circuit


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6n_f2.png
   :align: center

.. container:: centeralign

   Figure 2 Breadboard Connection of Current mirror test circuit


Hardware Setup:
---------------

In the current mirror configuration, the op amp serves as a virtual ground at the mirror input (base) node to convert the voltage steps from AWG 2 ( W2 output ) into current steps through the 1KΩ resistor. The collector voltage is swept using a ramp from AWG 1(output W1). Load the stairstep.csv file, set amplitude to 3V peak-to-peak with the offset to 1.5V. V\ :sub:`CE` of output device Q\ :sub:`2` is measured differentially by scope inputs 1+, 1-. The mirror output current is measured by scope inputs 2+. 2- across 1KΩ resistor, R\ :sub:`2`. If you don't want to use the op-amp configuration the following simplified configuration can be used as well.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 Alt, Simple current mirror test circuit


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6n_f4.png
   :align: center

.. container:: centeralign

   Figure 4 Breadboard Connection of Simple current mirror test circuit


Procedure:
----------

Two identical transistors with the same base to emitter voltage will have the same collector current I\ :sub:`C`. The second transistor, Q\ :sub:`2`, in effect mirrors the current in the first, Q\ :sub:`1`. Remembering the collector current to base emitter voltage relationship for a bipolar transistor:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6_e1.png
   :align: center
   :width: 200px

| where I\ :sub:`S` = the saturation current, and is a constant
| V\ :sub:`BE` is the base emitter voltage
| The thermal voltage, KT/q = 25.8 mV at room temperature
| Identical transistors by definition have the same I\ :sub:`S`. In the simple current mirror, both transistors have the same V\ :sub:`BE`. Thus, both transistors will have the same I\ :sub:`C` and if base currents are ignored, Iin = Iout. Actually I\ :sub:`C1`\ is I\ :sub:`in` - (I\ :sub:`B1` + I\ :sub:`B2`).

Plot the two waveforms using the Oscilloscope provided by the Scopy tool.


|image1|

.. container:: centeralign

   Figure 5 Current Mirror waveforms, W2 at 10kHz Sample Rate


Questions:
----------

You are to measure I\ :sub:`in`, Rout seen into the collector of Q\ :sub:`2`, the current mirror gain = I\ :sub:`out`/I\ :sub:`in` and determine the Norton and Thevenin equivalent circuits for this mirror.

Current Mirror with Base Current Compensation
=============================================

Modify the simple mirror circuit by adding the base current compensation transistor Q\ :sub:`3` as shown below in figure 6.


|image2|

.. container:: centeralign

   Figure 6 Current Mirror with Base Current Compensation


.. _hardware-setup-1:

Hardware Setup
--------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6n_f7.png
   :align: center

.. container:: centeralign

   Figure 7 Breadboard Connection of Current Mirror with Base Current Compensation


.. _procedure-1:

Procedure
---------

Repeat the same procedure you followed for the simple mirror circuit.


|image3|

.. container:: centeralign

   Figure 8 Current Mirror waveforms, W2 at 10kHz Sample Rate


.. _questions-1:

Questions:
----------

In addition to the same quantities and graphs, does your data indicate any advantage to this circuit? Any disadvantages?

Add questions more here:

References, further reading:
----------------------------

http://en.wikipedia.org/wiki/Current_mirror

Wilson Current Mirror
=====================

Modify the simple mirror into a Wilson Mirror as shown below in figure 9. Repeat the same procedure you followed for the simple mirror circuit.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9 Wilson current mirror


.. _hardware-setup-2:

Hardware Setup
--------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6n_f10.png
   :align: center

.. container:: centeralign

   Figure 10 Breadboard Connection of Wilson current mirror


.. _procedure-2:

Procedure
---------

Repeat the same procedure you followed for the simple mirror circuit.


|image4|

.. container:: centeralign

   Figure 11 Current Mirror waveforms, W2 at 10kHz Sample Rate


.. _questions-2:

Questions:
----------

In addition to the same quantities and graphs, does your data indicate any advantage to this circuit? Any disadvantages?

Add questions more here:

.. _references-further-reading-1:

References, further reading:
----------------------------

http://en.wikipedia.org/wiki/Wilson_current_source

Widlar current mirror
=====================

Modify the simple mirror into a Widlar Mirror as shown below in figure 12. Repeat the same procedure you followed for the simple mirror circuit. In addition to the same quantities and graphs, does your data indicate any advantage to this circuit? Any disadvantages?

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 12 Widlar current mirror


.. _hardware-setup-3:

Hardware Setup
--------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6n_f13.png
   :align: center

.. container:: centeralign

   Figure 13 Breadboard Connection of Widlar current mirror


.. _procedure-3:

Procedure
---------

Repeat the same procedure you followed for the simple mirror circuit.


|image5|

.. container:: centeralign

   Figure 14 Current Mirror waveforms, W2 at 10kHz Sample Rate


.. _questions-3:

Questions:
----------

| 1. Use the output impedance of the simple mirror to determine the Early voltage for the NPN transistor. 2. Build a mirror using PNP transistors and use the output impedance of the simple mirror to determine the Early voltage for the PNP transistor. 3. The output impedance of a Widlar current mirror is approximately,
| R\ :sub:`out` = r\ :sub:`o`\ [1 + g\ :sub:`m`\ R\ :sub:`3`]
| where:
| r\ :sub:`o` = V\ :sub:`AF`/I\ :sub:`C`, V\ :sub:`AF` is the Early voltage.
| g\ :sub:`m` = I\ :sub:`C`/V\ :sub:`T` is the transconductance.
| R\ :sub:`E` is the emitter resistor.

How accurately does this formula predict the output impedance of the Widlar current mirror you constructed? 4. If base currents are not ignored, how is I\ :sub:`out` related to Iin in the simple current mirror? 5. If I need a second (or third) copy of I\ :sub:`in` how would I make it?

.. _references-further-reading-2:

References, further reading:
----------------------------

http://en.wikipedia.org/wiki/Widlar_current_source

low Input Headroom Mirror
=========================

.. _objective-1:

Objective:
----------

The goal of this activity is to study BJT current source or current mirror with lower input headroom requirements.

.. _materials-1:

Materials:
----------

| 2 - 1K Resistors
| 1 - 150K Resistor (or a 100K? in series with a 47K?)
| 2 - small signal NPN transistor (2N3904 or SSM2212)
| 1 - small signal PNP transistor (2N3096)

.. _directions-1:

Directions:
-----------

The diode configuration with nearly zero turn on voltage from activity 2 is used here, in figure 15, to make a current mirror. The current input node at the collector of Q\ :sub:`1` (base of PNP Q\ :sub:`3`) is now much closer to ground compared to the conventional current mirror. What advantages would this have over the conventional mirror?

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6_f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 15 Low input head room mirror


.. _hardware-setup-4:

Hardware Setup
--------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a6n_f16.png
   :align: center

.. container:: centeralign

   Figure 16 Breadboard Connection of Low input head room mirror


.. _procedure-4:

Procedure
---------

Repeat the same procedure you followed for the simple mirror circuit.


|image6|

.. container:: centeralign

   Figure 17 Current Mirror waveforms, W1 at 10kHz Sample Rate


Ideally the collector of PNP Q\ :sub:`3` would be connected to some negative voltage with respect to ground. Try connecting the collector of Q\ :sub:`3` to the negative board supply Vn. What happens? Can the input node of the mirror get even closer to ground now?

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/bjt_current_mirror_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/bjt_current_mirror_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/a6n_f5.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/a6_f3.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/a6n_f8.png
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/a6n_f11.png
   :width: 500px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/a6n_f14.png
   :width: 500px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/a6n_f17.png
   :width: 500px
