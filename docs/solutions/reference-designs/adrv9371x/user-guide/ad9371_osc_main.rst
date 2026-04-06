AD9371/AD9375 IIO Oscilloscope
--------------------------------------------------------------------------------

.. include-template:: ../../common/using-iio-osc.rst.jinja

   has_linux: true
   has_no_os: true
   show_connection_image: false
   iio_has_plugin: true
   iio_plugin_ref: adrv9371x plugin
   iio_channel_description: |
     Main receivers RX1 and RX2 are handled by the axi-ad9371-rx-hpc IIO
     device, while the observation is handled by the axi-ad9371-rx-obs-hpc
     device.

     Channels:

     .. list-table::
        :header-rows: 1

        * -
          - Receiver Inputs
          -
        * - IIO Device Channels
          - voltage0_i voltage0_q
          - voltage1_i voltage1_q
        * - axi-ad9371-rx-hpc
          - RX1
          - RX2
        * - axi-ad9371-rx-obs-hpc
          - OBS RX1
          -

   iio_show_data_capture: true
   iio_show_time_domain: true
   iio_time_domain_image: ../images/myk_cap_time.png
   iio_show_frequency_domain: true
   iio_frequency_domain_image: ../images/myk_cap_freq.png
