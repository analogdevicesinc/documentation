Activity: Silicon Controlled Rectifiers (SCR) - ADALM1000
=========================================================

Objective:
----------

The objective of this Lab activity is to examine the structure and operation of the Silicon Controlled Rectifier or SCR. SCRs are mainly used in devices where the control of high power, possibly at high voltage, is needed. The ability to switch large currents on and off makes the SCR suitable for use in medium to high-voltage AC power control applications, such as lamp dimming, regulators and motor control. In addition, unintentional SCRs can form in integrated circuits and when these SCRs get triggered circuit malfunction or even reliability problems and damage can result.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H. In this Lab you will be using one of the channels of the ALM1000 in the split Input / Output mode. CB-Out is used to denote the connection to the Output pin and CB-In is used to denote the Input pin on the (expanded) 8 pin connector.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

A silicon controlled rectifier (SCR) is a four-layer solid state current controlling device with 3 terminals. They have anode and cathode terminals like a conventional diode and a third control terminal, referred to as the Gate. SCRs are unidirectional devices, i.e. they conduct current only in one direction like a diode or rectifier. SCRs are triggered only by currents going into the gate. The SCR combines the rectifying features of diodes and the On - Off control features of transistors.

SCRs are generally used in power switching applications. In the normal OFF state, the device restricts current flow to the leakage current. When the gate-to-cathode current exceeds a certain threshold, the device turns ON and conducts current. The SCR will remain in the ON state even after gate current is removed so long as the current through the device exceeds the holding current. Once the current falls below the holding current for a period of time, the device will switch OFF. If the gate is pulsed and the current through the device is below the latching current, the device will remain in the OFF state.

Looking at figure 1(a), the four layer structure of the SCR, we see the three terminals, one from the outer p-type layer called the anode A, the second from the outer n-type layer called the cathode K and the third from the base of the lower NPN transistor section and is called gate G.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-scr_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 SCR Equivalent Circuit


The SCR, as shown in figure 1(b), can be visualized as separated into two transistors. The equivalent circuit of an SCR is composed of a PNP transistor and an NPN transistor interconnected as shown in figure 1(c). We see that the collector of each transistor is connected to the base of the other, forming a positive feedback loop.

The SCR has two stable states. The first is the non-conducting OFF state. With the Gate terminal open let us first assume that no current is flowing into the base terminal of NPN transistor Q\ :sub:`2`. Given zero base current the collector current of Q\ :sub:`2` will also be zero. Given zero collector for Q\ :sub:`2` we infer that there should be zero current flowing out of the base of PNP transistor Q\ :sub:`1`. Given zero base current in Q\ :sub:`1` we infer that there should be zero collector current in Q\ :sub:`1`. This is consistent with our original assumption of zero current in the base of Q\ :sub:`2`. With zero collector current ( and zero base current ) in both Q\ :sub:`1` and Q\ :sub:`2` we can infer that there should be no emitter current in either transistor as well. This zero current OFF state is stable so long as any leakage current through Q\ :sub:`1` or Q\ :sub:`2` from emitter to collector is very small.

The second stable state is the conducting ON state. We can transition or switch the SCR from the OFF state to the ON state by injecting a small current into the Gate terminal. Going through the same procedure around the loop we just did for the off state we can see that as soon as a base current is supplied to Q\ :sub:`2`, a larger collector current ( ß\ :sub:`NPN` times the base current ) will start to flow. This Q\ :sub:`2` collector current becomes base current for Q\ :sub:`1`. This base current in Q\ :sub:`1` produces again a larger collector current ( ß\ :sub:`PNP` times the base current ) in Q\ :sub:`1`. The collector current of Q\ :sub:`1` feeds back into the base of Q\ :sub:`2` increasing its base current even more. Once this feedback loop of current is established the initial gate current can be removed and the SCR will remain in the conducting ON state for as long as the external circuit around the SCR supplies current through the SCR. The only way to turn off the SCR is for the current to drop below a critical "holding" current level.

An observation to note about this positive feedback loop is that it will hold the SCR ON and remain in this latched state as long as the following is true:

:math:`ß_PNP \times ß_NPN => 1`

