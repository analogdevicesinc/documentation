.. include-template:: ../template/prerequisites.rst.jinja

    prerequisites_ref: eval-cn0577-fmcz prerequisites
    chip_name: LTC2387-18
    eval_board: CN0577
    carriers_ref: eval-cn0577-fmcz carriers
    has_linux: true
    additional_hardware:
        - Test equipment for generating analog input signals: signal generator, SMA cable.
    additional_software:
        - :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`
        - UART terminal application (PuTTY/TeraTerm/Minicom), 115200 8N1
