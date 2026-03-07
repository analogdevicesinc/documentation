Activity: Diode Rectifiers, For ADALM1000
=========================================

Objective:
----------

The objective of this lab activity is to investigate half wave and full wave diode rectifiers used to convert AC to DC.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V, CB-V for the voltage waveforms and CA-I, CB-I for the current waveforms.

The ALM1000 generates and measures unipolar or single-ended signals in the range of 0 to 5 V. To simplify and better understand the concepts in this lab we would rather represent the signals as being bipolar swinging both positive and negative either side of the common node. With the ALM1000 we can use the fixed 2.5 V supply as the common node and then consider the allowed signal range as going from -2.5 V to +2.5 V.

In the ALICE desktop software we can make the following adjustments. As shown in figure 1, on the right hand side of the scope screen, enter 2.5 for the CA-V and CB-V offset adjustment. This is because in this lab we are referencing all the measurements to the +2.5 V common rail. Also enter 0 for the CH-A and CH-B vertical position settings (along bottom of scope screen). The vertical scale should now be centered on 0 and go from -2.5 to +2.5.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-lcres-d1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1, Adjust offset for 2.5 V signal reference


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 – Resistor (100 Ω or any similar value)
| 4 – small signal diode (1N914 or similar)

Directions:
~~~~~~~~~~~

Set up the breadboard with AWG Channel A attached to one end of the diode. The other end of the diode is connected to one end of the 100 Ω load resistor as shown in figure 2. The other end of the resistor is connected to the 2.5 V rail. Single ended input of scope channel B is connected to the end of the resistor not connected to the 2.5 V rail.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-rectifier-f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, Connection diagram for half wave diode rectifier


Hardware Setup:
~~~~~~~~~~~~~~~

Configure AWG CHA in SVMI mode with a 100 Hz Sine Shape and with Min value set to 0 and Max value set to 5.0. Channel B is set in Hi-Z mode and used to measure the voltage across the load resistor, R\ :sub:`L`. Both scope channels should be set to 0.5 V per division.

Procedure:
~~~~~~~~~~

Under the curves drop down menu select CA-V, CA-I and CB-V to be displayed. Adjust the vertical range for the Channel A current to fit nicely on the grid. As we can see from figure 2, I\ :sub:`CA` is the same as I\ :sub:`RL` and only flows when the voltage CA-V is positive (with respect to the 2.5 V rail). Using the Meas drop down menus select Max and Avg for CI-A to display the peak and average current through the resistor. Select Max and Avg for CB-V to display the peak and average voltage on the resistor.

Compare the measured voltage in CB-V with the voltage calculated by multiplying the CA-I current waveform by the 100 Ω value of R\ :sub:`L`.

Questions:
~~~~~~~~~~

| Why is the peak value of the rectified output less than the peak value of the AC input and by how much?
| At what point in the input waveform does the rectified waveform become positive i.e. something other than zero?
| What happens if the direction of the diode is reversed? Repeat the experiment with the direction of the diode reversed.

Further Exploration:
~~~~~~~~~~~~~~~~~~~~

Replace the 1N914 diode with a light-emitting diode, or LED.

1. How does the waveform for the rectified output compare to your earlier results with the 1N914 diode? By how much does the forward-bias voltage drop increase?

2. Experiment with the three different waveform shapes while the waveform generator remains set to 100 Hz, pay attention to the brightness of the LED. Discuss your observations of waveform shape and brightness and relate these observations to your measured effective DC (average and RMS)values for each waveform shape.

3. Reduce the waveform generator frequency. At what frequency does the flashing LED stop flickering and begin to appear as a constant intensity?

Full wave rectifier:
~~~~~~~~~~~~~~~~~~~~

The purpose of this activity is to investigate the use of two diodes as a full wave rectifier.

.. _directions-1:

Directions:
~~~~~~~~~~~

Again using 1N914 diodes, set up the breadboard with AWG CH-A attached to one end of the first diode, D\ :sub:`1`, and AWG CH-B to one end of the second diode, D\ :sub:`2`. Both diodes should face in the same direction as shown in figure 3. The other end of each diode is connected to one end of the 100 Ω load resistor R\ :sub:`L`. The other end of the resistor is connected to the 2.5 V rail.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-rectifier-f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, Connection diagram for full wave diode rectifier


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

The AWG CH-A waveform generator should be configured for a 100 Hz Sine wave with 0 volt Min value and 5 volt Max value. The AWG CH-B generator should also be configured for a 100 Hz Sine wave but with 5 volt Min value and 0 volt Max value. This effectively inverts, 180° phase shift, CH-B with respect to CH-A.

If both 0 degree and 180 degree phases of the AC input are available, then a second diode can fill in the missing half-wave of the input and produce the full-wave rectified signal. Again the forward voltage of the diodes will be apparent and the output waveform will not come to a sharp point at the zero crossing due to the non-zero turn on voltage of the diodes.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Under the curves drop down menu select CA-V, CA-I and CB-V, CB-I to be displayed. Adjust the vertical range for the Channel A and channel B current to fit nicely on the grid. As we can see from figure 3, I\ :sub:`CA` flows in R\ :sub:`L` for the half cycle when CA-V is positive and I\ :sub:`CB` flows in R\ :sub:`L` for the half cycle when CB-V is positive. The sum of I\ :sub:`CA` and I\ :sub:`CB` is the same as I\ :sub:`RL`. Using the Meas drop down menus select Max and Avg for CI-A to display the peak and average current from Channel A. Select Max and Avg for CB-I to display the peak and average current from Channel A.

To display the sum of the channel A and channel B current (in mA) enter the following Math Formula:

