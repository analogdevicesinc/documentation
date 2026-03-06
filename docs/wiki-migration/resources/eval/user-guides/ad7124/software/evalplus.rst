Eval+ Software Windows
======================

Configuration Tab
-----------------

The Configuration tab (Label 1) shows a block diagram of the AD7124-8. It allows the user to set up the ADC, reset the ADC, read the diagnostics to view errors present, as well as configure the device for different demo modes. The Configuration tab is shown in more detail below, along with explanations of the features on this tab.


|image1|

Board Selection (2)
~~~~~~~~~~~~~~~~~~~

This window displays the current mode of operation of the Eval+ Software. Clicking SELECT PRODUCT will allow you to change the Eval+ Software to simulation mode, or alternatively pick another board if there is more then one connected.

Tutorial Button (3)
~~~~~~~~~~~~~~~~~~~

Clicking on this Question Mark button will open up a tutorial on using the software, this give additional information on using the AD7124-8 software.

ADC Reset (4)
~~~~~~~~~~~~~

Click ADC RESET to perform a software reset of the AD7124-8. There is no hardware reset pin on the AD7124-8. To perform a hard reset, remove power from the board. However, the software reset has the same effect as a hard reset.

Summary (5)
~~~~~~~~~~~

Clicking the SUMMARY button (Label 6) displays the channel configuration information on each of the individual setups as well as information on any error present. These tabs can be used to quickly check how the ADC channels are configured, as well as any errors that are present.

