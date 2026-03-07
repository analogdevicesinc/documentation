ADMX6001-EBZ: DC-Coupled 10GSPS Digitizer Evaluation Board
==========================================================

FEATURES
--------

Dual-path, low noise design for broad coverage from DC to 5GHz

-  High-speed path with AD9213, a low noise 12-bit ADC running at 10GSPS

   -  ADL5580, a fully differential 10GHz ADC driver

-  Precision path with AD4080, a 20-bit, 40MSPS, differential SAR ADC reduces 1/f noise

ADC driver input, biased with DAC output voltage, adjusts DC offset of unipolar signal

-  Single-ended unipolar signal with DC offset to differential signal conversion by ADL5580
-  ADL5580 biased by DAC LTC2664 output for maximizing AD9213 input dynamic range

FMC+ HSPC connector for interface with Xilinx VCU118 FPGA board

PACKAGE CONTENT
---------------

ADMX6001-EBZ board

AC-DC power supply, SDI65-12-UC-P6 (12V/65W)

ADDITIONAL EQUIPMENT NEEDED
---------------------------

Xilinx VCU118 FPGA evaluation board

A benchtop function generator

APPLICATION TOOLS AND DRIVER NEEDED
-----------------------------------

Vivado Lab Edition, 2024.2 or newer (Xilinx Vivado Lab Edition downloads)

Silicon Labs USB to UART Virtual COM Port Driver (Silicon Labs VCP Windows Driver)

Terminal Emulator (Tera Term 5.4.0)

IIO Oscilloscope (optional)

Python 3.11 or newer and the Python for ADI I/O devices (PyADI-IIO) library (optional)

Xilinx VCU118 programming files (admx6001_v1_boot.zip)

GENERAL DESCRIPTION
-------------------

The ADMX6001-EBZ is a reference design of a DC-coupled single channel 10GSPS digitizer featuring the AD9213, a low noise, 12-bit high-speed analog-to-digital converter (ADC) :adi:`AD9213` and the AD4080, a 20-bit precision ADC :adi:`AD4080`. The dual-path design achieves true low noise digitization in the broad band from DC to 5GHz. By biasing the ADC driver ADL5580 :adi:`en/products/adl5580`.html with the precision digital-to-analog converter (DAC) LTC2664 :adi:`en/products/ltc2664`.html, it is capable of handling unipolar and bipolar signals at various DC levels, maximizing utility of the input dynamic range of AD9213. This design is ideal for high performance time-domain instruments such as time-of-flight mass spectrometry (TOF MS), distributed fiber optic sensing (DFOS), and digital oscilloscope.

This document guides the setup and evaluation of the ADMX6001-EBZ board in conjunction with the Xilinx VCU118 field programmable gate array (FPGA) board.


|image1|

.. container:: centeralign

   *Figure 1. ADMX6001-EBZ board*


HARDWARE SETUP
--------------

The ADMX6001-EBZ board operates with Xilinx VCU118 FPGA board that serves as the controller for configuring the ADMX6001-EBZ board and streams captured data to a PC for post processing.

The hardware setup includes the following components:

-  ADMX6001-EBZ board (the power adapter is included in the ADMX6001-EBZ package)
-  Xilinx VCU118 FPGA board (the power adapter is included in the Xilinx VCU118 package)
-  2x Micro-USB cables
-  Ethernet cable
-  Signal generator
-  PC running Windows 10 or 11

The 12V power adapters for the ADMX6001-EBZ board and the Xilinx VCU118 FPGA board must be unplugged from the wall outlets before inserting into the barrel connector (P4) on the ADMX6001-EBZ board and the power connector on the Xilinx VCU118 FPGA board with the VCU118 power switch in the OFF position.

Figure 2 shows the connection of the ADMX6001-EBZ board to the Xilinx VCU118 FPGA board via a FMC+ connector and other cables for the connection of power supplies, USB, Ethernet, and the test signal from the signal generator. The Micro-USB cables and Ethernet cable are connected to the PC via a USB adapter if needed. An example of the complete setup is shown in Figure 3. A small bench-top fan is required for heat dissipation of the ADMX6001-EBZ board (refer to Figure 3).


