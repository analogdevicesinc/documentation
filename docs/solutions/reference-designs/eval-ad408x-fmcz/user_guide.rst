User Guide
================================================================================

The complete user guides of the evaluation boards can be found at:
   - :adi:`EVAL-AD4080-FMCZ User Guide <media/en/technical-documentation/user-guides/eval-ad4080-ug-2214.pdf>`
   - :adi:`EVAL-AD4083-FMCZ User Guide <media/en/technical-documentation/user-guides/eval-ad4083.pdf>`
   - :adi:`EVAL-AD4086-FMCZ User Guide <media/en/technical-documentation/user-guides/eval-ad4086.pdf>`

Software guide
-------------------------------------------------------------------------------

The :adi:`EVAL-AD4080-FMC`, :adi:`EVAL-AD4083-FMC`, and :adi:`EVAL-AD4086-FMC`
evaluation boards are supported within the :ref:`libiio` library. This library
is cross-platform (Windows, Linux, Mac) with language bindings for C, C#,
Python, MATLAB, and others. The following software can be used for the
evaluation of the boards:

.. include-template:: ../common/using-iio-osc.rst.jinja

   has_linux: true
   has_no_os: false
   show_connection_image: false
   iio_has_plugin: false
   iio_show_data_capture: true
   iio_show_time_domain: true
   iio_time_domain_image: images/iio_408x_time_domain.png
   iio_show_frequency_domain: true
   iio_frequency_domain_image: images/iio_408x_freq_domain.png

PyADI-IIO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:git-pyadi-iio:`PyADI-IIO </>` is a Python abstraction module for ADI hardware
with IIO drivers. An example for the AD408x can be found
:git-pyadi-iio:`here <examples/ad4080_example.py>`.
