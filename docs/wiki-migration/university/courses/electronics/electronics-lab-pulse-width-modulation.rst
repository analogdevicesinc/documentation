Activity: Pulse Width Modulation
================================

Objective
---------

In this laboratory we examine pulse width modulation and its usage within a variety of applications.

Pulse Width Modulation (PWM) is a method for encoding an analog signal into a single digital bit. A PWM signal consists of two main components that define its behavior: a duty cycle and a frequency.

It is used in transmission of information by encoding a message into a pulsing signal, also for power control of electronic devices such as motors and as principal algorithm for photo-voltaic solar battery chargers.

The *duty cycle* describes the amount of time the signal is in a high (on) state as a percentage of the total time of it takes to complete one cycle.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/pwm-signal.png
   :width: 500px

The following diagram shows pulse trains at 0%, 25%, and 100% duty cycle.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/pwm-duty.png
   :width: 500px

The *frequency* determines how fast the PWM completes a cycle, and therefore how fast it switches between high and low states.

By varying a digital signal off and on at a fast-enough rate, and with a certain duty cycle, the output will appear to behave like a constant voltage analog signal when providing power to devices that respond much slower than the PWM frequency, such as audio speakers, electric motors, and solenoid actuators.

Materials
---------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 OP97 operational amplifier
| 1 1kΩ resistor 1 10kΩ potentiometer

Pulse Width Modulator - Principle of operation
----------------------------------------------

Pulse Width Modulation (PWM) is a technique to generate low frequency output signals from high frequency pulses. Rapidly switching the output voltage of an inverter leg between the upper and lower DC rail voltages, the low frequency output can be thought of as the average of voltage over a switching period.

Besides that, there are also other several ways of generating pulse-width modulated signals, including analog techniques, sigma-delta modulation, and direct digital synthesis.

One of the simplest methods of generating a PWM signal is to compare two control signals, a carrier signal and a modulation signal. This is known as carrier-based PWM. The carrier signal is a high frequency (switching frequency) triangular waveform. The modulation signal can be any shape.

Using this approach, the output waveform can be a PWM representation of any desired waveform shape. With machines, sinusoidal and trapezoidal waveform shapes are among the most common.

Consider the circuit in Figure 1.

.. container:: centeralign


|image1|

.. container:: centeralign

   Figure 1. PWM Principle of operation


Following the description of the PWM principle, we use the negative input of the operational amplifier for carrier, while the positive input for the modulation signal. Thus, a higher modulation signal will result in an output that is at a high level for a greater fraction of the PWM period.

Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard circuit for Pulse Width Modulation.

.. container:: centeralign


|image2|

.. container:: centeralign

   Figure 2. PWM Principle of operation - breadboard circuit


Procedure
~~~~~~~~~

Use the first waveform generator as the carrier signal providing a 4V amplitude peak-to-peak, 2.5V offset, 1 kHz triangle wave excitation to the circuit. Use the second waveform generator as the modulation signal with 3V amplitude peak-to-peak, 2.5V offset, 50Hz sine wave.

Supply the op amp with +5V from the power supply. Configure the scope so that the input signal is displayed on channel 1 and the output signal is displayed on channel 2 .

In the figure there are presented the two signal generator channels containing the two input signals (orange - carrier signal, purple - modulation signal).

.. container:: centeralign


|image3|

.. container:: centeralign

   Figure 3. Input Signals


A plot of the output signal on channel 2 of the scope is presented in Figure 4.

.. container:: centeralign


|image4|

.. container:: centeralign

   Figure 4. PWM output


If the instantaneous magnitude of the modulation signal is greater than the carrier signal at a point in time, the output will be high. If the modulation signal is lower than the carrier signal, the output will be low.

If the peak of the modulation is less than the peak of the carrier signal, the output will be a faithful PWM representation of the modulation signal. Edit

Pulse Width Control using a DC modulation Voltage
-------------------------------------------------

Background
~~~~~~~~~~

For this particular application we will use a simple operational amplifier in a switching mode configuration (see :doc:`Activity: Op Amp as Comparator </wiki-migration/university/courses/electronics/electronics-lab-opamp-comparator>` for further details) to demonstrate pulse-width modulation of a DC voltage.

Consider the circuit in Figure 5.

.. container:: centeralign


|image5|

.. container:: centeralign

   Figure 5. Pulse Width Control using a DC modulation Voltage


The circuit works as a simple comparator where the negative input of the operational amplifier is connected to the carrier waveform, while the positive input acts as a threshold voltage which establishes when the transitions between high voltage output and low voltage output occur. The potentiometer acts as a voltage divider for the input reference voltage, adjusting the threshold voltage, and implicitly the duty cycle of the output signal.

.. _hardware-setup-1:

Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard circuit for Pulse Width Control using a DC modulation Voltage.

.. container:: centeralign


|image6|

.. container:: centeralign

   Figure 6. Pulse Width Control using a DC modulation Voltage - Breadboard circuit


.. _procedure-1:

Procedure
~~~~~~~~~

Use the first waveform generator as source Vin to provide a 5V amplitude peak-to-peak, 1 kHz triangle wave excitation to the circuit. Use the second waveform generator as constant voltage source with 5V amplitude peak-to-peak. Supply the op amp to +5V from the power supply. Configure the scope so that the input signal is displayed on channel 1 and the output signal is displayed on channel 2.

An animated plot is presented in Figure 7.

.. container:: centeralign


|image7|

.. container:: centeralign

   Figure 7. Pulse Width Control using a DC modulation Voltage - waveforms


