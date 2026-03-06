Measuring Voltages Outside 0-5 V Range with ADALM1000
=====================================================

Objective:
----------

The objective of this document is to provide information and techniques on how to measure voltages outside the native 0-5 V range of the ADALM1000 (M1k) while performing the Active Learning Lab activities.

General Notes:
--------------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

To keep production cost of the ADALM1000 Active Learning Module low, certain tradeoffs were made. One was to forego software programmable input gain ranges that use resistor dividers and perhaps adjustable frequency compensation capacitors. This is a problematic limitation of the ADALM1000 limiting the input voltage range to 0 to +5 V. Many users complain about this restriction when testing circuits powered by supply voltages other than (generally larger) the built in supplies.

Before building any circuits that operate from power supplies outside the native 0 to 5 V range of the ADALM1000 we need to protect the analog inputs when in Hi-Z mode and extend the usable range of voltages. There are large protection diodes connected between the analog I/O pins and ground and the internal +5 volt power supply which are generally reverse biased when the voltage on the pins are in the range of 0 to 5 V. If the voltage on the pin were to go more than a forward diode voltage beyond this range the diodes will turn on and possibly conduct large currents.

Input Divider Calculator
~~~~~~~~~~~~~~~~~~~~~~~~

The limitation on the allowable voltages that can be measured directly can be expanded through the use of an external voltage divider. To make calculating an input resistor divider's Gain and Offset values based on the resistor values used and offset connections a simple calculator window has been included in the ALICE tools (since release 1.3.14). The button directly above the Gain and Offset entries will open the calculator.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/input-divider-calculator.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure Div1, Input Divider Calculator.


Values for resistor R1 and resistor R2 are entered as well as any offset voltage that is applied to the bottom of the divider. The Exact values, as measured with a bench DMM, can be entered for R1 and R2 to calculate more accurate gain and offset results. The Rint internal 1 MegΩ resistance of the channels is taken into account in the calculation as this will have a significant effect for higher values of R1 and R2. Click the Calculate button to calculate the values. The Channel A or B entries can then be set to the calculated values using the Set CH A and Set CH B buttons respectively. These values can then of course be tweaked as needed for even better accuracy.

AC response of a divider
^^^^^^^^^^^^^^^^^^^^^^^^

The input capacitance, C\ :sub:`INT`, of the analog inputs in the high Z mode is approximately 390 pF (for the rev D design and slightly higher for the rev F design). This relatively large capacitance along with relatively high resistance dividers can significantly lower the frequency response. In figure 1 we revisit the input structure of the ADALM1000 and connecting an external resistive voltage divider R\ :sub:`1` and R\ :sub:`2,3`. The contents of the blue box represent the input of the ADALM1000 in Hi-Z mode. To introduce an optional DC offset for measuring negative voltages resistor R\ :sub:`2` is included and could be connected to either the fixed 2.5V or 5V supplies on the ADALM1000. The C\ :sub:`INT` and effective resistance of the divider network form a low pass pole in the frequency response.

.. note::

   The ADALM1000 (Rev. F version) has the ability to separate the voltage measurement connection from the voltage / current output pin, the Split I/O mode control in the AWG settings. The size of the parasitic capacitance is significantly different when using the CH A/B pins in Hi-Z mode vs using the AIN/BIN pins. The required external compensation capacitor value will be very different between the two pins.


To give you a rough idea let's use 400 pF for C\ :sub:`INT` and 1 MΩ for the resistor divider. That would result in a low pass response with a 3 dB roll-off starting at around 400 Hz. A capacitor would generally be needed across the input resistor R\ :sub:`1` to :doc:`frequency compensate the divider </wiki-migration/university/courses/alm1k/circuits1/alm-cir-voltage-divider>`. Such a hardware solution generally requires the capacitor (or alternatively the divider resistors) to be adjustable.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, External voltage divider options.


It would be nice to not have to use a compensation capacitor, adjustable or otherwise. The ALICE Desktop software can adjust for any DC gain and offset when using an external divider. A digital (software) frequency compensation feature is also included in ALICE 1.3 (down load the latest version from :git-alice:`GitHub <releases>`).

The software frequency compensation for each channel consists of a cascade of two adjustable `first order high pass filters <https://en.wikipedia.org/wiki/High-pass_filter#Algorithmic_implementation>`__. The time constant and the gain of each stage can be adjusted. Normal first order high pass filters do not pass DC so a DC gain of 1 path is added to the overall second order high pass software compensation filter. This structure is often called a shelving filter because of the shape of its frequency response.

