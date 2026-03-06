ADALM1000 Analog Inputs
=======================

The analog input and output connections to the ADALM1000 active learning module are made though the 6 (original Rev D boards) or 8 pin (Revision F boards) single row female header (on 0.1" centers) connector. The Channel A and B analog pins are on the two outside end pins. A very simplified block diagram of one of the analog channels is shown in figure 1. There are two additional optional input only pins that were not populated on the Rev D, 6 pin header, shown with white circles around them in figure 2. The user can optionally populate these extra two pin locations to separate the analog output and input functions which by default share the common analog channel pin. There are extra switches not shown in the diagram which allow the voltage measuring “oscilloscope” hardware (volt meter in diagram) to be brought out along with the 1 MΩ input load resistor to a separate pin from the analog output source. These Split input pins are labeled AIN and BIN respectively on the Rev F boards. Note figure 3 extracted from schematic.

.. image:: https://wiki.analog.com/_media/university/tools/m1k_analog_input_f1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 1 ALM1000 analog input/output diagram


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2 Analog I/O connector (left Rev D, right Rev F)


.. image:: https://wiki.analog.com/_media/university/tools/m1k_adapter_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3 Detail of analog input switching


As we can see from figure 3 switch S\ :sub:`1` disconnects the CH A/B pins from the output drivers, putting that channel in the high impedance mode. Normally, S\ :sub:`4` is closed connecting the analog input buffer ( voltmeter in figure 1 ) to the CH A/B pins. It is also important to note that the white circle pin on Rev D boards and AIN/BIN on Rev F boards, is connected to CH A/B when S\ :sub:`4` is closed. If S\ :sub:`4` is opened then the analog input buffer is disconnected from the CH A/B pins and is now only available at the pin with the white circle or AIN/BIN pins.

The signals and power supplies that ADALM1000 can generate are limited by the +5 V USB power available from the computer. The analog inputs can measure 0 to +5 volt signals. Generally, this is not an issue when measuring the characteristics of simple passive two terminal devices and simple circuits powered from the provided +5 V supply. However, LC resonate circuits such as oscillators, DC-DC boost converters and other circuits can readily generate voltages beyond their input power supply voltage. To use the ALM1000 to experiment with a broader range of electronic circuits and systems we would like to be able to measure a wider range of input voltages.

This limitation on the allowable voltages that can be measured can be expanded through the use of an external resistor voltage divider. To properly design an input voltage attenuator we first need to understand the input characteristics of the ALM1000. A simulation schematic of the equivalent input circuit of the ALM1000 is shown in figure 4. RIN and CIN represent the analog input circuitry of the ALM1000. V1 represents the fixed +5 V power supply. VIN represents the voltage to be measured.

.. image:: https://wiki.analog.com/_media/university/tools/m1k_analog_input_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 Channel Simulation Equivalent Circuit


This input attenuator circuit works in conjunction with the internal 1 MΩ input resistance, RIN, of the ALM1000 when in the "high Z" measurement mode. Resistor R1 is the input of the divider. R2 can be connected to either ground or to the +2.5 V or +5 V supply to inject an offset to allow the measurement of negative voltages. Depending on the resistor values chosen, various ranges can be produced. For example, with R2 equal to 500 KΩ and connected to +5 V and R1 set to 1 MΩ the divider factor will be 4X with an offset such that 0 V in will result in +2.5 V as seen by the ALM1000, -10 V seen as 0V and +10 V seen as +5 V. This range is only valid for ideal resistors and will vary depending on resistor tolerance and the actual value of the +5V supply. Any differences can be calculated out with software calibration.

The input capacitance, CIN, of the analog inputs in the high Z mode is approximately 380 pF (for the ALM1000 rev D design). This capacitance with relatively high resistance levels can significantly lower the frequency response of the resistor divider. A frequency compensation capacitor is needed across the input resistors R1. Using Spice simulation and empirical testing it was found that for the example case with R1 = 500 KΩ and R2 = 1 MΩ, a total of about 130 pF was needed to compensate the divider. A 100 pF in parallel with 27 pF (total of 127 pF) or two 68 pF capacitors in parallel (total of 136 pF) provides nearly optimal compensation. The effective input impedance for the above example will be 1.333 MΩ and 96 pF.

If we open switch S4 in figure 3 and use the white circle pin as the scope input we see a much lower capacitance because instead of having the combined capacitance of three off switches and one on switch we have just the off capacitance of a single switch, S4. The typical capacitance in this configuration is approximately 90 pF (for the ALM1000 rev D design). The simulation schematic of the equivalent circuit of a white circle pin is shown in figure 5. The only difference between this and figure 4 is the values for the capacitors. CIN is now 90 pF and a 30 pF value for C2 results in perfect compensation in simulation.

.. image:: https://wiki.analog.com/_media/university/tools/m1k_analog_input_f4a.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5 White circle Pin Simulation Equivalent Circuit


An adjustable trimmer capacitor, such as the one pictured in figure 6, could of course be used for one of the capacitors to more precisely adjust the compensation.

.. image:: https://wiki.analog.com/_media/university/tools/m1k_analog_input_f4.jpg
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 6; 4 pF - 32 pF trimmer capacitor


Another variation on this input network is of course to insert a series capacitor to provide AC coupling. If we use a 1 MΩ resistor connected between CH A, for example, and the +5 V power supply the DC voltage seen at the input will be around 2.5 V based on the internal 1 MΩ resistor to ground. Depending on the desired low frequency cut off point and the parallel resistance, 500 KΩ, an appropriate series capacitor can be chosen. In the schematic, figure 7, a ridiculously large 47 uF cap was chosen which gives a sub 1 Hz high pass frequency. A zip file containing the two Simetrix (ADIsimPE) schematic files for the ALM1000 input equivalent circuits, shown in figures 4 and 5, are attached to this document.

.. image:: https://wiki.analog.com/_media/university/tools/input_probe_ac.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 7, AC coupling example


.. image:: https://wiki.analog.com/_media/university/tools/input_probe_ac-graph.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8 AC coupling simulation (red - input, green - output)


From figure 8 we can see that the red input signal is of the same amplitude but now centered on 2.5V as the green output signal seen at the CH A input pin.

A zip file containing the two Simetrix (ADIsimPE) schematic files for the ALM1000 input equivalent circuits shown in figures 4 and 5 are attached here: `m1k_input_simulation.zip <https://wiki.analog.com/_media/university/tools/m1k_input_simulation.zip>`__
