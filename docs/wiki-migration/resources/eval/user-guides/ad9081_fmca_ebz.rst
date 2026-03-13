AD9081 & AD9082 & AD9988 & AD9986 Prototyping Platform User Guide
=================================================================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081-fmca-ebz_ad9082-fmca-ebz.png
   :align: center
   :width: 600

The :adi:`AD9081-FMCA-EBZ`, :adi:`AD9988-FMCB-EBZ` or :adi:`AD9082-FMCA-EBZ`, :adi:`AD9986-FMCB-EBZ` is a FMC cards for the :adi:`AD9081`, :adi:`AD9988` or :adi:`AD9082`, :adi:`AD9986`, information on the card and how to use it with standard Xilinx and Intel Carriers, the design package that surrounds it, and the software which can make it work can be found here.

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to :doc:`ask </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`.

-  Use the board to better understand the :adi:`AD9081`, :adi:`AD9988`, :adi:`AD9082`, :adi:`AD9986`

   -  :doc:`Prerequisites to using the board </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/prerequisites>`
   -  :doc:`Installation of the Heat Sink with Integrated Fan </wiki-migration/resources/eval/ad9082>`
   -  :doc:`Quickstart </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart>`

      -  :doc:`Zynq-7000 SoC ZC706 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynq>`
      -  :doc:`Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynqmp>`
      -  :doc:`Virtex UltraScale+ VCU118 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/microblaze>`

   -  Linux Applications

      -  :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

         -  :doc:`AD9081 Capture Window </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_iio_osc>`
         -  :doc:`AD9081 Control Plugin </wiki-migration/resources/tools-software/linux-software/ad9081_plugin>`

      -  :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>`
      -  :doc:`JESD204 Eye Scan </wiki-migration/resources/tools-software/linux-software/jesd_eye_scan>`
      -  :doc:`IIO Command Line Tools </wiki-migration/resources/tools-software/linux-software/libiio/cmd_line>`

Useful links
------------

-  :doc:`AD9081/AD9082/AD9988/AD9986 Quick Start Guides </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart>`

   -  :doc:`Zynq-7000 SoC ZC706 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynq>`
   -  :doc:`Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynqmp>`
   -  :doc:`Virtex UltraScale+ VCU118 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/microblaze>`
   -  :doc:`Versal ACAP VCK190 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/versal>`
   -  `Arria10 SoC Quick Start Guide <https://wiki.analog.com/resources/eval/user-guides/ad9081/quickstart/a10soc]>`_

-  :doc:`AD9081-FMCA-EBZ (Single MxFE) HDL Reference Design </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_fmca_ebz_hdl>`

   -  :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`
   -  :doc:`Generic JESD204B block designs </wiki-migration/resources/fpga/docs/hdl/generic_jesd_bds>`
   -  :doc:`JESD204B High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`

-  :doc:`AD9081/AD9082/AD9988/AD9986 Linux Driver Support </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`

::

         - :doc:`JESD204 (FSM) Interface Linux Kernel Framework </wiki-migration/resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
         - :doc:`HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-pll/hmc7044>`
         - :doc:`AXI-DMAC DMA Controller Linux Driver </wiki-migration/resources/tools-software/linux-drivers/axi-dmac>`
         - :doc:`JESD204B Transmit Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`
           - :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>` 
         - :doc:`JESD204B Receive Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`
           - :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>` 
         - :doc:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`
           - :doc:`JESD204 Eye Scan </wiki-migration/resources/tools-software/linux-software/jesd_eye_scan>`
         - :doc:`AXI ADC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
         - :doc:`AXI DAC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
   * :doc:`MATLAB Support </wiki-migration/resources/tools-software/hsx-toolbox>`
        * MATLAB support is provided through the :doc:`High Speed Converter Toolbox </wiki-migration/resources/tools-software/hsx-toolbox>`
   * :doc:`Python Support </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`
        * PYTHON support is provided through the :doc:`Device Specific Python Interfaces For IIO Drivers </wiki-migration/resources/tools-software/linux-software/pyadi-iio>` 
        * `PyADI-IIO Documentation <https://analogdevicesinc.github.io/pyadi-iio/>`_
        * `AD9081 class documentation <https://analogdevicesinc.github.io/pyadi-iio/devices/adi.ad9081.html>`_
   * Product Datasheet
       * :adi:`AD9081 <media/en/technical-documentation/data-sheets/AD9081.pdf>`
       * :adi:`AD9082 <media/en/technical-documentation/data-sheets/AD9082.pdf>`
       * :adi:`AD9988 <media/en/technical-documentation/data-sheets/AD9988.pdf>`
       * :adi:`AD9986 <media/en/technical-documentation/data-sheets/AD9986.pdf>`
   * :adi:`UG-1578, Device User Guide <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`
   * :adi:`UG-1829, Evaluation Board User Guide <media/en/technical-documentation/user-guides/ad9081-fmca-ebz-9082-fmca-ebz-ug-1829.pdf>`