|

.. tip::

   **Exponential compensation**

   | An Exponential compensation technique adds one or more exponentially decaying terms to a step in the signal. With 2 available stages, ALICE can correct for multiple spurious inductances and capacitances in the input divider circuit. Exponential compensation works best for overshoots and undershoots smaller than about 10% of the step height. In this case, a sum of exponential terms is an accurate generic model for such defects.


In figure 2 we show the controls for the input frequency compensation. To turn on and off the compensation for Channels A and B check boxes are available under the Curves drop down menu. Turning on compensation applies to both the Scope and Spectrum tools (time and frequency measurements). The filter time constant and gain settings can be set using entry slots in the Settings Controls screen.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, Software compensation controls


The following examples use resistor values from the ADAPL2000 Analog Parts Kit and the intention is to keep the input resistance equal to at least 1 MΩ. No external compensation capacitor was used. A 500 Hz square wave from the Channel A AWG output is used to observe the step response of the example resistor dividers and adjust the compensation filter settings.

As a simple first example we can just use a 1 MΩ resistor for R\ :sub:`1` and not include the other resistors, R\ :sub:`2`, R\ :sub:`3` from figure 1. This gives us a total input resistance of 2 MΩ.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, Settings for just 1.0 MΩ R\ :sub:`1`\


As we can see in figure 3, the DC gain setting is slightly more than 2 which is to be expected based on the internal 1 MΩ resistor and external 1 MΩ R\ :sub:`1` resistor forming a 2:1 voltage divider. There is a small DC offset due to the leakage current from the ESD protection diodes on the M1K inputs and the parallel combination of R\ :sub:`INT` and R\ :sub:`1`.

The input gain factor of 2 (2.17 to be exact) increases the allowable measurement range from 0 to +5 V to about 0 to +10 V. Enough to work with circuits powered from a 9 V battery for example.

The stage 1 filter Time Constant is adjusted to correct for the majority of the AC rolloff and the stage 2 filter Time Constant and Gain are tweeked to take out the remaining higher frequency (2nd order) roll off. A number of TC and Gain combinations are potentially possible and there may be more than one "right answer". The following screen shot in figure 4 shows the before and after response to a square wave input from AWG Channel A with and without compensation.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Single 1 MΩ R\ :sub:`1` with (orange), without (dark orange) compensation


A factor of 2X might not be enough of an increase in the maximum voltage to be measured. We might also like to measure negative voltages. For a second example we use two 470 KΩ resistors for R\ :sub:`2` and R\ :sub:`3` along with the 1 MΩ R\ :sub:`1`. R\ :sub:`2` is connected to the fixed +5V supply to introduce some positive offset.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5, Settings for R\ :sub:`1` = 1.0 MΩ, R\ :sub:`2,3` = 470KΩ


As we can see in figure 5, the DC gain setting is slightly more than 6 based on the internal 1 MΩ resistor in parallel with the equivalent parallel combination of the two 470 KΩ R\ :sub:`2,3` resistors (235 KΩ) and the external 1 MΩ R\ :sub:`1` resistor forming a voltage divider of about 6:1. The input range is now slightly more than 30 V p-p.

The Screen shot in figure 6 shows the step response for this divider configuration with and without compensation.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, R\ :sub:`1` = 1.0 MΩ, R\ :sub:`2,3` = 470KΩ with (orange), without (dark orange) compensation


For a third example with an even bigger input voltage range we can use a 200 KΩ resistor for R\ :sub:`2` and a 470 KΩ resistor R\ :sub:`3` along with the 1 MΩ R\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 7, Settings for R\ :sub:`1` = 1.0 MΩ, R\ :sub:`2`\ = 200 KΩ, R\ :sub:`3` = 470 KΩ


As we can see in figure 7, the DC gain setting is slightly more than 9 now which means that the input range is now slightly more than 45 V p-p. The offset nearly centers the range around ground (approx. +/- 20 V). The Screen shot in figure 8 shows the step response for this divider configuration with and without compensation.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, R\ :sub:`1` = 1.0 MΩ, R\ :sub:`2` = 200 KΩ, R\ :sub:`3` = 470 KΩ with (orange), without (dark orange) compensation


10X Scope Probes
^^^^^^^^^^^^^^^^

