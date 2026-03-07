Activity: AC Synchronous Motors - ADALM1000
===========================================

Objective:
----------

The objective of this activity is to investigate the voltage and current waveforms of AC induction motors, specifically synchronous AC motors. Making measurements on a full size AC line voltage motor in a teaching lab setting can be both expensive and potentially hazardous. Fortunately, scaled down versions of AC induction motors are available in the form of small low voltage stepper motors.

Background:
-----------

Motors are electrical machines that convert electrical energy to rotational mechanical energy by the interaction of magnetic fields and conductors. Motors can be constructed that operate on direct current, DC, or sinusoidal time varying or alternating current, AC. Unlike motors that run directly on DC current, AC motors generally do not require brushes and commutators.

The rotor in a synchronous AC motor spins in sync with the excitation field (there is no "slip"). The magnetization of the rotor is produced by a permanent magnet in brushless designs or by windings with an AC current supplied through slip rings (usually in large, high-power motors).

Synchronous motors maintain a constant speed for all loads. If the load exceeds the rated load, the motor 'pulls out' of synchronism and ceases to rotate smoothly. Synchronous motors operate at a fixed rotational speed and are suitable for precision drives where accurate speed control is required. The rotational speed can be adjusted by varying the AC supply frequency from a variable frequency drive circuit.

Rotating Magnetic Fields
~~~~~~~~~~~~~~~~~~~~~~~~

For an induction motor to start running, a rotating magnetic field (RMF) must be produced in the stator, which induces rotational torque in the rotor. Since the stator does not physically move, the rotation of the magnetic field is produced by the interaction between electromagnetic forces produced in the stator windings. In a three-phase motor, with each winding supplied by a voltage waveform that is 120 degrees out of phase with the other windings, the sum of the forces produced is a vector that continuously rotates. This means that three-phase power can induce torque in the rotor from a standstill. Thus three phase motors can self start without additional components.

However, a single phase induction motor is powered from a single phase supply that runs through a single stator winding. One stator winding by itself cannot produce a RMF. The single coil merely produces a pulsing magnetic field (and force) that is made of two opposing fields spaced 180 degrees apart.

This creates two problems:
^^^^^^^^^^^^^^^^^^^^^^^^^^

First, the single phase motor will not be self starting because the magnetic field produced by the stator is not rotating.

Second, although a single winding can potentially drive the motor once it spins at a speed synchronous with the AC line frequency, it does not produce a constant torque in the rotor over a full revolution, which will lead to a loss of efficiency and performance. The rotor experiences maximum torque at approximately 10% slip (the difference in rotation angle between the rotor and the stator winding). Therefore the rotor will spend a large part of each revolution experiencing very low torque.

Auxiliary Winding
~~~~~~~~~~~~~~~~~

Single-phase induction motors use a second stator winding to overcome these problems, called an ‘auxiliary winding’ or ‘start winding.’ This second winding is physically rotated 90° with respect to the first “main” winding. The second winding, when supplied by a voltage with 90° phase shift with respect to the “main” winding, produces a second pulsing magnetic field. The 90° phase shifted second winding voltage can be generated from the first main supply by means of a capacitor that, in combination with the coil inductance, changes the phase of the supply voltage. This means that the interaction between the two windings produces a rotating magnetic field, and the motor will self start.

There are sometimes two different capacitors used by single phase induction motors for different parts of their operation.

Start Capacitors
^^^^^^^^^^^^^^^^

A start capacitor is one that is used to provide starting torque to the motor. They can have relatively high losses and low efficiency and are generally not designed for continuous duty. It is necessary to disconnect them once the motor gets up to speed using a centrifugal switch or relay of some kind.

Run Capacitors
^^^^^^^^^^^^^^

A run capacitor is used to smooth the motor's torque during each revolution, increasing efficiency and performance. They usually have lower values than a start capacitor and are of the non-polarized oil-filled type to reduce energy losses.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-ac-sync-motor-fig-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Single Phase Synchronous Motor with RUN Capacitor.


Low Voltage Stepper Motor as AC Synchronous Motor
-------------------------------------------------

While it would be possible to make measurements on a full size AC line voltage motor using the techniques outlined in this tutorial: :doc:`Making AC Mains Voltage and Current Measurements </wiki-migration/university/courses/tutorials/alm-awg-ac-mains-tests>` doing so in a teaching lab setting can be both expensive and potentially hazardous. Fortunately, a version operating on both scaled down voltage and current is available in the form of small low voltage stepper motors. These “stepper” motors are constructed essentially the same as AC power line motors with two windings physically rotated 90° with respect to each other. Versions designed to operate on as little as 5V are common as well as versions designed for 12 V or even 24 V are available. Un-loaded operating currents in the 100 mA to 200 mA are typical. The Maximum Peak coil current can generally be determined from the coil DC resistance and operating voltage spec.

Materials:
----------

| ADALM1000 module
| Jumper Wires
| Solderless Breadboard
| Small low voltage, low power stepper motor
| Various capacitors