|image2|

.. container:: centeralign

   *Figure 2. ADMX6001-EBZ board with VCU118 FPGA board*


   |image3|

.. container:: centeralign

   *Figure 3. Example of complete setup for ADMX6001-EBZ evaluation*


SOFTWARE SETUP
--------------

Download and install the following software to configure and evaluate the ADMX6001-EBZ board:

-  Xilinx Vivado or Vivado Lab Edition, https://www.xilinx.com/support/download.html
-  UART Terminal Tera Term, https://github.com/TeraTermProject/teraterm/releases
-  IIO Oscilloscope Download (see Note), :git-iio-oscilloscope:`releases`

Unless Xilinx Vivado has already been installed on your computer, it is recommended that you install the Vivado Lab Edition. Click Downloads and scroll down to the Vivado Lab Edition as highlighted in Figure 4 to download and install the Vivado Lab Edition. The default installation path for the Vivado Lab Edition is \*\* C:\\Xilinx\\Vivado_Lab\\2024.2\\bin \*\* where \*\* 2024.2 \*\* indicates the version. The path name needs to be revised accordingly if a different version of the Vivado Lab Edition is installed. The UART Terminal Tera Term is for monitoring the booting process and then logging in to the Xilinx VCU118 system.

Note: IIO Oscilloscope is optional for configuring the ADMX6001-EBZ board and visualizing/saving the captured data. Alternately, you can use Python scripts to configure the ADMX6001-EBZ board and plot/save the captured data.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure4_downloadvivado.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   *Figure 4. Download the Vivado Lab Edition for Windows*


PROGRAM THE XILINX VCU118 BOARD
-------------------------------

The programming files for Xilinx VCU118 FPGA are provided as a .zip file. Unzip the files to a working folder for all of the required files.

Refer to the Hardware Setup section. The 12V power adapters to both the ADMX6001-EBZ board and the Xilinx VCU118 FPGA board must be unplugged from the wall outlets before turning on the boards.

\*\* Turn on the boards sequentially. \*\* First, make sure that the connection of the 12V power adapter output to the barrel connector (P4) on the ADMX6001-EBZ board is securely in place, then turn on the ADMX6001-EBZ board by plugging in the 12V power supply to the wall outlet. The DS10 and DS11 on the same edge as the barrel connector on the ADMX6001-EBZ board must be lit. Otherwise, unplug the 12V power adapter from the wall outlet and wait for about 10 seconds before plugging the 12V power supply back to the wall outlet. Second, make sure that the power switch on the Xilinx VCU118 board is in the OFF position and the output of the 12V power supply is securely in place. Plug in the 12V power adapter for the Xilinx VCU118 board to the wall outlet, then turn on the Xilinx board by turning the power switch to the ON position. Refer to Figure 2 for the Xilinx VCU118 board power supply connector and switch.

Before programming the Xilinx VCU118 board, it is important to configure Ethernet to an IP 192.168.2.xx where xx can be any number between 2 and 255. If a USB adapter with Ethernet port is used, plug in the USB adapter before reviewing and/or configuring the IP address.

Follow these steps to configure the Ethernet IP address:

-  Control Panel > Network and Sharing Center > click Ethernet to open the Ethernet Status window, as shown in Figure 5.
-  Click Properties to open the Ethernet Properties window, as shown in Figure 6.
-  Select Internet Protocol Version 4 (TCP/IP), as shown in Figure 7.
-  Click Properties to open the Internet Protocol Version 4 (TCP/IPv4) Properties window, as shown in Figure 7.
-  Review/change IP address, as shown in Figure 8.

|image4|

.. container:: centeralign

   *Figure 5. Review and Change Ethernet IP Address—Network and Sharing Center*


   |image5|

.. container:: centeralign

   *Figure 6. Review and Change Ethernet IP Address—Ethernet Properties*


   |image6|

.. container:: centeralign

   *Figure 7. Review and Change Ethernet IP Address—TCP/IPv4*


   |image7|

.. container:: centeralign

   *Figure 8. Review and Change Ethernet IP Address—Internet Protocol Version 4 (TCP/IPv4) Properties*


