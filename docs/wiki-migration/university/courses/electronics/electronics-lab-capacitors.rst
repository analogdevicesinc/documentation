.. warning:: Conversion failed for ``university/courses/electronics/electronics-lab-capacitors``

   Reason: pandoc error: Error at "/tmp/tmp2j3eoa91.txt" (line 273, column 1):
expecting inline
not found
| MOS | 0.01% | Good DA Small Operational above +125° C Low inductance | Limited availability Available only in small capacitance values |
^

.. code-block:: text

   ====== Lab Notes on Capacitors ======
   
   ===== Function: =====
   
   A capacitor is an electrical device for storing charge. In general, capacitors are made from two or more plates of conducting material separated by a layer or layers of insulators. The capacitor can store energy to be returned to a circuit as needed.
   The capacitance //(C)// is defined as the ratio of the stored charge //(Q)// to the potential difference //(V)// between the conductors: 
   
   {{ :university:courses:electronics:acap_e1.png?100 |}}
   
   Capacitance is measured in farads //(F)// and
   
   {{ :university:courses:electronics:acap_e2.png?200 |}}
   
   The energy stored in a capacitor can be found by any of the following three equations, which are each in terms of different variables: 
   
   {{ :university:courses:electronics:acap_e3.png?300 |}}
   
   Capacitors in combination with resistors are used in timing circuits and filters. They are used to smooth or filter the varying DC power supplied by AC to DC rectifiers, by acting as a storage reservoir of charge. They are also used in certain amplifier and signal conditioning circuits because capacitors easily pass higher frequency AC signals but they block DC (constant) signals. 
   
   ===== Capacitance: =====
   
   This is a measure of a capacitor's ability to store charge. A large capacitance means that more charge per volt will be stored. Capacitance is measured in Farads, symbol F. One Farad is a very large capacitance, so prefixes are used to indicate the smaller values. 
   Three prefixes (multipliers) are used, µ (micro), n (nano) and p (pico):
     * µ means 10<sup>-6</sup> (millionth), so 1000 µF = 0.001 F 
     * n means 10<sup>-9</sup> (thousand-millionth), so 1000 nF = 1 µF 
     * p means 10<sup>-12</sup> (million-millionth), so 1000 pF = 1 nF 
   
   Capacitor values can be very difficult to determine from just looking at the capacitor because there are many types of capacitors with different labeling systems.
   
   There are many types of capacitor but they can be split into two groups, **polarized** and **unpolarized**. Each group has its own circuit symbol. 
   
   ==== Polarized capacitors (generally large values, => 1 µF) ====
   
   Examples:
   
   {{:university:courses:electronics:acap_f1.jpg?100 |}} {{:university:courses:electronics:acap_f2.jpg?100 |}}
   
   Circuit Symbol:
       
   {{:university:courses:electronics:acap_f3.png?100 |}}
   
   === Electrolytic Capacitors: ===
   
   Electrolytic capacitors are polarized and **they must be connected with the correct orientation**, at least one of their leads will be marked with a + or -. They are not generally damaged by heat when soldering but can overheat and be damaged if connected with the wrong polarity.
    
   There are two designs of electrolytic capacitors; **axial** where the leads are attached to each end and **radial** where both leads are at the same end. Radial capacitors tend to be a little smaller and they stand upright on the circuit board while axial capacitors can have a lower profile on a PC board but may take up more space.
    
   {{ :university:courses:electronics:acap_f4.png?100 |}}
   
   It is easy to find the value of electrolytic capacitors because they are clearly printed with their capacitance and voltage rating. The voltage rating can be quite low (6V for example) and it should always be checked when selecting an electrolytic capacitor. It the project parts list does not specify a voltage, choose a capacitor with a rating which is greater than the project's power supply voltage. 25V is a sensible minimum for most battery circuits. 
   
   === Tantalum Bead Capacitors ===
   
   Tantalum bead capacitors are polarized and have low voltage ratings similar to electrolytic capacitors. They can be more expensive but are very small, so they are used where a large capacitance is needed in a small space.
   
   {{ :university:courses:electronics:acap_f5.jpg?160 |}}
   
   Modern tantalum bead capacitors are printed with their capacitance and voltage in full. However older ones use a color-code system which has two stripes (for the two digits) and a spot of color for the number of zeros to give the value in µF. The standard color code is used, but for the spot, **grey** is used to mean × 0.01 and **white** means × 0.1 so that values of less than 10µF can be shown. A third color stripe near the leads shows the voltage (yellow 6.3V, black 10V, green 16V, blue 20V, grey 25V, white 30V, pink 35V). 
   For example:   **blue, grey, black spot**   translates to 68µF\\
   For example:   **blue, grey, white spot**   translates to 6.8µF\\
   For example:   **blue, grey, grey spot**   translates to 0.68µF\\
   
   ==== Unpolarized capacitors (small values, up to 1µF) ====
   
   Examples:
   
   {{:university:courses:electronics:acap_f6.jpg?100 |}} {{:university:courses:electronics:acap_f7.jpg?100}}
   {{:university:courses:electronics:acap_f8.png?250}} 
   
   Circuit symbol:
   
   {{:university:courses:electronics:acap_f9.png?200}}
    
   Small value capacitors are unpolarized and may be connected either way round. They are not damaged by heat when soldering, except for one unusual type (polystyrene). They have high voltage ratings of at least 50V, usually 250V or so. It can be difficult to find the values of these small capacitors because there are many types of them and several different labeling systems! 
   
   Many small value capacitors have their value printed but without a multiplier, so you need to use experience to work out what the multiplier should be! 
   
   For example **0.1** translates to 0.1µF = 100nF.
   
   Sometimes the multiplier is used in place of the decimal point:\\
   For example:   **4n7** translates to 4.7nF.
    
   ===== Capacitor Number Code =====
   
   A number code is often used on small capacitors where printing is difficult: 
     -  the 1st number is the 1st digit, 
     -  the 2nd number is the 2nd digit, 
     -  the 3rd number is the number of zeros to give the capacitance in pF. 
     -  Ignore any letters - they indicate tolerance and voltage rating.
   
   {{:university:courses:electronics:acap_f10.png?100 |}} {{:university:courses:electronics:acap_f11.png?60 |}}
   
   For example:   **102** translates to 1000pF = 1nF   //(not 102pF!)//\\
   For example:   **472J** translates to 4700pF = 4.7nF (J = 5% tolerance).\\
   
   ==== Capacitor Color Code ====
   
   A color code similar to the resistor color code was used on polyester capacitors for many years. It is now more or less obsolete, but of course there are many still around. The colors should be read like the resistor code, the top three color bands giving the value in pF. Ignore the 4th band (tolerance) and 5th band (voltage rating). 
   
   **Color Code**
   ^Color^Number^
   |Black|0|
   |Brown|1|
   |Red|2|
   |Orange|3|
   |Yellow|4|
   |Green|5|
   |Blue|6|
   |Violet|7|
   |Grey|8|
   |White|9|
   
   {{:university:courses:electronics:acap_f12.png?70 |}}
   
   For example:\\
   **brown, black, orange**   translates to 10000pF = 10nF = 0.01µF.
    
   Note that there are no gaps between the color bands, so 2 identical bands actually appear as one wide band. 
   
   For example:\\
   **wide red, yellow**   translates to 220nF = 0.22µF. 
   
   ==== Polystyrene Capacitors ====
   
   This type is rarely used now. Their value (in pF) is normally printed without units. Polystyrene capacitors can be damaged by heat when soldering (it melts the polystyrene!) so you should use a heatsink (such as an alligator clip) on the lead while soldering. attach the heatsink onto the lead between the capacitor and the solder joint. 
   
   {{ :university:courses:electronics:acap_f13.png?200 |}}
   
   ==== Real capacitor values (the E3 and E6 series) ====
   
   You may have noticed that capacitors are not available with every possible value, for example 22µF and 47µF are readily available, but 25µF and 50µF are not.
   
   Why is this? Imagine that you decided to make capacitors every 10µF giving 10, 20, 30, 40, 50 and so on. That seems fine, but what happens when you reach 1000? It would be pointless to make 1000, 1010, 1020, 1030 and so on because for these values 10 is a relatively small difference, too small to be noticeable in most circuits and capacitors cannot be made with that accuracy.
   
   To produce a sensible range of capacitor values you need to increase the size of the 'step' as the value increases. The standard capacitor values are based on this idea and they form a series which follows the same pattern for every multiple of ten. 
   
   **The E3 series** (3 values for each multiple of ten) 
   **10, 22, 47,** ... then it continues 100, 220, 470, 1000, 2200, 4700, 10000 etc. 
   
   Notice how the step size increases as the value increases (values roughly double each time). 
   **The E6 series** (6 values for each multiple of ten) 
   **10, 15, 22, 33, 47, 68,** ... then it continues 100, 150, 220, 330, 470, 680, 1000 etc. 
   Notice how this is the E3 series with an extra value in the gaps.
   
   The E3 series is the one most frequently used for capacitors because many types cannot be made with very accurate values.
   
   ===== Understanding the Parasitic Effects In Capacitors: =====
   
   Determining the right capacitor type for a particular circuit application is not that difficult. Generally, you  will find that most capacitors fall into one of four application categories:
   
     - AC coupling, including bypassing (passing ac signals while blocking dc)
     - Decoupling (filtering ac or high frequencies superimposed on dc or low frequencies in power, reference, and signal circuitry)
     - Active/passive RC filters or frequency-selective networks
     - Analog integrators and sample-and-hold circuits (acquiring and storing charge)
   
   {{ :university:courses:electronics:acap_f14.gif?400 |}}
   
   <WRAP centeralign> Figure 1 Capacitor applications </WRAP>
   
   Even though there are more than a dozen or so popular capacitor types- including poly, film, ceramic, electrolytic, etc.- you will find that, in general, only one or two types will be best suited for a particular application, because the salient imperfections, or “parasitic effects” on system performance associated with other types of capacitors will cause them to be eliminated.
   
   Unlike an “ideal” capacitor, a “real” capacitor is typified by additional “parasitic” or “non-ideal” components or behavior, in the form of resistive and inductive elements, nonlinearity, and dielectric memory. The resulting characteristics due to these components are generally specified on the capacitor manufacturer’ s data sheet . Understanding the effects of these parasitics in each application will help you select the right capacitor type.
   
   {{ :university:courses:electronics:acap_f15.gif?400 |}}
   
   <WRAP centeralign> Figure 2 Model of a “Real” Capacitor </WRAP>
   
   The four most common effects are leakage (parallel resistance), equivalent series resistance (ESR), equivalent series inductance (ESL), and dielectric absorption (memory).
   
   **Capacitor Leakage, RP:** Leakage is an important parameter in ac coupling applications, in storage applications, such as analog integrators and sample-holds, and when capacitors are used in high-impedance circuits.
   
   {{ :university:courses:electronics:acap_f16.gif?400 |}}
   
   <WRAP centeralign> Figure 3 Capacitor Leakage </WRAP>
   
   In an ideal capacitor, the charge, Q, varies only in response to current flowing externally. In a real capacitor, however, the leakage resistance allows the charge to trickle off at a rate determined by the R-C time constant.
   
   Electrolytic-type capacitors (tantalum and aluminum), distinguished for their high capacitance, have very high leakage current (typically of the order of about 5-20 nA per µF) due to poor isolation resistance, and are not suited for storage or coupling applications.
   
   The best choices for coupling and/or storage applications are Teflon (polytetrafluorethylene) and the other “ poly” types (polyproplene, polystyrene, etc).
   
   **Equivalent Series Resistance (ESR), RS:** The equivalent series resistance (ESR) of a capacitor is the resistance of the capacitor leads in series with the equivalent resistance of the capacitor plates. ESR causes the capacitor to dissipate power (and therefor produce loss) when high ac currents are flowing. This can have serious consequences at RF and in supply decoupling capacitors carrying high ripple currents, but is unlikely to have much effect in precision high-impedance, low-level analog circuitry.
   
   Capacitors with the lowest ESR include both the mica and film types.
   
   **Equivalent Series Inductance (ESL), LS:** The equivalent series inductance (ESL) of a capacitor models the inductance of the capacitor leads in series with the equivalent inductance of the capacitor plates. Like ESR, ESL can also be a serious problem at high (RF) frequencies, even though the precision circuitry itself may be operating at DC or low frequencies. The reason is that the transistors used in precision analog circuits may have gain extending up to transition frequencies (F<sub>t</sub>) of hundreds of MHz, or even several GHz, and can amplify resonances involving low values of inductance. This makes it essential that the power supply terminals of such circuits be decoupled properly at high frequency.
   
   Electrolytic, paper, or plastic film capacitors are a poor choice for decoupling at high frequencies; they basically consist of two sheets of metal foil separated by sheets of plastic or paper dielectric and formed into a roll. This kind of structure has considerable self inductance and acts more like an inductor than a capacitor at frequencies exceeding just a few MHz.
   
   A more appropriate choice for HF decoupling is a monolithic, ceramic-type capacitor, which has very low series inductance. It consists of a multilayer sandwich of metal films and ceramic dielectric, and the films are joined in parallel to bus-bars, rather than rolled in series.
   
   A minor tradeoff is that monolithic ceramic capacitors can be microphonic (i.e., sensitive to vibration), and some types may even be self-resonant, with comparatively high Q, because of the low series resistance accompanying their low inductance. Disc ceramic capacitors, on the other hand, are sometime quite inductive, although less expensive.
   
   Because leakage, ESR, and ESL are almost always difficult to spec separately, many manufacturers will lump leakage, ESR and ESL into a single specification known as dissipation factor, or DF, which basically describes the inefficiency of the capacitor. DF is defined as the ratio of energy dissipated per cycle to energy stored per cycle. In practice, this is equal to the power factor for the dielectric, or the cosine of the phase angle. If the dissipation at high frequencies is principally modeled as series resistance, at a critical frequency of interest, the ratio of equivalent series resistance, ESR, to total capacitive reactance is a good estimate of DF,
   
   <m> DF approx omega R_{S} C </m>
   
   Dissipation factor also turns out to be the equivalent to the reciprocal of the capacitor’ s figure of merit, or Q, which is also sometimes included on the manufacturer’ s data sheet.
   
   **Dielectric Absorption, RDA, CDA:** Monolithic ceramic capacitors are excellent for HF decoupling, but they have considerable dielectric absorption, which makes them unsuitable for use as the hold capacitor of a sample-hold amplifier (SHA). Dielectric absorption is a hysteresis-like internal charge distribution that causes a capacitor which is quickly discharged and then open-circuited to appear to recover some of its charge. Since the amount of charge recovered is a function of its previous charge, this is, in effect, a charge memory and will cause errors in any SHA where such a capacitor is used as the hold capacitor.
   
   {{ :university:courses:electronics:acap_f17.gif?400 |}}
   
   <WRAP centeralign> Figure 4 Dielectric Absorption </WRAP>
   
   Capacitors that are recommended for this type of application include the “poly” type capacitors we spoke about earlier, i.e., polystyrene, polypropylene, or Teflon. These capacitor types have very low dielectric absorption (typically <0.01%).
   
   *The characteristics of capacitors in general are summarized in the capacitor comparison chart below.
   
   **A note about high-frequency decoupling in general:** The best way to insure that an analog circuit is adequately decoupled at both high and low frequencies is to use an electrolytic-type capacitor, such as a tantalum bead, in parallel with a monolithic ceramic one. The combination will have high capacitance at low frequency, and will remain capacitive up to quite high frequencies. It’ s generally not necessary to have a tantalum capacitor on each individual IC, except in critical cases; if there is less than 10 cm of reasonably wide PC track between each IC and the tantalum capacitor, it’ s possible to share one tantalum capacitor among several ICs.
   
   Another thing to remember about high frequency decoupling is the actual physical placement of the capacitor. Even short lengths of wire have considerable inductance, so mount the HF decoupling capacitors as close as possible to the IC, and ensure that leads consist of short, wide PC tracks.
   
   Ideally, HF decoupling capacitors should be surface-mount parts to eliminate lead inductance, but wire-ended capacitors are ok, providing the device leads are no longer than 1.5 mm.
   
   {{ :university:courses:electronics:acap_f18.gif?400 |}}
   
   <WRAP centeralign> Figure 5 </WRAP>
   
   ===== Stray Capacitance: =====
   
   Now that we have talked about the parasitic effects of capacitors as components, let us talk about another form of parasitic known as “stray” capacitance.
   
   As in a parallel-plate capacitor, stray capacitors are formed whenever two conductors are in close proximity to each other (especially if they are running in parallel), and are not shorted together or screened by a conductor serving as a Faraday shield.
   
   {{ :university:courses:electronics:acap_f19.gif?400 |}}
   
   <WRAP centeralign> Figure 6 Capacitor Model </WRAP>
   
   Stray or “parasitic” capacitance commonly occurs between parallel traces on a PC board or between traces/planes on opposite sides of a PC board. The occurrence and effects of stray capacitance- especially at very high frequencies - are unfortunately often overlooked during circuit modeling and can lead to serious performance problems when the system circuit board is constructed and assembled; examples include greater noise, reduced frequency response, even instability.
   
   {{ :university:courses:electronics:acap_f20.gif?400 |}}
   
   <WRAP centeralign> Figure 7 </WRAP>
   
   For instance, if the capacitance formula is applied to the case of traces on opposite sides of a board, then for general purpose PCB material (ER = 4.7, d = 1.5 mm), the capacitance between conductors on opposite sides of the board is just under 3 pF/cm2. At a frequency of 250 MHz, 3 pF corresponds to a reactance of 212.2 ohms!
   
   You can never actually “eliminate” stray capacitance; the best you can do is take steps to minimize its effects in the circuit.
   
   One way to minimize the effects of stray coupling is to use a Faraday shield, which is simply a grounded conductor between the coupling source and the affected circuit.
   
   Look at Figure 8; it is an equivalent circuit showing how a high-frequency noise source, V<sub>N</sub>, is coupled into a system impedance, Z, through a stray capacitance, C. If we have little or no control over V<sub>n</sub> or the location of Z<sub>1</sub>, the next best solution is to interpose a Faraday shield:
   
   {{ :university:courses:electronics:acap_f21.gif?400 |}}
   
   <WRAP centeralign> Figure 8 </WRAP>
   
   As shown, below in Figure 9, the Faraday shield interrupts the coupling electric field. Notice how the shield causes the noise and coupling currents to return to their source without flowing through Z<sub>1</sub>.
   
   {{ :university:courses:electronics:acap_f22.gif?400 |}}
   
   <WRAP centeralign> Figure 9 </WRAP>
   
   Another example of capacitive coupling is in side-brazed ceramic IC packages. These DIP packages have a small, square, conducting Kovar lid soldered onto a metallized rim on the ceramic package top. Package manufacturers offer only two options: the metallized rim may be connected to one of the corner pins of the package, or it may be left unconnected. Most logic circuits have a ground pin at one of the package corners, and therefore the lid is grounded. But many analog circuits do not have a ground pin at a package corner, and the lid is left floating. Such circuits turn out to be far more vulnerable to electric field noise than the same chip in a plastic DIP package, where the chip is unshielded.
   
   {{ :university:courses:electronics:acap_f23.gif?400 |}}
   
   <WRAP centeralign> Figure 10 </WRAP>
   
   Whatever the environmental noise level, it is good practice for the user to ground the lid of any side brazed ceramic IC where the lid is not grounded by the manufacturer. This can be done with a wire soldered to the lid (this will not damage the device, as the chip is thermally and electrically isolated from the lid). If soldering to the lid is unacceptable, a grounded phosphor-bronze clip may be used to make the ground connection, or conductive paint can be used to connect the lid to the ground pin. //Never attempt to ground such a lid without verifying that it is, in fact, unconnected//; there do exist device types with the lid connected to a supply rail rather than to ground!
   
   One case where a Faraday shield is impracticable is between the bond wires of an integrated circuit chip. This has important consequences. The stray capacitance between two chip bond wires and their associated leadframes is of the order of 0.2 pF; observed values generally lie between 0.05 and 0.6 pF.
   
   {{ :university:courses:electronics:acap_f24.gif?400 |}}
   
   <WRAP centeralign> Figure 11 </WRAP>
   
   Consider a high-resolution converter (ADC or DAC), which is connected to a high-speed data bus. Each line of the data bus, (which will be switching at around 2 to 5 V/ns),will be able to influence the converter’ s analog port via this stray capacitance; the consequent coupling of digital edges will degrade the performance of the converter.
   
   {{ :university:courses:electronics:acap_f25.gif?400 |}}
   
   <WRAP centeralign> Figure 12 </WRAP>
   
   This problem may be avoided by isolating the data bus, interposing a latched buffer as an interface. Although this solution involves an additional component that occupies board area, consumes power, and adds cost, it can significantly improve the converter’ s signal-to-noise.
   
   {{ :university:courses:electronics:acap_f26.gif?400 |}}
   
   <WRAP centeralign> Figure 13 </WRAP>
   
   ===== CAPACITOR COMPARISON CHART =====
   
   ^ TYPE ^ TYPICAL DIELECTRIC ABSORPTION ^ ADVANTAGES ^ DISADVANTAGES ^
   | NPO ceramic | <0.1% | Small case size Inexpensive Good stability Wide range of values Many vendors Low inductance | DA generally low, but may not be specified Limited to small values (10 nF) |
   | Polystyrene | 0.001% to 0.02% | Inexpensive Low DA available Wide range of values Good stability 	| Damaged by temperature > +85° C Large case size High inductance |
   | Polypropylene	| 0.001% to 0.02% | Inexpensive Low DA available Wide range of values | Damaged by temperature > +105° C Large case size High inductance |
   | Teflon | 0.003% to 0.02% | Low DA available Good stability Operational above +125° C Wide range of values | Relatively expensive Large size High inductance
   | MOS | 0.01% | Good DA Small Operational above +125° C Low inductance | Limited availability Available only in small capacitance values |
   |Polycarbonate | 0.1% | Good stability Low cost Wide temperature range | Large size DA limits to 8-bit applications High inductance |
   | Polyester | 0.3% to 0.5% | Moderate stability Low cost Wide temperature range Low inductance (stacked film) | Large size DA limits to 8-bit applications High inductance |
   | Monolithic ceramic (High K) | >0.2% | Low inductance Wide range of values | Poor stability Poor DA High voltage coefficient |
   | Mica | >0.003% | Low loss at HF Low inductance Very stable Available in 1% values or better | Quite large Low values (<10 nF) Expensive |
   | Aluminum electrolytic	| High | Large values High currents High voltages Small size | High leakage Usually polarized Poor stability Poor accuracy Inductive |
   | Tantalum electrolytic | High | Small size Large values Medium inductance | Quite high leakage Usually polarized Expensive Poor stability Poor accuracy |
   
   ==== For more info on passive components see: ====
   
   [[adi>static/imported-files/application_notes/500824934643930414583807523874018494695982855668424783486554001060AN348.pdf|AN-348: Avoiding Passive-Component Pitfalls]]
   
   **Return to Lab Activities [[university:courses:electronics:labs|Table of Contents]]**
   
