Activity: External Power Supplies for Active Learning Labs
==========================================================

Objective:
----------

The objective of this document is to provide a number of options for the generation of external power supply voltages to be used in conjunction with the ADALM1000 (M1k) while performing Active Learning Lab activities where the built-in fixed 2.5 V and 5 V supplies may not provide the required supply voltage.

General Notes:
--------------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

The ADALP2000 Analog Parts Kit contains a number of power supply related parts. In addition to the ADP3300 3.3 V LDO regulator a few more parts that might help extend the power supply options have been included. One useful way to access more power is through the micro USB break-out board that can be plugged into the solderless breadboard. Using another USB cable (not supplied in the parts kit) plugged into a spare USB port (or USB wall charger) can provide an additional +5 V up to the current limit of the USB port.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-external-power-supplies-fig1.png
   :align: center
   :width: 400px

**Caution!**

Connecting your experimental circuits to an extra USB port on your computer can be hazardous and extreme care should be taken to not accidentally damage the computer or USB port power supply. It is important to note here, when using a spare USB port on the same computer that the M1k or M2k is plugged into, the ground side of the USB break-out board will be the same ground as (i.e. shorted to) the ground pin on the board (M1k or M2k).

A much safer option is to use a separate "wall wart" USB charger. Most all of these USB chargers (or any wall wart for that matter) are likely isolated so that the grounds will not be connected to anything else. The two leads, + and – can float and be attached to just about any node in your circuit. Most USB wall chargers with just two prong plugs will be isolated. To be doubly sure you can use an Ohmmeter or continuity tester to check if either of the pins has a path back to the AC plug.

A second power supply related part included in the kit is the :adi:`LT1054 Switched-Capacitor Voltage Converter with Regulator <en/products/power-management/inductorless-charge-pump-dc-dc-converters/regulated-step-up-charge-pumps/lt1054.html>` which can be used with just two capacitors as a voltage inverter to make -5 V from +5 V or with external diodes as a voltage multiplier to make larger positive and or negative voltages.

Using the LT1054 to generate negative voltages such as -5 V and -9.0 V from the +5 V supply in the M1k is particularly useful because the M1k lacks a built-in negative supply.

A third power supply related component is the :adi:`isolated μModule <en/products/power-management/umodule-regulators/isolated-umodule-converters/ltm8047.html#product-overview>` (Power Module) DC/DC Converter break-out board that can take a 3.1 V to 32V input. A trim pot on the breakout board allows the output voltage to be adjusted from 2.5V to 12V. Because the output voltage pins are fully isolated the voltage can be either positive or negative depending on which pin is connected to ground. The output current can be as much as 440 mA (when V\ :sub:`OUT` = 2.5V).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-external-power-supplies-fig2.png
   :align: center
   :width: 350px

.. container:: centeralign

   Adjustable DC/DC Converter break-out board


The fourth power supply related component is the :adi:`LT3080 <en/products/power-management/current-sources/lt3080.html>` adjustable linear voltage regulator (LDO) which can be programmed using a single resistor to set the output voltage from 0 to V\ :sub:`IN` - 1.2 V (i.e V\ :sub:`IN` must be 1.2 V greater than V\ :sub:`OUT`). It can source up to 1.1 A.

1.0 Measuring Voltage Outside 0-5 V Range:
------------------------------------------

To keep production cost of the ADALM1000 board low, certain tradeoffs were made. One was to forego programmable input gain ranges that use resistor dividers and perhaps adjustable frequency compensation capacitors. This is a problematic limitation of the ADALM1000 limiting the input voltage range from 0 to +5 V. Many users complain about this restriction when testing circuits powered by supply voltages other than (generally larger) the built in supplies.

Before building any circuits that operate from power supplies outside the native 0 to 5 V range of the ADALM1000 we need to protect the analog inputs when in Hi-Z mode and extend the usable range of voltages. There are large protection diodes connected between the analog I/O pins and ground and the internal +5 volt power supply which are generally reverse biased when the voltage on the pins are in the range of 0 to 5 V. If the voltage on the pin were to go more than a forward diode voltage beyond this range the diodes will possibly conduct large currents.

