Activity: MOS Differential pair
===============================

Objective:
----------

To investigate the simple differential amplifier using enhancement mode NMOS transistors.

First a few notes on hardware limitation issues. The waveform generator in the ADALM2000 Lab system has a high output bandwidth and with that high bandwidth comes wide band noise. The input signal level needed for the measurements in this lab activity is rather small because of the gain of the differential amplifier. If the waveform generator output were used directly the signal to noise ratio of its output is not high enough. The signal to noise ratio can be improved by increasing the signal level and then placing an attenuator and filter ( figure 1 ) between the generator outputs and the circuit inputs. The materials needed for this are:

| 2 - 100Ω resistors
| 2 - 1KΩ resistors
| 2 - 0.1uF capacitors (marked 104)
| |image1|

.. container:: centeralign

   Figure 1 11:1 attenuator / filter


This attenuator and filter will be used in all parts of this lab.

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less breadboard
| Jumper wires
| 2 - 10KΩ resistors
| 1 - 15KΩ resistor (use a 10KΩ in series with a 4.7KΩ)
| 2 - Small signal NMOS transistor (CD4007 or ZVN2110A)

Directions:
-----------

The connections to the Lab hardware are as indicated in figure 2. M\ :sub:`1` and M\ :sub:`2` should be selected from the available devices with the best matching of V\ :sub:`th`. The sources of M\ :sub:`1` and M\ :sub:`2` share a common connection with one end of R\ :sub:`3`. The other end of R\ :sub:`3`\ is connected to the Vn (-5V) and supplies the tail current. The base of M\ :sub:`1` is connected to the output of the first arbitrary waveform generator and the base of M\ :sub:`2` is connected to the output of the second arbitrary waveform generator. The two collector load resistors R\ :sub:`1` and R\ :sub:`2` connect between the collectors respectively of M\ :sub:`1` and M\ :sub:`2` and the positive supply Vp ( +5V ). The differential scope input 2 +/- is used to measure the differential output as seen across the two 10KΩ load resistors.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a12m_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 NMOS Differential pair


Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/diff_pair_tail_res_mos-bb.png
   :align: right

.. container:: centeralign

   Figure 3 NMOS Differential pair Breadboard Circuit


The first waveform generator should be configured for a 200 Hz Triangle wave with 4 volt amplitude peak-to-peak and 0 offset. The second generator should be configured also for a 200 Hz Triangle wave with 4 volts amplitude peak-to-peak and 0 volts offset but with 180 degree phase. Channel one of the scope should be connected with 1+ to the output of the first generator, W1 and 1- connected to W2. Channel 2 should be connected to display 2+ and 2- and set to 1 V per division.

Procedure:
----------

The following data should be taken: The X axis is the output of the arbitrary waveform generator and the Y axis is scope channel 2 using both the 2+ and 2- inputs. By changing the value of R\ :sub:`3`, the student can explore the effects of the level of the tail current on the gain of the circuit (as seen in the slope of the line as it passed through the origin) and the linear input range and the shape of the nonlinear fall off in the gain as the circuit saturates. With minor additions to the basic circuit, such as source degeneration resistors, the student can explore techniques to extend and linearize the range of the input swing and the effects on circuit gain.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/diff_pair_tail_res_mos-wav.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 NMOS Differential pair XY plot


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a12m_f3.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 5 Gain curves


Using a current source as the tail current.
===========================================

The use of a simple resistor as the tail current has limitations. The student should explore ways to construct a current source to bias the diff pair. These could be made with a couple of additional transistors and resistors as in the stabilized current source from Activity 8M above.

Additional Materials:
---------------------

2 - small signal NMOS transistors ( M\ :sub:`3`, M\ :sub:`4` CD4007 or ZVN2110A)

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a12m_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6 Diff pair with tail current source


.. _hardware-setup-1:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/diff_pair_tail_cs_mos-bb.png
   :align: right

.. container:: centeralign

   Figure 7 Diff pair with tail current source Breadboard Circuit


.. _procedure-1:

Procedure:
----------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/diff_pair_tail_cs_mos-wav.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 8 Diff pair with tail current source XY plot


Measuring Common Mode gain
==========================

Common mode rejection is a key aspect of the differential amplifier. CMR can be measured by connecting the base of both transistors M\ :sub:`1` and M\ :sub:`2` to the same input source. The plot below shows the differential output for both the resistively biased and current source biased differential pair as the common mode voltage from W1 is swept from +4.5V to -4.5V around ground. The gain will be effected the most as the transistors go from the saturation region to the triode (resistive) region as the positive voltage on the gates approaches the drain voltage. This can be monitored by observing the drain voltage single ended with respect to ground (i.e. with the 2- input grounded). The amplitude of the generator should be adjusted until the signal seen at the output just starts to clip/fold over(as you see in your waveform plot).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a12m_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9 Measuring Common Mode gain


.. _hardware-setup-2:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/common_mode_gain_mos-bb.png
   :align: right

.. container:: centeralign

   Figure 10 Common Mode Gain Breadboard Circuit


.. _procedure-2:

Procedure:
----------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/common_mode_gain_mos-wav.png
   :align: center

.. container:: centeralign

   Figure 11 Common Mode Gain Waveform


Questions:
----------

Would you characterize this transistor amplifier as being inverting or non-inverting to outputs 2+ and 2- with the base terminal of transistor M\ :sub:`1` being considered the input? Explain your answer.

Describe what happens to each of the output voltages (2+ and 2- ) as the input voltage (W1) Increases, Decreases:

Suppose this differential-pair circuit was perfectly balanced. In this condition, how much voltage would be expected between the drain terminals of M\ :sub:`1` and M\ :sub:`2`?

What is common-mode voltage, and how should a differential amplifier (ideally) respond to it?

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/ltspice/mos_diff_pair_bb`
   -  LTspice files: :git-education_tools:`m2k/ltspice/mos_diff_pair_ltspice`
   


**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/a12_f1.png
   :width: 400px
