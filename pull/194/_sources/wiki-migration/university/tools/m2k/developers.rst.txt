ADALM2000 for Developers
========================

The people who typical read these pages are those who write custom software or HDL (for the FPGA) that run directly on the M2K device. This may put the M2K in different modes, and support different external USB devices (including USB/LAB, or USB/WiFi), extending the capabilities of the device, or completely changing the data that is transferred to the host. Since the goal of the project is to keep things as open as possible, the details on how to compile kernels, create bit files, assemble FIT files and load them into the device, should be found here.

While we do have a few examples, and show how to re-create the default software loads, since this the hardware can be nearly a blank slate for your project, you can do anything you want.

Content
-------

.. container:: hide

   please make sure that all these are in the ./devs subdirectory


-  Introduction *(Coming soon)*
-  Hardware

   -  Detailed Specifications *(Coming soon)*
   -  `Schematics <https://wiki.analog.com/.devs/hardware>`_
   -  Detailed Performance *(Coming soon)*
   -  Accessing the Console\ *(Coming soon)* with the `ADALM-JTAGUART <https://wiki.analog.com/../uartjtag>`_ adapter
   -  Accessing FPGA JTAG\ *(Coming soon)* with the `ADALM-JTAGUART <https://wiki.analog.com/../uartjtag>`_ adapter

-  :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`

   -  :doc:`M2K HDL Architecture </wiki-migration/resources/fpga/docs/hdl/m2k>`
   -  :doc:`AXI_AD9963 </wiki-migration/resources/fpga/docs/axi_ad9963>`
   -  :doc:`AXI_ADC_DECIMATE </wiki-migration/resources/fpga/docs/axi_adc_decimate>`
   -  :doc:`AXI_DAC_INTERPOLATE </wiki-migration/resources/fpga/docs/axi_dac_interpolate>`
   -  :doc:`AXI_LOGIC_ANALYZER </wiki-migration/resources/fpga/docs/axi_logic_analyzer>`
   -  :doc:`AXI_ADC_TRIGGER </wiki-migration/resources/fpga/docs/axi_adc_trigger>`
   -  :doc:`UTIL_VAR_FIFO </wiki-migration/resources/fpga/docs/util_var_fifo>`
   -  :doc:`UTIL_EXTRACT </wiki-migration/resources/fpga/docs/util_extract>`

-  Device Drivers

   -  :doc:`AXI ADC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
   -  :doc:`AXI DAC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
   -  AXI DMAC Linux Driver
   -  etc.

-  Building the Firmware image from source

   -  :doc:`Obtaining the Build Sources </wiki-migration/university/tools/pluto/obtaining_the_sources>`
   -  :doc:`Building the Firmware Image </wiki-migration/university/tools/pluto/building_the_image>`

-  :doc:`USB OTG – HOST function Support </wiki-migration/university/tools/pluto/usb_otg_host_function_support>`
-  :doc:`Using U-Boot's DFU modes </wiki-migration/university/tools/pluto/users/firmware>`
-  :doc:`Rebooting M2k </wiki-migration/university/tools/pluto/devs/reboot>`
