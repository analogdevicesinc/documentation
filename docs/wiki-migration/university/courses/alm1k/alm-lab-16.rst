Activity: Capacitor Based DC-DC Converters - ADALM1000
======================================================

Objective:
----------

The object of this activity is to explore a capacitor based circuit which can produce an output voltage which is higher than the supplied voltage. This class of circuits are referred to as DC to DC converters or boost regulators.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

The circuits used in this Lab activity while generally low current can produce voltages beyond the 0 to 5 V analog input range of the ALM1000. :doc:`Input voltage divider techniques </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>` as discussed in the document on ALM1000 analog inputs will be required. Refer to the document and construct and use input dividers before preforming any of these experiments with the ALM1000.

Concept:
--------

The basic concept of capacitor based DC to DC converter is shown below in figure 1. These are often referred to as "flying capacitor" or "charge-pump" voltage converters. The operation alternates between the two configurations of the switches shown in figure 1. In one, switches S\ :sub:`1` and S\ :sub:`5` are closed connecting C\ :sub:`1` between ground and V\ :sub:`IN`. In the second, switches S\ :sub:`4` and S\ :sub:`8` are closed connecting C\ :sub:`2` between V\ :sub:`IN` and V\ :sub:`Boost`. For the half cycle shown capacitor C\ :sub:`1` is charged to the voltage at V\ :sub:`IN` and V\ :sub:`Boost` is the sum of the voltage at V\ :sub:`IN` and the voltage on capacitor C\ :sub:`2`. For the second half cycle the switches are reversed. Now with S\ :sub:`2` and S\ :sub:`6` closed C\ :sub:`1` is connected between V\ :sub:`IN` and V\ :sub:`Boost`. Also switches S\ :sub:`3` and S\ :sub:`7` will now be closed connecting C\ :sub:`2` between ground and V\ :sub:`IN`. So now we can see that after a few cycles V\ :sub:`Boost`, the voltage across capacitor C\ :sub:`3` will be equal to twice V\ :sub:`IN`. As you can see the capacitors "fly" back and forth between V\ :sub:`IN` and V\ :sub:`Boost`, thus the name "flying capacitor". One can also see that what is in effect happening is the charge on capacitors C\ :sub:`1` and C\ :sub:`2` is alternately transferred or pumped onto capacitor C\ :sub:`3` charging it up to two times V\ :sub:`IN`. This action gives rise to the second "charge pump" name.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab16_f1.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 1 Capacitor based voltage doubler


We will now replace the ideal switches in the diagram with actual electronic switches. There are a number of possible devices that could be used but the MOS FET transistor is most often used because it can have both a low voltage drop and resistance when turned on. The next diagram shows a direct substitution of NMOS ( S\ :sub:`1`,S\ :sub:`3`,S\ :sub:`5`,S\ :sub:`7` ) and PMOS ( S\ :sub:`2`,S\ :sub:`4`,S\ :sub:`6`,S\ :sub:`8` ) devices for the switches in the first diagram. It can be noted that switches S\ :sub:`1` and S\ :sub:`2` form a complementary pair and take the same form as a CMOS inverter logic gate. The other three sets of switches form similar complementary pairs.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab16_f2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2 CMOS voltage doubler


Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wire kit
| 1 – 1 MΩ resistor
| 1 – 200 KΩ resistor
| 1 – ZVN2110A NMOS FET ( 2N7000 )
| 2 – ZVN3310 NMOS FET ( 2N7000 )
| 1 – ZVP2110A PMOS FET
| 2 – 74HC04 HEX CMOS Inverters ( CD4007, CD4069 )
| 1 – LT1054
| 2 – 10uF capacitors
| 1 – 220uF capacitor
| 2 – 1N914 diodes (1N4001 or 1N5819 Schottky diodes)

*Additional Equipment:*

| Small handheld DMM ( optional )
| +5 V bench power supply or 4.5 V battery ( optional )

Directions:
~~~~~~~~~~~

Before we build any of the DC-DC converter circuits we need to build an input voltage divider circuit to attenuate or reduce the voltages being measured to a low enough value to fit safely within the 0V to +5V range allowed for the ADALM1000 analog inputs. Build the simple voltage divider shown in figure 3 on one end of your solderless breadboard. A DC offset voltage is supplied from the fixed 5 V supply to allow the ability to measure both positive and negative voltages.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab16_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Input voltage divider with buffer op-amp follower


Use the ALICE Desk-top input attenuator gain and offset entry widgets ( figure 4A ) to calibrate the displayed voltage level by connecting the divider input ( end of R\ :sub:`1` ) to ground and the fixed +5 V supply on the ADALM1000. Adjust the offset value such that the scope trace displays 0 V with the input grounded. Next adjust the gain value so that the trace displays as +5 V with the input connected to +5 V supply. With R\ :sub:`2` = 200 KΩ the gain factor should be around 6 but is actually 7.2 due to the internal 1 MΩ input resistance of the input. You can double check your settings by connecting the input to the +2.5 V supply and the trace should read as 2.5V. You can now safely measure voltages within the range shown in figure 3. Be sure to only use the voltage divider input when measuring voltages in this Lab.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab16_f4.png
   :align: center
   :width: 150px

.. container:: centeralign

   Figure 4A Input Attenuator settings


For this lab you will be mainly making DC measurements but the frequency response of the input divider can also be adjusted. To adjust the compensation settings open the Change Settings screen. Set CHA to SVMI mode and Shape Square. Set Min value to 0.5 and Max to 4.5. Set the Frequency to 500 Hz. With CHB in Hi-Z mode and connected to the voltage divider connect CHA output to the input of the divider. Adjust the CHB compensation TC1, A1 and TC2, A2 until the CHB wave shape is a flat top square wave just like CHA. Something like the settings shown in Figure 4B.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab16_f4b.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 4B Frequency compensation settings


