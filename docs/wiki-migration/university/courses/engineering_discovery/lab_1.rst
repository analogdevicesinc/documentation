Introduction to Electronic Components and Equipment
===================================================

.. image:: https://wiki.analog.com/_media/analogTV>4800534507001
   :alt: analogTV>4800534507001
   :align: right

Introduction
------------

Today’s electronic devices are made up of a wide variety of components. Some, like resistors and capacitors, are simple and passive, while others, such as advanced central processing unit (CPU) chips, are extremely complex and can contain over 20 billion transistors. In this lab, we introduce some simple components and some equipment that can be used to generate and characterize electronic signals in the forms of voltages and currents.

Objective
---------

To introduce resistors, capacitors and inductors as examples of passive components. To introduce diodes and transistors as simple semiconductor components, and an operational amplifier (op-amp) as an example of an integrated circuit (IC). To introduce the Analog Devices M1K and PixelPulse2 application software. Following completion of this lab you should be familiar with the parts in the :doc:`ADALP2000 Analog Parts Kit </wiki-migration/university/tools/adalp2000/parts-index>`, be able to give basic descriptions of passive components, diodes, transistors, and op-amps, understand the basics of resistor and capacitor codes, and understand the basic operation of the M1K and PixelPulse application software.

Materials and Apparatus
-----------------------

-  Resistor and capacitor code handouts
-  Computer running PixelPulse software
-  Analog Devices ADALM1000 (M1K)
-  :doc:`Solderless breadboard </wiki-migration/university/courses/electronics/electronics-lab-breadboards>` and jumper wires from the ADALP2000 Analog Parts Kit
-  Resistors from the ADALP2000 Analog Parts Kit
-  Capacitors from the ADALP2000 Analog Parts Kit
-  Inductors from the ADALP2000 Analog Parts Kit
-  Diodes from the ADALP2000 Analog Parts Kit
-  2N3904 transistor from the ADALP2000 Analog Parts Kit
-  OP484 quad op-amp from the ADALP2000 Analog Parts Kit

Procedure to set up ALM1000 hardware and software
-------------------------------------------------

-  Turn on the computer and download PixelPulse
-  Run PixelPulse and plug in the M1K using the supplied USB cable
-  Update M1K firmware, if necessary
-  Activate the M1K source/measurement traces using the arrow button
-  Observe basic M1K functions: Measure Voltage, Source Voltage/Measure Current, Source Current/Measure Voltage
-  Set up the M1K to source voltage/measure current on Channel A and measure voltage on channel B and connect Channel A to Channel B using a wire from the kit
-  Set up Channel A source waveform for a sine wave
-  Observe the sine wave voltage on Channel B
-  Observe all available waveforms by selecting each one on Channel A and observing them on Channel B

Introduction to the components in ADALP2000 Kit
-----------------------------------------------

A detailed list of the contents of the ADALP2000 Analog Parts Kit can be found :doc:`here </wiki-migration/university/tools/adalp2000/parts-index>`.

-  Identify the following resistors in the kit by using the :doc:`resistor color code </wiki-migration/university/courses/electronics/electronics-lab-resistors>`: 68 Ω, 100 Ω, 470 Ω, 2.2 KΩ, 5 MΩ
-  Identify the following capacitors in the kit by using the :doc:`capacitor codes </wiki-migration/university/courses/electronics/electronics-lab-capacitors>`: 39 pF, 0.047 μF, 10 μF, 220 μF
-  Identify the following inductors in the kit: 1.0 μH, 10 μH, 100 μH
-  Identify the LED's, 1N914 and 1N4001 diodes in the kit
-  Identify the 2N3904 transistor in the kit
-  Identify the OP484,OP482,OP37G op-amp IC in the kit
-  Identify the audio jack port,micro USB port,Speaker.

Theory
------

The components introduced in this lab will be used in the following labs to construct circuits that increase in complexity as the labs go on. The first of the subsequent labs uses two of the passive elements – resistors and capacitors – in ways that help illustrate how these elements behave in circuits.

Resistors (R) have the units of ohms (Ω), and control the instantaneous relationship between voltage (V) and current (I) according to Ohm’s law, V = I\*R. Capacitors store electric charge, allow more current to flow as the signal frequency increases, and exhibit a phase shift between voltage and current in which the sinusoidal current leads the voltage by 90 degrees, or equivalently, the sinusoidal voltage lags the current by 90 degrees. Inductors behave in an opposite fashion. Inductors store energy in a magnetic field, allow less current to flow as the signal frequency increases, and exhibit a phase shift between voltage and current in which the sinusoidal voltage leads the current by 90 degrees, or equivalently, the sinusoidal current lags the voltage by 90 degrees. Resistors, capacitors, and inductors do not add any energy to a circuit, and therefore cannot be used to amplify the power of a signal.

Diodes are the simplest of semiconductor devices and allow current flow in only one direction. The original diodes were electronic tubes, constructed of a filament that emitted electrons and a metal plate that collected the electrons. In these diodes, the electrons can only flow from the filament to the plate when the plate is biased at a positive voltage that attracts the negatively-charged electrons. Modern diodes use a semiconductor ‘pn junction” to obtain the same result. Diodes are often used as switches, and to convert alternating current (AC) to direct current (DC).

Transistors have three terminals in most cases, and are the simplest semiconductor devices that are capable of amplifying the power of a signal. This is accomplished by applying the signal to be amplified to the transistor input terminal, and using the input signal to control the power from an external power supply according to the input signal. The signal with increased power is available at the output terminal. The transistor output is therefore a replica of the input signal with increased voltage amplitude, current amplitude, or both. The third terminal is generally connected to a reference voltage.

Op-amps are examples of ICs that are most often used in negative feedback configurations to provide signal amplification that is of better quality than can be obtained with a single transistor. In the fourth lab, an op-amp is combined with a 2N3904 transistor to provide signal voltage amplification and current amplification to drive a loudspeaker. The op-amp provides the voltage gain and the transistor, placed inside the negative feedback loop to provide the best performance, provides the current gain.

Observations and Conclusions
----------------------------

-  Resistors, capacitors, and inductors are simple passive circuit elements that can be used to process signals with regard to amplitude and frequency response. They cannot amplify the power of a signal.
-  Diodes can be used as simple electronic switches, and are often used in the conversion of AC power to DC power.
-  Transistors are the simplest electronic devices that are capable of amplifying signal power
-  Op-amps are ICs that are normally operated in negative feedback configurations, and are often used to amplify signals at a better quality level than that available with a simple transistor

**Return to** :doc:`Engineering Discovery Index </wiki-migration/university/courses/engineering_discovery>`
