====== AD-FMCOMMS1-EBZ Quick Start Guide on Xilinx FPGA Boards Without OS ======

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



This guide provides some quick instructions on how to setup the AD-FMCOMMS1-EBZ on either:

-  `AC701 <https://www.xilinx.com/AC701>`__
-  `KC705 <https://www.xilinx.com/KC705>`__
-  `VC707 <https://www.xilinx.com/VC707>`__
-  `ZC702 <https://www.xilinx.com/ZC702>`__
-  `ZC706 <https://www.xilinx.com/ZC706>`__
-  `Avnet ZED Board <http://zedboard.org/product/zedboard/>`__

|

.. important::


| The ML605 XPS project remain on this website only for legacy purposes. The support for XPS projects has been discontinued.


Required Software
=================

-  We upgrade the Xilinx tools on every release. The supported version number can be found in our :git-hdl:`git repository <tree/master>`.

Required Hardware
=================

-  AD-FMCOMMS1-EBZ FMC Board
-  Xilinx ML605 / Xilinx AC701 / Xilinx KC705 / Xilinx VC707 / Xilinx ZC702 / Xilinx ZC706 / Digilent ZED

Downloads
---------

|

.. admonition:: Download
   :class: download

   **no-OS Drivers:** :git-no-OS:`fmcomms1`

   | \**ML605 HDL Reference Design for ISE: **:git-fpgahdl_xilinx:`cf_xcomm`
     **\ Latest release for VivadoAC701: **https:github.com/analogdevicesinc/hdl/tree/master/projects/fmcomms1/ac701
     \**KC705: \*\* https:\ github.com/analogdevicesinc/hdl/tree/master/projects/fmcomms1/kc705
     **\ VC707: **:git-hdl:`projects/fmcomms1/vc707`
     **\ ZC702: **:git-hdl:`projects/fmcomms1/zc702`
     **\ ZC706: **:git-hdl:`projects/fmcomms1/zc706`
     **\ ZED: **:git-hdl:`projects/fmcomms1/zed`
     **\ Old releases for Vivado\ **
   **\ For Vivado 2013.4 :\*\*\ :git-hdl:`projects/fmcomms1`


Hardware Setup
--------------

-  Connect the power and UART cables of the Xilinx FPGA board
-  Connect the AD-FMCOMMS1-EBZ FMC board to the Xilinx FPGA board on the:

   -  LPC FMC connector for KC705, ZC706, ZED;
   -  LPC FMC1 connector for ZC702;
   -  HPC FMC connector for AC701, ML605;
   -  HPC FMC2 connector for VC707.

The transmit signal may be observed using a spectrum analyzer. The receive side may be sourced by either the transmit side or a signal source. If it is the transmit side, connect an SMA cable from the transmit to receive or connect antennae on both. If it is a signal source the frequency needs to be 2.4G\ *+*\ f, 0 dBm where f is the baseband.

.. note::

   The default RX gain in case of no-OS software is 10 dB. This could be too high, when an SMA cable is used for external loop-back. In this case the user should reduce the RX gain to its minimum value: 4.5 dB, in order to prevent saturation.


Software Setup for Vivado
-------------------------

Example for a ZC702 board:

-  After :doc:`building the project in Vivado </wiki-migration/resources/fpga/docs/build>` for the used FPGA board, a **SDK_Export** folder will be created in **../fmcomms1_board.sdk/SDK**
-  Open the Xilinx SDK for Vivado. When the SDK starts it asks to provide a folder where to store the workspace. Any folder can be provided.
-  Go to **File->New->Application project**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/new_app_project.png
   :alt: New Application Project
   :align: center
   :width: 600px

-  Use a new hardware platform, so choose **New** in **Target Hardware** section

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/new_platform.png
   :alt: New Platform
   :align: center
   :width: 400px

