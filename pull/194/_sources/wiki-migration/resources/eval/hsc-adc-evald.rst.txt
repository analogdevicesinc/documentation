HSC-ADC-EVALDZ HIGH SPEED ADC CONVERTER EVALUATION PLATFORM
===========================================================

<fc #ff0000>**\* Please note the HSC-ADC-EVALDZ is obsolete and no longer manufactured or supported by Analog Devices. All active High Speed ADC Products previously using the HSC-ADC-EVALDZ have been redesigned to interface to the newer FMC-based HSC-ADC-EVALEZ Evaluation Platform \***</fc>

Preface
-------

| This user guide describes the :adi:`HSC-ADC-EVALDZ <hsadcevalboard>` JESD-204B Data Capture eval board. The application software tools used to interface with the product specific ADC Eval boards are also described.
| The product specific ADC data sheets provide additional information and should be consulted when using the evaluation board. All documents and software tools are available at :adi:`High Speed ADC Eval Boards <hsadcevalboard>`. For additional information or questions, send an email to highspeed.converters@analog.com.

Product Highlights
------------------

1. Easy to Set Up. Connect the included power supply along with the CLK and AIN signal sources to the two evaluation boards. Then connect to the PC via the USB port and use the ADI provided software tools to evaluate the ADC performance.

2. USB Port Connection to PC. PC interface is via a USB 2.0 connection (1.1 compatible) to the PC. A USB cable is provided in the kit.

3. 256 kB FIFO. The on-board FPGA contains an integrated FIFO to store data captured from the ADC for subsequent processing.

4. Support for eight (8) JESD-204B Lanes up to 6.25 Gbps. Up to 644 MSPS SDR/1.2 GSPS DDR Encode Rates on Each of Two Parallel Channels.

5. Supports ADCs with Serial Port Interface (SPI). Some ADCs include a feature set that can be changed via the SPI. The ADC capture board supports these SPI-driven features through the existing USB connection to the computer without additional cabling.

6. VisualAnalog™. VisualAnalog supports the HSC-ADC-EVALD hardware platform as well as enabling virtual ADC evaluation using ADIsimADC™, Analog Devices proprietary behavioral modeling technology. This allows rapid comparison between multiple ADCs, with or without hardware evaluation boards. For more information, see AN-737 at www.analog.com/VisualAnalog.

Typical Data Capture Setup
--------------------------

.. container:: centeralign

   \


   |image1|

.. container:: centeralign

   \ *Figure 1.* :adi:`AD9250 ADC Eval Brd (left) connected to HSC-ADC-EVALDZ (right) <hsadcevalboard>`


Features
--------

-  Xilinx Virtex-6 FPGA-based buffer memory board used for capturing digital data from high speed JESD-204B ADC evaluation boards to simplify evaluation
-  256 kB FIFO depth
-  Support for up to eight (8) 6.25 Gbps JESD-204B Lanes
-  Parallel input at 644 MSPS SDR and 1.2 Gbps DDR
-  Supports 1.2V, 1.8 V, 2.5 V CMOS, LVDS, and JESD204B interfaces
-  Supports multiple ADC channels
-  Measures performance with VisualAnalog™

   -  Real-time FFT and time domain analysis
   -  Analyzes SNR, SINAD, SFDR, and harmonics

-  Simple USB port interface (2.0)
-  Supports ADCs with serial port interfaces (SPI)
-  FPGA reconfigurable via JTAG or USB
-  On-board regulator circuit speeds setup
-  12V, 3 A switching power supply included
-  Compatible with Windows XP-Service Pack 3-32bit, Windows Vista-Service Pack 1-32&64bit, Windows 7-32&64bit

Helpful Documents
-----------------

-  :adi:`AN-905 Application Note <an-905>`, *VisualAnalog Converter Evaluation Tool Version 1.0 User Manual*
-  :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control Software*
-  :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*
-  :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and Evaluation*

Design and Integration Files
----------------------------

-  Schematic, `hadv6fpga01d.sch.1.pdf <https://wiki.analog.com/_media/resources/eval/hadv6fpga01d.sch.1.pdf>`_
-  Gerbers, `hadv6fpga01d.zip <https://wiki.analog.com/_media/resources/eval/hadv6fpga01d.zip>`_
-  BOM, `hsc_adc_evaldz_bomwiki.xlsx <https://wiki.analog.com/_media/resources/eval/hsc_adc_evaldz_bomwiki.xlsx>`_

===== Equipment Needed =====

-  Analog signal source and antialiasing filter
-  Low jitter ADC sample clock source (if not using the on-board oscillator)
-  High speed ADC evaluation board and ADC data sheet
-  Switching power supply (12.0 V, 3 A, provided)
-  PC running Windows®
-  Latest version of VisualAnalog and SPI Controller Software
-  USB 2.0 port

