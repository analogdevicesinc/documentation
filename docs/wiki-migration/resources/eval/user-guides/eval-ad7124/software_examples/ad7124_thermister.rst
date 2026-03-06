Thermistor Demo
===============

For this thermistor demo, a 10kΩ (44031) NTC thermistor sensor was used which is specified to measure temperature from -50°C to 150°C. The 44031 has a resistance of 10kΩ at 25°C, 441.117kΩ at -50°C and 237.16Ω at 150°C. This thermistor was chosen as it is a precision thermistor (accuracy of 0.1°C between 0°C and 70°C) and highlights the precision achievable from the AD7124. There are a large number of thermistors available with different accuracies ranging from 0.5°C to 1°C.

Hardware Set-up
---------------

Requirements
~~~~~~~~~~~~

-  Eval+ software installed and open
-  AD7124-4/AD7124-8 evaluation board
-  System demonstration platform board (EVAL-SDP-CB1Z)
-  USB cable
-  PC running Windows with USB 2.0 port
-  10kΩ 44031 NTC thermistor
-  Sensor voltage measured across AIN2-AIN3
-  10kΩ precision resistor

The configuration for the thermistor circuit is shown below. The thermistor is connected in series with the reference resistor in a voltage divider configuration. The internal 2.5V reference of the AD7124 is connected to the top side of the thermistor. The bottom side of the reference resistor is connected to AVss. The precision resistor is used to calculate the current through the thermistor.

Due to the high resistance of the thermistor at low temperatures, voltage excitation is used rather than current excitation. The lowest possible excitation current provided by the AD7124 would generate a voltage greater than [AVdd - AVss].

<fc #ff0000>Get high quality figure</fc>


|image1|

Jumper Positions
~~~~~~~~~~~~~~~~

See layout below for jumper locations

-  **LK1** noise test jumper must be **removed**.
-  **LK4** jumper between REFIN- and AVss must be **in**.
-  **LK6** (position B) is used to apply external 2.5V or internal 2.5V to REFIN+.

All other jumpers in their default positions, see `Hardware Link Options <https://wiki.analog.com/resources/eval/user-guides/eval-ad7124/eval-ad7124/hardware_guide/link_opt>`__

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_layout_thermistor.png
   :width: 600px

Software
--------

Below details the procedure for setting up the Eval software to perform a thermistor measurement. For information opening the Eval+ software see: `Launching the Software <https://wiki.analog.com/resources/eval/user-guides/eval-ad7124/software/launch_software>`__.

Once the software has been launched and the evaluation board is selected the, configuration tab of Eval+ software (shown below) should be displayed. For full information on the Eval+ software please go to the `Eval+ Guide <https://wiki.analog.com/resources/eval/user-guides/eval-ad7124/software/eval_plus>`__ section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_homepage_thermistor.png
   :width: 600px

Thermistor (1)
~~~~~~~~~~~~~~

In order to configure the evaluation board for the thermistor measurement demo, click the **thermistor** button. This configures the device to the following settings:

-  AINP_0 is set to AIN2
-  AINM_0 is set to AIN3
-  Channel_0 is enabled
-  Output data rate is set to 50 SPS. FS_0 = 384 <fc #ff0000>CHECK THIS</fc>
-  Digital filter is set to sinc4
-  Full power mode of operation
-  Programmable gain set to 1.
-  The internal 2.5V Reference is selected
-  Offset is the default factory value following a reset and the device is in bipolar mode.
-  Reference buffers and Analog input buffers enabled
-  Single Capture mode is enabled

Tutorial Access (2)
~~~~~~~~~~~~~~~~~~~

For quick access to the tutorial click the blue question mark icon next to the Thermistor button

Sampling mode (3)
~~~~~~~~~~~~~~~~~

-  Setting this to **single capture** causes a single batch of samples to be collected
-  Setting the program to **repeated capture** causes the software to continuously capture batches of samples from the ADC when sample is clicked.
-  Setting this to **data logging** causes the samples to be written to a file. Upon pressing sample in this mode, a dialog box will appear allowing the file name and save location to be set.

Required Samples (4)
~~~~~~~~~~~~~~~~~~~~

To select the number of samples required from the ADC in a batch, enter the value in the samples box. Default value is 100 samples.

Sample (5)
~~~~~~~~~~

The sample button sends the configuration to the evaluation board and initiates the data collection effort.

While the software is communicating with the board and retrieving the data, the window below will be displayed


|image2|

Waveform Tab
^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_waveform_thermocouple.png
   :width: 600px

Following the completion of the test, the waveform tab will display the the gathered samples. The plot shows each successive sample of the ADC (input referred). Indicators on the right of the screen show the channels being converted. These conversions can be displayed as codes, degrees or as volts (1). Navigation tools are provided to allow zooming and panning.

The **analysis** section (2) displays key parameters for the current batch of samples including; *peak-to-peak noise* and *rms noise*. When several analog input channels are enabled, a channel can be selected for analysis by selecting it in the drop down menu (3).

Histogram Tab
^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_histogram_thermocouple.png
   :width: 600px

This tab shows the histogram analysis. Similar to the waveform tab, the ability to pan, scroll and zoom are provided. For changing the channel being shown, select the desired channel from the drop down menu. The data can be displayed as volts or as codes in the graph configuration section.

Saving the conversion data
^^^^^^^^^^^^^^^^^^^^^^^^^^

To **save the conversion data** into an Excel file, right-click the waveform graph and select Export Data from the drop-down list that appears. A save dialog box displays, prompting the user to save the data to an appropriate folder location.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/thermistor_circuit.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_test_underway.png
   :width: 400px
