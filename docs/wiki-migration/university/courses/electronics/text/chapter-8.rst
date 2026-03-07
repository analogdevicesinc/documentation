Chapter 8: Transistors
======================

In this chapter we will explore our first active devices.

8.1 Basic principles
--------------------

An active device is any type of component with the ability to electrically control the flow of current (controlling one electric signal with another electric signal). For a circuit to be called electronic, it must contain at least one active device. All active devices control the flow of current through them. One type of active device uses a voltage to control the current while another type of active devices uses another current to be the controlling signal. Devices utilizing a voltage as the controlling signal are, not surprisingly, called voltage-controlled devices. Devices working on the principle of one current controlling another current are known as current-controlled devices. The first type of transistor successfully demonstrated was a current-controlled device.

As a side note: The origin of the term transistor is a contraction of "transconductance varistor", as proposed by Bell Telephone Laboratories. It is sometimes incorrectly attributed to a contraction of transresistance.

A simple and general form of such a device is shown in figure 8.1.1. It has three terminals; we will call them X, Y and Z for the moment. Let's also assume that the controlled current flows into terminal X and back out terminal Y. The third terminal, Z, is the control terminal. To describe the function of this block we first need to define the terminal currents *IX*\ <sub></sub>, //IY //and *IZ*\ :sub:`,` and the terminal voltages //VXY //and *VZY* as shown in the figure. Because current flows into terminal X, we generally assume the voltage seen at X is greater than terminal Y and voltage *VXY* is a positive number. The same can be said for the voltage seen at terminal Z with respect to terminal Y and voltage *VZY* is a positive number.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8.1.1 General Model


In the case of a current controlled device, let's assume that the control current *IZ,*\ <sub></sub>flows into terminal Z and back out terminal Y. Conservation of charge tells us that the sum of the currents flowing into a box must equal the sum of the currents flowing out. Thus *IY*\ <sub></sub>= *IX* + *IZ*. To make the device useful it would be desirable to have the control current *IZ* very small relative to the much larger controlled current *IX*. The ratio of *IX* to *IZ* is the gain of the device and the Greek letter β (beta) is used to represent this gain. The ratio of *IX*\ <sub></sub>to *IY* which is always less than unity, is also a measure of the device gain and is most often represented by the Greek letter α (alpha).

For the voltage controlled device let's assume, as we did before, that the current flows into terminal X and out terminal Y. The voltage on terminal Z now controls the amount of current in terminals X and Y. This voltage now needs to be referenced with respect to one of the two other terminals and we will use terminal Y for our purposes here. Also, since a voltage is the control signal in this case, we will assume that no current flows into (or out of) terminal Z. Comparing this back to the current controlled device we can say that α = 1 and β is infinite. The output current to control voltage relationship, expressed as amps/volt, is dimensionally a conductance and the letter *g* is most often used to represent conductance. This parameter of a transistor is called transconductance and *gm* is the common usage.

We can also describe complementary devices by reversing the direction of the currents such that the controlled current now flows out of terminal X and into terminal Y as shown in figure 8.1.2. Because direction of the current is now reversed, we generally assume the voltage seen at Y is greater than terminal X and voltage *VXY* is a negative number. The same can be said for the voltage seen at terminal Z with respect to terminal Y and voltage *VZY* is a negative number. For the current controlled case we also reverse the direction of the control current I\ :sub:`Z` which now flows out of terminal Z.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8.1.2 Complementary Model


To summarize we have described four types of active devices, a positive current controlled current source and it's complementary negative form, and a positive voltage controlled current source and it's complementary negative form.

8.1.1 Simple model characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we will examine the transfer characteristics of these simple transistor models and how they may need to be modified or extended to make them more realistic. First we will examine the output current vs. output voltage characteristics of a simple (ideal) voltage controlled current source as the voltage on the control input is stepped. The results for a controlled source with a transconductance of 1 mA/V is shown in figure 8.1.3 as V\ :sub:`XY` is swept from 0 to 5V and the control voltage V\ :sub:`ZY` is stepped in 0.4 volt increments from 0.1 V to 2.1 V. An ideal current controlled current source would have essentially the same characteristics except that each horizontal line would represent a different control current (in terminal Z) rather than a different control voltage.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8.1.3 Ideal Voltage (or Current) controlled current source characteristics