**Stepper Motor Specifications**

For this example setup a MITSUMI M35SP-7 stepping motor is used. The specifications are listed below. Other motors from different manufacturers with similar specifications can be just as easily be substituted.

-  Working Voltage: DC 5.4~6.6V
-  Rated Current/Phase 807mA max.
-  Coil DC Resistance 8Ω/phase±7%
-  Phase Inductance: 30 mH

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-ac-sync-motor-fig-2.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 2, Example MITSUMI motor.


Directions: 5 V motors
----------------------

Stepper motors specified for 5 Volt operation can be driven directly from the M1k SMU channels as shown in figure 3. For simple first pass testing purposes we can dispense with the Run Capacitor by driving Coil A from one SMU channel (CH A) with 0° phase shift and driving Coil B from the other SMU channel (CH B) with either a 90° or 270° phase shift (quadrature phase).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-ac-sync-motor-fig-3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Quadrature Phase Drive.


Connect the two motor windings to the M1k SMU channels as shown in figure 3. Set both AWG channel’s Max value to 4.9 and Min value to 0.1 (2.4 V peak centered on +2.5). Set both channel’s Freq to 60 Hz. Set channel B Phase to 270 (-90°). Set the mode of both channels to SVMI.

In the Time screen, select the voltage and current traces for both channels. Because the motor coils are connected to (referenced to) the +2.5V rail to simplify the time trace display and show the actual coil voltage waveforms, set the voltage channel offsets to 2.5 as shown. This will remove the 2.5 V offset.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-ac-sync-motor-fig-co.png
   :align: center
   :width: 200px

.. container:: centeralign

   Channel Offset settings.


To center the waveforms around 0, the Channel Range and Position settings are shown here.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-ac-sync-motor-fig-rg.png
   :align: center
   :width: 600px

.. container:: centeralign

   Channel Range and Position settings.


In addition to the Coil voltage and current waveforms there are two “calculated” signals of interest. The current and voltage waveforms are out of phase with each other so we are also interested with the sum of the two coil currents and the difference between the two voltage waveforms (we will be using the voltage difference later when calculating the value for a Run capacitor). We can use the Math traces to display these two signals. There already is a Built-In expression for CAV – CBV so select that. We can use the Y Math Trace to enter a formula to calculate the sum of the two channel currents. Enter IBuffA[t]+IBuffB[t] for the Y Formula and set Y Units to mA and Set Y Axis to I-A to use the same axis as the channel A current trace. Be sure to click on Check and Apply to make sure there are no typos and apply the formula to the Y Math Trace. Also remember to select (display) the Y Math Trace from the Curves Drop down Menu.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-ac-sync-motor-fig-mt.png
   :align: center
   :width: 300px

.. container:: centeralign

   Math Traces settings.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-ac-sync-motor-fig-4.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 4, Coil voltage and current time waveforms.


Viewing the waveforms in the time domain can be informative but using the Phase Analyzer Tool to display the waveforms as Phasors is even more instructive. Open the Phase Plot screen. Because the frequency is only 60 Hz we need to increase the number of FFT samples to 8192. The same six waveforms can be displayed as phase vectors (as of release version 1.3.13). Turn on voltages CA-V, CB-V and CA - B V and currents CA-I, CB-I and CA + B I.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-ac-sync-motor-fig-5.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 5, Coil voltage and current phasors.


Questions:
~~~~~~~~~~

-  What will happen if the Channel B Phase is changed to 90° instead of 270° (-90°)?
-  What will happen if the two motor coils are swapped coil A for coil B?
-  Can you make the motor start spinning with just one coil driven (other coil disconnected)? Try giving the motor shaft a spin by hand? Does it matter which direction you spin the shaft?

Calculating Run/Start capacitor Value:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The value of the Run Capacitor is a function of the line frequency and the coil inductance. We can actually derive a simplified formula for the Run Capacitor value from the equation for capacitive reactance:

:math:`\displaystyle X_C = \frac{1}{2} \pi F C`

Combined with a version of Ohm’s Law:

:math:`E = I X_C`

Or

:math:`C = I / 2 \pi F E`

Where I is the RMS Coil B current and E is the RMS voltage across the Run Capacitor (VA-VB V\ :sub:`RMS`). If we assume the line frequency F is 60 Hz we can take the 1/(2πF) part:

:math:`\displaystyle \frac{1}{2} \pi F = 0.002652`

To simplify, we can use approximate numbers and just call it amps times 0.002652. Then, divide by the voltage to get the capacitance. If we want C in microfarads (or millionths of a farad) we scale the above number by 1 million to get 2652.

Referring back to figure 1 we see that voltage across the Run capacitor is the Coil A voltage minus the Coil B voltage. Using the RMS values from figure 5 we have the coil B current is 64.26 mA RMS and the VA-VB voltage is 2.3 V RMS.

This gives us the capacitive reactance, which, multiplied by the amperage and then divided by the voltage, is the capacitance. So you get: Xc = 2,652 and E = 0.06426 x Xc = 170.41, so that 170.41 ÷ 2.3 V = 74.09 uF.

