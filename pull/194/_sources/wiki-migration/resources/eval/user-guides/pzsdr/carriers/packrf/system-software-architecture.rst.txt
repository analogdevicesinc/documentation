Portable Radio Software
=======================

The software for the ADRV-PACKRF is provided by Analog Devices as an open source reference design that can be used in various applications. The system source code consists of several components, which are used together to control onboard devices and provide connectivity to external tools for development. The following components are either used to build the ADRV-PACKRF firmware or can be used remotely from a host PC through a network connection:

-  FPGA HDL Code :git-hdl:`Standard Reference Design <projects/adrv9361z7035/ccpackrf_lvds>`, :git-TransceiverToolbox:`Modem Enhancements <CI/projects/adrv9361z7035/ccbox_lvds_modem>`)
-  Linux Kernel/Device Drivers (:doc:`Transceiver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`, :git-rfsom-box-gui:`Modem Controller <tun_tap>`)
-  `U-boot Bootloader <https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/18841973/Build+U-Boot>`_
-  `Graphical User Interface (GUI) <https://github.com/analogdevicesinc/rfsom-box-gui>`_
-  :doc:`Modem Design Workflow and Generation </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp_modem>`
-  :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`3rd Party Simulation and Development Tools </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`
-  :doc:`MATLAB/Simulink </wiki-migration/resources/eval/user-guides/matlab_bsp>`, :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`

The default design used for FPGAs in the PackRF kit contains the standard reference design built from the :git-hdl>`__. This design is provided by default since it allows a more general interaction with the transceiver, allowing an end-user to move data through the transceiver in a traditional way with standard tools. The modem design, which can be built from the `Transceiver Toolbox <https::`ADI HDL repository </github.com/analogdevicesinc/TransceiverToolbox>`, modifies the data pipelines which can be unintuitive for those starting out with the kit. The streaming interfaces in the modem design, which represent the transmit and receive chains in software still exist or will appear in development tools, but the data provided by them and their control mechanisms are different.

Getting Started
---------------

For those starting out with the PackRF kit, using the standard :doc:`ADRV9361 user-guide </wiki-migration/resources/eval/user-guides/adrv9361-z7035>` is the best place to begin to understand how to use the device. As well as getting started with the basic ADI tools and 3rd party software support.

If you need to create an SD card for the radios or update an existing card, follow :doc:`this guide </wiki-migration/resources/tools-software/linux-software/zynq_images>` selecting **zynq-adrv9361-z7035-box** boot files.