From these characteristic curves we can learn the following; first the current is indeed independent of the voltage across the X and Y terminals. Second, the current I\ :sub:`XY` is equal to 1mA per volt applied to the Z terminal with respect to the X terminal (figure 8.1.1). However, there is one thing that is evident that cannot happen in a real device and that is having I\ :sub:`XY` be something other than zero when the voltage V\ :sub:`XY` is zero. This implies that the device contains a source of energy and we know that is impossible. Otherwise we would have a solution to the world's energy crisis. A more realistic set of characteristics is something more like those shown in figure 8.1.4.

Curves like those in figure 8.1.4 make more physical sense but still have some properties that actual devices can't have. The plot shows abrupt breaks in the curves where the angled line, which goes through the origin, intersects the horizontal line at the constant controlled current value. This transition can never be this sharp and must somehow smoothly transition from one line to the other.

Another property of these simple curves is the perfectly horizontal nature of the current vs. voltage lines. A real device will show some change, usually an increase due to a finite real resistance, with the voltage across X and Y.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8.1.4 VCCS current must be zero when V\ :sub:`XY` = 0


A more complete complex mathematical model of the real physical transistor is shown in figure 8.1.5. We will explore this more complete model in the coming sections of this chapter.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8.1.5 Complex mathematical device model


8.2 Transistor Symbols
----------------------

There are four transistor types that correspond to these basic active device models. The schematic symbols for these are shown in figure 8.2.1. The n-type current controlled device is the NPN Bipolar Junction Transistor (BJT). The p-type current controlled device is the PNP BJT. The n-type voltage controlled device is the NMOS FET (metal oxide semiconductor field effect transistor). And finally, the p-type voltage controlled device is the PMOS FET. Rather than giving the device terminals generic names like X, Y and Z, the established convention for the BJT is Collector and Emitter for the current source terminals and Base for the current control terminal. Similarly, the convention for the MOS device is Drain and Source for the current source terminals and Gate for the voltage control terminal,

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8.2.1 transistor symbols


Note: Unless the reader gets into device fabrication, it is generally less important to understand the inner workings of transistors. The descriptions which one gets by getting into the intrinsic properties are not particularly satisfying for circuit design and can be difficult to fully comprehend. Rather for circuit analysis and design, it is usually enough to understand the extrinsic properties of transistors, treating them more or less as a black box. Adding some discussion about the subtleties which arise from the physics going on inside the black box is of course necessary for robust circuit design.

8.3 Bipolar Junction Transistor basics
--------------------------------------

A bipolar junction transistor (BJT) is a three-terminal electronic device constructed of doped semiconductor material and may be used in amplifying or switching applications. Bipolar transistors are so named because their operation involves both electrons and holes. Charge flow in a BJT is due to bidirectional diffusion of charge carriers across a junction between two regions of different charge concentrations. By design, most of the BJT collector current is due to the flow of charges injected from a high-concentration emitter into the base where they are minority carriers that diffuse toward the collector, and so BJTs are classified as minority carrier devices This mode of operation is contrasted with majority carrier transistors, such as field-effect transistors, in which only majority carriers are involved in current flow due to drift.

The typical cross section of a planar NPN transistor is shown in figure 8.3.1. An NPN transistor can be viewed as two PN junction diodes with a very thin shared anode, P layer. In typical operation, the base-emitter junction is forward biased and the base collector junction is reverse biased. In an NPN transistor, for example, when a positive voltage is applied to the base-emitter junction, the equilibrium between thermally generated carriers and the repelling electric field of the depletion region becomes unbalanced, allowing thermally excited electrons to inject into the base region. These electrons wander (or "diffuse") through the very thin base from the region of high concentration near the emitter towards the region of low concentration near the collector. The electrons in the base are called minority carriers because the base is doped p-type which would make holes the majority carrier in the base.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f7.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 8.3.1 Cross section of a planar NPN transistor


To minimize the percentage of carriers that recombine before reaching the collector-base junction depletion layer, the transistor's base region must be thin enough that carriers can diffuse across it in much less time than the semiconductor's minority carrier lifetime. In particular, the thickness of the base must be much less than the diffusion length of the electrons. The collector base junction is reverse-biased, and so little electron injection occurs from the collector to the base, but electrons that diffuse through the base towards the collector are swept into the collector by the electric field in the depletion region of the collector-base junction. The thin shared base and asymmetric collector-emitter doping is what differentiates a bipolar transistor from two separate and oppositely biased diodes stacked in series.

