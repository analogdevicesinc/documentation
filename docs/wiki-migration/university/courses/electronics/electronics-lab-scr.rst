Activity: Silicon Controlled Rectifiers (SCR) - ADALM2000
=========================================================

Objective:
----------

The objective of this Lab activity is to examine the structure and operation of the Silicon Controlled Rectifier or SCR. SCRs are mainly used in devices where the control of high power, possibly at high voltage, is needed. The ability to switch large currents on and off makes the SCR suitable for use in medium to high-voltage AC power control applications, such as lamp dimming, regulators and motor control. In addition, unintentional SCRs can form in integrated circuits and when these SCRs get triggered circuit malfunction or even reliability problems and damage can result.

Background:
-----------

A silicon controlled rectifier (SCR) is a four-layer solid state current controlling device with 3 terminals. They have anode and cathode terminals like a conventional diode and a third control terminal, referred to as the Gate. SCRs are unidirectional devices, i.e. they conduct current only in one direction like a diode or rectifier. SCRs are triggered only by currents going into the gate. The SCR combines the rectifying features of diodes and the On - Off control features of transistors.

SCRs are generally used in power switching applications. In the normal OFF state, the device restricts current flow to the leakage current. When the gate-to-cathode current exceeds a certain threshold, the device turns ON and conducts current. The SCR will remain in the ON state even after gate current is removed so long as the current through the device exceeds the holding current. Once the current falls below the holding current for a period of time, the device will switch OFF. If the gate is pulsed and the current through the device is below the latching current, the device will remain in the OFF state.

Looking at figure 1(a), the four layer structure of the SCR, we see the three terminals, one from the outer p-type layer called the anode A, the second from the outer n-type layer called the cathode K and the third from the base of the lower NPN transistor section and is called gate G.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/ascr_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1 SCR Equivalent Circuit


The SCR, as shown in figure 1(b), can be visualized as separated into two transistors. The equivalent circuit of an SCR is composed of a PNP transistor and an NPN transistor interconnected as shown in figure 1c. We see that the collector of each transistor is connected to the base of the other, forming a positive feedback loop.

The SCR has two stable states. The first is the non-conducting OFF state. With the Gate terminal open let us first assume that no current is flowing into the base terminal of NPN transistor Q\ :sub:`2`. Given zero base current the collector current of Q\ :sub:`2` will also be zero. Given zero collector for Q\ :sub:`2` we infer that there should be zero current flowing out of the base of PNP transistor Q\ :sub:`1`. Given zero base current in Q\ :sub:`1` we infer that there should be zero collector current in Q\ :sub:`1`. This is consistent with our original assumption of zero current in the base of Q\ :sub:`2`. With zero collector current ( and zero base current ) in both Q\ :sub:`1` and Q\ :sub:`2` we can infer that there should be no emitter current in either transistor as well. This zero current OFF state is stable so long as any leakage current through Q\ :sub:`1` or Q\ :sub:`2` from emitter to collector is very small.

The second stable state is the conducting ON state. We can transition or switch the SCR from the OFF state to the ON state by injecting a small current into the Gate terminal. Going through the same procedure around the loop we just did for the off state we can see that as soon as a base current is supplied to Q\ :sub:`2`, a larger collector current ( ß\ :sub:`NPN` times the base current ) will start to flow. This Q\ :sub:`2` collector current becomes base current for Q\ :sub:`1`. This base current in Q\ :sub:`1` produces again a larger collector current ( ß\ :sub:`PNP` times the base current ) in Q\ :sub:`1`. The collector current of Q\ :sub:`1` feeds back into the base of Q\ :sub:`2` increasing its base current even more. Once this feedback loop of current is established the initial gate current can be removed and the SCR will remain in the conducting ON state for as long as the external circuit around the SCR supplies current through the SCR. The only way to turn off the SCR is for the current to drop below a critical "holding" current level.

An observation to note about this positive feedback loop is that it will hold the SCR ON and remain in this latched state as long as the following is true:

ß\ :sub:`PNP` \* ß\ :sub:`NPN` => 1

The voltage drop across the SCR from terminal A to K when the SCR is conducting is the sum of Q\ :sub:`1VBE` and Q\ :sub:`2VCESAT` in parallel with the sum of Q\ :sub:`2VBE` and Q\ :sub:`1VCESAT` . We know that the ß of BJT devices falls as the collector base junction is forward biased into the saturation region i.e V\ :sub:`CE` less than V\ :sub:`BE`. The V\ :sub:`CE` of the two transistors will drop until the above positive feedback gain equation is satisfied and ß\ :sub:`PNP` \* ß\ :sub:`NPN` is equal to 1.

It is also important to note that the ß of BJT transistors is very low for very small values of collector current and from the above equation, the SCR will remain in the OFF state so long as the leakage current is so small that ß\ :sub:`PNP` \* ß\ :sub:`NPN` is less than 1 at this low leakage current level.

The ADALP2000 Analog Parts Kit does not include an SCR but we can emulate one by building the equivalent circuit shown in figure 1(c) from discrete PNP and NPN transistors.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less Breadboard
| 2 - 1 KΩ Resistors
| 2 - 100 KΩ Resistors
| 1 - 0.1 uF capacitor (marked 104)
| 1 - small signal NPN transistor (2N3904)
| 1 - small signal PNP transistor (2N3906)

Directions:
-----------

Build the model of the equivalent circuit of an SCR as shown in figure 2 on your solder-less breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/ascr_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 Circuit to emulate an SCR


