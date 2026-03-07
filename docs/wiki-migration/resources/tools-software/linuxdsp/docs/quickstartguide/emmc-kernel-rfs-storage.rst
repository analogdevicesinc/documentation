Store kernel image and RootFS on the eMMC
=========================================

.. note::

   The following instructions are for the ADSP-SC598-EZKIT development board (the EV-SC598-SOM System-on-Module (SOM) board attached to the EV-SOMCRR-EZKIT carrier board). Furthermore, this is supported on :doc:`version 3.0.0 of Linux for ADSP-SC5xx </wiki-migration/resources/tools-software/linuxdsp/releaselandingpages/3.0.0>`\


Introduction
------------

This example will guide you through some changes that are needed in order to store the kernel and rootfs on the eMMC, with U-Boot still booting out of QSPI.

This allows for storing larger images without having to plug in an external device, as the SC598-SOM comes with eMMC present on the SOM.

Prepare the build
-----------------

You should follow the steps up to and including the '**Preparing the buildtool'** step in :doc:`Yocto Linux 3.0.0 Quickstart Guide for ADSP-SC598 </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/quickstart_sc598_3_0_0>`

Apply patches
-------------

Two patches should be applied. The directory the changes needed to take place is ``$PROJECTDIR/sources/meta-adi/``.

.. code:: diff

   From 9d88cecc5ed849fb35192257138e6f3e3577858c Mon Sep 17 00:00:00 2001
   From: Nathan Barrett-Morrison <nathan.morrison@timesys.com>
   Date: Wed, 3 May 2023 11:27:55 -0400
   Subject: [PATCH] Adjust update_mmc to boot from separate fitImage-emmc-tools
    with proper provisioning initramfs (sshd, gzip, etc)

   ---
    include/configs/sc_adi_common.h | 2 +-
    1 file changed, 1 insertion(+), 1 deletion(-)

   diff --git a/include/configs/sc_adi_common.h b/include/configs/sc_adi_common.h
   index f7b5f8ca8e..a15686521e 100644
   --- a/include/configs/sc_adi_common.h
   +++ b/include/configs/sc_adi_common.h
   @@ -178,7 +178,7 @@
       "spiboot=run spi_boot\0"
    
    #define ADI_MMC_BOOT \
   -   "update_mmc=setenv bootcmd \'run mmcboot\'; saveenv; run ramboot\0" \
   +   "update_mmc=setenv bootcmd \'run mmcboot\'; saveenv; setenv imagefile fitImage-emmc-tools; run ramboot\0" \
       "mmcargs=setenv bootargs " ADI_BOOTARGS_MMC "\0" \
       "mmcload=" ADI_MMC_LOAD "\0" \
       "mmc_boot=" ADI_MMC_BOOTCMD "\0" \
   -- 
   GitLab