8.3.1 Voltage, current, and charge control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The collector emitter current can be viewed as being controlled by the base-emitter current (current control), or by the base-emitter voltage (voltage control). These views are related by the current-voltage relation of the base-emitter junction, which is just the usual exponential current-voltage curve of a PN junction (diode).

The physical explanation for collector current is the amount of minority-carrier charge in the base region.

Detailed models of transistor action, such as the Gummel-Poon model, account for the distribution of this charge explicitly to explain transistor behavior more exactly. The charge-control view easily handles phototransistors, where minority carriers in the base region are created by the absorption of photons, and handles the dynamics of turn-off, or recovery time, which depends on charge in the base region recombining. However, because base charge is not a signal that is visible at the terminals, the current- and voltage-control views are generally used in circuit design and analysis.

In analog circuit design, the current-control view is sometimes used because it is approximately linear. That is, the collector current is approximately ?\ :sub:`F` times the base current. Some basic circuits can be designed by assuming that the emitter-base voltage is approximately constant, and that collector current is beta times the base current. However, to accurately and reliably design robust BJT circuits, the voltage-control (for example, Ebers-Moll) model is more often used. The voltage-control model requires an exponential function to be taken into account. The following equation for the collector current I\ :sub:`C` shows the exponential relationship to V\ :sub:`BE`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e1.png
   :align: center
   :width: 250px

A fairly standard transistor operating at around 100uA may have a V\ :sub:`BE`\ of around 650mV at room temperature where q/kT is about 0.039/mV (or the thermal voltage, kT/q is 25mV). The exponential factor in the equation will be on the order of 10\ :sup:`11`. In this case we can safely drop the -1 term in the equation without serious error. Taking the natural logarithm, we get the equation for V\ :sub:`BE`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e2.png
   :align: center
   :width: 200px

When this exponential is linearized such that the transistor can be modeled as a transconductance, as in the Ebers-Moll model, design for circuits such as amplifiers again becomes a mostly linear problem, so the voltage-control view is often preferred. For translinear circuits, in which the exponential I-V curve is key to the operation, the transistors are usually modeled as voltage controlled with transconductance proportional to collector current. In general, transistor level circuit design is performed using SPICE or a comparable analog circuit simulator, so model mathematical complexity is usually not of much concern to the designer.

8.3.2 Transistor alpha and beta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The proportion of electrons able to cross the base and reach the collector is a measure of the BJT efficiency. The asymmetric heavy doping of the emitter region and light doping of the base region cause many more electrons to be injected from the emitter into the base than holes to be injected from the base into the emitter. The common\ *-*\ emitter// *current* //gain is represented by ß\ :sub:`F` or h\ :sub:`fe` and is approximately the ratio of the DC collector current to the DC base current in the forward-active region. It is typically greater than 100 for small-signal transistors but can be smaller in transistors designed for high-power applications. Another important parameter is the common-base current gain, a\ :sub:`F`. The common-base current gain is approximately the gain of current from emitter to collector in the forward-active region. This ratio usually has a value close to unity; between 0.98 and 0.998. Alpha and beta are more precisely related by the following identities (NPN transistor):

|image1| |image2| |image3|

A BJT consists of three differently doped semiconductor regions, the emitter region, the base region and the collector region. These regions are, respectively, *p* type, *n* type and *p* type in a PNP, and *n* type, *p* type and *n* type in a NPN transistor. Each semiconductor region is connected to a terminal, appropriately labeled: emitter (E), base (B) and collector (C).

The base is physically located between the emitter and the collector and is made from lightly doped, high resistivity material. The collector surrounds the emitter and base regions (figure 8.3.1), making it almost impossible for the electrons injected into the base region from the emitter region to escape being collected, thus making the resulting value of a very close to unity, and so, giving the transistor a large ß. A cross section view of a BJT, figure 8.3.1, indicates that the collector-base junction has a much larger area than the emitter-base junction.

The bipolar junction transistor, unlike the MOSFET transistor which we will discuss in detail shortly, is usually not a symmetrical device. This means that interchanging the collector and the emitter makes the transistor leave the forward active mode and start to operate in what is called the reverse active mode.

