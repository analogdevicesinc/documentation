Activity: Magnetic Coupling – For ADALM1000
===========================================

Objective:
----------

The objective of this lab activity is to study electromagnetic induction and the coupling of a varying magnetic field between adjacent coils of wire.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

**Electromagnetic Induction**

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-mag-fig1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1, A moving Magnet induces current in a coil.


When the permanent magnet shown in figure 1 is moved towards the coil, the pointer or needle of the zero centered meter will deflect away from its centered position in one direction. When the magnet stops moving and is held stationary with respect to the coil the needle of the meter returns back to zero because there is no physical movement of the magnetic field.

Similarly, when the magnet is moved away from the coil in the opposite direction, the needle of the meter deflects in the opposite direction with respect to when the magnet was moved towards the coil indicating a change in polarity. By moving the magnet back and forth towards the coil repeatedly the needle of the meter will deflect left or right, positive or negative, relative to the motion of the magnet.

Instead of moving a magnet, a time varying current flowing through a coil of wire will produce a time varying magnetic field. If that time varying magnetic field cuts through a second coil of wire a time varying current will be induced in the second coil.

`Electromagnetic <https://en.wikipedia.org/wiki/Electromagnetic_induction>`_ or magnetic induction is the production of an electromotive force across an electrical conductor in a time varying magnetic field. Michael Faraday is generally credited with the discovery of induction in 1831, and `James Clerk Maxwell <https://en.wikipedia.org/wiki/James_Clerk_Maxwell>`_ mathematically described it as `Faraday's law of induction <https://en.wikipedia.org/wiki/Faraday%27s_law_of_induction>`_.

Materials:
----------

| ADALM1000 hardware module
| 2 12 inch / 30 cm long 3 wire female to female header jumper wires (should be included with ADALM1000)

| From ADALP2000 parts kit:
| Solderless breadboard
| Male to Male jumper wires
| Male to male header pins (gender changers)
| 2 10 Ω resistors
| 2 10 mH Inductors (103)
| 1 1 mH Inductor (102)
| 1 100 uH Inductor (101)

Construction:
-------------

Construct the circuit as shown in figure 2 on your solder-less breadboard. The two coils (inductors) can be either inserted in the breadboard as shown on the right at various distances from each other or inserted into one end of the three wire female to female header jumper wires (between the black and white wires) as shown on the left. Using the header jumper wires allows the distance and orientation between the two coils to be just about anything. Another option is to insert one coil in the breadboard (making it stationary) and using the second coil connected to a jumper wire so it can be moved around with respect to the first coil.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-mag-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Connecting the coils to the measurement system.


The two 10 Ω resistors are not strictly needed when using the 10 mH coils because of the higher internal series resistance (about 23 ohms) but when using the 1 mH and 100 uH coils the external series resistance is required because of the much smaller internal series resistance of these other coils.

Hardware Configuration:
-----------------------

The connections shown in figure 2 allow either of both coils to be driven by the AWG signal generator channels. Both AWG channels should be set to the Split I/O mode. In the first set of tests AWG A will be the driving signal and set to the SVMI mode. AWG B will be used to measure the amount of coupling seen in Coil 2 and set in the Hi-Z mode.

Set AWG A waveform shape to Sine. Set the Min value to 0.5 and the Max value to 4.5. Set the Freq to 1000 Hz. In addition to displaying the Channel A and B voltage traces you can also display the Channel A current trace to monitor the current flow in the coil.

Directions:
-----------

The object of the experiment is to observe the amount (amplitude) of signal induced or coupled from one coil to the other as the distance between and respective orientation of the coils is changed. Start out with the two coils as close to each other as possible but not touching the ferrite “bobbins” to each other.

Coils of wire wrapped around a core or “bobbin” in the form of a `solenoid <https://en.wikipedia.org/wiki/Solenoid>`_ have a “polarity” depending on the direction the wire is wrapped, clock-wise or counter clock-wise, note the small black dots near the ends of the coil symbols in figure 2. The coils from the Analog Parts kit do not have the polarity indicated on them so you will have to experiment a little to determine which lead has the polarity dot. Depending on the direction of the winding and the direction of the current in the winding the magnetic field with have the North or South pole pointing out out the top (or bottom) of the coil as inserted in the breadboard. We use the `“Right Hand Rule” <https://en.wikipedia.org/wiki/Right-hand_rule>`_ to determine this direction or polarity.

With the two coils very far apart, more then 1 inch, there will be very little coupling between the two coils as shown in figure 3.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-mag-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Driving Coil 1, with Coil 2 at a distance.


