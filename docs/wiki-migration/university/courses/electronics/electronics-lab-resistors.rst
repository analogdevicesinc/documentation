Resistors
=========

**Understanding the differences between available resistor types and how to select the right one.**

First we will discuss the familiar "discrete" or axial-lead type resistors we are used to working with in the lab; then we will compare cost and performance tradeoffs of the discrete versions and thin- or thick-film networks.

**Axial Lead Types:**

The three most common types of axial-lead resistors are carbon composition, or carbon film, metal film and wire-wound:

• Carbon composition or carbon film-type resistors are used in general-purpose circuits where initial accuracy and stability with variations of temperature are not considered critical. Typical applications include their use as a collector or emitter load, in transistor/FET biasing networks, as a discharge path for charged capacitors, and as pull-up and/or pull-down elements in digital logic circuits.

Carbon-type resistors are assigned a series of standard values (Table 1) in a quasi-logarithmic sequence, from 1 ohm to 22 megohms, with tolerances from 2% (carbon film) to 5% up to 20% (carbon composition). Power dissipation ratings range from 1/8 watt up to 2 watts. The 1/4-watt and 1/2-watt, 5% and 10% types tend to be the most common. Carbon-type resistors have a poor temperature coefficient (typically 5,000 ppm/°C); so they are not well suited for precision applications requiring little resistance change over temperature, but they are inexpensive-as little as 3 cents [USD 0.03] each in quantities of 100 or more.

Table 1 lists a decade (10:1 range) of standard resistance values for 2% and 5% tolerances, spaced 10% apart. The smaller subset in lightface denote the only values available with 10% or 20% tolerances; they are spaced 20% apart.

====== ====== ====== ====== ======
10     **16** 27     **43** 68
**11** 18     **30** 47     **75**
12     **20** 33     **51** 82
**13** 22     **36** 56     **91**
15     **24** 39     **62** 100
====== ====== ====== ====== ======

Table 1. Standard resistor values: 2%, 5% and 10%

Carbon-type resistors use color-coded bands to identify the resistor's ohmic value and tolerance: (For more on the resistor color code see the section below "A brief history of the resistor color code")

.. image:: https://wiki.analog.com/_media/university/courses/electronics/arn_f1.jpg
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 1 Carbon-type resistors


EXAMPLE: Red-Violet-Green-Gold would have a resistance of 2.7 megohm with 5% tolerance

.. image:: https://wiki.analog.com/_media/university/courses/electronics/arn_f2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Table 2. Resistor Color code


• Metal film resistors are chosen for precision applications where initial accuracy, low temperature coefficient, and lower noise are required. Metal film resistors are generally composed of Nichrome, tin oxide or tantalum nitride, and are available in either a hermetically sealed or molded phenolic body. Typical applications include bridge circuits, RC oscillators and active filters. Initial accuracies range from 0.1 to 1.0 %, with temperature coefficients ranging between 10 and 100 ppm/°C. Standard values range from 10.0 Ω to 301 kΩ in discrete increments of 2% (for 0.5% and 1% rated tolerances).

==== ==== ==== ==== ==== ==== ==== ==== ====
1.00 1.29 1.68 2.17 2.81 3.64 4.70 6.08 7.87
1.02 1.32 1.71 2.22 2.87 3.71 4.80 6.21 8.03
1.04 1.35 1.74 2.26 2.92 3.78 4.89 6.33 8.19
1.06 1.37 1.78 2.31 2.98 3.86 4.99 6.46 8.35
1.08 1.40 1.82 2.35 3.04 3.94 5.09 6.59 8.52
1.10 1.43 1.85 2.40 3.10 4.01 5.19 6.72 8.69
1.13 1.46 1.89 2.45 3.17 4.09 5.30 6.85 8.86
1.15 1.49 1.93 2.50 3.23 4.18 5.40 6.99 9.04
1.17 1.52 1.96 2.55 3.29 4.26 5.51 7.13 9.22
1.20 1.55 2.00 2.60 3.36 4.34 5.62 7.27 9.41
1.22 1.58 2.04 2.65 3.43 4.43 5.73 7.42 9.59
1.24 1.61 2.09 2.70 3.49 4.52 5.85 7.56 9.79
1.27 1.64 2.13 2.76 3.56 4.61 5.96 7.72 9.98
==== ==== ==== ==== ==== ==== ==== ==== ====

Table 3. Standard values for film-type resistors

Metal film resistors use a 4 digit numbering sequence to identify the resistor value instead of the color band scheme used for carbon types:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/arn_f3.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 2 Metal film resistors


The indicated resistance here is 4990?. For values less than 100, an "R" indicates a decimal point, e.g., 49R9 = 49.9?