Support
-------

Analog Devices will provide limited online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone <community/fpga>`.

Software support
----------------

-  :doc:`AD9081/AD9082/AD9988/AD9986 Linux Driver Support </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`

Useful links
------------

-  :doc:`AD9081/AD9082/AD9988/AD9986 Quick Start Guides </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart>`

   -  :doc:`Zynq-7000 SoC ZC706 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynq>`
   -  :doc:`Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynqmp>`
   -  :doc:`Virtex UltraScale+ VCU118 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/microblaze>`
   -  :doc:`Versal ACAP VCK190 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/versal>`
   -  `Arria10 SoC Quick Start Guide <https://wiki.analog.com/resources/eval/user-guides/ad9081/quickstart/a10soc]>`_

-  :doc:`AD9081-FMCA-EBZ (Single MxFE) HDL Reference Design </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_fmca_ebz_hdl>`

   -  :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`
   -  :doc:`Generic JESD204B block designs </wiki-migration/resources/fpga/docs/hdl/generic_jesd_bds>`
   -  :doc:`JESD204B High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`

-  :doc:`AD9081/AD9082/AD9988/AD9986 Linux Driver Support </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`

::

         - :doc:`JESD204 (FSM) Interface Linux Kernel Framework </wiki-migration/resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
         - :doc:`HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-pll/hmc7044>`
         - :doc:`AXI-DMAC DMA Controller Linux Driver </wiki-migration/resources/tools-software/linux-drivers/axi-dmac>`
         - :doc:`JESD204B Transmit Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`
           - :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>` 
         - :doc:`JESD204B Receive Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`
           - :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>` 
         - :doc:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`
           - :doc:`JESD204 Eye Scan </wiki-migration/resources/tools-software/linux-software/jesd_eye_scan>`
         - :doc:`AXI ADC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
         - :doc:`AXI DAC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
   * :doc:`MATLAB Support </wiki-migration/resources/tools-software/hsx-toolbox>`
        * MATLAB support is provided through the :doc:`High Speed Converter Toolbox </wiki-migration/resources/tools-software/hsx-toolbox>`
   * :doc:`Python Support </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`
        * PYTHON support is provided through the :doc:`Device Specific Python Interfaces For IIO Drivers </wiki-migration/resources/tools-software/linux-software/pyadi-iio>` 
        * `PyADI-IIO Documentation <https://analogdevicesinc.github.io/pyadi-iio/>`_
        * `AD9081 class documentation <https://analogdevicesinc.github.io/pyadi-iio/devices/adi.ad9081.html>`_
   * Product Datasheet
       * :adi:`AD9081 <media/en/technical-documentation/data-sheets/AD9081.pdf>`
       * :adi:`AD9082 <media/en/technical-documentation/data-sheets/AD9082.pdf>`
       * :adi:`AD9988 <media/en/technical-documentation/data-sheets/AD9988.pdf>`
       * :adi:`AD9986 <media/en/technical-documentation/data-sheets/AD9986.pdf>`
   * :adi:`UG-1578, Device User Guide <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`
   * :adi:`UG-1829, Evaluation Board User Guide <media/en/technical-documentation/user-guides/ad9081-fmca-ebz-9082-fmca-ebz-ug-1829.pdf>`

Support
-------

Analog Devices will provide limited online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone <community/fpga>`.

Software support
----------------

-  :doc:`AD9081/AD9082/AD9988/AD9986 Linux Driver Support </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