Because the transistor's internal structure is usually optimized for forward-mode operation, interchanging the collector and the emitter makes the values of a and ß in reverse operation much smaller than those in forward operation; often the a of the reverse mode is lower than 0.5. The lack of symmetry is primarily due to the relative doping ratios of the emitter and the collector. The emitter is heavily doped, while the collector is lightly doped, allowing a large reverse bias voltage to be applied before the collector-base junction breaks down. The collector-base junction is reverse biased in normal operation. The reason the emitter is heavily doped is to increase the emitter injection efficiency: the ratio of carriers injected by the emitter to those injected by the base. For high current gain, most of the carriers injected into the emitter-base junction must come from the emitter.

The low-performance "lateral" bipolar transistors sometimes used in CMOS processes are sometimes designed symmetrically, that is, with no difference between forward and backward operation, figure 8.3.2. However, because the base width is often much larger than the vertical structure of figure 8.3.1 ß and a are not nearly as high. A layout technique to improve collection efficiency is to surround the emitter region completely on all four sides with a ring or doughnut shaped collector region. This structure is now no longer symmetrical of course.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f8.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 8.3.2 Lateral NPN cross section


Small changes in the voltage applied across the base-emitter terminals causes the current that flows between the emitter and the collector to change significantly. This effect can be used to amplify the input voltage or current. BJTs can be thought of as voltage-controlled current sources, but are more simply characterized as current-controlled current sources, or current amplifiers, due to the relatively low impedance seen at the base.

Early transistors were made from germanium but most modern BJTs are made from silicon. Special purpose devices are also made from III-V element compound semiconductors like gallium arsenide, especially for very high frequency applications.

8.3.3 NPN
~~~~~~~~~

The NPN is one of the two types of bipolar transistors, in which the letters "N" (negative) and "P" (positive) refer to the majority charge carriers inside the different regions of the transistor. Better performing bipolar transistors produced today are NPN, because electron mobility is higher than hole mobility in semiconductors, allowing greater currents and faster operation.

NPN transistors consist of a layer of P-doped semiconductor (the "base") sandwiched between two N-doped layers. A small current entering the base in common-emitter mode is amplified in the collector output. In other terms, an NPN transistor is "on" when its base is pulled high relative to the emitter. The arrow in the NPN transistor symbol is on the emitter leg and points in the direction of the conventional current flow when the device is in the forward active operating mode.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f9.png
   :align: center
   :width: 400px

One mnemonic device for identifying the symbol for the NPN transistor is "**n**\ ot **p**\ ointing i\ **n**, or '**n**\ ot **p**\ ointing, **n**\ o' "

8.3.4 PNP
~~~~~~~~~

The other type of BJT is the PNP with the letters "P" and "N" referring to the majority charge carriers inside the different regions of the transistor.PNP transistors consist of a layer of N-doped semiconductor between two layers of P-doped material. A small current leaving the base in common-emitter mode is amplified in the collector output. In other terms, a PNP transistor is "on" when its base is pulled low relative to the emitter.

The arrow in the PNP transistor symbol is on the emitter leg and points in the direction of the conventional current flow when the device is in forward active mode.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f10.png
   :align: center
   :width: 400px

8.3.5 BJT Regions of operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bipolar transistors have five distinct regions of operation, defined by the way the junctions are biased. In order to visualize the modes of operation draw an NPN transistor with its collector on top, base in the middle and emitter on the bottom. Now, there are two voltage differences: between Collector and base, and between base and emitter. Note two points: V\ :sub:`CB` = -V\ :sub:`BC`, and 'reverse biased base-collector junction' means V\ :sub:`BC` < 0 or V\ :sub:`CB`>0. In simple words, it means the collector has a higher voltage than the base (if probed). The mechanical analog can be a pipe and a valve.

The valve is base, and two sides of the pipe are collector and emitter. Now the amount of water (current) going through depends on how much the valve is open (base to emitter voltage), and how much water you have on top of the pipe (collector to base voltage). If you write the biases in term of applied voltages (V\ :sub:`CB`, V\ :sub:`BE`) instead of junction biasing the modes of operation can be described as:

-   Forward Active: Base higher than Emitter, Collector higher than Base ( in this mode the collector current is proportional to base current by β\ :sub:`F`).
   \* Saturation: Base higher than emitter, but collector is not higher than base.
   \* Cut-Off: Base lower than emitter, but collector is higher than base. It means the transistor is not letting conventional current to go through collector to emitter.
   \* Reverse Active: Base lower than emitter, collector lower than base: reverse conventional current goes through transistor.

