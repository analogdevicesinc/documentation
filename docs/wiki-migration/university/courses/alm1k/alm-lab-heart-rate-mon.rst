Activity: Heart Rate Monitor Circuit
====================================

Objective
---------

The objective of this Lab activity is to learn how to implement a series of amplifiers for signal amplifiaction and filtering, in a practical example, that aims to monitor heartbeat information. The result of the system provides a relevant output that is displayed using the ALM1000 tool.

Going through this lab activity, the students will learn how to drive a IR LED and a Phototransistor, will be able to design and understand the behavior of low-pass and high-pass filters and explore functionalities provided by the operational amplifiers in different configurations.

Combining the previously mentioned electronic devices, the result of the activity will demonstrate how a real world application can be implemented with minimum software and hardware equipment.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background
----------

A type of Heart Rate Monitor consists of an electronic circuit that monitors heartbeat by clipping onto a finger tip. It does this by shining light into or through your finger and measuring how much light is reflected or absorbed. This goes up and down as blood is pumped through your finger. For the operation as a optical heartbeat detector, a combination of an Infrared LED and Photo transistor is used. The LED emits light into or through the finger and the reflected or transmitted light is detected by the photo transistor, which acts like a variable current source conducting different amounts of current depending on the light received.

The voltage variations change with the heartbeat and are acquired from the collector of the photo transistor. The small signal obtained is used as input for the following circuit, providing an output signal as a heartbeat detector or monitor.

In order to have a relevant output, the input signal is passed through multiple circuits:

::

   *Preamplifier - the output signal from the heartbeat measurement setup is decoupled through the series capacitor and amplified using a negative feedback resistor(R4).
   *Low-Pass Filter - RC filter that cuts the high frequencies (noise).
   *[[/university/courses/alm1k/alm-lab-1|Voltage Follower]] - buffers the output of the low-pass filter and reproduces its voltage with a low impedance output;
   *[[/university/courses/alm1k/alm-lab-1|Inverting Amplifier]] with Low-Pass Filter - amplifies the voltage signal and cuts the high frequencies (noise);

Materials
---------

Select the following components from the ADALP2000 Analog Parts Kit. Note, the parts kit contains both OP-482 and OP-484 quad op-amps. They look very similar and are both in 14 pin DIP packages. The laser branding on the packages can be hard to read. Fortunately they share a common pinout so you will not damage them if you use the wrong one in this experiment by accident. The circuit will just not operate properly.

There are two black plastic devices with two leads in the kit that look almost exactly the same. One is the photo transistor and the other is a photo diode. The one with the slightly shorter leads should be the photo transistor. If you have a DMM with a diode test function handy you can verify which is the photo diode and which is the photo transistor (the photo diode will conduct in one direction and the photo transistor will not conduct in either direction)

| ADALM1000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 1 - OP484 precision rail-to-rail I/O op amp (14 pin DIP package)
| |image1|

.. container:: centeralign

   **OP484 Quad op-amp**


| Resistors are marked with color bands like this:
| |image2|

| Find resistors with the following color bands:
| 1 - 100Ω resistor (brown black brown)
| 1 - 470Ω resistor (yellow purple brown)
| 1 - 1KΩ resistor (brown black red)
| 1 - 1.5KΩ resistor (brown green red)
| 1 - 10KΩ resistor (brown black orange)
| 1 - 20KΩ resistor (red black orange)
| 1 - 47KΩ resistor (yellow purple orange)
| 2 - 1uF capacitors
| |image3|

| 1 - 47uF capacitor
| |image4|

| 1 - Infrared LED (QED-123) the longer of the two leads is the anode (+) and the shorter lead is the cathode (-).
| |image5|

.. container:: centeralign

   **QED-123 Infrared LED**


| 1 - Infrared Transistor (QSD-123) the longer of the two leads is the collector and the shorter lead is the emitter.
| |image6|

.. container:: centeralign

   **QSD123 Infrared Transistor**


1 - Red LED



|image7|

Directions
----------

On your solder-less breadboard construct the heartbeat monitor circuit as shown in figure 1. The values shown for the gain setting resistors R\ :sub:`5` and R\ :sub:`6` are approximate and may need to be adjusted based on the response of the person who's heart rate is being monitored. Increasing or decreasing the ratio may be needed to obtain an optimal output signal amplitude that fits within the available 0 to 5V range.

