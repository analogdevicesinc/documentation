Introduction to Transistors
===========================

.. image:: https://wiki.analog.com/_media/analogTV>5118161058001
   :alt: analogTV>5118161058001
   :align: right

Introduction
------------

Transistors are, for the most part, the simplest types of active circuit elements that are capable of increasing, or *amplifying*, the power of electrical signals. They do this by transferring power, usually derived from a DC power supply, to the signal. The operation of many transistor amplifier circuits can be accurately described as modulating the power that is derived from the power supply by the lower power input signal in such a way as to produce an output signal that is a higher power replica of the input signal.

Transistor operation relies on *pn junctions*, which are produced by *doping* silicon with impurity atoms that provide either an excess or shortage of electrons in the covalent bonds of the atoms in the semiconductor crystal structure. Silicon forms a crystal structure in which each atom shares four electrons with its neighbor to form covalent bonds. These four electrons are in the outer shell of each atom, and are referred to as *valence* electrons, and form the bonds. Doping introduces atoms with either three or five valence electrons into the crystal structure, and these atoms form bonds with silicon atoms that either lack one electron or have one extra electron. The atoms with three valence electrons are called *trivalent* and the ones with five valence electrons are called *pentavalent*. When trivalent atoms are introduced, the bonds lack one electron, and when pentavalent atoms are introduced the bonds have one extra electron that can freely move from one atom to another to produce an electrical current. The missing electrons are referred to as *holes* in the bonds, which can move from atom to atom and thereby produce an electrical current. The free electrons and holes are referred to as *carriers*. Silicon that is doped with trivalent atoms is called *p* type due to the fact that its hole concentration is higher than its electron concentration, and silicon doped with pentavalent atoms is called *n* type due to its electron concentration being higher than its hole concentration. A pn junction is formed when silicon is doped such that p material and n material are formed immediately adjacent to each other with a very abrupt boundary between them. Once the junction is formed, some of the free electrons immediately diffuse from the n material to fill the holes in the p material in a process called *recombination*. Recombination produces an electrical potential between the p and n regions at the junction because the diffused electrons produce negative ions in the p material and leave positive ions in the n material. This potential is built into all pn junctions.

Transistors can be divided into two broad categories: bipolar junction transistors (BJTs) and field effect transistors (FETs). BJTs are generally three-terminal transistors that are constructed in one of two arrangements of pn junctions: NPN and PNP. These names are derived form the junctions that comprise the transistors. As indicated by its name, the NPN transistor consists of two pn junctions with p material sandwiched between two regions of n material. Similarly, the PNP transistor consists of two pn junctions with n material sandwiched between two regions of p material. Both holes and electrons function as carriers in BJTs (this is where the term bipolar originates), and each material has *majority* carriers and *minority* carriers. The majority carriers carry the current that is used for the signal, and as would be expected, the majority carriers in PNP transistors are holes and the majority carriers in NPN transistors are electrons. The material sandwiched in the middle of each of these transistors is called the *base*, and is very thin compared with the surrounding material. One end of the transistor is called the *collector* and the other is called the *emitter*. A small current injected into the base, i\ :sub:`B` proportionally controls, or modulates, a much larger current that flows through the collector, i\ :sub:`C`. The proportionality constant is defined as the current gain, β, such that i\ :sub:`C` = βi\ :sub:`B`. By Kirchhoff's Current Law, the emitter current i\ :sub:`E` is equal to i\ :sub:`B` plus i\ :sub:`C`, or i\ :sub:`E` = (1/β)i\ :sub:`C` + βi\ :sub:`C`. Factoring out i\ :sub:`C`, we get i\ :sub:`E` = i\ :sub:`C`\ (1 + 1/β). The current gain is often 100 or more, so the (1 + 1/β) factor can be approximated as 1 with less than 1% error. If we do this we get i\ :sub:`E` ≈ i\ :sub:`C`. This results means that the base current is often small enough to be neglected. Many times when designing with BJTs, the base current is ignored and the collector and emitter currents are approximated to be equal to each other.

