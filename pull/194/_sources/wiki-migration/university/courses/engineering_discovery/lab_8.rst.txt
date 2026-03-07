Introduction to Diodes and LEDs
===============================

.. image:: https://wiki.analog.com/_media/analogTV>5094391273001
   :alt: analogTV>5094391273001
   :align: right

Introduction
------------

Diodes are two-terminal circuit elements that allow current to pass in one direction only. Early diodes were based on *thermionic emission*, which occurs in traditional incandescent light bulbs. Thermionic emission produces a cloud of free electrons that surrounds a heated metallic filament (typically placed in a vacuum), and when a positively metal plate is placed nearby in the vacuum, the electrons flow toward the plate due to the attractive force that exists between unlike charges. This electron flow constitutes an electrical current that flows from the filament to the plate, which only flows when the plate is positively charged with respect to the filament. Modern semiconductor diodes are comprised of two types of semiconductor materials, positively doped "P" type and negatively doped "N" type, separated by a sharp junction between them. This arrangement of the materials is called a *pn junction*, and allows current to flow in one direction when the voltage across the diode (the *bias voltage*) exceeds a certain value in one direction -- about 0.7 V in silicon diodes -- and substantially blocks current from flowing when the bias voltage is reversed.

Photons are released when currents flow through pn junctions. The color of the emitted light depends on the materials that comprise the pn junction. Light-emitting-diodes (LEDs) are diodes that are designed for the specific purpose of emitting light of a particular color. Many different colored LEDs are available today, and white high power LEDs are beginning to replace standard incandescent lights in a number of everyday applications. When the diode conducts current it is said to be *forward biased* and when it blocks current it is said to be *reverse biased*. Clearly, a LED must be forward biased in order for it to emit light.

The current flowing through a diode is an exponential function of the voltage across it. We can observe the basic shape of the diode current as a function of its voltage using the M1K and PixelPulse software.

Objective
---------

To study the basics of signal diodes and light-emitting diodes. To observe the current versus voltage characterists of a signal diode and a light-emitting diode. Following completion of this lab you should be able to explain the basic operation of a diode, what signal diodes and light-emitting diodes are used for, and describe the nonlinear shape of the current versus voltage diode characteristic.

Materials and Apparatus
-----------------------

-  Computer running PixelPulse software
-  Analog Devices ADALM1000 (M1K)
-  Solderless breadboard and jumper wires from the ADALP2000 Analog Parts Kit
-  (1) Yellow LED from the ADALP2000 Analog Parts Kit
-  (1) Green LED from the ADALP2000 Analog Parts Kit
-  (1) Red LED from the ADALP2000 Analog Parts Kit
-  (1) 1N914 signal diode from the ADALP2000 Analog Parts Kit
-  (1) 100 Ω resistor from the ADALP2000 Analog Parts Kit

Procedure
---------

-  Run PixelPulse and plug in the M1K using the supplied USB cable
-  Update M1K firmware, if necessary
-  Set up the M1K to source voltage/measure current on Channel A
-  Disable "Repeated Mode" Operation and change the "Sample Time" to 1 second
-  Set up Channel A source waveform for a 10 Hz “Triangle” output that swings between 0 V and of 2.0 V
-  Enable X-Y plots
-  Construct the following circuit on the solderless breadboard\

|lab_8_image_1.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard\

|lab_8_assembly_image_1.png|

-  Scale the Y-axis of the X-Y plot using the mouse and right mouse button such that the measured current ranges between 0.00 A and 0.09 A (90 mA)
-  Observe the LED flashing, the shape of the measured current waveform, and the shape of the X-Y plot, which is a plot of the diode current vs. diode voltage
-  Increase the peak level of the applied triangular voltage waveform to 2.2 V in 0.1 V increments and observe the change in the measured current waveform and X-Y plot as each step is made
-  Describe what is happening in the measured current and X-Y plot
-  Change the Y-axis scale to range between 0.00 A and 0.20 A (200 mA)
-  Increase the peak level of the applied triangular voltage waveform from 2.2 V to 2.4 V in 0.1 V increments and observe the change in the measured current waveform and X-Y plot as each step is made
-  Describe what is happening in the measured current and X-Y plot; why does the current flatten out at approximately 200 mA?
-  Observe that there is a difference in the voltage vs. current trajectory in the X-Y plot between increasing current and decreasing current when the triangle wave peak level is at 2.4 V (it may be helpful to expand the X-axis scale to better observe this); this difference is called "hysteresis"
-  Explain why the hysteresis occurs
-  Repeat the above procedure for the green and red LEDs
-  Observe and describe any differences seen in the behavior of the three different LEDs
-  Change the amplitude of the triangular voltage waveform to 0.6 V and adjust the X-Y vertical axis scale to range from 0.00 V to 0.09 V
-  Replace the LED with a 1N914 signal diode as shown in the following schematic\

