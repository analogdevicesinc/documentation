FMCOMMS11 Plugin Description
============================

The FMCOMMS11 plugin works with the `IIO Oscilloscope <https://wiki.analog.com/iio_oscilloscope>`_. You always use the latest version if possible. Changing any field will immediately write changes which have been made to the AD936X settings to the hardware, and then read it back to make sure the setting is valid. If you want to set something that the GUI changes to a different number, that either means that GUI is rounding (sorry), or the hardware (either the FMCOMMS11 or the FPGA fabric) does not support that mode/precision.

If you want to go play with ``/sys/bus/iio/devices/....`` and manipulate the devices behind the back of the GUI, it's still possible to see the settings by clicking the "refresh" button at the bottom of the GUI.

If you think the device has a setting that isn't managed by this tab, check out the `AD936X Advanced Plugin <https://wiki.analog.com/fmcomms2_advanced_plugin>`_ for the IIO Oscilloscope.

The FMCOMMS11 view is divided in four sections:

-  **ADC**
-  **Attenuator**
-  **DDS**
-  **DAC**
-  **Output VGA**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/controls.jpg
   :align: right
   :width: 400px

ADC
---

-  **Sampling frequency(MHz):** Dispay the sample rate of the ADC.
-  **Input Scales / Reference:** Set the scale of the signal input.
-  **Channel 0 Test mode:** control the JESD204B interface test injection points.

Input Attenuator
----------------

-  **Gain(dB):** Controls RX signal atteniation.

DDS
---

axi-ad9162-hpc
~~~~~~~~~~~~~~

The plugin provides several options on how the transmitted data is generated.I

It is possible to either use the built-in two tone **Direct Digital Synthesizer (DDS)** to transmit a bi-tonal signal on channels I and Q of the DAC. Or it is possible to use the **Direct Memory Access (DMA) facility** to transmit custom data that you have stored in a file.

This can be achieved by selecting one of the following options listed by the **DDS Mode**:

One CW Tone
~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/controls_1_tone.jpg
   :align: right
   :width: 200px

In **One CW Tone** mode one continuous wave (CW) tone will be outputted. The plugin displays the controls to set the Frequency, Amplitude and Phase for just one tone and makes sure that the amplitude of the other tone is set to 0. The resulting signal will be outputted on the Channel I of the DAC and the exact same signal but with a difference in phase of 90 degrees will be outputted on the Channel Q of the DAC.


Two CW Tone
~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/controls_2_tone.jpg
   :align: right
   :width: 340px

In **Two CW Tone** mode two continuous wave (CW) tones will be outputted. The plugin displays the controls to set the frequencies F1 and F2, amplitudes A1 and A2, phases P1 and P2 for the two tones. The resulting signal will be outputted on the Channel I of the DAC and the exact same signal but with a difference in phase of 90 degrees will be outputted on the Channel Q of the DAC.


Independent I/Q Control
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/controls_independent_i_and_q.jpg
   :align: right
   :width: 300px

In **Independent I/Q Control** the plugin displays the controls to set the frequencies, amplitudes and phases for the two tones that will be outputted on channel I and additionally it allows for the two tones that will be outputted on channel Q of the DAC to be configured independently.

|

.. note::

   Note: The bi-tonal signal (T) is defined as the sum of two tones:

   | T(t) = A1 \* sin(2 \* π \* F1 \* t + P1) + A2 \* sin(2 \* π \* F2 \* t + P2),
   | where A-amplitude, F-frequency, P-phase of a tone.



DAC Buffer Output
~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/controls_dac_buffer.jpg
   :align: right
   :width: 200px

The file selector under the **File Selection** section is used to locate and choose the desired data file. Under the **DAC Channels** section the enabled channels will be used to transmit the data stored in the file. To finalize the process, a click on the **Load** button is required.

| **Restrictions:**
| \* There are two types of files than can be loaded: **.txt** or **.mat**. The IIO-Oscilloscope comes with several :git-iio-oscilloscope:`data files <waveforms>` that can be used. If you want to create your own data files please take a look at the :doc:`Basic IQ Data Files </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>` documentation first.
| \* Due to hardware limitation only specific combinations of enabled channels are possible. You can enable a total of 1, 2, 4, etc. channels. If 1 channel is enabled then it can be any of them. If two channels are enabled then channels 0, 1 or channels 2, 3 can be enabled and so on.


Disable
~~~~~~~

| In this mode both DDS and DMA are disabled causing the DAC channels to stop transmitting any data.

DAC
---

-  **Sampling frequency(MHz):** Dispay the sample rate of the DAC.
-  **NCO Frequency (MHz):** Set the frequency for NCO to enable digital frequency shifts of signals with near infinite precision.
-  **Filter Settings:** Enable/disable finite impulse response filter with 85 dB digital attenuation that implements 2× NRZ mode.

Output VGA
----------

-  **Gain(dB):** Set the TX gain output.

.. note::

   Upon pressing **Reload Settings** button the values will be reloaded with the corresponding driver values. Useful in scenarios where the diver values get changed outside this plugin (e.g with the use of Debug plugin) and a refresh on plugin's values is needed.


.. hint::

   Some plugin values will be rounded to the nearest value supported by the hardware.