In figure 3 we see that voltage seen coupled on to coil 2, orange BIN trace, has a very small amplitude (nearly zero) compared to the applied voltage across Coil 1, green AIN trace. Also note that the current in Coil 1, cyan CA-I trace, is phase shifted about 90 degrees with respect to the voltage with the peak current appearing where the slope of the voltage waveform is highest. Record the peak-to-peak amplitude of all waveforms for future reference especially the current in Coil 1 (52 mA here).

With the coils connected with their polarity shown in figure 2 and positioned right next to each other the signal coupled from Coil 1 to Coil 2 will be as shown in figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-mag-fig4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Driving Coil 1, Coil 2 next to Coil 1.


In figure 4 we see that voltage seen coupled on to coil 2, orange BIN trace, is more or less in phase with the applied voltage across Coil 1, green AIN trace. Also note that the p-p current in Coil 1, cyan CA-I trace, is a little smaller now. As a side exercise explain why that happened? Record the peak-to-peak amplitude of all waveforms for future reference.

Change the separation and orientation of the two coils and observe any changes in the amplitude of the coupled signal. Explain any changes you see in your lab report.

Now reverse the connections, polarity of Coil 2. The phase of the coupled voltage seen across Coil 2 should now be inverted as shown in figure 5.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-mag-fig5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Driving Coil 1, Coil 2 polarity reversed.


Increasing the amount of coupling between the coils.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a small piece of magnetic material is placed such that is bridges between the ends of the two coils the magnetic field will be concentrated and coupling between the coils will be increased. A small chunk of ferrite such as shown in figure 3 works well is you have one. However, the shaft of the small screwdriver included in the Analog Parts kit is magnetic and can be used to demonstrate this effect as well. The amount the coupling increases will be smaller using the screwdriver over using a ferrite.

.. image:: https://wiki.analog.com/_media/university/tools/adalp2000/screwdriver.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 6, Screwdriver from Parts Kit.


In figure 8 we show the effect of holding the screwdriver from Parts Kit across the tops of the two coils bridging or concentrating the magnetic fields between the two coils as in figure 7. The two darker reference traces (for BIN and CA-I) are for the case with out the screwdriver bridging the coils and the lighter traces are for the new case with the screwdriver bridging the coils.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-mag-fig8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 7, Screwdriver Bridged across coils.


.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-mag-fig7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, Driving Coil 1, with Screwdriver from Parts Kit.


Turns Ratio:
~~~~~~~~~~~~

In this next part of the Activity you will replace the 10 mH Coil 2 (marked 103) with a 1 mH (marked 102) coil. The two coils look to be the same size (the ferrite bobbin at least) but with closer examination you will notice that thicker wire is used in the 1 mH coil. This means that the wire is wrapped fewer times around the bobbin and the overall length of the wire is shorter. A shorter, thicker wire will have less resistance. For comparison, figure 9 shows the coupled signals for both the original 10 mH Coil 2 (dark orange trace) and the new 1 mH Coil 2 (light orange trace). The fewer number of turns in the 1 mH coil vs the 10 mH coil results in the smaller amplitude.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-mag-fig9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 9, 10 mH Coil 1, 1 mH Coil 2.


In this next part of the Activity you will also replace the 10 mH Coil 1 (marked 103) with a 1 mH coil. The internal resistance of the 1 mH (marked 102) is much lower than the 10 mH coil.

We know that the strength of the magnetic field generated is proportional to the amount of current flowing so to remove that variable from the experiment we need to adjust the amplitude of the voltage applied to Coil 1. With the program paused (hit the Stop button), replace Coil 1 with the 1 mH coil. Lower the AWG A Max value to 2.6 and raise the Min value to 2.4, or 0.1 V either side of 2.5. Hit the Run again to start the scope sweeping. While monitoring the CA-I p-p current slowly increase the AWG Max value and lower the Min value, the same amount either side of 2.5 until the p-p current in Coil 1 is the same as it was with the 10 mH coil. (Min = 2.1, Max = 2.86)

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-mag-fig10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 10, 1 mH Coil 1, 1 mH Coil 2.


.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-mag-fig11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11, 1 mH Coil 1, 10 mH Coil 2.


Questions
---------

When you set the function generator at 4V P-P, what voltage do you observe across the inductor at 1 KHz vs at 10 KHz? At 100 Hz?

What qualitative differences do you observe between the input and output voltages at 1 KHz?

What circuit device did you construct by placing the two inductors next to each other / on top of each other?

**For Further Reading:**

:doc:`Transformers Lab </wiki-migration/university/courses/alm1k/alm-lab-transformers>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/labs/fieldsandwaves>`\ **.**
