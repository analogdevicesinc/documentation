Creating a Bootable Application
===============================

To create a bootable application that can be loaded into the processor's connected flash memory, a loader image (LDR) must be created. This requires the DXE developed in the :doc:`previous section </wiki-migration/resources/tools-software/crosscore/cces/getting-started/led-blink-app>` as the main application and -- if our app uses external memory -- an initialization file. This example fits entirely in on-chip memory but the process is described to give insight into developing larger applications.

Initialization File
===================

When using an emulator-based CCES debug session, the IDE dynamically loads the application’s executable file (DXE) to the processor’s on-chip and external memory, bypassing the boot process altogether. For on-chip memory there is no difference in how the emulator communicates with the processor and how the boot stream behaves.

However, the JTAG interface used to target the processor does not communicate directly with the board's external DDR memory. Instead, data for DDR space is sent via JTAG to the processor which then writes it out over its external bus to DDR. To support this, the emulator firmware must *first* set registers on the processor to configure the clocks and external bus *before* trying to write the application’s code and data to external memory. Not doing so would result in hardware errors and exceptions as the processor attempted to load to an unconfigured device.

Initialization File for Debugging
---------------------------------

For debugging applications on evaluation boards, registers and settings can be defined in XML files or a pre-load file.

Pre-load Files
~~~~~~~~~~~~~~

Pre-load files are similar to initcodes used in the creation of LDR files but are used during debugging. Currently only ADSP-SC5xx and ADSP-215xx processors use pre-load files. You can find the pre-built binary files in **SHARC\\ldr**.

The projects used to create pre-load binary files are located in **SHARC\\ldr\\init_code\\SC5xx_Init**. The main purpose of pre-load files is to set clocks and DMC settings so the debugger can load your application to external memory. If you want to change this setup you can update the source files, rebuild the pre-load executable, and place the binary in the **SHARC\\ldr** folder, overwriting the existing file.

In general, the master core is the only core that needs a pre-load. Debug configurations will automatically register the pre-load file as one of the applications to be loaded. For an ADSP-SC5xx processor, the pre-load will be part of the ARM Core 0 project. For an ADSP-215xx processor the preload will be part of the first SHARC+ core project.

XML files
~~~~~~~~~

Processors with simpler memory configurations use an XML file to specify which registers need written to enable external memory access. For example, the ADSP-BF707 evaluation platform has the *ADSP-BF707-resets.xml* file located in the CCES installation in the **\\System\\ArchDef** directory providing a list of Clock Generation Unit (CGU0) and Dynamic Memory Controller (DMC0) registers. These need programming to support the CLKIN and DDR memory specific to the ADSP-BF707 EZ-KIT Lite board, as shown in Listing 2:

