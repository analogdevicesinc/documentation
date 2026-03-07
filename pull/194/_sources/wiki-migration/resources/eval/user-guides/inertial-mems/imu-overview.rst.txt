ADI MEMS IMUs Glossary: Performance Characteristics, Measurement Setups and Applications
========================================================================================

This page is intended to introduce and discuss common characteristics of MEMS IMUs, how to measure those performance metrics and finally some applications where those metrics matter.

Bias Repeatability
==================

Measured in °/hour.

Bias Error
==========

Offset error in MEMs output on a particular axis. Fixed error typically. Measured in °/hour.

Sensitivity Error
=================

An error in the gain of the response. Non-uniformity that affects measurement output.

Allan Variance (AVAR)
=====================

A plot of noise versus averaging time.

In-run Bias Stability (IRBS)
============================

This can be thought of as the sensor resolution in an "ideal case." It is also found as the minimum of the AVAR plot.

Angle Random Walk (ARW)
=======================

Measured in °/hour/√Hz or °/√hour.

Applies to gyroscopes. It is the "close-in" (small τ) on the AVAR curve and is noise that comes from the quantization process. Taken at Τ = 1 second. In order to calculate the ARW, take the value of the square-root of the AllanVariance and divide by 60 [iMAR].

For an example consider the ADIS16153, with datasheet here: :adi:`ADIS16135.pdf#Page=08 <media/en/technical-documentation/data-sheets/ADIS16135.pdf#Page=08>`. The graph of the AllanVariance is this:


|image1|

Additional notes: `iMAR Research Background <http://home.engineering.iastate.edu/~shermanp/AERE432/lectures/Rate%20Gyros/Rate%20Gyro%20Explanations.pdf>`_

Rate Random Walk (ARRW)
=======================

Applies to gyroscopes and is the "far out" (large Τ) on the Allan Variance (AVAR) curve. This quantity represents long-term stability of the sensor measurement.

Velocity Random Walk (VRW)
==========================

Similar to the angular random walk (ARW) for gyroscopes. Noise from quantization of the axes.

Noise Density
=============

Similar to amplifier noise density. RMS noise per unit of BW. Can be approximated with the formula: ND ≅ ARW/60\* √2

Vibration Rectification Error (VRE)
===================================

Measured in degrees/sec/g².

Cross-Axis Sensitivity
======================

Unintended effect where rotation/acceleration from one axis is detected on another axis. Can be calculated from axis to axis misalignment error for accels/gyros: sin(axis to axis misalignment) in %

Example: For the ADIS16448, the accel axis to axis misalignment is 0.2 degrees. Therefore Cross-axis sensitivity accel is sin(0.2) = 0.197%. Gyro is sin(0.05) = 0.09%. Magnetometer: sin(0.25) = 0.247%

Linear Acceleration Effect (Linear-g), Linear Acceleration Effect on Bias, Linear-g Rejection (Linear-g Sensitivity)
====================================================================================================================

Unintended effect where linear acceleration is detected as rotation. Measured in degrees/sec/g.

Vibration Rejection (Gyros)
===========================

A combination of Linear-g and Vibration Rectification (VRE) specs.

Vibration response of a gyro = Linear-g X-Axis Acceleration + (VRE X-Axis Acceleration)^2

Additional Resources!
=====================

\* Information on Allan Variance for Gyros: http://www.alexandertrusov.com/uploads/pdf/2011-UCI-trusov-whitepaper-noise.pdf

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/2021-07-22_09_29_19-adis16135_rev._f_.png
