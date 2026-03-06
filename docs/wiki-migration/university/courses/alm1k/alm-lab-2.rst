Activity: Diode current vs. voltage curves, For ADALM1000
=========================================================

Objective:
----------

The purpose of this activity is to investigate the current vs. voltage characteristics of various solid state PN junction diodes such as the conventional Si diode, the Schottky barrier diode, the Zener diode and Light emitting diode (LED).

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

The PN junction diode is a device which is commonly used in circuit applications such as rectification where current is allowed to flow in only one direction. When the diode is fabricated in silicon, the forward voltage drop is typically 0.7 V and the V\ :sub:`D` vs. I\ :sub:`D` characteristic relating diode voltage and current can be described by an exponential relationship:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab2-e1.png
   :align: center
   :width: 200px

where I\ :sub:`S` and n are scale factors, and kT/q (˜ 25.4 mV at room temperature) is the so called thermal voltage V\ :sub:`T`.

Diode schematic symbols:
~~~~~~~~~~~~~~~~~~~~~~~~

Each type of diode has a specific schematic symbol which are variations of the conventional diode symbol shown on the left in figure 1. A sort of "Z" shaped cathode denotes a zener diode as in the second symbol in figure 1. An "S" shaped cathode denotes a Schottky diode as in the next symbol. The arrows pointing away from the diode denotes an LED as in the symbol on the right. Arrows pointing toward the diode would represent a photo diode light detector.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab2-f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1, Diode schematic symbols


Zener Diode Fundamentals:
~~~~~~~~~~~~~~~~~~~~~~~~~

A Zener diode is similar in construction and operation to an ordinary diode. Unlike a conventional diode where the intended use is to prevent current in the reverse direction, a zener diode is mostly used in the reverse region above the breakdown voltage. Its I vs, V characteristic curve is similar to ordinary diode. By adjusting the doping of the P and N sides of the junction, it is possible to design a Zener diode that breaks down at anywhere from a few volts to a few hundred volts. See Figure 2. In this breakdown or zener region the diode voltage will remain approximately constant over a wide range of currents. The maximum reverse-bias potential that can be applied before entering the Zener region is called the Peak Inverse Voltage (PIV) or the Peak Reverse Voltage (PRV).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab2-f2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2, Forward and reverse zener diode I/V characteristics


At voltages above the onset of breakdown, an increase in applied voltage will cause more current to flow in the diode, but the voltage across the diode will stay very nearly at V\ :sub:`Z`. A Zener diode operated in reverse breakdown can provide a reference voltage for systems like voltage regulators or voltage comparators.

Schottky Diode Fundamentals:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Schottky barrier diode uses a rectifying metal-semiconductor junction formed by plating, evaporating or sputtering one of a variety of metals onto n-type or p-type semiconductor material. Generally, n-type silicon and n-type GaAs are used in commercially available Schottky diodes. The properties of a forward biased Schottky barrier diode are determined by majority carrier phenomena. A conventional PN junction diode's properties are determined by minority carriers. Schottky diodes are majority carrier devices that can be switched rapidly from forward to reverse bias without minority carrier storage effects.

The normal current vs. voltage (I/V) curve of a Schottky barrier diode resembles that of a PN junction diode with the following exceptions:

| 1. The reverse breakdown voltage of a Schottky barrier diode is lower and the reverse leakage current higher than those of a PN junction diode made using the same resistivity semiconductor material.
| 2. The forward voltage at a specific forward current is also lower for a Schottky barrier diode than for a PN junction diode. For example, at 2 mA forward bias current a low barrier silicon Schottky diode will have a forward voltage of ~0.3 volts while a silicon PN junction diode will have a voltage of ~0.7 volts. This lower forward voltage drop can cut the power dissipated in the diode by more than one half. This power savings can be very significant when the diodes need to carry large forward currents. The current vs. voltage (I/V) relationship for a Schottky barrier diode is given by the following equation known as the Richardson equation. The primary difference from the conventional diode equation is in I\ :sub:`S` with the addition of the modified Richardson constant A\*.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab2-e1.png
   :align: center
   :width: 200px

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab2-e2.png
   :align: center
   :width: 200px

