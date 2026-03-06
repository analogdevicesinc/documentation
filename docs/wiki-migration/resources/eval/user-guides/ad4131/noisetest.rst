Noise Test
==========

Quick Start Demonstration
-------------------------

Double click the **AD4131 Eval Board** icon to open the **AD4131 Eval Board** view window. Expand the Tools button on the home screen, click on the Macro Tools button (Label 1). Click the **Open Folder** button (Label 2) to configure the device for the noise test. The AD4131-8 is now configured for the noise test demo, where the output data rate is 50 SPS, where the sinc3 digital filter and external reference REFIN1(±) is selected. Gain and offset are the default factory values following a reset. To gather samples, change the **Samples Count** to the number of samples required, then click the **Run Once** button to acquire the samples from the ADC.

Reading Samples from the ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board is set up to use the external 2.5 V on-board reference (ADR391). To read samples from the ADC, do the following:

-  The value in the **Refin1(+/−)** field on the **Configuration** tab is set to 2.5 V by default to use the external 2.5 V on-board reference (ADR391). If a different reference is used to the AD4131, the **Refin1(+/−)** field should be updated accordingly. (The analysis results are based on the value set in this input field.)
-  When selecting **Run Once**, a batch of samples is read when clicking the button; the batch size is set by the value in the **Samples** field.
-  When selecting **Run Continuous**, the software performs a continuous capture from the ADC by clicking the **Run Once** button. Click the **Stop Capture** button again to stop capturing data.
-  Use the navigation tools within each graph to control the cursor, zooming, and panning.

Waveform
~~~~~~~~

| Find the waveforms resulting from the gathered samples in the **Analysis** tab. The waveform graph shows each successive sample of the ADC output (input referred). The indicators beside this graph show the channels converting. The navigation tools allow you to control the cursor, zooming, and panning. You can also display the conversions as voltages or codes. Below the graph are parameters, such as peak-to-peak noise and rms noise, in the **Results** section for the current batch of samples. If there are several enabled analog input channels, you can select each enabled channel and the conversions through the analyzed channel using the **Results Tab**. To save the data into an Excel file, select the **Export button** from the Results Tab. A **Save** dialog box is displayed, prompting you to save the data to an appropriate folder location.
| |image1|

Noise Test Configuration
------------------------

To gather test sample results and comparing the performance with different filter types, PGA gains, and sampling frequency Fs from the ADC.

Memory Map Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

Running the Macro Tools from previous section. We can obtain the Noise Test Demo register settings, including default register values of the following:

+-------------+-------------+----------+------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Address** | **Name**    | **Bits** | \*\* Bit Name*\* | **Settings** | **Description**                                                                                                                                                           |
+=============+=============+==========+==================+==============+===========================================================================================================================================================================+
| 0001        | adc_control | 14       | bipolar          | 1            | BIPOLAR_ON. Offset Binary Coding. Input range: −Vref to Vref                                                                                                              |
|             |             |          |                  |              | Vref -> 0xFFFFFF                                                                                                                                                          |
|             |             |          |                  |              | 0 -> 0x800000                                                                                                                                                             |
|             |             |          |                  |              | −Vref -> 0x000000                                                                                                                                                         |
+-------------+-------------+----------+------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0009        | channel_0   | [12:8]   | ainm_0           | 00001        | Negative Analog Input Select for Channel '0'. These bits select which of the analog inputs is connected to the negative input for this channel 'AIN0'.                    |
+-------------+-------------+----------+------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0019        | config_0    | [3:1]    | pga[0]           |              | PGA Gain Control, for Setup ‘n’. Controls the gain of the PGA. If PGA_BYP_n of the same CONFIG_n register is set, the PGA_n bits are ignored, and the gain is fixed at 1. |
+-------------+-------------+----------+------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             |             |          |                  | 000          | Gain 1.                                                                                                                                                                   |
|             |             |          |                  | 001          | Gain=2.                                                                                                                                                                   |
|             |             |          |                  | 010          | Gain=4.                                                                                                                                                                   |
|             |             |          |                  | 011          | Gain=8.                                                                                                                                                                   |
|             |             |          |                  | 100          | Gain=16.                                                                                                                                                                  |
|             |             |          |                  | 101          | Gain=32.                                                                                                                                                                  |
|             |             |          |                  | 110          | Gain=64.                                                                                                                                                                  |
|             |             |          |                  | 111          | Gain=128.                                                                                                                                                                 |
+-------------+-------------+----------+------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0021        | filter_0    | [15:12]  | filter_mode[0]   |              | Filter Select for ADC Setup 'n'.                                                                                                                                          |
+-------------+-------------+----------+------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             |             |          |                  | 0000         | SINC4.SINC4 Standalone Filter                                                                                                                                             |
|             |             |          |                  | 0001         | SINC4 + SINC1.Sinc4 Averaging Mode.                                                                                                                                       |
|             |             |          |                  | 0010         | SINC3.SINC3 Standalone Filter                                                                                                                                             |
|             |             |          |                  | 0011         | SINC3 + REJ60.                                                                                                                                                            |
|             |             |          |                  | 0100         | SINC3 + SINC1.Sinc3 Averaging Mode.                                                                                                                                       |
|             |             |          |                  | 0101         | SINC3 + Post Filter 1. ODR = 27.27 SPS                                                                                                                                    |
|             |             |          |                  | 0110         | SINC3 + Post Filter 2. ODR = 25 SPS                                                                                                                                       |
|             |             |          |                  | 0111         | SINC3 + Post Filter 3. ODR = 20 SPS                                                                                                                                       |
|             |             |          |                  | 1000         | SINC3 + Post Filter 4. ODR = 16.67 SPS                                                                                                                                    |
+-------------+-------------+----------+------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             |             | [10:0]   | [fs[0]           |              | Filter Select Bits. These bits control the output data rate (ODR) of the ADC for Setup 'n'.                                                                               |
|             |             |          |                  |              | FS=0 is treated as FS=1.                                                                                                                                                  |
+-------------+-------------+----------+------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===Notice===

-  For configuring the FS, AD4131 only provides a sampling frequency less than 10 sps for Sinc4 Standalone and averaging filters, any value set in the ACE with fs higher than 10 would be automatically run in 10 sps.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval-AD4130/screenshot_2021-04-09_122834.png
   :width: 600px
