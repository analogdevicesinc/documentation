Installing U-boot
=================

The ADSP-SC5xx development boards do not ship with U-Boot or Linux pre-installed. The following steps should be taken when install U-Boot on to the development board for the first time, or the board has become unresponsive and the U-Boot console cannot be brought up:

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/initial_uboot_install.jpg
   :width: 600px

Software Preparation
--------------------

Make sure you have "**bitbake u-boot-adi**" succesfully following the previous section :doc:`Building The Linux Components </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/building>` and get the desired u-boot image in the deploy directory. Copy the **U-Boot loader file** to the **/tftpboot** directory so it can be uploaded to the target board.

::

   $ cp build/tmp/deploy/images/<MACHINE>/<UBOOT_LDR_FILE> /tftpboot

Where the macros in the above command are listed at the bottom of this page in **Appendix**.

Hardware Connection
-------------------

Connect the hardware as follows:

-  Connect the **ICE-1000 or ICE-2000** emulator to the **host PC** via the supplied **USB micro** cable
-  Connect the **ICE-1000 or ICE-2000** to the development board **Debug Port** using the cable provided
-  Connect the **host PC** to the **USB/UART** port of the development board using the the supplied **USB Nano** cable
-  Connect the **development board** to the **network** using the provided **ethernet** cable. For boards with two ethernet ports the **10/100/1000** port should be used, not the **10/100** port
-  Connect the **development board** to the **power supply** and plug in the power supply

| 
| ===== Write U-Boot onto Target Board via GDB =====

U-Boot Console Output
~~~~~~~~~~~~~~~~~~~~~

The output from u-Boot is transmitted to the host PC using the micro USB cable connected from the Host PC to the USB-to-UART port of the EZ-Kit. Make sure you've already configured the minicom followed above section :doc:`Setting up your host </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/setting_up_your_host_pc>`.

Open the minicom console, If you can see the output from minicom after you reset the board, you could skip the section "**Flash U-Boot for the First Time**" below and turn to section "**Flash U-Boot to SPI Flash**" directly.

::

   ;''**Terminal1: minicom**''
   :<code>$ sudo minicom </code>

Flash U-Boot for the First Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before booting Linux we need to use the **ICE-1000** or **ICE-2000** to load the U-Boot bootloader on to the EZ-Kit.

Connect the ICE-1000 or ICE-2000 to DEBUG port via a USB cable as well as switch the boot mode to No boot/Custom ROM (BMODE switch set to position 0).

::

   ;''**Terminal2: Run OpenOCD**''
   :In a second terminal window launch the OpenOCD and connect to the development board. The  **config file** parameters should be changed if you are using a different interface or target.

::

   $ cd /opt/analog/cces/2.8.3/ARM/openocd/share/openocd/scripts 
   $ sudo /opt/analog/cces/2.8.3/ARM/openocd/bin/openocd -f interface/<ICE>.cfg -f target/<TARGET>.cfg

Where **<ICE>** and **<TARGET>** should be replaced.

======= =========
ICE     TARGET
======= =========
ice1000 adspsc58x
ice2000 adspsc57x
======= =========

When success you should see a message similar to the console output below:

::

   Open On-Chip Debugger (Analog Devices CCES 2.9.0 OpenOCD 0.9.0-ga44a178) 0.9.0
   Licensed under GNU GPL v2
   Report bugs to <processor.tools.support@analog.com>
   adapter speed: 1000 kHz
   Info : transports supported by the debug adapter: "jtag", "swd"
   Info : auto-select transport "jtag"
   halt and restart using CTI
   trst_only separate trst_push_pull
   Info : ICE-1000 firmware version is 1.0.2
   Info : clock speed 1000 kHz
   Info : JTAG tap: adspsc58x.adjc tap/device found: 0x228080cb (mfg: 0x065, part: 0x2808, ver: 0x2)
   Info : JTAG tap: adspsc58x.dap enabled
   Info : adspsc58x.dap: hardware has 3 breakpoints, 2 watchpoints
   Info : adspsc58x.dap: but you can only set 1 watchpoint

::

   ;''**Terminal3: Loading U-Boot With GDB**''
   :In a third console window launch GDB and load the U-Boot image to flash:

::

   $ cd  tmp/deploy/images/<MACHINE>
   $ /opt/analog/cces/2.8.3/ARM/arm-none-eabi/bin/arm-none-eabi-gdb <UBOOT_BIN_FILE> 
   (gdb) target remote :3333
   (gdb) load <INIT_ELF_FILE> 
   (gdb) c 
   <Press Ctrl+C to interrupt the application>
   (gdb) load <UBOOT_BIN_FILE>
   (gdb) c

