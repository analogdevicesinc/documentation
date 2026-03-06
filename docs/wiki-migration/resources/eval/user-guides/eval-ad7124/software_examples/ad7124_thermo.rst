Thermocouple Demo
=================

The voltage generated across the thermocouple is measured with respect to an absolute reference, for example this reference is the internal reference.

Hardware Set-up
---------------

Requirements
~~~~~~~~~~~~

-  Eval+ software installed and open
-  AD7124-4/AD7124-8 evaluation board
-  System demonstration platform board (EVAL-SDP-CB1Z)
-  USB cable
-  PC running Windows with USB 2.0 port
-  Thermocouple type T
-  Sensor voltage measured across AIN2-AIN3
-  5.11kΩ precision resistor
-  250Ω resistor for headroom on the REFIN- buffer.

Shown in the diagram are the connections used for the measurement. Thermocouple itself is connected to A2 connector on the EVAL Board. This connector is connected to analog pins AIN2 and AIN3.

A thermistor or a RTD is connected between AIN4 and AIN5 used for the cold junction measurement, this uses a ratiometric configuration where the reference is provided externally from one of the on chip precision excitation currents and a precision resistor across the REFIN1(+/-).

In this example a thermistor is used (R28) which is connected across AIN4 and AIN5. The cold junction compensation measurement uses a ratiometric configuration where the 500μA on-chip excitation current is used to excite the thermistor. This current is also connected across the 5.11kΩ precision resistor.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/thermocouple_circuit.png
   :width: 400px

Jumper Positions <fc #ff0000>Check THIS</fc>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See layout below for jumper locations

-  **LK1** noise test jumper must be **removed**.
-  **LK3** (position A [<fc #ff0000>IS THIS CORRECT</fc>]) jumper to select REFIN- source from either J1 or J2.
-  **LK4** jumper between REFIN- and AVss must be **removed**.
-  **LK5** (position B) jumper to select REFIN+ source from either J1 or J2.
-  **LK6** is used to apply external 2.5V or internal 2.5V to REFIN+ must be **removed**.

All other jumpers in their default positions, see `Hardware Link Options <https://wiki.analog.com/resources/eval/user-guides/eval-ad7124/eval-ad7124/hardware_guide/link_opt>`__

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_layout_rtd.png
   :width: 600px

Software Set-up
---------------

Below details the procedure for setting up the Eval software to perform a Thermocouple measurement. For information opening the Eval+ software see: `Launching the Software <https://wiki.analog.com/resources/eval/user-guides/eval-ad7124/software/launch_software>`__.

Once the software has been launched and the evaluation board is selected the, configuration tab of Eval+ software (shown below) should be displayed. For full information on the Eval+ software please go to the `Eval+ Guide <https://wiki.analog.com/resources/eval/user-guides/eval-ad7124/software/eval_plus>`__ section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_homepage_thermocouple.png
   :width: 600px

Thermocouple (1)
~~~~~~~~~~~~~~~~

In order to configure the evaluation board for the Thermocouple measurement demo, click the **Thermocouple** button. This configures the device to the following settings:

-  AINP_0 is set to AIN2
-  AINM_0 is set to AIN3
-  AINP_1 is set to AIN4
-  AINM_1 is set to AIN5
-  Channel_0 (Thermocouple) and Channel_1(Cold junction) is enabled
-  Output data rate is set to 50 SPS. FS_0 = 384
-  Digital filter is set to sinc4
-  Full power mode of operation
-  Programmable gain set to 128.
-  The internal reference selected for channel 0.
-  REFIN1(+/-) is enabled for channel 1 and uses the precision resistor.
-  Offset is the default factory value following a reset and the device is in bipolar mode.
-  Reference buffers enabled for channel 1
-  AIN1 is enabled to IOUT0 and set to 500µA

Tutorial Access (2)
~~~~~~~~~~~~~~~~~~~

For quick access to the tutorial click the blue question mark icon next to the Thermocouple button

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


|image1|

Waveform Tab
^^^^^^^^^^^^

|image2| Following the completion of the test, the waveform tab will display the the gathered samples. The plot shows each successive sample of the ADC (input referred). Indicators on the right of the screen show the channels being converted. These conversions can be displayed as codes, degrees or as volts (1). Navigation tools are provided to allow zooming and panning.

The **analysis** section (2) displays key parameters for the current batch of samples including; *peak-to-peak noise* and *rms noise*. When several analog input channels are enabled, a channel can be selected for analysis by selecting it in the drop down menu (3).

Histogram Tab
^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_histogram_thermocouple.png
   :width: 600px

This tab shows the histogram analysis. Similar to the waveform tab, the ability to pan, scroll and zoom are provided. For changing the channel being shown, select the desired channel from the drop down menu. The data can be displayed as volts or as codes in the graph configuration section.

Saving the conversion data
^^^^^^^^^^^^^^^^^^^^^^^^^^

To **save the conversion data** into an Excel file, right-click the waveform graph and select Export Data from the drop-down list that appears. A save dialog box displays, prompting the user to save the data to an appropriate folder location.

:doc:`Return to Software Examples </wiki-migration/resources/eval/user-guides/eval-ad7124/software_examples>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_test_underway.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_waveform_thermocouple.png
   :width: 600px
