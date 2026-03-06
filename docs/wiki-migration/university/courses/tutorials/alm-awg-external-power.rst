External Power Supplies for Active Learning Labs
================================================

Objective:
----------

The objective of this document is to provide a number of options for the generation of external power supply voltages to be used in conjunction with the ADALM1000 (M1k) or ADALM2000 (M2k) while performing Active Learning Lab activities where the built-in supplies may not provide the required supply voltage. Many of these techniques can be applied generically when using other USB based Personal Instrumentation devices (such as M1k or M2k)

Background:
-----------

Batteries are a simple and obvious external source of power for lab experiments that certainly fits the anywhere, anytime, low cost model to supply the needed higher voltages and currents. And batteries are inherently isolated so can float above or below any node, ground or other power rail. Standard 9 volt batteries and connectors are inexpensive and readily available. Holders for multiple (from one to eight) 1.5 volt AA or AAA cells are also common and relatively inexpensive. The major drawback with using conventional batteries is that they discharge over time and need to be replaced. Batteries also do not supply a constant voltage as they discharge (a reason to include the linear voltage regulators in the ADALP2000 parts kits). The problem of having to replace dead batteries can be solved to some extent by using rechargeable versions.

Another alternative external power source is to use one or more of the common AC wall plug power adapters (the so called “wall wart”). These power adapters come in a wide range of fixed DC or AC output voltage ratings from 3.3 V to 24 V and current from 200 mA to 3 or 4 Amps. The cost ranges from as little as $1.00 for a +5 V at 1.0 Amp USB charger or $3.00 to $15.00 for the higher voltage and current versions. Aside from needing to be plugged into the wall for power they fit into the anywhere, anytime, students own the hardware model. Figure B1 shows what a typical “wall wart” looks like. Some will have the standard coaxial barrel style DC power connectors and some will have USB connectors.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-figb1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure B1, Typical “wall wart” power adapter.


The simplest of these wall adapters are step-down transformers with DC rectifiers and rudimentary filtering that supply unregulated voltages. Others, which cost a little more, are switching power supplies with regulated fixed DC output voltages, 5V is common. The problem with these wall adapters is their outputs are not adjustable, are one polarity and might be unregulated.

ADALP2000 power related parts
-----------------------------

The ADALP2000 Analog Parts Kit contains a number of power supply related parts. In addition to the fixed ADP3300 3.3 V LDO regulator a few more parts that might help extend the power supply options have been included. One useful way to access more power is through the micro USB break-out board that can be plugged into the solderless breadboard. Using another USB cable (not supplied in the parts kit) plugged into a spare USB port (or USB wall charger) can provide an additional +5 V up to the current limit of the USB port or Hub.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-fig-b2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure B2, Micro USB break out board


**Caution!**

Powering your experimental circuits from an extra USB port on your computer can be hazardous and extreme care should be taken to not accidentally damage the computer or USB port power supply. It is important to note here, when using a spare USB port on the same computer that the M1k (or M2k) is plugged into, the ground side of the USB break-out board will be the same ground as (i.e. shorted to) the ground pin on the board (M1k / M2k).

A much safer option is to use a separate "wall wart" USB charger. Most all of these USB chargers (or any wall wart for that matter) are likely isolated so that the grounds will not be connected to anything else. The two leads, + and – can float and be attached to just about any node in your circuit. Most USB wall chargers with just two prong plugs will be isolated. To be doubly sure you can use an Ohmmeter or continuity tester (DMM) to check if either of the pins has a path back to the AC plug.

1.0 Measuring Voltages Outside 0-5 V Range:
-------------------------------------------

To keep production cost of the ADALM1000 board low, certain tradeoffs were made. One was to forego programmable input gain ranges that use resistor dividers and perhaps adjustable frequency compensation capacitors. This is a problematic limitation of the ADALM1000 limiting the input voltage range from 0 to +5 V. Users will come up against this restriction when testing circuits powered by (generally larger) supply voltages other than the built in supplies.

**One quick note of caution before proceeding!**

Before building any circuits that operate from power supplies outside the native 0 to 5 V range of the ADALM1000 you need to protect the analog inputs when in Hi-Z or Split I/O modes and extend the usable range of voltages. There are large protection diodes connected between the analog I/O pins and ground and the internal +5 volt power supply which are generally reverse biased when the voltage on the pins is in the range of 0 to 5 V. If the voltage on the pin were to go more than a forward diode voltage beyond this range the diodes will possibly conduct large currents.

Full details on how to construct external voltage divider can be found in this document: :doc:`Measuring voltages beyond 0 to 5V with the ADALM1000 (M1K) </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>` **It is highly recommended that you read and follow this document before attempting any experiments on circuits powered by voltage outside 0-5 V.**

2.0 Power Supply Options Using LTM8067 isolated μModule:
--------------------------------------------------------