Find the UART COM port of the Xilinx VCU118 board by opening Device Manager and expanding Ports (COM & LPT). Locate Silicon Labs Dual CP2105 USB to UART Bridge Standard COM Port (COMx) to get the COM port number for the Tera Term serial terminal connection, as shown in Figure 9. The user may need to update the CP210x USB to UART Bridge VCP drivers.



|image8|

.. container:: centeralign

   *Figure 9. Find UART COM Port Number*


.. _program-the-xilinx-vcu118-board-1:

PROGRAM THE XILINX VCU118 BOARD
-------------------------------

Program the board using Vivado Lab tool with xsdb, as shown in Figure 10, by completing the following:

1. Open a Command Prompt window and go to the working folder where the programming files for Xilinx VCU118 FPGA are located.

2. Start xsdb.bat (for Vivado Lab Edition). The prompt should change to \*\* xsdb% \*\* .

**C:\\Xilinx\\Vivado_Lab\\2024.2\\bin\\xsdb.bat**

3. Program the VCU118 FPGA board.

**xsdb% source run.tcl**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure10.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   *Figure 10. Xilinx VCU118 Programming with Vivado Lab*


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure11.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   *Figure 11. Xilinx VCU118 Programming with Vivado Lab: xsdb%*


While programming the Xilinx VCU118 is in progress, open and start the serial terminal Tera Term session to observe the boot process and log in to the Xilinx VCU118 as shown in Figure 12 through Figure 14.

1. Start and connect the serial terminal Tera Term session using the COM port found previously.

2. In Tera Term, click Setup > Serial port … to set the speed to 115200.

3. Continue monitoring the Xilinx VCU118 boot process. Once the process is complete, log in with the following information:

Login: **root**

Password: **analog**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure12.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   *Figure 12. Serial Terminal Tera Term Session for Monitoring Xilinx VCU118 Booting and Login—Tera Term: New Connection*


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure13.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   *Figure 13. Serial Terminal Tera Term Session for Monitoring Xilinx VCU118 Booting and Login—Tera Term: Change Speed*


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure14.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   *Figure 14. Xilinx VCU118 Booting and Login—Tera Term: Login*


**Note the following:**

♦ For the Xilinx Vivado Lab version, only xsdb.bat is available (C:\\Xilinx\\Vivado_Lab\\2024\\bin\\xsdb.bat).

♦ It is required to program the Xilinx VCU118 board twice in the Vivado Lab window.

1. Run **source run.tcl** and wait for the login message to appear in the Tera Term window.

2. Run **source run.tcl** a second time. Observe the boot process in the Tera Term window and log in.

If using Python scripts is preferred, skip the Configure and Control the ADMX6001-EBZ With IIO Oscilloscope section and the ADMX6001-EBZ Data Acquisition With IIO Oscilloscope section, and go directly to the Configure and Control ADMX6001-EBZ With Python Scripts section.

CONFIGURE AND CONTROL THE ADMX6001-EBZ WITH IIO OSCILLOSCOPE
------------------------------------------------------------

Refer to the IIO Oscilloscope wiki page (:doc:`/wiki-migration/resources/tools-software/linux-software/iio_oscilloscope`) for guidance.

CONNECT TO XILINX VCU118 + ADMX6001-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Xilinx VCU118 board uses a static IP address, **192.168.2.1**. Launch the IIO-Oscilloscope application and go to Settings > Connect. In the popup window, connect to Xilinx VCU118 with manual URI **ip:192.168.2.1**, as shown in Figure 15.

Once the IIO device is connected, the user can read/write registers and view the plot of captured data, as shown in Figure 16 and Figure 17.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure15.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   *Figure 15. Launch IIO Oscilloscope and Connect to Xilinx VCU118*


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure16.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   *Figure 16. IIO Oscilloscope Window for Register Write/Read*


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure17.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   *Figure 17. IIO Oscilloscope Plot Window*


CONFIGURE THE AD9213 HIGH-SPEED PATH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set the following registers for the AD9213 high-speed path, as shown in Figure 18 through Figure 21.

