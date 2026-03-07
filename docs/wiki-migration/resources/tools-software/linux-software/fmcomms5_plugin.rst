FMComms5 Plugin Description
===========================

The FMCOMMS5 plugin works with the `IIO Oscilloscope <https://wiki.analog.com/iio_oscilloscope>`_. You always use the latest version if possible. Changing any field will immediately write changes which have been made to the FMComms5 settings to the hardware, and then read it back to make sure the setting is valid. If you want to set something that the GUI changes to a different number, that either means that GUI is rounding (sorry), or the hardware (either the AD9361 or the FPGA fabric) does not support that mode/precision.

.. note::

   **For the main OSC plot window: The allowed channel sections are based on following rules:**

   
   -  Channels need to enabled pairwise I & Q. (example voltage0 & voltage1 or voltage2 & voltage3, etc. )
   -  The number of enabled pairwise channels need to be equal between the two devices.
   -  Devices are split as following: voltage0..3 Device A, voltage4..7 Device B
   


If you want to go play with ``/sys/bus/iio/devices/....`` and manipulate the devices behind the back of the GUI, it's still possible to see the settings by clicking the "refresh" button at the bottom of the GUI.

If you think the device has a setting that isn't managed by this tab, check out the `fmcomms5 Advanced Plugin <https://wiki.analog.com/fmcomms2_advanced_plugin>`_ for the IIO Oscilloscope.

The FMComms5 view is divided in four sections:

-  **Device Global Settings**
-  **Receive Chain**
-  **Transmit Chain**
-  **FPGA Settings**

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/fmcomms5_plugin.png
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
-  **Filter FIR configuration**

   -  **FIR parameters file chooser** Allows a FIR filter configuration to be loaded from a file. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
   -  **Enable RX FIR Filter Only:** Enables/Disables the FIR filter on RX path. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
   -  **Enable TX FIR Filter Only:** Enables/Disables the FIR filter on TX path.\ :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
   -  **Enable RX & TX FIR filters:** Enables the FIR filter on both RX and TX paths.
   -  **Disable All:** Disables the FIR filter on both RX and TX paths.

-  **RX Path Rates:** Lists the rates of: BBPLL, ADC, R2, R1, RF, RXSAMP. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **TX Path Rates:** Lists the rates of: TXSAMP, TF, T1, T2, DAC, BBPLL. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **DCXO Coarse Tune:** Selects the attribute for a coarse tune. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **DCXO Fine Tune:** Selects the attribute for a fine tune. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

Note that all settings above apply to both ad9361 devices.

Receive Chain
-------------

-  **RF Bandwidth(MHz):** Configures RX analog filters: RX TIA LPF and RX BB LPF. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **Sampling Rate(MSPS):** Selects the sample rate of the ADC. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **RF Port Select:** Selects the RF Port of the receive channels. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **RX LO Frequency(MHz):** Selects the RX local oscillator frequency. Range 70MHz to 6GHz with 1Hz tuning granularity. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **Fastlock Mode** :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

   -  **Fastlock Profile:** Selects a profile to be stored or recalled.
   -  **Store:** Stores the selected profile.
   -  **Recall:** Recalls the selected profile.

-  **Tracking** :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

   -  **Quadrature**
   -  **RF DC**
   -  **BB DC**

-  **RX**

   -  **Hardware Gain(dB):** Controls the RX gain only in Manual Gain Control Mode (MGC). :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
   -  **RSSI(dB):** Displays the received strength signal level. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
   -  **Gain Control:** Displays the active gain mode. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
   -  **Gain Control Modes:** Selects one of the available modes: manual, slow_attack, hybrid and fast_attack. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

Note that only **RF Bandwidth**, **Sampling Rate**, **RF Port Select** and **Tracking** settings apply to both ad9361 devices.

Transmit Chain
--------------

-  **RF Bandwidth(MHz):** Configures TX analog filters: TX BB LPF and TX Secondary LPF. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **Sampling Rate(MSPS):** Selects the sample rate of the DAC. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **RF Port Select:** Selects the RF Port of the transmit channels. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **TX LO Frequency(MHz):** Selects the TX local oscillator frequency. Range 70MHz to 6GHz with 1Hz tuning granularity. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
-  **Fastlock Mode** :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

   -  **Fastlock Profile:** Selects a profile to be stored or recalled.
   -  **Store:** Stores the selected profile.
   -  **Recall:** Recalls the selected profile.

-  **TX**

   -  **Attenuation(dB):** Individually controlls attenuation for TX1 and TX2. The range is from 0 to -89.75 dB in 0.25dB steps. :doc:`Read More </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

Note that only **RF Bandwidth**, **Sampling Rate** and **RF Port Select** settings apply to both ad9361 devices.

FPGA Settings
-------------

-  **Transmit/DDS**

   -  **DDS Mode:** Selects on the the available modes:

      -  One CW Tone
      -  Two CW Tones
      -  Independent I/Q Control
      -  DAC Buffer Output (Output a data file)
      -  Disabled.

   -  **Tone**

      -  **Frequency(MHz):** Selects the frequency of the tone.
      -  **Scale:** Selects the scale of the tone.
      -  **Phase(degrees):** Selects the phase of the tone.

-  **Receive**

   -  **Phase Rotation :** Selects the rotation phase of a RX
