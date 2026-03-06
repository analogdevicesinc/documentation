CN0540 software
===============

First, prepare a workspace

::

   sergiu@analog:~$ mkdir cn0540
   sergiu@analog:~$ cd cn0540

Build the HDL project
---------------------

Clone the HDL repository

::

   sergiu@analog:~/cn0540$ git clone https://github.com/analogdevicesinc/hdl.git    
    Cloning into 'hdl'...
    remote: Enumerating objects: 518, done.
    remote: Counting objects: 100% (518/518), done.
    remote: Compressing objects: 100% (285/285), done.
    remote: Total 60517 (delta 305), reused 379 (delta 232), pack-reused 59999
    Receiving objects: 100% (60517/60517), 16.74 MiB | 2.36 MiB/s, done.
    Resolving deltas: 100% (43413/43413), done.

Go to the CN0540 project directory

::

   sergiu@analog:~/cn0540$ cd hdl/projects/cn0540/



.. raw:: html

   <details><summary>Xilinx</summary>

.. important::

   Source Xilinx's settings script in order to access build specific tools easier. This script can be found at [Xilinx install path]/Vivado/[Xilinx tool version]/settings64.sh:


::

   sergiu@analog:~/cn0540/hdl/projects/cn0540$ source /opt/Xilinx/Vivado/2019.1/settings64.sh

Start building the HDL

::

   sergiu@analog:~/cn0540/hdl/projects/cn0540$ make -C coraz7s
    Building util_cdc library [/home/sergiu/cn0540/hdl/library/util_cdc/util_cdc_ip.log] ... OK
    ...
    Building cn0540_coraz7s project [/home/sergiu/cn0540/hdl/projects/cn0540/coraz7s/cn0540_coraz7s_vivado.log] ... OK

Copy the synthesized HDL project in the root directory

::

   sergiu@analog:~/cn0540/hdl/projects/cn0540/$ cp ./coraz7s/cn0540_coraz7s.sdk/system_top.hdf ../../../

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Intel</summary>

.. important::

   Source Intel's settings script in order to access build specific tools easier. This script can be found at [Intel install path]/intelFPGA/[Tool version]/embedded/embedded_command_shell.sh


::

   sergiu@analog:~/cn0540/hdl/projects/cn0540$ source /opt/intelFPGA/18.1/embedded/embedded_command_shell.sh

Start building the HDL

::

   sergiu@analog:~/cn0540/hdl/projects/cn0540$ cd de10nano
   sergiu@analog:~/cn0540/hdl/projects/cn0540/de10nano$ make

After the build finished, compress the bitstream

::

   sergiu@analog:~/cn0540/hdl/projects/cn0540/de10nano$ quartus_cpf -c -o bitstream_compression=on cn0540_de10nano.sof soc_system.rbf
   sergiu@analog:~/cn0540/hdl/projects/cn0540/de10nano$ cp soc_system.rbf ../../../../

.. raw:: html

   </details>


Build the bootloader image
--------------------------



.. raw:: html

   <details><summary>Xilinx</summary>

Clone the uboot repository

::

   sergiu@analog:~/cn0540$ git clone https://github.com/analogdevicesinc/u-boot-xlnx.git
    Cloning into 'u-boot-xlnx'...
    remote: Enumerating objects: 537555, done.
    remote: Total 537555 (delta 0), reused 0 (delta 0), pack-reused 537555
    Receiving objects: 100% (537555/537555), 133.65 MiB | 5.56 MiB/s, done.
    Resolving deltas: 100% (435019/435019), done.

Go to the directory where the uboot repo was cloned

::

   sergiu@analog:~/cn0540$ cd u-boot-xlnx

Use the config for the Cora Z7

::

   sergiu@analog:~/cn0540/u-boot-xlnx$ make zynq_coraz7_defconfig

Build the uboot

::

   sergiu@analog:~/cn0540/u-boot-xlnx$ make

Copy the binary to the root folder

::

   sergiu@analog:~/cn0540/u-boot-xlnx$ cp u-boot ../u-boot.elf

.. important::

   Source Xilinx's settings script in order to access build specific tools easier. This script can be found at [Xilinx install path]/SDK/[Xilinx tool version]/settings64.sh


::

   sergiu@analog:~/cn0540$ source /opt/Xilinx/SDK/2019.1/settings64.sh

Create the first stage bootloader and copy the binaries in the root folder

