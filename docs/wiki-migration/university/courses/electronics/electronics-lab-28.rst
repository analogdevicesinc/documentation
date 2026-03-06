Build CMOS Logic Functions Using CD4007 Array - ADALM2000
=========================================================

Objective:
----------

The objective of this lab activity is to build the various CMOS logic functions possible with the CD4007 transistor array. The CD4007 contains 3 complementary pairs of NMOS and PMOS transistors.

Making inverters with the CD4007 transistor array
-------------------------------------------------

Below in figure 1 is the schematic and pinout for the CD4007:

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1 CD4007 CMOS transistor array pinout


As many as three individual inverters can be built from one CD4007 package. The simplest first one to configure as shown below is by connecting pins 8 and 13 together as the inverter output. Pin 6 will be the input. Be sure to connect pin 14 V\ :sub:`DD` to power and pin 7 V\ :sub:`SS` to ground.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2 Three Inverters


The second Inverter is made by connecting pin 2 to V\ :sub:`DD`, pin 4 to V\ :sub:`SS`, pins 1 and 5 are connected together as the output and with pin 3 as the input. The third inverter is made by connecting pin 11 to V\ :sub:`DD`, pin 9 to V\ :sub:`SS`, pin 12 is the output and pin 10 is the input.

Characterizing The CMOS Inverter
--------------------------------

There are a number of both static (DC) and dynamic (AC) performance characteristics of the CMOS inverter that are often specified and should be measured. In this section we will measure a number of them for the inverter but these same measurements can be made on other the types gates we will see in later sections of this activity. We will start with the static characteristics, threshold voltage, transition region width, output source and sink current.

Threshold voltage:
------------------

Generally the CMOS fabrication process is designed such that the threshold voltage, V\ :sub:`TH`, of the NMOS and PMOS devices are roughly equal i.e. complementary. The designer of the inverter then adjusts the width to length ratio, W/L, of the NMOS and PMOS devices such that their respective transconductance is also equal.

Directions:
-----------

On your solder-less breadboard build the first inverter shown in figure 2 to test the input to output switching characteristics of the CMOS inverter. The green boxes in figure 3 indicate the required connections to the connector on ADALM2000. Connect Vp (+5V) power to V\ :sub:`DD` (pin 14) through a 100Ω resistor to measure the supply current and ground to V\ :sub:`SS` (pin 7). Connect the output of the waveform generator to the inverter input (pin 6) along with scope input 1+ and connect the inverter output (pins 8,13) to scope input 2+. It is also generally good to ground the unused negative scope inputs (1- , 2-).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f3.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 3 Setup to measure input threshold and transition region


Hardware Setup:
---------------

Configure the waveform generator for a 100 Hz triangle wave with 5V amplitude peak-to-peak and 2.5V offset. Both scope channels should be set to 1V/Div. Configure the scope in XY mode with channel 1 on the horizontal axis and channel 2 on the vertical axis.


|image1|

.. container:: centeralign

   Figure 4 Breadboard connections Setup to measure input threshold and transition region


Procedure:
----------

First using scope channel 2 to measure the inverter output voltage vs. the input as the input is swept from 0 to 5V obtain a plot like the top curve in figure 5. Export the data to a .csv file and extract the width of the transition region and the threshold voltage at the input at the point where the output voltage is exactly 1/2 V\ :sub:`DD`.

Next move the channel 2 scope inputs 2+ and 2- to measure the voltage across the 100Ω resistor, R\ :sub:`1`, in figure 3. You may need to adjust the vertical scale of channel 2 for an optimal view of the current waveform. Now obtain a plot of I\ :sub:`D` vs. the input as the input is swept from 0 to 5V. This should give you a plot much like the bottom curve in figure 5. Export the data to a .csv file and extract the peak current ( measured voltage divided by the 100Ω resistor value) and the input and output voltages where the peak occurred.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f4.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 5 Inverter output voltage and supply current curves vs. input voltage


   |image2|

.. container:: centeralign

   Figure 6 Scopy screenshots: Inverter output voltage and supply current curves vs. input voltage


The input to output transfer characteristic plots the output voltage V\ :sub:`OUT` versus the input voltage V\ :sub:`IN`. Notice that when the input voltage increase from 0V to 5V the output voltage decreases from 5V to 0V. The supply current characteristic plots the current flowing through the transistors between V\ :sub:`DD` and ground also versus the input voltage V\ :sub:`IN`. The fact that there are two parts of the characteristic curves when the input voltage is near ground and V\ :sub:`DD`, no current flows between V\ :sub:`DD` and ground, is very attractive because there is no power dissipation at this stages. This very fact is the reason that today nearly all digital circuitry is now build using CMOS technology.

The width of the transition region as a fraction of the power supply leads to a performance measure that is often referred to as the noise margin, the part of the input range where the output remains at a constant high or low level. Given that there is likely to be noise superimposed on the input signal it is desirable to have the output not respond to small changes in the input. A narrow transition region also potentially reduces the amount of time the output spends transitioning between states and thus the so called "shoot through" current when both the NMOS and PMOS transistors are partially turned on.

