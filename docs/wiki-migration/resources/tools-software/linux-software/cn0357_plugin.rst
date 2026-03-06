CN0357 Plugin Description
=========================

The CN0357 view is divided in three sections:

-  **ADC Settings:** Lists the available options of the :adi:`AD7790` converter.
-  **Feedback Settings:** Lists the available options of the :adi:`AD5270` rheostat or fixed resistor feedback.
-  **System:** Lists measurements and parameters of the :adi:`CN0357` system.

| 
| |image1|

ADC Settings
------------

-  **Update Rate (Hz):** Sets the output rate of the ADC.

Feedback Settings
-----------------

-  **Feedback Type:** Allows user to declare the type of the feedback resistance that is being used on the CN0357 Board. It can be either the digital rheostat or a fixed resistor.
-  **RDAC Value / Resistor (Ohm):** The raw value to be written to the RDAC register of the rheostat. / The value of the resistor used instead.
-  **Program Rheostat:** Writes the value at **RDAC Value** field to the device.

System
------

-  **Measurements**

   -  **Concentration (ppm):** Displays the current concentration measured by the system.
   -  **Conversion (mV):** Voltage measured by the ADC converter.
   -  **Supply Voltage (V):** VDD supply voltage of the ADC converter.

-  **Data**

   -  **Sensor Sensitivity (nA/ppm):** The maximum amount of current in nanoamps (nA) the sensor will use per part per million (ppm).
   -  **Feedback Resistance (Ohm):** The feedback resistance of the transimpedance amplifier on the CN0357 Board.
   -  **ppm/mV:** The system conversion coefficient of ppm/mV.
   -  **mV/ppm:** The system conversion coefficient of mV/ppm.

The measurements are being continuously displayed at regular intervals of 1 second.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/cn0357_plugin.png
   :width: 460px
