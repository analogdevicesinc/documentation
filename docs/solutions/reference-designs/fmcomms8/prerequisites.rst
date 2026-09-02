.. include-template:: ../template/prerequisites.rst.jinja

    prerequisites_ref: fmcomms8 prerequisites
    chip_name: ADRV9009
    eval_board: EVAL-AD-FMCOMMS8-EBZ
    carriers_ref: fmcomms8 carriers
    has_linux: true
    additional_hardware:
        - Test equipment for generating analog input signals (signal generator, SMA cable).
    additional_software:
        - :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`
        - UART terminal application (PuTTY/TeraTerm/Minicom), 115200 8N1
