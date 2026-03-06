DE10-Nano Development Kit Quick Start Guide
===========================================

Generate the Raw Binary File for configuring the FPGA
-----------------------------------------------------

::

   analog@debian:~$ **cd hdl/projects/de10**
   analog@debian:~/hdl/projects/de10$ **make**
   rm -rf *.log *_INFO.txt *_dump.txt db *.asm.rpt *.done *.eda.rpt *.fit.* *.map.* *.sta.* *.qsf *.qpf *.qws *.sof *.cdf *.sld *.qdf hc_output system_bd hps_isw_handoff hps_sdram_*.csv *ddr3_*.csv incremental_db reconfig_mif *.sopcinfo *.jdi *.pin *_summary.csv *.dpf
   quartus_sh --64bit -t  system_project.tcl  >> de10nano_quartus.log 2>&1
   analog@debian:~/hdl/projects/de10$ **quartus_cpf -c -o bitstream_compression=on ./de10nano.sof soc_system.rbf**
   Info: Running Quartus Prime Convert_programming_file
       Info: Version 17.1.1 Internal Build 593 12/11/2017 SJ Standard Edition
       Info: Copyright (C) 2017  Intel Corporation. All rights reserved.
       Info: Your use of Intel Corporation's design tools, logic functions 
       Info: and other software and tools, and its AMPP partner logic 
       Info: functions, and any output files from any of the foregoing 
       Info: (including device programming or simulation files), and any 
       Info: associated documentation or information are expressly subject 
       Info: to the terms and conditions of the Intel Program License 
       Info: Subscription Agreement, the Intel Quartus Prime License Agreement,
       Info: the Intel FPGA IP License Agreement, or other applicable license
       Info: agreement, including, without limitation, that your use is for
       Info: the sole purpose of programming logic devices manufactured by
       Info: Intel and sold by Intel or its authorized distributors.  Please
       Info: refer to the applicable agreement for further details.
       Info: Processing started: Wed Mar 14 23:04:31 2018
   Info: Command: quartus_cpf -c -o bitstream_compression=on ./de10nano.sof soc_system.rbf
   Info: Quartus Prime Convert_programming_file was successful. 0 errors, 0 warnings
       Info: Peak virtual memory: 458 megabytes
       Info: Processing ended: Wed Mar 14 23:04:40 2018
       Info: Elapsed time: 00:00:09
       Info: Total CPU time (on all processors): 00:00:02

Generate the Preloader
----------------------

::

   Intel FPGA Embedded Command Shell

   Version 17.1 [Build 590]
   ------------------------------------------------
   analog@debian:~/hdl/projects/de10$ **bsp-create-settings --type spl --bsp-dir sw/bsp/ --preloader-settings-dir hps_isw_handoff/system_bd_sys_hps/ --settings sw/bsp/settings.bsp --set spl.boot.WATCHDOG_ENABLE false**
   ...
   INFO: Finished generating BSP files. Total time taken = 2 seconds
   INFO: BSP files generated in "/home/analog/hdl/projects/de10/sw/bsp"
   analog@debian:~/hdl/projects/de10$ **make -C sw/bsp/**
   ...
   mkpimage --header-version 0 -o preloader-mkpimage.bin uboot-socfpga/spl/u-boot-spl.bin uboot-socfpga/spl/u-boot-spl.bin uboot-socfpga/spl/u-boot-spl.bin uboot-socfpga/spl/u-boot-spl.bin
   make: Leaving directory '/home/analog/hdl/projects/de10/sw/bsp'
   analog@debian:~/hdl/projects/de10$ **make -C sw/bsp/ uboot**
   ...
   make[1]: Leaving directory '/home/analog/hdl/projects/de10/sw/bsp/uboot-socfpga'
   make: Leaving directory '/home/analog/hdl/projects/de10/sw/bsp'
   analog@debian:~/hdl/projects/de10$ **cat sw/bsp/preloader-mkpimage.bin sw/bsp/uboot-socfpga/u-boot.img > sw/preloader_bootloader.img**

Write the Preloader
-------------------

::

   analog@debian:~$ sudo dd of=/dev/mmcblk0p3 bs=512 if=sw/preloader_bootloader.img

Build and Copy Linux Kernel and DeviceTree
------------------------------------------

::

   analog@debian:~$ cd linux
   analog@debian:~$ export ARCH=arm
   analog@debian:~$ export CROSS_COMPILE=/path/to/arm/linux/gnueabi/cross-compiler
   analog@debian:~$ make socfpga_adi_defconfig
   analog@debian:~$ make zImage
   analog@debian:~$ cp arch/arm/boot/zImage /media/analog/BOOT/
   analog@debian:~$ make socfpga_cyclone5_de10_nano.dtb
   analog@debian:~$ cp arch/arm/boot/dts/socfpga_cyclone5_de10_nano.dtb /media/analog/BOOT/socfpga.dtb