-  ad9213 Register 0x1617 set to 0x01, as shown in Figure 18.
-  ad9213 Register 0x1601 set to 0x01, as shown in Figure 19.
-  ltc2664_clr set to 1, as shown in Figure 20.
-  adl5580_en set to 1, as shown in Figure 21.

The AD9213 high-speed path is ready for capturing data.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure18.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   *Figure 18. Register Settings for the AD9213 High-Speed Path Register 0x1617*


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure19.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   *Figure 19. Register Settings for the AD9213 High-Speed Path Register 0x1601*


   |image9|

.. container:: centeralign

   *Figure 20. Register Settings for the AD9213 High-Speed Path ltc2664_clr*


   |image10|

.. container:: centeralign

   *Figure 21. Register Settings for the AD9213 High-Speed Path adl5580_en*


CONFIGURE THE AD4080 PRECISION PATH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before capturing the AD4080 precision path data with the IIO Oscilloscope, a few registers need to be set, as shown in Figure 22 through Figure 25.

-  ltc2664_clr set to 1 (also required for the AD9213 high-speed path)
-  ltc2664 output_voltage1 raw value set to 49152
-  ltc2664 output_voltage2 raw value set to 36045
-  ada4945_disable (one-bit-adc-dac -> output_voltage3) set to 1
-  adg5419_ctrl (one-bit-adc-dac -> output_voltage4) set to 1

|image11|

.. container:: centeralign

   *FFigure 22. Register Settings for the AD4080 Precision Path: ltc2664_output_voltage1*


   |image12|

.. container:: centeralign

   *Figure 23. Register Settings for the AD4080 Precision Path: ltc2664_output_voltage2*


   |image13|

.. container:: centeralign

   *Figure 24. Register Settings for the AD4080 Precision Path: ada4945_disable*


   |image14|

.. container:: centeralign

   *Figure 25. Register Settings for the AD4080 Precision Path: adg5419_ctrl*


AD4080 DATA INTERFACE CONFIGURATION REGISTERS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD4080 low voltage differential signaling (LVDS) data interface is highly configurable. In the ADMX6001-EBZ design, the AD4080 is configured to output the result data on single data lane. The AD4080 data interface configuration Register 0x15 and Register 0x16 need to be configured so that the Xilinx VCU118 controls are aligned with AD4080 conversion data for correct data output.

Complete the following steps for setting the AD4080 data interface configuration registers:

-  AD4080 Register 0x15 set to 0x50 to enable the fixed pattern test, as shown in Figure 26. This step sets AD4080 in test mode.
-  In test mode, the 20-bit AD4080 data is expected to be binary 1010 1100 0101 1101 0110, decimal −342570, or hexadecimal 0xAC5D6. Save the AD4080 data to a .csv file in IIO Oscilloscope and check the value. Refer to the ADMX6001-EBZ Data Acquisition With IIO Oscilloscope section for saving data in IIO Oscilloscope.
-  If the AD4080 data is different from the expected decimal −342570, set the AD4080 Register 0x15 to one of the following values: 0x51, 0x61, 0x71, 0x81, 0x91, 0x01, 0x11, 0x21, 0x31, or 0x41, as shown in Figure 27. Save the data to a .csv file and check the value. Repeat this step with a value in the list until the AD4080 data is exactly −342570. The AD4080 register setting is completed.
-  Set AD4080 Register 0x15 back to 0x40 to disable the fixed pattern test and enable AD4080 normal mode.

The AD4080 data interface configuration registers are set and the AD4080 is ready for data acquisition.


|image15|

.. container:: centeralign

   *Figure 26. AD4080 Register 0x15 Setting—Value 0x50 for Fixed Test Pattern and 0x40 for Normal Data Acquisition Mode*


   |image16|

.. container:: centeralign

   *Figure 27. AD4080 Register 0x16 Setting*


IIO-OSCILLOSCOPE PLOT WINDOW
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data captured by the the AD9213 high-speed path and the AD4080 precision path can be visualized and saved to a .csv file in the IIO Oscilloscope plot window, as shown in Figure 28 and Figure 29.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure27.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   *Figure 28. IIO Oscilloscope Plot Window—Time Domain: axi-adrv9213-rx-hpc*


   |image17|

