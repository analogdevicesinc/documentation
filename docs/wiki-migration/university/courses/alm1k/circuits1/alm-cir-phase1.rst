Activity: What is Phase and why do we care? For ADALM1000
=========================================================

Objective:
----------

The objective of this lab activity is to understand what is meant by the phase
relationship between signals and to see how well theory agrees with practice. A
secondary outcome will be a preliminary understanding of the ADALM1000 hardware
and ALICE software.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as
CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

We will investigate the concept of phase by looking at sine waves and passive
components that will allow us to observe phase shift with real signals. First we
will look at a sin wave and the phase term in the argument. You should be
familiar with the equation:

:math:`f(t)= sin(\omega t + \Theta)` (1)

ω sets the frequency of the sin wave as t progresses and θ defines an offset in
time which defines a phase shift in the function.

The sin function results in a value from 1 to -1. First set t equal to a
constant, say, 1. The argument, ωt, is now no longer a function of time. With ω
in radians, the sin of π/4 is approximately 0.7071. 2π radians equals 360° so
π/4 radians corresponds to 45°. In degrees the sin of 45° is also 0.7071.

Now let t vary with time like it normally does. When the value of the ωt changes
linearly with time it yields a sin wave function as shown in figure 1. As ωt
goes from 0 to 2π the sin wave goes from 0 up to 1 down to -1 and back to 0.
This is one cycle or one period, T, of the sine wave. The x axis is the time
varying argument/angle, ωt, which varies from 0 to 2π.

The value of θ is 0 in the function plotted in figure1. Since the sin(0) = 0 the
plot starts at 0. This is a simple sine wave with no offset in time which means
no phase offset. Note that if we are using degrees ωt, goes from 0 to 2π or 0 to
360° to yield the sine wave shown in figure 1.

|image1|

.. container:: centeralign

   Figure 1: 2 cycles of SIN(t)

As a side note, what happens when ωt is greater than 2π? Enter 2.5π in a
calculator and see. As you should know the sine function repeats every 2π
radians or 360°. It is similar to subtracting 2π(I) radians from the argument
where I is the largest integer that yields a nonnegative result.

What happens when we plot a second sine wave function in figure 1 with ω the
same value and θ is also 0? We have another sine wave which lands on top of the
first sine wave. Since θ is 0 there is no phase difference between the sine
waves and they look the same in time.

Now change θ to π/2 radians or 90° for the second waveform. We see the original
sine wave and a sine wave shifted to the left in time. Figure 2 shows the
original sin wave (green) and the second sin (orange) with an offset in time.
Since the offset is a constant we see the original sin wave shifted in time by
the value θ which in this example is 1/4 of the wave period.

|image2|

.. container:: centeralign

   Figure 2: green - SIN(t) orange - SIN(t+π/2)

Theta is the time offset or phase portion of equation 1. The phase angle defines
the offset in time and vice versa. Equation 2 shows the relationship. We
happened to choose a particularly common offset of 90°. The phase offset between
a sine and cosine wave is 90°. The offset angle is almost always not 90. As a
matter of fact is often a function of frequency.

When there are 2 sine waves for example displayed on a scope the phase angle can
be calculated by measuring the time between the 2 waveforms (negative to
positive zero crossings, or “rising edges”, can be used as time measurement
reference points in the waveform). One full period of the sine wave in time is
the same as 360°. Taking the ratio of the time between the 2 waveforms, ∆t, and
the time in one period of a full sine wave, T, you can determine the angle
between them. Equation 2 shows the exact relationship.

**Phase:**

:math:`\Theta=∆t/T 360° = ∆t/T 2pi(rads) = ∆tf2pi(rads)` (2)

Where T is the period of the sinusoid.

**Naturally occurring time offsets in sine waves.**

Some passive components yield a time offset between the voltage across them and
the current through them. In class we showed that the voltage across and the
current through a resistor was a simple time independent relationship. V/I=R.
where R is real and in ohms. So the voltage across and current through a
resistor are always in phase.