The output signal is a PWM representation of the input voltage. Notice that, by varying the potentiometer value, the duty cycle of the signal changes, while the frequency remains constant.

Fixed 50% PWM with Astable Multivibrator
----------------------------------------

.. _background-1:

Background
~~~~~~~~~~

Consider the circuit in Figure 8.

.. container:: centeralign


|image8|

.. container:: centeralign

   Figure 8. PWM with Astable Multivibrator


The circuit shows an astable multivibrator using a single operational amplifier. The functionality is easy to understand while considering the functional principle of a Schmitt trigger (comparator circuit with hysteresis studied in :doc:`Activity: Op Amp as Comparator </wiki-migration/university/courses/electronics/electronics-lab-opamp-comparator>`): The input of the Schmitt trigger, which is identical to the inverting input of the operational amplifier, is connected to the output of the circuit via a resistor-capacitor network. While the capacitor voltage (which is also the input of the Schmitt trigger) is lower than the lower threshold, the output voltage equals the positive supply voltage of the circuit. Now the capacitor is charged via the resistor R\ :sub:`3`, until the upper threshold of the Schmitt trigger is reached. As a result, the output voltage of the operational amplifier is driven to the negative supply voltage. Now the capacitor is discharged via R\ :sub:`3`, until the voltage across those device reaches the lower threshold of the Schmitt trigger. The output voltage of the operational amplifier is driven to the positive supply voltage and the whole process starts again.

The advantage of this circuit is that it does not require an M2K to generate a carrier (but the duty cycle is fixed at 50%.)

.. _hardware-setup-2:

Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard circuit for PWM with Astable Multivibrator.

.. container:: centeralign


|image9|

.. container:: centeralign

   Figure 9. PWM with Astable Multivibrator Breadboard Circuit


.. _procedure-2:

Procedure
~~~~~~~~~

Supply the circuit to +/-5V from the power supply. Configure the scope so that the output signal is displayed on channel 1.

A plot with the output signal on channel 1 of the scope is presented in Figure 10.

.. container:: centeralign


|image10|

.. container:: centeralign

   Figure 10. PWM with Astable Multivibrator output waveform


Note that the duty cycle of the output signal is approximately around 50% while the low/high voltage values tend to reach the positive/negative supply values.

Extra Activity
--------------

In the previous example we generated a 50% fixed duty cycle PWM using astable multivibrators. But how can we adjust the duty cycle? For this we will need to alter the circuit slightly.

Consider the circuit presented in Figure 11.

.. container:: centeralign


|image11|

.. container:: centeralign

   Figure 11. Adjusting the duty cycle for PWM with Multivibrator


The resistor R\ :sub:`3` in Figure 8 was replaced by a potentiometer and two diodes were inserted. Now the charging current of the capacitor is running through D\ :sub:`1`, while the discharging current is running through D\ :sub:`2`. Depending on the adjustment of the potentiometer VR\ :sub:`1`, the resistance of the charging current - running through the upper branch of the circuit - is different from that of the discharging current - running through the lower branch.

.. _hardware-setup-3:

Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard circuit for adjusting the duty cycle for PWM with Multivibrators.

.. container:: centeralign


|image12|

.. container:: centeralign

   Figure 12. Adjusting duty cycle for PWM with Multivibrator Breadboard Circuit


.. _procedure-3:

Procedure
~~~~~~~~~

Supply the circuit to +/-5V from the power supply. Configure the scope so that the output signal is displayed on channel 1 and the voltage on the capacitor (at the negative input of the op amp) is displayed on channel 2.

Vary the potentiometer value and notice the duty cycle change. A plot example is presented in Figure 13.

.. container:: centeralign


|image13|

.. container:: centeralign

   Figure 13. Adjusting duty cycle for PWM with Astable Multivibrator waveforms


In this example the duty cycle was set to around 25%. Whenever the duty cycle is altered, there is inevitably a slight variation in the switching frequency, because the two coupling networks at the inverting and non-inverting input are both connected to the output of the operational amplifier.

Going Further with the Lab
--------------------------

All the activities in this laboratory are based on a simple op-amp (OP97) configured as comparator. The ADALP2000 Parts Kit contains also the comparator AD8561, designed for this single purpose. Therefore, the performance of the PWM circuits might be increased by using this part.

Build the above discussed circuits using AD8561 from the Parts Kit and discuss any noticeable changes of the circuit behavior and the input/output signals.

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/pwm_lab_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/pwm_lab_ltspice`
   


Further Reading
---------------

Some additional resources:

-  `Pulse-width modulation <https://en.wikipedia.org/wiki/Pulse-width_modulation>`__
-  :doc:`Activity: Pulse Width Modulation </wiki-migration/university/courses/alm1k/alm-lab-pwm>`
-  :adi:`Why and How to Control Fan Speed for Cooling Electronic Equipment <en/analog-dialogue/articles/how-to-control-fan-speed.html>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/pwm_carrier.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/pwm_carrier-bb.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/pwm-input.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/pwm-wav.png
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/pwm_dc_modulation1_ltspice.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/pwm_ref_voltage-bb.png
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/pwm_ref_voltage-wav.gif
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/pwm_astable_multivibr.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/pwm_multivibr-bb.png
.. |image10| image:: https://wiki.analog.com/_media/university/courses/electronics/pwm_multivibr-wav.png
.. |image11| image:: https://wiki.analog.com/_media/university/courses/electronics/pwm_dc_multivibr.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/university/courses/electronics/pwm_dc_multivibr-bb.png
.. |image13| image:: https://wiki.analog.com/_media/university/courses/electronics/pwm_dc_multivibr-wav.png
