**Quick Start Guide for Initial Bring-Up of the AD9213-Dual-EBZ ADC Evaluation Board With the Intel Stratix10 FPGA Board**
==========================================================================================================================

TYPICAL SETUP
-------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213_dualbrd_plus_stratix10_diagram_two_power_adapters.png
   :align: center

.. container:: centeralign

   \ *Figure 1. AD9213-DUAL-EVB and Intel Stratix 10 SX Board*\


SCOPE
-----

This QuickStart Guide provides the information to bring up the AD9213-DUAL-EVB in a Synchronized 10G Mode or an Interleaved 20G mode to enable data capture and visualization in IIO Oscilloscope and VisualAnalog. The AD9213 Manual Calibration and Interleaving Guide provides additional detail.

EQUIPMENT AND HARDWARE NEEDED
-----------------------------



- Signal Generators
  - Analog signal source: The frequency and power requirements depend on the tests to be performed. A bandpass filter is often used for single tone tests.
  - 500MHz Reference Clock source: The clock signal generator should have very low phase noise and be capable of supplying a 5dBm 500MHz clock signal.
- PC running Windows with at least 2 USB ports and an Ethernet port
  - Cables to connect to PC
  - One mini-USB
  - One micro-USB
  - One Ethernet
- AD9213-DUAL-EBZ Evaluation Board
- :doc:`AD9213-DUAL-EBZ Evaluation Board Hardware </wiki-migration/resources/eval/user-guides/ad9213_dual_ebz/hardware>`
- RF Power Splitter for splitting test tone to apply two equal signals to each of the two ADCs
- Phase matched coaxial cables to connect power splitter to the ADC input board connectors
- RF Balun for single-ended-to-differential conversion of 500MHz reference clock
- Coax cables for 500MHz reference clock connections
- Intel Stratix 10 SX SoC Development Kit (1SX280HU2F50E1VGAS)

HELPFUL DOCUMENTS
-----------------

-  :adi:`AD9213 Datasheet <en/products/ad9213.html>`

::

   *Intel Stratix 10 SX SoC Development Kit User Guide (from Intel website)

SOFTWARE NEEDED
---------------

-  `Intel Quartus Prime Programmer 19.3 <https://www.intel.com/content/www/us/en/software-kit/661657/intel-quartus-prime-pro-edition-design-software-version-19-3-for-windows.html>`_
-  `PuTTY SSH and telnet client <https://www.putty.org>`_
-  :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  `VisualAnalog <http://www.analog.com/en/design-center/interactive-design-tools/visualanalog.html>`_



- VisualAnalog Canvas for AD9213-DUAL-EBZ (supplied by ADI)
- `libiio (required for using iio Client block in provided VisualAnalog Canvas) <https://github.com/analogdevicesinc/libiio/releases>`_
- `IIO Plugin for Visual Analog <https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/va_iiopluginsetup.zip>`_

ADI SOFTWARE DELIVERABLES
-------------------------

-  `Dual-AD9213-EBZ <https://wiki.analog.com/_media/resources:eval:dual_ad9213_ebz.zip>`_

::

   *The link above contains the following:
   * FPGA binary for the Stratix 10 SX SoC
   * SD Card images containing IIO libraries and a system initialization sequence
   * Example scripts for Synchronization and Interleaving
   * PDF Documents: Software License, Quickstart Guide, Manual Calibration Guide
   * VisualAnalog (software from analog.com) Canvases for viewing FFTs

SETUP AND CONNECTION
--------------------

::

   *With all power and signal generators OFF, connect the boards as shown in Figure 1.
   *Install PC software
     *a. Intel Quartus Prime Programmer (free download from Intel website)
     *b. PuTTY (free, open-source)
     *c. IIO Oscilloscope (link shown above)
     *d. VisualAnalog (link shown above)
   *Configure the switches on the Stratix10 SX SoC FPGA board as follows:

**SW1**

+---------+----------+----------+----------+----------+-----------+-----------+-----------+
| OFF     | ON       | ON       | ON       | ON       | ON        | ON        | ON        |
+=========+==========+==========+==========+==========+===========+===========+===========+
| **S10** | **M10B** | **FMCA** | **FMCB** | **PCIE** | **MSTR0** | **MSTR1** | **MSTR2** |
+---------+----------+----------+----------+----------+-----------+-----------+-----------+

**SW2-MSEL**

======== ======== ======== ========
ON       ON       ON       OFF
======== ======== ======== ========
**PIN1** **PIN2** **PIN3** **PIN4**
======== ======== ======== ========

**SW3- USR_DIPSW_FPGA**