For capacitors and inductors the equation relating V to I is similar. V/I=Z,
where Z is an impedance with real and imaginary components. We are only going to
look at capacitors in this lab.

Generally, capacitors are made of two conductive plates separated by a
dielectric material. When a potential difference is applied across the plates,
an electric field is created between the plates. Capacitor dielectrics can be
made of many materials, including thin insulating films and ceramic. A
capacitor's distinguishing characteristic is its capacitance (C), measured in
Farads (F), which measures the ratio between voltage and charge buildup.

The basic rule for capacitors is that the voltage across the capacitor will not
change unless there is a current flowing into the capacitor. The rate of change
of the voltage (dv/dt) depends on the magnitude of the current. For an ideal
capacitor the current i(t) is related to the voltage by the following formula:

:math:`i(t) = C dv/dt` (3)

Right now, the full implications of this is beyond the scope of this lab. You
will observe this behavior in later labs. The impedance of a capacitor is a
function of frequency. The impedance goes down with frequency conversely the
lower the frequency the higher the impedance.

:math:`Zc = 1/(j \omega C)` (4)

Where ω is defined as the angular velocity:

:math:`ω=2pi f`

One subtle thing about equation 4 is the imaginary operator j. When we looked at
a resistor for example there was no imaginary operator in the equation for the
impedance. The sinusoidal current through a resistor and the voltage across a
resistor have no time offset between them because the relationship is completely
real. The only difference is the amplitude. The voltage is sinusoidal and is in
phase with the current sinusoid. This is not the case with a capacitor. When we
look at the waveform of a sinusoidal voltage across a capacitor it will be time
shifted compared to the current through the capacitor. The imaginary operator,
j, is responsible for this. Looking at figure 3 we can see that the current
waveform is at a peak ( maximum ) when the slope of the voltage waveform ( time
rate of change dv/dt ) is its highest.

The time difference can be expressed as a phase angle between the two waveforms
as defined in Equation 2.

|image3|

.. container:: centeralign

   Figure 3: Phase Angle Determination between Voltage and Current.

You probably have seen circuits made entirely from resistors. These circuits
have only real impedance, which means that voltages throughout the circuit will
all be in phase (i.e. θ = 0 degrees) as it is the complex impedance that shifts
the current in time with respect to the voltage. Note that the impedance of a
capacitor is wholly imaginary. Resistors have real impedances, so circuits that
contain both resistors and capacitors will have complex impedances.

To calculate the theoretical phase angle between voltage and current in an RC
circuit:

i(t) = v(t)/Z\ :sub:`circuit`

Where Z\ :sub:`circuit` is the total circuit impedance = I

Rearrange the equation until it looks like I=A+jB

Where A and B are real numbers.

The phase relationship of the current relative to the voltage is then:

:math:`\Theta = tan^-1 (B/A)` (5)

Materials:
~~~~~~~~~~

ADALM1000 hardware module 2 – 470 Ω resistors 1 – 1 uF capacitor

**Oscilloscope:**

You are going to use the ALM1000 board and the ALICE desktop software for the scope functions. The :doc:`user's guide </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` tells how to set things up.

**Signal Generator:**

You are going to also use the ALM1000 board for the signal generator functions. The :doc:`user's guide </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` tells how to set up the signal generator.

**Instructional Objectives:**

1. Explore the phase relationship of voltage and current in a resistive circuit.
   2. Explore the phase relationship of voltage and current in a capacitive,
   resistive (RC) circuit.

Procedure:
~~~~~~~~~~

Setup a quick measurement using ALICE Desktop:

• Be sure the ALM1000 is plugged into a USB port and start up the ALICE Desktop application. • The Main screen should look like a scope display with adjustable range, position and measurement parameters. • Along the bottom of the screen be sure that CA V/Div and CB V/Div are both set to 0.5. • Also check that CA V Pos and CB V Pos are set to 2.5. • CA I mA/Div should be set to 2.0 and CA I Pos should be set to 5.0. • In the AWG controls window, set the Frequency of CHA and CHB to 1000 Hz with 90° Phase, 0 V Min and 5 V Max values (5.000V Pk-Pk output). Select SVMI mode and Sin waveform shape.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-phase-4.png
   :align: center
   :width: 200

