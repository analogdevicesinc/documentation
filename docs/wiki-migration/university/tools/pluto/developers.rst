ADALM-PLUTO for Developers
==========================

The people who typical read these pages are those who write custom software or HDL (for the FPGA) that run directly on the Pluto device. This may put the Pluto in different modes, and support different external USB devices (including USB/LAB, or USB/WiFi), extending the capabilities of the device, or completely changing the data that is transferred to the host. Since the goal of the project is to keep things as open as possible, the details on how to compile kernels, create bit files, assemble FIT files and load them into the device, should be found here.

While we do have a few examples, and show how to re-create the default software loads, since this the hardware can be nearly a blank slate for your project, you can do anything you want.

Content
-------

.. container:: hide

   please make sure that all these are in the ./devs subdirectory


-  Hardware

   -  :doc:`Detailed Specifications </wiki-migration/university/tools/pluto/devs/specs>`
   -  :doc:`Schematics </wiki-migration/university/tools/pluto/hacking/hardware>`
   -  :doc:`Detailed Performance </wiki-migration/university/tools/pluto/devs/performance>`
   -  :doc:`Accessing FPGA JTAG </wiki-migration/university/tools/pluto/devs/fpga>` with the `ADALM-JTAGUART <https://wiki.analog.com/../uartjtag>`_ adapter

-  C Applications or Shell scripts on the Pluto

   -  :doc:`Running Scripts from USB drive </wiki-migration/university/tools/pluto/devs/usb_otg>`
   -  :doc:`Creating compiled apps to run on-device </wiki-migration/university/tools/pluto/devs/embedded_code>`

-  :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`

   -  :doc:`AD9361 HDL reference design </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>`
   -  :doc:`AXI_AD9361 </wiki-migration/resources/fpga/docs/axi_ad9361>`
   -  :doc:`High-Speed DMA Controller Peripheral </wiki-migration/resources/fpga/docs/axi_dmac>`

-  `device_drivers <https://wiki.analog.com/device_drivers>`_

   -  :doc:`AD9361 high performance, highly integrated RF Agile Transceiver™ Linux device driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
   -  :doc:`AXI ADC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
   -  :doc:`AXI DAC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
   -  :doc:`AXI-DMAC DMA Controller Linux Driver </wiki-migration/resources/tools-software/linux-drivers/axi-dmac>`
   -  :adi:`ADM1177` Digital Power Monitor Linux Driver
   -  etc.

-  Building the Firmware image from source

   -  `obtaining_the_sources <https://wiki.analog.com/obtaining_the_sources>`_
   -  `building_the_image <https://wiki.analog.com/building_the_image>`_

-  `controlling_the_transceiver_and_transferring_data <https://wiki.analog.com/controlling_the_transceiver_and_transferring_data>`_
-  :doc:`controlling_gpios </wiki-migration/university/tools/pluto/devs/controlling_gpios>`
-  Accessing the AD9363 inside Pluto from userspace

   -  :git-libiio:`libiio local mode example <examples/ad9361-iiostream.c>`
   -  :doc:`Linux driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

-  `usb_otg_host_function_support <https://wiki.analog.com/usb_otg_host_function_support>`_
-  :doc:`Connecting the Pluto to the Internet </wiki-migration/university/tools/pluto/devs/port_forwarding>`
-  :doc:`Using U-Boot's DFU modes </wiki-migration/university/tools/pluto/users/firmware>`
-  :doc:`Boot magic explained </wiki-migration/university/tools/pluto/devs/booting>`
-  :doc:`Reboot Modes </wiki-migration/university/tools/pluto/devs/reboot>`