• Wire-wound precision resistors are extremely accurate and stable (0.05%, <10 ppm/°C); they are used in demanding applications, such as tuning networks and precision attenuator circuits. Typical resistance values run from 0.1 ? to 1.2 M?.

High Frequency Effects:
-----------------------

Unlike its "ideal" counterpart, a "real" resistor, like a real capacitor (Analog Dialogue 30-2), suffers from parasitics. (Actually, any two-terminal element may look like a resistor, capacitor, inductor, or damped resonant circuit, depending on the frequency it's tested at.)

.. image:: https://wiki.analog.com/_media/university/courses/electronics/arn_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 High frequency resistor model


Factors such as resistor base material and the ratio of length to cross-sectional area determine the extent to which the parasitic L and C affect the constancy of a resistor's effective dc resistance at high frequencies. Film type resistors generally have excellent high-frequency response; the best maintain their accuracy to about 100 MHz. Carbon types are useful to about 1 MHz. Wire-wound resistors have the highest inductance, and the poorest frequency response. Even if they are non-inductively wound, they tend to have high capacitance and are likely to be unsuitable for use above 50 kHz.

Temperature effects: Should you always use resistors with the lowest temperature coefficient (TCRs)?
----------------------------------------------------------------------------------------------------

Not necessarily. A lot depends on the application. For the single resistor shown in figure 4, measuring current in a loop, the current produces a voltage across the resistor equal to I × R. In this application, the absolute accuracy of resistance at any temperature would be critical to the accuracy of the current measurement, so a resistor with a very low TC would be used.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/arn_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 Measuring current


A different example is the behavior of gain-setting resistors in a gain-of-100 op amp circuit, shown in figure 5. In this type of application, where gain accuracy depends on the ratio of resistances (a ratiometric configuration), resistance matching, and the tracking of the resistance temperature coefficients (TCRs), is more critical than absolute accuracy.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/arn_f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 Gain Stage


Here are a couple of examples that make the point.

1. Assume both resistors have an actual TC of 100 ppm/°C (i.e., 0.01%/°C). The resistance following a temperature change, ΔT, is:

.. container:: centeralign

   R = R\ :sub:`0`\ (1+ TC ΔT)


For a 10°C temperature rise, both R\ :sub:`F` and R\ :sub:`I` increase by 0.01%/°C × 10°C = 0.1%. Op amp gains are [to a very good approximation] 1 + R\ :sub:`F`/R\ :sub:`I`. Since both resistance values, though quite different (99:1), have increased by the same percentage, their ratio and the gain is unchanged. Note that the gain accuracy depends just on the resistance ratio, independently of the absolute values.

2. Assume that R\ :sub:`I` has a TC of 100 ppm/°C, but R\ :sub:`F`'s TC is only 75 ppm/°C. For a 10°C change, R\ :sub:`I` increases by 0.1% to 1.001 times its initial value, and R\ :sub:`F` increases by 0.075% to 1.00075 times its initial value. The new value of gain is

.. container:: centeralign

   (1.00075 R\ :sub:`F`)/(1.001 R\ :sub:`I`) = 0.99975 R\ :sub:`F`/R\ :sub:`I`


For an ambient temperature change of 10°C, the amplifier circuit's gain has decreased by 0.025% (equivalent to 1 LSB in a 12-bit system).

Another parameter that's not often understood is the self-heating effect in a resistor.

Self-heating causes a change in resistance because of the increase in temperature when the dissipated power increases. Most manufacturers' data sheets will include a specification called "thermal resistance" or "thermal derating", expressed in degrees C per watt (°C/W). For a 1/4-watt resistor of typical size, the thermal resistance is about 125°C/W. Let's apply this to the example of the above op amp circuit for full-scale input:

Power dissipated by R\ :sub:`I` is V\ :sup:`2`/R = (100 mV)2/100 W = 100 µW, leading to a temperature change of 100 µW × 125°C/W = 0.0125°C, and a negligible 1-ppm resistance change (0.00012%).

Power dissipated by R\ :sub:`F` is V\ :sup:`2`/R = (9.9 V)2/9900 W = 9.9 mW, leading to a temperature change of 0.0099 W × 125°C/W = 1.24°C, and a resistance change of 0.0124%, which translates directly into a 0.012% gain change.

Thermocouple Effects:
---------------------

Wire-wound precision resistors have another problem. The junction of the resistance wire and the resistor lead forms a thermocouple which has a thermoelectric EMF of 42 µV/°C for the standard "Alloy 180"/Nichrome junction of an ordinary wire-wound resistor. If a resistor is chosen with the [more expensive] copper/nichrome junction, the value is 2.5 µV/°C. ("Alloy 180" is the standard component lead alloy of 77% copper and 23% nickel.) Such thermocouple effects are unimportant in ac applications, and they cancel out when both ends of the resistor are at the same temperature; however if one end is warmer than the other, either because of the power being dissipated in the resistor, or its location with respect to heat sources, the net thermoelectric EMF will introduce an erroneous dc voltage into the circuit. With an ordinary wire-wound resistor, a temperature differential of only 4°C will introduce a dc error of 168 µV-which is greater than 1 LSB in a 10-V/16-bit system! This problem can be fixed by mounting wire-wound resistors so as to insure that temperature differentials are minimized.

This may be done by keeping both leads of equal length, to equalize thermal conduction through them, by insuring that any airflow (whether forced or natural convection) is normal to the resistor body, and by taking care that both ends of the resistor are at the same thermal distance (i.e., receive equal heat flow) from any heat source on the PC board.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/arn_f7.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 6 PC board layout


Resistor Networks
-----------------

A resistor network is a single package that contains two or more resistors. The package will include multiple leads by which the network can be made part of a larger circuit. Figure 7 shows typical packages used for resistor networks. There are commonly two ways the resistors are connected in the array, isolated and bussed where one end of all the resistors share a common connection as shown in figure 8. The bussed arrangement is commonly used for pull up, pull down or bus termination on logic signals.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/arn_f8.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 7 SIP and DIP resistor network packages


.. image:: https://wiki.analog.com/_media/university/courses/electronics/arn_f9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 8 SIP and DIP resistor network schematics


The differences between "thin-film" and "thick-film" networks
-------------------------------------------------------------

Besides the obvious advantage of taking up considerably less real estate, resistor networks-whether as a separate entity, or part of a monolithic IC-offer the advantages of high accuracy via laser trimming, tight TC matching, and good temperature tracking. Typical applications for discrete networks are in precision attenuators and gain setting stages. Thin film networks are also used in the design of monolithic (IC) and hybrid instrumentation amplifiers, and in CMOS D/A and A/D converters that employ an R-2R Ladder network topology.

Thick film resistors are the lowest-cost type-they have fair matching (<0.1%), but poor TC performance (>100 ppm/°C) and tracking (>10 ppm/°C).They are produced by screening or electroplating the resistive element onto a substrate material, such as glass or ceramic.

Thin film networks are moderately priced and offer good matching (0.01%), plus good TC (<100 ppm/°C) and tracking (<10 ppm/°C). All are laser trimmable. Thin film networks are manufactured using vapor deposition.

Tables 4 compares the advantages/disadvantages of a thick film and several types of thin-film resistor networks. Table 5 compares substrate materials.

+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| **Type**             | **Advantages**                                                                                                                                                | **Disadvantages**                                  |
+======================+===============================================================================================================================================================+====================================================+
| Thick film           | Low cost, High power, Laser-trimmable, Readily available, Fair matching (0.1%)                                                                                | Poor TC (>100 ppm/°C), Poor tracking TC(10 ppm/°C) |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| Thin film on glass   | Good matching (<0.01%), Good TC (<100 ppm/°C), Good tracking TC (2 ppm/°C), Moderate cost Laser-trimmable, Low capacitance                                    | Delicate, Often large geometry, Low power          |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| Thin film on ceramic | Good matching (<0.01%), Good TC (<100 ppm/°C), Good tracking TC (2 ppm/°C), Moderate cost, Laser-trimmable, Low capacitance, Suitable for hybrid IC substrate | Often large geometry                               |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| Thin film on silicon | Good matching (<0.01%), Good TC (<100 ppm/°C), Good tracking TC (2 ppm/°C), Moderate cost, Laser-trimmable, Low capacitance, Suitable for hybrid IC substrate |                                                    |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+

Table 4. Resistor Networks

+---------------+---------------------------------------------------+-------------------------------------+
| **Substrate** | **Advantages**                                    | **Disadvantages**                   |
+===============+===================================================+=====================================+
| Glass         | Low capacitance                                   | Delicate, Low power, Large geometry |
+---------------+---------------------------------------------------+-------------------------------------+
| Ceramic       | Low capacitance, Suitable for hybrid IC substrate | Large geometry                      |
+---------------+---------------------------------------------------+-------------------------------------+
| Silicon       | Suitable for monolithic construction              | Low power, Capacitance to substrate |
+---------------+---------------------------------------------------+-------------------------------------+
| Sapphire      | Low capacitance                                   | Low power, Higher cost              |
+---------------+---------------------------------------------------+-------------------------------------+

Table 5. Substrate Materials

In the example of the IC instrumentation amplifier shown figure 9, tight matching between resistors R\ :sub:`1`-R\ :sub:`1`', R\ :sub:`2`-R\ :sub:`2`', R\ :sub:`3`- R\ :sub:`3`' insures high common-mode rejection (as much as 120 dB, dc to 60 Hz). While it is possible to achieve higher common mode rejection using discrete op amps and resistors, the arduous task of matching the resistor elements is undesirable in a production environment.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/arn_f10.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9 IC Instrumentation Amplifier


Matching, rather than absolute accuracy, is also important in R-2R ladder networks (including the feedback resistor) of the type used in CMOS D/A converters. To achieve n-bit performance, the resistors have to be matched to within 1/2n, which is easily achieved through laser trimming. Absolute accuracy error, however, can be as much as ±20%. Shown in figure 10 is a typical R-2R ladder network used in a CMOS digital to analog converter.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/arn_f11.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10 R/2R resistor ladder


A brief history of the resistor color code:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following is excerpted from a mixture of:

| https:*en.wikipedia.org/wiki/Electronic_Industries_Alliance#History
  https:*\ en.wikipedia.org/wiki/Electronic_color_code#History
| https:*hsm.stackexchange.com/questions/7096/resistor-color-code
  *\ https://hackaday.com/2020/01/13/why-do-resistors-have-a-color-code/\ *
  https:*\ www.dailybreak.com/break/cabinet-of-curiosities-why-indigo-is-in-the-rainbow
| https://en.wikipedia.org/wiki/Isaac_Newton's_occult_studies

Before industry standards were established (1925), each manufacturer used their own unique system for color coding or marking their components.

Then in 1924, 50 radio manufacturers in Chicago formed a trade group. The idea was to share patents among the members. Almost immediately the name changed from “Associated Radio Manufacturers” to the “Radio Manufacturer’s Association” or RMA.

The standard color code was developed by the Radio Manufacturers Association (RMA) in the 20’s as a three band code for resistor values. The three bands were more compact than the number value because the third band represented the number of zeroes. Initially the three colors were not three separate bands, and there was no neutral background color. Instead, they were the body color, the tip color and the dot color.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/resistor-colors.png
   :align: center
   :width: 600px

Identical adjacent colors were allowed.

For example, 250 000 Ω was reduced to three bands. In addition, color bands remained visible in whatever position a resistor was soldered, whereas a stamped number value could be out of sight. The fourth band, representing the tolerance, was added later.

`Radio Physics Course, Ghirardi, 1931 <https://books.google.nl/books?id=VJALAQAAIAAJ&q=%22The%20code%20identifies%20resistors%20by%20means%20of%203%20colors,%20known%20as%20%22body,%22%20%22tip%22%20and%20%22dot%22%20colors%22&dq=%22The%20code%20identifies%20resistors%20by%20means%20of%203%20colors,%20known%20as%20%22body,%22%20%22tip%22%20and%20%22dot%22%20colors%22&hl=en&sa=X&ved=0ahUKEwiGoq-m5cjZAhWCjqQKHQmgBi8Q6AEILTAB>`__

In 1952, it was standardized in IEC 62:1952 by the International Electrotechnical Commission (IEC) and since 1963 also published as EIA RS-279.

The sequence of the central group of colors, ROYGBV, was chosen to match the rainbow mnemonic: red-orange-yellow-green-blue-violet, "ROYGBIV", without indigo because most people do not (can not) distinguish, with their eyes, a separate color between blue and violet, plus it’s a little silly color; and is only there because Newton was a little bit of a kook. (Of the rainbow's widely accepted seven colors, three are primary (red, yellow and blue); three are secondary (green, orange and violet) and just one is tertiary (indigo) – When Newton in 1665 named the colors in the rainbow after passing them through a prism – he wanted to the colors in the rainbow to match the 7 notes in a Dorian scale (a scale with no sharps or flats that starts on D), and Newton had a history of dabbling in the occult, and seven is considered a sacred number in the secretive paranormal sciences). The rainbow group is preceded by two low brightness colors, black and brown, representing the lowest digits 0 and 1, and succeeded by two bright colors, grey and white, representing the highest digits 8 and 9.

`Electrical Engineering Science, Preston, 1960, p.115 <https://books.google.nl/books?id=4tkiAAAAMAAJ&redir_esc=y>`__

Color bands were used because they were easily and cheaply printed on tiny components. However, there were drawbacks, especially for color blind people. Overheating of a component or dirt accumulation may make it impossible to distinguish brown from red or orange. Advances in printing technology have now made printed numbers more practical on small components. The values of components in surface mount packages are marked with printed alphanumeric codes instead of a color code.

For more info on passive components see:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:adi:`AN-348: Avoiding Passive-Component Pitfalls <static/imported-files/application_notes/500824934643930414583807523874018494695982855668424783486554001060AN348.pdf>`

\*\* Return to Lab Activity :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>` \*\*
