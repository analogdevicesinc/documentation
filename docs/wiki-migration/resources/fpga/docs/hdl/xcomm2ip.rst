A simple BBP for RF Transceivers
================================

This wiki page is a follow up documentation to the ADI article titled "A Simple Baseband Processor for RF Transceivers". The article covers the theory and implementation details of a simple BBP using the ZC706 + AD-FMCOMMS3 rapid prototyping platform. This page details the demonstration and build process of the BBP design on the ZC706 + AD-FMCOMMS3 hardware.

Please note that Analog Devices does NOT support this design. It is unlikely that we maintain this core or design as we would the reference design. The recommended procedure for a BBP design is to model it in Simulink and subsequently implement the design using HDL coder. The core of the axi_xcomm2ip is intentionally obfuscated to discourage any use or modification of the IP. However, the radio communication demonstration detailed here may be used as a frame work and implementation flow for such designs. It is also meant to illustrate a work flow using the ADI github repositories, especially the HDL. The build process serves as a use case example for a set of frequently asked questions about the use of the HDL repository and the project frame work.

This document and the design, at present, is applicable and built only for Xilinx tools and devices. An Altera equivalent is in the plans and may be added sometime in the near future. It is assumed that the reader is familiar with the ADI reference designs, Vivado, TCL scripts and Linux. Also note that the instructions exclusively use a Linux command line environment. Please do not seek support or ask questions outside the scope of this document.

This guide has two sections, the first section covers the hardware demonstration, what it is and how to run it. The second section covers the build process of the demo from the source files.

Setup and Running the demo
==========================

The demo is a simple chat (as in transmitting and receiving text messages) program between two ZC706 + AD-FMCOMMS3-EBZ platforms. You may place the two boards adjacent to each other within your lab desk space. Please do NOT try to use it with your significant other(s) across the seven seas. The best learning or experimentation setup requires two hardware platforms. This allows one to understand the importance and need for carrier tracking. It is possible for you to run the demo on a single platform in loopback mode. The default setup assumes two independent hardware platforms. So the single platform loopback mode requires some additional LO changes.

Download run-time files
=======================

.. admonition:: Download
   :class: download

   `RFBBP Run-Time Files (binary files, for running the demonstration on hardware) <https://wiki.analog.com/_media/resources/fpga/docs/hdl/runfiles.tar.gz>`_


Setup (host Linux desktop)
==========================

The setup assumes that you are familiar with the AD-FMCOMMS3-EBZ user guide and used it to capture some signals or at least done a sanity level testing. You also have the image with the boot and file system partitions in the SD card.

To begin with, download the RFBBP demo run-time files and extract the contents. ++++ Show/Hide Commands: \|

::

   [~]> mkdir rfbbp
   [~]> cd rfbbp

   [~/rfbbp]> gunzip runfiles.tar.gz
   [~/rfbbp]> tar -xvf runfiles.tar

++++

Now mount your SD card. You should see two mount points; BOOT and rootfs. The software routines run in user space and we need a directory to keep them. This way, you can blow it away when you don't need it. You may have to be a little mindful of the file permissions as the board user is "analog". A simple solution is to grant the permissions to everyone. ++++ Show/Hide Commands: \|

::

   [~/rfbbp]> cp uImage /media/rkutty/BOOT/
   [~/rfbbp]> cp BOOT.BIN /media/rkutty/BOOT/
   [~/rfbbp]> cp devicetree.dtb /media/rkutty/BOOT/

++++

Simply copy the the Linux user space files to the "xcomm2ip" folder in the home directory. ++++ Show/Hide Commands: \|

