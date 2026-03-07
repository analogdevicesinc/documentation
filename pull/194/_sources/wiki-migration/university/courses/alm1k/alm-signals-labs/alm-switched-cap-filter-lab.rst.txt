Activity: Switched Capacitor Filters
====================================

Objective:
----------

The objective of this Lab exercise is to explore the concepts of Switched Capacitor based filter circuits.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

A switched capacitor is an electronic circuit element used in discrete time signal processing systems. It works by transferring charge onto and off of a capacitor when switches are opened and closed. Usually, non-overlapping signals are used to control the switches, often termed Break before Make switching, so that all switches are open for a very short time during the switching transitions. Filters implemented with these elements are termed 'switched-capacitor filters'. Unlike continuous time analog filters, which must be constructed with resistors, capacitors and sometimes inductors whose values are accurately known, switched capacitor filters depend only on the ratios between capacitances and the switching frequency. This makes them much more suitable for use within integrated circuits, where the accurately specified absolute value of passive components such as resistors and capacitors are not economical to construct.

The switched capacitor resistor:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The most simple switched capacitor circuit is shown in figure 1, the switched capacitor resistor. It consists of one capacitor C\ :sub:`1` and two switches S\ :sub:`1` and S\ :sub:`2` which connect the capacitor alternately to the input, V\ :sub:`IN` and the output, V\ :sub:`OUT`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-switch-cap-filter-lab-fig1.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 1, Basic Switched Capacitor circuit


Each switching cycle transfers a charge Eq from the input to the output at the switching frequency F. Recall that the charge q on a capacitor C with a voltage V between the plates is given by:

:math:`q = CV`

Where V is the voltage across the capacitor. Therefore, when S\ :sub:`1` is closed while S\ :sub:`2` is open, the charge transferred from the input source to C is:

:math:`q_IN = C_1 V_IN`

And when S\ :sub:`2` is closed while S\ :sub:`1` is open, the charge transferred from C\ :sub:`1` to the output is:

:math:`q_OUT = C_1 V_OUT`

The charge transferred in each cycle is:

:math:`\Delta q = q_OUT - q_IN = C_1( V_OUT - V_IN )`

Since a charge Δq is transferred at a rate F, the rate of transfer of charge per unit time is:

:math:`I = \Delta q F`

Note that I is used, the symbol for electric current, for this quantity. This is to demonstrate that a continuous transfer of charge from one node to another is the same as current. Substituting for tq in the equation above, we get:

:math:`I = C_1(V_OUT - V_IN) F`

We define V, the voltage across the circuit from input to output, as:

:math:`\Delta V = V_OUT - V_IN`

We now have a relationship between I and V, which we can rearrange to give an equivalent resistance R:

:math:`R = V / I = 1 / (C_1 F)`

Thus, the circuit behaves like a resistor whose value depends on C\ :sub:`1` and F.

The Switched Capacitor resistor is often used as a replacement for simple resistors in integrated circuits because it is easier to fabricate reliably with a wide range of values. It also has the benefit that the equivalent resistor value can be adjusted or tuned by changing the switching frequency.

This same circuit can be used in discrete time systems (such as analog to digital converters) as a track and hold circuit. During the appropriate clock phase, the capacitor samples the analog voltage through switch one and in the second phase presents this held sampled value to an electronic circuit for processing. Further reading on `switched capacitors <https://en.wikipedia.org/wiki/Switched_capacitor>`_.

Example Circuit
---------------

The next step is to build an example circuit using the Switched Capacitor as a resistor. By adding a second capacitor C\ :sub:`2` across the output of figure 1, we get the RC low pass circuit shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-switch-cap-filter-lab-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 Switched Capacitor RC low pass filter


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard
| Jumper wires
| 1 – LTC1043 Switched Capacitor Building Block (used as SPDT analog switch)
| 1 – 4.7 nF capacitor (472)
| 1 – 470 pF capacitor (471)
| 2 – 39 pF capacitors
| 1 – 100 pF capacitor (101)

Below in figure 3 is the schematic and pinout for the LTC1043. The LTC1043 contains four SPDT CMOS switches all driven from the same non-overlapping clock source.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-switch-cap-filter-lab-fig3.png
   :align: center
   :width: 175px

.. container:: centeralign

   Figure 3 LTC1043 pinout


Directions:
~~~~~~~~~~~

The breadboard connections are as shown in figure 4. The circuit will operate from the fixed +5V supply provided from the ALM1000 board.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-switch-cap-filter-lab-fig4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Switched capacitor RC low pass filter


Hardware Setup:
~~~~~~~~~~~~~~~

Channel A should be configured in SVMI mode as a 100 Hz sine wave with 2.0 Min and 3.0 Max values to start out. Channel B should be configured in Hi-Z mode. Channel A should be connected to the input of the filter and Channel B should be connected to the output of the filter.

Procedure:
~~~~~~~~~~