Dynamic performance
-------------------

In this section we will investigate the dynamic properties of the CMOS inverter, that is, its behavior during the time when switching the input signal from low-to-high or high-to-low voltages and the associated power dissipation.

We now consider a CMOS inverter driven by a voltage pulse. Typical input/output waveforms are shown in figure 5. Delay characterization of the dynamic behavior of an inverter is given by two propagation delay times, T\ :sub:`HL` and T\ :sub:`LH` as illustrated in figure 7. Note that these propagation times are specified with respect to the mid supply voltage V\ :sub:`DD`/2.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f5.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 7 CMOS Inverter propagation delay


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8 CMOS Inverter rise / fall time


.. _hardware-setup-1:

Hardware Setup:
---------------

Now configure the waveform generator for a 500 KHz square wave with 5V amplitude peak-to-peak and 2.5V offset. Be sure to reconnect scope channel 2 to measure the output voltage waveform. Both scope channels should be set to 1V/Div. Adjust the horizontal scale so that you can view both the rising and falling edges of the input and output waveforms similar to what is shown in figures 7 and 8.


|image3|

.. container:: centeralign

   Figure 9 CMOS inverter Breadboard connections


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f10a.JPG
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10 Scopy screenshot: CMOS Inverter propagation delay


Measurements:
-------------

Propagation delay, T\ :sub:`HL` and T\ :sub:`LH` = time between input transition (when V\ :sub:`IN` = V\ :sub:`DD`/2) and output transition (when V\ :sub:`OUT` = V\ :sub:`DD`/2). Rise time, T\ :sub:`R` = time for a waveform to rise from 10% to 90% of its steady state value. Fall time, T\ :sub:`F` = time for a waveform to fall from 90% to 10% of its steady state value.

Making a CMOS Schmitt Trigger with the CD4007 transistor array
--------------------------------------------------------------

The input of the Schmitt trigger, as shown in figure 11, is tied to the gates of four stacked devices. The upper two are PMOS and the lower two are NMOS. Transistors M\ :sub:`5` and M\ :sub:`6` operate as source followers and introduce hysteresis by feeding back the output voltage, V\ :sub:`OUT`, to the two points in the stack midway between the two NMOS and two PMOS devices.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11 CMOS Schmitt trigger circuit


When V\ :sub:`IN` is at 0V, transistors M\ :sub:`1` and M\ :sub:`3` are on, and M\ :sub:`2`, M\ :sub:`4` and M\ :sub:`5` are off. Since V\ :sub:`OUT` is high, M\ :sub:`6` is on and acts as a source follower, the drain of M\ :sub:`2`, which is also the source of M\ :sub:`4`, is at V\ :sub:`DD` - V\ :sub:`TH`. If the input voltage is ramped up to one threshold above ground transistor M\ :sub:`2` begins to turn on, M\ :sub:`2` and M\ :sub:`6` both being on form a voltage divider network biasing the source of M4 at roughly half the supply. When the input is a threshold above 1/2 V\ :sub:`DD`, M\ :sub:`4` begins to turn on and regenerative switching is about to take over. Any more voltage on the input causes V\ :sub:`OUT` to drop. When V\ :sub:`OUT` drops, the source of M\ :sub:`6` follows its gate, which is V\ :sub:`OUT`, the influence of M\ :sub:`6` in the voltage divider with M\ :sub:`2` rapidly diminishes, bringing V\ :sub:`OUT` down further yet. Meanwhile M\ :sub:`5` has started to turn on, its gate being brought low by the rapidly dropping V\ :sub:`OUT`. M\ :sub:`5` turning on brings the source of M\ :sub:`3` low and turns M\ :sub:`3` off. With M\ :sub:`3` off, V\ :sub:`OUT` will collapse all the way down to ground. The snapping action is due to greater than unity loop gain through the stack caused by positive feedback through the source follower transistors. When the input is brought low again a similar process occurs in the upper portion of the stack and the snapping action takes place when the lower threshold its reached.

.. _directions-1:

Directions:
-----------

On your solder-less breadboard build the Schmitt trigger circuit shown in figure 11 to test the input to output switching characteristics as you did with the plain inverter.

.. _hardware-setup-2:

Hardware Setup:
---------------

Configure the waveform generator for a 1 KHz triangle wave with 5V amplitude peak-to-peak and 2.5V offset. Both scope channels should be set to 1V/Div. Configure the scope in XY mode with channel 1 on the horizontal axis and channel 2 on the vertical axis.


|image4|

.. container:: centeralign

   Figure 12 CMOS Schmitt trigger circuit breadboard connections


.. _procedure-1:

Procedure:
----------

