Activity: Transformer Coupled Amplifier – ADALM1000
===================================================

Objective
---------

The objective of this activity is to become familiar with the use of transformer coupling in amplifiers for impedance matching.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background
----------

A basic definition of a transformer is a component that takes an AC signal at one voltage (on the primary) and transforms it into another voltage either higher or lower than the original voltage (on the secondary), thus a “step-up or step-down transformer”. A transformer can also be used to isolate a circuit from the ground in which case the transformer is called an "isolation transformer". But importantly, the usage of the transformer that we are going to tackle is its capability to match impedances of circuits to achieve maximum power transfer. Consider the simulation circuit presented in figure 1. The circuit is a Transformer Coupled Class A Power Amplifier. This is like the normal common emitter amplifier circuit but connected to a transformer as the collector load.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-trans-coupled-amp-fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1. Transformer Coupled Class A Power Amplifier, LTspice simulation schematic.


The waveforms from the simulation are shown in figure2. The amplifier has considerable gain. A 50 mV peak-to-peak signal on the base, V(vbase), results in a 1.96 V peak-to-peak signal centered on the +5 V power supply on the collector, V(vcol). A gain of about 39.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-trans-coupled-amp-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2. Transformer Coupled Class A Power Amplifier, simulation waveforms.


The signal on the secondary side of the 1:1 transformer at V(bin) is nearly equal to the signal on the primary side at 1.89 V peak-to-peak across the 100 Ω load resistor. However it is now centered on +2.5V (DC reference voltage Vmid).

The power transferred from the power amplifier to the load will be at a maximum only if the amplifier output impedance equals the load impedance R\ :sub:`L` (R4). This is in accordance with the maximum power transfer theorem. The transfer of maximum power from the amplifier to the output device, matching of amplifier output impedance with the impedance of the output device is necessary. This is accomplished by using a step-down transformer of suitable turns ratio.

Thus, the ratio of the transformer input and output resistances varies directly as the square of the transformer turn ratio:

.. container:: centeralign

   :math:`R_Lp/R_L = (Np/Ns)^2 = n^2`


Giving us the equation finding the reflected impedance,

.. container:: centeralign

   :math:`R_Lp = (n^2) \times R_L`


where

-   n is the ratio of primary to secondary turns of the step-down transformer
   \* R\ :sub:`Lp` is the reflected impedance in the primary

The efficiency of a conventional class A power amplifier is about 30% whereas it can be improved to about 50% by using a transformer coupled configured class A power amplifier. Increased efficiency is one of the advantages of this configuration but aside from that the following are the other advantages of transformer coupled class A power amplifier,

-  No loss of signal power in the base or collector resistors.
-  Excellent impedance matching is achieved.
-  Gain is high.
-  DC isolation is provided.

But this configuration is not perfect thus having the following disadvantages,

-  Low-frequency signals are less amplified comparatively.
-  Hum noise is introduced by transformers.
-  Transformers are bulky and costly.
-  Poor frequency response.

Materials
---------

| ADALM1000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 NPN transistor (2N3904)
| 1 10k resistor
| 1 20k resistor
| 1 1k resistor
| 1 6.8k resistor
| 1 100 Ω resistor
| 1 47 Ω resistor
| 1 10uF capacitor
| 1 1uF capacitor
| 1 HPH1-1400L 6 winding transformer

Hardware Setup
--------------

Build the circuit from figure 1, using figure 3 as the reference. Use power supplied +5V and +2.5V of ADALM1000. The signal we need to apply to the base is rather small so a resistor divider consisting of the 6.8 k (R5) and 1 k (R6) is used to attenuate the channel A AWG sine source.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-trans-coupled-amp-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3. Transformer Coupled Class A Power Amplifier


Procedure
---------

Set AWG channel A in SVMI mode to Shape sine with a Min value of 1.75 and a Max value of 3.25. Set the Frequency to 10kHz. Set channel B to HiZ Split I/O mode.

Monitor both channels on the oscilloscope. The result should be similar to Figure 4. The green trace is the AWG A output (before the resistor divider) and the orange trace is the secondary voltage across the load resistor. As can be seen the overall gain of the combined resistor divider and amplifier is nearly one. There is power gain however in that the input impedance will be greater than 6.8 k while the output load impedance is 100 Ω (a ratio of > 68:1).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-trans-coupled-amp-fig4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4. Measured Input and Output Voltage waveforms


Questions
---------

In the above activity, we used a 1:1 turns ratio transformer, now try changing the transformer's turns ratio to 2:1 and see what happens.

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/trans_coupled_amp_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/trans_coupled_amp_ltspice`
   


Further Reading
---------------

Refer to Transformers Lab activity to know more about the 6 winding transformer:

-  :doc:`Transformers </wiki-migration/university/courses/alm1k/alm-lab-transformers>`

**Return to Lab Activity Table of Contents**
