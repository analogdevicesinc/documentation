AD936X Plugin Description
=========================

The AD936X plugin (formerly known as the FMComms2/3/4 Plugin) works with the `IIO Oscilloscope <https://wiki.analog.com/iio_oscilloscope>`_. You always use the latest version if possible. Changing any field will immediately write changes which have been made to the AD936X settings to the hardware, and then read it back to make sure the setting is valid. If you want to set something that the GUI changes to a different number, that either means that GUI is rounding (sorry), or the hardware (either the AD9361 or the FPGA fabric) does not support that mode/precision.

If you want to go play with ``/sys/bus/iio/devices/....`` and manipulate the devices behind the back of the GUI, it's still possible to see the settings by clicking the "refresh" button at the bottom of the GUI.

If you think the device has a setting that isn't managed by this tab, check out the `AD936X Advanced Plugin <https://wiki.analog.com/fmcomms2_advanced_plugin>`_ for the IIO Oscilloscope.

The AD936X view is divided in four sections:

-  **Device Global Settings**
-  **Receive Chain**
-  **Transmit Chain**
-  **FPGA Settings**

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/fmcomms2_plugin.png
   :align: right
   :width: 380px

Device Global Settings
----------------------

-  **Active ENSM:** Displays the active mode of the Enable State Machine. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **ENSM Modes:** Selects one of the available modes: FDD and TDD. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **Calibration Mode:** Displays the active calibration mode. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **Calibration Modes:** Selects one of the available modes: auto, manual, rf_dc_offs and tx_quad. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **TRX Rate Governor:** Displays the active option of the Rate Governors. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **TRX Rate Governor Available:** Selects one of the available options: nominal and highest_osr. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **Filter FIR configuration:** Allows a FIR filter configuration to be loaded from a file. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **RX Path Rates:** Lists the rates of: BBPLL, ADC, R2, R1, RF, RXSAMP. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **TX Path Rates:** Lists the rates of: TXSAMP, TF, T1, T2, DAC, BBPLL. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **DCXO Coarse Tune:** Selects the attribute for a coarse tune. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **DCXO Fine Tune:** Selects the attribute for a fine tune. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

Receive Chain
-------------

-  **RF Bandwidth(MHz):** Configures RX analog filters: RX TIA LPF and RX BB LPF. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **Sampling Rate(MSPS):** Selects the sample rate of the ADC. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **RX LO Frequency(MHz):** Selects the RX local oscillator frequency. Range 70MHz to 6GHz with 1Hz tuning granularity. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **External RX LO:** Allows switching between external and internal LO on the fly. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **RF Port Select:** Selects the RF port to be used. Can be either any of the inputs on the Rx input mux (in single ended or differential) or the Tx monitor input. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **Fastlock Profile:** Selects one of the 8 available profiles of frequency configuration information. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **Store:** Stores the current frequency configuration into the profile pointed by **Fastlock Profile**.
-  **Recall:** Recalls the profile pointed by **Fastlock Profile**.
-  **Tracking** :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

   -  **Quadrature**
   -  **RF DC**
   -  **BB DC**

-  **RX**

   -  **Hardware Gain(dB):** Controls the RX gain only in Manual Gain Control Mode (MGC). :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
   -  **RSSI(dB):** Displays the received strength signal level. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
   -  **Gain Control:** Displays the active gain mode. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
   -  **Gain Control Modes:** Selects one of the available modes: manual, slow_attack, hybrid and fast_attack. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

Transmit Chain
--------------