The two 100 KΩ resistors, R\ :sub:`1`, R\ :sub:`2`, are placed across the respective V\ :sub:`BE` of each transistor to insure that any small leakage currents do not self trigger the simulated SCR. Resistor R\ :sub:`3` converts the voltage pulse from AWG2 into a triggering current.

Hardware Setup:
---------------

AWG1 should be configured as a sine wave with an amplitude of 10 V peak-to-peak, zero offset and a frequency of 100 Hz. AWG2 should be configured as a square wave with an amplitude of 800 mV peak-to-peak, 400 mV offset, a frequency of 100 Hz. Be sure to run the two AWG channels synchronously.


|image1|

.. container:: centeralign

   Figure 3 Breadboard connections of Circuit to emulate an SCR


Procedure:
----------

Trigger the scope on channel 1. While observing the input sine wave on scope channel 1 and the voltage across R\ :sub:`L` on scope channel 2, adjust the phase of AWG2 in steps from 180º to 360º. Depending on the phase setting of AWG2 you should see something that looks similar to the figures below. You will notice that the voltage across R\ :sub:`L` is zero, SCR in OFF state, until the trigger pulse from AWG2 occurs and the SCR remains in the ON state until the input sine wave voltage crosses zero.


|image2|

.. container:: centeralign

   Figure 4 Example waveforms


.. image:: https://wiki.analog.com/_media/university/courses/electronics/ascr_f3a.png
   :align: center

.. container:: centeralign

   Figure 5 Example Scopy waveforms


Measure and report the voltage drop across the SCR when it is in the ON state and conducting current. How does this voltage compare to a conventional PN junction diode?

Find the minimum pulse voltage ( amplitude ) above ground that will trigger the SCR by adjusting AWG2. Estimate the minimum trigger current based on this voltage, R\ :sub:`3` and the V\ :sub:`BE` of Q\ :sub:`2`. Explain your result.

Try larger ( 1 MΩ ) and smaller ( 10KΩ ) values for R\ :sub:`1` and R\ :sub:`2`. How does this change the minimum trigger voltage?

Replace resistor R\ :sub:`3` with a 0.1uF capacitor. This coupling capacitor acts as a differentiator turning the square pulse of the AWG output into narrow positive and negative spikes of current on the rising and falling edges of the square wave. How does this effect when and how the SCR is triggered?

Questions:
----------

-   How does the SCR differ from an ordinary rectifier diode?
-   Draw the V-I characteristics of an SCR. What can you infer from them?
-   Why is an SCR always turned on by a current into the gate?
-   Why can't the SCR be used as a bidirectional current switch?
-   How does an SCR control the power delivered to the load?
-   Why are SCRs mostly used in AC circuits?

If a source of smaller ( low current ) SCRs is available, you could repeat the experiment with an actual device rather than our equivalent circuit emulation.

Unintentional parasitic SCRs in Integrated circuits
---------------------------------------------------

We have explored applications for the SCR that intentionally make use of its characteristics. Unfortunately, unintentional SCRs can form in integrated circuits and if these parasitic SCRs get triggered circuit malfunction can result or even reliability issues and damage to the integrated circuit.

LATCH-UP
~~~~~~~~

Latch-up is a potentially destructive situation in which a parasitic SCR is triggered, shorting the positive and negative supplies together. If current flow is not limited, electrical over-stress will occur. The classic case of latch-up occurs in CMOS output devices, in which the driver transistors and wells form a four layer PNPN SCR structure when one of the two parasitic base-emitter junctions is momentarily forward biased during an over-voltage upset event. The SCR turns on and essentially causes a short between the V\ :sub:`DD` power supply and ground.

Since all these MOS devices are located close together on the monolithic die, with appropriate external excitation, the parasitic SCR devices may turn on, a behavior common with poorly designed CMOS circuits. Figure 4 illustrates a simplified cross section showing two transistors, one PMOS and one NMOS; these could be connected together as logic gates or as an analog amplifier or switch. The parasitic bipolar transistors responsible for latch-up behavior, Q\ :sub:`1` (vertical PNP) and Q\ :sub:`2` (lateral NPN) are as indicated.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/ascr_f4.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 6 Cross-section of PMOS and NMOS devices, with parasitic transistors Q\ :sub:`1` and Q\ :sub:`2`


Proper design methods to reduce the possibility of SCR formation include increasing the spacing between NMOS and PMOS devices and interposing highly doped regions between and around Nwells and Pwells. Both of these kinds of layout approaches attempt to lower the ß of either the vertical PNP or the lateral NPN parasitic bipolar transistors to less than 1. Some of these methods also tend to lower the resistance of R\ :sub:`PWELL` and R\ :sub:`NWELL` which increases the minimum trigger current needed to turn on the SCR.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/silicon_ctrl_rectifier_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/silicon_ctrl_rectifier_ltspice`
   


The Programmable UJT (PUT)
--------------------------

The Programmable unijunction transistor or PUT is a close relative of other four layer devices in the thyristor family. Its has a four layered construction just like the SCR and has three terminals named anode(A), cathode(K) and gate(G) again like the thyristors. Background and example circuits that use the PUT can be found in this :doc:`ADALM1000 Lab Activity </wiki-migration/university/courses/alm1k/alm-lab-scr>`.

**For Further Reading:**

| `The Silicon Controlled Rectifier <http://en.wikipedia.org/wiki/Silicon-controlled_rectifier>`__
| :adi:`Electrically Induced Damage to Standard Linear Integrated Circuits <static/imported-files/application_notes/AN-397.pdf>`
| :adi:`Winning the Battle Against Latch-up in CMOS Analog Switches <library/analogDialogue/archives/35-05/latchup/latchup.pdf>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/ascr_bb.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/ascr_f3.png
   :width: 500px