The software should now be calibrated for using the input divider with CHB.

**First DC-DC converter**

The breadboard connections for the first version are as shown in figure 5 below. The voltage divider circuit should be connected to measure the voltage at VBoost. (or DMM could be used). The +5V bench power supply or 4.5 V battery should be connected to the Vin node. The digital pulse output drives the input of the first Inverter gate at pin 1. Scope input CA-H through the external resistor divider (see figure 3) is connected to the drain terminal of M\ :sub:`1` and scope input CB-H through an external resistor divider is connected to the drain terminal of M\ :sub:`2`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab16_f5.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 5 NMOS and Diode DC-DC converter


Hardware Setup:
~~~~~~~~~~~~~~~

The V\ :sub:`Clock` pulse can be supplied from the Channel A output or the digital pulse source circuit (details below in figure 8) and should generate a 50% duty cycle square wave with at least a 20 KHz output frequency. The input of scope channel CB-V with the external resistor divider is used to measure the waveform seen at the drain of M\ :sub:`1` and to measure the waveform seen at the drain of M\ :sub:`2` and to measure the V\ :sub:`Boost` output voltage.

Procedure:
~~~~~~~~~~

Be sure to start up the digital pulse source output before turning on the +5V bench supply or connecting the 4.5 V battery. The boosted output voltage at node V\ :sub:`Boost` should be observed and should be approximately equal to 2 times the DC value of the external supply.

Questions:
~~~~~~~~~~

What is the voltage on V\ :sub:`Boost`? Why is it not exactly 2 times V\ :sub:`IN`?

What is the effect of changing the frequency of the digital pulse output? Is there a minimum? or a maximum?

How much current can the circuit supply to a load? Try various resistors as a load.

Is that current affected by the frequency of the digital pulse output?

Calculate the conversion efficiency of the circuit. Ratio of output power (I\ :sub:`OUT`\ \*V\ :sub:`Boost`) to input power (I\ :sub:`IN`\ \* 5V)

Change the value of C\ :sub:`1` and C\ :sub:`2` and redo the above. How have the results changed?

Connect the other inverters in the 74HC04 package in parallel with INV1 and INV2 in the diagram. What effect do these added drivers have on the results?

.. _directions-1:

Directions:
~~~~~~~~~~~

The breadboard connections for another version are as shown in figure 6 below. A one package of CMOS inverters is used for the upper set of switches (INV1 and INV2) rather than the discrete FETs and diodes. The ground connection of the 74HC04 at pin 7 is connected to the VIN node and the supply connection at pin 14 becomes the V\ :sub:`Boost` node. The voltage divider input should be connected to measure the voltage at V\ :sub:`Boost`. The +5V power supply should be connected to the V\ :sub:`IN` node. The LT1054 is used as both the clock digital pulse source and first driver output for capacitor C\ :sub:`1` and drives the input of the Inverter at the gates of NMOS M\ :sub:`1` and PMOS M\ :sub:`2`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab16_f6.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 6 All CMOS Inverter configuration


Figure 7 shows an inverting DC-DC configuration that produces V\ :sub:`Boost` equal to –V\ :sub:`IN`. The 74HC04 is connected below ground as shown to produce a V\ :sub:`Boost` that is equal to –V\ :sub:`IN`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab16_f7.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 7 Supply voltage inverter.


Digital pulse generator:
~~~~~~~~~~~~~~~~~~~~~~~~

What sort of circuit could you make to generate the 100 KHz square wave? There are four additional inverters in the 74HC04 package. The other inverters along with RC delay network, R\ :sub:`4` C\ :sub:`4` can be configured into a ring oscillator as shown below. The values for R\ :sub:`4` and C\ :sub:`4` are approximate for 100 KHz and can be adjusted as needed.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab16_f8.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 8 square wave oscillator


.. _questions-1:

Questions:
~~~~~~~~~~

What other types of oscillator circuits might be used to generate the 100 KHz square wave?

**For further reading:**

| :adi:`The Interleaved Inverting Charge Pump—Part 1: A New Topology for Low Noise Negative Voltage Supplies <en/analog-dialogue/articles/the-interleaved-inverting-charge-pump-part-1.html>`
| `Dc-DC Converter <http://en.wikipedia.org/wiki/DC-to-DC_converter>`__
| `Charge Pump <http://en.wikipedia.org/wiki/Charge_pump>`__
| `Capacitive voltage conversion aka the charge pump <https://www.radiolocman.com/review/article.html?di=619561>`__
| :adi:`ADM660,8660 Data Sheet <static/imported-files/data_sheets/ADM660_8660.pdf>`

Appendix:
~~~~~~~~~

Hex inverter Pinouts:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f3.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 9 74HC04 and CD4069 share the same package pinouts


CD4007 Pinout:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 10 CD4007 CMOS array pinout


As many as three individual inverters can be built from one CD4007 package. The simplest first one to configure as shown below is by connecting pins 8 and 13 together as the inverter output. Pin 6 will be the input. Be sure to connect pin 14 V\ :sub:`DD` to power and pin 7 V\ :sub:`SS` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm_lab20_f6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11 CD4007 inverter connections


The second Inverter is made by connecting pin 2 to V\ :sub:`DD`, pin 4 to V\ :sub:`SS`, pins 1 and 5 are connected together as the output and with pin 3 as the input.

The third inverter is made by connecting pin 11 to V\ :sub:`DD`, pin 9 to V\ :sub:`SS`, pin 12 is the output and pin 10 is the input.

Two of these inverters can be used to construct the inverters needed in figure 5.

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