FETs are also generally three-terminal transistors, and are available in more varieties than BJTs. The common feature among FETs is that a current flowing through a *channel*, which is a region of p or n type material, is controlled, or modulated, by an applied electric field. The part of the transistor that supplies the field must be isolated from the channel, and the method of isolation falls into two basic categories: isolation provided by reverse-biased pn junctions and isolation provided by an electrically insulating material. Devices that use reverse-biased junction isolation are called Junction FETs, or JFETs, and devices that use insulating materials are called Metal-Oxide Semiconductor FETS, or MOSFETs. JFETs are available with channels made from p material and n material, so we have p-channel JFETs and n-channel JFETs. All JFETs operate in *depletion mode*, which describes how the channel current is controlled. With no applied field, the channel has evenly distributed carriers and acts as a conductor with low resistance. An applied electric field produces a *depletion region* in which the carriers do not flow, thereby reducing the channel current. The electric field, therefore, can be used to control the channel current. The relationship between the applied voltage, which produces the electric field, and channel current is called the *transconductance* g\ :sub:`m`, and varies considerably over the allowable applied voltage range. The terminal at which the channel current enters the JFET is called the *drain* and the terminal at which the current exits the channel is called the *source*. The voltage that produces the electric field is applied across the *gate* and source terminals. For a n-channel JFET, the gate is composed of p material to form the pn junction across which the gate voltage is applied. This gate-source junction is *always* reverse biased or biased at zero volts; it should never be forward biased. There are even more types of MOSFETS, including enhancement and depletion operating modes, each with p channel and n channel. Electrons have a higher mobility than holes, meaning that they are easier to move when influenced by an electric field, and are the carriers in n-channel JFETs, and the majority carriers in NPN BJTs. High mobility is desirable, and is one reason why NPN BJTs and n-channel JFETs are sometimes preferred over their counterparts.

We will begin with BJTs in this lab and move on to FETs in later labs.

Objective
---------

To study the basic operational principles of BJTs. To observe the collector current versus collector-to-emitter voltage characteristics of a NPN transistor for various base currents. To calculate the approximate current gain, β, of the NPN transistor using the observed characteristics. Following completion of this lab you should be able to explain the basic operation of BJTs, explain what the saturation and forward active regions of operation are for BJTs, give a typical base-emitter voltage for a BJT operating in its forward active region, describe what the collector current versus collector-to-emitter voltage characteristics look like for BJTs, calculate the approximate current gain of a BJT, and give a basic description of what the Early effect does to the collector current versus collector-to-emitter voltage characteristics of a BJT.

Materials and Apparatus
-----------------------

-  Data sheet handout for the 2N3904 NPN transistor
-  Computer running PixelPulse software
-  Analog Devices ADALM1000 (M1K)
-  Solderless breadboard and jumper wires from the ADALP2000 Analog Parts Kit
-  (1) 2N3904 NPN transistor from the ADALP2000 Analog Parts Kit
-  (4) 200 KΩ resistor from the ADALP2000 Analog Parts Kit

Procedure
---------

-  Construct the following circuit on the solderless breadboard. The circuit should be built in such a way as to allow three more resistors to be added in parallel to R\ :sub:`B`\


|lab_9_image_1.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard. Note that the R\ :sub:`B` jumper wires are added to facilitate adding resistors in parallel with the 200 KΩ resistor\

|lab_9_assembly_image_1.png|

