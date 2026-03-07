Activity: Switched Capacitor Power Supplies
===========================================

Objective:
----------

The objective of this activity is to understand the operation of several switched-capacitor power conversion circuits.

Background:
-----------

A high quality power supply is essential for nearly any electronic circuit. If you have never had a circuit fail because of a power integrity issue, it is likely because you are starting with a high-quality power supply. But what if the only supply you have available is nominally the correct voltage, but varies over time or temperature - your 9V-battery powered op-amp circuit may work fine when you first power it up, but begin to fail in new and interesting ways as the battery voltage drifts down to 8V, 7V, 6V, 5V, etc. This particular situation can be remedied with a linear voltage regulator, supplied with a voltage higher than the regulated output voltage. An LM7805 will provide a stable, 5V source when powered from a 9V battery. This is done by adjusting the drive to a power transistor, such that the voltage drop across the transistor results in the correct output voltage.

Linear regulators have widespread application and are well deserving of their own activity, but there are some things that a linear regulator just can't do:

-  "Boost" a lower voltage to a higher voltage
-  "Invert" a positive voltage to a negative voltage
-  Reduce a high voltage to a lower voltage any more efficiently than could be achieved with a power resistor in series with the supply, at an equivalent output current.

This is where other techniques must be employed. One such technique is "switched-capacitor" voltage conversion, and conceptually involves little more than capacitors, switches, and some form of control to the switches.

Side note - A quick survey of switching regulators will reveal that the vast majority involve inductors, rather than capacitors. There are reasons for this, but for understanding power conversion, there is merit to starting with capacitors. Capacitors are easier for many students to grasp (literally), at least in terms of energy storage. A large capacitor charged from a battery stores the energy as a static electric charge. You can disconnect the battery, and hold the stored energy in your hand for a "human perceptible" amount of time - seconds, minutes, even hours or days. This is generally not possible with inductors (unless they are superconducting) - they store energy in a field induced by a moving current. One could attempt to quickly switch out a battery from an inductor, and short the inductor such that the current continues to circulate, but the current will rapidly decrease to zero (for any inductor that you could hold in your hand, anyway.)

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| PC running LTspice and Scopy
| LT1054 Switched-Capacitor Voltage Converter
| Electrolytic capacitors from ADALP2000 parts kit
| Solderless breadboard
| 5V USB power supply
| Voltmeter (optional, can use M2K in Voltmeter mode.)
| LTspice files for this activity: `switch_cap_ltspice_files.zip <https://wiki.analog.com/_media/university/courses/electronics/sw_cap/switch_cap_ltspice_files.zip>`_

Activity 0: Human-switched capacitor power conversion
=====================================================

The introduction alluded to being able to hold a capacitor with stored energy in your hands. Let's do a quick experiment and make a human-switched-capacitor voltage inverter.

Say you have a 9V battery, and you want to make a split +/-9V supply. Charge the 220uF cap from the parts kit by holding it to the terminals of a 9V battery (OBSERVE PROPER POLARITY!), then connect cap (+) to battery (-), measuring from battery (-) to cap (-). |image1|


|image2|

.. container:: centeralign

   Figure 1. Human switched-cap inverter


This "flips" the positive voltage across the capacitor below ground, and you now have a split supply... until the capacitor discharges, either through your circuit, or through internal leakage.

Similarly, if you have a 9V battery need a higher voltage, say 18V, you can charge the capacitor again, then connect capacitor (-) to battery (+). This "stacks" the positive voltage across the capacitor on top of the battery's own 9V, producing 18V... until the capacitor discharges, either through your circuit, or through internal leakage.

|image3| |image4|

.. container:: centeralign

   Figure 2. Human switched-cap doubler


If you do this fast enough, your circuit won't notice the switching and will see a continuous, steady voltage, but it would quickly get tiring for the human switcher.

With a basic idea of switched capacitors, let's proceed to something more practical.

Activity 1: Switched Capacitor Voltage Inverter
===============================================

Theory and Simulation
---------------------

Some op-amp circuits can operate on a single supply, with the op-amp negative supply pin connected to ground. However there are applications that benefit from the use of a "split" supply with voltages of opposite polarity referred to circuit ground, for example, with the op-amp's supply pins connected to positive 5V and negative 5V. Such a supply can be created by using two 9-V batteries, an LM7805 positive regulator, and an LM7905 negative regulator. But this extra battery is an inconvenience - when is the last time you saw a product that required TWO 9V batteries?