.. container:: centeralign

   *Figure 29. IIO Oscilloscope Plot Window—Time Domain: ad4080*


The two data paths are listed in the top-left corner. Check one or both and then click the Capture/Stop button to view the data stream. For the IIO Oscilloscope to work smoothly, it is recommended that the number of samples is set to power of 2, such as 2\ :sup:`10` (1024) or 2\ :sup:`16` (65536). The IIO Oscilloscope supports only one scale for each axis so that it is not practical to view the AD9213 high-speed path and the AD4080 precision path simultaneously because the AD9213 (10GSPS) high-speed path is 320 times faster than the AD4080 (31.25MSPS) precision path for the horizontal axis and AD4080 (20-bit) has higher bit resolution than AD9213 (12-bit) for the vertical axis in the ADMX6001-EBZ design.

The IIO Oscilloscope plot window can also view the captured data in the frequency domain. An example of a 2MHz sinewave captured by AD4080 is shown in Figure 30.


|image18|

.. container:: centeralign

   *Figure 30. IIO Oscilloscope Plot Window—Frequency Domain*


The data can be saved in a .csv file for post processing and analysis, as shown in Figure 31. From the File menu, select Save As to open the Save As window. Make sure to select the path from the dropdown list and select the correct checkbox before clicking the Save button on bottom-right.



|image19|

.. container:: centeralign

   *Figure 31. Save Data as a .CSV File in the IIO Oscilloscope Plot Window*


INPUT SIGNAL OFFSET SHIFT FOR AD9213
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The input signal is often from transducers or sensors as a unipolar signal with DC offset, whereas the AD9213 works best with differential input. By biasing the ADL5580 input terminal with the output of the precision DAC LTC2664, the ADL5580 converts the unipolar signal to a differential signal with an adjustable DC offset to maximize the utility of the AD9213 input dynamic range. The actual use case may vary depending on the specific application.

The DAC value of 32768 corresponds to 0V and is used as the default biasing to ADL5580. To achieve a targeted DC offset shift **x** mV, the DAC value can be calculated as

DAC value = 32768×(1 + **x** /5000)

where **x** is the DC offset in mV.

Round the DAC value to the nearest integer as the DAC LTC2664 input. The DAC output range is −5V to +5V.

To change the LTC2664 DAC value for ADL5580 biasing, write the DAC value as raw data to output_voltage0, as shown in Figure 32. To illustrate the effect of offset shift, clear the Auto scale checkbox, set the Y max to 2048, and set the Y min to −2048. Figure 33 through Figure 35 show the AD9213 high-speed path data with the same sinewave input but different DAC settings for offset shift.


|image20|

.. container:: centeralign

   *Figure 32. Write DAC Value of Targeted Voltage to LTC2664*


   |image21|

.. container:: centeralign

   *Figure 33. AD9213 Data with DC Offset at 0mV (32768 LSBs)*


   |image22|

.. container:: centeralign

   *Figure 34. AD9213 Data with DC Offset at +100mV (33423 LSBs)*


   |image23|

.. container:: centeralign

   *Figure 35. AD9213 Data with DC Offset at −100mv (32112 LSBs)*


CONFIGURE AND CONTROL ADMX6001-EBZ WITH PYTHON SCRIPTS
------------------------------------------------------

Utilizing Python scripts offers advantages for configuring and controlling the ADMX6001-EBZ board and enables data visualization and processing. Python scripts are more efficient than the manual register read and write with IIO Oscilloscope. The Python virtual environment (venv) for running ADMX6001-EBZ Python scripts can be set with or without an IDE such as PyCharm. It is required that the user installs Python 3.11.5 or a newer version and downloads the PyADI-IIO library before proceeding to the venv setting in the following section.

INSTALL PYTHON AND GIT FOR WINDOWS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

► Download Windows Installer (64-bit), as shown in Figure 36.

Install Python 3.11.5. It is recommended to install Python 3.11.5 as an administrator by right clicking on the installer, as shown in Figure 37.

► Download the 64-bit Git for Windows Setup as shown in Figure 38 and install Git.


|image24|

.. container:: centeralign

   *Figure 36. Download Python Windows Installer*


   |image25|

