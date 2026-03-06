FMComms1 Plugin Description
===========================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



| The FMComms1 view is divided in two sections:
| **FMComms1 Receive Chain** and **FMComms1 Transmit Chain**. |image1|

-  **ADC settings**

   -  **Sampling frequency(MHz):** Sets the sampling frequency of the ADC.

-  **Gain amplifier settings**

   -  **Lock Channels:** Forces both gains to the same value.
   -  **Gain(dB):** Allows to interdependently set gain on the I and Q channels. The gain can be configured from 4.5 dB to 20.5 dB. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`

-  **LO settings:** Configures the RX PLL

   -  **Enable:** Enables/disables the local oscillator. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4350>`
   -  **Frequency(MHz):** Sets the receive base frequency. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4350>`
   -  **Spacing(Hz):** Selects the frequency spacing. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4350>`

-  **FMComms1 Transmit Chain**

   -  **DDS:** Selects on the the available modes: One CW Tone, Two CW Tones, Independent I/Q Control, DAC Buffer Output and Disabled.

      -  **Tone**

         -  **Frequency(Mhz):** Selects the frequency of the tone. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
         -  **Scale:** Selects the scale of the tone. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
         -  **Phase(degrees):** Selects the phase of the tone. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

   -  **DAC Frequency**

      -  **Data:** Selects the DAC data clock (MHz). :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
      -  **Interpolation (Hz):** Selects one of the available interpolation DAC frequencies. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
      -  **Center Shift (Hz):** Selects one of the available center shift frequencies. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

   -  **LO**

      -  **Enable:** Enables/disables the local oscillator. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4350>`
      -  **Frequency(MHz):** Selects the output frequency of the TX local oscillator. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4350>`
      -  **Spacing(Hz):** Selects the frequency spacing. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4350>`

Clicking the "Save Settings" button will write changes which have been made to the FMComms1 settings to the hardware.

.. hint::

   Upon saving values will be rounded to the nearest value supported by the hardware. After the "Save Settings" button has been clicked these values will be displayed.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/fmcomms1_plugin.png
   :width: 400px
