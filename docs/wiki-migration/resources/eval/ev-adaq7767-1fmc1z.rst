Evaluation Board for ADAQ7767-1 Flexible Resistive Input, 24-Bit, 1MSPS, Alias Free μModule® DAQ Solution
=========================================================================================================

Features
--------

-  Full featured evaluation board for the ADAQ7767-1
-  On-board IEPE Sensor interface
-  On-board reference and power supply circuits
-  PC software for control and data analysis of time and frequency domain
-  System demonstration platform-compatible (:adi:`SDP-H1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-h1.html>`)
-  Optional PMOD Connector

Evaluation Kit Contents
-----------------------

-  EV-ADAQ7767-1FMC1Z evaluation board

Equipment Needed
----------------

-  SDP-H1 (:adi:`EVAL-SDP-CH1Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-h1.html>`) system demonstration platform
-  DC/AC signal source (Audio Precision or similar high performance signal source)
-  PC running Windows 7, Windows 8, or Windows 10 with USB 2.0 port

Software Needed
---------------

-  :adi:`ACE Evaluation Software <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`
-  ADAQ7767-1 ACE Plug-In

General Description
-------------------

The EV-ADAQ7767-1FMC1Z evaluation kit enables the simplified evaluation of the ADAQ7767-1: a 24-bit, 1 MSPS, alias free µModule® data acquisition (DAQ) solution with flexible resistive inputs. The evaluation board is used alongside a downloadable evaluation software to fully configure the features of the ADAQ7767-1 and display the conversion results in the time and frequency domains.

The EV-ADAQ7767-1FMC1Z board connects to the USB port of the PC via the (:adi:`EVAL-SDP-CH1Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-h1.html>`) system demonstration platform board. By default, the 3.3V rail is supplied by the EVAL-SDP-CH1Z, and is regulated by the on-board power solution to ±15V and 5.3V to power the ADAQ7767-1 and its support components. An IEPE-interface and a pair of input buffers are included to evaluate the ADAQ7767-1 across a variety of input types.

For a full description of the ADAQ7767-1, see the ADAQ7767-1 data sheet, which must be consulted in conjunction with this user guide when using the evaluation board.

Evaluation Board Photograph
---------------------------

.. container:: centeralign

   |image1|\ *Figure 1. EV-ADAQ7767-1FMC1Z Board*


Quick Start Guide
-----------------

.. container:: centeralign

   |image2|\ *Figure 2. Evaluation Board Setup*


To begin using the evaluation board, take the following steps:

-  Ensure the SDP-H1 system demonstration platform board is disconnected from the PC. Install the ACE (Analysis, Control, Evaluation) software to evaluate ADAQ7767-1. Restart the PC after the software installation is complete. For complete software installation instructions, see the Software Installation Procedures section.
-  Connect the SDP-H1 board to the unpowered EV-ADAQ7767-1FMC1Z evaluation board. The J4 connector of the SDP-H1 board connects to the receiving socket, P5, on the EV-ADAQ7767-1FMC1Z printed circuit board (PCB), as shown in Figure 2.
-  Ensure that the hardware links are in place according to the desired operation. For more details see Table 3.
-  Connect the 12 V dc supply to the SDP-H1 board and then connect to the PC using the supplied USB cable. Choose to automatically search for the drivers for the SDP-H1 if prompted by the operating system.
-  Launch the ACE (Analysis, Control, Evaluation) software from the **Analog Devices** subfolder in the **Programs** menu.
-  Double click the **ADAQ7767-1 Eval Board icon** to open the board view window. LED (DS2) should turn on, indicating board power up.
-  Double click the **ADAQ7767-1 chip icon** in the board view window to open the chip view window.
-  Click on the **Proceed to Analysis** button to show the Analysis view window.
-  Apply an input signal at AINP/AINN, or through the optional IEPE input (IEPE_IN), then click on **Run Once**.

To power off, first disconnect the input signal, and close the software. Then press the reset button on the SDP-H1 board before disconnecting the power or USB.

Example Data Capture – AC SIGNAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Start the ADAQ7767-1 evaluation software. On power-up, the software sets the input range to IN2, ADC power mode to “fast”, and the filter to “wideband low ripple” with an ODR = 256 kSPS.
-  Connect the analog input signal (10.6 Vp) to AINP and AINN. Use IN2 as input pins to the ADAQ7767-1 by setting jumpers P1 and P2 (default: IN2, G = 4/11 V/V).
-  The user can see the result directly by clicking on the **Run Once** button (capturing 8192 samples by default).
-  The sampled data is now present in the data capture tabs (**Waveform, Histogram, and FFT** tabs). Change between each of these tabs to view the results.
-  These settings give a dynamic range of approximately 106 dB, which can be seen on the Results section of the FFT tab.

