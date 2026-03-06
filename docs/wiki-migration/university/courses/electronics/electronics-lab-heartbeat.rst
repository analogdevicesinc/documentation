Activity: Heartbeat Measurement Circuit
=======================================

Objective
---------

The objective of this Lab activity is to learn how to use a chain of amplifiers for gain and filtering, in a practical example, that aims to recover heartbeat information. The result of the system provides an relevant output that is displayed using the Scopy tool.

Going through this lab activity, the students will learn how to drive a IR LED and a Phototransistor, will be able to design and understand the behavior of a low-pass filter and explore functionalities provided by the operational amplifiers in different configurations.

Combining the previously mentioned electronic devices, the result of the activity will demonstrate how a real world application can be implemented with minimum software and hardware equipment.

Background
----------

A type of Heartbeat Measurement Device consists of an electronic circuit that monitors heartbeat by clipping onto a finger tip. It does this by shining light through your finger and measuring how much light is absorbed. This goes up and down as blood is pumped through your finger. For the operation as a optical heartbeat detector, a pair of IR LED and Phototransistor is used. The LED emits light through the finger and is detected by the phototransistor, which acts like a variable resistor conducting different amounts of current depending on the light received.

The voltage variations change with the heartbeat and are acquired from the collector of the phototransistor. The small signal obtained is used as input for the circuit, obtaining the behavior of a heartbeat detector.

In order to have a relevant output, the input signal is passed through multiple circuits:

::

   *Preamplifier - the output signal from the heartbeat measurement setup is decoupled through the series capacitor and amplified using a negative feedback resistor(R4).
   *Low-Pass Filter - RC filter that cuts the high frequencies (noise).
   *[[/university/courses/electronics/electronics-lab-1|Voltage Follower]] - buffers the output of the low-pass filter and reproduces its voltage with a low impedance output;
   *[[/university/courses/electronics/electronics-lab-1|Inverting Amplifier]] with Low-Pass Filter - amplifies the voltage signal and cuts the high frequencies (noise);

Materials
---------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - OP484 precision rail-to-rail I/O op amp
| 1 - 100Ω resistor
| 1 - 470Ω resistor
| 1 - 1KΩ resistor
| 1 - 10KΩ resistor
| 2 - 47KΩ resistor
| 2 - 1uF capacitor
| 1 - 47uF capacitor
| 1 - Infrared LED ( QED-123 )
| 1 - Infrared Transistor ( QSD-123)

Directions
----------

On your solder-less breadboard construct the heartbeat measurement circuit (designed in LTspice) as shown in Figure 1.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/heartbeat_measurement.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure 1 Heartbeat Measurement Circuit


The LTspice simulation uses OP284s, included in the standard set of LTspice models. The actual circuit is constructed with the quad OP484FPZ from the ADALP2000 Analog Parts Kit, powered by ± 5V from the ADALM2000 module (a total supply voltage of 10V.)

IR LED
~~~~~~

In order to have a proper current that will not damage the IR LED, a resistor needs to be added in series to limit the current. Varying the value between in the operating range will change the intensity of the emmited signal of the IR LED. The following formula expresses the value of the forward current (I\ :sub:`F`) through the LED, based on the positive voltage supply +5V (V\ :sub:`P`), series resistance (R\ :sub:`1`) and forward voltage drop on the LED (V\ :sub:`F`):

.. container:: centeralign

   :math:`I_F=V_P-V_F/R_1`


Phototransistor
~~~~~~~~~~~~~~~

To acquire information from the phototransistor (Q\ :sub:`1`) when is in contact with the IR light, a common-emmiter amplifier circuit is designed. This circuit generates an output which transitions from a high state to a low state when light in the infrared range is detected by the phototransistor. The output is created by connecting a resistor (R\ :sub:`2`), whose value was determined experimentally, between the voltage supply and the collector pin of the component.

Preamplifier
~~~~~~~~~~~~

The input signal from the heartbeat measurement setup is fed into a Differentiator Amplifier Circuit [1]_ (C\ :sub:`1`, A\ :sub:`1`, R\ :sub:`3`). The capacitor blocks any DC content, C\ :sub:`1` and R\ :sub:`3` behaving as a high pass filter with the cut-off frequency F\ :sub:`c1` being determined by the following formula:

.. container:: centeralign

   :math:`\displaystyle F_c1=\frac{1}{2} \pi R_3C_1`


Besides filtering, this stage serves also as an amplifier taking as input the current (I\ :sub:`A1`), and generating at the output an inverted voltage (V\ :sub:`A1`) based on the negative feedback resistance (R\ :sub:`3`):

.. container:: centeralign

   :math:`V_A1=-I_A1 \times R_3`


Active Low-Pass Filter
~~~~~~~~~~~~~~~~~~~~~~

Active Filters contain active components such as operational amplifiers, within their circuit design. They draw their power from an external power source and use it to boost or amplify the output signal. Active Low-Pass Filter [2]_ principle of operation and frequency response is the same as of a simple RC Low-Pass Filter, the only difference being that that it uses an op-amp for amplification and gain control.

This first-order low pass active filter (A\ :sub:`2`, R\ :sub:`4`, C\ :sub:`2`), consists simply of a passive RC filter stage providing a low frequency path to the input of a non-inverting operational amplifier.