-  **RF Bandwidth(MHz):** Configures TX analog filters: TX BB LPF and TX Secondary LPF. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **Sampling Rate(MSPS):** Selects the sample rate of the DAC. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **TX LO Frequency(MHz):** Selects the TX local oscillator frequency. Range 70MHz to 6GHz with 1Hz tuning granularity. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **External TX LO:** Allows switching between external and internal LO on the fly. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **RF Port Select:** Selects the RF port to be used. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **Fastlock Profile:** Selects one of the 8 available profiles of frequency configuration information. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **Store:** Stores the current frequency configuration into the profile pointed by **Fastlock Profile**.
-  **Recall:** Recalls the profile pointed by **Fastlock Profile**.
-  **TX**

   -  **Attenuation(dB):** Individually controlls attenuation for TX1 and TX2. The range is from 0 to -89.75 dB in 0.25dB steps. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

      -  **RSSI(dB):** TX Received Strength Signal Indicator. Active when TX_MONITOR port is selected in the RX **RF Port Select**. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

FPGA Settings
-------------

Transmit/DDS
~~~~~~~~~~~~

The plugin provides several options on how the transmitted data is generated.I

It is possible to either use the built-in two tone **Direct Digital Synthesizer (DDS)** to transmit a bi-tonal signal on channels I and Q of the DAC. Or it is possible to use the **Direct Memory Access (DMA) facility** to transmit custom data that you have stored in a file.

This can be achieved by selecting one of the following options listed by the **DDS Mode**:

One CW Tone
~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/one_cw_tone.png
   :align: right

In **One CW Tone** mode one continuous wave (CW) tone will be outputted. The plugin displays the controls to set the Frequency, Amplitude and Phase for just one tone and makes sure that the amplitude of the other tone is set to 0. The resulting signal will be outputted on the Channel I of the DAC and the exact same signal but with a difference in phase of 90 degrees will be outputted on the Channel Q of the DAC.


Two CW Tone
~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/two_cw_tones.png
   :align: right

In **Two CW Tone** mode two continuous wave (CW) tones will be outputted. The plugin displays the controls to set the frequencies F1 and F2, amplitudes A1 and A2, phases P1 and P2 for the two tones. The resulting signal will be outputted on the Channel I of the DAC and the exact same signal but with a difference in phase of 90 degrees will be outputted on the Channel Q of the DAC.


Independent I/Q Control
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iq_independent.png
   :align: right

In **Independent I/Q Control** the plugin displays the controls to set the frequencies, amplitudes and phases for the two tones that will be outputted on channel I and additionally it allows for the two tones that will be outputted on channel Q of the DAC to be configured independently.

|

.. note::

   Note: The bi-tonal signal (T) is defined as the sum of two tones:

   | T(t) = A1 \* sin(2 \* π \* F1 \* t + P1) + A2 \* sin(2 \* π \* F2 \* t + P2),
   | where A-amplitude, F-frequency, P-phase of a tone.



DAC Buffer Output
~~~~~~~~~~~~~~~~~

|image1| The file selector under the **File Selection** section is used to locate and choose the desired data file. Under the **DAC Channels** section the enabled channels will be used to transmit the data stored in the file. To finalize the process, a click on the **Load** button is required.

| **Restrictions:**
| \* There are two types of files than can be loaded: **.txt** or **.mat**. The IIO-Oscilloscope comes with several :git-iio-oscilloscope:`data files <waveforms>` that can be used. If you want to create your own data files please take a look at the :doc:`Basic IQ Data Files </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>` documentation first.
| \* Due to hardware limitation only specific combinations of enabled channels are possible. You can enable a total of 1, 2, 4, etc. channels. If 1 channel is enabled then it can be any of them. If two channels are enabled then channels 0, 1 or channels 2, 3 can be enabled and so on.


Disable
~~~~~~~

| In this mode both DDS and DMA are disabled causing the DAC channels to stop transmitting any data.
|

.. note::

   Upon pressing **Reload Settings** button the values will be reloaded with the corresponding driver values. Useful in scenarios where the diver values get changed outside this plugin (e.g with the use of Debug plugin) and a refresh on plugin's values is needed.


.. hint::

   Some plugin values will be rounded to the nearest value supported by the hardware.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/dac_output_buffer_panel.png
