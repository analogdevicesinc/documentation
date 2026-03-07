Choosing Discrete Transistors
=============================

by James Bryant

One of the common questions the author and his colleagues in the Applications Department are asked is "The application note for XXXX calls for a 3N14159 transistor - where can I get one?" Research reveals that the 3N14159 has been obsolete for years - or is only obtainable (in minimum orders of 1,000,000 pieces) with a lead time of 21 months from a factory in Timbuktu. The correct question is not "Where do I get that specific device?" but "What other, easily obtained, devices will work in this application?"

There are tens of thousands, possibly hundreds of thousands, of different types of discrete transistor and there are almost always a few places in a system where a discrete transistor is necessary. Which do we choose - and why?

For many applications there is no need to choose a particular transistor - we should just use the first reasonably suitable one that comes to hand. How do we make a good choice of a transistor without wasting time on unnecessary detail?

We shall not discuss the physics of transistors here. There are plenty of textbooks which give a good summary of the basics and there are innumerable other books and articles on both basic principles and detailed studies of particular issues. But we do need to know what they do and it may be helpful to know a little about why they behave as they do - so we'll talk, just a little, about transistor structures.

TRANSISTORS
-----------

A transistor is a solid-state three-terminal amplifying device. There is a terminal common to the input and output signals, and a signal on one of the remaining terminals controls the current in the other.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/ctrans_f1.jpg
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 1 Basic Function of a Transistor


There are two basic types of transistor - bipolar junction transistors and field-effect transistors, known respectively as BJTs and FETs.

The most basic question of all when choosing a transistor, though, is not whether it's a BJT or an FET but its polarity - in use is its output terminal positive or negative with respect to its common terminal? If the answer is positive we need an NPN BJT or an N-channel FET, otherwise we need a PNP or a P-channel. This is critically important, but so obvious that little further discussion is needed on the topic. For the rest of the article, except when specifically addressing this issue, we shall use the positive cases (NPN & N-channel) for all our examples.

Although FETs had been demonstrated and patented almost twenty years earlier than BJTs\ :sup:`1` the first practical transistors were bipolar\ :sup:`2`. An NPN transistor consists of a thin base of P-type semiconductor sandwiched between two N-type regions, the emitter and the collector. If a current flows from the base to the emitter and a positive bias is present on the collector, a larger current, proportional to the base current, flows in the collector.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/ctrans_f2.jpg
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 2 An NPN Bipolar Junction Transistor (BJT)


From figure 2 we see that a BJT is a current amplifier - the output current is ß times the input current, and ß may vary slightly with the base current so that the amplifier is not quite linear. (The ß or h\ :sub:`fe` is the *current gain* of the transistor.) The input impedance is neither low nor linear so we can also view a BJT as an I\ :sub:`out`/V\ :sub:`in` (transconductance) amplifier with a silicon diode as its input device. It is clear that the greater the value of ß the better the current amplifier. For most applications a minimum value of 80-100 is adequate but higher values to a few hundred are not uncommon. ("Super-beta" transistors with ß up to several thousand are possible, but they have a very narrow base region and low breakdown voltages and are so fragile that they are rarely used except within analog integrated circuits.)

There are two types of FET, junction FETs (JFETs) and Insulated Gate FETs (IGFETs), more commonly, but less accurately, called Metal Oxide Silicon FETs (MOSFETs) which is the name I shall use here, and both come in either polarity (N-channel for positive supply, P-channel for negative). FETs have very high input resistance (but their input capacitance may be quite large - tens or even hundreds of pF) and are therefore transconductance (I\ :sub:`out`/V\ :sub:`in`) devices.

Today the MOSFET is the commoner device. The N-channel version consists of a strip of P-type silicon with two N-type diffusions. Over the strip between the diffusions is a very thin layer of silicon dioxide (or some other insulator) covered with a conducting film (usually aluminum or polycrystalline silicon). A positive potential on this conducting gate causes the P-type material just under the insulator to become N-type, joining the drain and source diffusions and allowing a current to flow. The amount of current varies with the applied voltage so the device works as an amplifier as well as a switch.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/ctrans_f3.jpg
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 3 An N-Channel Enhancement mode MOSFET