The filter has the aim to cut the high frequencies that correspond to the noise signal. Taking into account that the heartrate does not exceed a value of 180 beats pe minute (bpm) and the dependecy between the bpm and the frequency is:

.. container:: centeralign

   :math:`bpm = frequency(Hz) \times 60`


will result that frequencies that are higher than 3Hz should be cut. The RC Low-Pass Filter is designed for the mentioned frequency value using the formula:

.. container:: centeralign

   :math:`\displaystyle F_c2=\frac{1}{2} \pi R_4C_2`


The amplifier is configured as a voltage-follower (Buffer) giving it a DC gain of one, A\ :sub:`V` = +1.

The advantage of this configuration is that the op-amps high input impedance prevents excessive loading on the filters output while its low output impedance prevents the filters cut-off frequency point from being affected by changes in the impedance of the load. While this configuration provides good stability to the filter, its main disadvantage is that it has no voltage gain above one. However, although the voltage gain is unity the power gain is very high as its output impedance is much lower than its input impedance.

Final Amplifier with Low-Pass Filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The configuration of the final stage represents a AC Op-amp Integrator with DC Gain Control [3]_. In simpler words, the circuit has the aim to low-pass filter (R\ :sub:`4`, C\ :sub:`2`) the signal from the remaining unnecessary frequencies that are higher than the maximum frequency of the heartbeat and amplify through the inverting amplifier the useful signal with a gain (A\ :sub:`V`)determined by ratio between R\ :sub:`6` and R\ :sub:`5`:

.. container:: centeralign

   :math:`A_V=-R_6/R_5`


.. container:: centeralign

   :math:`\displaystyle F_c3=\frac{1}{2} \pi R_6C_3`


Simulation
----------

Considering the circuit designed in LTspice, two types of simulation are made:

::

   *Transient - Connect at the input of the circuit a waveform generation source. Configure the source to generate a sine with amplitude of 500uV, frequency 2Hz and 500mV offset. Observe the output signal amplitude in order to determine graphically the total gain of the circuit(Figure 2).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/heartbeat-graph-tr.png

.. container:: centeralign

   Figure 2 Output Voltage - Transient Analysis


::

   *AC Sweep - Connect at the input of the circuit a AC Source. Configure the source to have a magnitude of 500uV. Observe the output signal in a chosen frequency domain (100mHz - 1kHz) in order to determine graphically in which frequency range the output signal has the biggest amplification (Figure 3).


   |image1|

.. container:: centeralign

   Figure 3 Output Voltage - AC Sweep


Hardware Setup
--------------

Use the variable positive and negative power supply from the ADALM2000 module set to 5 V to power your circuit. Use scope channel 1 to monitor the voltage at the collector node of V\ :sub:`out`.

The circuit implemented on the breadboard should look similar to the one in Figure 4. The blue LED represents the IR LED, and the grey one represents the Phototransistor.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/heartbeat-bb.png
   :align: right

.. container:: centeralign

   Figure 4 Breadboard Heartbeat Measurement Circuit


Procedure
---------

| Put the top of your finger between the IR LED(D1) and the Phototransistor(Q1). The emitter and the receiver should be alligned and pointing one to another.
| Observe the voltage waveform seen at the the output of the 3rd stage op amp (A\ :sub:`3`). An example of output waveform is presented in Figure 5.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/heartbeat-waveform.png

.. container:: centeralign

   Figure 5 Heartbeat Output Waveform


In the Oscilloscope feature of the Scopy tool activate the measure feature in order to read the frequency of the obtained signal. To convert the frequency into beats per minute(bpm) use the formula from laboratory directions.

Questions
---------

1. Using the values and formulas provided in the laboratory directions compute the following parameters:

::

   *Forward current through the IR LED. (use datasheet of the QED-123)
   *Cut-off frequency of the high-pass filter.
   *Cut-off frequency of the second stage low-pass filter.
   *Cut-off frequency of the third stage low-pass filter.
   *Gain of the third stage amplifier

2. Using the oscilloscope, capture the voltage signal at the output of the first stage and try to compute the amplitude of the input current.

3. What role has the buffer in the second stage?

4. What parameters change if R\ :sub:`5` is modified? How will the signal look on the Oscilloscope?

5. What parameters change if R\ :sub:`6` is modified? How will the signal look on the Oscilloscope?

6. On the Heartbeat Output Waveform the signal is not centered on 0V, even though the DC component should have been removed. Why is this happening? What should be added at the output of the circuit to reduce the offset?


| 
|

.. admonition:: Download
   :class: download

   \*\* Lab Resources:\*\*

   
   -  LTSpice files: :git-education_tools:`m2k/ltspice/heartbeat_ltspice`
   -  Fritzing files: :git-education_tools:`m2k/fritzing/heartbeat_bb`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**

.. [1]
   `Differentiator Amplifier <http://www.electronics-tutorials.ws/opamp/opamp_7.html>`__

.. [2]
   `Active Low-Pass Filter <http://www.electronics-tutorials.ws/filter/filter_5.html>`__

.. [3]
   `AC Op-amp Integrator with DC Gain Control <http://www.electronics-tutorials.ws/opamp/opamp_6.html>`__

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/heartbeat-graph-ac.png