The limitation on the allowable voltages that can be measured directly can be expanded through the use of an external voltage divider. The input capacitance, C\ :sub:`INT`, of the analog inputs in the high Z mode is approximately 390 pF (for the rev D design and slightly higher for the rev F design). This relatively large capacitance along with relatively high resistance dividers can significantly lower the frequency response. In figure 1.1 we revisit the input structure of the ADALM1000 and connecting an external resistive voltage divider R\ :sub:`1` and R\ :sub:`2,3`. The contents of the blue box represent the input of the ADALM1000 in Hi-Z mode. To introduce an optional DC offset for measuring negative voltages resistor R\ :sub:`2` is included and could be connected to either the fixed 2.5V or 5V supplies on the ADALM1000. The C\ :sub:`INT` and effective resistance of the divider network form a low pass pole in the frequency response. To give you a rough idea let's use 400 pF for C\ :sub:`INT` and 1 MΩ for the resistor divider. That would result in a low pass response with a 3 dB roll-off starting at around 400 Hz, A capacitor would generally be needed across the input resistor R\ :sub:`1` to :doc:`frequency compensate the divider </wiki-migration/university/courses/alm1k/circuits1/alm-cir-voltage-divider>`. Such a hardware solution generally requires the capacitor (or alternatively the divider resistors) to be adjustable.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1.1, External voltage divider options.


It would be nice to not have to use a compensation capacitor, adjustable or otherwise. The ALICE Desktop can adjust for any DC gain and offset when using an external divider. A digital (software) frequency compensation feature is also included in the ALICE 1.2 Desktop software package (down load the latest version from :git-alice:`GitHub <releases>`).

The software frequency compensation for each channel consists of a cascade of two adjustable `first order high pass filters <https://en.wikipedia.org/wiki/High-pass_filter#Algorithmic_implementation>`_. The time constant and the gain of each stage can be adjusted. Normal first order high pass filters do not pass DC so a DC gain of 1 path is added to the overall second order high pass software compensation filter. This structure is often called a shelving filter because of the shape of its frequency response.

In figure 1.2 we show the controls for the input frequency compensation. To turn on and off the compensation for Channels A and B check boxes are added under the Curves drop down menu. Turning on compensation applies to both the Scope and Spectrum tools (time and frequency measurements). The filter time constant and gain settings can be set using new entry slots in the Settings Controls screen. The DC gain and offset adjust controls are unchanged.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.2, Software compensation controls


The following examples use resistor values from the ADAPL2000 Analog Parts Kit and the intention is to keep the input resistance equal to at least 1 MΩ. No external compensation capacitor was used. A 500 Hz square wave from the Channel A AWG output is used to observe the step response of the example resistor dividers and adjust the compensation filter settings.

As a simple first example we can just use the 1 MΩ R\ :sub:`1` resistor and not include the other resistors from figure 1.1. This gives us a total input resistance of 2 MΩ.

