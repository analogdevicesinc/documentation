Profile generation flow using TES
=================================

Profiles
--------

ADRV9002 uses profiles to designate different device configuration settings for the Tx/Rx channels. The profile dictates how the digital filters, analog filters, clock rates, and clock dividers are configured in the device. Some specific parameters set by profiles include the IQ data rate, ADC clock rate, analog filter corners, FIR filter coefficients, and interpolation/decimation factors in the half-band filters. Several profiles can be examined in the ADRV9002 Transceiver Evaluation Software for given device clock frequencies. If the desired profile exists in the software, it is recommended to set up the desired profile in and use the generated JSON file by pressing the ``Generate Profile File`` button. Custom profiles can be generated using other ADI software tools not described here :adi:`ADRV9002 transceiver evaluation software (TES) <en/design-center/landing-pages/001/transceiver-evaluation-software.html>`.

.. warning::

   Profiles are specific to the versions of ADRV9001/2 API that the driver uses. Therefore, they must be generated from the :adi:`TES software <en/design-center/landing-pages/001/transceiver-evaluation-software.html>` that coincides with that API version. Unfortunately, profiles themselves are not versioned so it is recommended to note the API version in the generated profile filenames when created. The driver will print the API version during boot for reference.


For more information about profiles and how to load please see here: :doc:`Profile section on the ADRV9002 Linux driver documentation </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002>`

.. note::

   We are about to release a library which allows device profile generation outside of TES. This library can be used in applications such as the :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`, or other SDR software.


Installation and Configuration
------------------------------

Detailed installation and configuration instructions can be found under section ``TRANSCEIVER EVALUATION SOFTWARE (TES)`` in the :adi:`UG-1828: ADRV9001 system development user guide <media/en/technical-documentation/user-guides/adrv9001-system-development-user-guide-ug-1828.pdf>`

Download:

-  :adi:`TRANSCEIVER EVALUATION SOFTWARE (TES) <en/license/licensing-agreement/transceiver-evaluation-software.html>`

Worked example
--------------

In the following picture we can see the base controls for the profile:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/jupiter-sdr/tes_main_configuration_4.png
   :align: center
   :width: 800px

In here, one can change the main profile type (LTE, DMR, etc), interface rate, disabling ports and so on...

.. important::

   Special care for the fields highlighted in channel 2 (also applies for channel 1) that must be set like in the image. The LVDS enforcement is specific to **jupiter**.


Once we are done with the settings, time to generate the stream and the profiles files:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/jupiter-sdr/tes_save_profile_and_stream_2.png
   :align: center
   :width: 800px

In the next subsections, we can see some extra and useful settings that one might want to set before generating the stream and the profile files.

Enable NCO Frequency offset
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/jupiter-sdr/tes_enable_nco_correction_2.png
   :align: center
   :width: 800px

.. note::

   Enabling this setting, enables the IIO attribute ':doc:`in_voltage0_nco_frequency </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002>`'. These settings are on by default on **jupiter** default profile.


Enable Antenna Diversity
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/jupiter-sdr/tes_diversity_settings_2.png
   :align: center
   :width: 800px

.. note::

   This setting affects the LO mapping (which ports each LO drives). Basically having this on, means that all ports are mapped into the same LO.


.. warning::

   This settings is obviously only available if TDD is set in the **Device Configuration** tab


Enable Frequency hopping
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/jupiter-sdr/test_fh_enablement_2.png
   :align: center
   :width: 800px

.. note::

   The only thing needed to do in TES is just to enable Frequency hopping as highlighted. All the other settings does not map in any profile setting...