Where the macros in the above command are listed at the bottom of this page in **Appendix**.

| 
| At this point U-Boot will now be running in RAM on your target board. You should see U-Boot booting in the minicom console. Press a key to interrupt the boot process before the countdown terminates:

::

   U-Boot 2015.01 ADI-YOCTO-1.0.0 (May 14 2020 - 19:26:23)

   CPU:   ADSP ADSP-SC589-0.1 (Detected Rev: 1.1) (spi flash boot)
   VCO: 450 MHz, Cclk0: 450 MHz, Sclk0: 112.500 MHz, Sclk1: 112.500 MHz, DCLK: 450 MHz
   OCLK: 150 MHz
          Watchdog enabled
   I2C:   ready
   DRAM:  224 MiB
   MMC:   SC5XX SDH: 0                                                                                                        
   SF: Detected IS25LP512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB                                           
   In:    serial                                                                                                              
   Out:   serial                                                                                                              
   Err:   serial                                                                                                              
   other init                                                                                                                 
   Net:   dwmac.3100c000                                                                                                      
   Hit any key to stop autoboot:  0                                                                                           
   sc #

| 
| ==== Flash U-Boot to SPI Flash ==== Here we use the u-Boot console to TFTP a version of u-Boot into RAM, and then write this application into SPI flash.

Configuring the U-Boot Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the U-Boot console, configure the board IP address. This can either be a static address or DHCP allocated. For DHCP:

::

   sc # dhcp

The console should report the IP address allocated to the board.

If you want to manually assign an IP address:

::

   sc # set ipaddr <ADDR>

Where **<ADDR>** is the IP address you want to assign.

Next, set the serverip variable to the IP address of your host PC where the **TFTP** server is running:

::

   sc # set serverip <SERVERIP>

Where **<SERVERIP>** is the IP address of your host PC.

Next, save the environment:

::

   sc # save

Next, run the U-Boot **update** command to copy the U-Boot loader file from the host PC to the target board, and write it into flash:

::

   sc # run update

You will see output similar to the following:

::

   Speed: 1000, full duplex
   Using dwmac.3100c000 device
   TFTP from server 192.168.0.43; our IP address is 192.168.0.44
   Filename 'u-boot-sc589-mini.ldr'.
   Load address: 0xc2000000
   Loading: ########################
            777.3 KiB/s
   done
   Bytes transferred = 347148 (54c0c hex)
   SF: Detected IS25LP512 with page size 256 Bytes, erase size 64 KiB, total 64 MiB
   SF: 524288 bytes @ 0x0 Erased: OK
   SF: 347148 bytes @ 0x0 Written: OK
   sc # 

Note that the update operation will overwrite the flash memory storing the environment configuration, so if you wish to preserve it you need to save it again:

::

   sc # save

At this point the U-Boot binary is stored in flash. You can now disconnect the ICE-1000 or ICE-2000 from the development board and make sure to switch the BMODE to position 1. You will only need to reconnect this if your board fails to boot and you need to re-follow these instructions.

| 
| ===== Appendix: Macro Definition =====

+------------------+----------------------+--------------------+------------------------+
| ``MACHINE``      | ``INIT_ELF_FILE``    | ``UBOOT_BIN_FILE`` | ``UBOOT_LDR_FILE``     |
+==================+======================+====================+========================+
| adsp-sc589-mini  | init-sc589-mini.elf  | u-boot-sc589-mini  | u-boot-sc589-mini.ldr  |
+------------------+----------------------+--------------------+------------------------+
| adsp-sc589-ezkit | init-sc589-ezkit.elf | u-boot-sc589-ezkit | u-boot-sc589-ezkit.ldr |
+------------------+----------------------+--------------------+------------------------+
| adsp-sc584-ezkit | init-sc584-ezkit.elf | u-boot-sc584-ezkit | u-boot-sc584-ezkit.ldr |
+------------------+----------------------+--------------------+------------------------+
| adsp-sc573-ezkit | init-sc573-ezkit.elf | u-boot-sc573-ezkit | u-boot-sc573-ezkit.ldr |
+------------------+----------------------+--------------------+------------------------+

| 
| ---- \*\* PREV::doc:`Installing Linux On The Hardware </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/installing>`\ HOME PAGE:\*\* :doc:`Linux for ADSP-SC5xx Processors </wiki-migration/resources/tools-software/linuxdsp>`