.. container:: centeralign

   *Figure 37. Install Python 3.11.5 as an Administrator*


   |image26|

.. container:: centeralign

   *Figure 38. Download 64-bit Git for Windows Setup*


DOWNLOAD THE PYADI-IIO LIBRARY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start a Command Prompt window and clone the PyADI-IIO library for ADMX6001-EBZ, as shown in Figure 39.

► Create and navigate to the folder for saving the PyADI-IIO library,

**mkdir temp1 > cd temp1 > mkdir pyadi > cd pyadi**

► Clone the required PyADI-IIO library from the GitHub website,

**git clone** :git-pyadi-iio:`tree/admx6001_v1`


|image27|

.. container:: centeralign

   *Figure 39. Clone PyADI-IIO Library for the ADMX6001-EBZ Evaluation Board*


CREATE AND CONFIGURE PYTHON VENV FOR THE ADMX6001-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The venv module supports creating lightweight virtual environments, each with their own independent set of Python packages installed in the site directories of the virtual environments. The venv contains a specific Python interpreter, software libraries, and binaries that are needed to support a project (library or application).

Complete the following steps to create and activate the venv for ADMX6001-EBZ and install the libraries:

-  Create a folder and copy the Python scripts to this folder, in the example that follows C:\\ADMX6001_PythonScripts.

-  Open a Command Prompt window and go to the Python 3.11 folder ( C:\\Python311 in the following example).

-  To create the venv in the Command Prompt window run the following script: python -m venv c:\\ADMX6001_Python-Scripts\\myenv.

-  Activate the venv. Go to C:\\ADMX6001_PythonScripts\\myenv\\Scripts>activate. Notice the prompt changes to (myenv), indicating the venv is activated.

-  In the (myenv) command window, install the PyADI-IIO library. Go to the PyADI-IIO library folder (C:\\temp1\\pyadi\\pyadi-iio in the example) and install pyadi-iio library: pip install.

The venv is now created and activated, and the PyADI-IIO library is installed, as shown in Figure 40.


|image28|

.. container:: centeralign

   *Figure 40. Create and Activate the Venv and Install the PyADI-IIO library for the ADMX6001-EBZ Evaluation Board*


The user can also setup the venv for ADMX6001-EBZ with an integrated development environment (IDE) such as PyCharm. To create and activate the venv, complete the following:

-  Launch PyCharm and open the ADMX6001_Pythonscripts project, as shown in Figure 41.
-  Navigate to File > Settings > Project > Python interpreter,click Add Interpreter > Add Local Interpreter to create the venv, as shown in Figure 42 through Figure 44.
-  The user can add additional Python libraries in a Command Prompt window (see the Install Additional Python Libraries section) or in PyCharm, as shown in Figure 45 and Figure 46.
-  Launch a Command Prompt window to activate venv and install the PyADI-IIO, as shown in Figure 47.

|image29|

.. container:: centeralign

   *Figure 41. Launch PyCharm and Open the Python Scripts Project*


   |image30|

.. container:: centeralign

   *Figure 42. Open File or Project*


   |image31|

.. container:: centeralign

   *Figure 43. ADMX6001-EBZ Python Scripts*


   |image32|

.. container:: centeralign

   *Figure 44. Create Venv by Adding a Local Interpreter*


   |image33|

.. container:: centeralign

   *Figure 45. Install Additional Python Libraries in PyCharm*


   |image34|

.. container:: centeralign

   *Figure 46. Python Interpreter Settings*


   |image35|

.. container:: centeralign

   *Figure 47. Activate Venv and Install PyADI-IIO*


This completes the Python venv for running Python scripts for the ADMX6001-EBZ board.

INSTALL ADDITIONAL PYTHON LIBRARIES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Python scripts for the ADMX6001-EBZ board utilize modules from various libraries. Install these libraries, such as scipy and matplotlib, using pip install <library name> within venv before running the Python scripts, as shown in Figure 48.


|image36|

.. container:: centeralign

   *Figure 48. Install Additional Libraries and Run Python Scripts for ADMX6001-EBZ Evaluation Board*