::

   [~/rfbbp]> mkdir -p /media/rkutty/rootfs/home/analog/xcomm2ip/
   [~/rfbbp]> cp xcomm2ip_m.c /media/rkutty/rootfs/home/analog/xcomm2ip/
   [~/rfbbp]> cp xcomm2ip.c /media/rkutty/rootfs/home/analog/xcomm2ip/
   [~/rfbbp]> cp xcomm2ip.sh /media/rkutty/rootfs/home/analog/xcomm2ip/
   [~/rfbbp]> cp xcomm2ip_1.ini /media/rkutty/rootfs/home/analog/xcomm2ip/
   [~/rfbbp]> cp xcomm2ip_2.ini /media/rkutty/rootfs/home/analog/xcomm2ip/
   [~/rfbbp]> chmod go+rwx /media/rkutty/rootfs/home/analog/xcomm2ip/*.*

++++

Now unmount the SD card 1, and mount SD card 2 and repeat the same process. After that, unmount SD card 2. If you haven't already done so, you need to prepare the two hardware platforms (let's designate them as SYSTEM-1 and SYSTEM-2 for easy reference) with the keyboard, mouse and display connections. Insert the SD cards into the SYSTEM-1 and SYSTEM-2 ZC706 boards and power them up. The rest of the setup is done in the hardware platforms. That is, the following instructions do NOT use your host machine.

Setup SYSTEM-1 (board Linux desktop)
====================================

In the desktop, open a terminal and login as root. If the OSC application is already open and running, close it. Then run the shell script with the "System ID" set to 1. The script compiles the two c files and then opens three terminals. In the first terminal it runs the osc application with a profile that sets the receive and transmit LO differenty. The second is a "view" terminal. This terminal echo the transmit text messages and display the received text messages. The third terminal is the "transmit-text-entry" terminal. You may enter the text messages in this terminal. A null entry (pressing enter without any text) exits the chat routines. This in any way meant to suggest or otherwise taken as a method of writing a software application. The inner workings of this is discussed in detail later in the build process section. ++++ Show/Hide Commands: \|

::

   [~/xcomm2ip]> ./xcomm2ip.sh
   System ID [1|2]> 1

++++

.. note::

   If you are running this demo in a single system with loopback, set the receive and transmit LO frequencies to be the same.


Setup SYSTEM-2 (board Linux desktop)
====================================

As you may have now guessed, the setup is same as SYSTEM-1 except that you set the ID to 2. This sets the receive LO frequency of SYSTEM-2 same as the transmit LO frequency of SYSTEM-1 and vice-versa. ++++ Show/Hide Commands: \|

::

   [~/xcomm2ip]> ./xcomm2ip.sh
   System ID [1|2]> 2

++++

.. note::

   Obviously, though we also mention it, in a single system with loopback, you skip this setup.


Using the chat application
==========================

Now you may enter text messages in the "transmit-text-entry" terminals of either SYSTEM-1 or SYSTEM-2 and the "view" terminal of the "other" system should display them. This all seem a round about way of "talking to yourself", but that is not really the idea here. As you may have now realized that you don't have much to communicate with your "other-self", exit the applications and shutdown the system gracefully. Then return to this document as it explains some behind-the-demo points which may be a bit more interesting than the demo itself.

Building the demo files from source
===================================

The main intent behind this design excercise is to illustrate as an example to some of the most frequently asked questions about the HDL repository and how to modify and use it. The following sections may be able to give you some ideas. These sections do a walk through of the build process to generate the demo files above from the source files. As we go through these sections, we cover the above mentioned frequently asked question and reveal (hopefully) our method to madness.

Download Source files
=====================

.. admonition:: Download
   :class: download

   `RFBBP Source Files (build and generate the demonstration files) <https://wiki.analog.com/_media/resources/fpga/docs/hdl/srcfiles.tar.gz>`_


Setup a workspace
=================

<fc #800000>*\* How to best use the ADI HDL repository? \**</fc>

The ADI reference design repositories are hosted on GitHub and uses git version control system. However you may use your own repository and/or a different version control system. In any case, try not to download the repository as a zip file. The best strategy is to clone the repository and leave it as it is. Occassionally, perhaps, fetching and rebasing it. The RFBBP build flow shows how to setup the ADI HDL repository and another repository side by side. The two repositories are independent to each other but sharing files and frame work. ++++ Show/Hide Commands: \|

::

   [~]> mkdir rfbbp
   [~]> cd rfbbp

   [~/rfbbp]> git clone git@github.com:analogdevicesinc/hdl.git
   [~/rfbbp]> cd hdl
   [~/rfbbp/hdl]> git checkout hdl_2016_r1
   [~/rfbbp/hdl]> git fetch
   [~/rfbbp/hdl]> git rebase origin/hdl_2016_r1
   [~/rfbbp/hdl]> cd ..

++++

The build setup assumes you have cloned the "hdl" and "linux" repositories with the respective branches checked out. The RFBBP files are separated into two additional independent repositories namely "ip" and "zc706". Note that the "linux" repository doesn't work the same way as the HDL and requires some special handling. We cover that later in this page. ++++ Show/Hide Commands: \|

::

   [~/rfbbp]> git clone git@github.com:analogdevicesinc/linux.git
   [~/rfbbp]> cd linux
   [~/rfbbp/linux]> git checkout 2016_R1
   [~/rfbbp/linux]> git fetch
   [~/rfbbp/linux]> git rebase origin/2016_R1
   [~/rfbbp/linux]> cd ..

++++

Creating the IP library
=======================

<fc #800000>\ **How do I create my own Vivado IP library and IP core?**\ </fc>

The RFBBP is developed as an IP core that is part of a different library separate from the ADI library. A Vivado library is just a directory that needs to contain some specific files. In our case, we create a library (named "ip") and the RFBBP core (named "axi_xcomm2ip") inside our workspace. The generic set of files an IP needs are the Makefile, HDL files, constraints (if any) along with a TCL file to build the IP. The structure of our source files is presented below , that is - this is how you see the downloaded source files. You do NOT run these commands but simply extract the source files from the archive. The files simply falls into the directory structure referenced here. ++++ Show/Hide Commands: \|

::

   [~/rfbbp]> mkdir -p ip/axi_xcomm2ip
   [~/rfbbp]> touch ip/axi_xcomm2ip/Makefile
   [~/rfbbp]> touch ip/axi_xcomm2ip/axi_xcomm2ip.v
   [~/rfbbp]> touch ip/axi_xcomm2ip/axi_xcomm2ip_constr.xdc
   [~/rfbbp]> touch ip/axi_xcomm2ip/axi_xcomm2ip_ip.tcl

++++

This library can later be added to the Vivado library search paths to include all the IP cores within as follows. This is detailed in the project script flow sections below. ++++ Show/Hide Commands: \|

::

   set_property ip_repo_paths ip [current_fileset]

++++

<fc #800000>\ **Why write a TCL file to create a custom IP core?**\ </fc>

The TCL file is optional. You may create the IP and save the generated files. However, we like the TCL flow because it makes the tool conform to our needs. We do not wish to discuss the reasons (too many), but consider this- so far we were unable to generate the Vivado library files across various versions using the same tool commands. If you plan to stay with a single version of the tools you may not see these benefits. So the choice is up to you, but we encourage you to use the TCL flow. We have created some wrapper procedures around the tool commands. As Xilinx changes its commands and functionality over each version of the tool, we change them within these procedures so that bulk of our library remains unaltered. ++++ Show/Hide Commands: \|

::

   set ad_hdl_dir $::env(ADI_HDL_DIR)
   set ad_phdl_dir $::env(ADI_HDL_DIR)

   source $ad_hdl_dir/library/scripts/adi_ip.tcl

   adi_ip_create axi_xcomm2ip
   adi_ip_files axi_xcomm2ip [list \
     "$ad_hdl_dir/library/common/ad_rst.v" \
     "$ad_hdl_dir/library/common/ad_mem.v" \
     "$ad_hdl_dir/library/common/up_axi.v" \
     "axi_xcomm2ip_core.v" \
     "axi_xcomm2ip.v" ]

   adi_ip_properties axi_xcomm2ip
   adi_ip_constraints axi_xcomm2ip [list \
     "axi_xcomm2ip_constr.xdc" ]

   ipx::save_core [ipx::current_core]

++++

Note the use of the environment variable "AD_HDL_DIR" in the TCL file. This variable is used to point to the ADI HDL repository and use the files and scripts inside of it. This way, your IP may reside anywhere in your file system independent of the ADI HDL repository.

<fc #800000>\ **Why write a Make file to create a custom IP core?**\ </fc>

As with the TCL file, the Makefile is also a choice (watched the Matrix too many times). If you choose to follow our frame work, simply list your dependencies and targets. Again note the export of the environment variable. This variable is set based on the workspace setup we discussed above. ++++ Show/Hide Commands: \|

::

   export ADI_HDL_DIR := ../../../hdl
   export ADI_PHDL_DIR := ../../../hdl

   M_DEPS += $(ADI_HDL_DIR)/library/scripts/adi_env.tcl
   M_DEPS += $(ADI_HDL_DIR)/library/scripts/adi_ip.tcl
   M_DEPS += $(ADI_HDL_DIR)/library/common/ad_mem.v
   M_DEPS += $(ADI_HDL_DIR)/library/common/ad_rst.v
   M_DEPS += $(ADI_HDL_DIR)/library/common/up_axi.v
   M_DEPS += axi_xcomm2ip_constr.xdc
   M_DEPS += axi_xcomm2ip_ip.tcl
   M_DEPS += axi_xcomm2ip.v

   M_VIVADO := vivado -mode batch -source

   M_FLIST := *.cache
   M_FLIST += *.data
   M_FLIST += *.xpr
   M_FLIST += *.log
   M_FLIST += component.xml
   M_FLIST += *.jou
   M_FLIST +=  xgui
   M_FLIST += .Xil

   .PHONY: all clean clean-all
   all: axi_xcomm2ip.xpr


   clean:clean-all


   clean-all:
       rm -rf $(M_FLIST)


   axi_xcomm2ip.xpr: $(M_DEPS)
       rm -rf $(M_FLIST)
       $(M_VIVADO) axi_xcomm2ip_ip.tcl  >> axi_xcomm2ip_ip.log 2>&1

++++

<fc #800000>\ **How do I build the IP cores and library?**\ </fc>

In order for our directory "ip" to be a library, it must alteast have one "ip-core" inside it. The "ip-core" is identified by the tool with the existence of the generated files from the TCL script. Also note that you don't need to generate this separately, the project make does check the existence of all the "ip-cores" it needs and builds them accordingly. ++++ Show/Hide Commands: \|

::

   [~/rfbbp]> cd ip/axi_xcomm2ip
   [~/rfbbp/ip/axi_xcomm2ip]> make
   [~/rfbbp/ip/axi_xcomm2ip]> cd ../..
   [~/rfbbp]>

++++

Creating the IP core
====================

<fc #800000>\ **How do I create a custom AXI IP core using ADI frame work?**\ </fc>

As mentioned in the article, the RFBBP IP is an AXI core, making it a peripheral that interfaces to the processor so that it can be accessed via software. In order to create an AXI IP core, one could make use of the ADI library common modules. All you need in such a case would be to instantiate the "up_axi" module. This module interfaces to the processor's AXI master bus (via an interconnect in most cases) and translates AXI bus transactions to simple memory like interface internally. The BBP IP core illustrates how to use this interface to implement the register and memory address space for the processor access. The "up_axi" module uses dword addressing, instead of the AXI byte addressing. The following code in the RFBBP core infers the "up_axi" module, there by in-effect creating it as an AXI IP core. ++++ Show/Hide Commands: \|

::

     wire            up_clk;
     wire            up_rstn;
     wire            up_wreq_s;
     wire    [13:0]  up_waddr_s;
     wire    [31:0]  up_wdata_s;
     wire            up_wack_s;
     wire            up_rreq_s;
     wire    [13:0]  up_raddr_s;
     wire    [31:0]  up_rdata_s;
     wire            up_rack_s;

     assign up_clk = s_axi_aclk;
     assign up_rstn = s_axi_aresetn;

     up_axi i_up_axi (
       .up_rstn (up_rstn),
       .up_clk (up_clk),
       .up_axi_awvalid (s_axi_awvalid),
       .up_axi_awaddr (s_axi_awaddr),
       .up_axi_awready (s_axi_awready),
       .up_axi_wvalid (s_axi_wvalid),
       .up_axi_wdata (s_axi_wdata),
       .up_axi_wstrb (s_axi_wstrb),
       .up_axi_wready (s_axi_wready),
       .up_axi_bvalid (s_axi_bvalid),
       .up_axi_bresp (s_axi_bresp),
       .up_axi_bready (s_axi_bready),
       .up_axi_arvalid (s_axi_arvalid),
       .up_axi_araddr (s_axi_araddr),
       .up_axi_arready (s_axi_arready),
       .up_axi_rvalid (s_axi_rvalid),
       .up_axi_rresp (s_axi_rresp),
       .up_axi_rdata (s_axi_rdata),
       .up_axi_rready (s_axi_rready),
       .up_wreq (up_wreq_s),
       .up_waddr (up_waddr_s),
       .up_wdata (up_wdata_s),
       .up_wack (up_wack_s),
       .up_rreq (up_rreq_s),
       .up_raddr (up_raddr_s),
       .up_rdata (up_rdata_s),
       .up_rack (up_rack_s));

++++

<fc #800000>\ **How do I infer register and memory space using the "up_axi" module?**\ </fc>

<fc #800000>\ **How do I create a custom AXI IP core to be able to use inside an ADI project?**\ </fc>

The BBP is implemented as an "insert-able" core in the ADI design. If you are pondering to do something similar in other designs, you could follow the same procedure. However, in terms of placement, this requires a better understanding of the design and the various data path components. If your custom IP core can meet the throughput, placing it next to the interface core is a logical choice. If you need it to be an offline core, place it along with a DMA engine off the DDR memory. This allows you to collect data in the DDR and pass it to your custom core at its own pace.

Once the placement has been fixed, match the "inserting-point" interfaces of the data path. The custom IP core interfaces are simply mirrored from its adjoining cores. As you may have already guessed, the RFBBP is intended to interface with the "axi_ad9361" core. It is placed right in front of the "axi_ad9361" IP core. It is also intended to run at the AD9361 interface clock. So we use the same clock and reset signals as that of the AXI_AD9361 IP. ++++ Show/Hide Commands: \|

::

     input           clk,
     input           rst,

++++

In the receive direction it needs to interface to the ADC data ports of the AXI_AD9361 core. This makes it essentially an offline data processing core. So we mirror the "axi_ad9361" core's adc data interface. ++++ Show/Hide Commands: \|

::

     input           adc_valid_i0,
     input   [15:0]  adc_data_i0,
     input           adc_valid_q0,
     input   [15:0]  adc_data_q0,
     input           adc_valid_i1,
     input   [15:0]  adc_data_i1,
     input           adc_valid_q1,
     input   [15:0]  adc_data_q1,

++++

Similarly, in the transmit direction it needs to interface to the DAC data ports of the AXI_AD9361 core. However, this breaks the default data path of the ADI design in which the DAC data is sourced from the DMA core. So the BBP IP core needs the DMA signals in order to maintain the default data path unless programmed by the software otherwise. ++++ Show/Hide Commands: \|

::

     input           dac_valid_i0,
     input   [15:0]  dma_data_i0,
     output  [15:0]  dac_data_i0,
     input           dac_valid_q0,
     input   [15:0]  dma_data_q0,
     output  [15:0]  dac_data_q0,
     input           dac_valid_i1,
     input   [15:0]  dma_data_i1,
     output  [15:0]  dac_data_i1,
     input           dac_valid_q1,
     input   [15:0]  dma_data_q1,
     output  [15:0]  dac_data_q1,
     input           dma_dovf,
     input           dma_dunf,
     output          dac_dovf,
     output          dac_dunf,

++++

The data path can then be altered by infering a simple multiplexer. ++++ Show/Hide Commands: \|

::

     assign dac_data_i0 = dac_data_i0_int;
     assign dac_data_q0 = dac_data_q0_int;
     assign dac_data_i1 = dac_data_i1_int;
     assign dac_data_q1 = dac_data_q1_int;
     assign dac_dovf = dac_dovf_int;
     assign dac_dunf = dac_dunf_int;

     always @(posedge rst or posedge clk) begin
       if (rst == 1'b1) begin
         dac_enable_m1 <= 1'd0;
         dac_enable <= 1'd0;
         dac_data_i0_int <= 'd0;
         dac_data_q0_int <= 'd0;
         dac_data_i1_int <= 'd0;
         dac_data_q1_int <= 'd0;
         dac_dovf_int <= 'd0;
         dac_dunf_int <= 'd0;
       end else begin
         dac_enable_m1 <= up_dac_enable;
         dac_enable <= dac_enable_m1;
         if (dac_enable == 1'b1) begin
           dac_data_i0_int <= dac_data_i;
           dac_data_q0_int <= dac_data_q;
           dac_data_i1_int <= 16'd0;
           dac_data_q1_int <= 16'd0;
           dac_dovf_int <= 1'd0;
           dac_dunf_int <= 1'd0;
         end else begin
           dac_data_i0_int <= dma_data_i0;
           dac_data_q0_int <= dma_data_q0;
           dac_data_i1_int <= dma_data_i1;
           dac_data_q1_int <= dma_data_q1;
           dac_dovf_int <= dma_dovf;
           dac_dunf_int <= dma_dunf;
         end
       end
     end

++++

<fc #800000>\ **How do I send my own data to the ADI IP core?**\ </fc>

This is NOT something we can answer. It is also a question of "what" than "how". The "how" part is that you either generate the data in hardware or in software. As for the "what", note that the most of the interface cores are meant to for analog data. That is, though it is a digital interface, the data must be and considered to be analog. An often asked question is why the data one sent to the DAC does not match the data received at the ADC. This is a mis-conception, the digital data to the DAC is must be and in fact a "digitized" analog signal. The "data" in its commonly used sense, must be encoded and modulated before passing it to the analog domain.

As for our RFBBP core, it is suffice to say that the rest of the logic generate its own transmit data for the DAC and process the received data from the ADC as it seems fit. This part, though critical to understanding the workings of a radio design, is beyond the scope of this document and is intentionally left out of our discussion.

Modifying and customizing ADI projects
======================================

<fc #800000>\ **How do I insert a custom AXI IP core inside an ADI project?**\ </fc>

As mentioned above, the RFBBP AXI core is designed for the "fmcomms2" projects and is to be placed next to the "axi_ad9361" core. In order to do this, we need to modify the "fmcomms2" project. This can be easily done using the ADI TCL frame work. We create this as a new project inheritting the "fmcomms2" board design and doing the necessary customizations. In the RFBBP design, this is all done using a single TCL file. ++++ Show/Hide Commands: \|

::

   [~/rfbbp]> mkdir zc706
   [~/rfbbp]> cd zc706
   [~/rfbbp/zc706]> touch zc706.tcl
   [~/rfbbp/zc706]> touch Makefile

++++

Lets look at the "zc706.tcl" file contents. In order to use the ADI frame work we need to source the TCL procedures. ++++ Show/Hide Commands: \|

::

   set ad_hdl_dir $::env(ADI_HDL_DIR)
   set ad_phdl_dir $::env(ADI_HDL_DIR)

   source $ad_hdl_dir/projects/scripts/adi_board.tcl
   source $ad_hdl_dir/projects/scripts/adi_project.tcl

++++

Then we set the "zynq" flag and create the new project. Set the board part for the predefined settings. ++++ Show/Hide Commands: \|

::

   set sys_zynq 1

   create_project zc706 . -part xc7z045ffg900-2 -force

   set_property board_part xilinx.com:zc706:part0:1.2 [current_project]

++++

Now, pay special attention, we set the ip repository folders. The default ADI library and the "ip" library we created above for the "axi_xcomm2ip" core. ++++ Show/Hide Commands: \|

::

   set_property ip_repo_paths [list $ad_hdl_dir/library ../ip]  [current_fileset]

   update_ip_catalog

++++

Once the libraries are read, we can inherit the "fmcomms2" board design and customize it. The board design is inherited by simply sourcing the carrier (zc706) and the fmc (fmcomms2) board. ++++ Show/Hide Commands: \|

::

   create_bd_design "system"
   source $ad_hdl_dir/projects/common/zc706/zc706_system_bd.tcl
   source $ad_hdl_dir/projects/fmcomms2/common/fmcomms2_bd.tcl

++++

The customization, inserting the "axi_xcomm2ip", requires us to remove the existing connection at the "axi_ad9361" DAC interface. This can be done by removing the nets connected to the "axi_ad9361" DAC interface ports using the "delete_bd_objs" command. ++++ Show/Hide Commands: \|

::

   delete_bd_objs [get_bd_nets -of_objects [find_bd_objs -relation connected_to [get_bd_pins axi_ad9361/dac_valid_i0]]]
   delete_bd_objs [get_bd_nets -of_objects [find_bd_objs -relation connected_to [get_bd_pins axi_ad9361/dac_data_i0]]]
   delete_bd_objs [get_bd_nets -of_objects [find_bd_objs -relation connected_to [get_bd_pins axi_ad9361/dac_valid_q0]]]
   delete_bd_objs [get_bd_nets -of_objects [find_bd_objs -relation connected_to [get_bd_pins axi_ad9361/dac_data_q0]]]
   delete_bd_objs [get_bd_nets -of_objects [find_bd_objs -relation connected_to [get_bd_pins axi_ad9361/dac_valid_i1]]]
   delete_bd_objs [get_bd_nets -of_objects [find_bd_objs -relation connected_to [get_bd_pins axi_ad9361/dac_data_i1]]]
   delete_bd_objs [get_bd_nets -of_objects [find_bd_objs -relation connected_to [get_bd_pins axi_ad9361/dac_valid_q1]]]
   delete_bd_objs [get_bd_nets -of_objects [find_bd_objs -relation connected_to [get_bd_pins axi_ad9361/dac_data_q1]]]
   delete_bd_objs [get_bd_nets -of_objects [find_bd_objs -relation connected_to [get_bd_pins axi_ad9361/dac_dunf]]]

++++

Add the "axi_xcomm2ip" core. ++++ Show/Hide Commands: \|

::

   set axi_xcomm2ip [create_bd_cell -type ip -vlnv analog.com:user:axi_xcomm2ip:1.0 axi_xcomm2ip]
   set_property -dict [list CONFIG.XCOMM2IP_1T1R_OR_2T2R_N {0}] $axi_xcomm2ip

++++

Connect its slave AXI interface to the "ps7" with an address map of 0x79040000. ++++ Show/Hide Commands: \|

::

   ad_cpu_interconnect 0x79040000 axi_xcomm2ip

++++

And the data path connections; clock, reset, ADC and DAC interfaces. ++++ Show/Hide Commands: \|

::

   ad_connect  axi_ad9361/clk axi_xcomm2ip/clk
   ad_connect  axi_ad9361/rst axi_xcomm2ip/rst
   ad_connect  axi_ad9361/adc_valid_i0 axi_xcomm2ip/adc_valid_i0
   ad_connect  axi_ad9361/adc_data_i0 axi_xcomm2ip/adc_data_i0
   ad_connect  axi_ad9361/adc_valid_q0 axi_xcomm2ip/adc_valid_q0
   ad_connect  axi_ad9361/adc_data_q0 axi_xcomm2ip/adc_data_q0
   ad_connect  axi_ad9361/adc_valid_i1 axi_xcomm2ip/adc_valid_i1
   ad_connect  axi_ad9361/adc_data_i1 axi_xcomm2ip/adc_data_i1
   ad_connect  axi_ad9361/adc_valid_q1 axi_xcomm2ip/adc_valid_q1
   ad_connect  axi_ad9361/adc_data_q1 axi_xcomm2ip/adc_data_q1
   ad_connect  axi_xcomm2ip/dac_valid_i0 axi_ad9361/dac_valid_i0
   ad_connect  axi_xcomm2ip/dac_data_i0 axi_ad9361/dac_data_i0
   ad_connect  axi_xcomm2ip/dac_valid_q0 axi_ad9361/dac_valid_q0
   ad_connect  axi_xcomm2ip/dac_data_q0 axi_ad9361/dac_data_q0
   ad_connect  axi_xcomm2ip/dac_valid_i1 axi_ad9361/dac_valid_i1
   ad_connect  axi_xcomm2ip/dac_data_i1 axi_ad9361/dac_data_i1
   ad_connect  axi_xcomm2ip/dac_valid_q1 axi_ad9361/dac_valid_q1
   ad_connect  axi_xcomm2ip/dac_data_q1 axi_ad9361/dac_data_q1
   ad_connect  axi_xcomm2ip/dac_dovf axi_ad9361/dac_dovf
   ad_connect  axi_xcomm2ip/dac_dunf axi_ad9361/dac_dunf

   ad_connect  util_ad9361_dac_upack/dac_data_0 axi_xcomm2ip/dma_data_i0
   ad_connect  util_ad9361_dac_upack/dac_data_1 axi_xcomm2ip/dma_data_q0
   ad_connect  util_ad9361_dac_upack/dac_data_2 axi_xcomm2ip/dma_data_i1
   ad_connect  util_ad9361_dac_upack/dac_data_3 axi_xcomm2ip/dma_data_q1
   ad_connect  axi_ad9361_dac_dma/fifo_rd_underflow axi_xcomm2ip/dma_dunf
   ad_connect  axi_xcomm2ip/dma_dovf GND

++++

Some clean-up, saving and validating. ++++ Show/Hide Commands: \|

::

   delete_bd_objs [get_bd_cells ila_adc]
   delete_bd_objs [get_bd_nets axi_ad9361_tdd_dbg] [get_bd_cells ila_tdd]

   regenerate_bd_layout
   save_bd_design
   validate_bd_design

++++

Generate all the targets, create the top level wrapper and add the reset of the files. ++++ Show/Hide Commands: \|

::

   generate_target {synthesis implementation} [get_files zc706.srcs/sources_1/bd/system/system.bd]
   make_wrapper -files [get_files zc706.srcs/sources_1/bd/system/system.bd] -top
   import_files -force -norecurse -fileset sources_1 zc706.srcs/sources_1/bd/system/hdl/system_wrapper.v

   adi_project_files zc706 [list \
     "$ad_hdl_dir/library/common/ad_iobuf.v" \
     "$ad_hdl_dir/projects/fmcomms2/zc706/system_top.v" \
     "$ad_hdl_dir/projects/fmcomms2/zc706/system_constr.xdc"\
     "$ad_hdl_dir/projects/common/zc706/zc706_system_constr.xdc" ]

++++

Now build the project. ++++ Show/Hide Commands: \|

::

   adi_project_run zc706

++++

Building Linux
==============

Making the HDL IP core accessable to Linux
==========================================

What do I need to do to access a HDL IP core from Linux?
--------------------------------------------------------

Accessing the HDL IP core in Linux
==================================

How do I access a HDL IP core from Linux?
-----------------------------------------
