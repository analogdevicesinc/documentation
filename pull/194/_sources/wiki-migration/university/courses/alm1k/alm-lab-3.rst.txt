Activity: The BJT connected as a diode, For ADALM1000
=====================================================

Objective:
----------

The purpose of this activity is to investigate the forward and reverse current vs. voltage characteristics of a bipolar junction transistor (BJT) connected as a diode.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

The Diode Connected NPN transistor
----------------------------------

Materials:
~~~~~~~~~~

| ADALM1000 Hardware Module
| Solder-less Breadboard
| 1 - 470 Ω Resistor (or any similar value)
| 1 - small signal NPN transistor (2N3904)

Directions:
~~~~~~~~~~~

The current vs. voltage characteristics of the base-emitter junction of an NPN transistor can be measured using the ALM1000 module and the following connections. Set up the breadboard with the channel A generator, CA-V, attached to one end of resistor R\ :sub:`1`. Connect the base and collector of Q\ :sub:`1` to the opposite end of R\ :sub:`1` as shown in the diagram. The emitter of Q\ :sub:`1` is connected to ground. Connect channel B scope input, CB-H, to the base - collector node of Q\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab3_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 NPN diode connection diagram


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz triangle wave with a 5 volt Max and 0 volt Min. The channel A ammeter function (CA-I) measures the current in the resistor (and in the transistor). Scope channel B is connected to measure the voltage across the transistor. The current flowing through the transistor, can also be calculated as the voltage difference CA-V - CB-V math waveform divided by the resistor value (470 Ω for example).

Procedure:
~~~~~~~~~~

Load the captured data in to a spreadsheet program like Excel and calculate the current. Plot the current ( measured and calculated ) vs. the voltage across the transistor (V\ :sub:`BE`). No current flows in the reverse direction. In the forward conduction region, the voltage, current relationship is logarithmic. If the current is plotted on a log scale the line should be straight.

Questions:
~~~~~~~~~~

Derive the mathematical expression for the current, I\ :sub:`C`, given the voltage across the transistor V\ :sub:`BE`?

Reverse Breakdown Characteristics
---------------------------------

.. _objective-1:

Objective:
~~~~~~~~~~

The purpose of this activity is to investigate the reverse break down voltage characteristics of the emitter base junction of a bipolar junction transistor (BJT) connected as a diode.

.. _materials-1:

Materials:
~~~~~~~~~~

| 1 - 100 Ω Resistor (or any similar value)
| 1 - small signal PNP transistor (2N3906)
| 4.5 volt battery ( three AA cells in series for example )

.. _directions-1:

Directions:
~~~~~~~~~~~

Set up the breadboard with the channel A generator output attached to one end of the series connected resistor 100 ? R\ :sub:`1` and base and collector of Q\ :sub:`1` as shown in figure 2. The emitter is connected to the negative 4.5 Volt fixed battery voltage. The channel B scope input, CB-H, is connected to the base - collector node. Scope trace CA-I measures the current through Q\ :sub:`1`. The PNP 2N3906 is chosen over the NPN 2N3904 because the PNP emitter base breakdown voltage is less than the +9.5 V max that can be generated using ALM1000 and the external 4.5V battery while the NPN's is likely to be higher than 10 V.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab3_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 PNP Emitter Base Reverse breakdown configuration


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz triangle wave with 5 volt Max and 0 volt Min. Scope channel B is used to measure the voltage across the transistor. Both channels should be set to 0.5 V per division. The current flowing through the transistor is the current measured in channel A (CA-I) or the Math trace voltage difference between CA-V - CB-V divided by the resistor value (100 Ω).

.. _procedure-1:

Procedure:
~~~~~~~~~~

The ALM1000 hardware power supply limits the maximum voltage available to 5 volts. The emitter base reverse breakdown voltage of many transistors is larger than this. In the configuration shown, voltages between 4.5 volts and 9.5 volts ( CA-V peak to peak swing + external battery voltage ) can be measured.

Capture the scope waveforms and export them into a spreadsheet program such as Excel. For the 2N3906 PNP used in the example, the breakdown voltage of the emitter base junction should be around 8.5 volts. Remember to add the 4.5 V offset from the external battery to your calculations. Be sure to measure the actual battery voltage for the most accurate measurements.

.. _questions-1:

Questions:
~~~~~~~~~~

| Disconnect the collector of Q\ :sub:`1`\ and leave it open. How does this change the breakdown voltage?
| Now connect the collector to the emitter. How does this change the breakdown voltage?

Try measuring the NPN 2N3904 emitter base reverse breakdown voltage. You can also check the emitter base breakdown voltage for the two power transistors, TIP31 and TIP32, which are included in the Analog Parts Kit. Are they higher or lower than the PNP 2N3906 and is it lower than the +9.5 volts you can measure with this setup? If it is higher what could you change in the setup to allow you to measure higher breakdown voltages?

Lowering the effective forward voltage of the diode
---------------------------------------------------

