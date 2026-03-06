DroneTRX Software User Guide
============================

DroneTRX is an HDL reference modem showcasing ADI’s best-in-class RF transceivers in wireless communications applications. The design is implemented using the ADRV9361-Z7035 system on module (SOM). The SOM is based on the AD9361 RF Transceiver and the Xilinx Zynq®-7000 All Programmable (AP) SoC.

DroneTRX integrates an HDL PHY layer alongside a demo application for video streaming. The DroneTRX HDL PHY layer originally supports Orthogonal Frequency Domain Multiplexing 1T1R Single-Input Single-Output (OFDM-SISO) mode. This is further extended to support multiple input multiple output (OFDM-MIMO) spatial diversity mode. The wireless standard is based on a modified IEEE 802.11n protocol.

This page provides instructions on how to build and set up the software for the DroneTRX reference modem.

| 
| ==== Requirements ==== To prepare the DroneTRX SD card, you will need the following:

-  A host PC or laptop with USB port and SD card reader
-  Windows or Linux operating system
-  A Class 10 SD card, at least 16 GB size
-  An SD imager utility to format and write to the SD card. You may use the default Windows format utility or 3rd-party utility such as Raspberry Pi Imager.

Please also ensure you have the correct hardware setup/evaluation board. Refer to the :doc:`DroneTRX Hardware Setup Guide </wiki-migration/resources/eval/user-guides/dronetrx/hardware>` for details.

To build the SDR driver, please take note of the additional build prerequisites:

-  A Linux OS host PC, laptop or virtual machine. Ubuntu 22.04 distribution is recommended.
-  A compiler for the target SDR platform. For our case, we shall use the GCC ARM compiler from https://gitlab.com/RK3588_Linux/rk/prebuilts/gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf.git

To build the FPGA bitstream, please take note of the additional build prerequisites:

-  Vivado 2021.1
-  Xilinx evaluation licenses for the following IPs

   -  AXI Interconnect 2.1

      -  AXI IIC 2.1

         -  Clocking Wizard 6.0
         -  Constant 1.1
         -  Concat 2.1
         -  Utility Vector Logic 2.0
         -  Zynq7 Processing System 5.5
         -  GMII to RGMII 4.1
         -  Processor System Reset Module 5.0
         -  Utility Reduced Logic 2.0
         -  Slice 1.0
         -  AXI DMA Controller 7.1
         -  Block Memory Generator 8.4
         -  Complex Multiplier 6.0
         -  Divider Generator 5.1
         -  Fast Fourier Transform 9.1
         -  Viterbi Decoder 9.1

| 
| ===== Software Repositories ===== Source code and binaries mentioned in this guide can be accessed from the following repositories.

+---------------------------------+------------------------------------------------------------------------------------+
| **Description**                 | **Link**                                                                           |
+---------------------------------+------------------------------------------------------------------------------------+
| OpenWiFi Base Image             | https://drive.google.com/file/d/12egFLT9TclmY8m3vCMHmUuSne3qK0SWc/view?usp=sharing |
+---------------------------------+------------------------------------------------------------------------------------+
| Pre-built binaries              | https://bitbucket.analog.com/scm/cos-apjc/drone_trx-images.git                     |
+---------------------------------+------------------------------------------------------------------------------------+
| SDR driver and demo application | https://bitbucket.analog.com/scm/cos-apjc/drone_trx-sdr-app.git                    |
+---------------------------------+------------------------------------------------------------------------------------+
| HDL                             | https://bitbucket.analog.com/scm/cos-apjc/drone_trx-hdl.git                        |
+---------------------------------+------------------------------------------------------------------------------------+

| 

--------------

SD Card Setup
-------------

To run the DroneTRX system, an SD card containing the software and FPGA image must be first prepared. An SD card size of at least 16 GB is required.

|

| === Set up the Base Image ===

-  First, download the base “vanilla” image from the `OpenWiFi Download Image QuickStart page <https://github.com/open-sdr/openwifi?tab=readme-ov-file#download-img-and-quick-start>`__.

-  Flash this openwifi.img file using Balena Etcher or Raspberry Pi imager using the instructions indicated here:

   -  :doc:`Linux Hosts </wiki-migration/resources/tools-software/linux-software/zynq_images/linux_hosts>`

      -  :doc:`Windows Hosts </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>`

| 
| === Update FPGA and Driver === Once the SD card has been successfully flashed, you will need to update the FPGA bitstream and other system related files. Perform the following steps on a host machine.

-  First, get the pre-built binaries from this repository: https://bitbucket.analog.com/scm/cos-apjc/drone_trx-images.git
-  On the HDL folder, you will see two subfolders: SISO and MIMO. Each of these subfolders will contain the FPGA bitstream and other binaries to start a DroneTRX SISO or MIMO version. If you wish to set up a SISO system, copy the files from the HDL/SISO folder. Otherwise, copy the files from the HDL/MIMO folder to set up a MIMO system.
-  On a host machine, mount the prepared SD card from step 1. Copy the BOOT.bin, devicetree.dtb and uImage to the BOOT partition of the SD card.

