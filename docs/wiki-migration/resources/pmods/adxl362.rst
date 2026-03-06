The :adi:`ADXL362` is an ultralow power, 3-axis MEMS accelerometer that consumes less than 2 μA at a 100 Hz output data rate and 270 nA when in motion triggered wake-up mode. Unlike accelerometers that use power duty cycling to achieve low power consumption, the :adi:`ADXL362` does not alias input signals by undersampling; it samples the full bandwidth of the sensor at all data rates.

The :adi:`ADXL362` always provides 12-bit output resolution; 8-bit formatted data is also provided for more efficient single-byte transfers when a lower resolution is sufficient. Measurement ranges of ±2 g, ±4 g, and ±8 g are available, with a resolution of 1 mg/LSB on the ±2 g range. For applications where a noise level lower than the normal 550 μg/√Hz of the :adi:`ADXL362` is desired, either of two lower noise modes (down to 175 μg/√Hz typical) can be selected at minimal increase in supply current.

In addition to its ultralow power consumption, the :adi:`ADXL362` has many features to enable true system level power reduction. It includes a deep multimode output FIFO, a built-in micropower temperature sensor, and several activity detection modes including adjustable threshold sleep and wake-up operation that can run as low as 270 nA at a 6 Hz (approximate) measurement rate. A pin output is provided to directly control an external switch when activity is detected, if desired. In addition, the :adi:`ADXL362` has provisions for external control of sampling time and/or an external clock.

The :adi:`ADXL362` operates on a wide 1.6 V to 3.5 V supply range, and can interface, if necessary, to a host operating on a separate, lower supply voltage. :adi:`ADXL362` is available in a 3 mm × 3.25 mm × 1.06 mm package.

Applications
============

-  Hearing aids
-  Home healthcare devices
-  Motion enabled power save switches
-  Wireless sensors
-  Motion enabled metering devices

.. image:: https://wiki.analog.com/_media/resources/pmods/adxl362_pmod_acl2.jpg
   :align: center