.. _objective-2:

Objective:
~~~~~~~~~~

The purpose of this activity is to investigate a circuit configuration with smaller forward voltage characteristics than that of a bipolar junction transistor (BJT) connected as a diode.

.. _materials-2:

Materials:
~~~~~~~~~~

| 1 - 1KΩ Resistor
| 1 - 150KΩ Resistor ( or 100KΩ in series with 47KΩ )
| 1 - small signal NPN transistor (2N3904)
| 1 - small signal PNP transistor (2N3906)

.. _directions-2:

Directions:
~~~~~~~~~~~

Set up the breadboard, as shown in figure 3, with the channel A generator attached to one end of the series connected resistor R\ :sub:`1` and collector of NPN Q\ :sub:`1` and the base of PNP Q\ :sub:`2`. The emitter of Q\ :sub:`1` is connected to ground. The collector of Q\ :sub:`2`\ is connected to ground. The first end of Resistor R\ :sub:`2` is connected to +5V. The second end of R\ :sub:`2` is connected to the base of Q\ :sub:`1` and the emitter of Q\ :sub:`2`. The channel B scope input, CB-H, is connected to the collector of Q\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab3_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 Configuration to lower effective forward voltage drop of diode


.. _hardware-setup-2:

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz triangle wave with 5 volt Max and 0 volt Min. Scope channel B is used to measure the voltage across the transistor. The current flowing through the transistor is the current measured in channel A (CA-I) or the Math trace voltage difference between CA-V - CB-V divided by the resistor value (1 KΩ).

.. _procedure-2:

Procedure:
~~~~~~~~~~

The turn on voltage of the "diode" is now about 100mV compared to 650mV for the simple diode connection in the first example. Plot the V\ :sub:`CE` of Q\ :sub:`1` as CA-V is swept.

.. _questions-2:

Questions:
~~~~~~~~~~

| Could the collector of the PNP Q\ :sub:`2` be connected to some other node such as a negative supply voltage?
| And what would be the effect?

The value of R\ :sub:`2` sets the current in Q\ :sub:`2`. What is the effect of increasing or decreasing the value of R\ :sub:`2`?

VBE Multiplier Circuit
----------------------

.. _objective-3:

Objective:
~~~~~~~~~~

Now that we have seen a way to make V\ :sub:`BE` effectively smaller, the purpose of this activity is to make V\ :sub:`BE` larger. Larger forward voltage characteristics than that of a single bipolar junction transistor (BJT) connected as a diode.

.. _materials-3:

Materials:
~~~~~~~~~~

| 2 - 2.2 KΩ Resistors
| 1 - 1 KΩ Resistor
| 1 - 5 KΩ Variable resistor, potentiometer
| 1 - small signal NPN transistor (2N3904)

.. _directions-3:

Directions:
~~~~~~~~~~~

Set up the breadboard, as shown in figure 4, with the channel A generator attached to one end of resistor R\ :sub:`1`. The emitter of Q\ :sub:`1` is connected to ground. Resistors R\ :sub:`2`, R\ :sub:`3` and R\ :sub:`4` form a voltage divider with the wiper of potentiometer R\ :sub:`3` connected to the base of Q\ :sub:`1`. The collector of Q\ :sub:`1` is connected to the second end of R\ :sub:`1` and the top of the voltage divider at R\ :sub:`2`. Scope channel B is connected to the collector of Q\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab3_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4 V\ :sub:`BE` Multiplier configuration


.. _hardware-setup-3:

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz triangle wave with 5 volt Max and 0 V Min. The input of scope channel B is used to measure the voltage across the transistor. The software should be configured to display CA-V and channel CB-V, the collector voltage of Q\ :sub:`1`. The current flowing through the transistor is the current measured in channel A (CA-I) or the Math trace voltage difference between CA-V - CB-V divided by the resistor value (1 KΩ).

.. _procedure-3:

Procedure:
~~~~~~~~~~

Starting with the potentiometer R\ :sub:`3` set at the middle of its range the voltage at the collector of Q\ :sub:`2` should be about 2 times V\ :sub:`BE`. With R\ :sub:`3` set to its minimum the voltage at the collector should be 9/2 (or 4.5) times V\ :sub:`BE`. With R\ :sub:`3` set to its maximum the voltage at the collector should be 9/7 times V\ :sub:`BE`.

.. _questions-3:

Questions:
~~~~~~~~~~

How does the voltage vs current characteristics of this V\ :sub:`BE` multiplier compare to those of a simple diode connected transistor?

Aside from the position of the potentiometer wiper, do the values of R\ :sub:`2`, R\ :sub:`3` and R\ :sub:`4` effect the shape of the I vs V curve? To arrive an answer try using values much larger and much smaller than those listed above.

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/bjt_as_diode_ltspice`
-  Fritzing files: :git-education_tools:`m1k/fritzing/bjt_as_diode_bb`

**For Further Reading:**

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
