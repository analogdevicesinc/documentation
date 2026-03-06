ADE9153A Total Harmonic Distortion Measurement
==============================================

GENERAL DESCRIPTION
-------------------

The ADE9153A is a highly accurate, single-phase, energy metering IC with autocalibration. However, ADE9153A does not have Total Harmonic Distortion (THD) feature. But, it is possible to calculate and measure THD for currents and voltages through certain parameters on the part and process raw data to microcontroller.

The EV-ADE9153ASHIELDZ accommodates microcontroller such as Arduino microcontroller. The data sheet for this device should be consulted in conjunction with this evaluation board user guide.

EV-ADE9153ASHIELZ Evaluation Board
----------------------------------

|image1|

.. container:: centeralign

   \ *Figure 1. EV-ADE9153ASHIELDZ*\


UNDER CONSTRUCTION
==================

Set-Up
------

There is two-ways for user to either use Fast Fourier Transform (FFT) or Goertzel Algorithm for the implementation of THD to ADE9153A. On this Wiki, the implementation that will be done to measure THD value for ADE9153A is through Goertzel Algorithm. The process and the output will be done on the microcontroller side. Goertzel Algorithm program will be provided for user testing.

The following must be done or determined to run the User program properly onto the EV-ADE9153ASHIELDZ:

| • Interface the ADE9153A on a Microcontroller (Arduino)
| • Determine the required Sampling frequency, Number of samples & Data
| • Configure/Read the registers needed to acquire data to act as an input on the Microcontroller.
| • Process the data from the Goertzel Algorithm done on the microcontroller.

.. _under-construction-1:

UNDER CONSTRUCTION
~~~~~~~~~~~~~~~~~~

LINK TO DOCUMENTS
-----------------

| 1. :adi:`ADE9153A Datasheet <media/en/technical-documentation/data-sheets/ade9153a.pdf>`
| 2. :adi:`ADE9153A UG-1253 <media/en/technical-documentation/user-guides/ev-ade9153ashieldz-ug-1253.pdf>`
| 3. :adi:`ADE9153A UG-1247 <media/en/technical-documentation/user-guides/ade9153a-technical-reference-manual-ug-1247.pdf>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-ade9153ashieldztop-web.png
   :width: 400px
