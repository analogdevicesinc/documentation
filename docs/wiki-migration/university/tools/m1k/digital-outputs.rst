ADALM1000 Digital Output Pins
=============================

The ADALM1000 (M1K) active learning module provides access to some of the microcontroller digital input/output pins through the digital port connector. Four general purpose input/output pins along with ground and the 3.3V power supply are available as shown in figure 1.

.. image:: https://wiki.analog.com/_media/university/tools/m1k-digital-outputs_f1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 1 Digital I/O connector


Part of the ALM1000 rev D schematic is shown in figure 2D and rev F schematic is shown in figure 2F. As can be seen each of the four general purpose PIO pins ( connector P3 ) is connected to a 220 Ω and a 470 Ω resistor in rev D and in rev F 4.7K resistors in place of the 470 Ω resistors. The 220 Ω resistors connect to Port A pins 0-3 and the 470 Ω / 4.7k resistors connect to Port A pins 4-7. This configuration with two digital port pins connected though two different series resistors is unique and not generally typical of digital pins in other small portable USB based hardware such as the Analog Discovery module.

.. image:: https://wiki.analog.com/_media/university/tools/m1k-digital-outputs_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2D ALM1000 Rev D digital interface input/output diagram


.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/m1k-f-digital-outputs_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2F ALM1000 Rev F digital interface input/output diagram


The state of the Port A pins can be controlled using the predefined Python functions that interface to the C++ libsmu library. Contained in the pysmu.py file they provide the high level access functions to configure and control the ALM1000 hardware. Through Python we can control any or all of these 8 Port A digital pins. For example, to set PA0 to output 0 V ( logic 0 ) we use:

devx.ctrl_transfer(DevID, 0x40, 0x50, 0, 0, 0, 0, 100)

To set a PA1 to output 3.3 V ( logic 1 ) we use:

devx.ctrl_transfer(DevID, 0x40, 0x51, 1, 0, 0, 0, 100)

The hex number 0x50 sets a pin low, the hex number 0x51 sets a pin high. The next value after the 0x50 or 0x51 is the number of the Port pin (0-7). The rest of the values are always the same and should not be changed.

The Port pins can also be set as an input which in effect sets it to a high impedance state. For example to set PA4 as an input or high Z state:

Pio4 = devx.ctrl_transfer(DevID, 0xc0, 0x91, 4, 0, 0, 1, 100)

The value after 0x91 is the number of the Port pin. The function returns the input logic value of the pin. We are not at this point interested in this value.

**Using these pins for purposes other than digital**

This configuration with two possible digital output drivers connected to a single connector pin through two different series resistors could be viewed in a different light. We might consider the CMOS output diver of the microcontroller pin as a three position single pole switch that can connect to ground or the 3.3 V supply or open circuit as shown in figure 3. This is more of an analog representation of the circuit. Looking at the circuit in this way it can perhaps be used in part to teach and learn concepts in DC resistor networks such as Thevenin and Norton equivalent circuits, series/parallel resistors, KVL, KCL, voltage dividers and nodal analysis etc.

.. image:: https://wiki.analog.com/_media/university/tools/m1k-digital-outputs_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Switch based analog representation of the circuit


There are nine possible combinations of the switches which give rise to the 8 Thevenin equivalent circuits shown in figure 4, with the ninth being of course an open circuit. It is important to note here that the resistance and voltage values given are for ideal nominal conditions and actual values may be noticeably different. It also assumes that the ON resistance of the MOS FET switches is zero which is actually never the case.

.. image:: https://wiki.analog.com/_media/university/tools/m1k-digital-outputs_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, 8 Equivalent circuits


The first four cases are obvious. The next two are for the case where the 220 Ω resistor is connected in parallel with the 470 Ω resistor. The last two are for the case where the 220 Ω resistor is connected to ground and the 470 Ω resistor is connected to 3.3 V and the reverse.

A simple Python demonstration script has been written to control the 8 PA0-7 digital pins. Figure 5 is a screen shot of the controls. The 8 pins can be set to either 0, high Z, or 1. In the top row of the screen the DC values measured on Channels A and B are displayed and updated each time a bit state is changed. These can be used to measure node voltages at points in the network being investigated. An ALICE plug-in version of the control program is also included in the zip archive at the end of this document.

.. image:: https://wiki.analog.com/_media/university/tools/m1k-digital-outputs_f5.png
   :align: center
   :width: 225px

.. container:: centeralign

   Figure 5, Demo Python script


With four essentially identical copies of this circuit, the fixed 2.5V, 3.3V and 5V power supplies and a few external resistors an almost endless number of resistor networks can be built to demonstrate and explore DC circuit concepts. Simply shorting two of the PIO pins together results in 9 X 9 or 81 total possible combinations. Many are redundant and some give the same voltage but with different source resistance values. Shorting all four pins together results in 6561 possible combinations using no external resistors. Limited only by your imagination and far more than can be listed in this document.

If external resistors are used in place of the shorts some well know special case resistor networks can be constructed. One example, the R-2R digital-to-analog converter ladder network, is shown in figure 6. The two 220 Ω resistors in parallel are the 'R' part of the ladder and the internal 220 Ω resistors are the '2R' part of the ladder.

.. image:: https://wiki.analog.com/_media/university/tools/m1k-digital-outputs_f6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, R-2R resistor ladder


In the case shown only the internal 220 Ω resistors are used. If the 7 220 Ω resistors are replaced with 470 Ω resistors then the internal 470 Ω resistors are used. This 4 bit DAC has 16 output levels from 0 V to about 3.1 V or about 200mV per step. Both versions could be built and their relative DC accuracy compared.

`Digital output demo archive <https://wiki.analog.com/_media/university/tools/m1k-digital-outputs-demo.zip>`_

**For Further Reading:**

| :doc:`ADALM1000 Python Tutorials </wiki-migration/university/tools/python-tutorial/table-of-contents>`
| :doc:`ADALM1000 Analog Inputs </wiki-migration/university/tools/m1k/analog-inputs>`

**Return to** :doc:`Table of Contents </wiki-migration/university/tools/m1k>`\ **.**