.. container:: centeralign

   |image3|\ *Figure 3. FFT of 10.6Vp 1kHz fully differential signal applied to IN2+/- of ADAQ7767-1*


Example Data Capture – DC SIGNAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Sinc3 filter with ODR=50SPS is a sweet spot for measurement a pure DC signal, as the sinc notch appears at 50Hz and can be used to reject the 50Hz line frequency. Take the following steps to setup the DUT for a 50SPS Sinc3 filter:

-  As an example for RMS noise, short the AINP and AINN connectors to GND, and use IN2 as input pins to the ADAQ7767-1 by setting jumpers P1 and P2 (default: IN2, G = 4/11 V/V).
-  At the Chip View of the ACE software, click the **Filter Configuration** icon.
-  Use the drop-down menu to select Sinc3 (programmable decimation rate) option as shown in Figure 4.

.. container:: centeralign

   |image4|\ *Figure 4. Set the digital filter type*


-  Configure the **Sinc3 Decimation Rate** by typing in the value **‘13FF’** in the text box near the lower right corner as shown in Figure 5. This is also reflected in the registers SINC3_DEC_RATE_LSB and SINC3_DEC\_ RATE_MSB located at the memory map of the ACE software. Afterwards, click the **Apply Changes** for this to take effect.

.. container:: centeralign

   |image5|\ *Figure 5. Set the Sinc3 filter decimation ratio*


-  Before clicking on the Run Once button, make sure to adjust the number of samples to be collected accordingly. Collecting the default 8192 samples at 50SPS will take 8192/50/60=2.73 minutes!
-  Set to 1024 samples, which should take about 20 seconds.
-  The same condition (Sinc3 50SPS) is used to measure Low Frequency Noise, as specified in the datasheet. In the **Histogram** tab, noise is displayed as Transition noise in LSB. To compare with datasheet’s referred to input (RTI) Low Frequency Noise in uVrms, apply the formula:

.. container:: centeralign


|image6|

-  For example, using IN2 with measured Transition Noise = 0.704 LSB = 0.945 uVrms RTI

.. container:: centeralign

   |image7|\ *Figure 6. Histogram of output codes. IN2+ and IN2- shorted to GND, Sinc3 at 50SPS*


How to calculate the SINC3_DEC_RATE value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, this board provides the DUT with a MCLK of approximately 16.384MHz. To achieve an ODR of 50 SPS using the sinc3 filter, use the following equation:

.. container:: centeralign

   :math:`ODR = Mclk/MclkDiv \times DecRate`


Assuming the ADAQ7767-1 is using MCLK_DIV = 2,

.. container:: centeralign

   :math:`DecRate = Mclk/MclkDiv \times ODR`


Decimation Rate = 163,840

The SINC3_DECIMATION_RATE registers (Register 0x1A and Register 0x1B) increments the value in the registers by one and then multiplies it by 32 to give the actual decimation rate. To set the decimation rate to 163,840, simply follow the equation:

.. container:: centeralign

   :math:`Value = DecRate/32 -1`


The value to be written to the sinc3 decimation registers is 5119 or 0x13FF.

Refer to the ADAQ7767-1 datasheet for more information on the DUT register configuration.

Evaluation Board Hardware
-------------------------

.. container:: centeralign

   |image8|\ *Figure 7. Simplified Evaluation Board Block Diagram*


Figure 7 shows the simplified evaluation board block diagram of the EV-ADAQ7767-1FMC1Z evaluation board connected to the SDP-H1 controller board. The evaluation board is installed with the featured ADAQ7767-1 µModule® (U1), the ADR444 4.096V reference (U4), and the on-board power solution consisting of ADP5076 (VR1), ADP7142 (U8), ADP7182 (U9), and LTC3526LB-2 (U7). A pair of ADA4622-1 (U2 and U3) can be used to buffer the inputs, while the on-board IEPE interface can be used to bias the IEPE sensor used as an input to the signal chain.

Analog Inputs
~~~~~~~~~~~~~

The analog inputs, AINP and AINN, are accessible either through the Subminiature Version B (SMB) connectors, or the turrets (T1, T2). A Subminiature Version A (SMA) connector is also provided to connect to an IEPE sensor, which receives its current bias from the on-board IEPE interface. The default settings of the board are as follows:

