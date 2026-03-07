Frequency Response of a Common-Emitter BJT Amplifier
====================================================

1 Circuit Topology
------------------

The schematic of a typical common-emitter amplifier is shown in figure 1. Capacitors C\ :sub:`B` and C\ :sub:`C` are used to block the amplifier DC bias point from the input and output (AC coupling). Capacitor C\ :sub:`E` is an AC bypass capacitor used to establish a low frequency AC ground at the emitter of Q\ :sub:`1`. Miller capacitor C\ :sub:`F` is a small capacitance that will be used to control the high frequency 3-dB response of the amplifier.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/afr_f1.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 1: Common-emitter BJT amplifier.


1.1 DC Biasing and Mid-band Frequency Response
----------------------------------------------

For this section, assume that C\ :sub:`B` = C\ :sub:`C` = C\ :sub:`E` = 1 Farad and C\ :sub:`F` = C\ :sub:`Π` = C\ :sub:`µ` = 0. You can find the DC collector current (I\ :sub:`C`) and the resistor values following the analysis provided in your text book. Since the topology and the requirements might be slightly different than in the text, you will need to make minor modifications to the design procedure and equations.

1.2 Low Frequency Response
--------------------------

Figure 2 shows the low-frequency small-signal equivalent circuit of the amplifier. Note that C\ :sub:`F` is ignored since it is assumed that its impedance at these frequencies is very high. R\ :sub:`B` is the parallel combination of R\ :sub:`B1` and R\ :sub:`B2`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/afr_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2: Low-frequency equivalent circuit.


Using short-circuit time constant analysis, the lower 3-dB frequency (ω\ :sub:`L`) can be found as:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/afr_e1.png
   :align: center
   :width: 250px

Where

|image1| |image2| |image3|

1.3 High Frequency Response
---------------------------

Figure 3 shows the high-frequency small-signal equivalent circuit of the amplifier. At high frequencies, C\ :sub:`B`, C\ :sub:`C` and C\ :sub:`E` can be replaced with short circuits since their impedance becomes very small compared to R\ :sub:`S`, R\ :sub:`L` and R\ :sub:`E`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/afr_f3.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 3: High-frequency equivalent circuit.


The higher 3-dB frequency (ω\ :sub:`H`) can be derived as:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/afr_e5.png
   :align: center
   :width: 320px

Where

|image4| |image5|

Thus, if we assume that the common-emitter amplifier is properly characterized by these dominant low and high frequency poles, then the frequency response of the amplifier can be approximated by:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/afr_e8.png
   :align: center
   :width: 230px

2 Pre-Lab
---------

Assuming C\ :sub:`B` = C\ :sub:`C` = C\ :sub:`E` = 1 Farad and C\ :sub:`F` = C\ :sub:`Π` = C\ :sub:`µ` = 0, and using a 2N3904 transistor, design a common-emitter amplifier with the following specifications:

| V\ :sub:`CC` = 5 V
| R\ :sub:`S` = 50Ω
| R\ :sub:`L` = 1 kΩ
| R\ :sub:`IN` > 250
| Isupply < 8mA
| A\ :sub:`V` > 50
| peak-to-peak unclipped output swing > 3 V
| 1. Show all your calculations, design procedure, and final component values.
| 2. Verify your results using the LTSpice circuit simulator. Submit all necessary simulation plots showing that the specifications are satisfied. Also provide the circuit schematic with DC bias points annotated.
| 3. Using the LTSpice simulator, find the higher 3-dB frequency (f\ :sub:`H`) while C\ :sub:`F` = 0.
| 4. Determine Cp, Cµ and r\ :sub:`b` of the transistor from the simulated operating point data, (refer to your simulator's documentation on how to obtain operating point data). Calculate f\ :sub:`H` using the equation from section 1.3 and compare it with the simulation result obtained in Step 3. Remember that the equation gives you the radian frequency and you need to convert to Hz.
| 5. Calculate the value of C\ :sub:`F` to have f\ :sub:`H` = 50 kHz. Simulate the circuit to verify your result, and adjust the value of C\ :sub:`F` if necessary.
| 6. Calculate C\ :sub:`B`, C\ :sub:`C`, C\ :sub:`E` to have f\ :sub:`L` = 500 Hz. Simulate the circuit to verify your result, and adjust the values of capacitors if necessary.
| 7. Be prepared to discuss your design at the beginning of the lab period with your TA.

3 Lab Procedure
---------------

Objective:
~~~~~~~~~~

The objective of this section of the Lab Activity is to validate your pre-Lab design values by building the actual circuit and measuring its frequency response performance.

Materials:
~~~~~~~~~~

| ADALM2000 Active Learning Module
| Solder-less breadboard
| 6 - Resistors various values from the ADALP2000 Analog Parts Kit
| 4 - Capacitors various values from the ADALP2000 Analog Parts Kit
| 1 - small signal NPN transistor (2N3904)
| Note on the source resistor R\ :sub:`S` and the AWG output of the ADALM2000. The AWG output has a 50 Ω series output resistance and you will need to include it along with the external resistance in series with its output. Also because of the relatively high gain of your design you will need an input signal with a small amplitude of around 100mV peak-to-peak. Rather than turning down the AWG in software it would be better from a noise point of view to insert a resistor voltage divider between the AWG output and your circuit input to attenuate the signal. Using something like that shown in figure 4 will provide both an attenuation factor of 1/8 and a 60Ω equivalent source resistance. Other combinations of resistor values are of course also possible based on what you have available.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/afr_f4.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 4 Signal attenuator with 60Ω source resistance


Hardware Setup
~~~~~~~~~~~~~~

Construct the circuit on your breadboard.


|image6|

.. container:: centeralign

   Figure 5 Common Emitter BJT amplifier breadboard connection


Directions:
~~~~~~~~~~~

| 1. Construct the amplifier, based on the schematic in figure 1, you designed in the pre-lab. Based on your design values from the pre-Lab, use the closest standard value from your kit. Remember that you can combine the standard values in series or parallel to get a combined value closer to your design number.
| 2. Check your DC operating point by measuring I\ :sub:`C`, V\ :sub:`E`, V\ :sub:`C` and V\ :sub:`B`. If any DC bias value is significantly different than the one obtained from simulation, modify your circuit to get the desired DC bias before moving onto the next step.
| 3. Measure Isupply.
| 4. Use the Network analyzer instrument in the Scopy software to obtain the magnitude of the frequency response of the amplifier from 10 Hz to as high as 5 MHz and determine the lower and upper 3-dB frequencies f\ :sub:`L` and f\ :sub:`H`.
| 5. At mid-band frequencies, measure A\ :sub:`V`, R\ :sub:`IN`, and R\ :sub:`OUT`.
| 6. Measure the maximum un-clipped output signal amplitude.
| 7. Prepare a data sheet showing your simulated and measured values.
| 8. Be prepared to discuss your experiment with your TA. Have your lab data sheet checked off by your TA before submitting the lab report. |image7|

.. container:: centeralign

   Figure 6 Scopy Network Analyzer plot with C\ :sub:`F` = 0


   |image8|

.. container:: centeralign

   Figure 7 Scopy Oscilloscope plot with C\ :sub:`F` = 0 at frequency = 500Hz


For further experimentation replace each capacitor with ones that are factors of 2 and 10 larger and smaller than your design values and re-measure the response curve with the Network Analyzer instrument. Do this to only one capacitor at a time to observe its individual effect on the response. Explain the changes in the response that you see.

.. admonition:: Download
   :class: download

   **Resources**

   
   -  LTSpice files: :git-education_tools:`m2k/ltspice/freq_resp_bjt_ltspice`
   -  Fritzing files: :git-education_tools:`m2k/fritzing/freq_resp_bjt_bb`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/afr_e2.png
   :width: 150px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/afr_e3.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/afr_e4.png
   :width: 125px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/afr_e6.png
   :width: 200px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/afr_e7.png
   :width: 130px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/afr_nf5.png
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/afr_nf6.png
   :width: 500px
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/afr_nf7.png
   :width: 500px