| In terms of junction biasing: ('reverse biased base-collector junction' means V\ :sub:`BC`\ <0 or V\ :sub:`CB`>0)
| \* Forward\ **-**\ active (or simply, active): The base-emitter junction is forward biased and the base-collector junction is reverse biased. Most bipolar transistors are designed to afford the greatest common-emitter current gain, β\ :sub:`F`, in forward-active mode. If this is the case, the collector-emitter current is approximately proportional to the base current, but many times larger, for small base current variations.
| \* Reverse\ **-**\ active (or inverse\ **-**\ active or inverted): By reversing the biasing conditions of the forward-active region, a bipolar transistor goes into reverse-active mode. In this mode, the emitter and collector regions switch roles. Because most BJTs are designed to maximize current gain in forward-active mode, the β\ :sub:`F` in inverted mode is several (2-3 for the ordinary germanium transistor) times smaller. This transistor mode is seldom used, usually being considered only for failsafe conditions and some types of bipolar logic. The reverse bias breakdown voltage to the base may be an order of magnitude lower in this region.
| \* Saturation: With both junctions forward-biased, a BJT is in saturation mode and facilitates high current conduction from the emitter to the collector. This mode corresponds to a logical "on", or a closed switch.
| \* Cutoff: In cutoff, biasing conditions opposite of saturation (both junctions reverse biased) are present. There is very little current flow, which corresponds to a logical "off", or an open switch.

-   Avalanche*\* **breakdown** \**region

Although these regions are well defined for sufficiently large applied voltage, they overlap somewhat for small (less than a few hundred millivolts) biases. For example, in the typical grounded-emitter configuration of an NPN BJT used as a pull-down switch in digital logic, the "off" state never involves a reverse-biased junction because the base voltage never goes below ground; nevertheless the forward bias is close enough to zero that essentially no current flows, so this extreme of the forward active region can be regarded as the cutoff region.

8.4.1 Bipolar Junction Transistor large signal Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As we just learned, the bipolar junction transistor (BJT) can operate in one of three regions:

-   Cutoff region: Transistor is off and no current flows between collector and emitter (i.e., collector-emitter resistance is infinite).
   \* Active region: Transistor acts like a current controlled current source between collector and emitter as in the basic model.
   \* Saturation region: When the voltage between collector and emitter drops below a certain level (typically when the collector to base voltage is zero or less) the base current increases and the ratio of *I\ C* to *I\ B*, or β is much smaller than in the active region.

In the active region, the transistor adjusts the collector current to be ? times the base current. If the base current I\ :sub:`B`, falls to 0, the transistor enters the cutoff region and shuts off. When the collector voltage becomes less than or equal to the base voltage the base current rises and β falls. In this case, the transistor enters the saturation region. To keep the transistor out of the saturation region, the general rule of thumb is that the voltage on the collector should be more positive than the voltage on the base. That is the collector base junction is always reversed biased.

A simple model for the operation of NPN and PNP BJT transistors in the active region is shown in figure 8.4.1. It requires knowing the current gain β in order to design a circuit. In both of these models,

.. container:: centeralign

   I\ :sub:`C` = βI\ :sub:`B`, I\ :sub:`E` = (β + 1)I\ :sub:`B` and


.. container:: centeralign

   I\ :sub:`E`\ =I\ :sub:`C`\ +I\ :sub:`B`


The emitter is separated from the base by a diode. In order for this diode to conduct current, in the case of a Silicon based device, it must be forward biased with ~0.65V.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8.4.1 (a) Active region NPN (b) Active region PNP


The Base-Emitter Diode: Always keep figure 8.4.1 in mind. The Ebers-Moll model of a BJT treats the current-voltage relationship of the base-emitter junction just like a Shockley ideal diode whose current is mirrored in the collector with gain. When V\ :sub:`B` and V\ :sub:`E` are not obvious, remember the base-emitter diode.