| Where:
| A = junction area
| A\* = modified Richardson constant (value varies by material and dopant) = 110 A/(°K\ :sup:`2`-cm\ :sup:`2`) for n-type Si
| T = absolute temperature in ºK
| q = electronic charge = 1.6 \* 10\ :sup:`-19` C
| f\ :sub:`B` = barrier height in volts k = Boltzman's constant = 1.37 \* 10\ :sup:`-23` J/K
| n = ideality factor (forward slope factor, determined by metal-semiconductor interface)

LED Fundamentals:
~~~~~~~~~~~~~~~~~

The LED is a junction diode that emits light when forward biased. Actually all PN junction diodes emit photons when forward biased, it is just that the photons are in the infrared band and the physical shape of the diode does not allow the photons to escape the package. To achieve the visible light emitting property, it is necessary to fabricate the LED from materials with larger band-gaps other than silicon. As a result, the forward voltage drop of the LED is greater than 0.7V; usually on the order of 1.5 to 2 volts depending on the wavelength of the emitted light. The LED is also built in a special transparent package as shown in figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab2-f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, Light emitting diodes


An LED is a semiconductor device that emits electromagnetic radiation at optical and infrared frequencies. The device is a PN junction diode made from p-type and n-type semiconductors, usually GaAs, GaP or SiC. They emit light only when an external applied voltage is used to forward bias the diode above a minimum threshold value. The gain in electrical potential energy delivered by this voltage is sufficient to force electrons to flow out of the n-type material, across the junction barrier, and into the p-type region. This threshold voltage for the onset of current flow across the junction and the production of light is V\ :sub:`0`. The emission of light occurs after electrons enter into the p-region (and holes into the n-region). These electrons are a small minority surrounded by holes (essentially the anti-particles of the electrons) and they will quickly find a hole to recombine with. Energetically, the electron relaxes from the excited state (conduction band) to the ground state (valence band). The diodes are called light emitting because the energy given up by the electron as it relaxes is emitted as a photon. Above the threshold value, the current and light output increases exponentially with the bias voltage across the diode. The quanta of energy or photon has an energy E = hf. The relation between the photon energy and the turn-on voltage V\ :sub:`0`, is:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab2-e3.png
   :align: center
   :width: 200px

| Where:
| E\ :sub:`g` is the size of the energy gap
| V\ :sub:`0` is the threshold voltage
| f and λ are the frequency and wavelength of the emitted photons
| c is the velocity of light
| e is the electronic charge
| h is Planck's constant

Lab Experiments:
----------------

You will be making I vs. V measurements on various types of diodes in this part of the Lab.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less Breadboard
| 1 - Resistor (47 Ω or any similar value from 47 Ω to 1 KΩ)
| 1 - Conventional diode (1N4001 or similar)
| 1 - Schottky diode (1N5817 or similar)
| 1 - 6.2 volt Zener diode (1N4735 or similar)
| Various - LED diode ( 5mm red, yellow, green, blue or white etc.)

Directions:
~~~~~~~~~~~

The current vs. voltage characteristics of the PN junction diode can be measured using the M1000 module and the following connections shown in figure 4. The green boxes indicate where to connect the ALM1000. Set up the breadboard with the channel A generator output attached to one end of the resistor. The other end of the resistor is connected to one end of the diode being measured as shown in the diagram. The channels B input is also connected to the second end of the resistor. The other end of the diode is connected to ground. Be sure to note the proper polarity of the diode.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab2-f4.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 4, Connection diagram for diode I vs. V curves


Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz triangle wave with 3 volt Max and 0 volt Min. The channel A current trace is used to measure the current in the resistor (and diode). The scope channel B is used to measure the voltage across the diode. The vertical range should be setup with channel A at 5mA per division and channel B set also at 0.2V per division. The current flowing through the diode, I\ :sub:`D`, is also the voltage measured across the resistor (100 Ω in this example). The Math trace that is the difference of CA-V - CB-V divided by the resistor is also the current. Use the XY display mode to plot the voltage across the diode (channel B-V) on the X axis vs. the current in the diode (CA-I) on the Y axis.