-  Analog inputs to ADAQ7767-1 obtained from AINP and AINN; IEPE_IN is disconnected by P4.
-  The AINP and AINN inputs are buffered by the pair of optional amplifiers ADA4622-1 (U2 and U3).
-  Using the ADR444 (U4) as a 4.096V reference and the IN2+/- ADAQ7767-1 inputs, the full-scale differential input range is ±11.2V.

See Table 2 for the suggested power supply rails and Table 3 for necessary jumper positions and link options for different input configurations and input ranges. It is recommended to use a low distortion AC source, such as the Audio Precision APx555 series, when evaluating the dynamic performance of the ADAQ7767-1.

IEPE Interface
^^^^^^^^^^^^^^

An IEPE sensor can be used as an input to the EV-ADAQ7767-1FMC1Z through the SMA connector at IEPE_IN. The on-board IEPE interface biases the IEPE sensor, which can be operated by providing a +24V rail at HV_VDD via the on-board supply or an external supply, and switching on SW_S1 and SW_S2 on the mechanical switch S2. Inserting P4 connects the IEPE input to the ADAQ7767-1. With a dropout of 1.2V across the current source (LT3092, U6) delivering a 4.5 mA bias to the IEPE sensor, this circuit complies to the usable excitation voltage and current bias of a typical IEPE interface. For overvoltage protection from the IEPE sensor, the AD5421F (U5) fault protection switch is placed the at the IEPE input. Under normal operating conditions, the IEPE LED indicator (DS1) is on.

Most IEPE sensors have their output biased at 8-14V, with an AC swing ±5V around the bias. The EV-ADAQ7767-1FMC1Z can be modified to allow AC-coupled or DC-coupled IEPE input. By default, the 0Ω resistor at R13 configures the IEPE input to be DC-coupled. The ADAQ7767-1 28V (IN3) input is designed to allow direct DC-coupled connections to IEPE sensors. For an AC-coupled IEPE input, simply replace R13 with a ceramic capacitor, and insert a resistor at R14 to implement a high-pass filter with a cut-off frequency at the sub-hertz range. The AC-coupled IEPE signal swing is suitable for the 4.096V (IN1) or the 11.2V (IN2) input ranges of the ADAQ7767-1, depending on the AC swing of the IEPE sensor.

Table 1 summarizes the recommended jumper settings related to using an IEPE sensor input.

**Table 1. Jumper Settings when applying an IEPE sensor input**


|image9|

Power Supplies
~~~~~~~~~~~~~~

The EV-ADAQ7767-1FMC1Z obtains its power from the 3.3V rail of the SDP-H1 by default. This is boosted and regulated to provide the supply rails required by the ADAQ7767-1, voltage reference, additional signal conditioning, and the IEPE interface.

The ADAQ7767-1 contains an internal 5V low dropout regulator (LDO) with the purpose of simplifying the power solution and layout of the signal chain µModule®. Together with this internal LDO, the ADAQ7767-1 can operate with only a 5.3V and a 3.3V rail. In the EV-ADAQ7767-1FMC1Z, the 3.3V from the SDP-H1 directly powers the VDD_IO. This 3.3V rail is boosted to 5.3V by the LTC3526LB-2, which is then regulated by the internal LDO to 5V, powering the VDD_FDA, VDD_ADC, VDD2_ADC, the ADR444 VREF and the optional reference buffer AD8628. The 5.3V LED (DS2) is on when a 5.3V rail is powered by the on-board or external 5.3V supply.

The higher voltage rails used by the input buffers and the IEPE interface, VDD/VSS_BUF and HV_VDD, are connected to the on-board rails, INT_VDD and INT_VSS, which are powered by the ADP5076 dual switching regulator, ADP7142 positive LDO, and ADP7182 negative LDO, as shown in Figure 8. This power tree boosts and regulates the 3.3V to a default of +15V and −15V. For the larger input signal covered by the IN3 (28V) range, the buffers and IEPE interface may require a higher voltage supply. In this case, the voltage of the rails can be increased to 28V simply moving the 0Ω links at the feedback resistors of the ADP5076, ADP7142, and ADP7182. As an option, VDD/VSS_BUF and HV_VDD can also be connected to the external supply rails EXT_VDD and EXT_VSS. See Table 2 for the recommended power supply rails when using the buffers and/or the IEPE interface and Table 3 for the power supply link options. Each supply is decoupled at the point where it enters the board and again at the point where it connects to each device. The ADAQ7767-1 has built-in 0.1uF supply decoupling capacitors on the VDD_FDA, VDD_ADC, VDD2_ADC, and VDD_IO supply pins.

The power solution for this evaluation board was designed with the aid of :adi:`LTpowerCAD <en/design-center/ltpowercad.html>`. This tool is helpful in planning and designing power systems, with component recommendations to optimize the overall power solution.