The collector load resistor R\ :sub:`2` of the photo transistor can also be adjusted to optimally center the signal.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_fig1_heart-rate-mon.png
   :align: center
   :width: 750px

.. container:: centeralign

   Figure 1 Heartbeat Monitor Circuit


The circuit uses the OP484FPZ quad opamp from the ADALP2000 Analog Parts Kit, the schematic design was implemented with three of the Precision Rail-to-Rail Operational Amplifiers. They operate from a single supply (+5V) from the ADALM1000 module.

IR LED
~~~~~~

In order to supply a proper current that will not damage the IR LED, a resistor is added in series to limit the current. Varying the value in the operating range will change the intensity of the emmited light of the IR LED. The following formula expresses the value of the forward current (I\ :sub:`F`) through the LED, based on the positive voltage supply +5V (V\ :sub:`P`), series resistance (R\ :sub:`1`) and forward voltage drop on the LED (V\ :sub:`F`):

.. container:: centeralign

   :math:`I_F=V_P-V_F/R_1`


Phototransistor
~~~~~~~~~~~~~~~

To generate a voltage signal from the phototransistor (Q\ :sub:`1`) when ilumonated with the IR light from the LED, a common-emmiter amplifier circuit is used. This circuit generates an output which transitions from a high state to a low state when light in the infrared range is detected by the phototransistor. The output is created by connecting a resistor (R\ :sub:`2`), whose value is determined experimentally, between the voltage supply and the collector pin of the component.

Preamplifier
~~~~~~~~~~~~

The input signal from the heartbeat monitor sensor is fed into a Differentiator Amplifier or high pass filter Circuit [1]_ (C\ :sub:`1`, A\ :sub:`1`, R\ :sub:`3`). The capacitor blocks any DC content, C\ :sub:`1` and R\ :sub:`3` behaving as a high pass filter with the cut-off frequency F\ :sub:`c1` being determined by the following formula:

.. container:: centeralign

   :math:`\displaystyle F_c1=\frac{1}{2} \pi R_3C_1`


In addition to filtering, this stage serves also as an amplifier taking at the input the current (I\ :sub:`A1`), and generating at the output an inverted voltage (V\ :sub:`A1`) based on the negative feedback resistance (R\ :sub:`3`):

.. container:: centeralign

   :math:`V_A1=-I_A1 \times R_3`


Active Low-Pass Filter
~~~~~~~~~~~~~~~~~~~~~~

Active Filters contain active components such as operational amplifiers, within their circuit design. They draw their power from an external power source and use it to boost or amplify the output signal. Active Low-Pass Filter [2]_ principle of operation and frequency response is the same as of a simple RC Low-Pass Filter, the only difference being that that it uses an op-amp for amplification and gain control.

This first-order low pass active filter (A\ :sub:`2`, R\ :sub:`4`, C\ :sub:`2`), consists simply of a passive RC filter stage providing a low frequency path to the input of a non-inverting operational amplifier.

The filter has the aim to cut the high frequencies that correspond to the noise signal. Taking into account that the heart rate does not exceed a value of 180 beats per minute (bpm) and the dependency between the bpm and the frequency is:

.. container:: centeralign

   :math:`bpm = frequency(Hz) \times 60`


will result that frequencies that are higher than 3Hz should be filtered out. The RC Low-Pass Filter is designed for this frequency value using the formula:

.. container:: centeralign

   :math:`\displaystyle F_c2=\frac{1}{2} \pi R_4C_2`


The amplifier is configured as a voltage-follower (Buffer) giving it a DC gain of one, A\ :sub:`V` = +1.

The advantage of this configuration is that the op-amps high input impedance prevents excessive loading on the filters output while its low output impedance prevents the filters cut-off frequency point from being affected by changes in the impedance of the load.

While this configuration provides good stability to the filter, its main disadvantage is that it has no voltage gain above one. However, although the voltage gain is unity the power gain is very high as its output impedance is much lower than its input impedance.

Final Amplifier with Low-Pass Filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The configuration of the final stage represents a AC Op-amp Integrator with DC Gain Control  [3]_. In simpler words, the circuit has the aim to low-pass filter (R\ :sub:`4`, C\ :sub:`2`) the signal from the remaining unnecessary frequencies that are higher than the maximum frequency of the heartbeat and amplify through the inverting amplifier the useful signal with a gain (A\ :sub:`V`)determined by ratio between R\ :sub:`6` and R\ :sub:`5`:

.. container:: centeralign

   :math:`A_V=-R_6/R_5`


.. container:: centeralign

   :math:`\displaystyle F_c3=\frac{1}{2} \pi R_6C_3`


Simulation
----------

Considering the circuit designed in LTSpice or ADIsimPE, two types of simulation are performed:

::

   *Transient - Connect at the input of the circuit a waveform generation source. Configure the source to generate a sine with amplitude of 250uV, frequency 2Hz and 500mV offset. Observe the output signal amplitude in order to determine graphically the total gain of the circuit(Figure 2).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/heartbeat-graph-tr.png

.. container:: centeralign

   Figure 2 Output Voltage - Transient Analysis


::

   *AC Sweep - Connect at the input of the circuit a AC Source. Configure the source to have a magnitude of 250uV. Observe the output signal in a chosen frequency domain (100mHz - 1kHz) in order to determine graphically in which frequency range the output signal has the biggest amplification (Figure 3).


   |image8|

.. container:: centeralign

   Figure 3 Output Voltage - AC Sweep


Hardware Setup
--------------

Use the fixed positive power supply from the ADALM1000 module for the 5 V to power your circuit. Use scope channel A to monitor the voltage at the collector node of V\ :sub:`out`.

Procedure
---------

The Heart Rate monitor can operate in either of two modes. In the first mode, as shown on the left of figure 4, the light from the LED is reflected as it passes into the tip of the finger and bounces back into the photo transistor. Arrange the LED and photo transistor right next to each other both facing up. It might be useful to shorten the leads so that they sit against the breadboard surface. In the second mode, as shown on the right of figure 4, the light from the LED passes through the tip of the finger and into the photo transistor on the other side. Put the tip of your finger between the IR LED (D1) and the Photo transistor (Q1). The emitter and the receiver should be aligned and pointing one to another.


|image9|

.. container:: centeralign

   Figure 4 Two Modes


The red LED should blink on and off once per heart beat, about once per second.

Observe the voltage waveform seen at the the output of the 3rd stage op amp (A\ :sub:`3`). The signal is very slow, low frequency, and is best viewed using the Alice M1K Strip Chart tool. Start the Strip Chart and select CH-A on 1 grid, then hit Run. An example of the output waveform is shown in Figure 5.


|image10|

.. container:: centeralign

   Figure 5 Heartbeat Output Waveform


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

   
   -  **Heartbeat Monitor Resource Files**
   -  Download: `Circuit Schematic - ADIsim <https://wiki.analog.com/_media/university/courses/electronics/heartbeat-circuit-dl.zip>`__
   -  Download: `Breadboard Circuit - Fritzing <https://wiki.analog.com/_media/university/courses/electronics/heartbeat-bb-dl.zip>`__
   


**For further reading:**

| `Photoplethysmogram <https://en.wikipedia.org/wiki/Photoplethysmogram>`__
| `Heart rate monitor <https://en.wikipedia.org/wiki/Heart_rate_monitor>`__

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`\ **.**

.. [1]
   `Differentiator Amplifier <http://www.electronics-tutorials.ws/opamp/opamp_7.html>`__

.. [2]
   `Active Low-Pass Filter <http://www.electronics-tutorials.ws/filter/filter_5.html>`__

.. [3]
   `AC Op-amp Integrator with DC Gain Control <http://www.electronics-tutorials.ws/opamp/opamp_6.html>`__

.. |image1| image:: https://wiki.analog.com/_media/university/tools/adalp2000/op484.jpg
   :width: 250px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/adalp2000/20k.jpg
   :width: 250px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/alm1k/1uf.jpg
   :width: 250px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/alm1k/47uf.jpg
   :width: 250px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/a22_g1.jpg
   :width: 250px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/a22_g2.jpg
   :width: 250px
.. |image7| image:: https://wiki.analog.com/_media/university/tools/adalp2000/leds.jpg
   :width: 250px
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/heartbeat-graph-ac.png
.. |image9| image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab_heart-rate-mon-2modes.png
   :width: 500px
.. |image10| image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab_heart-rate-mon-wave.png
   :width: 750px