• Under the Meas drop down select P-P for both CA-V, CA-I and CB-V. • Set the Time/Div to 0.5 mS and under Curves drop down select CA-V, CA-I and CB-V.

Note that the CHA and CHB function generator outputs connect to the channel
inputs directly on the board. You don't need a wire to make the connection.

• On your solderless breadboard connect the CHA output to one end of a 470 Ω resistor. • Connect the other end of the resistor to GND. • Click on the scope Start button.

If the board has been calibrated correctly you should see one sine wave on top
of the other. With CHA and CHB both equal to 5.00 Vpp. If the calibration isn't
correct you might see 2 sine waves in phase with the amplitude of CHA different
from CHB. Re-calibrate if there is a significant voltage difference.

2. Measure the phase angle between two generated waveforms:

• Be sure that CA V/Div and CB V/Div are both still set to 0.5 and that CA V Pos and CB V Pos are set to 2.5. • CA I mA/Div should be set to 2.0 and CA I Pos should be set to 5.0 • Set the Frequency of CHA and CHB to 1000 Hz with 90° Phase, 0 V Min and 5 V Max values (5.0V Pk-Pk output). Select SVMI mode and Sin waveform shape.

You should see what looks like 1 sine wave. There are two just one is on top of
the other.

• In the AWG control window, change the phase, θ, of CH B to 135° ( 90 + 45 ). • Which Channel looks like the sine is occurring before the other? \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

The CHB signal should look like it is leading (happening before) the CHA signal.
The CHB signal crosses the 2.5 V axis from below to above before the CHA signal.
It turns out a positive θ is called a phase lead. The low to high crossing time
reference point is arbitrary. The high to low crossing could also be used.

• Change the phase offset of CHB to 45° (90 - 45).

Now it looks like the CHB signal lags the CHA signal.

• Set the Meas display for CA to Frequency and A-B Phase. For CB display B-A Delay. • Set the Time/Div to 0.2 mS. • Press the red Stop button to pause the program. Using the left mouse button we can add marker point on the display.

If the CHA sine wave crosses 'first' and the CHB 'second' we can measure the
time offset between them.

• Make sure the vertical position of the 2 signals is set to 2.5. • Measure the time difference between the CHA and CHB signal zero crossings using the markers.

What is the ∆t? \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

• Use the measured ∆t and equation 2 to calculate the phase offset. θ \_\_\_\_\_\_\_\_°

Note you cannot measure the frequency of a signal that does not have at least
one full period displayed on the screen. Usually you need more than 2 cycles to
get consistent results. You are generating the frequency so you already know
what it is. You don't need to measure it in this part of the lab.

3. Measuring Magnitude using a real circuit.

|image4|

.. container:: centeralign

   Figure 4: R-R circuit.

   |image5|

.. container:: centeralign

   Figure 5: R-R breadboard connections.

• Build the circuit shown in Figure 4 on your solderless breadboard using two 470 Ω resistors. • In the AWG controls window, set the Frequency of CHA to 200 Hz with 90° Phase, 0 V Min and 5 V Max values (5.0V Pk-Pk output). Select SVMI mode and Sin waveform shape. • Select Hi-Z mode for CHB. The rest of the settings for CHB do not matter because it is now being used just as an input.

• Connect the CHA output CHB input and GND with wires as shown by the colored test points. • Set the horizontal time scale to 1.0 mS/Div to display two cycles of the waveform. • Click on the scope Start button if it is not already running.

The voltage waveform displayed in CHA is the voltage across both resistors (V\ :sub:`R1`\ +V\ :sub:`R2`). The voltage waveform displayed in CHB is the voltage across just R\ :sub:`2` (V\ :sub:`R2`). To display the voltage across R\ :sub:`1` we use the Math waveform display options. Under the Math drop down menu select the CAV-CBV equation. You should now see a third waveform for the voltage across R\ :sub:`1` (V\ :sub:`R1`). To see both traces you can adjust the vertical position of a channel to separate them. Make sure to set the vertical positon back to realign the signals.