.. container:: centeralign

   |image10|\ *Figure 8. VDD_BUF, VSS_BUF, and HV_VDD Jumper Settings*


**Table 2. Recommended Power Supply Rails when using Input Buffers and/or IEPE interface**



|image11|

Hardware Link Options
---------------------

Multiple link options must be set correctly for the appropriate operating setup before applying the power and signal to the EV-ADAQ7767-1FMC1Z. Table 3 shows the default link positions for the EV-ADAQ7767-1FMC1Z.

**Table 3. Default Links and Link Options**


|image12|

On-Board Connectors
-------------------

Table 4 provides information about the external on-board connectors on the EV-ADAQ7767-1FMC1Z.

\**Table 4. On-Board Connectors \*\*


|image13|

Evaluation Board Software
-------------------------

Software Installation Procedures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`ACE Software </wiki-migration/resources/tools-software/ace/userguide>`

Connecting the EV-ADAQ7767-1FMC1Z and the SDP-H1 to a PC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After installing the ACE software, take the following steps to set up the EV-ADAQ7767-1FMC1Z and the SDP-H1, as shown in Figure 2:

-  Ensure that all configuration links are in the appropriate positions, as detailed from Table 3.
-  Connect the EV-ADAQ7767-1FMC1Z securely to the 160-way connector on the SDP-H1. The EV-ADAQ7767-1FMC1Z does not require an external power supply adapter.
-  Connect the SDP-H1 to the PC via the USB cable included in the SDP-H1 kit.

After completing the steps in the Evaluation Board Software section and the Evaluation Board Hardware section, set up the system for data capture as follows:

-  Run the **Found New Hardware Wizard** after the SDP-H1 system demonstration platform board is plugged into the PC. If using Windows XP, the user may need to search for the SDP-H1 drivers. Automatically search for the drivers for the SDP-H1 system demonstration platform board if prompted by the operating system.
-  Check that the evaluation board is connecting to the PC correctly using the **Device Manager** of the PC. Access the Device Manager as follows:

   -  Right click **My Computer** and then click Manage.
   -  A dialog box appears asking for permission to allow the program to make changes to the computer. Click **Yes**.
   -  The **Computer Management** window appears. Click **Device Manager** from the list of **System Tools** (see Figure 9).
   -  If the SDP-H1 system demonstration platform board appears under **ADI Development Tools**, the driver software is installed and the evaluation board is connecting to the PC correctly.

.. container:: centeralign

   |image14|\ *Figure 9. Checking that the Evaluation Board is connected to the PC correctly*


Launching the Software
~~~~~~~~~~~~~~~~~~~~~~

When the EV-ADAQ7767-1FMC1Z and SDP-H1 boards are properly connected to the PC, launch the ACE software. To launch the ACE software, take the following steps:

-  From the **Start** menu, select **All Programs > Analog Devices > ACE > ACE.exe** to open the main software window shown in Figure 10.

.. container:: centeralign

   |image15|\ *Figure 10. EV-ADAQ7767-1FMC1Z ACE Software Main Window*


-  The EV-ADAQ7767-1FMC1Z icon appears in the **Attached Hardware** section.
-  If the EV-ADAQ7767-1FMC1Z is not connected to the USB port via the SDP-H1 board when the software is launched, the EV-ADAQ7767-1FMC1Z board icon does not appear in the **Attached Hardware** section. Connect the EV-ADAQ7767-1FMC1Z and SDP-H1 board to the USB port of the PC and wait a few seconds, then continue following these instructions.
-  Double-click the **EV-ADAQ7767-1FMC1Z board icon** to open the board view window shown in Figure 11.

.. container:: centeralign

   |image16|\ *Figure 11. EV-ADAQ7767-1FMC1Z Board View*


-  Double click the **ADAQ7767-1 chip icon** to open the chip view window shown in Figure 12.

.. container:: centeralign

   |image17|\ *Figure 12. EV-ADAQ7767-1FMC1Z Chip View*


-  Click **Software Defaults** and then click **Apply Changes**.
-  Click **Proceed to Analysis** to open the EV-ADAQ7767-1FMC1Z analysis shown in Figure 13.

Exiting the Software
~~~~~~~~~~~~~~~~~~~~

To exit the software, click file icon on the upper right tab and then click Exit.

Description of the Analysis Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click **Proceed to Analysis** in the chip view window to open the window shown in Figure 13. The analysis view contains the **Waveform** tab, the **Histogram** tab, and the **FFT** tab.

Capture Settings
^^^^^^^^^^^^^^^^