.. code:: diff

   From 2cf70574c8146cac16cf5b8f3895c557c0e23a2f Mon Sep 17 00:00:00 2001
   From: Nathan Barrett-Morrison <nathan.morrison@timesys.com>
   Date: Wed, 3 May 2023 11:26:21 -0400
   Subject: [PATCH] Fixup adsp-sc5xx-minimal-emmc + adsp-sc5xx-ramdisk-emmc-tools
    so that we can provision and boot from MMC

   ---
    .../classes/adsp-fit-generation.bbclass         | 12 ++++++++++--
    .../images/adsp-sc5xx-minimal-mmc.bb            | 17 ++++++++++-------
    .../images/adsp-sc5xx-ramdisk-emmc-tools.bb     |  5 +++--
    3 files changed, 23 insertions(+), 11 deletions(-)

   diff --git a/meta-adi-adsp-sc5xx/classes/adsp-fit-generation.bbclass b/meta-adi-adsp-sc5xx/classes/adsp-fit-generation.bbclass
   index c6cd418..5001b82 100644
   --- a/meta-adi-adsp-sc5xx/classes/adsp-fit-generation.bbclass
   +++ b/meta-adi-adsp-sc5xx/classes/adsp-fit-generation.bbclass
   @@ -58,7 +58,7 @@ emit_its() {
    
           ramdisk-3 {
               description = "Initial Ram File System";
   -           data = /incbin/("adsp-sc5xx-ramdisk-${MACHINE}.cpio.gz");
   +           data = /incbin/("adsp-sc5xx-${1}-${MACHINE}.cpio.gz");
               type = "ramdisk";
               arch = "${ARCH}";
               os = "linux";
   @@ -95,7 +95,15 @@ EOF
    
    do_assemble_fitimage() {
       cd ${DEPLOY_DIR_IMAGE}
   -   emit_its;
   +
   +   #Provisioning fitImage for flashing MMC
   +   if [ "${IMAGE_BASENAME}" = "adsp-sc5xx-minimal-mmc" ]; then
   +       emit_its ramdisk-emmc-tools;
   +       uboot-mkimage -D "${UBOOT_MKIMAGE_DTCOPTS}" -f fit-image.its fitImage-emmc-tools
   +   fi
   +
   +   #Normal fitImage for booting
   +   emit_its ramdisk;
       uboot-mkimage -D "${UBOOT_MKIMAGE_DTCOPTS}" -f fit-image.its fitImage
    }
    
   diff --git a/meta-adi-adsp-sc5xx/recipes-adi/images/adsp-sc5xx-minimal-mmc.bb b/meta-adi-adsp-sc5xx/recipes-adi/images/adsp-sc5xx-minimal-mmc.bb
   index eb1bcfe..b856841 100644
   --- a/meta-adi-adsp-sc5xx/recipes-adi/images/adsp-sc5xx-minimal-mmc.bb
   +++ b/meta-adi-adsp-sc5xx/recipes-adi/images/adsp-sc5xx-minimal-mmc.bb
   @@ -1,13 +1,13 @@
    inherit adsp-sc5xx-minimal
    
   -IMAGE_INSTALL += "kernel kernel-devicetree"
   +DEPENDS += "adsp-sc5xx-ramdisk-emmc-tools"
    
   -#We do not need these files in the rootfs -- remove them to reduce the minimal rootfs size
   -fakeroot do_rootfs_cleanup(){
   -
   -   #We need this for eMMC boot -- do not delete
   -   #rm -rf ${IMAGE_ROOTFS}/boot
   +do_rootfs[depends] += " \
   +   adsp-sc5xx-ramdisk-emmc-tools:do_image_complete \
   +"
    
   +fakeroot do_rootfs_cleanup(){
   +   #We do not need these files in the rootfs -- remove them to reduce the minimal rootfs size
       rm -rf ${IMAGE_ROOTFS}/etc/udev/hwdb.bin
       rm -rf ${IMAGE_ROOTFS}/etc/udev/hwdb.d
    
   @@ -16,8 +16,11 @@ fakeroot do_rootfs_cleanup(){
    
       rm -rf ${IMAGE_ROOTFS}/usr/lib/libX11.so.6
       rm -rf ${IMAGE_ROOTFS}/usr/lib/libX11.so.6.3.0
   +
   +   #Pack fitImage into MMC RFS:
   +   cp ${DEPLOY_DIR_IMAGE}/fitImage ${IMAGE_ROOTFS}/boot
    }
    
   -addtask rootfs_cleanup after do_rootfs before do_image
   +addtask rootfs_cleanup after do_assemble_fitimage before do_image_ext4
    
    IMAGE_FSTYPES:append = " wic.gz ext4 "
   diff --git a/meta-adi-adsp-sc5xx/recipes-adi/images/adsp-sc5xx-ramdisk-emmc-tools.bb b/meta-adi-adsp-sc5xx/recipes-adi/images/adsp-sc5xx-ramdisk-emmc-tools.bb
   index e7872eb..dbf441e 100644
   --- a/meta-adi-adsp-sc5xx/recipes-adi/images/adsp-sc5xx-ramdisk-emmc-tools.bb
   +++ b/meta-adi-adsp-sc5xx/recipes-adi/images/adsp-sc5xx-ramdisk-emmc-tools.bb
   @@ -1,4 +1,4 @@
   -inherit core-image extrausers adsp-sc5xx-compatible
   +inherit adsp-sc5xx-ramdisk adsp-fit-generation
    
    SUMMARY = "eMMC/MMC provisioning ramdisk image for Analog Devices ADSP-SC5xx boards"
    LICENSE = "MIT"
   @@ -6,6 +6,7 @@ LICENSE = "MIT"
    #For transferring data to flash eMMC/SD via ramdisk
    MMC_UTILS = " \
        openssh \
   +    openssh-sshd \
        e2fsprogs-resize2fs \
        gzip \
        adi-flash-emmc \
   @@ -15,4 +16,4 @@ MMC_UTILS = " \
    
    IMAGE_INSTALL:append = " \
        ${MMC_UTILS} \
   -"
   +"
   \ No newline at end of file
   -- 
   GitLab

You can copy and paste the contents of the above two patches in files under the target directory (``PROJECTDIR/sources/meta-adi/''), e.g. patch1.patch & patch2.patch, and apply them with git, e.g. '' git apply patch1.patch && git apply patch2.patch``

Build and boot the eMMC image
-----------------------------

Return to the ``build`` directory of your project, i.e. ``$PROJECTDIR/build/`` and build the eMMC provisioning ramdisk:

.. code:: bash

   bitbake adsp-sc5xx-minimal-mmc

When that's done, Boot U-Boot from JTAG on the target board and flash SPI. This is described in detail in :doc:`Yocto Linux 3.0.0 Quickstart Guide for ADSP-SC598 </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/quickstart_sc598_3_0_0>` during the '**Running U-Boot on the Board for the first time**' section.

Now that you have U-Boot flashed on the target board, you can boot the eMMC provisioning ramdisk like so:

::

   ;''**Target board**''
   :<code bash>

=> env default -a

=> setenv tftpserverip xxx.xxx.xxx.xxx;

=> run update_mmc </code>

Flash the eMMC form your host/build machine via SSH
---------------------------------------------------

You need to start ``sshd`` on your target board:

::

   ;''**Target board**''
   :<code bash>

$ ssh-keygen -A

$ mkdir /var/run/sshd

$ /usr/sbin/sshd </code>

On your build machine, you need to flash the image to the target board via SSH:

::

   ;''**Build machine**''
   :<code bash>

$ cd $PROJECTDIR/build/tmp/deploy/images/adsp-sc598-som-ezkit

$ dd if=adsp-sc5xx-minimal-mmc-adsp-sc598-som-ezkit.wic.gz \| ssh root@<your board's ip> 'adi-flash-emmc.sh'

Flashing image... 75396+1 records in 75396+1 records out 38602977 bytes (39 MB, 37 MiB) copied, 23.0113 s, 1.7 MB/s Image flashed... Resizing partition to fill empty space... Resized! Complete! </code>

Finally, reboot your target board:

::

   ;''**Target board**''
   :<code bash>

$ echo b > /proc/sysrq-trigger </code>

It should now reset and boot from eMMC.
