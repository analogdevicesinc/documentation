Best Engineering practices when using ADXL accelerometers
=========================================================

Introduction
------------

This document intention is to provide some tips and basic considerations when using ADI ADXL accelerometers. We thank you for choosing ADI and want to let you know that our main focus is to offer High Performance Inertial Sensors for the most demanding applications.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/adxl_broadmarket.png
   :align: center
   :width: 800px

The first and most important advise we would like to offer when using our ADXL portfolio is to **carefully read the product datasheet**, this can save you precious time.

Common terminology in ADXL's datasheet specifications
-----------------------------------------------------

Full-Scale Range (FSR)
~~~~~~~~~~~~~~~~~~~~~~

The FSR is the guaranteed dynamic range at the output of the signal chain. FSR is specified as a minimum value and is guaranteed across all conditions. Acceleration measurement may be possible beyond this minimum value. However, performance characteristics are not guaranteed.

Nonlinearity
~~~~~~~~~~~~

Device nonlinearity is the maximum deviation of any sensor data point from the least squares linear fit of the acceleration data set at an equivalent input acceleration level. The acceleration data set can encompass any range of applied acceleration, up to the complete FSR. Nonlinearity is defined mathematically as

.. image:: https://wiki.analog.com/_media/resources/technical-guides/nonlinearity.png
   :align: center
   :width: 250px

where: ACCMEAS is the measured acceleration at a defined gn. ACCFIT is the predicted acceleration at a defined gn. gn is the input acceleration level.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/nonlinearity2.png
   :align: center
   :width: 400px

Cross Axis Sensitivity
~~~~~~~~~~~~~~~~~~~~~~

Cross axis sensitivity is the measured output of the device in response to input stimuli orthogonal to the intended sense axis. It is measured as a percentage of the applied acceleration, as follows:

.. image:: https://wiki.analog.com/_media/resources/technical-guides/crossaxissen.png
   :align: center
   :width: 250px

where: ACCMEAS(gx) is the measured x-axis acceleration. gy is the applied y-axis acceleration. gz is the applied z-axis acceleration.

The cross axis sensitivity specification accounts for device level cross axis components only. These components include variations in sensor fabrication and the alignment of the sensor to the orthogonal axes of the package (also known as package alignment error). The cross axis specification does not account for system level sources of misalignment (for example, on the PCB or module).

Resonant Frequency (fo)
~~~~~~~~~~~~~~~~~~~~~~~

fo is the natural frequency at which the MEMS element has a higher gain when subjected to acceleration events. Input acceleration at this resonant frequency causes the sensor to displace by an amount equal to the applied acceleration multiplied by the quality factor (Q). Some parts use different sensor types for the horizontal (x- and y-axes) and the vertical (z-axis) sensing axes. Therefore, the resonant frequency responses of these sensors are not the same.

Quality Factor
~~~~~~~~~~~~~~

The quality factor is a scalar factor that governs the increase or decrease in amplitude of an acceleration signal applied at the resonant frequency of a MEMS element.

Sensitivity
~~~~~~~~~~~

Sensitivity is the slope of the line of best fit for the acceleration transfer function, as measured across the output FSR. The sensitivity defines the change in output (LSB) per unit change of input (g). The inverse, scale factor, is in units of g/LSB.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/sensitivity.png
   :align: center
   :width: 400px

Measurement Resolution
~~~~~~~~~~~~~~~~~~~~~~

Measurement resolution specifies the number of data bits in each acceleration data-word. For example, the 14-bit measurement of the ADXL317 has 16,384 bits of resolution. For an FSR of ±16 g (32 g total), this resolution yields a sensitivity of 500 LSB/g and a scale factor of 2.0 mg/LSB.

Zero g Bias Error
~~~~~~~~~~~~~~~~~

The zero g bias error (also called offset) is any static error term on the sensor output. Zero g bias error is measured as the deviation from 0 g with no externally applied acceleration (including gravity). To more accurately measure offset, take measurements at orientations of +1 g and –1 g and average the results. Each measurement must be taken over a sufficiently long time window to reduce the influence of external physical stimuli that may exist in the measurement system.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/offset.png
   :align: center
   :width: 400px

Initial Zero g Output Deviation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initial zero g output deviation is the error level at ambient conditions, measured immediately after completion of device manufacture. The initial zero g output deviation value denotes the standard deviation of the measured offset values across a large population of devices.

Cutoff (−3 dB) Frequency
~~~~~~~~~~~~~~~~~~~~~~~~

For applied ac acceleration, the cutoff (−3 dB) frequency is the frequency at which the input stimulus is attenuated in amplitude by 29.3% (1 − √2/2) at the output of the signal chain.

Power supply considerations
---------------------------

It is important to respect the power supply limits and considerations described in the datasheet. For example, for the ADXL34x devices, supply limits are specified from 2V to 3.6V, utilizing the sensor at lower voltages than 2V can result in improper operation, whereas applying higher voltages than 3.6V can permanently damage the device.

Recommended VS and VDDIO power sequencing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some products, e.g. ADXL313, specifies that VS and VDDIO can be applied in any sequence without damaging the part, whereas the the ADXL355 specifies that, VS cannot be powered before VDDIO.

Power supply decoupling specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generally it is recommend to use a 0.1uF ceramic capacitor and a 1-to-10uF tantalum capacitor between VS/VDDIO. Following this recommendation is very important to meet the datasheet specifications, for example in terms of noise level.

Power Cycling
~~~~~~~~~~~~~

It is common in ULP applications to power cycle the accelerometer to reduce power consumption. When using this technique, please remember that it is highly recommend to always start up the accelerometer from ground level (0 V) to ensure proper operation.

.. tip::

   As a general rule, it is *highly recommended* to always be started up the accelerometer from ground level (0 V).


If this is not possible, care must be taken regarding the following specifications:

-  *V

.. container:: lo

   RESET


*: During start-up or power cycling, the VS and VDDIO supplies must always be started up from below V_RESET voltage. Also, when the device is in operation, any time power is removed or falls below the accelerometer power supply lower range voltage (VS_MIN), VS and VDDIO supplies must be discharged below V_RESET and powered back up for proper operation. **This specification is mandatory**.
-  *Hold time*: VS and VDDIO supplies must be held below V_RESET for at least the specified hold time before re-powering the part.
-  *Rise time*: The supply voltage rise time is defined as the time from 0 V to 90% of VS.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/por_graph_generic.png
   :align: center
   :width: 400px

For example for the ADXL362 and ADXL37x devices, the power cycling requirements are:

-  *V

.. container:: lo

   RESET


*: equal or lower than 100 [mV].
-  *Hold time*: equal or grater than 200 [ms].
-  *Rise time*: should be linear and with a slope equal or higher than 6 [V/ms].

.. note::

   Fully discharging the power supply to the ground level allows a much more relaxed rise time. For the example of ADXL362 and ADXL37x devices, the rise time slope can be as low as 2.5 [V/ms], for a 200 [ms] hold time.


To enable supply discharge, it is recommended to power the device from a microcontroller general-purpose input/output (GPIO), connect a shutdown discharge switch to the supply, or use a voltage regulator with a shutdown discharge feature.
