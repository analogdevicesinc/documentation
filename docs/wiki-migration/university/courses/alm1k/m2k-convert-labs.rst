Doing the Lab Activities Using Either ALM1000 or ALM2000
========================================================

Objective:
----------

The objective of this document is to provide guidance on performing the Circuits and Electronics lab activities with either the ADALM1000 or ADALM2000 hardware modules. The ALICE desktop software interface for the ADALM1000 (M1K) and the Scopy software interface for ADALM2000 (M2K) provide user interface environments for performing these lab activities.

Notes:
------

The green shaded rectangles used in the figures indicate connections to the analog I/O connector on either the ALM1000 or ALM2000.

For the ALM1000 module we use the following terminology when referring to the connections to the connector and configuring the hardware. The analog I/O channel pins are referred to as CA and CB.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   ALM1000 analog input/output connector (left Rev D, Right Rev F


When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. The fixed power and ground connections are referred as GND, +5 and +2.5.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

For the ALM2000 module we use the following terminology when referring to the connections to the connector and configuring the hardware. The analog input channel pins are referred to as 1+ and 1- for the channel 1 differential input and 2+ and 2- for the channel 2 differential inputs. The two arbitrary waveform signal generator outputs are referred to as W1 and W2. There are four ground connections which are all connected together and are referred to as GND. The positive user power V+ is referred to by the voltage it is set to such as +2.5 or +5.0. Similarly the negative user supply V- is referred to by the voltage it is set to such as -2.5 or -5.0.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f2.png
   :align: center
   :width: 400px

.. container:: centeralign

   ALM2000 pin designations


Scope traces are similarly referred to by channel number. Such as C1-V , C2-V for the voltage waveforms.  

Background:
-----------

The ALM1000 hardware module is capable of producing and measuring single ended voltages from 0.0 to 5.0 V. It also can source and measure bipolar currents from -200 mA to +200 mA. It provides fixed +2.5 and +5 volt power supplies that can also source or sink up to 200 mA. The use of :doc:`external voltage divider networks </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>` can extend the 0 to +5 V measurement range of the ALM1000 to almost anything depending on the resistor divider ratio chosen.

The ALM2000 hardware module is capable of producing single ended voltages from -5.0 to 5.0 V. It can measure differential voltages well beyond that range but for purposes here we can confine the voltage range to that same -5.0 to 5.0 volts. It provides adjustable 0 to -5.0 and 0 to +5 volt power supplies that can also source or sink up to 50 mA. The waveform generator outputs include 50 Ω series termination resistors which will reduce to output voltage swing possible depending on the impedance of the load being driven. For example when driving a 50 Ω load the available output swing would be reduced to +/- 2.5V from the +/- 5V when the outputs are not loaded.

On the surface the supported voltage and current ranges would seem rather different but we can consider the M1000 voltage capabilities as a subset of the M2000 voltage capabilities. Similarly, the current capabilities of the M2000 can be considered as a subset of the M1000 current capabilities. If our lab activities are confined to operate within the combination of the two subsets with perhaps minor component value adjustments we should be able to perform the same lab experiments with either hardware module. Testing and operation over extended voltage ranges when using the M2000 are an added bonus while testing over extended current ranges when using the M1000 are again an added bonus.

**Some general rules to follow:**

1. Experiment setups that use a single positive power supply ( +5.0V ) and not either of the +2.5V or +3.3V supplies of the ALM1000 can be performed almost directly with either hardware module. Other positive fixed voltages could possibly be generated using one of the AWG channels in the ALM2000 and of course taking the series 50 Ω resistor into account when driving any significant load resistance. Experiments that only use the AWG signal generator outputs and scope inputs can also be performed almost directly with either hardware module.

2. The single ended 0 to 5V range of the ALM1000 can be considered to be from -2.5 V to +2.5 V if the +2.5 V fixed supply is viewed as the common voltage reference rather than ground. The ground pin would be considered to be at -2.5 V with respect to the common and the +5 V supply would be considered to be at +2.5 V with respect to the common. On the ALM2000, this would map to using the variable power supplies set to -2.5 V and +2.5 V respectively. This remapping is shown in figure 1. **It is extremely important to note that the "Earth" ( USB connector ) ground of the ALM1000 and ALM2000 will be connected to different nodes within the circuit under test and any connections to other external devices may result in short circuiting a ground to something it should not be connected to.**


|image1|

.. container:: centeralign

   Figure 1, Single supply to dual supply mapping.


3. When using the differential inputs on the ALM2000 to measure single ended voltages the 1- and 2- inputs should be connected to ground.

4. When using the differential inputs on the ALM2000 to measure current by inserting a series resistor the + and – inputs are connected across the resistor and one of the Math traces is used to display current by dividing the measured voltage by the resistor value. For example to display current in mA using scope channel 1 and a 100 Ω series resistor set the Math formula to:

VBuffA[t]/0.1

To convert volts to mA divide by the resistance in Kilo Ohms. Because 1 mA is equal to 100 mV across a 100 Ω resistor or 0.1 KΩ.  

Materials:
~~~~~~~~~~

ADALM1000 and ADALM2000 hardware modules

Examples:
---------

The following examples are not intended to completely cover how to perform all the Active Learning lab activities with either hardware module but rather to serve as guidance for the less obvious differences.  

Labs that measure voltage vs current characteristics:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following examples are intended to show the connection mapping for experiments involving measuring the voltage and current characteristics of any two terminal component or network such as resistors, capacitors, inductors, series and parallel connected R-L-C networks and of course semiconductor diodes used in the examples.

Case 1 is the measurement of the current vs voltage curve of a diode when forward biased. When performed with the ALM1000 the current I\ :sub:`D` is available as the Channel A current trace. It can also be plotted by subtracting the channel B voltage from the channel A voltage and dividing by the resistor value.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2(a), M1K version.


When performed with the ALM2000 the current I\ :sub:`D` can be obtained by connecting Channel 2 differentially across the resistor and dividing by the resistor value.



|image2|

.. container:: centeralign

   Figure 2(b), M2K version.


Because the Zener diode provided in the ALP2000 Analog Parts kit has a reverse break down voltage larger than the +5.0 available when using the ALM1000, two ( or one or three ) 1.5 volt cells are used to bias the negative side of the diode below ground as shown in figure 3(a). The added external voltage is mathematically added to the Channel B measurement to obtain the voltage across the diode. As in the forward bias example the diode current is available as the Channel A current trace.



|image3|

.. container:: centeralign

   Figure 3(a), M1K Zener Diode I/V curves.


Because the ALM2000 has a built in negative supply it can be substituted for the external battery as shown in figure 3(b). The negative supply can be programed to any appropriate value up to the -5.0 volt limit. The voltage across the diode is measure differentially by connecting the 1- input to the negative end of the diode. The diode current trace is obtained as before using Channel 2 and dividing by the resistor value.



|image4|

.. container:: centeralign

   Figure 3(b), M2K Zener Diode I/V curves.


Labs that measure transistor characteristic curves:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The common emitter test setup for supplying base current and measuring the collector current when using the ALM1000 is rather simple, requiring only a single resistor to convert the voltage from one of the waveform generators into small base current steps.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 (a) M1K NPN I\ :sub:`C` vs. V\ :sub:`CE` characteristic curve measurment setup.


When performed with the ALM1000 the collector current I\ :sub:`C` is available as the Channel A current trace. The collector, emitter voltage V\ :sub:`CE` is the Channel A voltage trace. The base current I\ :sub:`B` is available as the Channel B current trace.

As shown in Figure 5(a) the collector current for the various base current steps can be plotted vs the collector voltage using the X-Y plotting tool with the Channel B voltage on the X axis and the Channel A current on the Y axis.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 (a) M1K typical NPN I\ :sub:`C` vs. V\ :sub:`CE` characteristic curves.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f10.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 (b) M2K NPN I\ :sub:`C` vs. V\ :sub:`CE` characteristic curve measurment setup.


When measuring the collector current characteristic curves with the ALM2000 the current I\ :sub:`C` can be obtained by connecting channel 2 differentially across the 10Ω resistor and dividing by the resistor value. The collector, emitter voltage V\ :sub:`CE` is measured using the scope 1 differential inputs with 1+ connected to the collector and 1- connected to the emitter (ground in this case). The base current I\ :sub:`B` is can be measured by connecting channel 2 differentially across the 22KΩ resistor and dividing by the resistor value.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f11.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 (b) M2K typical NPN I\ :sub:`C` vs. V\ :sub:`CE` characteristic curves.


As shown in Figure 5(b) when using the ALM2000, the collector current for the various base current steps can be plotted vs the collector voltage using the X-Y plotting tool using a Math channel to plot Channel 1 voltage on the X axis and the other Math to calculate the collector current from the Channel 2 differential voltage divided by the 10 ohm resistor on the Y axis.

Comparing figures 5(a) and 5(b) we can see the effect of the internal 50 Ω series resistor and external 10 Ω used to sense the collector current in the ALM2000 case. The collector, emitter voltage does not make it all the way to + 5 volts due to the drop across these resistors. However, in the ALM1000 case the collector, emitter voltage does swing all the way to +5 volts.  

Labs that use op-amps:
~~~~~~~~~~~~~~~~~~~~~~

In the case of the ALM1000, when performing lab activities using operational amplifiers the positive and negative supply pins are connected to the fixed +5.0 supply and ground respectively as shown in figure 6(a). The fixed +2.5 V supply is then generally considered to be the common voltage reference node for the inputs and output.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f12.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 6(a) M1K Power and ground connections.


In the case of the ALM2000, when performing lab activities using operational amplifiers the positive and negative supply pins are connected to the variable positive and negative supplies respectively as shown in figure 6(b). Ground would then generally be considered to be the common voltage reference node for the inputs and output.

Note: It would also be possible to power the op-amp from just the positive supply and ground as in figure 6(a). However, the ALM2000 does not directly produce a low impedance +2.5 V supply that might be needed as the common voltage reference node for the inputs and output.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f13.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 6(b), M2K Power and ground connections.


Next we show a couple of common op-amp configurations and how they should be connected to the ALM1000 and ALM2000 respectively. General Rule #2 is the basis for most any op-amp related lab activity.

There is not much difference in the connections for the unity gain follower example. The difference comes when setting the Min and Max voltage swing for the input. For the ALM1000 the AWG voltage would generally be centered on +2.5 V. For example Min = 1.0 and Max = 4.0.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f14.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 7(a), M1K Unity gain follower.


For the ALM2000 the AWG voltage would generally be centered on 0.0 V. For example Min = -1.5 and Max = 1.5.



|image5|

.. container:: centeralign

   Figure 7(b), M2K Unity gain follower.


For the inverting amplifier case the + input of the op-amp needs to be biased at the mid-point of the power supply voltage. This will be the +2.5 V supply in the ALM1000 case as shown in figure 8(a).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f16.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 8(a), M1K Inverting amplifier configuration.


This common reference point will be ground in the ALM2000 case as shown in figure 8(b).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f17.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 8(b), M2K Inverting amplifier configuration.


Current Mirror Labs:
~~~~~~~~~~~~~~~~~~~~

Because the ALM1000 can either source voltage or current while simultaneously measuring both current and voltage, testing the input current and voltage as well as the output current and voltage of the current mirror is a relatively simple matter as shown in figure 9(a). The channel A signal source is configured to source current (I\ :sub:`in`) while measuring voltage and the channel B signal source is configured to source voltage while measuring current (I\ :sub:`out`). All four traces can be displayed simultaneously.


|image6|

.. container:: centeralign

   Figure 9(a) M1K current mirror test circuit.


On the other hand the ALM2000 can only source voltage and measure voltage. To supply a current to the input of the current mirror the voltage from AWG channel W1 is converted to a current by a resistor. The current is measured by dividing the differential voltage across the resistor, measured by scope Channel 1, by the value of the resistor. Similarly, on the output the current is converted to a voltage by the second resistor. The voltage across the resistor is measured differentially by scope Channel 2. Because there are only two measurement channels only the currents can be displayed or only the voltages ( in loopback mode or by connecting the 1- and 2- inputs to ground).



|image7|

.. container:: centeralign

   Figure 9(b), M2K current mirror test circuit.


Appendix, Techniques to Split A single Positive Supply:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image8|   Voltage Divider with op-amp buffer.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f21.png
   :align: center
   :width: 500px

Fixed voltage reference.

**For Further Reading:**

| :doc:`ALICE desktop user guide for ADALM1000 </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`
| :doc:`Scopy (User Guide for ADALM2000) </wiki-migration/university/tools/m2k/scopy>`

**Return to Circuits Lab Activities** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`

**Return to Electronics Lab Activities** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f3.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f5.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f6.png
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f7.png
   :width: 500px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f15.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f18.png
   :width: 500px
.. |image7| image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f19.png
   :width: 500px
.. |image8| image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f20.png
   :width: 500px