{{ :university:courses:alm1k:circuits1:input-comp-figure-3.png?500 \|}

.. container:: centeralign

   Figure 1.3, Settings for just 1.0 MΩ R\ :sub:`1`\


As we can see in figure 1.3, the DC gain setting is slightly more than 2 which is to be expected based on the internal 1 MΩ resistor and external 1 MΩ R\ :sub:`1` resistor forming a 2:1 voltage divider. There is a small DC offset due to the leakage current from the ESD protection diodes on the M1k inputs and the parallel combination of R\ :sub:`INT` and R\ :sub:`1`.

The input gain factor of 2 (2.17 to be exact) increases the allowable measurement range from 0 to +5 V to about 0 to +10 V. Enough to work with circuits powered from a 9 V battery for example. The stage 1 filter Time Constant is adjusted to correct for the majority of the AC rolloff and the stage 2 filter Time Constant and Gain are tweeked to take out the remaining higher frequency (2nd order) roll off. A number of TC and Gain combinations are potentially possible and there may be more than one "right answer". The following screen shot in figure 1.4 shows the before and after response to a square wave input from AWG Channel A with and without compensation.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1.4, Single 1 MΩ R\ :sub:`1` with (orange), without (dark orange) compensation


A factor of 2X might not be enough of an increase in the maximum voltage to be measured. We might also like to measure negative voltages. For a second example we use two 470 KΩ resistors for R\ :sub:`2` and R\ :sub:`3` along with the 1 MΩ R\ :sub:`1`. R\ :sub:`2` is connected to the fixed +5V supply to introduce some positive offset.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.5, Settings for R\ :sub:`1` = 1.0 MΩ, R\ :sub:`2,3` = 470KΩ


As we can see in figure 1.5, the DC gain setting is slightly more than 6 based on the internal 1 MΩ resistor in parallel with the equivalent parallel combination of the two 470 KΩ R\ :sub:`2,3` resistors (235 KΩ) and the external 1 MΩ R\ :sub:`1` resistor forming a voltage divider of about 6:1. The input range is now slightly more than 30 V p-p.

The Screen shot in figure 1.6 shows the step response for this divider configuration with and without compensation.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1.6, R\ :sub:`1` = 1.0 MΩ, R\ :sub:`2,3` = 470KΩ with (orange), without (dark orange) compensation


For a third example with an even bigger input voltage range we can use a 200 KΩ resistor for R\ :sub:`2` and a 470 KΩ resistor R\ :sub:`3` along with the 1 MΩ R\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.7, Settings for R\ :sub:`1` = 1.0 MΩ, R\ :sub:`2`\ = 200 KΩ, R\ :sub:`3` = 470 KΩ


As we can see in figure 1.7, the DC gain setting is slightly more than 9 now which means that the input range is now slightly more than 45 V p-p. The offset nearly centers the range around ground (approx. +/- 20 V).

The Screen shot in figure 1.8 shows the step response for this divider configuration with and without compensation.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1.8, R\ :sub:`1` = 1.0 MΩ, R\ :sub:`2` = 200 KΩ, R\ :sub:`3` = 470 KΩ with (orange), without (dark orange) compensation


Finally, a common 10X (passive) scope probe can be used. To connect the probe to the Channel B input of the M1k just a BNC connector with short leads terminated in male pins is used. The input end of the probe is connected to the Channel A output to test/calibrate the divider as shown in the photo 1.9. It is difficult to inject a DC offset when using the probe so the input voltage range will be just positive voltages up to 10X the 0-5 V native range of the M1k or 0 to +50 V.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.9, scope probe connected to M1k


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-10.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1.10, Settings for 10X scope probe


The step response of the 10X probe without compensation is very poor. With compensation the step response lines up with the output of Channel A. The Screen shot in figure 1.11 shows the step response for 10X scope probe configuration with and without compensation.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1.11, 10X scope probe with (orange), without (dark orange) compensation


With the software frequency compensation feature in ALICE 1.2 and a couple of resistors you can measure just about any range of voltages you need. Obvious first choices would be to use a 1 MΩ for R\ :sub:`1` and either 1 MΩ, 470 KΩ, 200 KΩ or 100 KΩ for R\ :sub:`2`\ with R\ :sub:`3` left open. It is good practice to keep one or more of these simple voltage dividers installed at one end of your breadboard (to keep it away from any high frequency switching noise from DC-DC power converters or regulators) for use at all times.

2.0 Power Supply Option, LTM8067 isolated μModule:
--------------------------------------------------

One of the simplest ways to create just about any supply voltage, positive or negative, is with the LTM8067 isolated μModule (Power Module) DC/DC Converter break-out board. Because the positive and negative output terminals are isolated from the input terminals the output voltage can be referenced to ground in either direction as shown in figure 2.1. The output voltage can be adjusted to any voltage from 3 V to 15 V with the on board potentiometer.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-external-power-supplies-fig2-1.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2.1, Positive or negative output voltages


To use the LTM8067 module with the ADALM1000 built-in +5 V supply an inductor must be connected in series with the V\ :sub:`IN` terminal as shown in figure 2.2. Any value equal to or larger than 100 uH (marked 101) is sufficient to isolate the switching noise generated by the DC-DC converter from affecting the built-in +5 V supply driver.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-external-power-supplies-fig2-2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2.2, Inductor isolates switcher noise


3.0 Power Supply Options, LT1054 DC-DC converter:
-------------------------------------------------

In this section we cover many of the ways the LT1054 switched capacitor DC-DC converter can be configured to produce multiple supply voltages. Refer to the :adi:`LT1054 datasheet <en/products/power-management/inductorless-charge-pump-dc-dc-converters/regulated-step-up-charge-pumps/lt1054.html>` for complete application information. The ADM660 is a similar CMOS switched capacitor DC-DC converter and can be used in much the same way.

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

The first and simplest configuration for the LT1054 is the voltage inverter shown in figure 3.1. It can generate -5 V from the +5 volt power supply using just two capacitors. C\ :sub:`1` is typically 10 uF and C\ :sub:`2` can be anything larger than 47uF. When using electrolytic capacitors be sure to observe the polarity and connect the capacitor with the correct polarity. If connected backward, at best the circuit won't work, at worst you can damage either the capacitor or LT1054.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-external-power-supplies-fig3-1.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 3.1, Voltage Inverter to generate -5 V


The negative output voltage can be adjusted from approximately 0 to – 5 V by adding a potentiometer circuit as shown in figure 3.2. Resistor R\ :sub:`1` is 10 KΩ, resistor R\ :sub:`2` is 20 KΩ and potentiometer R\ :sub:`POT` is 50 KΩ. Noise filter capacitor C\ :sub:`3` is 0.01 uF.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-external-power-supplies-fig3-2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.2, Adjustable Voltage Inverter


A second configuration for the LT1054 is the positive voltage doubler shown in figure 3.3. This scheme does not generate the full +10 V output because of the forward drop of the two diodes. Using Schottky diodes such as the 1N5819 for D\ :sub:`1` and D\ :sub:`2` can reduce this voltage loss to around 0.5 V rather than as much as 1.2 V with conventional diodes. C\ :sub:`1` is typically 10 uF and C\ :sub:`2` can be anything larger than 47uF.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-external-power-supplies-fig3-3.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 3.3, Voltage Doubler to generate +9.0 V


The configuration shown in figure 3.4, can generate both positive and negative voltages and is useful when working with non rail-to-rail amplifiers. The added 1.3 volts outside the 0 and 5 volts generally means that the amplifier output can still swing all the way from 0 to 5 V. Note that the polarity of D\ :sub:`3` and D\ :sub:`4` are reversed with respect to D\ :sub:`1` and D\ :sub:`2` to generate a negative voltage. Again using Schottky diodes such as the 1N5819 for D\ :sub:`1`, D\ :sub:`2`, D\ :sub:`3` and D\ :sub:`4` can reduce the voltage loss to around 0.5 V and generate closer to +7 V and -2 V.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-external-power-supplies-fig3-4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3.4, Use +2.5 V to generate +6.3 V and -1.3 V


A second set of voltage doubling diodes and boosting capacitor can be added to the configuration of figure 2.2 to make an even larger positive voltage as shown in figure 3.5. Again using Schottky diodes such as the 1N5819 for D\ :sub:`1`, D\ :sub:`2`, D\ :sub:`3` and D\ :sub:`4` can reduce the total voltage loss to around 2 times 0.5 V and generate closer to +9.5 V and +14.0 V.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-external-power-supplies-fig3-5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3.5, Voltage Doubler and Tripler to generate +9.0 V and +13 V


With the LT1054 connected to generate -5V and the diodes of the voltage doubler referenced to -5 V the configuration shown in figure 3.6, generates –9 volts.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-external-power-supplies-fig3-6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.6, Negative Voltage Doubler to generate -5 V and -9.0 V


Combining parts from figure 3.3 and figure 3.6 we can build the +/- 9 volt supply circuit shown in figure 2.7.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-external-power-supplies-fig3-7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3.7 LT1054 simultaneously generating +9.0, -5 and -9.0 from +5


Option 4, Linear Regulators:
----------------------------

**For Further Reading:**

| `Voltage multiplier <https://en.wikipedia.org/wiki/Voltage_multiplier>`_
| `Charge pump <https://en.wikipedia.org/wiki/Charge_pump>`_
| `Voltage doubler <https://en.wikipedia.org/wiki/Voltage_doubler>`_
| :adi:`ADM660 Datasheet <media/en/technical-documentation/data-sheets/ADM660_8660.pdf>`
| :adi:`LT1054 Datasheet <media/en/technical-documentation/data-sheets/1054lfh.pdf>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