Use scope channel 2 to measure the output voltage vs. the input as the input is swept from 0 to 5V obtain a plot like you did for the simple inverter. Export the data to a .csv file and extract the upper and lower threshold voltages and the width of the hysteresis region. Is the hysteresis region centered around 1/2 V\ :sub:`DD`?


|image5|

.. container:: centeralign

   Figure 13 CMOS Schmitt trigger Scopy plot


Making a NAND / AND gate with the CD4007 transistor array
---------------------------------------------------------

As shown in figure 14, one 2 input NAND gate and one inverter can be built from one CD4007 package. Configure the NAND gate as shown below by connecting pins 12 and 13 together as the NAND output. Pin 14 and pin 11 is connected to V\ :sub:`DD` for power and pin 7 V\ :sub:`SS` to ground. Pin 9 should be tied to pin 8 to complete N side of the NAND gate. Pin 6 will be the A input and pin 10 will be the B input.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 14 2 input NAND and Inverter


   |image6|

.. container:: centeralign

   Figure 14.1 2 input NAND breadboard connections


   |image7|

.. container:: centeralign

   Figure 14.2 2 input AND breadboard connections


The Inverter is made by connecting pin 2 to V\ :sub:`DD`, pin 4 to V\ :sub:`SS`, pins 1 and 5 are connected together as the output and with pin 3 as the input. An AND gate is made by connecting the output of the NAND at pins 12 and 13 to the inverter input at pin 3.

A single 3 input NAND gate can be made by using all 6 devices as shown in figure 15.

.. _directions-2:

Directions:
-----------

Build both the 2 input and 3 input NAND gates and confirm their logic function by filling out a truth table for each. You can also measure the input threshold voltage for each input as you did for the simple inverter by connecting the unused input(s) to V\ :sub:`DD`.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 15 3 input NAND gate


   |image8|

.. container:: centeralign

   Figure 15.1 3 input NAND breadboard connections


Making a NOR / OR gate with the CD4007 transistor array
-------------------------------------------------------

As shown in figure 16, one 2 input NOR gate and one inverter can be built from one CD4007 package. Configure the NAND gate as shown below by connecting pins

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 16 2 input NOR and Inverter


   |image9|

.. container:: centeralign

   Figure 16.1 2 input NOR breadboard connections


   |image10|

.. container:: centeralign

   Figure 16.2 2 input OR breadboard connections


A single 3 input NOR gate can be made by using all 6 devices as shown in figure 17.

.. _directions-3:

Directions:
-----------

Build both the 2 input and 3 input NOR gates and confirm their logic function by filling out a truth table for each. You can also measure the input threshold voltage for each input as you did for the simple inverter by connecting the unused input(s) to ground.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 17 3 input NOR gate


   |image11|

.. container:: centeralign

   Figure 17.1 3 input NOR gate breadboard connections


By combining the two input NOR gate and the inverter along with an RC delay element a monostable multivibrator or one-shot can be constructed as shown in figure 18.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f13.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 18 NOR gate One-Shot


The width of the output pulse is determined by R\ :sub:`T` and C\ :sub:`T` according to the following formula:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_e1.png
   :align: center
   :width: 200px

Questions:
~~~~~~~~~~

| What happens if the trigger input is held high longer than τ?
| What happens if more than one trigger pulse is applied during τ?
| How would you modify the one-shot circuit in figure 18 to use a 2 input NAND gate in place of the NOR gate?

Making a SPDT Analog Switch with the CD4007 transistor array
------------------------------------------------------------

In addition to an analog SPDT switch this configuration is often called a pass gate or 2 into 1 MUX (multiplexer). The configuration is shown in figure 19.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f12.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 19 Single Pole Double Throw CMOS Switch


The on resistance, R\ :sub:`ON` of a pass gate or switch is an important specification. Please refer to the Activity on :doc:`CMOS analog switches </wiki-migration/university/courses/electronics/electronics-lab-18>` to find the procedure to measure the resistance of the NMOS, PMOS and combined CMOS switches.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/cmos_logic_func_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/cmos_logic_func_ltspice`
   


For Further reading:
--------------------

| `4000 Series Logic and Analog Circuitry <https://wiki.analog.com/_media/university/courses/4000_series_article.pdf>`__
| CMOS Logic: http:*en.wikipedia.org/wiki/CMOS
  Noise Margin: http:*\ en.wikipedia.org/wiki/Noise_margin
| Propagation Delay: http:*en.wikipedia.org/wiki/Propagation_delay
  Rise / Fall time:* http://en.wikipedia.org/wiki/Rise_time *http:*\ en.wikipedia.org/wiki/Fall_time
| Schmitt Trigger: http://en.wikipedia.org/wiki/Schmitt_trigger
| **Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f3bb.JPG
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f4a.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/a28_nf9a.PNG
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f12a.png
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f13a.JPG
   :width: 350px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f141.JPG
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f142.JPG
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f151.JPG
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f161.JPG
.. |image10| image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f162.JPG
.. |image11| image:: https://wiki.analog.com/_media/university/courses/electronics/a28_f171.JPG