A power supply related component from the parts kit is the isolated μModule (Power Module) `LTM8067 <http://www.analog.com/en/products/power-management/umodule-regulators/isolated-umodule-converters/ltm8067.html#product-overview>`__ based DC/DC Converter break-out board that can take a 3.1 V to 32V input (likely from a wall plug power adapter “wall wart”). A trim pot on the breakout board allows the output voltage to be manually adjusted from 2.5V to 15V. Because the output voltage pins are fully isolated the voltage can be either positive or negative depending on which pin is connected to common or ground. The output current can be as much as 440 mA (when VOUT = 2.5V).

.. image:: https://wiki.analog.com/_media/university/tools/adalp2000/bob_ltm8067.png
   :align: center
   :width: 320px

.. container:: centeralign

   Figure 2.0, Adjustable DC/DC Converter break-out board.


One of the simplest ways to create just about any supply voltage, positive or negative, is with the LTM8067 isolated μModule (Power Module) DC/DC Converter break-out board. Because the positive and negative output terminals are isolated from the input terminals the output voltage can be referenced to ground in either direction as shown in figure 2.1. The output voltage can be adjusted to any voltage from 3 V to 15 V with the on board potentiometer.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-fig-2-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2.1, Positive or negative output voltages


To use the LTM8067 module with the ADALM1000 built-in +5 V supply an inductor must be connected in series with the V\ :sub:`IN` terminal as shown in figure 2.2. Any value equal to or larger than 100 uH (marked 101) is sufficient to isolate the switching noise generated by the DC-DC converter from affecting the built-in +5 V supply driver.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-fig-2-2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2.2, Inductor isolates switcher noise


3.0 Power Supply Options Using LT1054 DC-DC converter:
------------------------------------------------------

A power supply related component from the parts kit is the `LT1054 Switched-Capacitor Voltage Converter with Regulator <http://www.analog.com/en/products/power-management/inductorless-charge-pump-dc-dc-converters/regulated-step-up-charge-pumps/lt1054.html>`__ which can be used with just two capacitors as a voltage inverter to make -5 V from +5 V or with external diodes as a voltage multiplier to make larger positive and or negative voltages. Using the LT1054 to generate negative voltages such as -5 V and -9.0 V from the +5 V supply in the M1k is particularly useful because the M1k lacks a built-in negative supply. The LT1054 can also be used as a :doc:`9V battery voltage "Rail-Splitter" </wiki-migration/university/courses/alm1k/circuits1/alm_cir_lab-rail-splitter>`.

In this section we cover many of the ways the LT1054 switched capacitor DC-DC converter can be configured to produce multiple supply voltages. Refer to the `LT1054 datasheet <http://www.analog.com/en/products/power-management/inductorless-charge-pump-dc-dc-converters/regulated-step-up-charge-pumps/lt1054.html>`__ for complete application information. The ADM660 is a similar CMOS switched capacitor DC-DC converter and can be used in much the same way.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 – LT1054 Switch Cap DC-DC converter (or ADM660)
| 2 – 4.7 uF capacitors
| 2 – 10 uF capacitors
| 2 – 22 uF capacitors
| 2 – 47 uF capacitors
| 5 – 1N4001 diodes (or 1N5819 Schottky diodes)

Directions:
~~~~~~~~~~~

The first and simplest configuration for the LT1054 is the voltage inverter shown in figure 3.1. It can generate -5 V from the +5 volt power supply using just two capacitors. C<sub>1</sub is typically 10 uF and C\ :sub:`2` can be anything larger than 47uF. When using electrolytic capacitors be sure to observe the polarity and connect the capacitor with the correct polarity. If connected backward, at best the circuit won't work, at worst you can damage either the capacitor or LT1054.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-fig-3-1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.1, Voltage Inverter to generate -5 V


Making the output adjustable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The negative output voltage can be adjusted from approximately 0 to –5 V by adding a potentiometer circuit as shown in figure 3.2. Resistor R\ :sub:`1` is 10 KΩ, resistor R\ :sub:`2` is 20 KΩ and potentiometer R\ :sub:`POT` is 50 KΩ. Noise filter capacitor C\ :sub:`3` is 0.01 uF.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-fig-3-2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3.2, Adjustable Voltage Inverter


Software Adjustable DC source:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rather than using a mechanical potentiometer it might be desirable to adjust the negative output voltage through software. The ADALP2000 Analog Parts Kit also includes an AD5626 12 bit DAC break-out-board, figure 3.2b, that can be used to provide an adjustable DC voltage source. The 0 to 4 V output (1 mV/bit with a 4.095 V full scale) of the AD5626 serial interface DAC can be programed through the controls built into the ALICE desktop software. Set the EnableAD5626SerialMode = 1 option in the alice_init.ini start-up file.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig1b.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 3.2b, AD5626 DAC bread-out-board


The SCLK, SDIN and LDAC BAR inputs are controlled by three of the digital outputs from the ADALM1000 digital connector, figure 3.2c.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-signal-sources-fig1c.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3.2c, AD5626 DAC interface connections