Now that we have an approximate value for the Run Capacitor we can drive the motor with just one of the SMU channels or with both channels set to the same phase as shown in figure 6. To make a 74 uF capacitor, a close approximation is to use a 47 uF cap in parallel with a 33 uF cap for a total of 80 uF. Another close approximation would be a 47 uF cap in parallel with 22 uF or 69 uF. Generally caps of these values will be polarized electrolytic capacitors. Using such capacitors on AC signals without a DC bias is not a good idea long term but in this use case as a lab experiment they will work fine. Just choose capacitors with much higher voltage ratings such as 35 V or higher.

Connect the Run Cap C1 between the Coil B winding and the CH B pin on M1k. Connect the BIN pin on M1k to the Coil B winding. Change the AWG channel B mode to Split I/O (still in SVMI) so that voltage Trace B will be the coil voltage. The AWG B output waveform will be identical to the AWG A output waveform so we don’t really need to display it. The current trace for channel B will still be the coil B current waveform. The AWG channel A and channel B voltage waveforms need to be set to the same frequency, amplitude and phase now, as if they are the same signal. Set the channel B phase back to 0 to match channel A.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-ac-sync-motor-fig-6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, Single Phase Drive with RUN Capacitor.


The following time and phase screens in figures 7 and 8 were taken using the same stepper motor using two electrolytic capacitors in parallel, a 47 uF and a 33 uF, as Run capacitor C1. The results are very similar to the measurements seen in figures 4 and 5.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-ac-sync-motor-fig-7.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 7, Run capacitor Coil voltage and current time waveforms.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-ac-sync-motor-fig-8.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 8, Run capacitor Coil voltage and current phasors.


Note that the sum of the two coil currents are in phase with the AC supply voltage (VA = VB) and the Power factor will be 1. Refer to this activity on :doc:`AC Power Factor </wiki-migration/university/courses/alm1k/circuits1/alm-cir-ac-power-factor>` for more on how it is calculated.

.. _questions-1:

Questions:
^^^^^^^^^^

-  How important is the value of the Run capacitor?
-  What happens if the value is off from the ideal value, too high or too low?

Directions: 12 V motors
-----------------------

**Stepper Motor Specifications**

For this 12 V example setup a MITSUMI M35SP-5 stepping motors is used (just the 12 V version of the 5 V motor used above). The specifications are listed below. Other motors from different manufacturers with similar specifications can be just as easily substituted.

-  Working Voltage: DC 12V
-  Rated Current/Phase 450 max.
-  Coil DC Resistance 95 Ω/phase
-  Phase Inductance: 64 mH

Stepper motors specified for 12 Volt or higher operation cannot be driven directly from the M1k SMU channels. An AC to AC step-down transformer can be used as shown in figure 9 to provide a suitable 60 Hz voltage level to drive the motor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-ac-sync-motor-fig-9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 9, Using step-down transformer to drive motor.


Four clamp diodes are used to insure there is a path for the coil current when the M1k SMU channels are off i.e. in a High Z state while the ALICE software is not taking measurements. Other than that the measured waveforms are much the same. The SMU outputs are set to DC 2.5 V to act as amp meters referenced to the same 2.5 V DC value as the common side of the transformer output. Because the current is now measured at the opposite end of the coils from where the voltage is being measured the current waveforms will be inverted. This can be corrected by setting the current channel gains to -1.0 rather than 1.0.

To measure the coil voltages, which will be greater than the 0 to 5 V input range of the M1k, 11:1 voltage dividers are used between the coils and the Split I/O inputs of M1k. The resistor divider values shown are just suggested values and just about any combination of resistors that provides enough reduction in the voltage to fit within the M1k input range is possible. Refer to this tutorial on how to calibrate external voltage dividers: :doc:`Measuring voltages beyond 0 to 5V with the ADALM1000 (M1K) </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>`.

Appendix: Other Common Motors
-----------------------------

These lowest cost "hobbyist" small 5V gear reduction stepper motors are the most commonly available from electronic distributors on the web:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/gear-reduction-stepper.png
   :align: center
   :width: 300px

.. container:: centeralign

   Gear reduction stepper motor.


They can have either 16:1 or 64:1 gear reduction so the output shaft will rotate very slowly when driven by moderate frequency sine sources like 60 Hz.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/gear-stepper-inside.png
   :align: center
   :width: 300px

.. container:: centeralign

   Inside gear reduction motor.


The gear reduction should not change the voltage and current waveforms so these motors could be used to demonstrate these same properties of AC induction motors.

**For Further Reading:**

| `AC Motors <https://en.wikipedia.org/wiki/AC_motor>`_
| `Synchronous Motors <https://en.wikipedia.org/wiki/Synchronous_motor>`_
| ` <https://www.allaboutcircuits.com/textbook/alternating-current/chpt-13/synchronous-motors/>`__

**Return to Lab Activity Table of Contents**