This is where a switched-capacitor inverter can come in handy - A single battery can now provide both a positive supply (direct connection to the positive terminal), and a negative supply (through an inversion circuit.) Before testing real circuits, let's get a feel for how the circuit works by runnign an idealized simulation. This simulation essentially automates the procedure from Experiment 0.

Open the *switch_cap_inverter.asc* schematic from the zip file in LTspice.

The key element in this simulation is a switch:


|image5|

.. container:: centeralign

   Figure 3. LTspice switch


which is assigned a value of **my_sw**. Any switch in the schematic with value **my_sw** will have properties defined by the spice directive:

.model my_sw sw(Vt= 0.5 Vh=-.25 Ron=0.01 Roff=100Meg)

Which says:

-  When the ( + ) input is greater than the ( - ) input by more than 0.5V, the switch resistance is 0.01 ohms
-  When the ( + ) input is not greater than the ( - ) input by more than 0.5V, the switch resistance is 100 million ohms

**Why not zero ohms and infinity ohms?** *SPICE can get confused when the range of values in a simulation covers too great a range. In this simulation, we're charging and discharging capacitors, and without some simulated resistance, currents will approach infinity. The Vh parameter is the hysteresis at the input, which ensures that the switch changes state properly.*

The 0.5V threshold was chosen so that the switch can be controlled by an intuitive voltage level, where 0V = OFF and 1V = ON.

The switches are controlled by two pulse generators, with outputs labeled **clk** and **clk_bar**.


|image6|

.. container:: centeralign

   Figure 4. Clock Sources


Right-clicking will bring up the parameter windows:



|image7|

.. container:: centeralign

   Figure 5. clk Parameters


   |image8|

.. container:: centeralign

   Figure 6. clk_bar Parameters


Each source outputs 3 microsecond pulses with a 10 microsecond period. The only difference is that V3 is delayed by 5us - this produces a "non-overlapping clock", which allows switches to be alternately turned on and off, and never on at the same instant. Running the simulation, and probing clk and clk_bar, shows what's going on:



|image9|

.. container:: centeralign

   Figure 7. Non-overlapping Clock Waveforms


The last step in making the idealized simulation is to put the pieces together, to do what human hands did in experiment zero. When **clk** is asserted (at 1V, closing S1 and S2), the capacitor is charged to +5V:



|image10|

.. container:: centeralign

   Figure 8. Inverter Phase 0


When **clk_bar** is asserted, the left terminal of C1 that was charged to 5V is then grounded (to zero volts), which drives the right terminal negative:



|image11|

.. container:: centeralign

   Figure 9. Inverter Phase 1


Run the simulation, and probe **vout**, **clk**, and **clk_bar**.



|image12|

.. container:: centeralign

   Figure 10. Inverter Startup Waveforms


Notice that the output voltage does not immediatly reach its final value, but takes several "steps." This is because while C1 is initially charged to 5V, C2 is initially discharged. Thus the charges in each capacitor are:

q(C1) = 5V \* 1uF = 5uc

q(c2) = 0V \* 1uF = 0uc

When S3 and S4 close, C1 and C2 are placed in parallel, so the 5uc is then divided among two 1uF capacitors, resulting in a voltage of -2.5V. Subsequent charge / discharge cycles drive the output voltage closer to its final value of nearly -5V. The 1k load resistor prevents the output from ever reaching exactly -5V, but if the switching is fast enough, it can come close.

Circuit Construction and Testing
--------------------------------

With the simulation understood, let's move on to actual components. Open the *LT1054_inverter.asc* schematic from the zip file in LTspice. Construct the circuit on a breadboard, following the LTspice schematic.


|image13|

.. container:: centeralign

   Figure 11. Inverter Breadboard circuit


Build the following breadboard circuit for the voltage inverter.



|image14|

.. container:: centeralign

   Figure 12. Inverter Breadboard circuit


The circuit can also be soldered on a "Perma Proto" solderable breadboard from Adafruit, which matches the layout of typical solderless breadboards.



|image15|

.. container:: centeralign

   Figure 13. Inverter Circuit Soldered on PermaProto board


Connect a voltmeter (or M2K in voltmeter mode) between circuit ground and the OUT pin of the LT1054, and Apply 5V to the IN pin. The voltmeter should read close to -5V.

Next, let's take a look at what the circuit is actually doing. Make the following connections from the ADALM2000 (M2K) to the circuit:

-  M2K GND to Circuit Ground (there are four GND pins, choose one.)
-  M2K CH1-, CH2- to Circuit Ground
-  M2K CH1+ to LT1054 pin 5
-  M2K CN2+ to LT1054 pin 4

Set Scopy to Oscilloscope mode, with the following settings:

-  Timebase: 250us/div
-  CH1, CH2: 1V/div
-  Triggering: Ch1, -1V, Falling Edge, Single Shot mode.

Momentarily short LT1054 pin 1 (FB) to ground. This disables the LT1054. Release FB; this allows the LT1054 to operate again, and produces a "clean" turn-on transient. You should see a waveform similar to the figure below:


|image16|

.. container:: centeralign

   Figure 14. LT1054 Inverter Startup Scopy Measurement


Run the LTspice simulation, and probe the corresponding nodes. You should see results similar to the figure below:



|image17|

.. container:: centeralign

   Figure 15. LT1054 Inverter Startup LTspice Simulation


This shows reasonable correlation between the simulation and actual measurements. This is a good thing, but it's always important to keep in mind that:

-  No simulation is perfect, ever
-  No measurement is perfect, ever

Much of electrical engineering involves putting bounds on **HOW** imperfect your simulation is, and **HOW** imperfect your measurements are. In this case, the circuit is fairly simple, and it is operating at a fairly low frequency of 25kHz (just above the audio range.) The M2K is more than adequate, so we can have some confidence in its measurements.

There is another benefit of running simulations - you can probe more points than you might be able to with your actual test equipment, and you can probe parameters that are otherwise difficult or impossible to measure directly. One example in the LT1054 inverter circuit is the displacement current in the "flying" capacitor (C2). If one side of the capacitor was connected to ground, you might be able to insert a small resistor, and calculate the current from the measured voltage (a common technique.) But both sides of C2 are driven, so the only real way to measure this current is with a current probe, which not every lab is equipped with. But we have shown reasonable correlation between LTspice's voltage mesurements and measurements taken on the actual circuit, so we can assume with some confidence that other measurements will correlate. The current through C2 is plotted below:


|image18|

.. container:: centeralign

   Figure 16. LT1054 Inverter Startup Simulation w/ Capacitor Current


If you built this circuit up on a PermaProto board, you can put it in a box and use it with your next project that requires a split (positive and negative) power supply.

*Be sure to read the pin description for Vout in the LT1054 datasheet!*

Questions:
----------

It was mentioned above that "if the switching is fast enough, the output can come close (to -5V)." How close? Activity 19 derives an expression for the equivalent resistance of a switched-capacitor circuit, and the same analysis can be applied to the switched-capacitor inverter. The LTspice simulation of the (close to) ideal inverter switches a 1uF capacitor at 100kHz. What is the equivalent resistance at the output? This resistance represents a theoretical limit to the power supply's load regulation performance. Try increasing the size of the output capacitor to "smooth out" the ripple due to individual switching events, and decrease the value of the load resistor such that the output voltage is decreased by 10% (to -4.5V.) The LT1054 has additional losses due to voltage drops across the switching transistors; this is discussed in detail in the datasheet.

Activity 2: Charge Pump Voltage Doubler
=======================================

.. _theory-and-simulation-1:

Theory and Simulation
---------------------

Another useful power conversion function is producing a high voltage from a lower voltage, which was demonstrated in the second half of Experiment 0. The LT1054 switches are not configured in a way that will perform this function directly, but we can use the LT1054 to drive a "charge pump" to double the input voltage. Once again, let's start with a close to ideal simulation to illustrate the idea. Open the *switch_cap_pump_doubler.asc* schematic from the zip file in LTspice.

This circuit borrows the nonoverlapping clocks from the inverter simulation. The two states are easy to visualize:

**clk** asserts, turning S4 on, pulling the lower terminal of C1 to ground. D2 conducts, charging C1 to Vusb (minus a diode drop.)


|image19|

.. container:: centeralign

   Figure 17. Doubler Phase 0


**clk_bar** asserts, turning on S1. The lower terminal of C1 is driven to Vusb, and the Pump node is driven to Vusb plus another Vusb (minus a diode drop.)



|image20|

.. container:: centeralign

   Figure 18. Doubler Phase 1


The result is that Vout is "pumped" to 2X Vusb, minus two diode drops. Probing Vout and Pump confirms this:



|image21|

.. container:: centeralign

   Figure 19. Doubler Startup LTspice Simulation


As with the inverter circuit, the output takes several clock cycles to reach its final value due to charge sharing.