The voltage drop across the SCR from terminal A to K when the SCR is conducting is the sum of Q\ :sub:`1VBE` and Q\ :sub:`2VCESAT` in parallel with the sum of Q\ :sub:`2VBE` and Q\ :sub:`1VCESAT` . We know that the ß of BJT devices falls as the collector base junction is forward biased into the saturation region i.e V\ :sub:`CE` less than V\ :sub:`BE`. The V\ :sub:`CE` of the two transistors will drop until the above positive feedback gain equation is satisfied and ß\ :sub:`PNP` \* ß\ :sub:`NPN` is equal to 1.

It is also important to note that the ß of BJT transistors is very low for very small values of collector current and from the above equation, the SCR will remain in the OFF state so long as the leakage current is so small that ß\ :sub:`PNP` \* ß\ :sub:`NPN` is less than 1 at this low leakage current level.

The Analog Parts Kit does not include an SCR but we can emulate one by building the equivalent circuit shown in figure 1(c) from discrete PNP and NPN transistors.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less Breadboard and jumper wire kit
| 1 - 1 KΩ Resistor
| 1 - 100 Ω Resistor
| 2 - 100 KΩ Resistors
| 1 - 0.1 uF capacitor (marked 104)
| 1 - small signal NPN transistor (2N3904)
| 1 - small signal PNP transistor (2N3906)

Directions:
~~~~~~~~~~~

Build the model of the equivalent circuit of an SCR as shown in figure 2 on your solder-less breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-scr_f2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2 Circuit to emulate an SCR


The two 100 K? resistors, R\ :sub:`1`, R\ :sub:`2`, are placed across the respective V\ :sub:`BE` of each transistor to insure that any small leakage currents do not self trigger the simulated SCR. Resistor R\ :sub:`3` converts the voltage pulse from channels B into a triggering current.

Hardware Setup:
~~~~~~~~~~~~~~~

The channel A voltage generator should be configured as a sine wave with a 0 V Min value and a 5 V Max value. Set a frequency of 100 Hz. Channel B should be configured in the Split I/O mode with the termination set to 2.5V. Shape is set as a square wave with a 0 mA Min value and a 16 mA Max value. Also set to a frequency of 100 Hz and a duty cycle of 10%.

Procedure:
~~~~~~~~~~

Select all four traces to be displayed, CA-V, CA-I, CB-V and CB-I. While observing the input sine wave on trace CA-V and the voltage across R\ :sub:`L` on trace CB-V, adjust the phase of the channel A sine wave in steps from 90º to 270º. Depending on the phase setting of the channel B square wave you should see something that looks similar to figure 3. The trigger pulse should happen at some time point when CV-A is above the 2.5 V level. You will notice that the voltage across R\ :sub:`L` is zero, SCR in OFF state, until the trigger pulse from the square wave occurs and the SCR remains in the ON state until the input sine wave voltage crosses zero (below the 2.5V level).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-scr_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3 Example waveforms


Measure and report the voltage drop across the SCR when it is in the ON state and conducting current. How does this voltage compare to a conventional PN junction diode? Find the minimum pulse voltage ( amplitude ) above 2.5 V that will trigger the SCR by adjusting the Max value of the channel B square wave. Explain your result? Try larger ( 1 MΩ ) and smaller ( 10KΩ ) values for R\ :sub:`1` and R\ :sub:`2`. How does this change the minimum trigger voltage?

Try reducing the width of the trigger pulse by changing the channel B duty cycle. What is the minimum pulse width that will trigger the SCR?

Replace resistor R\ :sub:`3` with a 0.1uF capacitor. This coupling capacitor acts as a differentiator turning the square pulse of the trigger source output into narrow positive and negative spikes of current on the rising and falling edges of the square wave. How does this effect when and how the SCR is triggered?

Questions:
~~~~~~~~~~

-   How does the SCR differ from an ordinary rectifier diode?
-   Draw the V-I characteristics of an SCR. What can you infer from them?
-   Why is an SCR always turned on by a current into the gate?
-   Why can't the SCR be used as a bidirectional current switch?
-   How does an SCR control the power delivered to the load?
-   Why are SCRs mostly used in AC circuits?

If a source of small ( low current ) SCRs is available, you could repeat the experiment with an actual device rather than our equivalent circuit emulation.

Unintentional parasitic SCRs in Integrated circuits
---------------------------------------------------