======== ======== ======== ========
OFF      OFF      OFF      OFF
======== ======== ======== ========
**PIN1** **PIN2** **PIN3** **PIN4**
======== ======== ======== ========

**SW4**

============ ================= ================ =================
ON           OFF               OFF              ON
============ ================= ================ =================
**I2C FLAG** **DC_POWER CTRL** **FACTORY LOAD** **SECURITY MODE**
============ ================= ================ =================


| \*Download the ADI Linux Image (image_2021-07-28-ADI-Kuiper-full.zip) available under Old Releases Section from :doc:`ADI SD Card Images </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>`



- Program a blank SD card (at least 16 GB) with the downloaded image using the instructions in :doc:`Formatting and Flashing SD Cards using Windows </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>`

**NOTE:** Once the image is programmed eject the SD Card and re-insert it. The SD card will already include a few folders in its BOOT partition. Those can be ignored for this setup.*

::

   *For the SD card to boot correctly place the socfpga_stratix10_socdk.dtb and the u-boot.itb files provided in the SD card folder into the top-level directory (BOOT D:). In addition to this, also place one of the Image files either from the Dual 10G Image [for Synchronized 10G Mode] folder or the Single 20G Image [for Interleaved 20G Mode] folder into the top-level directory based on use case
   *Replace the SD Card on the Stratix10 SX SoC Board with the SD Card you just programmed.
   *Power up the boards and configure the signal generators as in the Signal Generators section above.
     *a. Start with low test signal power (about 0dBm). This can be adjusted later as desired.
     *b. For the reference clock signal set the generator power to 5dBm.
   *Setup the COM port connection to your PC
   *
     *a. Determine the USB-COM port connection to your PC by looking in the device manager under Ports (COM & LPT).

.. container:: centeralign

   \ |ad9213dual_quickstart_fig2_COM_port_setup.png|\


.. container:: centeralign

   \ *Figure 2. Setting up the COM port connection from the Stratix10 SX SoC board to the PC*\


::

   *
     *b. Once you determine the COM port connection, right click to open properties, and navigate to the Port Settings tab. In that tab change the Bits per second value to 115200. Click Ok to apply the new settings.

.. container:: centeralign

   \ |ad9213dual_quickstart_fig3_config_COM_port_settings.png|\


.. container:: centeralign

   \ *Figure 3. Configuring the COM port settings**NOTE:**\ This procedure needs to be performed every time the Stratix 10 board’s USB to mini-USB COM connection cable is physically disconnected and re-connected to the PC.*

::

   *Run PuTTY to establish communications
   *In the PuTTY Options page, specify:
     *a. Serial as the Connection Type
     *b. The COM port as determined (in the section above) as the serial line Note: The COM port number will depend on port availability on the user’s machine.
     *c. 115200 as the Speed
     *d. Save this configuration for quicker setup next power cycle

.. container:: centeralign

   \ |ad9213dual_quickstart_fig4_Open_COM_using_PuTTY.png|\


.. container:: centeralign

   \ *Figure 4. Opening the COM port connection using PuTTY*\


::

    *Program the Board using the Quartus Prime Programmer 19.3:
     *a. Start Quartus Prime Programmer 19.3
     *b. The software should be able to detect the Stratix10H SoC Evaluation Board automatically and it will show up in the Hardware Setup section on the top. If it does not show up automatically try to select it manually.
     *c. Once you see the board has been detected, click on 'Add File'.

.. container:: centeralign

   \ |ad9213dual_quickstart_fig5_Quartus_setup.png




.. container:: centeralign

   \ *Figure 5. Setting up the Quartus Programmer to program the FPGA Image*\


::

   *
     *d. Navigate to the location of the FPGA program (ADI provided) and select the file. (ad9213_dual_ebz_s10soc_hps_20_4.sof), and click 'Open'.

**NOTE:** It will take a few seconds for the file to add and the FPGA device to show up on the screen.*

::

   *
     *e. Click 'Start'.
     *f. Wait for the programmer to complete.

**NOTE:** The FPGA being programmed also triggers the Linux boot on the HPS. The PuTTY COM console provides updates on the progress of the boot.*

.. container:: centeralign

   \ |ad9213dual_quickstart_fig6_Using_Quartus_Programmer.png|\


.. container:: centeralign

   \ *Figure 6. Using the Quartus Programmer to program the FPGA Image*\


::

   *The PuTTY COMx console will display a verbose running of the initialization scripts at the end of which the setup will be ready

.. container:: centeralign

   \ |ad9213dual_quickstart_fig7_COM_console_process \_initialization.png|\


.. container:: centeralign

   \ *Figure 7. COM console once the boot process and initialization are complete*\


