User Guide
================================================================================

The complete user guides of the evaluation boards can be found at:
   - :adi:`AD9081/AD9082 System Development User Guide <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`
   - :adi:`Evaluating the AD9081, AD9082, AD9986, or AD9988 Mixed Signal, Front-End RF Transceiver <media/en/technical-documentation/user-guides/eval-ad9081-9082-9986-9988-ug-1829.pdf>`

Software Guide
-------------------------------------------------------------------------------
The :adi:`EVAL-AD9081`, :adi:`EVAL-AD9082`, :adi:`EVAL-AD9986`, and
:adi:`EVAL-AD9988` evaluation boards are supported within the :ref:`libiio`
library. This library is cross-platform (Windows, Linux, Mac) with language
bindings for C, C#, Python, MATLAB, and others. The following software can be
used for the evaluation of the boards:

.. include-template:: ../common/using-iio-osc.rst.jinja

   has_linux: true
   has_no_os: false
   show_linux_connection_image: true
   linux_connection_image: images/iio_ad9209_connection.jpg
   iio_has_plugin: true
   iio_channel_description: |

      .. list-table::
        :header-rows: 1

        * -
          -
          - Receiver Inputs
          -
          -
        * - IIO Device Channels
          - voltage0_i voltage0_q
          - voltage1_i voltage1_q
          - voltage2_i voltage2_q
          - voltage3_i voltage3_q
        * - axi-ad9081-rx-hpc
          - RX1
          - RX2
          - RX3
          - RX4

   iio_show_data_capture: true
   iio_show_time_domain: true
   iio_time_domain_image: images/iio_ad9209_time_domain.jpeg
   iio_show_frequency_domain: true
   iio_frequency_domain_image: images/iio_ad9209_freq_domain.jpeg