We have explored applications for the SCR that intentionally make use of its characteristics. Unfortunately, unintentional SCRs can form in integrated circuits and if these parasitic SCRs get triggered circuit malfunction can result or even reliability issues and damage to the integrated circuit.

LATCH-UP
~~~~~~~~

Latch-up is a potentially destructive situation in which a parasitic SCR is triggered, shorting the positive and negative supplies together. If current flow is not limited, electrical over-stress will occur. The classic case of latch-up occurs in CMOS output devices, in which the driver transistors and wells form a four layer PNPN SCR structure when one of the two parasitic base-emitter junctions is momentarily forward biased during an over-voltage upset event. The SCR turns on and essentially causes a short between the V\ :sub:`DD` power supply and ground.

Since all these MOS devices are located close together on the monolithic die, with appropriate external excitation, the parasitic SCR devices may turn on, a behavior common with poorly designed CMOS circuits. Figure 4 illustrates a simplified cross section showing two transistors, one PMOS and one NMOS; these could be connected together as logic gates or as an analog amplifier or switch. The parasitic bipolar transistors responsible for latch-up behavior, Q\ :sub:`1` (vertical PNP) and Q\ :sub:`2` (lateral NPN) are as indicated.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-scr_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4 Cross-section of PMOS and NMOS devices, with parasitic transistors Q\ :sub:`1` and Q\ :sub:`2`\


Proper design methods to reduce the possibility of SCR formation include increasing the spacing between NMOS and PMOS devices and interposing highly doped regions between and around Nwells and Pwells. Both of these kinds of layout approaches attempt to lower the ß of either the vertical PNP or the lateral NPN parasitic bipolar transistors to less than 1. Some of these methods also tend to lower the resistance of R\ :sub:`PWELL` and R\ :sub:`NWELL` which increases the minimum trigger current needed to turn on the SCR.

Programmable UJT (PUT).
-----------------------

Looking back at figure 1 we note that the triggering current is injected at the base of the NPN Q2. The ON state can just as eaisily be triggered by pulling a current out of the base of the PNP transistor Q1 as shown in figure 5.

The Programmable unijunction transistor or PUT is a close relative of other four layer devices in the thyristor family. Its has a four layered construction just like the SCR and has three terminals named anode(A), cathode(K) and gate(G) again like the thyristors. It is often referred to as a programmable Uni-Junction Transistor because its characteristics and parameters are similar to those of the UJT. The programmability of typical UJT parameters like intrinsic standoff ratio (η), peak voltage(Vp) etc is made by connecting two external resistors. In a conventional UJT, the parameters like Vp, η etc are fixed by the device processing and cannot be changed by the user. The main application of programmable UJT are relaxation oscillators , thyristor triggering, pulse circuits and timing circuits. ON Semiconductor® is the only manufacturer of PUTs today. 2N6027 is the most common type number and it is available in a TO-92 plastic package. The internal block diagram and circuit symbol of PUT are shown below.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-scr_f5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, PUT circuit symbol and Equivalent Circuit


From figure 5, we see that the PUT has a four layered construction. The top P-layer is called the anode (A). The N-layer next to the anode is called the gate (G). The P-layer next to the gate is left unconnected. The bottom most N-layer is called cathode (K). Ohmic contacts are made on the anode, cathode and gate layers for external connection.

PUT characteristics.
~~~~~~~~~~~~~~~~~~~~

PUT characteristics are best shown as a plot of the anode voltage Va and anode current Ia of the PUT. The typical biasing diagram and characteristics plot of a PUT is shown in figure 6.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-scr_f6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, PUT test circuit and I\\V diagram


Typically the anode of the PUT is connected to a positive voltage and the cathode is connected to the ground. The gate is connected to the junction of the two external resistor R1 and R2 which forms a voltage divider. The value ( ratio actually ) of these two resistors determines the intrinsic standoff ratio (η) and peak voltage (Vp) of the PUT.

When the anode to cathode voltage (Va) is increased the anode current will also increase through the PN anode to gate junction and R2 to ground and the current behaves like a typical P-N junction. At a point where a sufficient number of charges are injected and the PNP part starts to turn on and inject current into the base of the NPN. Beyond this point the anode current (Ia) increases and the anode voltage (Va) decreases. This is a negative resistance region. This negative resistance region of the PUT characteristic is used in relaxation oscillators. When the anode voltage (Va) is reduced to a particular level called “Valley Point”, the device becomes fully saturated and no more decrease in Va is possible. There after the device behaves like a fully saturated P-N junction.