8.4.2 Early Effect (Base width modulation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Early Effect was first observed and explained by James Early while at Bell Labs. In our ideal device, the collector current should be equal to the base current multiplied by a constant gain β. But, as we have seen above, each p-n junction has two depletion layers. For the collector-base junction, one depletion layer extends into the collector, the other into the base. The base is almost always more heavily doped than the collector, so its depletion layer is fairly shallow. However, the base is also very thin, so even a shallow depletion layer takes up a significant portion of the base width. As the collector voltage increases, the depletion layers widen. In the collector region this has little effect (as long as it doesn't hit the other side of the collector), but in the base region it narrows the base-width. Since the gain of a bipolar transistor is very much dependent on the base-width, the gain simply increases as the effective base-width decreases. If you draw a straight line, extending the slope in the forward active region (from 0.4 to 15 Volts for example) into the negative quadrant and let it intersect with the zero-current line, you get the Early Voltage V\ :sub:`A`. In the exaggerated case shown in figure 8.4.2 the Early voltage would be -15 Volts (but is generally expressed as 15V). Depending on the base-width designed into the manufacturing process it can be more or less than that shown with the slope correspondingly shallower or steeper.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f12.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8.4.2 Early Voltage


8.5 Metal-Oxide-Semi-conductor Field-Effect Transistor basics
-------------------------------------------------------------

8.5.1 Basic Structure and Principle of Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The n-type Metal-Oxide-Semiconductor Field-Effect-Transistor (MOSFET) consists of a source and a drain, two highly conducting n-type semiconductor regions which are isolated from the p-type substrate by reversed-biased PN diodes. A poly-crystalline silicon gate covers the region between source and drain, but is separated from the semiconductor by an insulating layer of oxide. The basic structure of an n-type MOSFET and the corresponding circuit symbol are shown in figure 8.5.1.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f13.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8.5.1 Cross section and circuit symbol of an n-type Metal-Oxide-Semiconductor-Field-Effect-Transistor (MOSFET)


As can be seen in the figure the source and drain regions are identical. It is the applied voltages which determine which n-type region provides the electrons and becomes the source, while the other n-type region collects the electrons and becomes the drain. The voltages applied to the drain and gate electrode as well as to the substrate by means of a back contact are referred to the source potential, as also indicated on the figure.

A top view of the same MOSFET is shown in figure. 8.5.2, where the gate length, L, and gate width, W, are identified. Note that the gate length does not equal the physical dimension of the gate, but rather the distance between the source and drain regions underneath the gate. The overlap between the gate and the source and drain region is required to ensure that the inversion layer forms a continuous conducting path between the source and drain region. Typically this overlap is made as small as possible in order to minimize its parasitic capacitance.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f14.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 8.5.2 Top view of an n-type Metal-Oxide-Semiconductor- Field-Effect-Transistor (MOSFET)


The flow of electrons from the source to the drain is controlled by the voltage applied to the gate. A positive voltage applied to the gate, attracts electrons to the interface between the gate dielectric and the semiconductor. These electrons form a conducting channel between the source and the drain, called the inversion layer. No gate current is required to maintain the inversion layer at the interface since the gate oxide blocks any carrier flow. The net result is that the current between drain and source is controlled by the voltage which is applied to the gate.

The typical current versus voltage (I-V) characteristics of a MOSFET are shown in the figure below. Implemented is the quadratic model for the MOSFET.

8.6 MOS FET Large signal model
------------------------------

8.6.1 Modes of operation
~~~~~~~~~~~~~~~~~~~~~~~~

The operation of a MOSFET can be separated into three different modes, depending on the voltages at the terminals. In the following discussion, a simplified algebraic model is used that is accurate only for old technology. Modern MOSFET characteristics require computer models that have rather more complex behavior.

For an enhancement\ **-**\ mode*\*, **n-channel** \**MOSFET, the three operational modes are:

| Cutoff, subthreshold, or weak-inversion mode
| When :math:`V_GS < V_th` :
| Where V\ :sub:`th` is the threshold voltage of the device.

According to the basic threshold model, the transistor is turned off, and there is no conduction between drain and source. In reality, the Boltzmann distribution of electron energies allows some of the more energetic electrons at the source to enter the channel and flow to the drain, resulting in a subthreshold current that is an exponential function of gate-source voltage. While the current between drain and source should ideally be zero when the transistor is being used as a turned-off switch, there is a weak-inversion current, sometimes called subthreshold leakage. In weak inversion the current varies exponentially with gate-to-source bias V\ :sub:`GS` as given approximately by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e6.png
   :align: center
   :width: 200px

| Where:
| I\ :sub:`D0` = current at V\ :sub:`GS` = V\ :sub:`th`

and the slope factor *n* is given by

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e7.png
   :align: center
   :width: 170px

With:

C\ :sub:`D` = capacitance of the depletion layer

And

C\ :sub:`OX` = capacitance of the oxide layer.

In a long-channel device, there is no drain voltage dependence of the current once V\ :sub:`DS` >> V\ :sub:`T`, but as channel length is reduced drain-induced barrier lowering introduces drain voltage dependence that depends in a complex way upon the device geometry (for example, the channel doping, the junction doping and so on). Frequently, threshold voltage V\ :sub:`th` for this mode is defined as the gate voltage at which a selected value of current I\ :sub:`D0` occurs, for example, I\ :sub:`D0` = 1 µA, which may not be the same V\ :sub:`th`-value used in the equations for the following modes.

Some micropower analog circuits are designed to take advantage of subthreshold conduction. By working in the weak-inversion region, the MOSFETs in these circuits deliver the highest possible transconductance-to-current ratio, namely:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e8.png
   :align: center
   :width: 150px

Which is almost the same as a bipolar transistor.

The subthreshold I-V curve depends exponentially upon threshold voltage, introducing a strong dependence on any manufacturing variation that affects threshold voltage; for example: variations in oxide thickness, junction depth, or body doping that change the degree of drain-induced barrier lowering. The resulting sensitivity to fabrication variations complicates optimization for leakage and performance.

Triode mode or linear region (also known as the resistive mode)

When

:math:`V_GS > V_th`

and

:math:`V_DS < ( V_GS - V_th )`

The transistor is turned on, and a channel has been created which allows current to flow between the drain and the source. The MOSFET operates like a resistor, controlled by the gate voltage relative to both the source and drain voltages. The current from drain to source is modeled as:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e9.png
   :align: center
   :width: 300px

| Where:
| μ\ :sub:`n` is the charge-carrier effective mobility,
| W is the gate width,
| L is the gate length
| C\ :sub:`ox` is the gate oxide capacitance per unit area.

The transition from the exponential subthreshold region to the triode region is not as sharp as the equations suggest.

Saturation or active mode,

When

:math:`V_GS > V_th`

and

:math:`V_DS > ( V_GS - V_th )`

The switch is turned on, and a channel has been created, which allows current to flow between the drain and source. Since the drain voltage is higher than the gate voltage, the electrons spread out, and conduction is not through a narrow channel but through a broader, two- or three-dimensional current distribution extending away from the interface and deeper in the substrate. The onset of this region is also known as **pinch-**\ off to indicate the lack of channel region near the drain. The drain current is now weakly dependent upon drain voltage and controlled primarily by the gate-source voltage, and modeled very approximately as:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e10.png
   :align: center
   :width: 300px

The additional factor involving λ, the channel-length modulation parameter, models current dependence on drain voltage due to the Early effect, or channel length modulation. According to this equation, a key design parameter, the MOSFET transconductance is:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e11.png
   :align: center
   :width: 300px

The combination :math:`V_ov = V_GS - V_th` is called the overdrive voltage. Another key design parameter is the MOSFET output resistance r\ :sub:`O`\ given by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e12.png
   :align: center
   :width: 150px

r\ :sub:`out` is the inverse of g\ :sub:`ds` where

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e13.png
   :align: center
   :width: 150px

V\ :sub:`DS` is the expression in saturation region.

If ? is taken as zero, an infinite output resistance of the device results that leads to unrealistic circuit predictions, particularly in analog circuits. As the channel length becomes very short, these equations become quite inaccurate. New physical effects arise. For example, carrier transport in the active mode may become limited by velocity saturation. When velocity saturation dominates, the saturation drain current is more nearly linear than quadratic in V\ :sub:`GS`. At even shorter lengths, carriers transport with near zero scattering, known as quasi-ballistic transport. In addition, the output current is affected by drain-induced barrier lowering of the threshold voltage.

8.7 Small Signal Hybrid-pi models
---------------------------------

The hybrid-pi model is a popular circuit model used for analyzing the small signal behavior of bipolar junction and field effect transistors. The model can be quite accurate for low-frequency circuits and can easily be adapted for higher frequency circuits with the addition of appropriate inter-electrode capacitances and other parasitic elements.

8.7.1 Bipolar junction (BJT) parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The hybrid-pi model is a linearized two-port network approximation to the BJT using the small-signal base-emitter voltage v\ :sub:`be` and collector-emitter voltage v\ :sub:`ce` as independent variables, and the small-signal base current i\ :sub:`b` and collector current i\ :sub:`c` as dependent variables. A basic, low-frequency hybrid-pi model for the bipolar transistor (NPN) is shown in figure 8.7.1.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f15.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8.7.1 BJT Hybrid-pi Model


The various parameters are as follows:

The transconductance, g\ :sub:`m`, in siemens, is given by the following equation,

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e14.png
   :align: center
   :width: 100px

| where:
| //I\ :sub:`C` // is the quiescent collector current (also called the collector bias or DC collector current) |image4| is the thermal voltage, calculated from Boltzmann's constant *k*, the charge of an electron *q*, and the transistor temperature in kelvins, *T*. At 300 K (approximately room temperature) *V\ T* is about 26 mV.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e16.png
   :align: center
   :width: 175px

| where:
| |image5| is the current gain at low frequencies (also referred to as *h\ FE*).

Here *I\ B* is the quiescent point base current. This is a parameter specific to each transistor, and can be found on a datasheet; ß is a function of the choice of collector current.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr-e18.png
   :align: center
   :width: 200px

Is the output resistance due to the Early effect (*V\ A* is the Early voltage).

Related terms:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e19.png
   :align: center
   :width: 100px

The reciprocal of the output resistance is named the output conductance.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e20.png
   :align: center
   :width: 100px

The reciprocal of g\ :sub:`m` is called the intrinsic resistance *r\ E*

8.7.2 MOSFET parameters
~~~~~~~~~~~~~~~~~~~~~~~

A basic, low-frequency hybrid-pi model for the MOSFET (n-type) is shown in figure 8.7.2.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f16.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8.7.2 MOSFET Hybrid-pi Model


The various parameters are as follows:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e21.png
   :align: center
   :width: 200px

gm is the transconductance in siemens, evaluated in terms of the drain current *I\ D.* where:

*I\ D* is the quiescent drain current (also called the drain bias or DC drain current) *V\ th* = threshold voltage and *V\ GS* = gate-to-source voltage.

The combination: |image6| often is called the overdrive voltage.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e23.png
   :align: center
   :width: 250px

r\ :sub:`o` is the output resistance due to channel length modulation, using the approximation for the channel length modulation parameter λ.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e24.png
   :align: center
   :width: 100px

Here *V\ E* is a technology-related parameter (about 4 V/µm for the 65 nm technology node) and L is the length of the source-to-drain separation.

The reciprocal of the output resistance is named the drain conductance

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e25.png
   :align: center
   :width: 100px

8.8 The T Model
---------------

The hybrid-pi model is definitely the most popular small-signal model for the BJT and MOS transistors. The alternative is the T model, which is useful in certain situations. The T model also has two versions:

The small-signal T models for PNP BJTs and PMOS are identically the same as those shown here for the NPN transistors and NMOS. It is important to note that there is no change in any polarities (voltage or current) for the p-type models relative to the n-type models. Again, these small-signal models are identically the same. The model can be quite accurate for low-frequency circuits and can easily be adapted for higher frequency circuits with the addition of appropriate inter-electrode capacitances and other parasitic elements.

A basic, low-frequency T model for the MOSFET and BJT is shown in figure 8.8.1.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-f17.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8.8.1 MOSFET and BJT T Model


Some important MOS equations.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e25.png
   :align: center
   :width: 100px

Some important BJT equations.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e26.png
   :align: center
   :width: 500px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e27.jpg
   :align: center
   :width: 200px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e28.jpg
   :align: center
   :width: 200px

Lab Activities
--------------

| **ADALM1000 Lab Activity 3,** :doc:`BJT as a diode </wiki-migration/university/courses/alm1k/alm-lab-3>`
| **ADALM1000 Lab Activity 4,** :doc:`BJT I/V curves </wiki-migration/university/courses/alm1k/alm-lab-4>`

| **ADALM1000 Lab Activity 3M,** :doc:`MOS as a diode </wiki-migration/university/courses/alm1k/alm-lab-3m>`
| **ADALM1000 Lab Activity 4M,** :doc:`MOS I/V curves </wiki-migration/university/courses/alm1k/alm-lab-4m>`

**Return to** :doc:`Previous Chapter </wiki-migration/university/courses/electronics/text/chapter-7>`

**Go to** :doc:`Next Chapter </wiki-migration/university/courses/electronics/text/chapter-9>`

**Return to** :doc:`Table of Contents </wiki-migration/university/courses/electronics/text/electronics-toc>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e3.png
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e4.png
   :width: 100px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e5.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e15.png
   :width: 100px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e17.png
   :width: 100px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr8-e22.png
   :width: 200px
