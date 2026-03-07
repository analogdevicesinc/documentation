Activity: Band-Pass Filter Step Response
========================================

Objective:
----------

The objective of this activity is to simulate, measure and analyze the time-domain step response of a simple first order Band-pass filter.  

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current  / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V, CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.  

Introduction
------------

One, perhaps obvious, way to build a band-pass filter is to cascade a low-pass filter section followed by a high-pass filter. A unity gain buffer is used between the low-pass and high-pass filter sections. This band-pass filter is intended to pass the frequencies between the low-pass and high-pass filter's cutoff frequencies. In this activity you will measure the time-domain step response of this filter.

Activity Objectives
~~~~~~~~~~~~~~~~~~~

A square wave, will be applied to a two section band-pass filter. The first section is a high-pass filter consisting of C\ :sub:`1` and R\ :sub:`1`. The second section is a low-pass filter consisting of C\ :sub:`2` and R\ :sub:`2`. The time-domain unit step response will be measured for the over-all high-pass filter at Vlp.

The waveform, Vhp, is applied to the low-pass filter through an op-amp “buffer”. The buffer has a gain of “1” (output is exactly equal to the input). The buffer has very high input impedance so that it does not affect or load the high-pass filter section. The buffer also has very low output impedance so that it acts las a voltage source to drive the low-pass filter section. This allows us to calculate the transfer function of each filter independently. You will compare your measurement results to hand calculations and LTSpice simulation.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solderless Breadboard
| 1 - 2 KΩ resistor (made from 2 1 KΩ in series)
| 1 – 4.7 KΩ resistor
| 1 – AD8542 dual op-amp
| 2 - 0.1 µF capacitors

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-bp-step-lab-fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Band-Pass Filter schematic


Procedure:
~~~~~~~~~~

1. Using the ALICE Ohmmeter tool and Impedance Analyzer tool measure and confirm the values of the components you are using.

R\ :sub:`1` \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ R\ :sub:`2` \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ C\ :sub:`1` \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ C\ :sub:`2` \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2. Build the circuit in figure 1 on your solderless breadboard. Channel A AWG generator is set in SVMI mode to produce a 200 Hz, 1 V peak-to-peak, square wave, centered around 2.5 V.

3. Connect channel B in Hi-Z mode alternately to nodes Vhp, Vbuff and Vlp.

4. Set time base to 0.5 mS per division, trigger to CA-V, rising edge. Observe the CA-V trace and carefully adjust AWG A frequency and amplitude. You should observe exactly one cycle of the waveform.

5. Observe CB-V (Vhp). You should see a waveform similar to the figure 2 graph on the left. Measure and record the time constant, T, of the response by measuring as accurately as possible the time it takes for the waveform's amplitude to decay to exactly 2.868 V ( 0.368 V greater than the 2.5 V baseline).

The reciprocal of the time constant T is the decay rate, α, of the exponential response.

T \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ α \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-bp-step-lab-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2


7. The signal Vbuff is the input to the low pass filter. Verify that the signal at the input of the low-pass filter is exactly the same as the signal Vhp by moving the channel B scope input to pin 1, Vbuff, of the op-amp. Now move the channel B scope input to display Vlp. You should observe a waveform similar to the graph above on the right.

8. Set the time base to 0.2 mS per division and channel B vertical input to measure the signal amplitude as accurately as possible. Measure and record the amplitude, V\ :sub:`P`, and the time of occurrence, t\ :sub:`P`, of the positive peak.

V\ :sub:`P` \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ t\ :sub:`P` \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If you are recording the measurements from the screen, try setting the zero reference to the bottom of the screen and set volts per division for a largest display. Using the time and voltage cursors can be helpful.

The objective is to record the response at the output of the low-pass filter as accurately as possible for comparison to theoretical expectation. Only the positive response will be analyzed.

Analysis
--------

1. Simulate the band-pass filter circuit using transient analysis. Be sure to use the measured values of your components in the simulation.

2. Compare the following measured results with the simulated results:

   a) Amplitude and decay rate of the exponential waveform Vhp.
   > b) Amplitude and time of occurrence of the positive peak of the response at Vlp.
   > c) Express the percent error of the measurements of (a) and (b) above compared to the simulated results.

LTspice Example: Band-Pass Filter Pulse response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This LTSpice simulation uses the AD8542 model from the opamp library. It is easy to use and requires power supply connections.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-bp-step-lab-spice-fig.png
   :align: center
   :width: 600px

.. container:: centeralign

   LTSpice simulation schematic


The source Vpulse is set to produce a 2 mS pulse with a repetition rate of 4 mS.

The high-pass and overall band-pass filter's pulse response is plotted below in figure 3. Note that the 2 millisecond pulse width allows the filter's response to return to steady state in between each pulse.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-bp-step-lab-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3


**For Further Reading:**

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-signals-labs-list>`\ **.**
