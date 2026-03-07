Activity: The BJT connected as a diode
======================================

Objective:
----------

The purpose of this activity is to investigate the forward and reverse current vs. voltage characteristics of a bipolar junction transistor (BJT) connected as a diode.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less Breadboard
| 1 - 1KΩ Resistor (or any similar value)
| 1 - small signal NPN transistor (2N3904)

Directions:
-----------

The current vs. voltage characteristics of the base-emitter junction of an NPN transistor can be measured using the ADALM2000 Lab hardware and the following connections. Set up the breadboard with waveform generator, W1, attached to one end of resistor R\ :sub:`1`. Also connect scope input 2+ here. Connect the base and collector of Q\ :sub:`1` to the opposite end of R\ :sub:`1` as shown in the diagram. The emitter of Q\ :sub:`1` is connected to ground. Connect scope input 2- and scope input 1+ to the base - collector node of Q\ :sub:`1`. (Scope input 1- can be optionally grounded as well).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a3_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 NPN diode connection diagram


Hardware Setup:
---------------

The waveform generator should be configured for a 100 Hz triangle wave with 6 volt amplitude peak-to-peak and 0 offset. The differential scope channel 2 (2+, 2-) measures the current in the resistor (and in the transistor). Scope channel 1 (1+) is connected to measure the voltage across the diode connected transistor. The current flowing through the transistor, is the voltage difference 2+ and 2- (which is the channel 2 voltage) divided by the resistor value (1KΩ).


|image1|

.. container:: centeralign

   Figure 2 NPN diode breadboard circuit


Procedure:
----------

Load the captured data in to a spreadsheet program like Excel and calculate the current. Plot the current vs. the voltage across the transistor (V\ :sub:`BE`). No current flows in the reverse direction. In the forward conduction region, the voltage, current relationship is logarithmic. If the current is plotted on a log scale the line should be straight.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/npn_diode_c_vs_v-wav.png

.. container:: centeralign

   Figure 3 NPN diode XY plot


.. image:: https://wiki.analog.com/_media/university/courses/electronics/npn_diode-wav.png
   :align: center

.. container:: centeralign

   Figure 4 NPN diode waveform


Questions:
----------

Derive the mathematical expression for the current, I\ :sub:`C`, given the voltage across the transistor V\ :sub:`BE`?

Reverse Breakdown Characteristics
=================================

.. _objective-1:

Objective:
----------

The purpose of this activity is to investigate the reverse break down voltage characteristics of the emitter base junction of a bipolar junction transistor (BJT) connected as a diode.

.. _materials-1:

Materials:
----------

| 1 - 100Ω Resistor
| 1 - small signal PNP transistor (2N3906)

.. _directions-1:

Directions:
-----------

Set up the breadboard with the waveform generator output attached to one end of the series connected resistor 100Ω R\ :sub:`1` and base and collector of Q\ :sub:`1` as shown in figure 2. The emitter is connected to the negative 5 Volt fixed power supply. Scope channel 1 (1+) is connected to the base - collector node while 1- is connected to the emitter node. Scope channel 2 measures the voltage across R\ :sub:`1` and thus the current through Q\ :sub:`1`. The PNP 2N3906 is chosen over the NPN 2N3904 because the PNP emitter base breakdown voltage is less than the +10 V max that can be generated using ADALM2000 while the NPN's is likely to be higher than 10 V.


|image2|

.. container:: centeralign

   Figure 5 PNP Emitter Base Reverse breakdown configuration


.. _hardware-setup-1:

Hardware Setup:
---------------

The waveform generator should be configured for a 100 Hz triangle wave with 10 volt amplitude peak-to-peak and 0 volt offset. Scope channel 1 (1+) is used to measure the voltage across the transistor. The setup should be configured with channel 2 connected across resistor R\ :sub:`1` (2+, 2-). Both channels should be set to 1 V per division. The current flowing through the transistor is the voltage difference between 2+ and 2- divided by the resistor value (100Ω).


|image3|

.. container:: centeralign

   Figure 6 PNP Emitter breadboard circuit


.. _procedure-1:

Procedure:
----------

The Lab hardware power supplies limits the maximum voltage available to less than 10 volts. The emitter base reverse breakdown voltage of many transistors is larger than this. In the configuration shown voltages between 0 volts and 10 volts ( W1 peak to peak swing ) can be measured.


|image4|

.. container:: centeralign

   Figure 7 PNP Emitter waveform


Capture the scope waveforms and export them into a spreadsheet program such as Excel. For the 2N3906 PNP used in the example, the breakdown voltage of the emitter base junction is around 8.5 volts.

.. _questions-1:

Questions:
----------

Disconnect the collector of Q\ :sub:`1`\ and leave it open. How does this change the breakdown voltage? Now connect the collector to the emitter. How does this change the breakdown voltage?

Try measuring the NPN 2N3904 emitter base reverse breakdown voltage. You can also check the emitter base breakdown voltage for the two power transistors, TIP31 and TIP32, which are included in the ADALP2000 Analog Parts Kit. Are they higher or lower than the PNP 2N3906 and is it lower than the +10 volts you can measure with this setup? If it is higher what could you add to the setup to allow you to measure higher breakdown voltages?

Lowering the effective forward voltage of the diode
===================================================

.. _objective-2:

Objective:
----------

The purpose of this activity is to investigate a circuit configuration with smaller forward voltage characteristics than that of a bipolar junction transistor (BJT) connected as a diode.