-  At the **Target Hardware Specification** section browse the location of the hardware description file. This file's extension should be **.xml** or **.hdf**, and is located in the directory of the hdl design. **Note:** If the file does not exist, probably you forgot to make an **Export hardware** (in Vivado **File** -> **Export** -> **Export Hardware...**)

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/fmcomms1_new_hw_project.png
   :alt: New Hardware Project
   :align: center
   :width: 400px

-  Then give a name to the project and click **Next**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/project_name.png
   :alt: Project Name
   :align: center
   :width: 400px

-  In the next window choose **Empty Application** and click **Finish**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/templates.png
   :alt: Available Templates
   :align: center
   :width: 400px

-  Now the project without source code looks like this

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/empty_project_zynq.png
   :alt: Empty Project
   :align: center
   :width: 600px

-  Then the source code(all folders from **no-OS Drivers**, except Chipscope, Evaluate and PIC) must be added from Github to **src** folder.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/fmcomms1_project_without_include_directories_paths.png
   :alt: Project without directories paths
   :align: center
   :width: 600px

-  Afterwards click right on project name and go to **Properties**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/project_properties.png
   :alt: Project properties
   :align: center
   :width: 600px

-  In the window that appears go to **Settings->Directories** and include the paths of the directories from **src** for both **Debug** and **Release** configurations.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/fmcomms1_settings_include_directories_paths.png
   :alt: Include paths
   :align: center
   :width: 600px

-  The *Project Explorer* window now shows the projects that exist in the workspace and the files for each project. The SDK should automatically build the projects and the *Console* window will display the result of the build. If the build is not done automatically select the **Project->Build Automatically** menu option.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/fmcomms1_project_explorer_zynq.png
   :alt: Project Explorer
   :align: center
   :width: 600px

-  The default project configuration assumes that a Xilinx ML605 FPGA board is used and that the FMCOMMS1 is connected to this board on the FMC LPC connector. In the file *Common/main.c* change the *XCOMM_DefaultInit* initialization structure so that the FPGA board and the FMC port used to connect the FMCOMMS1 to the FPGA board correspond to your actual hardware setup.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/board_config.png
   :alt: Board Configuration
   :align: center
   :width: 400px

-  At this point the software project setup is complete, the FPGA can be programmed and the software can be downloaded into the system. You can program the FPGA by going to **Xilinx Tools**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/fmcomms1_program_fpga.png
   :alt: Program FPGA
   :align: center
   :width: 600px

-  Then choose this bitstream and press **Program**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/fmcomms1_program_fpga_with_bitstream.png
   :alt: Program FPGA with bitstream
   :align: center
   :width: 400px

-  This window will appear next.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/fmcomms1_program_fpga_progress.png
   :alt: Program FPGA progress
   :align: center
   :width: 400px

-  Afterwards a *Run Configuration* must be created and then press **Run**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/fmcomms1_run_configuration.png
   :alt: Run Configuration
   :align: center
   :width: 600px

The no-OS drivers source code contains an example on how to:

-  initialize the board
-  test the ADC communication
-  test the DAC communication
-  set the VGA gain
-  set the receive and transmit frequencies
-  send a sinewave over the air and receive it back

The example code outputs on the UART the status of each operation as shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/fmcomms1_test_uart.png
   :alt: UART Test
   :align: center
   :width: 300px

The output of the example program can be viewed in the SDK console by enabling the *Connect STDIO Console* option and setting the baud rate of the UART port to 115200.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/stdio_config_vivado.png
   :alt: Baud rate
   :align: center
   :width: 600px

As an alternative an UART terminal can be used to capture the output of the example program. The number of used UART port depends on the computer's configuration. The following settings must be used in the UART terminal:

-  Baud Rate: 115200bps
-  Data: 8 bit
-  Parity: None
-  Stop bits: 1 bit
-  Flow Control: none

The example code is located in the "*Common/main.c*" file and the implementations of the ADC and DAC test routines can be found in the "*Common/test.c*" file.

After running the example program the system is configured to generate a sinewave and send it over the air using a 2.4GHz carrier. The signal is received back, brought to baseband again and digitized by the ADC on the FMCOMMS1. The I and Q samples generated by the ADC can be viewed using the *Vivado Hardware Manager*. These are the steps than need to be followed to view the sine waves:

-  First make sure that the board is programmed and the program is currently running
-  Then open Vivado and go to **Flow->Open Hardware manager**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/vivado_open_hardware_manager.png
   :alt: Open Hardware Manager
   :align: center
   :width: 600px

-  In the new window select **Open a new hardware target**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/vivado_open_new_hardware_target.png
   :alt: Open New Hardware Target
   :align: center
   :width: 600px

-  Then click **Next** 4 times and then **Finish**

| |Open New Hardware Target|\ |Server name|\ |Select Target| |Set Properties|\ |image1|
| \* This is how the *Vivado Hardware Manager* looks like. Now go to Probes files. |Device Properties|

-  And browse for the folder where the project was compiled **../fmcomms1_board.runs/impl_1/debug_nets.ltx**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/fmcomms1_specify_probes_file.png
   :alt: Specify Probes File
   :align: center
   :width: 400px

-  Then do a right click on the active target and choose **Refresh Device**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/vivado_hw_refresh_device.png
   :alt: Refresh Device
   :align: center
   :width: 600px

-  Afterwards do another right click on the active target and choose **Run Trigger**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/vivado_hw_run_trigger.png
   :alt: Run Trigger
   :align: center
   :width: 600px

-  This is how the 56 digital signals look like. Now we have to compose the sinewaves.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/fmcomms1_vivado_hw_ila_signals.png
   :alt: ILA Signals
   :align: center
   :width: 600px

-  First select the first 14 signals, do a right click and choose **New Virtual Bus**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/fmcomms1_vivado_hw_ila_signals_new_virtual_bus.png
   :alt: New Virtual Bus
   :align: center
   :width: 600px

-  Then give a name to that virtual bus

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/fmcomms1_vivado_hw_ila_signals_new_virtual_bus_specify_name.png
   :alt: Specify Virtual Bus Name
   :align: center
   :width: 600px

-  In order to see a sinewave you have to right click on the name of the virtual bus, choose **Analog** for **Waveform Style** option.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/fmcomms1_vivado_hw_ila_signals_waveform_style_analog.png
   :alt: Analog Waveform Style
   :align: center
   :width: 600px

-  Now you can see a sinewave, but the radix is not the good one. In order to have the right radix, you must choose **Signed Decimal** for **Radix**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/fmcomms1_vivado_hw_ila_signals_radix_signed_decimal.png
   :alt: Signed Decimal Radix
   :align: center
   :width: 600px

-  Now the signal looks like a sinewave

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/fmcomms1_vivado_hw_ila_signals_one_virtual_bus_forms_a_sinewave.png
   :alt: One Virtual Bus Sinewave
   :align: center
   :width: 600px

-  And after you did the same steps for the other 3x14 remaining signals, you should have 4 sinewaves composed of 56 signals. Because of the working frequency of the ILA core, data has been split into 2 buses, so the actual data from the Evaluation board would be I_0 interleaved with I_1, and Q_0 interleaved with Q_1.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/fmcomms1_vivado_hw_ila_signals_4_virtual_buses_form_sinewaves.png
   :alt: 4 Virtual Buses Sinewaves
   :align: center
   :width: 600px

.. image:: https://wiki.analog.com/_media/navigation AD-FMCOMMS1-EBZ#zynq
   :alt: Linux on ZC702, ZC706, ZED#.:\|Quick Start Guides#none

.. |Open New Hardware Target| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/vivado_open_new_hardaware_target_start.png
   :width: 290px
.. |Server name| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/vivado_open_new_hardaware_target_server_name.png
   :width: 290px
.. |Select Target| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/vivado_open_new_hardware_target_select_target.png
   :width: 290px
.. |Set Properties| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/vivado_open_new_hardware_target_set_properties.png
   :width: 290px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/vivado_open_new_hardware_target_finish.png
   :width: 290px
.. |Device Properties| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/vivado_hardware_device_properties.png
   :width: 600px