**ODR (Output Data Rate).** The ODR is automatically calculated by the software based on the selected ADC filter settings. By default, this is set to 256 kSPS. **Sample Count.** The default sample count is set at 8192 samples, but it can be changed to the selection of the dropdown list, ranging from 512 to 131072 samples. Click **Run Once** in the **Capture Settings** section to start a data capture of the samples at the sample rate specified in the **Sample Count** dropdown list. These samples are stored on the FPGA device and are only transferred to the PC when the sample frame is complete. Click **Run Continuously** in the **Capture Settings** section to start a data capture that gathers samples continuously with one batch of data at a time.

Waveform Tab
^^^^^^^^^^^^

The **Waveform Results** section displays time domain characteristics of the signal, such as minimum, maximum, and peak-to-peak expressed in codes or in volts. Click **Export** to export captured data, which include the waveform, histogram, and FFT data is stored in .xml files along with the values of parameters at capture. The waveform graph shows each successive sample of the µModule output. The user can zoom in on and pan across the waveform using the embedded waveform tools. Click the display unit’s dropdown list (shown with the **Volts** option selected in Figure 13) to select whether the data graph displays in units of hexadecimal, volts, or codes. The axis controls are dynamic. When selecting either y-scale dynamic or x-scale dynamic, the corresponding axis width automatically adjusts to show the entire range of the µModule results after each batch of samples.

.. container:: centeralign

   |image18|\ *Figure 13. EV-ADAQ7767-1FMC1Z Waveform*


Histogram Tab
^^^^^^^^^^^^^

The **Histogram** tab contains the histogram graph and the **Results** pane, as shown in Figure 14. The **Results** pane displays the information related to the dc performance. The histogram graph displays the number of hits per code within the sampled data. This graph is useful for dc analysis and indicates the noise performance of the device.

.. container:: centeralign

   |image19|\ *Figure 14. EV-ADAQ7767-1FMC1Z Histogram*


FFT Tab
^^^^^^^

The **FFT** tab displays FFT information for the last batch of samples gathered, as shown in Figure 15 and Figure 16.

.. container:: centeralign

   |image20|\ *Figure 15. EV-ADAQ7767-1FMC1Z FFT (without buffers)*


.. container:: centeralign

   |image21|\ *Figure 16. EV-ADAQ7767-1FMC1Z FFT with shorted inputs*


Configuring the Board
---------------------

Input Range Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

-  To select the input range, configure the P1 and P2 jumpers on the board to either IN1, IN2, or IN3.
-  To properly detect and scale the applied input voltage when displaying results in Volts: in **Chip View** of the ACE software, click on the **Active LPF** and select the corresponding input range, then click **Apply Changes.**

.. container:: centeralign

   |image22|\ *Figure 17. Input range selection menu*


ADC Configuration
~~~~~~~~~~~~~~~~~

Apart from the input range, other settings configurable from the **Chip View** window pertain to the core ADC settings. Applied changes to the core ADC through the **Chip View** window are automatically reflected in their respective registers, which can also be read / write through the **Memory Map.** The **Memory Map** contains the complete list of registers. The following are the core ADC settings configurable in **Chip View:**

-  Linearity Boost Buffers
-  Reference Buffers
-  Power Control
-  Clock Management
-  Filter Configuration
-  Digital Interface and Logic

Reset Switches
~~~~~~~~~~~~~~

Press S1 switch to reset the DUT.

A reset switch is also available on the SDP-H1 to reset the interface board.

Resetting the DUT will reset all the register settings to its default value. Resetting the digital interface board will result in losing communication with the DUT.

The user can restart the software tool to re-initialize the board.

Example Data Capture
~~~~~~~~~~~~~~~~~~~~

For an example data capture, go back to the **Quick Start Guide** at the beginning of this wiki.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/evb_photo.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/evb_setup.png
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/example_ac.png
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/set_the_digital_filter_type.png
   :width: 800px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/set_the_sinc3_filter_dec_rate.png
   :width: 800px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/eq_rti_noise.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/example_dc.png
   :width: 800px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/simplified_evb_block_diagram.png
   :width: 800px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/table1.png
   :width: 800px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/adaq7767-1_evb_supply.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/table2.png
   :width: 800px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/table3.png
   :width: 800px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/table4.png
   :width: 800px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/pc_check.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/main_window.png
   :width: 800px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/board_view.png
   :width: 800px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/chip_view.png
   :width: 800px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/waveform.png
   :width: 800px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/histogram.png
   :width: 800px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/fft_no_buffers.png
   :width: 800px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/fft_shorted.png
   :width: 800px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq7767-1/input_range_selection.png
   :width: 800px
