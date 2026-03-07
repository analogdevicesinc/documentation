User Guide for the AD7944/AD7985/AD7986, 14-/16-/18-Bit PulSAR® ADCs
====================================================================

Features
--------

-  **Full-featured evaluation board for the** :adi:`AD7944`\ **/**\ :adi:`AD7985`\ **/**\ :adi:`AD7986`
-  \**PC Control in conjunction with the converter and evaluation development board :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>` \*\*
-  **PC software for control and data analysis of time and frequency domain**
-  **Versatile analog signal conditioning circuitry**
-  **On-board reference, clock oscillator, and buffers**
-  **Standalone capability**

.. image:: https://wiki.analog.com/_media/resources/eval/10387-001.jpg
   :align: right
   :width: 600px

System Requirements
~~~~~~~~~~~~~~~~~~~

-  Windows XP SP2
-  Windows Vista
-  Windows 7
-  USB 2.0 Port

Software needed
~~~~~~~~~~~~~~~

-  Enclosed CD or available via Website download

Evaluation Kit Contents
~~~~~~~~~~~~~~~~~~~~~~~

-  Evaluation board (as ordered EVAL-AD7944EDZ, EVAL-AD7985EDZ, or EVAL-AD7986EDZ)
-  Software CD

Documents required
~~~~~~~~~~~~~~~~~~

-  :adi:`AD7944` data sheet
-  :adi:`AD7985` data sheet
-  :adi:`AD7986` data sheet

Equipment required
~~~~~~~~~~~~~~~~~~

-  Precision source

   -  DC source (low noise for checking different input ranges)
   -  AC source (low distortion).

-  Band-pass filter suitable for 16-bit or 18-bit testing (value based on signal frequency).
-  SMB cable
-  Evaluation converter evaluation and development board, :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>`.
-  World-compatible 7 V dc supply (enclosed with :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>`)

General Description
===================

The EVAL-AD79XXEDZ is an evaluation board for the 20-lead :adi:`AD7944` (14-bit), :adi:`AD7985` (16-bit), and :adi:`AD7986` (18-bit) PulSAR® analog-to-digital converters (ADCs). On-board components include a high precision, buffered band gap 5.0 V reference (:adi:`ADR435`), reference buffers (:adi:`AD8032`), a signal conditioning circuit with two op amps (:adi:`AD8021`), and an FPGA for deserializing the serial conversion results. The evaluation board interfaces to the CED capture board by using a 96-pin DIN connector. In addition, SMB connectors, J1 and J2, are provided for the low noise analog signal source.

Quickstart
==========

-  Install the software from the enclosed CD or by downloading from the Analog Devices, Inc., Website, at www.analog.com.

   -  Ensure the evaluation board is disconnected from the USB port of the PC while installing the software.
   -  A PC restart may be required after installation.

-  Connect the EVAL-CED1Z board to the evaluation board as shown in Figure 2.
-  Connect the power supply adapter included in the kit to Connecter J4 on the :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>` board.
-  Connect the EVAL-CED1Z board to the PC via the USB cable.

   -  Choose to automatically search for the drivers for the :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>` board if prompted by the operating system.
   -  For Windows® XP, you may need to search for the :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>` drivers.

-  Launch the EVAL-AD7944/AD7985/AD7986EDZ software from the **Analog Devices** subfolder in the **Programs** menu.
-  Select the appropriate device from the drop-down menu :adi:`AD7944`, :adi:`AD7985`, or :adi:`AD7986`.
-  Apply a signal source to the AIN+/AIN− SMB inputs on the evaluation board.
-  Configure the signal source for the appropriate signal applied to the input of the device.
-  Capture data by initiating a single capture **(F3)** or a continuous capture **(F4)**.
-  See details on configuring the software in the Running the ADC Analysis Software section.

Note that the measurements made by Analog Devices use the Audio Precision SYS-2522.

|image1| **Figure 2. Hardware Configuration—Setting up the Evaluation Board**

Evaluation Board Hardware
=========================

| The low power, :adi:`AD7944`/:adi:`AD7985`/:adi:`AD7986` ADCs offer very high performance of up to 2.0 MSPS (:adi:`AD7986`) and 2.5 MSPS (:adi:`AD7944` and :adi:`AD7985`) throughput rates using a flexible parallel interface on the 96-pin interface to the :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>` board.

| The evaluation board is designed to demonstrate the performance of the ADC and to provide an easy-to-understand interface for a variety of system applications.
| The evaluation board is ideal for use with the Analog Devices Converter and Evaluation Development EVAL-CED1Z (CED). The design offers the flexibility of applying external control signals and is capable of generating conversion results on parallel 16-bit wide buffered outputs.

| Figure 2 shows the EVAL-AD7944/AD7985/AD7986EBZ evaluation board. The on-board FPGA, U3, provides the necessary control signals for conversion and deserializes the serial data as the :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>` board uses a parallel interface. The evaluation board is a flexible design that enables the user to choose among many different board configurations, analog signal conditioning, reference, and different modes of conversion data.

| This evaluation board is a 6-layer board carefully laid out and tested to demonstrate the specific high accuracy performance of the :adi:`AD7944`, :adi:`AD7985`, and :adi:`AD7986`. See the Design Support Package section for the board schematic and layout.

Device Description
------------------

| The :adi:`AD7944` is a 14-bit, 2.5 MSPS successive approximation analog-to-digital converter (SAR ADC), whereas the :adi:`AD7985` is a 16-bit version of the SAR ADC. The :adi:`AD7986` is an 18-bit, 2 MSPS SAR ADC.
| These ADCs are low power and high speed and include an internal conversion clock, an internal reference (and buffer), error correction circuits, and a versatile serial interface port. On the rising edge of CNV, the ADC samples an analog input, IN+, between 0 V and REF with respect to the ground sense, IN−. The ADCs feature a very high sampling rate turbo mode (TURBO is high) and a reduced power normal mode (TURBO is low) for low power applications where the power is scaled with the throughput. A full description of these products is available in their respective data sheets and should be consulted when using this evaluation board.

Power Supplies
--------------

Power is supplied to the board through P1 when used with the :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>`. Each supply is decoupled at the point where it enters the board and again at each device. A single ground plane on this board minimizes the effect of high frequency noise interference.

Standalone Operation
--------------------

The evaluation board can be used in standalone mode without the CED controller board. In this case, power supplies need to be applied to the board at P4 or at the relevant test points. At a minimum, the board requires ±5 V, +12 V, +7 V, or + 2.5 V. See the Design Support Package section for details regarding power supply connections.

Grounding
---------

The evaluation board ground plane is separated into two sections: a plane for the digital interface circuitry and an analog plane for the analog input and external reference circuitry. To attain high resolution performance, the board was designed to ensure that all digital ground return paths do not cross the analog ground return paths by connecting the planes together directly under the converter.

Conversion Control
------------------

The on-board FPGA performs a number of digital functions, one of them being the deserialization of the serial conversion results as the CED data capture board uses a 16-bit parallel interface. If desired, the deserialized data can be monitored on the 96-pin edge connecter, P1, BD[15:0]. The CED uses a buffered busy signal, BBUSY, as the general interrupt for data.

Analog Inputs
-------------

| The analog inputs to the evaluation board are J1, J2, and SMB (push on). These inputs are buffered with dedicated amplifier circuitry (A2, A3, and discretes) to allow configuration changes such as positive or negative gain, input range scaling, filtering, addition of a dc component, and use of different op amps and supplies. The analog input amplifiers are set as unity-gain buffers at the factory. The supplies are selectable with solder pads and are set for the +7 V to −5 V ranges.
| The default configuration sets both A2 and A3 at midscale generated from either a buffered reference voltage divider or the internal reference of the ADC.
| The evaluation board is factory configured for providing either a single-ended path or a fully differential path. Because the AD7986 is differential, both inputs and amplifier circuits are used to buffer the IN+ and IN- inputs of the ADCs. For the AD7944 and AD7985 evaluation boards, only the J2, A3, and associated circuitry is used in the path.
| For dynamic performance, an FFT test can be executed by applying a very low distortion ac source. For low frequency testing, an audio precision source can be used directly because the outputs on these are isolated. Set the audio precision outputs for balanced and floating. Although different sources can be used, most are single ended and use a fixed output resistance.
| Because the evaluation board uses the amplifiers in unity gain, the noninverting input has a common-mode input with a 590 Ω series resistor, which needs to be taken into account when directly connecting a source (voltage divider).

Serial Interface
----------------

The 3-wire serial interface SDI, SCK, and SDO together with CNV are present on the digital interface test points, and FPGA buffered versions are on the 96-pin connector, P1. The on-board Altera FPGA can be reprogrammed to the user’s configuration as the serial device and U1 is in-circuit programmable.

Jumpers, Solder Pads and test points
------------------------------------

A number of 3-pin jumpers, solder pads, and test points are provided on the evaluation board and are detailed in Table 1, Table 2, and Table 7. Most of the 3-pin jumpers are used for the reference selection of the ADCs (see the Reference Options section for details and settings).

Table 1. 3-Pin Jumper Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------+------------------+----------------------------------------------------------------------------------------------------------+
| Jumper | Default Position | Function                                                                                                 |
+========+==================+==========================================================================================================+
| P2     | REF to middle    | ADC REF/REFIN select                                                                                     |
+--------+------------------+----------------------------------------------------------------------------------------------------------+
| P9     | REFS to VREF     | On-board reference/external reference selection                                                          |
+--------+------------------+----------------------------------------------------------------------------------------------------------+
| P10    | BUF to middle    | Selection of either Amplifier U2 or bypassing.                                                           |
+--------+------------------+----------------------------------------------------------------------------------------------------------+
| P11    | REFIN to GND     | Selection of either the internal reference and/or reference buffer. Used in conjunction with P12 and P9. |
+--------+------------------+----------------------------------------------------------------------------------------------------------+
| P12    | PDREF to VIO     | Selection of either the internal reference of the ADC or an external reference.                          |
+--------+------------------+----------------------------------------------------------------------------------------------------------+

Table 2. Solder Pad Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Solder Pad | Default Position          | Function                                                                                                                                                                                                                                                                                |
+============+===========================+=========================================================================================================================================================================================================================================================================================+
| JP1, JP2   | A2, A3 (bottom to middle) | ADC inputs: bottom pad to middle pad are for A2/A3 output. To bypass and use J1/J2 directly, solder top pad to middle pad.                                                                                                                                                              |
+------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| JP3        | ADC specific              | Single or differential ADC input selection. Top pad to middle pad for the AD7986; bottom pad to middle pad for AD7944 and the AD7985.                                                                                                                                                   |
+------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| JP9, JP10  | Left pads                 | 10-lead or 20-lead amplifier to ADC selection for future use.                                                                                                                                                                                                                           |
+------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VDRV−      | −5 VA                     | Buffer amplifier negative supply: Selection of GND or −5 VA.                                                                                                                                                                                                                            |
+------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VDRV+      | +7 V                      | Buffer amplifier positive supply: selection of 12 V, 7 V, or 5 V.                                                                                                                                                                                                                       |
+------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VCC REF    | +7 V                      | Reference circuit positive supply: selection of 12 V or 7 V.                                                                                                                                                                                                                            |
+------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AVDD       | +2.5 V                    | ADC AVDD (analog core) supply: selection of 2.5 V or 5 V on the board or externally. To prevent permanent damage to the ADC, do not solder to 5 V or connect this supply to > 2.5 V.                                                                                                    |
+------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DVDD       | +2.5 V                    | ADC DVDD (digital core) supply: selection of 2.5 V or 5 V on the board or externally. To prevent permanent damage to the ADC, do not solder to 5 V or connect this supply to > 2.5 V.                                                                                                   |
+------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BVDD       | +5 V                      | ADC BVDD 5 V supply: selection of 5 V on the board or externally. For an external reference, the best performance is obtained when the reference source that is connected to the REF pins and BVDD are the same. See the External Reference: Factory Configuration section for details. |
+------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VIO        | +2.5 V                    | ADC digital input/output supply voltage.                                                                                                                                                                                                                                                |
+------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Solder pads are factory configured for the device being evaluated.

Reference Options
-----------------

The AD7944/AD7985/AD7986 each have an internal 4.096 V reference together with an internal buffer useful for using an external reference, or it can use an external 5.0 V reference directly. The evaluation board can be configured to use any of these references. A number of jumpers are used to set the reference and are detailed in Table 3.

External Reference: Factory Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board includes the :adi:`ADR435` which is a 5 V precision voltage reference. This reference can drive the ADCs and the REF pin directly or it can be buffered with the :adi:`AD8032`; both of which serve as the factory default setting. The best attainable SNR is achieved by using the maximum reference voltage of 5 V (see the appropriate ADC datasheet for details).

Table 3. Factory Reference Jumper Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

====== =====================
Jumper Setting
====== =====================
P2     REF and middle
P9     REFS to VREF
P10    BUF to middle
P11    REFIN to GND
P12    PDREF to VIO
BVDD   5 V (factory default)
====== =====================

To use an external reference source as opposed to the internal reference, there are two methods available, as follows:

-  For an external unbuffered reference, leave P10 to P12 as the factory settings, open P2, and connect a source to the REF test point.
-  The ability to buffer the user external reference is also available. In this case, replace P2, open P9, and apply the source to the VREF test point.

ADC Reference Supply, BVDD
~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board includes a 5 V source for the ADC reference supply, BVDD, set with a pair of solder pads of either 5 V or EXT_B, and a test point, EXT_B. For the best performance, derive this supply from the external reference. To use the EXT_B, remove the solder from the 5 V pad and solder the EXT_B pad to BVDD.

Internal 4.096 V Reference
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADC has an internal 4.096 V precision reference and can be used on most applications. Connecting PDREF to GND enables the internal reference. When the internal reference is enabled, 4.096 V as well as a 1.2 V band gap are present on the ADC REF pin and test point. Note when using the internal reference, external sources must not be connected to these test points because they are directly connected to the ADC pins.

Table 4. Internal Reference Jumper Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

====== =============
Jumper Setting
====== =============
P2     Open
P9     REFS to VREF
P10    Don’t care
P11    Open
P12    PDREF to GND
BVDD   5 V (factory)
====== =============

Internal Reference Buffer
~~~~~~~~~~~~~~~~~~~~~~~~~

The internal reference buffer is useful when using an external 1.2 V reference. When using the internal reference buffer, applying 1.2 V to REFIN, which is directly connected to the REFIN pin of the ADC, produces 4.096 V at the REF pin of the ADC. Because there is no 1.2 V reference on the board, there are two methods to generate a 1.2 V reference. The first method is to connect an external source to the REFIN test point using the jumper settings listed in Table 5.

Table 5. Fully External Reference Buffer Jumper Configuration: REFIN Test Point Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

====== =====================
Jumper Setting
====== =====================
P2     Open
P9     Don’t care
P10    Don’t care
P11    Open
P12    PDREF to VIO
BVDD   5 V (factory default)
====== =====================

The second method is to use the U2 op amp to voltage divide down the 5 V output of the :adi:`ADR435` to 1.2 V by using R2/R4 = 1 kΩ/316 Ω. To use this method, replace R4 and set the jumpers to the settings listed in Table 6.

Table 6. Fully External Reference Buffer Jumper Configuration: Divide Down Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

====== =====================
Jumper Setting
====== =====================
P2     REFIN to middle
P9     REFS to VREF
P10    BUF to middle
P11    REFIN to Pin 1
P12    PDREF to VIO
BVDD   5 V (factory default)
====== =====================

Evaluation Board Software
=========================

Important Software Pre-Installation Information
-----------------------------------------------

The :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>` board must not be connected to the USB port of the PC until after the software is installed. However, to check that the board has power (evidenced by the green LED light being lit), the 7 V dc supply can be connected to the power input connector on the :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>`.

Software Installation
~~~~~~~~~~~~~~~~~~~~~

| It is recommended to close all Windows® applications prior to installing the software. The evaluation board comes with a CD as part of the evaluation kit. The latest software versions are always available from the Analog Devices product page, visit www.analog.com. Note that the user must accept the license agreement during the installation process.
| |image2| **Figure 3. To Install, the User Must Accept License Agreement**

| After downloading the software, it is recommended to use the WinZip extract function to extract all of the necessary components rather than immediately selecting **setup.exe** from within the zipped file. After extracting the software, click **setup.exe** in the folder created during the extraction process and follow the instructions on the screen.
| If another version of the software already exists on the computer, it may be necessary to remove it. To remove prior versions of the software, click the Windows **Start** button, select **Control Panel**, and then select **Add or Remove Programs**. When the list populates, navigate to **Analog Devices High Resolution sampling ADC’s Evaluation Software** or **PulSAR Evaluation Software** and select **Remove**.

Typical Install Process
^^^^^^^^^^^^^^^^^^^^^^^

|image3| **Figure 4. Initiating Install from setup.exe**

|image4| **Figure 5. Default Location for Install Files**

|image5| **Figure 6. Installing Software**

|image6| **Figure 7. Install Complete**

USB Drivers
~~~~~~~~~~~

The software also installs the necessary USB drivers through a separate installation process. When the software installation completes the drivers installation wizard displays: click **Install** to install the drivers automatically, as shown in Figure 8 and Figure 9.

|image7| **Figure 8. Driver Install Process**

|image8| **Figure 9. Install Complete**

After installing the software and drivers, power the CED board and connect it to the PC USB 2.0 port, at which time the **Welcome to the Found New Hardware Wizard** initiates. |image9| **Figure 10. Found New Hardware**

When installed properly, the hardware wizard displays the following message, shown in Figure 11, signaling that the evaluation board software is setup and ready to use. |image10| **Figure 11. Evaluation Board Software Installation Complete**

On some PCs, the **Found New hardware Wizard** may show up again and, if so, follow the same procedure to install it properly. Use the **Device Manager**, shown in Figure 12, to verify that the driver was installed correctly. |image11| **Figure 12. Device Manager Verification**

Troubleshooting the Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the driver was not installed properly, Windows does not recognize the CEDIZ board and the Device Manager menu displays a question mark for **Other devices**. |image12| **Figure 13. Device Manager Menu Displaying Unrecognized Device**

The USB device can be opened to view its uninstalled properties, as shown in Figure 14. |image13| **Figure 14. USB Device Uninstalled Properties**

The most usual reason for uninstalled properties is caused by the installation of the software and drivers by a user without administrative privileges. If this is the case, log on as an administrator with full privileges and reinstall the software.

Running the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The evaluation board includes software for analyzing the AD7944, AD7985, and AD7986. The :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>` is required when using the software. Use the software to perform the following tests:

-  Histogram for determining code transition noise (dc).
   \* Fast Fourier transforms (FFT) for signal-to-noise ratio (SNR), SNR and signal-to-noise-and-distortion (SINAD), total harmonic distortion (THD), and spurious free dynamic range (SFDR).
   \* Decimation (digital filtering).
   \*

The software is located at <local_drive>:\\Program Files\\Analog Devices\\PulSAR ADC Evaluation Software\\Eval PulSAR CED.exe. A shortcut is also added to the Windows **Start** menu under **Analog Devices PulSAR Evaluation Software, Eval PulSAR CED**. To run the software, select the program from either location.

Running the ADC Analysis Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The evaluation board includes software for analyzing the :adi:`AD7944`, :adi:`AD7985`, and :adi:`AD7986` ADCs. The :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>` is required when using the ADC analysis software. Use the software to perform the following tests:

-  Histogram for determining code transition noise (dc).
-  FFT for SNR, SNR and SINAD, THD, and SFDR.
   \*

| Refer to Figure 15 to Figure 20 for additional details and features of the software.
| The ADC analysis software is located at C:\\Program Files\\Analog Devices\\ PulSAR ADC Evaluation Software\\Eval PulSAR CED.exe. A shortcut is also added to the Windows **Start** menu under **Analog Devices PulSAR ADC Evaluation Software, Eval PulSAR CED.** To run the software, select the program from either location.

Software Operation
------------------

The following steps detail the operation of the software located in the default directory: <local_drive>:\\Program Files\\Analog Devices\\PulSAR ADC Evaluation Software\\Eval PulSAR CED.exe, which opens the **Raw Data Capture** window.

|image14| **Figure 15. Setup Screen**

-  To start the software, click the arrow in the upper left corner of the screen. When running, the arrow icon is displayed as shown in the area in Figure 15 marked with the Number 1.
-  Select the device to be evaluated (see the area in Figure 15 marked with the Number 2).
-  Set the controls (see the area in Figure 15 marked with the Number 3) for the following:

   -  **Sample Frequency:** Enter the sample rate in kHz. Units can be used such as 10k (case sensitive) for 10,000,000 Hz or 10 MSPS.
   -  **Input Range:** Because the ADCs have a variable input range depending on the reference voltage, select the correct one (4.096 V or 5 V) to display the correct LSB size.
   -  **Interface Mode:** Options for using or not using the busy mode. In busy mode, the SDO can be monitored to see the actual conversion time (BUSY high to low transition).
   -  **Turbo CTRL:** Select the fastest mode, turbo mode, or normal mode. Note that the throughput must be manually changed when changing modes.
   -  **CNV Mode:** Selects between continuous (Cont.) or burst conversion modes. In continuous mode, the ADC is continuously converting. In burst mode, the ADC does not continuously convert.
   -  **Coding:** For the AD7986, **2 compl** must be selected in the **Coding** field because the ADC result is always twos complement. For the AD7985 and AD7944, binary is set because the ADC output is straight binary.

-  Use the controls shown in the area of Figure 15 marked with the Number 4 for functions such saving, printing, help, and so forth. These functions are also accessible from the **File** menu.

   -  **Save (F5):** In the **Save** **(F5)** pull-down menu, there are several options as follows:

      -  **LV Config:** selects the LabVIEW® configuration, which allows the current configuration to be saved to a filename.dat file. This option is useful when changing many of the default controls. To load the saved configuration, click **Load Previous Configuration** located above **Save (F5)**.
      -  **Html:** saves the current screen shot to an html file.
      -  **Spreadsheet:** saves the current data displayed in the chart in a tab delimited spreadsheet. Raw ADC data includes time domain (in V or code), FFT, or decimated (in dB).

   -  **Stop (F10):** Click **Stop (F10)** to stop running the software. Likewise, clicking the stop sign icon, on the top menu bar also stops the software.
   -  **RESET:** click **RESET** to reset the CED capture board.

Context Help
------------

On-Screen Help
~~~~~~~~~~~~~~

| To use the on-screen help. Select **Help**, **Show Context Help** or click **Help (F1)**. These function areas on the screen are indicated by Number 1 in Figure 16. Hovering the cursor over most screen items displays useful information for the particular control or displayed unit.
| |image15| **Figure 16. Context Help and Histogram Controls**

Histogram Controls
^^^^^^^^^^^^^^^^^^

| The histogram controls, shown in the area indicated by Number 2 in Figure 16, are used for axes and zooming panning, as follows:

Graph Axis Lock
^^^^^^^^^^^^^^^

| Locks the graph axis to automatically fit the data.

Axis Rescaling
^^^^^^^^^^^^^^

| Uses the last axis set by the user. These allow the user to rescale the x- and y-axis, respectively, to the automatic values.

Axis Properties
^^^^^^^^^^^^^^^

| These are used to set the x- and y-axis properties, such as format, precision, color, and so forth.

Cursor Display
^^^^^^^^^^^^^^

| Displays the cursor.

Zooming
^^^^^^^

| Zooms in and out.

Panning
^^^^^^^

| Use to pan.

Graph Properties
^^^^^^^^^^^^^^^^

Sets various graph properties such as graph type, colors, lines, and so forth.

Histogram and Oscilloscope Charts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The areas of the **Raw Data Capture** window that pertain to working with histogram or oscilloscope charts are demarcated by the sections numbered 1, 2, and 3 in Figure 17.
| |image16| **Figure 17. Histogram Data Window**

Single or Continuous Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Use the buttons shown in Section 1 in Figure 17 to perform either a single capture or continuous capture of data. Enter the number of samples that are required in the **# of Samples (k)** field (located to the left of the **Single Capture (F3)** button). The statistics for the x- and y-axes are displayed in the **Histogram Data** section of the window, shown as the Number 2 and Number 3 areas within Figure 17.
| The graphic results are displayed in the chart area of the window. Note that the results can be displayed as either a histogram (see Figure 18) or an oscilloscope (see Figure 19) by selecting the relevant tab, **Oscilloscope**, above the chart display (shown as Number 1 in Figure 20).
| Time domain data can also be viewed by using the **Oscilloscope** tab. In addition, the charts can be displayed together when the **Summary** tab is selected (see Figure 21).
| |image17| **Figure 18. Histogram Chart Display**

| |image18| **Figure 19. Oscilloscope Chart Display (Time Domain)**
| |image19| **Figure 20. Oscilloscope**
| |image20| **Figure 21. Summary Tab**

FFT Spectrum Data
^^^^^^^^^^^^^^^^^

| To review the FFT spectrum data, select the **Spectrum** tab in the **Raw Data Capture** window. Figure 22 shows the FFT spectrum window and sections numbered 1, 2, and 3 of this window are described as follows:

Displaying the FFT
^^^^^^^^^^^^^^^^^^

| From the **Raw Data Capture** window, in the section of Figure 22 labeled with Number 1, select the **Spectrum** tab to display the FFT when the spectrum chart is selected.

Displaying the Spectrum Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| The **Spectrum Data** section (Number 2 and Number 3 in Figure 22), is located beneath the spectrum chart. These areas of the **Spectrum Data** section display the data for the x-axis (shown in the area labeled as Number 2) and y-axis, (shown in the area labeled as Number 3).
| |image21| **Figure 22. FFT Spectrum**
| ====== Troubleshooting ======

Software Tips
-------------

-  Always install the software from the CD or the Analog Devices website prior to connecting hardware to the PC.
-  Always allow the installation to fully complete (the software is a two part installation: the ADC software and the drivers). The installation may require a restart of the PC.
-  When you first plug in the board via the USB cable, allow the **New Found Hardware Wizard** to run completely. Though this may take some time, it is required prior to starting the software.
-  Where the board does not appear to be functioning, ensure the following: that the ADC evaluation board is connected to the CED board, the daughter card is connected, and the board is being recognized in the **Device Manager**, as described in the Troubleshooting the Install section.

Hardware Tips
-------------

If the software does not read any data back, take the following steps:

-  Check that power is applied to the CED board and that the voltages are present on the P connectors as described in Table 3.
-  Confirm the signal source is applied and outputting the expected signal.
-  Probe different points in the signal path to ensure that the applied signal is present at the input of both the driver amplifiers and the ADC.

If there are issues getting SNR performance, note the following:

-  Some signal sources may require a filter in series to achieve performance. The SNR measurements for this board were tested with the AP-2322 signal source. This is a high performance audio analyzer and source.
-  To achieve best SNR performance, ensure that the signal amplitude is sufficient to deliver a full-scale input range to the ADC. Monitor the maximum and minimum amplitude or fundamental amplitude in the **Spectrum** tab. Ideally, the fundamental should provide a full-scale swing; therefore, adjust the signal source output to cover the full-scale range.

Design Support Package
======================

Schematics
----------

`Evaluation board schematics <https://wiki.analog.com/_media/resources/eval/ad7944_85_86_d.pdf>`_

Gerber Files
------------

`Evaluation board gerber files <https://wiki.analog.com/_media/resources/eval/fab5010091a4-21.zip>`_

Bill Of Materials
-----------------

`BOM for AD7944/AD7985/AD7986 <https://wiki.analog.com/_media/resources/eval/eval_ad7944_85_86_bom_01_19_12.xls>`_

Software
--------

Software compatible with CED evaluation board available :adi:`here <static/imported-files/eval_boards/PulSAR_Software_Rev1.7.zip>`.

Related Links
=============

+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Resource                                                                                                             | Description                                                                                         |
+======================================================================================================================+=====================================================================================================+
| :adi:`AD7944`                                                                                                        | Product Page, AD7944, 14-bit, 2.5 MSPS ADC with internal reference                                  |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| :adi:`AD7985`                                                                                                        | Product Page, AD7985, 16-bit, 2.5 MSPS ADC with internal reference                                  |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| :adi:`AD7986`                                                                                                        | Product Page, AD7986, 18-bit, 2 MSPS differential input ADC with internal reference                 |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| :adi:`AD8021`                                                                                                        | Product Page, AD8021, low noise, high speed amplifier                                               |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| :adi:`AD8032`                                                                                                        | Product Page, AD8031/32, low power, low noise amplifier                                             |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| :adi:`ADA4899-1`                                                                                                     | Product Page, ADA4899-1, low noise, high speed amplifier                                            |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| :adi:`ADR435`                                                                                                        | Product Page, ADR435, ultralow noise XFET voltage reference with current sink and source capability |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| :adi:`ADP1715`                                                                                                       | Product Page, high accuracy low IQ, 500 mA, ANYCAP®, adjustable low dropout regulator               |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| :adi:`ADP3334`                                                                                                       | Product Page, ADP3334, 500 mA low dropout CMOS linear regulator with soft start                     |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| :adi:`EVAL-CED1Z <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>`                     | Product Page, converter and evaluation development board                                            |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| :adi:`AN-931`                                                                                                        | Application Note, *Understanding PulSAR ADC Support Circuitry*                                      |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| :adi:`AN-932`                                                                                                        | Application Note, *Power Supply Sequencing*                                                         |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ad7944_85_86.jpg
   :width: 900px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/10387-003.jpg
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/10387-004.jpg
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/10387-005.jpg
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/10387-006.jpg
   :width: 300px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/10387-007.jpg
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/10387-008.jpg
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/10387-009.jpg
   :width: 300px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/10387-010.jpg
   :width: 300px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/10387-011.jpg
   :width: 300px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/10387-012.jpg
   :width: 300px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/10387-013.jpg
   :width: 300px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/10387-014.jpg
   :width: 300px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/10387-015.jpg
   :width: 700px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/10387-016.jpg
   :width: 700px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/10387-017.jpg
   :width: 700px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/10387-018.jpg
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/10387-019.jpg
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/10387-020.jpg
   :width: 700px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/10387-021.jpg
   :width: 700px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/10387-022.jpg
   :width: 700px