Procedure:
~~~~~~~~~~

Load the captured data for each type of diode into a data analysis software program like MATLAB or a spreadsheet (Excel) and calculate the diode current I\ :sub:`D`. Plot the current vs. the forward bias voltage across the diode. The diode voltage, current relationship should be logarithmic. If plotted on log scale the line should be straight.

LED data analysis:
~~~~~~~~~~~~~~~~~~

As was discussed in the background section on LEDs, the I/V relationship of different color (i.e. wavelength) LEDs might be used to measure Planck's constant. The datasheets for your various color LEDs should list the wavelength of the light emitted. Use those numbers in your calculations.

One method to consider begins with plotting the I/V data for each color LED on a semi-log graph. Your data should approximate a straight line, indicative of the exponential nature of the current vs. voltage relationship. An operational definition of the threshold voltage could be the value of the bias voltage when the current reaches 0.01 mA. Extrapolate the I/V curves to where they cross 0.01mA current and use that as the working value of V\ :sub:`0`.

Construct a table with columns for V\ :sub:`0`, λ, and f. For each LED, use the measured value of V\ :sub:`0` and the value of f to determine a value for Planck's constant and enter it as a column in the table. Find the mean value of Planck's constant and its uncertainty from your experimental values. Compare to the value given earlier.

Questions:
~~~~~~~~~~

What is the mathematical expression for the diode current, I\ :sub:`D`, given the voltage across the diode V\ :sub:`D`?

How do the diode parameters change based on the type of diode, Schottky, LED etc.?

Zener Breakdown voltage measurements:
-------------------------------------

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

2 - 1.5 Volt cells in series ( AA cells for example )

.. _directions-1:

Directions:
~~~~~~~~~~~

To measure the reverse breakdown voltage of your Zener diode we need to produce a voltage difference larger than the breakdown voltage of the 6.2 V 1N4735 diode. The ADALM1000 hardware can only produce (and measure) voltages up to the 5 V maximum. We can add an external negative voltage source to combine with the positive internal voltage to produce a total voltage high enough for this experiment. The simplest way is to add a fixed negative voltage from an external battery (3 V) as shown in figure 5. By using different numbers of 1.5 V cells, negative voltages of -1.5, -3 and -4.5 are possible. The total reverse voltage applied to the Zener diode will be this negative voltage subtracted from the positive voltage generated by AWG channel A.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab2-f5.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 5, Zener diode I vs. V setup


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A generator should be configured for a 100 Hz triangle wave with 3 volt Max and 0 volt Min such that it swings from 0 volts to +3 volt. This swing added to the -3 V offset from the external battery should be enough larger than the breakdown voltage of your 1N5230 4.7 volt zener. Be sure to connect the external battery before taking your measurements.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Load the captured data for each type of diode into a data analysis software program like MATLAB or a spreadsheet (Excel) and calculate the diode current I\ :sub:`D`. Be sure to add the 3 volt offset to the measurements for channel B to obtain the true voltage across the zener diode. You should probably measure the actual battery voltage for accurate measurements of the breakdown voltage. Plot the current vs. the calculated reverse bias voltage across the diode.

.. _questions-1:

Questions:
~~~~~~~~~~

What is the slope (effective resistance) of the curve above the breakdown voltage?

How much does the voltage change as the current changes from 100uA to 10 mA?

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/diode_i_vs_v_ltspice`
-  Fritzing files: :git-education_tools:`m1k/fritzing/diode_i_vs_v_bb`

**For Further Reading:**

| `Diodes <https://en.wikipedia.org/wiki/Diode>`__
| `Schottky diodes <https://en.wikipedia.org/wiki/Schottky_diode>`__
| `Light-emitting diode <https://en.wikipedia.org/wiki/Light-emitting_diode>`__
| `Diode modelling <https://en.wikipedia.org/wiki/Diode_modelling>`__

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**