::

   *The IP address of the board can be obtained by running the ifconfig command in the console

.. container:: centeralign

   \ |ad9213dual_quickstart_fig8_Using_ifconfig_for_Stratix10_IP_address.png|\


.. container:: centeralign

   \ *Figure 8. Using ifconfig to obtain the IP address of the Stratix10 SX SoC board ethernet connection*\


::

   *Open PuTTY again to establish an SSH connection to the board. This connection allows you to control components on the board via SPI.

**NOTE:** This step is only needed if you need to perform SPI writes or reads to the board components using scripts when using Interleaved 20G Mode*

::

   *In the PuTTY Options page, specify:
     *i. SSH as the Connection Type
     *ii. IP address of the Stratix10 board, obtained in the previous step.
     *iii. Port number 22
     *iv. Save this configuration for quicker setup next time

.. container:: centeralign

   \ |ad9213dual_quickstart_fig9_Opening_SSH_connection.png|\


.. container:: centeralign

   \ *Figure 9. Opening an SSH connection to the Stratix10 SX SoC board using PuTTY*\


::

   *
     *v.   Login: root; Password: analog

.. container:: centeralign

   \ |ad9213dual_quickstart_fig10_SSH_login_successful.png|\


.. container:: centeralign

   \ *Figure 10. SSH connection after login ready to access the components on the board via SPI**NOTE:**\ An example script for when you are looking to use this scripting environment for SPI reads and writes can be provided.*

::

   *Run IIO Oscilloscope
     *a. Go to the Connect Tab, select manual, enter the IP address of the board prefaced by 'ip:' in the URL input box, and click refresh.

.. container:: centeralign

   \ |ad9213dual_quickstart_fig11_Setup_IIO_Scope.png|\


.. container:: centeralign

   \ *Figure 11. Setting up a connection to IIO Scope*\


::

   *
     *b. Once you click refresh all the IIO Devices on the Dual-9213 evaluation board including the two AD9213s and the other clock chips will show up. Click Connect.

.. container:: centeralign

   \ |ad9213dual_quickstart_fig12_IIO_Ready_to_Connect.png|\


.. container:: centeralign

   //Figure 12. All devices on evaluation board ready to connect to IIO Scope //


**NOTE:** These two steps only need to be done when using IIO Scope with a setup for the first time. The next time you open IIO Scope and are using the same setup it will auto-detect the setup and open the configuration and plotting windows.*

::

   *
     *c. After you connect a SPI Controller window and a Plotting window will open.
     *d. Use the SPI controller window to select a device you'd like to communicate with and then use the register section at the bottom to read or write individual registers.

**NOTE:** This only needs to be used if you are looking to do reads and writes in addition to the automatic startup configuration that has already been run.*

.. container:: centeralign

   \ |ad9213dual_quickstart_fig13_Read_Write_SPI_Registers.png|\


.. container:: centeralign

   //Figure 13. Using the IIO Scope Controller View to Read and Write SPI //


::

   *
     *e. Use the plotting window to capture data from one AD9213 at a time or from both simultaneously. The selection of the AD9213 and the number of samples can be made using the panels on the left. The tool allows both time domain and frequency domain captures.

**NOTE:** If the SD card image used is for the Interleaved 20G Mode, voltage 0 (channel 0) will represent data from both ad9213_0 and ad9213_1 as a combined waveform or a combined FFT*

.. container:: centeralign

   \ |ad9213dual_quickstart_fig14_Plot_separate_domain_outputs.png|\


.. container:: centeralign

   \ *Figure 14. Using the IIO Scope Plotting View to plot separate time domain outputs from each AD9213 (Ain = 136 MHz @5dBm)**NOTE:**\ Frequency domain plotting with more detailed analysis can be performed using a Visual Analog Canvas, the following are the steps to use VA*



- One-Time IIO Installations Before Running VisualAnalog (only needed if VisualAnalog Canvas provided by ADI will be used)
  - a. Install `libiio <https://wiki.analog.com/github.com/analogdevicesinc/libiio/releases>`_ (required for using iio Client block in VisualAnalog)
  - b. Install `IIO Plugin for VisualAnalog <https://wiki.analog.com/_media/wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/va_iiopluginsetup.zip>`_

Run Visual Analog For Synchronized 10G Mode

::

   *a. Go to the Existing Tab and browse to the location where you placed the ‘Dual9213_IIOScope_FFT.vac’ canvas. Select the canvas and click ‘open’.

.. container:: centeralign

   \ |ad9213dual_quickstart_fig15_Open_VisualAnalog_Canvas.png|\


