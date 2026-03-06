Activity: Amplitude Modulators
==============================

Objective:
----------

The objective of this activity is to construct an Amplitude Modulator circuit using an NPN transistor differential amplifier.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

An AM modulator can be constructed by varying the tail current of an NPN differential amplifier as a variable transconductance amplifier. The transconductance of Q1 and Q2 in figure 1 varies directly and linearly versus the emitter current as set by Q3. The higher the current from Q3, the higher the transconductances of Q1 and Q2 and the higher the signal gain that Q1 and Q2 provide.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-am-mod-fig1.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure 1, The transconductance amplifier as AM modulator


In simulation Q1 and Q2 will be parametrically identical and track each other over temperature and the circuit will have no offset or gain errors. However, attempting to make this circuit using discrete transistors, (2N3904 for example) will not perform as well as it does in simulation. Discrete devices do not parametrically match or track each other so the current split between the differential pair will be extremely unstable versus temperature. This is why integrated circuits perform much better, where all the devices constructed on the same silicon substrate will be at the same temperature and have matching electrical parameters.

In an improved discrete implementation, shown in figure 2, Q1 and Q2 operate as a differential pair. However, unlike the conventional differential pair of figure 1, where the emitters of the pair are directly connected together, the emitters are capacitively coupled to each other. Additionally, different than the standard differential pair, Q1 and Q2 each have their own current sources, Q3 and Q4, rather than sharing a single current source. The two tail current sources are generally considered to be thermally at the same temperature. If Q1, Q2 and Q3, Q4 are parametrically slightly mismatched versus temperature, it will not cause significant errors in the single-ended AM output below 100% modulation.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-am-mod-fig2.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure 2, The AM modulator simulation circuit


From the above circuit, we see the following SPICE results. The op-amp, U1, converts the differential signal seen at the collectors of Q1 and Q2 into a single-ended signal at AMoutput.

In Figure 3, the carrier signal from source VC appears differentially at the collectors of Q1 (V(n001)) and Q2 (V(n003)) with no modulation signal applied from source VM. Note that the collector signals are 180° out of phase with respect to each other.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-am-mod-fig3.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 3, Carrier signals with no modulation applied


In figure 4, with no carrier signal applied from source VC, the modulating signal from source VM shows up as common mode (zero differential signal) at the collectors of Q1 and Q2. The collector signals are at zero degrees phase angle with respect to each other.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-am-mod-fig4.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 4, Modulating signal with no carrier


If we turn on both the carrier and modulation signals, in figure 5, the result is the amplitude modulated carrier with the modulating signal itself getting cancelled out in that subtraction.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-am-mod-fig5.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 5, Carrier signals with modulation applied


Materials:
----------

| ADALM1000 hardware module
| Solder-less Breadboard
| Jumper wires
| 4 – 2N3904 NPN transistors
| 2 – 1K resistors
| 2 – 1.5K resistors
| 2 – 2.2K resistors
| 2 – 4.7K resistors
| 2 – 10K resistors
| 4 – 20K resistors
| 2 – 1 uF capacitors
| 1 – 4.7 uF capacitor
| 1 – 10 uF capacitor
| 1 – AD8542 rail-to-rail op-amp
| 1 – HPH1-1400L 6 winding transformer

Directions:
-----------

On your solder-less breadboard construct the AM modulator circuit as shown in figure 6.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-am-mod-fig6.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 6, AM modulator


Procedure
---------

Sine waves are generally used for the Carrier and Modulation signals in this activity.

The amplitude of the Carrier signal, VC in figure 2, is small. AWG channel A is AC coupled to the circuit so the DC level is unimportant so we can set the Min and Max values most anywhere as long as they are only around 100 mV apart. Centering on the 2.5 V middle of the supply range is advisable. A Min value of 2.45 and a Max value of 2.55 are good starting values. The Carrier frequency should be set to 20 KHz.

The amplitude of the Modulation signal, VM in figure 2, is larger and the AWG channel B is also AC coupled to the circuit. The Modulation frequency should be set to 100 Hz. While observing the modulated AMoutput signal with AIN in the Split I/O mode, adjust the difference between the Channel B Min and Max values until the modulation level approaches 100 % similar to that shown in figure 5.

Try increasing the amplitude of the Carrier signal. How does it affect the modulation level seem in the output? Is there a point beyond which there is no affect?

Modifications for operation at high frequency
---------------------------------------------

Using an active operational amplifier to convert the differential signal to a single ended signal at radio frequencies is impractical and a transformer is more often used as we see in figure 7. Here two of the six windings in a HPH1-1400L are used as the collector loads. The remaining 4 windings are connected in series to form the secondary winding.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-ss-am-mod-fig7.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 7, Tuned LC load, AM modulator


By using the inductance of the coil with capacitor C5, a parallel resonate or tuned load can be implemented. The LC resonate frequency is tuned to be equal to the carrier frequency. In the case of the 200 uH coil inductance and a 20 KHz carrier frequency C5 is set to 80 nF. Because of device tolerances the exact resonance might fall at a slightly different frequency. You should observe the amplitude of the AM output signal as you adjust (sweep) the frequency of the Carrier either side of where you calculate the resonance to happen. Find the frequency that results in the highest amplitude output. That will be the resonate frequency of the modulator.

**For Further Reading:**

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-signals-labs-list>`\ **.**