Using the scope display observe the output amplitude (p-p) of the filter relative to the input as you change the input frequency, Channel A. Also note any changes in the output amplitude as you change the switching frequency by connecting different size capacitors to pin 16 of the LTC1043, C\ :sub:`OSC`, no external cap, 39pF, 2 39pF caps in parallel (78 pF total) and 100pF.

Stop and disable the Oscilloscope screen and now open the Bode plotter screen. You will need to select Channel A as the sweep source. Set up to sweep the filter input from 100 Hz to 10 KHz. Run sweeps with no external Cap, 39pF, 2 39pFcaps in parallel (78 pF total) and 100pF.

The approximate frequency of the internal oscillator can be calculated using this equation:

:math:`F_osc = 190KHz (24pF) / (24pF+C_OSC)`

Export the amplitude and phase data for each sweep to a .csv file and using a spreadsheet program make plots of the amplitude and phase vs. frequency similar to the plot in figure 5. The darker curves are for the case with no C\ :sub:`OSC` connected and the lighter curves are for the case when C\ :sub:`OSC` = 100 pF.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-switch-cap-filter-lab-fig5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Low Pass Amplitude / Phase plot


Note that the amplitude curve for highest switching frequency (no C\ :sub:`OSC`) crosses the -3 dB line at 3 KHz and that the curve for C\ :sub:`OSC` = 100 pF crosses at 600 Hz, a factor of 5 times lower than the highest switching frequency curve.

Are your results consistent with the LTC1043 internal oscillator equation and an external 100 pF C\ :sub:`OSC`?

Questions:
~~~~~~~~~~

How well do the measured Bode plot curves match the expected response of a simple RC low pass filter? Determine the equivalent resistance and RC time constant for each switching frequency, no external Cap, 39 pF, 2 39 pF caps in parallel and 100 pF. Based on these measurements and the values of C\ :sub:`1` and C\ :sub:`2` calculate the effective sample rate for each external capacitor configuration.

High Pass Filter:
~~~~~~~~~~~~~~~~~

The switched capacitor resistor and capacitor can be interchanged to form the equivalent RC high pass filter shown in figure 6.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Modify the circuit on your breadboard as shown in figure 6. Perform the same Bode plot sweeps you did on the low pass configuration for each switching frequency by changing C\ :sub:`OSC`, no external Cap, 39 pF, 2 39 pF caps in parallel and 100 pF.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-switch-cap-filter-lab-fig6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, Switched capacitor RC high pass filter


Export the amplitude and phase data for each sweep to a .csv file and using a spreadsheet program make plots of the amplitude and phase vs. frequency similar to the plot in figure 7. The darker curves are for the case with no C\ :sub:`OSC` connected and the lighter curves are for the case when C\ :sub:`OSC` = 100 pF.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-switch-cap-filter-lab-fig7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, High Pass Amplitude / Phase plot


Note that the amplitude curve for highest switching frequency (no C\ :sub:`OSC`) crosses the -3 dB line at 3 KHz and that the curve for C\ :sub:`OSC` = 100 pF crosses at 850 Hz, lower than the highest switching frequency curve.

Are your results consistent with the LTC1043 internal oscillator equation and an external 100 pF C\ :sub:`OSC`?

.. _questions-1:

Questions:
~~~~~~~~~~

How well do the measured Bode plot curves match the expected response of a simple RC high pass filter? Determine the equivalent resistance and RC time constant for each switching frequency, no external Cap, 39 pF, 2 39 pF caps in parallel and 100 pF. Based on these measurements and the values of C\ :sub:`1` and C\ :sub:`2` calculate the effective sample rate for each external capacitor configuration.

Now might external measurement conditions, such as the loading effect of the ALM1000 inputs, alter your results and do they explain any differences from the expected frequency response?

Appendix:
---------

Analog Switch Alternatives to the LTC1043:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Other analog switches can be substituted for the LTC1043 in the event one is not available. There are four members of the CD4000 family of ICs that can possibly be used: the CD4066 Quad SPST switch, CD4051 8-channel analog multiplexer/demultiplexer, CD4052 Dual 4-channel analog multiplexer/demultiplexer, CD4053 Triple 2-channel analog multiplexer/demultiplexer. The CD4007 CMOS transistor array can be configured as a single SPDT analog switch as shown in figure 8.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-switch-cap-filter-lab-fig8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, CD4007 as SPDT analog switch


To use any of these alternatives in this Lab you will need to supply an external clock source. **For Further Reading:**

| :adi:`Take the Mystery Out of the Switched-Capacitor Filters <media/en/technical-documentation/application-notes/an40f.pdf>`
| `Low Pass Filters <https://en.wikipedia.org/wiki/Low-pass_filter>`_
| `High Pass Filters <https://en.wikipedia.org/wiki/High-pass_filter>`_

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-signals-labs-list>`\ **.**