• Record V\ :sub:`R1` and V\ :sub:`R2`.

V\ :sub:`R1`\ \_\_\_\_\_\__V\ :sub:`PP`. V\ :sub:`R2`\ \_\_\_\_\_\__V\ :sub:`PP`. V\ :sub:`R1`\ +V\ :sub:`R2`\ \_\_\_\_\_\__V\ :sub:`PP`.

• Can you see any difference between the zero crossings of V\ :sub:`R1` and V\ :sub:`R2`? \_\_\_\_\_\_\_\_\_ • Can you even see two distinct sine waves? \_\_\_\_\_\_\_\_

Probably not. There should be no observable time offset and thus no phase shift.

4. Measure Magnitude of an interesting real circuit.

• Replace R\ :sub:`2` with a 1 uF capacitor C\ :sub:`1`.

|image6|

.. container:: centeralign

   Figure 6: RC circuit.

   |image7|

.. container:: centeralign

   Figure 7: RC breadboard connections.

• In the AWG controls window, set the Frequency of CHA to 500 Hz with 90° Phase, 0 V Min and 5 V Max values (5.0V Pk-Pk output). Select SVMI mode and Sin waveform shape. • Select Hi-Z mode for CHB. • Set the horizontal time scale to 0.5 mS/Div to display two cycles of the waveform.

Because there is no DC current through the capacitor we have to handle the
average (DC) values of the waveforms differently.

• On the right hand side of the main screen there are places to enter a DC Offset for channels A and B. Set the offset values as shown.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-phase-7.png
   :align: center
   :width: 180

• Now that we have removed the offset from the inputs we need to change the vertical position of the waveforms to re-center them on the grid. Set CA V Pos and CB V Pos to 0.0.

• Click on the scope Start button if it is not already running. • Measure CA-V, CA-I, CB-V and Math (CAV - CBV) pk-pk.

What signal is the Math waveform? \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

• Record V\ :sub:`R1`, V\ :sub:`C1` and V\ :sub:`R1`\ +V\ :sub:`C1`.

V\ :sub:`R1`\ \_\_\_\_\_\_\_\_\_\_\__V\ :sub:`PP`. I\ :sub:`R1`\ \_\_\_\_\_\_\_\_\_\_\__mA\ :sub:`PP`. V\ :sub:`C1`\ \_\_\_\_\_\_\_\_\_\_\_\_\_\__V\ :sub:`PP`. V\ :sub:`R1`\ +V\ :sub:`C1`\ \_\_\_\_\_\_\_\_\_\_\__V\ :sub:`PP`.

Now something to do with phase. Hopefully you see a few sine waves with time
offsets or phase differences displayed on the grid. Let's measure the time
offsets and calculate the phase differences.

5. Measure the time difference between V\ :sub:`R1`, I\ :sub:`R1` and V\ :sub:`C1`.and calculate the phase offsets.

Use equation 2 and the measured ∆t to calculate the phase angle θ.

:math:`\Theta = \Delta tf360°`

The markers are useful for determining ∆t. Here's how.

• Display at least 2 cycles of the sine waves.

• Set the Horizontal Time/Div. to 0.5 uSec. Be sure to click on the red Stop button before trying to place markers on the grid.

Note the Marker Delta display keeps track of the sign of the difference.

You can use the measurement display to get frequency. Since you set the
frequency of the source you don't really need to depend on the measurement
window for this value.

Assume ∆t is 0 if you really can't see any difference with 1 or 2 cycles of the
sine wave on the screen.

• Put a first marker at the neg. to pos. zero crossing location for the CA-V ( V\ :sub:`R1` + V\ :sub:`C1`) signal. Put a second marker at the nearest neg. to pos. zero crossing location for the Math ( V\ :sub:`R1` ) signal. Record the time difference and calculate the phase angle. Note ∆t maybe a negative number. Does this mean the phase angle leads or lags?

∆t \_\_\_\_\_\_\_\_\_, θ\_\_\_\_\_\_\_\_\_