Normally MOSFETs are of this type - off when unbiased and turned on by a bias voltage. Such devices are known as enhancement mode devices. It is possible, however to make FETs which are on when unbiased and turned off by a negative (positive for P-channel) voltage. All JFETs (junction field-effect transistors) are of this type but there are some depletion mode MOSFETs as well.

A depletion mode MOSFET has a shallow diffusion under the gate oxide, joining the drain and source and allowing current to flow without gate bias. When the gate is biased negative (for N-channel) this diffusion is pinched by the resulting electric field and the device ceases to conduct.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/ctrans_f4.jpg
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 4 An N-Channel Depletion mode MOSFET


An N-channel JFET consists of a strip of N-type silicon with connections (drain and source) at each end and a P-type gate diffusion between them. Without bias on the gate, current can flow in the N-type channel below the diffusion. When the gate is biased negative the depletion zone expands to fill the channel and the drain current is pinched off.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/ctrans_f5.jpg
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 5 An N-Channel Depletion mode JFET


CHOOSING TRANSISTORS
--------------------

For most general purpose transistor applications we need devices which are non-conducting with zero bias on the control input (base or gate). Such devices are BJTs or enhancement mode MOSFETs. The remainder of this article will not consider depletion mode FETs - although they are valuable components in a number of applications they are so much less common than BJTs and enhancement mode devices that a separate section for them is not really necessary, particularly when most of the issues we shall discuss are common to all transistors of any type.

So we need a transistor. We know whether its supply is positive or negative, and so whether we need an NPN/N-channel device or a PNP/P-channel one. But do we need a BJT or a MOSFET?

In many cases it does not matter. Discrete MOSFETs are perhaps ten or twenty percent more expensive than BJTs, but they do not need base resistors which cost and occupy expensive board area. They are slightly more vulnerable to electrostatic damage (ESD) during handling but they do not draw base current and load circuits at DC (since they have relatively large input capacitance they may give rise to capacitive loading issues in higher frequency circuits). At one time the gate threshold voltage (the value of V\ :sub:`gs` at which a MOSFET starts to conduct) was several volts, so they could not be used with very low supply voltages, but today the threshold voltages of many devices are comparable to the 0.7V base turn-on voltage of a silicon BJT. So where we want an amplifier or a logic driven switch we probably don't care.

But the input of a BJT is a silicon diode. We can use its thermal properties to measure temperature, and its high current when over-driven to act as a clamp or limiting circuit, so there are some circuits where we must have a BJT.

For some twenty years the magazine Elektor\ :sup:`3` has published circuits designed around transistors which it calls TUNs and TUPs ("Transistor Universal NPN" and "Transistor Universal PNP"). These transistors are silicon planar BJTs and any transistor which exceeds the following specification qualifies:-

+--------+------+----------------+-------------------+------------------------+---------------------+-------------------+
| Device | Type | BV\ :sub:`ceo` | I\ :sub:`c` (Max) | ß [h\ :sub:`fe`] (Min) | P\ :sub:`tot` (Max) | f\ :sub:`t` (Min) |
+========+======+================+===================+========================+=====================+===================+
| TUN    | NPN  | 20 V           | 100 mA            | 100                    | 100 mW              | 100 MHz           |
+--------+------+----------------+-------------------+------------------------+---------------------+-------------------+
| TUP    | PNP  | -20 V          | -100 mA           | 100                    | 100 mW              | 100 MHz           |
+--------+------+----------------+-------------------+------------------------+---------------------+-------------------+

Most cheap small-signal silicon transistors do qualify. I should propose adding to the list MUNs and MUPs ("MOSFET universal N-channel" and "MOSFET universal P-channel") - and most cheap small MOSFETs qualify for this specification:-

