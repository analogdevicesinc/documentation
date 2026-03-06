Activity: Transformer Coupled Amplifier
=======================================

Objective
---------

The objective of this activity is to become familiar with the operation of transformer coupled in amplifiers as impedance matching.

Background
----------

A basic definition of a is that it is a device that takes AC at one voltage and transforms it into another voltage either higher or lower than the original voltage, thus a “step-up/step-down transformer”. A transformer can also be used to isolate a circuit from the ground in which case the transformer is called an "isolation transformer". But importantly, the usage of the transformer that we are going to tackle is its capability to match impedances of circuits to achieve maximum power transfer.

Consider the circuit presented in Figure 2. The circuit is a Transformer Coupled Class A Power Amplifier. This is like the normal amplifier circuit but connected with a transformer in the collector load.


|image1|

.. container:: centeralign

   Figure 1. Transformer Coupled Class A Power Amplifier


The power transferred from the power amplifier to the load will be maximum only if the amplifier output impedance equals the load impedance R\ :sub:`L` (R4). This is in accordance with the maximum power transfer theorem. The transfer of maximum power from the amplifier to the output device, matching of amplifier output impedance with the impedance of the output device is necessary. This is accomplished by using a step-down transformer of suitable turn-ratio.

Thus, the ratio of the transformer input and output resistances varies directly as the square of the transformer turn ratio:

.. container:: centeralign

   :math:`R_Lp/R_L = (Np/Ns)^2 = n^2`


Giving us the equation finding the reflected impedance,

.. container:: centeralign

   :math:`R_Lp = (n^2) \times R_L`


where

-   n is the ratio of primary to secondary turns of the step-down transformer
   \* R\ :sub:`Lp` is the reflected impedance in the primary

The efficiency of a class A power amplifier is nearly than 30% whereas it has got improved to 50% by using the transformer coupled class A power amplifier. Increased efficiency is one of the advantages of this configuration but aside from that the following are the other advantages of transformer coupled class A power amplifier,

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

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 NPN transisotr (2N3904)
| 1 10k resistor
| 1 20k resistor
| 1 100 resistor
| 1 10uF capacitor
| 1 1uF capacitor
| 1 HPH1-0190L/1400L 6 winding transformer

Hardware Setup
--------------

Build the circuit in Figure 1, see Figure 2 as the reference. Use power supplied +5V and -5V of ADALM2000.


|image2|

.. container:: centeralign

   Figure 2. Transformer Coupled Class A Power Amplifier


Procedure
---------

Set Signal Generator channel 1 to produce a 500mV 100Hz sine wave with 0V offset. Monitor both channels on the oscilloscope. The result should be similar to Figure 3.


|image3|

.. container:: centeralign

   Figure 3. Transformer Coupled Class A Power Amplifier Input vs Output Voltage


Questions
---------

| In the above activity, we used a 1:1 turns ratio transformer, now try changing the transformer's turns ratio to 2:1 and see what happens.
|

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/trans_coupled_amp_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/trans_coupled_amp_ltspice`
   


Further Reading
---------------

Refer to Transformers Lab activity to know more about the 6 winding transformer:

-  `Activity: Transformers <https://wiki.analog.com/university/labs/comms_lab_transformers_adalm2000]>`__

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/labs/trans_coupled_class_a_amp.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/university/labs/trans_coupled_class_a_amp_bb.png
.. |image3| image:: https://wiki.analog.com/_media/university/labs/trans_coupled_class_a_amp_res.png
   :width: 500px