| 
| === Transfer DroneTRX User Space Scripts ===

-  Eject the SD card from the host PC and insert into the ADRV9361-SOM board’s SD card slot.
-  Switch on the ADRV9361-SOM board. You will see that the system will start to boot. Once booted, you should have access to the console or Kuiper desktop.
-  Open a terminal and switch to the root user.
-  Note that the default user is the “analog” user, the password for this user is “analog”. The password for the “root” account is “analog” as well.
-  Copy the user space files (demo app and scripts) from https://bitbucket.analog.com/scm/cos-apjc/drone_trx-sdr-app.git and copy into /home/analog directory.
-  **(OPTIONAL -- ONLY FOR MIMO build)** Get the pre-built SDR kernel modules from STEP1 under the SDR/MIMO subdirectory or build the SDR kernel modules from source (See `#update_fpga_and_driver_section <https://wiki.analog.com/>`__). Copy the sdr.ko and tx_intf.ko into the /root/openwifi folder.

| 

--------------

Building the Project from Source
--------------------------------

|

| ==== FPGA Bitstream ==== You will need Vivado on WSL as a prerequisite to build the project. Please refer to the README.txt from the repository for instructions. The repository provides a single one-time script that will setup and build the project. The HDL build process will generate the BOOT.bin, device tree and uImage files that will be copied back to the SD card.

SDR Driver
~~~~~~~~~~

To build the SDR driver, please refer to the following out-of-tree build instructions.

1. Download the ARM compiler by executing the following command:

<code> git clone https://gitlab.com/RK3588_Linux/rk/prebuilts/gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf.git\ </code>

-  Take note of the path where you cloned this directory.

| |image1|
| 2. Clone the **drone_trx-sdr-app** repository and apply the patches.

<code> git clone https://bitbucket.analog.com/scm/cos-apjc/drone_trx-sdr-app.git </code>


|image2|

::

   cd drone_trx-sdr-app

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sdr_driver_3.png
   :align: center
   :width: 800px

::

   git submodule init

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sdr_driver_4.png
   :align: center
   :width: 800px

::

   git submodule update –init –recursive

| 
| This command will try to update and initialize all submodules, which includes the linux kernel and the openwifi repos. |image3|

Once the submodules are initialized, go to dronetrx-openwifi folder and apply patch. You will see that there are two patch files.

-  ``cd dronetrx-openwifi``


|image4|

-  ``git apply patch.diff``
-  ``git apply patch_makefile.diff``

|image5|

3. Navigate to the driver directory

::

   cd /openwifi/driver

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sdr_driver_8.png
   :align: center
   :width: 800px

4. Run the sed command below to update the cross compiler path at line 73 based on where your toolchain resides. Ensure to replace /path/to with the actual path where you cloned the compile in step 1.

::

   sed -i '73s|.*|CROSS_COMPILE=/path/to/gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf/bin/arm-none-linux-gnueabihf-|' make_all.sh

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sdr_driver_9.png
   :align: center
   :width: 800px

5. Run the build script. This will take several minutes. <code> ./make_all.sh 32 </code>

6. After make completes, it will generate the kernel modules on the following folders: <code> /path/to/dronetrx-openwifi/openwifi/driver/sdr.ko </code> <code> /path/to/dronetrx-openwifi/openwifi/tx_intf/tx_intf.ko </code>

7. From your host/build machine, copy the compiled kernel driver modules (\*.ko file) mentioned in step 6 to an external media. From the external media, transfer these files to the openwifi root directory on the ADRV9361-Z7035 SDR platform.


| 

User Space
~~~~~~~~~~

For the user space code, there is no need to build since these are either bash scripts or python code that can be executed.

On your host machine, clone the drone_trx-sdr-app repository. No need to repeat this if you already did this as part of the `#update_fpga_and_driver <https://wiki.analog.com/>`__ section.

<code> git clone https://bitbucket.analog.com/scm/cos-apjc/drone_trx-sdr-app.git </code>

You will see two folders. Simply copy the entire dronetrx-demo-app folder user space files (demo app and scripts) to an external media and copy into /home/analog directory on the ADRV9361-Z7035 SDR platform.

|

--------------

Troubleshooting
---------------

Refer to the :doc:`Troubleshooting section </wiki-migration/resources/eval/user-guides/dronetrx>` from the DroneTRX Overview page for commonly encountered issues and how to resolve them.


| 

Help and Support
----------------

For questions and more information, please visit the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone Support Community <reference-designs>`


Additional Resources
--------------------

-  :doc:`Linux on RF-SOM </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynq>`
-  :doc:`Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

|

| |Overview #:[[:resources:eval:user-guides:dronetrx:hardware\| DroneTRX Hardware User Guide#none|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sdr_driver_1.png
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sdr_driver_2.png
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sdr_driver_5.png
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sdr_driver_6.png
   :width: 800px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sdr_driver_7.png
   :width: 800px
.. |Overview #:[[:resources:eval:user-guides:dronetrx:hardware\| DroneTRX Hardware User Guide#none| image:: /navigation #/resources/eval/user-guides/dronetrx