To remove the markers for the next measurement click on the red Stop button.

• Put a first marker at the neg. to pos. zero crossing location for the CA-V ( V\ :sub:`R1` + V\ :sub:`C1`) signal. Put a second marker at the nearest neg. to pos. zero crossing location for the CB-V ( V\ :sub:`C1` ) signal. Record the time difference and calculate the phase angle.

∆t \_\_\_\_\_\_\_\_\_, θ\_\_\_\_\_\_\_\_\_

• Put a first marker at the neg. to pos. zero crossing location for the Math ( V\ :sub:`R1` ) signal. Put a second marker at the nearest neg. to pos. zero crossing location for the CB-V ( V\ :sub:`C1` ) signal. Record the time difference and calculate the phase angle.

∆t \_\_\_\_\_\_\_\_\_, θ\_\_\_\_\_\_\_\_\_

Is there any measurable time different ( phase shift ) between the Math ( V\ :sub:`R1` ) signal and the displayed CA-I current waveform? Since this is a series circuit the current sourced by AWG channel A is equal to the current in R\ :sub:`1` and C\ :sub:`1`.

6. Measure the time difference and calculate the phase θ offset at a different
   frequency.

• Set AWG CHA to 1000 Hz and the time / div to 0.2 mSec/div. • Put a first marker at the neg. to pos. zero crossing location for the CA-V ( V\ :sub:`R1` + V\ :sub:`C1`) signal. Put a second marker at the nearest neg. to pos. zero crossing location for the Math ( V\ :sub:`R1` ) signal. Record the time difference and calculate the phase angle. Note ∆t maybe a negative number. Does this mean the phase angle leads or lags?

∆t \_\_\_\_\_\_\_\_\_, θ\_\_\_\_\_\_\_\_\_

To remove the markers for the next measurement click on the red Stop button.

• Put a first marker at the neg. to pos. zero crossing location for the CA-V ( V\ :sub:`R1` + V\ :sub:`C1`) signal. Put a second marker at the nearest neg. to pos. zero crossing location for the CB-V ( V\ :sub:`C1` ) signal. Record the time difference and calculate the phase angle.

∆t \_\_\_\_\_\_\_\_\_, θ\_\_\_\_\_\_\_\_\_

• Put a first marker at the neg. to pos. zero crossing location for the Math ( V\ :sub:`R1` ) signal. Put a second marker at the nearest neg. to pos. zero crossing location for the CB-V ( V\ :sub:`C1` ) signal. Record the time difference and calculate the phase angle.

∆t \_\_\_\_\_\_\_\_\_, θ\_\_\_\_\_\_\_\_\_

Post-lab Questions:
~~~~~~~~~~~~~~~~~~~

Answer all the questions within the procedure section.

Appendix:
~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-phase-8.png
   :align: center
   :width: 700

.. container:: centeralign

   Screen capture of step 5 with Time/ Div set to 0.5 mS.

**Use the Phase Analyzer Virtual Instrument**

ALICE includes a Phase Analyzer Virtual Instrument that can assist in
understanding phase relationships between signals and polar notation and polar
plots.

:doc:`Phase Analyzer User Guide. </wiki-migration/university/tools/m1k/alice/phase-analyzer-user-guide>`

**Resources:**

-  Fritzing files: :git-education_tools:`m1k/fritzing/phase_bb`
-  LTSpice files: :git-education_tools:`m1k/ltspice/phase_ltspice`

**For Further Reading:**

:doc:`ALICE Desktop User's Guide </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` `Wikipedia page on Phase and waves <https://en.wikipedia.org/wiki/Phase_(waves)>`_

**Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents** **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**

.. |image1| image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-phase-1.png
   :width: 550
.. |image2| image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-phase-2.png
   :width: 550
.. |image3| image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-phase-3.png
   :width: 600
.. |image4| image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-phase-5.png
   :width: 420
.. |image5| image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/rail_to_rail_bb.png
   :width: 420
.. |image6| image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-phase-6.png
   :width: 420
.. |image7| image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/rc_cir_bb.png
   :width: 420