+--------+-----------+---------------+-------------------+------------------+---------------------+----------------------------------+
| Device | Type      | BV\ :sub:`ds` | I\ :sub:`c` (Max) | V\ :sub:`GS(th)` | P\ :sub:`tot` (Max) | t\ :sub:`on`/t\ :sub:`off` (Max) |
+========+===========+===============+===================+==================+=====================+==================================+
| MUN    | N-channel | 20 V          | 100 mA            | 0.5 V to 2V      | 100 mW              | 20 nS                            |
+--------+-----------+---------------+-------------------+------------------+---------------------+----------------------------------+
| MUP    | P-channel | -20 V         | -100 mA           | -0.5 V to -2V    | 100 mW              | 20 nS                            |
+--------+-----------+---------------+-------------------+------------------+---------------------+----------------------------------+

Most versions of SPICE contain standard BJTs and MOSFETs which are similar to these "universal" devices. So when designing a system which contains discrete small-signal transistors use these generics during the design stage and choose the most convenient (i.e. best package, ready availability and low cost) when ordering. When publishing, or specifying, the design, though, use generic terminology so that it is clear that the exact choice of device is unlikely to matter.

Of course many designs cannot use these standard devices - some specification will need to be outside the simple standard. In such cases specify the exceptions, for example:-

.. container:: centeralign

   MUN *except* higher BV\ :sub:`ds` =250V


.. container:: centeralign

   TUP *except* higher ß = 200


.. container:: centeralign

   or whatever....


