Activity: Transmission Lines as Filters – For ADALM1000
=======================================================

Objective:
----------

The objective of this activity is to examine the use of open and shorted transmission line stubs as resonators for use in notch filters. Lumped LC artificial transmission lines will be used for demonstration purposes because of ease of use over actual coaxial transmission lines.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

For background on transmission lines in general and artificial lumped LC transmission lines specifically please refer to this `earlier lab activity. <:doc:`/wiki-migration/university/courses/alm1k/alm-lc-atline`>`__

A stub or resonant stub is a length of transmission line that is connected to some part of a circuit or network at one end only. The unconnected or free end of the stub is either left open-circuit, or short-circuited. Neglecting transmission line resistive losses, the input impedance of the stub is purely reactive; either capacitive or inductive, depending on the electrical length of the stub, and on whether it is open or short circuit. Stubs may thus function as capacitors, inductors and resonant circuits. The resonant behavior of transmission line stubs is due to standing waves along their length.

Materials:
----------

| ADALM1000 hardware module
| 20 inductors with values in the range of 47 uH to 150 uH
| 21 capacitors with values in the range of 6.8 nF to 100 nF
| 2 resistors with values in the range of 27 Ω to 56 Ω

Setup Directions:
-----------------

While it is potentially possible to construct a 20 section LC transmission line model on a solder-less breadboard using thru-hole devices it is difficult and can be problematic to get the expected results. Constructing the transmission line model on a more compact PC board using surface mount components is a more reliable solution and produces better results.

The experiment PC board shown figure 1 is from the education tools on the :git-education_tools:`ADI GitHub repository <experiment-boards>` and has 20 unit LC sections. The specific board shown is populated with 100 uH surface mount inductors and 47 nF thru-hole capacitors. The PC board can be populated with either SMD or thru-hole components. The above L and C values give a characteristic line impedance of close to 50 ohms so 47 ohm source and termination resistors are used.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-tl-filter-fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Lumped LC transmission line experiment board


Male pin headers around the board provide connection points at the beginning and end of the transmission line and each tap along the line. In the upper left corner of the board, the left most three pins of header JP1 are schematically shown in figure 2 as Pin U1, U2 and U3. Similarly, in the lower left corner of the board, the left most three pins of header JP3 are schematically shown as Pin L1, L2 and L3. The lumped LC units on the board are divided into 2 10 unit long sections, T1 and T2, separated by jumper pins on the far right side of the board shown as lumper JP5 in figure 2. A shorting jumper is inserted at J5 to connect both sections together.

The AC common node of the transmission line appears on Pins U2 and L2 as well as 6 other header pins as indicated in figure 1. The +2.5 V fixed supply source will be used as the AC common for the line. The output of AWG channel A, CH A, will be used to drive the line at Pin U1 through the 47 ohm Rs, the series source resistance. The signal seen at the beginning, Tap 1, of the line will be measured by the Channel B Split input, BIN. A shorting jumper is inserted across Pins L1 and L2 to terminate the line with the 47 ohm resistor Rt. Leaving pins L1, L2 and L3 open will be the open stub condition and inserting a shorting jumper across pins L2 and L3 will be the shorted stub condition.

Open stub lengths of 20, JP5 shorted, or 10, JP5 open, are possible. Shorted stubs of any length (2, to 20) are possible by shorting the appropriate tap point to the AC common node.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-tl-filter-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Lumped LC transmission line experiment board


Directions:
-----------

A common way to measure the response of a filter is to apply an impulse function. Impulse functions contain a wide spectrum of frequencies and a Sin X/X (or Sinc) impulse function will contain equally spaced, equal amplitude frequency components starting at the fundamental frequency. The frequencies will be spaced at both even and odd harmonics of the fundamental. The ALICE desktop software has a Sin X/X (or Sinc) impulse function built into the AWG wave shapes. For this specific filter we will be measuring the response from 500 Hz to 50 KHz. If we use the settings shown in figure 3 the spectrum of the Sinc impulse will start at 500 Hz and have 100 “harmonics” up to 50 KHz.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-tl-filter-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Sinc Impulse wave shape settings.


We can view the Sinc Impulse in the time domain with the Scope screen settings shown in figure 4. Note that the sample rate is 200 KSPS and Smooth option is turned on. The green CA-V trace is the output of the AWG and the orange CB-V trace is the waveform seen at the beginning of the transmission line.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-tl-filter-fig4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Sinc impulse in the time domain


We can now open the Spectrum Analyzer tool and also view the impulse response in the frequency domain as set up in figure 5. To match the spectrum of the SinX/X impulse the start frequency is set to 500 Hz and the stop frequency is set to 50000. The horizontal frequency axis is set to Linear. The FFT zero-stuffing factor is set to 5. The number of FFT samples is set to 512. Remember that the fundamental frequency of the impulse is 500 Hz with harmonics spaced every 500 Hz. To get a “smooth” trace we need the FFT bandwidth to be wider than the frequency spacing.

The Magenta trace is the CH B dB – CH A dB gain and the cyan is the relative phase between CH A and CH B. The darker straight lines are for reference purposes and show the response of an ideal lossless terminated transmission line. The lighter traces are for the actual line when the 47 ohm Rt is connected across the end of the full 20 section long line.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-tl-filter-fig5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, ideal and terminated stub L=20


In figure 6 we keep the terminated stub case as the darker reference traces and add the open stub case as the lighter traces. Note that the amplitude or gain is a maximum at the lowest frequency and there are periodic dips or notches in the gain. Also note that the relative phase seen at the stub passes through zero at the peaks and valleys of the gain trace.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-tl-filter-fig6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, terminated and open stub L=20


In figure 7 we keep the open stub case as the darker reference traces and add the shorted stub case as the lighter traces. Note that opposite of the open stub case, for the shorted stub case the amplitude or gain is a minimum at the lowest frequency. The periodic dips or notches in the gain happen where the peaks are for the open stub case.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-tl-filter-fig7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, open and shorted stub L=20


It is interesting to go back and look at the time domain waveforms for the open and shorted cases as shown in figure 8 for the open stub case and figure 9 for the shorted stub case. We can see the positive reflected voltage impulse when it returns to the input end of the transmission line for the open case and the negative reflected voltage impulse for the shorted case.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-tl-filter-fig8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, impulse reflection open stub L=20


.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-tl-filter-fig9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 9, impulse reflection shorted stub L=20


In figure 10 we look at the open and shorted stub cases for a line length of 10. The notches will happen at higher frequencies (shorter wave length) for the shorter line length. The first notch happens at approximately twice the frequency as the 20 section long line.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-tl-filter-fig10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 10, open and shorted stub L=10


In figure 11 we show the different notch frequencies when shorting the 15th and 16th taps. Changing the length of the line tunes the frequency of the filter notches.

.. image:: https://wiki.analog.com/_media/university/courses/fieldsandwaves/alm-fandw-tl-filter-fig11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11, shorted stub L=15 and L=16


Questions:
----------

Appendix:
---------

`Build LC transmission line on a Solder-less breadboard <:doc:`/wiki-migration/university/courses/alm1k/alm-lc-atline`>`__

**For Further Reading:**

| `Transmission Line Stub <https://en.wikipedia.org/wiki/Stub_(electronics)>`__
| `Distributed-element Filter <https://en.wikipedia.org/wiki/Distributed-element_filter>`__

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/labs/fieldsandwaves>`\ **.**