.. container:: centeralign

   \ *Figure 15. Opening the Visual Analog Canvas to plot FFTs for the dual AD9213s [Synchronized 10G Mode]*\


::

   *b. Once the canvas is open, open the settings for the IIO Client module.
   *c. In the settings enter the IP address for the Stratix 10 SX SoC board, the sampling frequency, the sample size per AD9213 and enable both AD9213s. Once done click ‘ok’.

.. container:: centeralign

   \ |ad9213dual_quickstart_fig16_Setup_VA_for_dualAD9213.png|\


.. container:: centeralign

   \ *Figure 16. Setting up the VA Canvas for capture for the dual AD9213s [Synchronized 10G Mode]*\


::

   *d. The canvas is now ready to capture FFTs for each of the AD9213s, hit play to capture.
   *e. In addition to the FFT plot and its analysis the canvas also displays sample data for each AD9213.

.. container:: centeralign

   \ |ad9213dual_quickstart_fig17_VA_FFT_capture_data_analysis.png|\


.. container:: centeralign

   \ *Figure 17. VA canvas FFT capture, analysis and sample data for AD9213_0 (150.3MHz @14.90dBm)*\


For Interleaved 20G Mode

::

     *a.Go to the Existing Tab and browse to the location where you placed the ‘Dual9213_Interleaved20G_FFT’ canvas [for Interleaved 20G Mode]. Select the canvas and click ‘open’.
     *b. Once the canvas is open, open the settings for the IIO Client module.
     *c. In the settings enter the IP address for the Stratix 10 SX SoC board, set the sampling frequency to 20000, the sample size to 65536 and enable the datapath (shows up at Channel 0, but contains a sample interleaved stream of data from both AD9213). Once done click ‘ok’

**NOTE:** Before you are ready to capture the two AD9213s need to be gain and timing aligned and the sample clock to one AD9213 needs to be inverted with respect to the other*

::

    *d.  Use the instructions in the AD9213 Manual Calibration and Interleaving Guide to run the example scripts in the SSH connection environment you opened to the board to align and interleave
    *e.  The canvas is now ready to capture an FFT, hit play to capture
    *f.  In addition to the FFT plot and its analysis the canvas also displays sample data

.. |ad9213dual_quickstart_fig2_COM_port_setup.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig2_COM_port_setup.png
   :width: 600px
.. |ad9213dual_quickstart_fig3_config_COM_port_settings.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig3_config_COM_port_settings.png
   :width: 600px
.. |ad9213dual_quickstart_fig4_Open_COM_using_PuTTY.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig4_Open_COM_using_PuTTY.png
   :width: 600px
.. |ad9213dual_quickstart_fig5_Quartus_setup.png
| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig5_Quartus_setup.png
   :width: 600px
.. |ad9213dual_quickstart_fig6_Using_Quartus_Programmer.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig6_Using_Quartus_Programmer.png
   :width: 600px
.. |ad9213dual_quickstart_fig7_COM_console_process \_initialization.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig7_COM_console_process _initialization.png
   :width: 600px
.. |ad9213dual_quickstart_fig8_Using_ifconfig_for_Stratix10_IP_address.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig8_Using_ifconfig_for_Stratix10_IP_address.png
   :width: 600px
.. |ad9213dual_quickstart_fig9_Opening_SSH_connection.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig9_Opening_SSH_connection.png
   :width: 600px
.. |ad9213dual_quickstart_fig10_SSH_login_successful.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig10_SSH_login_successful.png
   :width: 600px
.. |ad9213dual_quickstart_fig11_Setup_IIO_Scope.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig11_Setup_IIO_Scope.png
   :width: 600px
.. |ad9213dual_quickstart_fig12_IIO_Ready_to_Connect.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig12_IIO_Ready_to_Connect.png
   :width: 600px
.. |ad9213dual_quickstart_fig13_Read_Write_SPI_Registers.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig13_Read_Write_SPI_Registers.png
   :width: 600px
.. |ad9213dual_quickstart_fig14_Plot_separate_domain_outputs.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig14_Plot_separate_domain_outputs.png
   :width: 600px
.. |ad9213dual_quickstart_fig15_Open_VisualAnalog_Canvas.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig15_Open_VisualAnalog_Canvas.png
   :width: 600px
.. |ad9213dual_quickstart_fig16_Setup_VA_for_dualAD9213.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig16_Setup_VA_for_dualAD9213.png
   :width: 600px
.. |ad9213dual_quickstart_fig17_VA_FFT_capture_data_analysis.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_dual_ebz/ad9213dual_quickstart_fig17_VA_FFT_capture_data_analysis.png
   :width: 600px
