Stratix 10 SoC Development Kit Linux Quick Start Guide
======================================================

Get aarch64-none-linux-gnu and set CROSS_COMPILE and ARCH variables
-------------------------------------------------------------------

::

   analog@debian:~$ **mkdir tools**
   analog@debian:~$ **cd tools**
   analog@debian:~/tools$ **wget https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu-a/10.3-2021.07/binrel/gcc-arm-10.3-2021.07-x86_64-aarch64-none-linux-gnu.tar.xz**
   analog@debian:~/tools$ **tar xvf gcc-arm-10.3-2021.07-x86_64-aarch64-none-linux-gnu.tar.xz**
   analog@debian:~/tools$ **export CROSS_COMPILE=/home/analog/tools/gcc-arm-10.3-2021.07-x86_64-aarch64-none-linux-gnu/bin/aarch64-none-linux-gnu-**
   analog@debian:~/tools$ **export ARCH=arm64**
   analog@debian:~/tools$ **cd ~**

Build Linux kernel
------------------

::

   analog@debian:~$ **git clone https://github.com/analogdevicesinc/linux**
   analog@debian:~$ **cd ./linux**
   analog@debian:~/linux$ **git checkout altera_adxcvr_master**
   analog@debian:~/linux$ **make adi_stratix10_defconfig**
   analog@debian:~/linux$ **make Image**
   analog@debian:~/linux$ **make altera/socfpga_stratix10_socdk_ad9213_dual.dtb**
   analog@debian:~/linux$ **cp arch/arm64/boot/Image /media/analog/BOOT/**
   analog@debian:~/linux$ **cp arch/arm64/boot/dts/altera/socfpga_stratix10_socdk_ad9213_dual.dtb /media/analog/BOOT/socfpga_stratix10_socdk.dtb**
   analog@debian:~/linux$ **cd ~**

Build ARM Trusted Firmware
--------------------------

::

   analog@debian:~$ **git clone https://github.com/altera-opensource/arm-trusted-firmware**
   analog@debian:~$ **cd ./arm-trusted-firmware**
   analog@debian:~/arm-trusted-firmware$ **git checkout rel_socfpga_v2.6.0_22.07.02_pr**
   analog@debian:~/arm-trusted-firmware$ **make bl31 PLAT=stratix10 DEPRECATED=1**
   analog@debian:~/arm-trusted-firmware$ **cd ~**

Build U-Boot and copy u-boot.itb to SD card
-------------------------------------------

::

   analog@debian:~$ **git clone https://github.com/altera-opensource/u-boot-socfpga**
   analog@debian:~$ **cd ./u-boot-socfpga**
   analog@debian:~/u-boot-socfpga$ **git checkout rel_socfpga_v2022.01_22.11.02_pr**
   analog@debian:~/u-boot-socfpga$ **ln -sf ../arm-trusted-firmware/build/stratix10/release/bl31.bin .**
   analog@debian:~/u-boot-socfpga$ **sed -i 's/earlycon panic=-1/earlycon panic=-1 console=ttyS0,115200 root=\/dev\/mmcblk0p2 rw rootwait/g' configs/socfpga_stratix10_defconfig**
   analog@debian:~/u-boot-socfpga$ **sed -i '/^CONFIG_NAND_BOOT=y/d' configs/socfpga_stratix10_defconfig**
   analog@debian:~/u-boot-socfpga$ **sed -i '/^CONFIG_SPL_NAND_SUPPORT=y/d' configs/socfpga_stratix10_defconfig**
   analog@debian:~/u-boot-socfpga$ **sed -i '/^CONFIG_CMD_UBI=y/d' configs/socfpga_stratix10_defconfig**
   analog@debian:~/u-boot-socfpga$ **echo %%'CONFIG_USE_BOOTCOMMAND=y' >> configs/socfpga_stratix10_defconfig%%**
   analog@debian:~/u-boot-socfpga$ **echo %%'CONFIG_BOOTCOMMAND="bridge enable 0xf; setenv ethaddr 00:15:17:ab:cd:ef; load mmc 0:1 ${kernel_addr_r} Image; load mmc 0:1 ${fdt_addr_r} socfpga_stratix10_socdk.dtb; booti ${kernel_addr_r} - ${fdt_addr_r}"' >> configs/socfpga_stratix10_defconfig%%**
   analog@debian:~/u-boot-socfpga$ **make socfpga_stratix10_defconfig**
   analog@debian:~/u-boot-socfpga$ **sed -i '/4GB/,/0x80000000>;/creg = <0 0x00000000 0 0x80000000>;' arch/arm/dts/socfpga_stratix10_socdk.dts**
   analog@debian:~/u-boot-socfpga$ **make**
   analog@debian:~/u-boot-socfpga$ **cp u-boot.itb /media/analog/BOOT/**
   analog@debian:~/u-boot-socfpga$ **cd ~**

Generate .sof (SRAM Object File) and .jic (JTAG Indirect Configuration) files
-----------------------------------------------------------------------------

::

   analog@debian:~$ **git clone https://github.com/analogdevicesinc/hdl**
   analog@debian:~$ **cd hdl/projects/ad9213_dual_ebz/s10soc**
   analog@debian:~/hdl/projects/ad9213_dual_ebz/s10soc$ **make**
   Building ad9213_dual_ebz_s10soc [/home/analog/hdl/projects/ad9213_dual_ebz/s10soc/ad9213_dual_ebz_s10soc_quartus.log] ... OK
   analog@debian:~/hdl/projects/ad9213_dual_ebz/s10soc$ **quartus_pfg -c ad9213_dual_ebz_s10soc.sof -o hps_path=../../../../u-boot-socfpga/spl/u-boot-spl-dtb.hex ad9213_dual_ebz_s10soc_hps.sof**
   analog@debian:~/hdl/projects/ad9213_dual_ebz/s10soc$ **quartus_pfg -c ad9213_dual_ebz_s10soc_hps.sof ad9213_dual_ebz_s10soc_hps.jic -o device=MT25QU02G -o flash_loader=1SX280HU2F50E1VGAS**

Set FPGA configuration mode
---------------------------

**SW2** 4-bit DIP Switch

========== ====== ======= ======= ========
Switch Bit **1**  **2**   **3**   **4**
Name       MSEL0  MSEL1   MSEL2   Not Used
JTAG Mode  **ON** **ON**  **ON**  **OFF**
QSPI Mode  **ON** **OFF** **OFF** **OFF**
========== ====== ======= ======= ========