.. _materials-2:

Materials:
----------

| 1 - 1KΩ Resistor
| 1 - 150KΩ Resistor ( or 100KΩ in series with 47KΩ )
| 1 - small signal NPN transistor (2N3904)
| 1 - small signal PNP transistor (2N3906)

.. _directions-2:

Directions:
-----------

Set up the breadboard with waveform generator W1 attached to one end of the series connected resistor R\ :sub:`1` and collector of NPN Q\ :sub:`1` and the base of PNP Q\ :sub:`2` as shown in the diagram. The emitter of Q\ :sub:`1` is connected to ground. The collector of Q\ :sub:`2`\ is connected to Vn (-5V). The first end of Resistor R\ :sub:`2` is connected to Vp (+5V). The second end of R\ :sub:`2` is connected to the base of Q\ :sub:`1` and the emitter of Q\ :sub:`2`. Single ended input of scope channel 2 (2+) is connected to the collector of Q\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a3_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 8 Configuration to lower effective forward voltage drop of diode


.. _hardware-setup-2:

Hardware Setup:
---------------

The waveform generator should be configured for a 100 Hz triangle wave with 8 volt amplitude peak-to-peak and 2 volt offset. Scope channel 2 (2+) is used to measure the voltage across the transistor. The current flowing through the transistor, is the voltage difference between scope input 1+ and 1- divided by the resistor value (1K?).


|image5|

.. container:: centeralign

   Figure 9 Lower effective forward voltage drop of diode - breadboard circuit


.. _procedure-2:

Procedure:
----------

The turn on voltage of the "diode" is now about 100mV compared to 650mV for the simple diode connection in the first example. Plot the V\ :sub:`CE` of Q\ :sub:`1` as W1 is swept.


|image6|

.. container:: centeralign

   Figure 10 Lower effective forward voltage drop of diode - waveform


.. _questions-2:

Questions:
----------

Could the collector of the PNP Q\ :sub:`2` be connected to some other node such as ground? And what would be the effect?

The value of R\ :sub:`2` sets the current in Q\ :sub:`2`. What is the effect of increasing or decreasing the value of R\ :sub:`2`?

VBE Multiplier Circuit
======================

.. _objective-3:

Objective:
----------

Now that we have seen a way to make V\ :sub:`BE` effectively smaller, the purpose of this activity is to make V\ :sub:`BE` larger. Larger forward voltage characteristics than that of a single bipolar junction transistor (BJT) connected as a diode.

.. _materials-3:

Materials:
----------

| 2 - 2.2KΩ Resistors
| 1 - 1KΩ Resistor
| 1 - 5KΩ Variable resistor, potentiometer
| 1 - small signal NPN transistor (2N3904)

.. _directions-3:

Directions:
-----------

Set up the breadboard with waveform generator W1 attached to one end of resistor R\ :sub:`1` as indicated in figure 4. The emitter of Q\ :sub:`1` is connected to ground. Resistors R\ :sub:`2`, R\ :sub:`3` and R\ :sub:`4` form a voltage divider with the wiper of potentiometer R\ :sub:`3` connected to the base of Q\ :sub:`1`. The collector of Q\ :sub:`1` is connected to the second end of R\ :sub:`1` and the top of the voltage divider at R\ :sub:`2`. Scope channel 2 (2+) is connected to the collector of Q\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a3_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 11 V\ :sub:`BE` Multiplier configuration


.. _hardware-setup-3:

Hardware Setup:
---------------

The waveform generator should be configured for a 100 Hz triangle wave with 4 volt amplitude peak-to-peak and 2V offset. The Single ended input of scope channel 2+ is used to measure the voltage across the transistor. The setup should be configured with channel 1+ connected to display the output of generator W1 and channel 2+ connected to display the collector voltage of Q\ :sub:`1`. The current flowing through the transistor, is the voltage difference between the W1 measured by scope input 1+ and scope input 2+ divided by the resistor value (1KΩ).


|image7|

.. container:: centeralign

   Figure 12 V\ :sub:`BE` Multiplier breadboard circuit


.. _procedure-3:

Procedure:
----------

Starting with the potentiometer R\ :sub:`3` set at the middle of its range the voltage at the collector of Q\ :sub:`2` should be about 2 times V\ :sub:`BE`. With R\ :sub:`3` set to its minimum the voltage at the collector should be 9/2 (or 4.5) times V\ :sub:`BE`. With R\ :sub:`3` set to its maximum the voltage at the collector should be 9/7 times V\ :sub:`BE`.


|image8|

.. container:: centeralign

   Figure 13 V\ :sub:`BE` Multiplier breadboard waveform


.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/bjt_diode_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/bjt_diode_ltspice`
   


.. _questions-3:

Questions:
----------

How does the voltage vs current characteristics of this V\ :sub:`BE` multiplier compare to those of a simple diode connected transistor?

Aside from the position of the pot wiper, do the values of R\ :sub:`2`, R\ :sub:`3` and R\ :sub:`4` effect the shape of the I vs V curve? To arrive at an answer try using values much larger and much smaller than those listed above.

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/npn_diode-bb.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/a3_f2.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/pnp_emitter-bb.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/pnp_emitter-wav.png
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/loweff_vdrop-bb.png
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/loweff_vdrop-wav.png
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/vbe_multiplier-bb.png
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/vbe_multiplier-wav.png
