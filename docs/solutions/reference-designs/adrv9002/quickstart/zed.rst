.. include-template:: ../../template/quickstart/zed.rst.jinja

   # General configuration
   quickstart_ref: adrv9002-zed
   eval_board: EVAL-ADRV9002
   hdl_project_doc: adrv9001
   prerequisites_ref: adrv9002 prerequisites

   # Feature flags
   has_linux: true
   has_no_os: true
   has_lvds_support: true
   has_vadj_warning: true
   has_vadj_led: true
   has_local_display: true

   # General/shared images
   quickstart_image: ../images/adrv9002_zed_quickstart.png
   vadj_led_image: ../images/adrv9002_vadj_led.png
   jumper_config_image: ../images/jumper_config.png

   # Linux-specific configuration
   linux_setup_steps_file: linux_setup_steps.rst
   boot_log_file: boot_log.rst
   linux_additional_hardware:
     - Signal generator
     - Signal analyzer
     - Signal synthesizer (required only if using external clock source)
     - 1x SMA cable for signal generator
     - 1x SMA cable for signal analyzer
     - 1x SMA cable for signal synthesizer (if using external clock)
     - (Optional) USB keyboard & mouse and a HDMI compatible monitor

   # No-OS specific configuration
   no_os_project_path: projects/adrv9001
   no_os_project_specific_doc: projects/rf-transceiver/adrv9001
   no_os_setup_image: ../images/adrv9002_noos_setup.jpeg
   no_os_has_loopback: true
   no_os_additional_hardware:
     - 2x SMA cable for loopback
   no_os_setup_steps_file: no_os_setup_steps.rst
   no_os_console_output_file: no_os_console_output.rst
