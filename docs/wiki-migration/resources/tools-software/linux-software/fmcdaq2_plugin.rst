DAQ2/3 Plugin Description
=========================

The DAQ2/3 plugin works with the `IIO Oscilloscope <https://wiki.analog.com/iio_oscilloscope>`__. You always use the latest version if possible. Changing any field will immediately write changes which have been made to the DAQ2/3 settings to the hardware, and then read it back to make sure the setting is valid. If you want to set something that the GUI changes to a different number, that either means that GUI is rounding (sorry), or the hardware (either the AD9144 (DAQ2), AD9152(DAQ3), AD9680 (DAQ2/3) or the FPGA fabric) does not support that mode/precision.

The DAQ2/3 view is divided in three sections:

-  **ADC**
-  **DDS**
-  **DAC**

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/daq2_3_plugin.png
   :align: right
   :width: 400px

ADC
===

-  **Sampling frequency(MHz):** Displays the sample rate of the ADC.
-  **Test options:** Sets the ADC channels in different testing modes.

DDS
===

-  **DDS Mode:** Selects one of the available modes:

   -  One CW Tone
   -  Two CW Tones
   -  Independent I/Q Control
   -  DAC Buffer Output

      -  Any data using the buffer must be of even length with the standard DMA drivers and HDL.

   -  Disabled

-  **Tone**

   -  **Frequency(Mhz):** Selects the frequency of the tone. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
   -  **Scale:** Selects the scale of the tone. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
   -  **Phase(degrees):** Selects the phase of the tone. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

DAC
===

-  **Data:** Displays the DAC data clock (MHz).