.. code:: xml

       <!-- Init clocks( CCLK = 400Mhz, SYSCLK = 200Mhz, SCLK0 = 100Mhz -->
       <!--              SCLK1 = 200Mhz, DCLK = 200Mhz, PLLCLK = 800Mhz -->
       <!-- WARNING: Do not change the order of these registers as the -->
       <!-- WARNING: debugger expects them in a certain order so that  -->
       <!-- WARNING: it can poll on status bits to make sure the init  -->
       <!-- WARNING: has completed                                     -->
       <register name="CGU0_DIV" reset-value="0x42042442" core="Common" />
       <register name="CGU0_CTL" reset-value="0x00002000" core="Common" />
       
       <!-- Init DDR0 based on the clock settings above -->
       <!-- WARNING: Do not change the order of these registers as the -->
       <!-- WARNING: debugger expects them in a certain order so that  -->
       <!-- WARNING: it can poll on status bits to make sure the init  -->
       <!-- WARNING: has completed                                     -->
       <register name="DMC0_PHY_CTL4" reset-value="0x00000001" core="Common" />
       <register name="DMC0_PHY_CTL3" reset-value="0x0A0000C0" core="Common" />
       <register name="DMC0_CAL_PADCTL2" reset-value="0x0078283C" core="Common" />
       <register name="DMC0_CAL_PADCTL0" reset-value="0xF0000000" core="Common" />
       <register name="DMC0_CFG" reset-value="0x00000522" core="Common" />
       <register name="DMC0_TR0" reset-value="0x20B08323" core="Common" />
       <register name="DMC0_TR1" reset-value="0x20270618" core="Common" />
       <register name="DMC0_TR2" reset-value="0x00323209" core="Common" />
       <register name="DMC0_MR" reset-value="0x00000432" core="Common" />
       <register name="DMC0_EMR1" reset-value="0x00000000" core="Common" />
       <register name="DMC0_EMR2" reset-value="0x00000000" core="Common" />
       <register name="DMC0_CTL" reset-value="0x00002404" core="Common" />
       <register name="DMC0_DLLCTL" reset-value="0x0000054B" core="Common" />

Initialization File for Boot Image
----------------------------------

When moving to a standalone boot image (i.e., when the emulator is not doing this automatically), the same initialization must be performed by the application. This is handled by an **initialization file**.

An initialization file is a small processor DXE that is prepended as an *initialization block* at the top of the LDR image before the application code. This block is booted into on-chip memory first and runs *before* any external memory accesses are attempted. In the boot stream, once the initialization block has loaded and run, flow returns to the boot ROM so the rest of the application can be loaded, which includes writing code and data to off-chip memory in addition to overwriting the on-chip memory used by the initialization code.

Step 1: Create a Boot Image
===========================

Creating a bootable image differs between processor families. Follow the correct guide for your target processor:

-  :doc:`Creating a boot image (single-core processors) </wiki-migration/resources/tools-software/crosscore/cces/getting-started/boot-app-bf70x>`
-  :doc:`Creating a boot image (dual-core ADSP-BF60x processors) </wiki-migration/resources/tools-software/crosscore/cces/getting-started/boot-app-bf60x>`
-  :doc:`Creating a boot image (multi-core ADSP-SC5xx processors) </wiki-migration/resources/tools-software/crosscore/cces/getting-started/boot-app-sc5xx>`

After creating your boot image, please return to this page and continue from `Step 2 <https://wiki.analog.com/>`_ below.

Step 2: Write Application to Flash Memory
=========================================

With the LDR file generated, the final step is to write your application to your device's SPI flash memory. This is handled via the Command Line Device Programmer (cldp.exe) utility. Again, we will use the :doc:`blink example </wiki-migration/resources/tools-software/crosscore/cces/getting-started/led-blink-app/sc573-blink>` project created previously for the ADSP-SC573 EZ-KIT.

Just as the JTAG interface does not directly access DDR memory when downloading the DXE during debug, the CLDP does not interact directly with the board's flash memory. Instead, it uses the processor to load a host driver to communicate with flash, then passes the LDR image via JTAG so the processor can write it by issuing the proper commands to the flash. To coordinate this, **cldp.exe** needs several command-line switches and arguments to initialize the JTAG programmer, load the flash driver to the processor, then load the LDR image to the EZ-Kit's memory, as follows:

**-proc**: target processor (e.g. ADSP-BF707, ADSP-BF609, ADSP-SC573, etc.)

**-emu**: emulator driver (**-1000** or **-2000**) for the active debug session. Needed to send LDR image to processor

.. tip::

   This example uses the ICE-2000 emulator so this switch is set to **ICE-2000**. Consult CCES On-Line Help for CLDP settings appropriate for your configuration.


**-core** the core used to run the flash memory driver.

.. important::

   For processors containing ARM and SHARC+ cores, **core 1 must run the flash memory driver**.


**-driver**: flash memory device driver (included with the Board Support Package installation) the processor uses to work with the board's flash device

**-cmd**: the flash program command (**prog**) must be issued explicitly

**-erase**: the **affected** region of flash memory must be erased before programming

**-file**: LDR image to be written to flash.

Example cldp.exe command lines
------------------------------

.. code:: bash

       cldp -proc ADSP-BF707 –emu ICE-1000 -driver "<ADSP-BF707 EZ-KIT BSP root directory>\BF707_EZ-Board\Blackfin\Examples\Device_Programmer\bf707_w25q32bv_dpia.dxe" -cmd prog –erase affected -file "<workspace directory>\Debug\CCES Example.ldr"

.. code:: bash

       cldp -proc ADSP-BF609 –emu ICE-1000 -driver "<ADSP-BF609 EZ-KIT BSP root directory>\BF609_EZ-Board\Blackfin\Examples\Device_Programmer\serial\bf609_w25q32bv_dpia.dxe" -cmd prog –erase affected -file "<workspace directory>\Debug\CCES Example.ldr"

.. code:: bash

       cldp -proc ADSP-SC573 -emu ICE-2000 -core 1 -driver "<ADSP-SC5xx EZ-KIT BSP root directory>\ADSP-SC5xx_EZ-KIT\Examples\Device_Programmer\sc573\sharc\sc573_w25q128fv_dpia_Core1\sc573_w25q128fv_dpia_Core1.dxe" -core 1 -cmd prog -erase affected -file "<workspace directory>\Debug\CCES_Example_Core2.ldr"

.. important::

   \ *<directory>* indicates the full path to these files is required based on where the BSP is installed and where the CCES project was created.


Method 1: Use Command-Line Device Programming Utility Directly
--------------------------------------------------------------

1. Open a Command Prompt and navigate to your CrossCore Embedded Studio root installation folder. By default, on Windows this is **C:\\Analog Devices\\CrossCore Embedded Studio 2.X\\**. cldp.exe is located in this directory

2. Run the flash driver using the appropriate command line from above and tailoring as required:

-  Our blink example targets the ADSP-SC589 heterogeneous processor so we must specify **-core 1**
-  Ensure the path to the **-driver** file correctly points to the core 1 ``*.dpia`` file in your Board Support Package
-  Ensure the **-path** parameter points to the ``*.ldr`` file created previously.

.. image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/getting-started/07_cldp_command_prompt.png

*Figure 1: Flashing device directly with cldp.exe*

The successful **. . . . . . done** message indicates device programming is complete and the application is now stored in the flash memory. To verify the application boots properly without CCES, close CCES and verify the boot selector switch (SW1) on the board is in Position 1 to boot from SPI flash. If the board’s power is cycled or reset button pushed, the LED blink application will boot from flash memory should behave as it did during debug.

Method 2: Configure CCES to Automatically Trigger cldp.exe on Successful Build
------------------------------------------------------------------------------

CCES can be configured to automatically call **cldp.exe** at the end of the build process: 1. In **Project Explorer** view, right-click any of the projects and select **Properties…** 2. On **C/C++ Build Settings** page, select **Build Steps** 3. Under **Post-build steps**, populate **Command** field with appropriate command line (see *Figure 5*).

.. warning::

   Do *not* copy and paste the command line from above as formatting differences will cause cldp.exe to fail.


.. image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/getting-started/08_postbuild_configuration.gif

*Figure 2: CLDP Command Line in Project Settings Build Steps Window*

--------------

.. image:: https://wiki.analog.com/_media/navigation CCES Getting Started#led-blink-app
   :alt: LED Blink Application#.|CCES Getting Started#.|CCES Getting Started