.. _circuit-construction-and-testing-1:

Circuit Construction and Testing
--------------------------------

With the simulation understood, let's move on to actual components. Construct the LT1054 doubler circuit, following the LTspice schematic *LT1054_doubler.asc* from the zip file.


|image22|

.. container:: centeralign

   Figure 20. Doubler Schematic


Build the following breadboard circuit for the voltage inverter.



|image23|

.. container:: centeralign

   Figure 21. Doubler Breadboard circuit


The circuit can also be soldered on a "Perma Proto" solderable breadboard from Adafruit, which matches the layout of typical solderless breadboards.



|image24|

.. container:: centeralign

   Figure 22. Doubler Circuit Soldered on PermaProto board


Connect a voltmeter (or M2K in voltmeter mode) between circuit ground and the OUT pin of the LT1054, and Apply 5V to the IN pin. The voltmeter should read close to +8.6V.

Next, let's take a look at what the circuit is actually doing. Make the following connections from the ADALM2000 (M2K) to the circuit:

-  M2K GND to Circuit Ground (there are four GND pins, choose one.)
-  M2K CH1-, CH2- to Circuit Ground
-  M2K CH1+ to OUT node
-  M2K Ch2+ to Pump node

Set Scopy to Oscilloscope mode, with the following settings:

-  Timebase: 250us/div
-  CH1, CH2: 1V/div
-  Triggering: Ch1, +5V, Rising Edge, Single Shot mode.

Momentarily short LT1054 pin 1 (FB) to ground. This disables the LT1054. Release FB; this allows the LT1054 to operate again, and produces a "clean" turn-on transient. You should see a waveform similar to the figure below:


|image25|

.. container:: centeralign

   Figure 23. LT1054 Doubler Startup Scopy Measurement


Run the LTspice simulation, and probe the corresponding nodes. You should see results similar to the figure below:



|image26|

.. container:: centeralign

   Figure 24. LT1054 Doubler Startup LTspice Simulation


*Note that there is a noticeable qualitative difference between the Scopy measurement and the LTspice simulation; the measured rampup appears more linear, while the LTspice rampup appears more exponential.*

TBD: Activity 3: Voltage Divider
================================

Experiment based on:

http://www.analog.com/media/en/technical-documentation/lt-journal-article/lt1054_0299_mag.pdf

Going Further: High-power switched capacitor circuits
=====================================================

Why are switched capacitor power circuits uncommon? High transient currents, EMI, etc. present challenges, but there are a number of practical, high-power switched-capacitor power converters. The LTC7820 is a fixed ratio high power charge pump controller - the evaluation board application circuit will halve the voltage of a 36V to 60V, at up to 10A (300W), at 99% efficiency.

.. _questions-1:

Questions:
----------

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/switch_cap_bb`
   -  LTSpice files: :git-education_tools:`switch_cap_ltspice <m2k/ltspice/switched_cap_ltspice>`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/human_inverter_phase_0.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/human_inverter_phase_1.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/human_doubler_phase_0.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/human_doubler_phase_1.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/switch.png
   :width: 200px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/clocks.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/clk_param_window_phase0.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/clk_param_window_phase1.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/nonoverlapping_clocks.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/switch_cap_inverter_phase_0.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/switch_cap_inverter_phase_1.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/switch_cap_inverter_waveforms.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/lt1054_inverter_schematic.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/lt1054_inverter_breadboard.png
.. |image15| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/lt1054_inverter.jpg
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/lt1054_inverter_turn_on_scopy.png
.. |image17| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/lt1054_inverter_turn_on_ltspice2.png
   :width: 600px
.. |image18| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/lt1054_inverter_turn_on_ltspice_w_cap_current.png
   :width: 600px
.. |image19| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/switch_cap_pump_doubler_phase_0.png
   :width: 500px
.. |image20| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/switch_cap_pump_doubler_phase_1.png
   :width: 500px
.. |image21| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/switch_cap_pump_doubler_waveforms.png
   :width: 600px
.. |image22| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/lt1054_doubler_schematic.png
   :width: 600px
.. |image23| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/lt1054_doubler_breadboard.png
.. |image24| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/lt1054_boost.jpg
   :width: 600px
.. |image25| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/lt1054_doubler_turn_on_scopy.png
.. |image26| image:: https://wiki.analog.com/_media/university/courses/electronics/sw_cap/lt1054_doubler_turn_on_ltspice.png
   :width: 600px