The Python scripts call modules in the PyADI-IIO library to initialize the ADMX6001-EBZ board by setting required registers, JSED and LVDS data lanes, and other control signals. Examples of Python scripts can be found at the product page for the ADMX6001-EBZ.

RUN EXAMPLE PYTHON SCRIPTS FOR THE ADMX6001-EBZ
-----------------------------------------------

Examples of Python scripts are provided on the ADMX6001-EBZ board product page for board evaluation. These Python scripts call modules in the PyADI-IIO library to initialize the ADMX6001-EBZ board by setting required registers, JSED and LVDS data lanes, and other control signals. The user is encouraged to check the product page of the ADMX6001-EBZ board for updated and/or additional examples of Python scripts.

The example script **ADMX6001_MultiClass_pCal.py** defines the classes to setup, initiate, configure, and operate the ADMX6001-EBZ for data acquisition and visualization. A list of useful methods defined in this script for operating the setup of the ADMX6001-EBZ board and the Xilinx VCU118 board follows.

-  AD4080_CAl(self): configure the AD4080 LVDS data interface, Register 0x15 and Register 0x16, for correct data output.

-  set_dac_offset(self, voltage): set the DC offset in mV for the AD9213 path. By setting the appropriate DC offset, the signal can be moved up or down for maximizing the dynamic range of the AD9213.

-  capture_data_ad9213(self, nsamples): the AD9213 captures data of nsamples at 10GSPS.

-  capture_data_ad4080(self, nsamples): the AD4080 captures data of nsamples at 31.25MSPS.

-  plot_data_ad9213(self, data): plot data captured by the AD9213.

-  plot_data_ad4080(self, data): plot data captured by by AD4080.


|image37|

.. container:: centeralign

   *Figure 49. Run the Python Script ADMX6001_acquisition.py to Acquire and Visualize Data*


The example script **ADMX6001_acquisitionl.py** creates instance of classes defined in ADMX6001_multiClass_pCal.py and calls the methods to initialize the ADMX6001-EBZ board, calibrate the AD4080 LVDS data interface, and perform data acquisition. Figure 50 through Figure 52 show the plots that the Python script **ADMX6001_acquisition.py** generated.



|image38|

.. container:: centeralign

   *Figure 50. Plots Generated by Python Script ADMX6001_acquisition.py*


   |image39|

.. container:: centeralign

   *Figure 51. AD9213 Data with Different DC Offsets*


   |image40|

.. container:: centeralign

   *Figure 52. AD4080: Data and AD4080: Spectrum*


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure1_admx6001.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure2_boards.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure3_completesetup.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure5_ip_network.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure6_ip_properties.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure7_ip_tcpip.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure8_ip_ipreview.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure9_uart.jpg
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure20.jpg
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/ajaxperflookupdelay/figure21_added.jpg
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure21.jpg
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure22.jpg
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure23.jpg
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure24.jpg
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure25.jpg
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure26.jpg
   :width: 600px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure28.jpg
   :width: 600px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure29.jpg
   :width: 600px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure30.jpg
   :width: 600px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure31.jpg
   :width: 600px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure32.jpg
   :width: 600px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure33.jpg
   :width: 600px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure34.jpg
   :width: 600px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure35.jpg
   :width: 600px
.. |image25| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure36.jpg
   :width: 600px
.. |image26| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure37.jpg
   :width: 600px
.. |image27| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure38.jpg
   :width: 600px
.. |image28| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure39.jpg
   :width: 600px
.. |image29| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure40.jpg
   :width: 600px
.. |image30| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure41.jpg
   :width: 600px
.. |image31| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure42.jpg
   :width: 600px
.. |image32| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure43.jpg
   :width: 600px
.. |image33| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure44.jpg
   :width: 600px
.. |image34| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure45.jpg
   :width: 600px
.. |image35| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure46.jpg
   :width: 600px
.. |image36| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure47.jpg
   :width: 600px
.. |image37| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure48.jpg
   :width: 600px
.. |image38| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure49.jpg
   :width: 600px
.. |image39| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure50.jpg
   :width: 600px
.. |image40| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/figure51.jpg
   :width: 600px