|lab_8_image_2.png|

-  Increase the peak level of the applied triangular voltage waveform to 0.9 V in 0.1 V increments and observe the change in the measured current waveform and X-Y plot as each step is made
-  Observe the exponential shape of the diode current versus voltage characteristic and that the knee of the curve -- commonly referred to as the "cut in" voltage -- is nominally between 0.70 V and 0.75 V
-  Set up Channel A to source 5 V DC and Channel B to measure voltage
-  Construct the following circuit on the solderless breadboard\

|lab_8_image_3.png|

-  Refer to the illustration below for one way to install the components in the solderless breadboard\

|lab_8_assembly_image_2.png|

-  Record the DC voltage on Channel A
-  Repeat the above for the green and red LEDs

Theory
------

An ideal diode would act as a short circuit to currents flowing in one direction and an open circuit to currents flowing in the other direction. When a diode is conducting current it is said to be *forward biased*, and when behaving as an open circuit it is said to be *reverse biased*. When forward biased, practical diodes have a current versus voltage (I/V) characteristic that is exponential, and beyond the knee of the exponential the slope becomes very steep. Diodes are often forward biased to operate on the steep vertical parts of their I/V characteristics where they exhibit small incremental resistances; incremental resistance is defined as the reciprocal of the slope of the I/V characteristic in the immediate vicinity of the bias point. When the diode is reverse biased, a very small *leakage current* flows.

In the lab we operate three different color LEDs and one 1N914 signal diode in the forward bias mode and examine the exponential current versus voltage characteristics of each. They all exhibit exponential behavior, with some differences in where the knee occurs and how steep the curve becomes beyond the knee. The forward bias voltage at the exponential knee is often referred to as the *cut-in* voltage because the diode is just beginning to conduct current and is "cutting in" from an effective open circuit to a low resistance. Because the slope of the I/V characteristic is so steep beyond the knee, the change in voltage is very small with respect to change in current. Because of this, the diode voltage is often approximated to be a constant over a wide range of currents, which makes designing with diodes simple for many circuits. The cut-in voltage and diode characteristic are generally not tightly controlled, so designing with diodes often involves approximations.

As an example of designing with a LED, we can observe the I/V characteristic and find the region of current in which we wish to operate. The change in diode voltage over this region is small with respect to the change in current so one thing we can do is to take the diode voltage at the midpoint of our current range and use it as a constant. For instance, as in the lab, we desire 30 mA through a LED that is powered from 5 VDC. We see that the diode voltage is nominally 2 V in this region of the I/V characteristic so we use that as an approximation of the diode voltage (even if the current changes). We can easily calculate a resistor to set the approximate diode current using Ohm's law as R = V/I = (5 V - 2 V)/30 mA = 100 Ω. The same considerations apply to signal diodes. Typical values often used for a signal diode voltage when it is forward biased up in the steep part of its I/V characteristic range from 0.7 V to 0.8 V. This small voltage range corresponds to a wide current range. Using this approach we can develop a primitive circuit model for the diode consisting of its small incremental resistance in series with a DC voltage equal to the forward bias voltage.

The exponential I/V characteristic has a dependence on a quantity that is called the *thermal voltage*, which depends on the diode pn junction temperature. As current passes through the diode, its junction temperature increases due to Joule heating, and thereby changes the thermal voltage. When this happens in any device it is called *self heating*. We can see the effects of self heating in the diodes manifested as hysteresis in the I/V characteristic when the currents get large.

Observations and Conclusions
----------------------------

-  Ideal diodes conduct current flowing in one direction and act as open circuits to current flowing in the opposite direction
-  A diode that is biased such that it is conducting current is said to be forward biased and is said to be reverse biased when biased such that it is not conducting current
-  Modern practical diodes are constructed from pn junctions, and exhibit an exponential I/V characteristic when forward biased
-  Diode pn junctions emit photons when current passes through them and are widely used to produce LEDs of various colors
-  Diodes have different I/V characteristics that depend on the materials from which they are constructed
-   Because the diode voltage changes very little for large current changes, the diode voltage can be approximated as constant for a wide range of currents, simplifying design
-  Diode I/V characteristics are affected by self heating

**Return to** :doc:`Engineering Discovery Index </wiki-migration/university/courses/engineering_discovery>`

.. |lab_8_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_8_image_1.png
   :width: 400px
.. |lab_8_assembly_image_1.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_8_assembly_image_1.png
   :width: 1000px
.. |lab_8_image_2.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_8_image_2.png
   :width: 350px
.. |lab_8_image_3.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_8_image_3.png
   :width: 600px
.. |lab_8_assembly_image_2.png| image:: https://wiki.analog.com/_media/university/courses/engineering_discovery/lab_8_assembly_image_2.png
   :width: 1000px
