Xilinx SDSoc Targeting Example
==============================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/targetting/sdsoc_logo.png
   :width: 200px

The Xilinx SDSoC™ development environment is a member of the Xilinx SDx™ family that provides a greatly simplified ASSP-like C/C++ programming experience including an easy to use Eclipse IDE and a comprehensive design environment for heterogeneous Zynq® All Programmable SoC and MPSoC deployment. Complete with the industry’s first C/C++ full-system optimizing compiler, SDSoC delivers system level profiling, automated software acceleration in programmable logic, automated system connectivity generation, and libraries to speed programming.

To access the capabilities of SDSoC, please visit http://www.xilinx.com/products/design-tools/software-zone/sdsoc.html

Analog Devices is an SDSoC development environment-qualified Xilinx Alliance Member and offers FMC boards and reference designs that can be used together with the SDSoC environment. Each SDSoC design is based on a platform which defines the hardware and software components on which the SDSoC compiler and linker generate hardware functions and IP-based data motion networks for communication between hardware functions and the platform as well as software drivers and applications. Currently Analog Devices provides SDSoC platform support for the following FMCOMMSx SDR systems:

-  :adi:`AD-FMComms2-EBZ`
-  :adi:`AD-FMComms3-EBZ`

The supported Xilinx Zynq based carriers are:

-  `ZC702 <https://www.xilinx.com/ZC702>`_
-  `ZC706 <https://www.xilinx.com/ZC706>`_

FMCOMMSx SDSoC Platforms
------------------------

The FMCOMMSx SDSoC platforms are automatically generated from the Analog Devices HDL reference designs that accompany the FMCOMMSx boards. Platform generation is done by running a tcl script in the Vivado tcl console. This script creates the platform Vivado project from the HDL reference design, as well as the platform software files. The generated platforms support Linux OS.

Platform generation steps:

-  Download the Analog Devices HDL reference designs repository from github using the link provided in the *Downloads* section below
-  Download the platform generation files using the link provided in the *Downloads* section below
-  Copy the platform generation files to the location where you cloned the HDL repository into the target project folder, *eg: \\hdl\\projects\\fmcomms2\\zc702*

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/targetting/sdsoc_platform_folder.png
   :align: center
   :width: 500px

-  Open Vivado and in the tcl console *cd* to the target project sdsoc folder, *eg. \\hdl\\projects\\fmcomms2\\zc702*
-  Update the HDL design to Vivado 2015.2 by running the *sdsoc_platform/update_hdl.tcl* script. This step needs to be ran only once after downloading the HDL reference design.
-  Regenerate the IP libraries following the steps described here: http://wiki.analog.com/resources/fpga/docs/hdl. This step needs to be ran only once after downloading the HDL reference design, or every time the IP libraries are modified.
-  Generate the SDSoC platform by running the *sdsoc_platform/sdsoc_platform.tcl* script. Before running the script you need to edit it and change line 26 "*set argv [list C:/Xilinx/SDSoC/2015.2/platforms]*" to point to your SDSoC platforms folder. At the end of the process the new platform will be placed in the SDSoC platforms folder and will be named *<board>\_<carrier>*, where *<board>* is the name of the FMCOMMSx board and *<carrier>* is the name of the Xilinx carrier, *eg. fmcomms2_zc702*

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/targetting/tcl_update_hdl.png
   :align: center
   :width: 500px

.. admonition:: Download
   :class: download

   
   -  :git-hdl:`Analog Devices HDL reference design <tree/hdl_2015_r1>`
   -  `FMCOMMS2 + ZC702 SDSoC platform generation files <https://wiki.analog.com/_media/resources/eval/user-guides/targetting/fmcomms2_zc702_sdsoc_platform.zip>`_
   -  `FMCOMMS2 + ZC706 SDSoC platform generation files <https://wiki.analog.com/_media/resources/eval/user-guides/targetting/fmcomms2_zc706_sdsoc_platform.zip>`_
   -  `FMCOMMS3 + ZC702 SDSoC platform generation files <https://wiki.analog.com/_media/resources/eval/user-guides/targetting/fmcomms3_zc702_sdsoc_platform.zip>`_
   -  `FMCOMMS3 + ZC706 SDSoC platform generation files <https://wiki.analog.com/_media/resources/eval/user-guides/targetting/fmcomms3_zc706_sdsoc_platform.zip>`_
   


FMCOMMS2 SDSoC Example
----------------------

The platform is accompanied by an example SDSoC project which implements a DDS block that will generate a CW that can be sent/received using the Analog Devices FMCOMMS2 board and the Xilinx ZC702 carrier board. The received signal can be displayed in the Analog Devices Linux IIO Oscillscope application. These are the steps to recreate the DDS project.

-  Download the SDSoC DDS project source code using the link in the *Downloads* section below
-  Start the SDSoC terminal and *cd* to the location where the project source code was extracted
-  In the SDSoC terminal type *make*. This will build the software, generate the DDS IP and insert it into the FMCOMMSx platform. It will also generate the Linux SD card image.
-  Create a SD card with the ADI Linux image as instructed here: :doc:`/wiki-migration/resources/tools-software/linux-software/zynq_images`
-  On the newly created SD card copy the *boot.bin* generated by SDSoC in the *sd_card* folder
-  Insert the SD card in the Xilinx ZC702 carrier board, connect antennas to the RF ports of the FMCOMMS2 or loopback cables between Rx and Tx, connect the FMCOMMS2 to the ZC702, connect the ZC702 to a HDMI monitor, connect a mouse and keyboard to the ZC702, connect an Ethernet cable to the ZC702, start the system
-  After Linux boots the IIO Oscilloscope starts automatically. In the IIO Oscilloscope configure the Rx and Tx LO frequencies to be the same, eg. 2.4GHz
-  In the IIO Oscilloscope configure the Transmit/DDS as shown below. Please make sure to select a file unde ‘DAC Buffer settings’, any file will do, and press the *Load* button. All the DAC Channels must be selected before pressing *Load*.
-  Using a program like WinSCP copy from the project folder the *dds_script.sh* to the device’s */usr/local/bin folder*. The credentials for the SCP connection between the PC and the device are: user – analog, password – analog. In order to configure the SCP connection you need the IP of the device, to get that just type *ifconfig* in a terminal on the device.
-  Run the *dds_script.sh* as shown below. This will initialize and activate the DDS IP.
-  On the IIO Oscilloscope select the *voltage0* and *voltage1* channels and press the *Play* button. You should see the DDS waveforms displayed by the IIO Oscilloscope .

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/targetting/dds_out.png
   :align: center
   :width: 400px

.. admonition:: Download
   :class: download

   
   -  `SDSoC DDS source code <https://wiki.analog.com/_media/resources/eval/user-guides/targetting/sdsoc_dds_src.zip>`_
   