Finally, a common 10X (passive) scope probe can be used. To connect the probe to the Channel B input of the M1K just a BNC connector with short leads terminated in male pins is used. The input end of the probe is connected to the Channel A output to test/calibrate the divider as shown in the photo of figure 9. It is difficult to inject a DC offset when using the probe so the input voltage range will be just positive voltages up to 10X the 0-5 V native range of the M1k or 0 to +50 V.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9, scope probe connected to M1K


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-10.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10, Settings for 10X scope probe


The step response of the 10X probe without compensation is very poor. With compensation the step response lines up with the output of Channel A. The Screen shot in figure 11 shows the step response for 10X scope probe configuration with and without compensation.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-comp-figure-11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11, 10X scope probe with (orange), without (dark orange) compensation


With the software frequency compensation feature in ALICE 1.3 and a couple of resistors you can measure just about any range of voltages you need. Obvious first choices would be to use a 1 MΩ for R\ :sub:`1` and either 1 MΩ, 470 KΩ, 200 KΩ or 100 KΩ for R\ :sub:`2`\ with R\ :sub:`3` left open. It is good practice to keep one or more of these simple voltage dividers installed at one end of your breadboard (to keep it away from any high frequency switching noise from DC-DC power converters or regulators) for use at all times.

Appendix: Off the Shelf Voltage Dividers
----------------------------------------

The analog inputs on the Arduino microcontroller boards allow 0 to +5V input voltages much like the M1k and require a voltage divider to measure larger voltages. An online search for “Arduino voltage sensor divider” will turn up a number of pre-built resistor voltage divider adapter boards.

One such board is the `VOLT-01 <https://www.digikey.com/en/products/detail/osepp-electronics-ltd/VOLT-01/11198557?utm_adgroup=Development%20Boards%2C%20Kits%2C%20Programmers&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_DK%2BSupplier_Osepp%20Electronics&utm_term=&utm_content=Development%20Boards%2C%20Kits%2C%20Programmers&gclid=Cj0KCQjw1dGJBhD4ARIsANb6OdlkZCgeRSoYZKqV5LGRrLbT0YfXmNkRgO-4G41NY-cwy39Hv0l0oU0aApXIEALw_wcB>`__ available from Digikey by OSEPP Electronics LTD. The board and its schematic are shown in figure A1. The 5 to 1 voltage divider is made with 30 KΩ and 7.5 KΩ resistors which gives a total input resistance of 37.5 KΩ. That is much smaller than the M1k built in resistance of 1 MΩ and may load sensitive circuits but probably sufficiently high for measuring power supply voltages up +25V which is its stated purpose. As we can see in the schematic the input screw terminal ground (common) and the output pin header ground (common) are connected together and to the grounded end of the resistor divider (7.5K resistor) which does not allow for inserting a positive offset to allow measuring negative voltages.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-divider-fig-a1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A1, VOLT-01 5:1 voltage divider board


Another simple divider board, the DFR0051, is available through `Arrow <https://www.arrow.com/en/products/dfr0051/dfrobot>`__ and `Digikey <https://www.digikey.com/en/products/detail/dfrobot/DFR0051/6579310?s=N4IgTCBcDaICIDEBKAGFBWAjCAugXyA>`__ and `Newark <https://www.newark.com/dfrobot/dfr0051/analogue-voltage-divider-v2-arduino/dp/87AH5865>`__.

This also appears to be a 5:1 divider with the same 30 KΩ and 7.5 KΩ resistors and common input and output ground terminals but with the addition of an LED and 470 Ω series resistor connected across the input voltage terminals. The 470 Ω resistor seems a little small based on 25 V Max on the input, the LED current would be around 50 mA which would burn out most SMD LEDS. Also not something you would necessarily want across the thing you measuring. But once the LED burns out and becomes an open circuit that issue goes away.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-divider-fig-a2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A2, DFR0051 5:1 voltage divider board


This third option, the 36209-MP, available at `MPJA.com <https://www.mpja.com/Voltage-Divider-Module-for-Arduino/productinfo/36209%20MP/>`__ has a divider ratio of 0.18 (~5.55X) using 820 KΩ and 180 KΩ resistors. The 1 MΩ total input resistance is much better than the other two examples and close to the M1k’s built-in 1 MΩ. However, it too has the grounds terminals (commons) connected together and to the grounded end of the resistor divider (180K resistor) which does not allow for inserting a positive offset to allow measuring negative voltages.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/input-divider-fig-a3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A3, 36209-MP 5.55:1 voltage divider board


**For Further Reading:**

:doc:`ALICE Desk-top User's Guide </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