Selecting External Reference (6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two options to select the external reference on the AD7124-8 front panel, AVDD and REFIN1(+/-). The REFIN1(+/-). Field sets the external reference voltage that is connected between REFIN1+ and REFIN1-, and the AVDD field is used to set the voltage level of the AVDD voltage for the AD7124-4. Using EVAL-AD7124-8BSDZ eval board the AVDD voltage is 3.3V. Either of these can be used in calculating the results on the Waveform and Histogram tabs. The evaluation board has an external 2.5V ADR4525 reference, which can be bypassed; if bypassing the ADR4525 on board ensure to change the external reference voltage value in REFIN1(+/-) to ensure correct calculation of results in the Waveform and Histogram tabs.

Functional Block Diagram (7)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The functional block diagram of the ADC shows each of the functional blocks within the ADC. Clicking a configuration button on this graph opens the configuration popup window for that block.

Configuration Popup Button (8)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each configuration popup button opens a different window allowing for configuration of the relevant functional block.

Demo Modes (9)
~~~~~~~~~~~~~~

The AD7124-8 software supports a number of demo modes, these demo modes configure the AD7124-8 for each of the modes shown. The is a help file for each demo mode that is available once the question mark is clicked on.

Device Error (10)
~~~~~~~~~~~~~~~~~

The Device Error LED indicates if an overall error is present in the diagnostics register. For this indicator to work, the check for the different diagnostic errors must be enabled in the Error_EN register..

Status Bar (11)
~~~~~~~~~~~~~~~

The status bar displays status updates such as Analysis Completed, Reset Completed, Configuring Demo Mode etc. during software use, as well as the software version and busy indicator.

Waveform Tab
------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/eval_plus_waveform_labels.png
   :align: center
   :width: 600px

The Waveform tab graphs the conversions gathered and processes the data, calculating the peak-to-peak noise, rms noise, and resolution.

Waveform Graph and Controls (1 & 2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The data waveform graph shows each successive sample of the ADC output. Zoom in on the data in the graph using the control toolbar. Change the scales on the graph by typing values into the x-axis and y-axis.

Analysis Channel (3)
~~~~~~~~~~~~~~~~~~~~

The Noise Analysis section and histogram graph show the analysis of the channel selected via the Analysis Channel control.

Samples (4 & 5)
~~~~~~~~~~~~~~~

The Samples numeric control and batch control set the number of samples gathered per batch. Batch control sets whether a single batch or multiple batches of samples are gathered. This control is unrelated to the ADC mode. You can capture a defined sample set or continuously gather batches of samples. In both cases, the number of samples set in the Samples numeric input dictates the number of samples.

Sample (6)
~~~~~~~~~~

Click the SAMPLE button to start gathering ADC results. Results appear in the waveform graph (Label 1).

Channel Selection (7)
~~~~~~~~~~~~~~~~~~~~~

The channel selection control selects which channels display on the data waveform and shows the analog inputs for the channel labeled next to the on and off controls. These controls only affect the display of the channels and have no effect on the channel settings in the ADC register map.

Display Units and Axis Controls (8)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click the Display Units drop-down menu to select whether the data graph displays in units of voltages or codes. This control affects both the waveform graph and the histogram graph. The axis controls switch between dynamic and fixed. When dynamic is selected, the axis automatically adjusts to show the entire range of the ADC results after each batch of samples. When selecting Fixed, the axis ranges can be programmed; however, these ranges do not automatically adjust after each batch of samples.

Device Error (9)
~~~~~~~~~~~~~~~~

The Device Error LED indicates if an overall error is present in the diagnostics register. For this indicator to work, the check for the different diagnostic errors must be enabled in the Error_EN register.

Noise Analysis (10)
~~~~~~~~~~~~~~~~~~~

The Noise Analysis section displays the results of the noise analysis for the selected analysis channel, including both noise and resolution measurements.

Histogram Tab
-------------

The Histogram tab generates a histogram using the gathered samples and processes the data, calculating the peak-to-peak noise, rms noise, and resolution.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/eval_plus_histogram_labels.png
   :align: center
   :width: 600px

Histogram Graph and Controls (1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The data histogram graph shows the number of times each sample of the ADC output occurs. Zoom in on the data using the control toolbar in the graph (5). Change the scales on the graph by typing values into the x-axis and y-axis.

Analysis Channel (2)
~~~~~~~~~~~~~~~~~~~~

The Noise Analysis section and histogram graph show the analysis of the channel selected via the Analysis Channel control.

Noise Analysis (3)
~~~~~~~~~~~~~~~~~~

The Noise Analysis section displays the results of the noise analysis for the selected analysis channel, including both noise and resolution measurements.

Display Units and Axis Controls (4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click the Display Units drop-down box to select whether the data graph displays in units of voltages or codes. This control affects both the waveform graph and the histogram graph. The axis controls can be used to switch between dynamic and fixed range. When Dynamic is selected, the axis automatically adjusts to show the entire range of the ADC results after each batch of samples. When selecting Fixed, the user can program the axis ranges; the axis ranges do not automatically adjust after each batch of samples.

Modelling Performance Tab
-------------------------

The Modelling Performance performance tab uses an ideal model of the AD7124 to give frequency responses based on the users required specifications. It provides the user with key information such as the 'Filter Profile', 'Filter Step Response' and 'Power/Timing Diagrams'.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/eval_plus_model_label.png
   :align: center
   :width: 600px

Model Selection (1)
~~~~~~~~~~~~~~~~~~~

This drop down bar allows the user to select between modelling the filter profile, the step response or the power/timing diagrams. The main graph window (3) will update upon selection.

Channel Selection (2)
~~~~~~~~~~~~~~~~~~~~~

Allows the user to select which channel of the AD7124 they want to get modelling information from.

Waveform Window (3)
~~~~~~~~~~~~~~~~~~~

Shows the results of the requested modelled system. The window can be navigated using the graphing tools in the top right hand corner (4). The results will update on the fly as new information is entered.

Filter Rejection (5)
~~~~~~~~~~~~~~~~~~~~

Filter Performance (6)
~~~~~~~~~~~~~~~~~~~~~~

This window shows the Passband frequency at 3dB, along with the settling time and the notch and ADC frequencies. This values update in real time as the inputs to the filter rejection window (5) change.

Register Map Tab
----------------

Use the Register Map tab to access the registers of the AD7124-8. This tab changes register settings and shows additional information about each bit in each individual register.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/eval_plus_register_map_labels.png
   :align: center
   :width: 600px

Register Map (1)
~~~~~~~~~~~~~~~~

On the top of the tab are the registers of the AD7124-8. Click any register to read the register value. Access each register of the AD7124-8 using the register map.

Search (2)
~~~~~~~~~~

This search bar can be used to search for a particular register or bitfield within the AD7124-8 register map. To use the search bar, enter the register name or bitfield that you want to search for, then clock the 'plus' icon to the left of the Register Maps folder to expand out the folder and show the search results.

Save and Load Buttons (3)
~~~~~~~~~~~~~~~~~~~~~~~~~

The Save and Load buttons on the Register Map tab allow the user to save and load register settings. Click Save to save all the current register settings to a file for later use. Click Load to load a previously saved register map.

Export (4)
~~~~~~~~~~

The export button allows the user to save the current register configuration as a C file. When the export button is clicked, file explorer will be opened and you will be asked where to save the register configuration code for flashing the part at a later time.

Register (5)
~~~~~~~~~~~~

The Register section shows the value that is set in the selected register. Check the value of the register in this window by clicking on the bits. Clicking any individual bit changes the bit from 1 to 0 or 0 to 1, depending on the initial state of the bit. The register value can also be changed by writing the hexadecimal value in the input field to the right of the individual bits.

Documentation (6)
~~~~~~~~~~~~~~~~~

The Documentation section shows information relating to the different bit fields when selected from the register map section on the left. This information is the same information in the AD7124-8 data sheet.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/eval_plus_home_labels.png
   :width: 600px
