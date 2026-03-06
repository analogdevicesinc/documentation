Activity: NMOS Differential pair
================================

Objective:
----------

To investigate the simple differential amplifier using enhancement mode NMOS transistors.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

In this Lab you will be using both of the channels of the ALM1000 in the split Input / Output mode. CB-Out is used to denote the connection to the Output pin and CB-In is used to denote the Input pin on the (expanded) 8 pin connector.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

First a few notes on hardware limitation issues. While the waveform generator in the ALM1000 system uses a 16 bit wide dynamic range DAC there is still significant wide band noise which can reduce the signal to noise ration when generating very small amplitude signals. The input signal level needed for the measurements in this lab activity is rather small because of the gain of the differential amplifier. If the waveform generator output were used directly the signal to noise ratio of its output is not high enough. The signal to noise ratio can be improved in this case by increasing the signal level and then placing an attenuator and filter ( single ended example shown in figure 1 ) between the generator outputs and the circuit inputs. The materials needed for this are:

| 1 - 47Ω resistors
| 1 - 1KΩ resistors
| 1 - 0.1uF capacitors (marked 104)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-12_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 20:1 attenuator / filter example


An attenuator and filter like this will be used in all parts of this lab.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wire kit
| 2 - 10KΩ resistors
| 1 - 47Ω resistor
| 2 - 1KΩ resistor
| 1 - 2.2KΩ resistor
| 1 - 0.1uF capacitors (marked 104)
| 2 - Small signal NMOS transistor (CD4007 or ZVN2110A)

Directions:
~~~~~~~~~~~

Build the NMOS differential pair test circuit shown in figure 2. The connections to the ALM1000 are as indicated in the green boxes. M\ :sub:`1` and M\ :sub:`2` should be selected from your available transistors with the best matching of V\ :sub:`TH`. The sources of M\ :sub:`1` and M\ :sub:`2` share a common connection with one end of R\ :sub:`3`. The other end of R\ :sub:`3`\ is connected to ground (0V) and supplies the tail current. The gate of M\ :sub:`1` is connected to the output of the first arbitrary waveform generator, CH A, and the gate of M\ :sub:`2` is connected to the output of the second arbitrary waveform generator, CH B, through the 20:1 attenuator network. The two drain load resistors R\ :sub:`1` and R\ :sub:`2` connect between the drains respectively of M\ :sub:`1` and M\ :sub:`2` and the positive supply +5V. The two Split I/O inputs AIN and BIN are used to measure the differential output as seen across the two 10K load resistors.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-12m_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 NMOS Differential pair with tail resistor


Hardware Setup:
~~~~~~~~~~~~~~~

Both channels A and B should be set to the SVMI Split I/O mode. Both generators should be configured for a 500 Hz sine wave, with Channel A phase set to 90 degrees and Channel B set to 270 degrees ( 180 degrees difference ). The resistor dividers will reduce the signal amplitude seen at the gate of M\ :sub:`1`\ with respect to the gate of M\ :sub:`2`\ to slightly less than 200 mV. Channel CA-In and CB-In (Hi-Z inputs) should be connected to display the voltage at the drains of M\ :sub:`1` and M\ :sub:`2`. To also display the AWG channel A and B output waveforms we can use the X Math and Y Math traces. From the Curves drop down menu select CA-V, CB-V, X Math and Y Math traces. Open the Math controls screen and enter AWGAwaveform[t] in the X Math Formula entry and AWGBwaveform[t] in the Y Math Formula entry. The Units can be V and the X Axis can be V-A, the Y Axis can be V-B.

Procedure:
~~~~~~~~~~

Set to display all four traces. Turn on the display of the average voltage for the CA-V and CB-V traces. Set the channel A input offset equal to the average value. The displayed average should now be nearly zero. Do the same with channel B. Set the channel A and B position to 0 ( the CA-V and CB-V traces should now be centered on the grid. Turn on the CA-V - CB-V math trace, this will now display the differential output voltage.

By changing the value of R\ :sub:`3`, you should explore the effects of the level of the tail current on the gain of the circuit and the linear input range and the shape of the nonlinear fall off in the gain as the circuit saturates. With minor additions to the basic circuit, such as emitter degeneration resistors, you should also explore techniques to extend and linearize the range of the input swing and the effects on circuit gain.

Using a current source as the tail current.
-------------------------------------------

The use of a simple resistor as the tail current has limitations. You should explore ways to construct a current source to bias the diff pair. These could be made with a couple of additional transistors and resistors as in the stabilized current source from :doc:`Activity 8M </wiki-migration/university/courses/alm1k/alm-lab-8m>`.

Additional Materials:
~~~~~~~~~~~~~~~~~~~~~

2 - small signal NMOS transistors ( CD4007 or ZVN2110A)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-12m_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3 Diff pair with tail current source


Measuring Common Mode gain
--------------------------

Common mode rejection is a key aspect of the differential amplifier. CMR can be measured by connecting the gate of both transistors M\ :sub:`1` and M\ :sub:`2` to the same input source. You should generate plots showing the differential output for both the resistively biased and current source biased differential pair as the common mode voltage is swept + and - 500mV around 2.5V.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-12m_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4 Common Mode Gain configuration


Questions:
~~~~~~~~~~

Would you characterize this transistor amplifier as being inverting or non-inverting to outputs at each of the drain terminals with the gate terminal of transistor M\ :sub:`1` being considered the plus (non-inverting) input? Explain your answer.

Describe what happens to each of the output voltages (CA-In and CB-In ) as the input voltage (CA-Out) increases, Decreases:

Suppose this differential-pair circuit was perfectly balanced. In this condition, how much voltage would be expected between the drain terminals of M\ :sub:`1` and M\ :sub:`2`?

What is common-mode voltage, and how should a differential amplifier (ideally) respond to it?

Repeat the common mode gain measurements on the circuit shown in figure 3 with the tail current source. How has the result changed and why.

**For Further Reading:**

`Differential amplifier <https://en.wikipedia.org/wiki/Differential_amplifier>`__

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`