::

   sergiu@analog:~/cn0540$  echo "setws ." >> fsbl.tcl && \
    echo "sdk createhw -name hw -hwspec system_top.hdf" >> fsbl.tcl && \
    echo "sdk createapp -name fsbl -app {Zynq FSBL} -hwproject hw -proc ps7_cortexa9_0 -os standalone -lang C" >> fsbl.tcl && \
    echo "configapp -app fsbl build-config release" >> fsbl.tcl && \
    echo "sdk projects -build -type all" >> fsbl.tcl && \
    echo "exit" >> fsbl.tcl
   sergiu@analog:~/cn0540$ xsdk -batch -source fsbl.tcl 
   sergiu@analog:~/cn0540$ cp fsbl/Release/fsbl.elf .
   sergiu@analog:~/cn0540$ cp hw/system_top.bit .

Create a boot information file so the bootgen utility can arrange the binaries.

::

   sergiu@analog:~/cn0540$ echo "the_ROM_image:" >> boot.bif && \
    echo "{" >> boot.bif && \
    echo " [bootloader] fsbl.elf" >> boot.bif && \
    echo " system_top.bit" >> boot.bif && \
    echo " u-boot.elf" >> boot.bif && \
    echo "}" >> boot.bif

Build the BOOT image

::

   sergiu@analog:~/cn0540$ bootgen -arch zynq -image boot.bif -o BOOT.bin -w

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Intel</summary>

::

   sergiu@analog:~/cn0540/hdl/projects/cn0540/de10nano$ bsp-create-settings --type spl --bsp-dir sw/bsp/ --preloader-settings-dir hps_isw_handoff/system_bd_sys_hps/ --settings sw/bsp/settings.bsp --set spl.boot.WATCHDOG_ENABLE false
   sergiu@analog:~/cn0540/hdl/projects/cn0540/de10nano$ make -C sw/bsp/
   sergiu@analog:~/cn0540/hdl/projects/cn0540/de10nano$ make -C sw/bsp/ uboot
   sergiu@analog:~/cn0540/hdl/projects/cn0540/de10nano$ cat sw/bsp/preloader-mkpimage.bin sw/bsp/uboot-socfpga/u-boot.img > sw/preloader_bootloader.img
   sergiu@analog:~/cn0540/hdl/projects/cn0540/de10nano$ cp sw/preloader_bootloader.img ../../../../

.. raw:: html

   </details>


Build the kernel and devicetree
-------------------------------

Clone the linux repository

::

   sergiu@analog:~/cn0540$ git clone https://github.com/analogdevicesinc/linux.git        
    Cloning into 'linux'...
    remote: Enumerating objects: 146, done.
    remote: Counting objects: 100% (146/146), done.
    remote: Compressing objects: 100% (111/111), done.
    remote: Total 8081800 (delta 84), reused 63 (delta 35), pack-reused 8081654
    Receiving objects: 100% (8081800/8081800), 2.20 GiB | 9.21 MiB/s, done.
    Resolving deltas: 100% (6784073/6784073), done.
    Updating files: 100% (62933/62933), done.

Go to the directory where the linux repo was cloned

::

   sergiu@analog:~/cn0540$ cd linux 

Now set some environment variables required by the Makefile

::

   sergiu@analog:~/cn0540/linux$ export ARCH=arm
   sergiu@analog:~/cn0540/linux$ export CROSS_COMPILE=arm-linux-gnueabihf-



.. raw:: html

   <details><summary>Xilinx</summary>

Use the default Zynq kernel configuration

::

   sergiu@analog:~/cn0540/linux$ make zynq_xcomm_adv7511_defconfig

Start building the kernel

::

   sergiu@analog:~/cn0540/linux$ make uImage

   ...

     LD      arch/arm/boot/compressed/vmlinux
     OBJCOPY arch/arm/boot/zImage
     Kernel: arch/arm/boot/zImage is ready
     UIMAGE  arch/arm/boot/uImage
   Image Name:   Linux-4.19.0-gc2beb57d774b
   Created:      Wed Sep  2 22:37:31 2020
   Image Type:   ARM Linux Kernel Image (uncompressed)
   Data Size:    5935616 Bytes = 5796.50 KiB = 5.66 MiB
   Load Address: 00008000
   Entry Point:  00008000
     Kernel: arch/arm/boot/uImage is ready

Copy the uImage to the root folder

::

   sergiu@analog:~/cn0540/linux$ cp arch/arm/boot/uImage ../