-  Run PixelPulse and plug in the M1K using the supplied USB cable
-  Update M1K firmware, if necessary
-  Set up the M1K to source voltage/measure current on Channel A
-  Set up Channel A source waveform for a 20 Hz “Triangle” output that swings between 0 V and of 5.0 V
-  Enable X-Y plots
-  Scale the Y-axis of the X-Y plot using the mouse and right mouse button such that the measured current ranges approximately between 0.000 A and 0.009 A (9 mA)
-  Scale the current waveform using the mouse and right mouse button such that the current range between 0.000 A and 0.009 A (9 mA) can be observed with good resolution on Channel A
-  Scale the voltage waveform using the mouse and right mouse button such that a voltage of 0.7 V plus or minus a few tenths of a volt can be observed with good resolution on Channel B
-  Observe the i\ :sub:`C` versus v\ :sub:`CE` characteristic of the transistor with a 200 KΩ resistor in the base circuit
-  Observe the i\ :sub:`C` versus time on Channel A and note the wide regions where the current is relatively constant over varying v\ :sub:`CE` and the dips when the transistor is operating in its saturation region
-  Measure and record the collector current in the wide region
-  Observe the base-emitter voltage v\ :sub:`BE` as approximately 0.7 V in the forward active region; observe the dips in v\ :sub:`BE` when the transistor is operating in its saturation region
-  Calculate i\ :sub:`B` by first determining the voltage across R\ :sub:`B` as the difference between the 2.5 V supplied by the M1K and v\ :sub:`BE`, which is equal to 1.8 V, then using Ohm's law to determine i\ :sub:`B` ≈ (1.8 V)/(200 KΩ) = 9 μA.
-  Calculate the transistor current gain β = i\ :sub:`C`/i\ :sub:`B`
-  Add a 200 KΩ resistor in parallel with the existing base resistor and repeat the previous six steps
-  Add two more 200 KΩ resistors, one at a time, repeating the above procedure
-  Observe that as the base current increases the slope of the i\ :sub:`C` versus v\ :sub:`CE` characteristic increases as a manifestation of the Early effect.
-  If the breadboard was constructed as shown above, when completed it should appear as shown below\

|lab_9_assembly_image_2.png|

Theory
------

An ideal BJT would produce constant collector current i\ :sub:`C` over all values of collector-to-emitter voltage, v\ :sub:`CE`. Real transistors behave close to the ideal, but their collector currents vary slightly over the range of v\ :sub:`CE` that is used in linear operation. This range is called the *forward active region* of the transistor, defined as where the base-emitter junction is forward biased, the collector-base junction is reverse biased, and the collector current is very close to constant over varying v\ :sub:`CE`. When v\ :sub:`CE` becomes small and the collector-base junction becomes forward biased, the transistor enters its *saturation* region of operation. When looking at the i\ :sub:`C` versus v\ :sub:`CE` characteristic, the saturation region can be identified by a steep positive dependence of i\ :sub:`C` on v\ :sub:`CE` for very low v\ :sub:`CE` voltages. As v\ :sub:`CE` increases the transistor moves out of its saturation region into the forward active region, where it is most commonly used. The forward active region is easily identified by a nearly constant i\ :sub:`C` versus v\ :sub:`CE` characteristic. We can see the saturation and forward active regions using the X-Y plot feature in the PixelPulse software. We can also observe that the transistor behavior is not ideal in the forward active region due to the Early effect, in which i\ :sub:`C` varies with v\ :sub:`CE` for a given value of base current, I\ :sub:`B`.

Observations and Conclusions
----------------------------

-  BJTs operate as current amplifiers with current gain defined as β
-  For large β (typically > 100) we can ignore base current and say that the emitter current is approximately equal to the collector current
-  A BJT operating in its forward active region has a forward-biased base-emitter voltage, reverse-biased collector-base junction, and relatively constant collector current over variations in collector-to-emitter voltage
-  When a BJT is operating in its forward active region the base-emitter voltage can be approximated as 0.7 V
-  When a BJT is operating in its saturation region its collector-to-emitter voltage is very small and its collector-base junction becomes forward-biased
-  There is a slight variation in collector current versus collector-to-emitter voltage in the forward active region due to the Early effect

**Return to** :doc:`Engineering Discovery Index </wiki-migration/university/courses/engineering_discovery>`

.. |lab_9_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_9_image_1.png
   :width: 600px
.. |lab_9_assembly_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_9_assembly_image_1.png
   :width: 1000px
.. |lab_9_assembly_image_2.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_9_assembly_image_2.png
   :width: 500px