To use the AD5626 to set the negative output voltage of the LT1054, we can substitute the adjustable DAC output for the fixed 2.5V internal reference voltage of the LT1054 (pin 6, Vref) and replace R\ :sub:`1`, R\ :sub:`2`, and R\ :sub:`POT` with fixed resistors as in figure 3.2d. With R\ :sub:`1` = 10KΩ and R\ :sub:`2` = 22KΩ the negative output voltage can be adjusted from 0 to –5 V by setting the DAC output voltage from 1.9 V to 4.095 V (full scale).

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-fig-3-2d.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3.2d, LT1054 connected to AD5626 DAC


Positive Voltage Doubler
~~~~~~~~~~~~~~~~~~~~~~~~

A second configuration for the LT1054 is the positive voltage doubler shown in figure 3.3. This scheme does not generate the full +10 V output because of the forward drop of the two diodes. Using Schottky diodes such as the 1N5819 for D\ :sub:`1` and D\ :sub:`2` can reduce this voltage loss to around 0.5 V rather than as much as 1.2 V with conventional diodes. C\ :sub:`1` is typically 10 uF and C\ :sub:`2` can be anything larger than 47uF.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-fig-3-3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.3, Voltage Doubler to generate +9.0 V


The configuration shown in figure 3.4, can generate both positive and negative voltages and is useful when working with non rail-to-rail amplifiers. The added 1.3 volts outside the 0 and 5 volts generally means that the amplifier output can still swing all the way from 0 to 5 V. Note that the polarity of D\ :sub:`3` and D\ :sub:`4` are reversed with respect to D\ :sub:`1` and D\ :sub:`2` to generate a negative voltage. Again using Schottky diodes such as the 1N5819 for D\ :sub:`1-4` can reduce the voltage loss to around 0.5 V and generate closer to +7 V and -2 V.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-fig-3-4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3.4, Use +2.5 V to generate +6.3 V and -1.3 V


A second set of voltage doubling diodes and boosting capacitor can be added to the configuration of figure 3.3 to make an even larger positive voltage as shown in figure 3.5. Again using Schottky diodes such as the 1N5819 for D\ :sub:`1-4` can reduce the total voltage loss to around 2 times 0.5 V and generate closer to +9.5 V and +14.0 V.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-fig-3-5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3.5, Voltage Doubler and Tripler to generate +9.0 V and +13 V


With the LT1054 connected to generate -5V and the diodes of the voltage doubler referenced to -5 V the configuration shown in figure 3.6, generates –9 volts.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-fig-3-6.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 3.6, Negative Voltage Doubler to generate -5 V and -9.0 V


Combining parts from figure 3.3 and figure 3.6 we can build the +/- 9 volt supply circuit shown in figure 3.7.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-fig-3-7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.7, LT1054 simultaneously generating +9.0, -5 and -9.0 from +5


Option 4, Linear Regulators:
----------------------------

In addition to the ADP3300 fixed 3.3 V LDO regulator, the ADALP2000 kit also includes the `LT3080 <http://www.analog.com/en/products/power-management/current-sources/lt3080.html>`__ adjustable linear voltage regulator (LDO) which can be programmed using a single resistor to set the output voltage from 0 to V\ :sub:`IN` - 1.2 V (i.e V\ :sub:`IN` must be at least 1.2 V greater than V\ :sub:`OUT`). It can source up to 1.1 A (with an appropriate heat-sink). The TO-220 package version is supplied in the kit which has staggered leads that need to be bent slightly to fit into a solderless breadboard. Inserted on the breadboard in the photo below is a LT3080 with the leads bent and bolted to a small heat-sink. A 9 V battery supplies the input voltage and the 500 KΩ pot will adjust the output voltage from 0 to 5 V. The 9 V battery holder has a built-in on-off switch is handy.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-fig-4-1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4.1, LT3080 inserted in breadboard with heat sink


The LT3080 produces an output voltage that is equal to the voltage on the SET pin. This voltage is set usually by the 10 uA current and the external resistor. It can also be driven to the required output voltage as shown in figure 4.2 using the AD5626 serial DAC as an example,

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ext-power-fig-4-2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4.2, LT3080 SET driven by AD5626 DAC


**For Further Reading:**

| `Voltage multiplier <https://en.wikipedia.org/wiki/Voltage_multiplier>`__
| `Charge pump <https://en.wikipedia.org/wiki/Charge_pump>`__
| `Voltage doubler <https://en.wikipedia.org/wiki/Voltage_doubler>`__
| `ADM660 Datasheet <http://www.analog.com/media/en/technical-documentation/data-sheets/ADM660_8660.pdf>`__
| :adi:`LT1054 datasheet <en/products/power-management/inductorless-charge-pump-dc-dc-converters/regulated-step-up-charge-pumps/lt1054.html>`
| :adi:`AD5626 datasheet <AD5626>`

**Return to Lab Activity Table of Contents**