The name of the board is CN0540 and the carrier is the CoraZ7 so the following devicetree is needed : *zynq-coraz7s-cn0540.dtb*

::

   sergiu@analog:~/cn0540/linux$ make zynq-coraz7s-cn0540.dtb
     DTC     arch/arm/boot/dts/zynq-coraz7s-cn0540.dtb

Copy the devicetree to the root folder and rename it so the bootloader can find it

::

   sergiu@analog:~/cn0540/linux$ cp arch/arm/boot/dts/zynq-coraz7s-cn0540.dtb ../devicetree.dtb

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Intel</summary>

Use the default Socfpga kernel configuration

::

   sergiu@analog:~/cn0540/linux$ make socfpga_adi_defconfig

Start building the kernel

::

   sergiu@analog:~/cn0540/linux$ make zImage

   ...

     LD      arch/arm/boot/compressed/vmlinux
     OBJCOPY arch/arm/boot/zImage
     Kernel: arch/arm/boot/zImage is ready
     UIMAGE  arch/arm/boot/uImage
   Image Name:   Linux-4.19.0-gc2beb57d774b
   Created:      Wed Sep  2 22:37:31 2020
   Image Type:   ARM Linux Kernel Image (uncompressed)
   Data Size:    5935616 Bytes = 5796.50 KiB = 5.66 MiB
   Load Address: 00008000
   Entry Point:  00008000
     Kernel: arch/arm/boot/zImage is ready

Copy the zImage to the root folder

::

   sergiu@analog:~/cn0540/linux$ cp arch/arm/boot/zImage ../

The name of the board is CN0540 and the carrier is the DE10-nano so the following devicetree is needed : *socfpga_cyclone5_de10_nano_CN0540.dtb*

::

   sergiu@analog:~/cn0540/linux$ make socfpga_cyclone5_de10_nano_CN0540.dtb
     DTC     arch/arm/boot/dts/socfpga_cyclone5_de10_nano_CN0540.dtb

Copy the devicetree to the root folder and rename it so the bootloader can find it

::

   sergiu@analog:~/cn0540/linux$ cp arch/arm/boot/dts/socfpga_cyclone5_de10_nano_CN0540.dtb ../socfpga.dtb

.. raw:: html

   </details>


Prepare the SD-card
-------------------

Write the :doc:`Kuiper Images </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` image to the SD-card.

Mount the SD-card after Kuiper image has been written and copy the necessary files.

::

   sergiu@analog:~/cn0540$ mkdir BOOT
   sergiu@analog:~/cn0540$ sudo mount /dev/mmcblk0p1 ./BOOT

Create the environment variable file for the bootloader

::

   sergiu@analog:~/cn0540$ echo "uenvcmd=run adi_sdboot" >> uEnv.txt && \
    echo "adi_sdboot=echo Copying Linux from SD to RAM...&& fatload mmc 0 0x3000000 \${kernel_image} && fatload mmc 0 0x2A00000 \${devicetree_image} && if fatload mmc 0 0x2000000 \${ramdisk_image}; then bootm 0x3000000 0x2000000 0x2A00000; else bootm 0x3000000 - 0x2A00000; fi" >> uEnv.txt && \
    echo "bootargs=console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait" >> uEnv.txt



.. raw:: html

   <details><summary>Xilinx</summary>

::

   sergiu@analog:~/cn0540$ cp {BOOT.bin, uImage, devicetree.dtb, uEnv.txt} BOOT

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Intel</summary>

Create the u-boot script

::

   sergiu@analog:~/cn0540$ echo "fatload mmc 0:1 \$fpgadata soc_system.rbf;" >> boot.script && \
    echo "fpga load 0 /$fpgadata $filesize;" >> boot.script && \
    echo "run bridge_enable_handoff;" >> boot.script && \
    echo "run mmcload;" >> boot.script && \
    echo "run mmcboot;" >> boot.script
   sergiu@analog:~/cn0540$ mkimage  -A arm -O linux -T script -C none -a 0 -e 0 -n "uboot_scr" -d boot.script u-boot.scr
   sergiu@analog:~/cn0540$ cp {soc_system.rbf, socfpga.dtb, zImage, uEnv.txt, u-boot.scr} BOOT
   sergiu@analog:~/cn0540$ sudo dd of=/dev/mmcblk0p3 bs=512 if=preloader_bootloader.img

.. raw:: html

   </details>


::

   sergiu@analog:~/cn0540$ sudo umount BOOT

Now your SD-card is good to go!