Peak voltage (Vp): Is the anode to cathode voltage where the PUT jumps into the negative resistance region. The peak voltage Vp will be usually one diode drop (about 0.7V) plus the gate to cathode voltage (Vg). Peak voltage can be expressed using the equation:

Vp = 0.7V + Vg = 0.7V + VR1 = 0.7V + ηVB

Where η is the intrinsic standoff ratio and VB is the total voltage across the resistor divider network. Intrinsic standoff ratio ( η) : The Intrinsic standoff ratio of a PUT is the ratio of the external resistor R1 to the sum of R1 and R2. It allows us to predict how much voltage there will be across the gate to cathode for a given VB. The intrinsic standoff ratio can be expressed using the equation:

η = R\ :sub:`1`/(R\ :sub:`1`\ +R\ :sub:`2`).

.. _directions-1:

Directions:
~~~~~~~~~~~

Modify your circuit from figure 2 to look like figure 7.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-scr_f7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 7 PUT test circuit


.. _procedure-1:

Procedure:
~~~~~~~~~~

Repeat the same measurements you did on the circuit in figure 2 adjusting the trigger pulse from CH-B output to be a negative pulse rather than a positive pulse.

PUT relaxation oscillator.
~~~~~~~~~~~~~~~~~~~~~~~~~~

A relaxation oscillator is a common application of a programmable UJT. A PUT relaxation oscillator can be used for generating a wide range of saw tooth wave forms. It is called a relaxation oscillator because the timing interval is started by the gradual charging of a capacitor and the timing interval is terminated by the sudden discharge of the capacitor when the PUT is triggered. The circuit diagram of a PUT relaxation oscillator is shown below in figure 8.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-scr_f8.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 8, PUT relaxation oscillator circuit


Resistors R\ :sub:`1` and R\ :sub:`2` set the peak voltage (Vp) and intrinsic standoff ratio (η) of the PUT. Resistor R\ :sub:`k` limits cathode current of the PUT. Resistor R\ :sub:`T` and capacitor C\ :sub:`T` set the frequency of the oscillator. When the supply voltage V\ :sub:`CC` is applied, the capacitor C\ :sub:`T` starts charging through resistor R\ :sub:`T`. When the voltage across the capacitor exceeds the peak voltage (Vp) the PUT is triggered and goes into negative resistance mode and this creates a low resistance path from anode(A) to cathode(K). The capacitor discharges through the PUT. When the voltage across the capacitor goes below valley point voltage (Vv) the PUT reverts to its OFF initial condition and the capacitor C\ :sub:`T` will stop discharging. The capacitor will start to charge again and the cycle is repeated. This series of charging and discharging results in a exponential sawtooth waveform across the capacitor as shown in the figure 9 below.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-scr_f9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 9, PUT relaxation oscillator output waveform


The frequency of oscillation of a PUT relaxation oscillator can be expressed by the following equation:

:math:`F=1/(R_T \times C_T \times ln(1/(1-\eta)))`

Where F is the frequency, η is the intrinsic standoff ratio, R\ :sub:`T` is the resistance and C\ :sub:`T` is the capacitance.

Ramp Generator:
---------------

We can make a linear ramp generator by substituting a current source for R\ :sub:`T` so that the capacitor C\ :sub:`T` charges at a constant rate.

.. _materials-1:

Materials:
~~~~~~~~~~

| 2 – NPN transistors ( 2N3904 )
| 3 – PNP transistors ( 2N3906 )
| 2 – 4.7 KΩ resistors
| 3 – 10 KΩ resistors
| 1 – 200 KΩ resistor
| 1 – 68 KΩ resistor
| 1 – 10 KΩ potentiometer
| 1 – 10 nF capacitor

.. _directions-2:

Directions:
~~~~~~~~~~~

