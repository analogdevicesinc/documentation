.. include-template:: ../template/prerequisites.rst.jinja

    prerequisites_ref: ad9656_fmc prerequisites
    chip_name: AD9656
    eval_board: EVAL-AD9656
    carriers_ref: ad9656_fmc carriers
    additional_hardware:
      - Test equipment for generating analog input signals (signal generator, SMA cable)
    additional_software:
      - :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`
      - UART terminal application (PuTTY/TeraTerm/Minicom), 115200 8N1