When a published design uses a particular transistor it is sensible to consider whether the chosen device is necessary for the design or was simply the first transistor to fall out of the junk box\ :sup:`4` when the designer built his prototype\ :sup:`5`. Study the data sheet (if the transistor is so arcane that you cannot discover a data sheet study the circuit it's used in):-

-   Does the device have some unusual characteristic?
-   Is this characteristic exploited in the circuit?
-   Would you expect the circuit to work with a TUN/TUP?
-   Does a quick software (SPICE) check suggest that it would work with a TUN/TUP?
-   Does a slightly less quick hardware (breadboard) check suggest that it would work with a TUN/TUP?

If the answers to all the questions are "Yes" then it is probably wise to investigate 1 & 2 a little more closely, but if the answers are "No, no, yes, yes, yes" it almost certainly safe to replace the device with a generic one.

TRANSISTOR PARAMETERS
---------------------

**Maximum collector/drain voltage. BVceo or BVds** If the maximum supply voltage is less than BV\ :sub:`ceo` or BV\ :sub:`ds` and there is no inductive circuitry in the collector/drain which might produce higher voltage transients, and there is no external signal source which might apply higher voltages, then we need not worry about this specification.

On the other hand there are many circuits where a transistor may be expected to work with high values of V\ :sub:`ce` or V\ :sub:`ds`, either steady state or as transients, and it is very important that where this is the case the correct maximum is chosen. Older textbooks tend to suggest that transistors are low voltage devices and that the rare exceptions are expensive - it is useful to remember that today

BJTs and MOSFETs with breakdown voltages of more than 500V are inexpensive and readily available, although the current gain, ß, of high voltage BJTs is more often in the range 40-100 rather than the =100 of the TUN/TUP. Similarly the gate threshold voltage of a high voltage MOSFET is more likely to be in the range 2-5V rather than 500-2000mV of the MUN/MUP.

**Absolute maximum collector/drain current. Ic(max) or Id(max)** The maximum current expected in the collector/drain must not exceed the absolute maximum current rating of the device. Given that the TUN/etc value for this is 100 mA this is unlikely for small-signal circuits, but if the transistor is required to provide power to a load the maximum current must be checked.

The absolute maximum current rating of some devices may be divided into a DC (or perhaps mean) current rating and a higher transient rating for short pulses. It is important to ensure that peak transient currents are within their rated limits.

Most small-signal transistors have I\ :sub:`max` ratings greater than 100 mA - usually 300-1000 mA - and many devices which meet the TUN/etc specification will actually have such a rating and may be used when such medium currents are needed. If higher currents are required TUN/etc devices will be inadequate and a power device must be chosen. At higher currents it is important to comply with power ratings as well as current ratings, packages will probably be larger, and a heat sink may be necessary. BJTs with higher maximum currents may have lower values of ß at high currents.

**Packages & Power.** There are innumerable different transistor packages from near microscopic surface mount ones to large plastic and metal packages capable of handling several kW with adequate cooling. Choose the one which is most convenient for your application - surface mount for mass production, leaded for prototyping and small scale production where ease of hand soldering is helpful, and whatever power package is appropriate when dissipation and heat sinks need to be considered.

A few of the more common transistor packages are shown in figure 6, together with a pair of very early British "Red Spot" audio frequency (f\ :sub:`t`\ =700kHz) germanium junction transistors in forged aluminum cans from the late 1950s. (The "Red Spots" are included for historical interest - as a teenager the author of this article used these "Red Spot" transistors, which were rejects from a production line making devices which actually had type numbers - despite being rejects they still cost about £1 each [over $20 at present day prices], to build a number of different radios and amplifiers, and a Geiger counter.)

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/ctrans_f6.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6 Some transistor packages


Heat escapes from most packages through their leads, so the actual thermal characteristics of a small-signal transistor depend as much on the PCB where it is mounted as on its package. Even the smallest surface mount transistors can dissipate several hundred mW, far more than the maximum limit of the TUN/etc specification. The same device in different packages may have different maximum power ratings - RTFDS\ :sup:`6` carefully.

Higher power device packages have metal areas to allow thermal conduction to a heat sink, so read the dissipation specifications and heat sink requirements for these devices carefully. The TO-264 package in figure 6 can dissipate 2.5 kW on a suitable heat sink.

Different devices in the same package may have different pinouts. It is important to realize that two transistors with exactly the same electrical specification and package may not have the same pinout, and are therefore not immediately interchangeable. Figure 7 shows the six possible BJT connections of TO-92 & SOT-23 packages. Back in the 1990s the author managed to track down at least one device with each of these pinouts and although that list has been lost he has no reason to suppose that modern transistors are any less diverse.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/ctrans_f7.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 7 Six pinouts are possible on a package


In high frequency design it may be useful to select a device with a pinout which allows the least parasitic reactance in the PCB layout.

\**Collector/drain leakage current. Ice0 or Idss0 \**(Sometimes called the **"cutoff current"**.) This is the small leakage current which flows from collector to emitter or drain to source when the transistor is turned off. It is usually in the order of tens of nA but data sheets sometimes set rather larger worst case maximum values to reduce testing costs. Transistors used as very low level switches or amplifiers should be chosen for leakage below 50 nA but for most applications 200 nA or even more is quite satisfactory.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/ctrans_f8.jpg
   :align: center
   :width: 220px

.. container:: centeralign

   Figure 8 Very low power inverter using low leakage MOSFET


The low power inverter shown in figure 8 is an example of circuits requiring very low collector/drain leakage. Drain leakage of 100 nA gives a voltage drop of 1V and an output voltage of 2.0V, only just on the threshold of permitted logic 1 levels, so practical designs should use an MOSFET having drain/source leakage =50 nA. (Note that although this inverter is very low power [300 nA = 0.9 µW when the transistor is on] it is also very slow - assuming a transistor output capacitance plus track capacitance plus next stage input capacitance of 20 pF, which is not unreasonable, it has a rise time of some 0.2 msec - not a problem for DC applications, but useless for even medium speed switching circuits.)

\**Current gain. ß or hfe \**The current gain of a BJT is the ratio of the collector current to the base current when the device is not in saturation (i.e. the collector/base voltage is positive [for an NPN device]). ß is usually fairly constant over a wide range of currents, but it may be slightly lower at very low base currents and will almost certainly start to fall as the collector current approaches its absolute maximum value. Since it is a ratio it is a dimensionless value.

TUNs and TUPs have ß = 100, but high current and high voltage BJTs may have slightly lower (=40 or 50) minimum specified values.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/ictrans_f9.jpg
   :align: center
   :width: 150px

.. container:: centeralign

   Figure 9 Transistor (BJT or MOSFET) emitter/source follower


An emitter follower/source follower output stage, illustrated in figure 9, is equally accurate with a BJT or an MOSFET. In simple emitter followers it is assumed that the base/emitter or gate/source voltages V\ :sub:`be` or V\ :sub:`gs` remain constant, giving a fixed offset between the input and the load voltage, but in more accurate circuits feedback may be taken from the emitter (source)/load connection.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/ctrans_f10.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10 Since the base current does not flow in their outputs, BJTs are less precise than FETs as current output stages


Since some of the emitter current must flow in the base the collector and emitter currents of a BJT are not identical, which means that the current output stage in figure 10 should be made with a MOSFET rather than a BJT since MOSFETs have virtually zero gate current.

\**Forward transconductance. gfs \**The forward transconductance of an FET is the ratio of ΔI\ :sub:`ds`/ΔV\ :sub:`gs` when the device is turned on and the drain circuit is not current-limited. It is measured in siemens (S) (or, for traditionalists amongst us, in mhos or reciprocal ohms [Ʊ], which are the obsolete name and symbol for exactly the same thing). Small-signal FETs and MOSFETs may have g\ :sub:`fs` as low as a few mS but larger ones can have gains of large fractions of a siemens to several siemens or more.

In general a few volts change of gate voltage is sufficient to change the drain current from minimum (off) to its absolute maximum value. It is also important to know at what gate voltage conduction starts - see:-

\**Gate threshold voltage. Vgs(th) \**The gate threshold voltage of a MOSFET is the gate/source voltage at which the correctly biased drain starts to draw current. The definition of "starts" will be specified on the data sheet and may be as low as a few µA, but is more likely to be defined as 1 mA, or even more with a high power MOSFET. Above this threshold drain current will rise very quickly with small increases of gate voltage.

If an MOSFET is to be driven by logic it is important that its threshold voltage be above the worst case value of logic 0 over the temperature range of the circuit, which is likely to be at least several hundreds of mV, as otherwise it may start to turn on when it is supposed to be turned off.

\**Saturation Voltage. Vce(sat) \**When a BJT is turned on hard enough that the voltage drop in its collector load is sufficient to bring the collector potential below the base potential (in other words the base-collector junction is forward biased) it is said to be *saturated*. This saturation voltage is not proportional to the collector current, so the model of a saturated transistor is not just a resistance between its collector and emitter.

Two examples of the importance of a low saturation voltage are:-

[A] In classic TTL logic each input sources 1.6 mA into a logic 0 output driving it. With a full fan-out of 10 this means that a TTL output transistor may be called upon to sink some 16 mA with a saturation voltage of no more than 400 mV.

[B] When a power BJT is used to switch high current loads its dissipation, for a given load current, is proportional to its saturation voltage. The lower the saturation voltage, the less heat must be removed from the transistor.

Note that when you remove the input drive from a saturated transistor there is a delay (usually nsecs or tens of nsecs, but it can be more) before it starts to turn off. This is its *saturation recovery time* and may be specified, under well defined conditions, on its data sheet.

**On Resistance. Ron** MOSFETs do not saturate because they are majority carrier devices. When they are turned hard on with a gate voltage well above their gate threshold voltage they behave as low value resistors and their *on resistance* is specified on their data sheet. Ohm's law applies - the voltage drop is proportional to the current and the on resistance, and their dissipation is I\ :sup:`2`\ R.

**Noise Figure. NF** The majority of transistor applications are relatively high-level and noise is not an issue. Where it is an issue, though, it is critically important. Many transistors, both BJTs and FETs, have their noise figure specified and guaranteed by their manufacturers. When comparing the noise figures of different devices it is very important that the noise figures should have been measured with the same source impedance. If the transistors are intended for use in radio systems it is likely that their NF will have been measured at 50Ω and so comparison is simple, but it is meaningless to compare the NFs of two devices whose NFs were measured at different impedances. A paper associated with an earlier RAQ\ :sup:`7` covers this and other noise issues in detail and should be consulted if you are interested in the topic.

**Transition Frequency. ft** The f\ :sub:`t` of a BJT is the frequency at which the current gain, with a short circuit (at HF) output, is unity. Again I do not propose to discuss how this may be measured\ :sup:`8` but simply to observe that f\ :sub:`t` is the most widely used figure of merit for comparing the frequency response of BJTs. Most TUNs and TUPs will have f\ :sub:`t` well over the 100 MHz minimum but high power and high voltage transistors will often have rather lower values.

FETs are transconductance devices with infinitesimal DC input current so it is incorrect to consider their DC current gain. But since they have input capacitance (C\ :sub:`gs`) of pF to hundreds of pF their capacitive input impedance is relatively low at HF and so their HF input current may be measured and their f\ :sub:`t` derived. Occasionally an FET or MOSFET data sheet will contain a value of f\ :sub:`t` derived in this way and it is certainly valid to use it, if available, to evaluate FET frequency response, but usually the speed of FETs is specified in terms of switching times.

**Switching Times. t(on) & t(off)** Most FETs, and many BJTs, have switching time specifications, defined as the time taken, under specified conditions (RTFDS\ :sup:`9`) for the output current to rise from zero to a specified value, or to return to zero, respectively. The switching signal is either assumed to be instantaneous (a legal fiction) or defined as a few nsec. Comparing switching times is a reliable way of comparing the relative speeds of transistors, provided they are tested under similar conditions.

**Capacitances. C\ ??** There are three capacitances associated with a transistor - the input capacitance C\ :sub:`in`, the output capacitance C\ :sub:`out` and the Miller\ :sup:`10` (or feedback) capacitance C\ :sub:`fb`. Different manufacturers use different names (therefore the C\ :sub:`??` in the heading) but which is which should be perfectly clear from figure 11.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/ctrans_f11.jpg
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 11 Parasitic capacitances of transistors (different manufacturers use different names/symbols)


As we have already seen, FETs, especially power MOSFETs, may have values of Cin as large as 1 nF or even more, although small-signal MOSFETs will have much smaller values, probably in the range of 15-50 pF. It is important, though, when designing circuits where such capacitance may affect rise times or circuit stability to ensure that the design takes account of such values and that devices are chosen to have capacitances which the circuit design can tolerate.

CHOOSING A TRANSISTOR
---------------------

So we need a transistor for a design. How do we choose?

It would be nice to have a database of every transistor in the World attached to a spreadsheet so that after entering limiting values of every important parameter we see a list of every one which meets our requirements. Unfortunately such a list is impossible to compile - it is enormous and would change day by day as new transistors are introduced and old ones become obsolete. However such distribution companies as Avnet, Arrow, Digi-Key, Mouser, Premier Farnell and RS Components have parametric search engines\ :sup:`11` on their websites which allow us to do much the same thing with the advantage that, although they do not show every device in the World, the ones that they do show are likely to be readily available. Many manufacturers have such parametric search engines as well, which are even more up-to-date, but the advantage of the distributors' ones is that they allow us to compare devices from many manufacturers on one site and, generally, also give some idea of actual availability.

So the answer to the question is make a list of necessary parameters and go online. Each distributor's search engine is slightly different, and of course each distributor's stock (and maybe prices) differ too, so it's probably best to use more than one and compare the results.

We've already discussed what parameters to select for but to summarize the essential ones in order:-

| **Polarity:-** NPN/N-channel or PNP/P-channel?
| \**Type:- **BJT or FET?
  **\ Operating voltage:-\*\* Select the minimum safe value of BV\ :sub:`ceo` or BV\ :sub:`ds` (It may be a good idea to select a maximum value too, as very high voltage transistors may have lower gain and higher V\ :sub:`ce(sat)` or R\ :sub:`on` and are sure to be a bit more expensive.)
| \**Maximum current:- **Select a value =33% above the maximum expected collector/drain current. (You may need to consider peak transient currents as well as maximum steady state currents.)
  **\ Package:-\*\* What package, *and pinout*, do you require? (If a device comes in several packages the absolute maximum current and power ratings may vary with the package chosen - check this. Also the parametric selection guide may not provide pinout details.)
| **Power:-** What is the maximum dissipation? (Remember that a switch dissipates very little power when off, and when it is on most of the power is in the load, not the switch itself. During switching dissipation is higher but this is only important if the device is continually switching at a high rate.)
| It is necessary to decide the above parameters whenever we choose a transistor. The remaining ones may be critical in some applications and unimportant in others, so you must decide for yourself which ones matter in your application, and select devices which meet your requirements. Consider all the remaining list but only specify the ones you actually care about:-

| \**Leakage current:- **I\ ce0 or I\ ds0
  **\ Current gain:- **ß or h\ fe - Few applications need ß = 100
  **\ Transconductance:- **g\ fs - Rarely needs to be specified.
  **\ Gate threshold voltage:-\*\* V\ :sub:`gs(th)` - This must be compatible with the levels of any logic used to drive a MOSFET as a switch, and must not be too large if a MOSFET is used with a low supply voltage.
| \**Saturation voltage:- **V\ ce(sat) - Only important when a BJT is used as a switch (logic or power).
  **\ On resistance:- **R\ on - Important when a MOSFET is used as a power switch, but not usually in amplifier or logic applications
  **\ Noise figure:- **NF - Only important in (very) small signal amplifiers or low noise oscillators.
  **\ Transition frequency:- **f\ t - Only important in HF (High Frequency) amplifiers or oscillators.
  **\ Switching time:- **t\ (on) & t\ (off) This parameter is rarely important except for transistors used in fast logic interfaces and fast power switching.
  **\ Capacitance:- \**C\ :sub:`in`, C\ :sub:`out` & C\ :sub:`fb` (Or different manufacturers' versions of these.) - These parameters need rarely be specified for LF BJT applications, but since MOSFETs may have quite large C\ :sub:`in` it is sensible to put worst case values into SPICE models of circuits with discrete MOSFETs to ensure that their capacitance is not an issue.

When you enter your chosen parameters into a search engine you will, with luck, obtain a list of devices with the characteristics you need. If you are sure that you have chosen your parameters correctly choose the five to ten cheapest which are available off the shelf. Do the same thing with a couple more distributors' search engines and then compare your lists. You should find that they are similar - if so choose the lowest cost device which is available from most suppliers.

Obtain a SPICE model of this device and make sure that it is compatible with the SPICE simulation of your design. If it is, build prototype hardware with that device and check its performance too. If all is well you've chosen a transistor.

However, when you publish your design, or send it to production, do not specify the device you have chosen as if it were the only possible choice. The specification should read something like:- "Transistor TR3 is an N-channel MOSFET in a TO-92 package (pinout s-g-d on pins 1-2-3), its BV\ :sub:`ds0` should be at least +25V, I\ :sub:`ds(max)` should not be less than 250 mA, V\ :sub:`gs(th)` should be within the limits 600 mv - 1.8V and C\ :sub:`in` should be less than 65 pF. Most NMOSFETs meeting this description should work in this circuit, but the SPICE analysis and prototyping was done with a 2Nxxxx. SPICE analysis of 2Nyyyy, 2Nzzzz and VNaaaa suggests that these devices should also work well, but many other NMOSFETs with similar specifications may be satisfactory too." Of course you should actually do the SPICE analysis of the 2Nyyyy, 2Nzzzz and VNaaaa, which will, of course, be some of the cheapest and most readily available devices from your list.

A similar procedure applies if a design you want to use calls for a 3N14159. and you can't find one. If you have its data study the circuit and decide which of the device parameters are important. If you can't find its data study the circuit and try to determine what transistor parameters are necessary for it to work correctly and safely. Try a SPICE simulation to check functionality, but be a bit conservative in choosing smoke free (i.e. safe - it will not blow up) values of breakdown voltage, current and power since it's not your design and there may be something you've overlooked. Use the values you have chosen in a parametric search, followed by software and hardware checks, as described above. If all goes well you have some substitutes for the 3N14159 and will not have to go to Timbuktu.

James Bryant Calshot - England April 2014

**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/chapter-8>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-9>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`

References
~~~~~~~~~~

[1]Julius Lillienfield - Canadian Patent Application CA272437 (1925) / US Patent US1745175 - Method and apparatus for controlling electric currents 1930-01-28

| [2]Shockley, Brattain & Bardeen - Bell Telephone Labs 1947
| John Bardeen & Walter Brattain:- US Patent US2524035 - Three-electrode circuit element utilizing semiconductive materials 1948-02-26 (Issued 1950-10-03)
| William Shockley:- US Patent US2569347 - Circuit element utilizing semiconductive material 1948-06-26 (Issued 1951-09-25)

[3]\ http://www.elektor.com/

[4]Every engineer should have a box of used components left over from previous projects as a source for suddenly needed parts for new ones. Ideally they should have a reasonable range of stuff, but not so much as to be difficult to search. A matchbox is too small, a 40' intermodal container is generally too large (unless you're a marine engineer working on offshore drilling rigs).

[5]Integrated circuit designers do this far too often when writing data sheets. Instead of specifying a generic part they specify the one they actually used - which was a pre-production sample from a Patagonian start-up that went bankrupt in 1976 or something equally preposterous.This is one of the reasons for the high incidence of insanity among applications engineers, who have to persuade customers that using a substitute is not actually an admission of defeat, nor likely to precipitate Armageddon or rains of frogs and fishes.

[6]"Read The Friendly Data Sheet!"

[7]These references discuss thermal noise and noise figures in the context of resistors and op-amps, but the physics is equally valid for transistors.

http://www.analog.com/en/high-speed-op-amps/low-noise-low-distortion-amplifiers/products/raq_jb_resistor_noise_can_be_deafening_issue25/resources/faq.html?display=popup

http://www.analog.com/en/all-operational-amplifiers-op-amps/operational-amplifiers-op-amps/products/RAQ_JB_Op_Amp_Noise_can_be_Deafening_Too_Issue26/resources/faq.html?display=popup

http://www.analog.com/static/imported-files/rarely_asked_questions/moreInfo_raq_opAmpNoise2.html

| [8]Cadence do a good job at
| http://www.cadence.com/Community/blogs/rf/archive/2008/07/16/measuring-transistor-ft.aspx

[9]"Read The Friendly Data Sheet"

[10]Named after John Milton Miller, who first described its effects in 1920.

https://en.wikipedia.org/wiki/John_Milton_Miller Miller was, of course, working with thermionic valves (tubes) but the name, and the effect, are still valid today with semiconductor triodes (BJTs & FETs).

| [11] Transistor sources
| https://avnetexpress.avnet.com/store/em/EMController/Discrete/Bipolar-Transistor/GP-BJT/_/N-100083?action=products&cat=1&catalogId=500201&categoryLink=true&cutTape=&inStock=&langId=-1&myCatalog=&npi=&proto=&regionalStock=&rohs=&storeId=500201&term=&topSellers=&categoryLink=true and
| https://avnetexpress.avnet.com/store/em/EMController/Discrete/Transistor/MOSFET/_/N-100099?action=products&cat=1&catalogId=500201&categoryLink=true&cutTape=&inStock=&langId=-1&myCatalog=&npi=&proto=&regionalStock=&rohs=&storeId=500201&term=&topSellers=&categoryLink=true

| http://components.arrow.com/semiconductor-discrete/transistors/ and
| http://components.arrow.com/part/search/%5E7/42/855?region=na&whereFrom=gnav and
| http://components.arrow.com/part/search/%5E7/42/942?region=na&whereFrom=gnav

| http://www.digikey.com/product-search/en/discrete-semiconductor-products/transistors-bjt-single/1376376?k=transistor and
| http://www.digikey.com/product-search/en/discrete-semiconductor-products/fets-single/1376381?k=transistor

| http://www.mouser.com/Semiconductors/Discrete-Semiconductors/Transistors/Transistors-Bipolar-BJT/_/N-ax1sh/ and
| http://www.mouser.com/Semiconductors/Discrete-Semiconductors/Transistors/MOSFET/_/N-ax1sf/

http://uk.farnell.com/transistors-bipolar-bjt-single and http://uk.farnell.com/mosfets

| http://uk.rs-online.com/web/c/semiconductors/discrete-semiconductors/bipolar-transistors/ and
| http://uk.rs-online.com/web/c/semiconductors/discrete-semiconductors/mosfet-transistors/