Build the circuit of the ramp generator with PUT (SCR) trigger as shown in figure 10 on your solder-less breadboard. PNP transistors Q\ :sub:`1` and Q\ :sub:`2` form a current mirror current source. PNP Q\ :sub:`3` and NPN Q\ :sub:`4` simulate the operation of the PUT. Emitter follower, Q\ :sub:`5`, is added to provide a low impedance output for the ramp signal. The peak voltage where the simulated PUT triggers is set by potentiometer R\ :sub:`6`. The charging current is fixed ( set by R\ :sub:`3` ) so changing the trigger voltage not only changes the amplitude of the ramp but also the ramp time.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-scr_f10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 10, Ramp generator


Resistor R\ :sub:`4` sets the minimum holding current when the “PUT” is in the ON state. This minimum current must be larger than the charging current from Q\ :sub:`2` in order for the circuit to return to the OFF state and oscillate. If R\ :sub:`3` is made smaller, increasing the charging current, R\ :sub:`4` will also need to be made smaller increasing the holding current by a similar amount. If your circuit fails to oscillate you may need to adjust R3 and/or R4 to satisfy this condition ( based on the betas of your particular Q\ :sub:`3` and Q\ :sub:`4` ).

.. _procedure-2:

Procedure:
~~~~~~~~~~

With both scope input channels in Hi-Z mode attach CH-A to the ramp output at the emitter of Q\ :sub:`5` and CH-B on the trigger voltage at the wiper of R\ :sub:`6`. Adjust the scope time base such that you see at least two cycles of the ramp on the screen. Now adjust R\ :sub:`6` and note the amplitude of the ramp as the trigger voltage is adjusted up and down. Does the slope of the ramp change? What about the frequency of the ramp? Try different values for C\ :sub:`T`.

On channel B you should see the trigger voltage go up and down as R\ :sub:`6` is changed. You should also see a narrow negative pulse each time the circuit triggers and discharges the capacitor.

Temporarily move CH-A to the emitter of PNP Q\ :sub:`3` and compare the ramp seen there to the trigger level seen at the wiper of R6. When does the “PUT” trigger?

.. _questions-1:

Questions:
~~~~~~~~~~

| What is the purpose for resistors R\ :sub:`1` and R\ :sub:`2` in the current mirror?
| How linear is the ramp and what factors in the circuit would effect the linearity

Stair Step Waveform Generator:
------------------------------

As a further demonstration of the switching function of the PUT device configuration consider the LTspice simulation schematic shown in figure 11. To understand the operation of the circuit we first assume there is no charge on capacitor C5 and node Vcap is near the positive supply voltage. A square wave is applied at Vin and is capacitively coupled to the emitter of Q3. The falling edge of the input waveform induces a slug of charge equal to the change in voltage times the value of C4. The charge in voltage also drives the emitter of Q3 below ground turning it on until an equal amount of charge flows through Q3 discharging the voltage on node Vcap toward ground. The change is the voltage on C5 is proportional to the voltage swing of the input waveform and the ratio of C4/C5. The voltage on Vcap continues to discharge until the voltage reaches the trigger voltage of the (simulated) PUT formed by NPN Q4 and PNP Q6. Emitter follower Q1 buffers the Vcap waveform at Vout.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-scr_f11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11. PUT as a Stair Step waveform generator.


The LTspice simulation results are shown in figure 12. A 3.5 V step at the input produces approximately 0.8 V change in the output stair step waveform.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-scr_f12.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 12, Simulated input and output waveforms.


.. _procedure-3:

Procedure:
~~~~~~~~~~

Build the circuit in figure 11 on your solder-less breadboard. Use AWG A to produce the input square wave. Change the amplitude of the waveform to see how it effects the step size in the output waveform. Try different values for capacitors C4 and C5 to see how their ratio changes the step size.

.. _questions-2:

Questions:
~~~~~~~~~~

| What other circuits could be used to generate the input waveform and does it have to be a square wave?
| Will the ramp generator from figure 10, with it’s sharp falling edge, work as the input to the stair step generator? Would it need to be modified in anyway?

**For Further Reading:**

| http://en.wikipedia.org/wiki/Silicon-controlled_rectifier
| :adi:`Electrically Induced Damage to Standard Linear Integrated Circuits <static/imported-files/application_notes/AN-397.pdf>`
| :adi:`Winning the Battle Against Latch-up in CMOS Analog Switches <library/analogDialogue/archives/35-05/latchup/latchup.pdf>`

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
