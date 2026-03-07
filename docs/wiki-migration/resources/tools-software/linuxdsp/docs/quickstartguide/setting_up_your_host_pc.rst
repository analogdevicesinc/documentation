.. important::

   The following instructions are correct for developers using Ubuntu 18.04 LTS.


Installing Required Packages
============================

In order to build and deploy Linux to your ADSP-SC5xx development board you will need to install several additional packages on to your host PC. This can be performed using the following command and respond yes(y) to any prompts:

::

   $ sudo apt-get update
   $ sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev xterm u-boot-tools openssl curl tftpd-hpa python

If you are running on a 64-bit host, then you also need to install the following packages:

::

   $ sudo apt-get install zlib1g:i386 libncurses5:i386

| 
| ==== Installing CrossCore Embedded Studio ==== Browse to :adi:`en/design-center/evaluation-hardware-and-software/software/linuxaddin`.html#software-overview and download the 2.8.3 release of CrossCore Embedded Studio. Install the .deb package.

::

   $ sudo dpkg -i adi-CrossCoreEmbeddedStudio-linux-x86-2.8.3.deb

Add the **/opt/analog/cces/2.8.3/ARM/arm-none-eabi/bin** directory to your path.

| 
| ==== Setting Up TFTP ==== We use the TFTP server on the host to transfer images to the EZ-KIT. This needs to be configured for use:

::

   $ sudo vi /etc/default/tftpd-hpa

   #add following commands 
   TFTP_USERNAME="tftp"
   TFTP_DIRECTORY="/tftpboot"
   TFTP_ADDRESS="0.0.0.0:69"
   TFTP_OPTIONS="--secure"

   $ sudo mkdir /tftpboot
   $ sudo chmod 777 /tftpboot
   $ sudo service tftpd-hpa restart

| 
| ==== Setting Up NFS Server ==== We can use the NFS server on the host to transfer images to the EZ-KIT. If you wish to use the NFS boot method you can install the NFS server on your host PC. This needs to be configured for use:

::

   $ sudo apt-get install nfs-kernel-server
   $ sudo vi /etc/exports

   #Add following commands
   /romfs *(rw,sync,no_root_squash,no_subtree_check)

   $ sudo mkdir /romfs/
   $ sudo chmod 777 /romfs/
   $ sudo service nfs-kernel-server start

| 
| ==== Configuring Minicom ==== In order to communicate with the U-Boot bootloader, a UART connection must be made between the host PC and the development board. It is recommended that you use **minicom** to do this. Minicom must be configured to connect to U-Boot correctly.

On the host PC open a terminal and execute the following commands:

::

   $ sudo apt-get install minicom
   $ sudo minicom -s

               +-----[configuration]------+


               | Filenames and paths      |

               | File transfer protocols  |
               | Serial port setup        |
               | Modem and dialing        |
               | Screen and keyboard      |
               | Save setup as dfl        |
               | Save setup as..          |
               | Exit                     |
               | Exit from Minicom        |
               +--------------------------+


   # Select Serial port setup
        Set Serial Device to /dev/ttyUSB0
        Set Bps/Par/Bits to 57600 8N1
        Set Hardware Flow Control to No
        
        Close the Serial port setup option by press Esc
    Select Save setup as dfl
    Select Exit

| 
| ---- **HOME PAGE:** :doc:`Linux for ADSP-SC5xx Processors </wiki-migration/resources/tools-software/linuxdsp>` **NEXT:** :doc:`Setting Up Sources </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/source-setup>`