Evaluation Board Description
----------------------------

The Analog Devices, Inc. high speed converter evaluation platform (HSC-ADC-EVALDZ) utilizes the latest version of VisualAnalog and an FPGA-based buffer memory board to capture blocks of digital data from the Analog Devices high speed analog-to-digital converter (ADC) evaluation boards. The ADC capture board is connected to the PC through a USB port and is used with VisualAnalog to quickly evaluate the performance of high speed ADCs. Users can view an FFT for a specific analog input and encode rate to analyze SNR, SINAD, SFDR, and harmonic information.

The ADC capture board is easy to set up. Additional equipment needed includes an Analog Devices high speed ADC evaluation board, a signal source, and a clock source. Once the kit is connected and powered, the evaluation is enabled instantly on the PC.

The ADC capture board enables numerous expansion and evaluation possibilities by virtue of its powerful reconfigurable FPGA core.

The system can acquire JESD-204B digital data at speeds up to 6.25 Gbps. The FPGA contains an integrated FIFO memory that allows capture of data record lengths up to a total of 256 kB. A USB 2.0 microcontroller communicating with VisualAnalog allows for easy interfacing to computers using the USB 2.0 interface.

The HSC-ADC-EVALDZ capture board provides all of the support circuitry required to accept eight lanes of JESD-204B data, as well as two 18-bit channels from an ADC’s parallel CMOS or LVDS outputs. When using the HSC-ADC-EVALDZ in conjunction with an ADC evaluation board, it is critical that the signal sources used for the ADC board’s analog input and clock have very low phase noise (<1 ps rms jitter) to achieve the ultimate performance of the converter. Proper filtering of the analog input signal to remove harmonics and lower the integrated or broadband noise at the input is also necessary to achieve the specified noise performance.

Evaluation Board Hardware
-------------------------

EASY START Requirements
~~~~~~~~~~~~~~~~~~~~~~~

-  HSC-ADC-EVALDZ ADC capture board, VisualAnalog, 12 V wall transformer, and USB cable
-  High speed ADC evaluation board and ADC data sheet
-  Power supply for ADC evaluation board
-  Analog signal source and appropriate filtering
-  Low jitter clock source applicable for specific ADC evaluation, typically <1 ps rms jitter
-  PC running Windows®
-  PC with a USB 2.0 port

EASY START Steps
~~~~~~~~~~~~~~~~

**Important Note**\ Administrative rights for the Windows operating systems are needed during the entire software installation procedure. Completion of every step before reverting to a normal user mode is recommended.

1. Download and Install VisualAnalog. For the latest updates to the software, check the Analog Devices website at :adi:`High Speed ADC Eval Boards <hsadcevalboard>`.

2. Connect the ADC capture board to the ADC evaluation board. If an adapter is required, insert the adapter between the ADC evaluation board and the ADC capture board.

3. Connect the provided USB cable to the ADC capture board and to an available USB port on the computer.

4. The ADC capture board is supplied with a wall mount switching power supply. Connect the supply end to an ac wall outlet rated for 100 Vac to 240 Vac at 47 Hz to 63 Hz. The other end is a 2.1 mm inner diameter jack that connects to the PCB at P1301. The supply is fused and conditioned before connecting to the regulators that supply the proper bias to the entire HSC-ADC-EVALDZ capture board.

5. Once the USB cable is connected to both the computer and the HSC-ADC-EVALDZ board, and power is applied, the USB driver starts to install. The Found New Hardware Wizard opens and prompts you through the automated install process.

6. (Optional) Verify in the Windows device manager that Analog Devices HADV6 is listed under the USB hardware.

7. Refer to the instructions included in the respective ADC data sheet found at www.analog.com for more information about connecting the ADC evaluation board’s power supply and other requirements. After verification of power supply connections, apply power to the ADC evaluation board and check the voltage levels on the ADC board to make sure they are correct.

8. Make sure the evaluation boards are powered on before connecting the analog input and clock. Connect the appropriate analog input (which should be filtered with a band-pass filter) and low jitter clock signal.

| 9. Refer to the VisualAnalog User Manual at :adi:`High Speed ADC Eval Boards <hsadcevalboard>` for detailed software operating instructions.

HSC-ADC-EVALD Supported ADC Evaluation Boards
---------------------------------------------

| Refer to the Analog Devices High Speed ADC capture board product page at :adi:`High Speed ADC Eval Boards <hsadcevalboard>` for a table of HSC-ADC-EVALD compatible ADC evaluation boards.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ad9250connections.png
   :width: 600px
