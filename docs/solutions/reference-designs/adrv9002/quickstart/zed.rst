.. include-template:: ../../template/quickstart/zed.rst

   # General configuration
   quickstart_ref: adrv9002-zed
   eval_board: EVAL-ADRV9002
   hdl_project_doc: adrv9001
   prerequisites_ref: adrv9002 prerequisites

   # Feature flags
   has_linux: true
   has_noos: true
   has_lvds_support: true
   has_vadj_warning: true
   has_vadj_led: true
   iio_has_plugin: true
   scopy_has_plugin: true
   has_pyadi_iio: true

   # General/shared images
   quickstart_image: ../images/adrv9002_zed_quickstart.png
   vadj_led_image: ../images/adrv9002_vadj_led.png
   jumper_config_image: ../images/jumper_config.png

   # Linux-specific configuration
   linux_setup_steps_file: linux_setup_steps.rst
   boot_log_file: boot_log.rst
   linux_show_connection_image: true
   linux_connection_image: ../images/ADRV9002_IIO_connection_zed.png
   linux_additional_hardware:
     - Signal generator
     - Signal analyzer
     - Signal synthesizer (required only if using external clock source)
     - 1x SMA cable for signal generator
     - 1x SMA cable for signal analyzer
     - 1x SMA cable for signal synthesizer (if using external clock)
     - (Optional) USB keyboard & mouse and a HDMI compatible monitor
   iio_plugin_ref: adrv9002-plugin
   linux_iio_show_data_capture: true
   linux_iio_show_time_domain: true
   linux_iio_show_frequency_domain: true
   linux_iio_time_domain_image: ../images/ADRV9002_time_domain.png
   linux_iio_frequency_domain_image: ../images/ADRV9002_fourier_domain.png
   scopy_plugin_path: plugins/adrv9002/adrv9002
   pyadi_iio_example: /examples/adrv9002_example.py

   # No-OS specific configuration
   noos_project_path: projects/adrv9001
   noos_project_specific_doc: projects/rf-transceiver/adrv9001
   noos_setup_image: ../images/adrv9002_noos_setup.jpeg
   noos_has_loopback: true
   noos_additional_hardware:
     - 2x SMA cable for loopback
     - (Optional) USB keyboard & mouse and a HDMI-compatible monitor
   noos_setup_steps_file: noos_setup_steps.rst
   noos_console_output_file: noos_console_output.rst
   noos_iio_has_plugin: true