(IBuffA[t] + IBuffB[t])*1000

Under Math select Formula to display the calculated waveform. Set the Math-Axis to I-A. This also in effect displays the voltage across R\ :sub:`L`. The voltage is the current (in A) times the 100 Ω value of R\ :sub:`L`. You can turn off the individual CA-I and CB-I curves at this point.

.. _questions-1:

Questions:
~~~~~~~~~~

| What happens if the direction of the diodes is reversed? Repeat experiment with the direction of both diodes reversed.
| What happens if the direction of one diode is opposite of the other? Repeat experiment with the direction of one diode (D\ :sub:`1`) reversed.
| How could both 0 degree and 180 degree phases be created from a single source? (how about a transformer?)

.. _further-exploration-1:

Further exploration:
~~~~~~~~~~~~~~~~~~~~

Replace D\ :sub:`1` and D\ :sub:`2` with red and green LEDs. Reduce the frequency of both AWG channels to 5 Hz or less. Are the two LEDs ever both on at the same time? You will need to increase the time per division setting to display more than one cycle of the signal.

1. How does the waveform for the rectified output compare to your earlier results with the 1N914 diodes? By how much does the forward-bias voltage drop increase?

2. Experiment with the three different waveform shapes while the waveform generator is set to 100 Hz, pay attention to the brightness of the LEDs. Discuss your observations of waveform shape and brightness and relate these observations to your measured effective DC values for each waveform shape.

3. Reduce the waveform generator frequency. At what frequency do the flashing LEDs stop flickering and begin to appear as a constant intensity?

Bridge rectifier
~~~~~~~~~~~~~~~~

The purpose of this part of the lab is to investigate the use of four diodes as a bridge rectifier.

.. _directions-2:

Directions:
~~~~~~~~~~~

Four diodes (1N914) can be arranged in a bridge configuration to provide a full-wave rectification from an AC source such as a center-taped transformer winding. The center taped winding can be represented by the two AWG outputs centered around a common node if they are 180 degrees out of phase with the center tap being the +2.5 V common rail, shown in figure 4. The load resistors R\ :sub:`L1` and R\ :sub:`L2` (100 Ω each) are connected to the common node +2.5 V rail thus producing both positive and negative rectified outputs measured by inputs AIN and BIN with respect to the common node. However, it can also be noted that only the AC input or the load can be referenced to the common (+2.5 V rail in this case ). Note that if R\ :sub:`L1` and R\ :sub:`L2` are equal to each other then no net current will flow into or out of the +2.5 V common mode.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-rectifier-f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 Connection diagram for diode bridge rectifier


.. _hardware-setup-2:

Hardware Setup:
~~~~~~~~~~~~~~~

The AWG CH-A waveform generator should be configured for a 100 Hz Sine wave with 0 volt Min value and 5 volt Max value. Check the B= Comp A check box as shown in figure 5 to set channel B to be the complement of channel A i.e. same p-p value but 180 degrees out of phase. Set the mode to be SVMI Split I/O to generate the sine waves on the CH A and CH B pins and measure the voltage waveforms at the bridge output on the AIN and BIN pins.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-rectifier-f5.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 5, AWG channel settings


Checking the Sync AWG box means you will not need to set a trigger input source or level.

.. _procedure-2:

Procedure:
~~~~~~~~~~

Under the Curves drop down menu select CA-V, CA-I and CB-V, CB-I to be displayed. Adjust the vertical range for the Channel A current to fit nicely on the grid. As we can see from figure 4, I\ :sub:`CA` flows through D\ :sub:`2` and D\ :sub:`3` (green arrows) in R\ :sub:`L` for the half cycle when CA-V is positive and flows through D\ :sub:`1` and D\ :sub:`4` (red arrows) in R\ :sub:`L` for the half cycle when CA-V is negative. The current in channel A changes direction (blue arrow) from sourcing current (+) in the positive half cycle to sinking current (-) in the negative half cycle. We see that the absolute value of I\ :sub:`CA` is the same as I\ :sub:`RL` (black arrow).

On the Math setup screen select CA-CB to display the differential voltage waveform across the load resistors at the output of the bridge. You should see traces like those shown in figure 6. Note that the AIN and BIN voltage traces are symmetric around the +2.5 V common node voltage.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-rectifier-f6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, Voltage and Current traces


The disadvantage of this circuit is that now two diode drops are in series with the load and the peak value of the rectified output is less than the AC input by 1.5 Volts rather than the 0.75 V in the previous circuits.

**Added activities**

Try replacing the diodes with RED (D\ :sub:`1`, D\ :sub:`4`) and GREEN (D\ :sub:`2`, D\ :sub:`3`) LEDs to match the arrows in figure 4. Reduce the AWG frequency to 10 Hz or less to see when the current is flowing in each diode.

Connect a 100 uF capacitor across the bridge output to filter the rectified voltages. Be sure to note the correct polarity of the electrolytic capacitor with respect to the positive and negative outputs of the bridge. How does this filter cap change the voltage and current waveforms?

.. _questions-2:

Questions:
~~~~~~~~~~

How could you reconfigure this circuit to allow one end of the load resistor to be connected to ground rather than how it is shown figure 4 with one end of the AC source grounded?

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/diode_rectifiers_ltspice`
-  Fritzing files: :git-education_tools:`diode_rectifiers_bb <m1k/fritzing/diode_rectifiers-bb>`

**For Further Reading:**

| `Rectifiers <https://en.wikipedia.org/wiki/Rectifier>`_
| `Bridge Rectifier <https://en.wikipedia.org/wiki/Diode_bridge>`_

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to** :doc:`Circuits </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>` **Lab Activity Table of Contents**
