AD7124 Eval+ Demo Modes
=======================

Requirements
------------

-  Eval+ software installed and open
-  AD7124-4/AD7124-8 evaluation board
-  System demonstration platform board (EVAL-SDP-CB1Z/EVAL-SDP-CK1Z)
-  USB cable
-  PC running Windows with USB 2.0 port

Noise Test Demo
~~~~~~~~~~~~~~~

While the AD7124-4/AD7124-8 is a 24-bit ADC, there will be noise or flicker in the LSBs. This is expected for sigma delta converters. The noise test measures the noise for an externally shorted input. The magnitude of the noise is dependent on the output data rate, gain and filter type selected. For a shorted input, the noise of the AD7124-4/AD7124-8’s internal blocks only are measured i.e. the ADC core and the PGA. Note that for a shorted input, the reference (internal or external) does not contribute to the noise measurement. The reference noise becomes important for non-zero inputs.

Hardware Set-up
^^^^^^^^^^^^^^^

Jumper positions
""""""""""""""""

See layout below for jumper locations

-  **LK1** noise test jumper must be in place
-  **LK4** jumper between REFIN- and AVss must be in place
-  **LK6** in **A** position is used to apply external 2.5V to REFIN+

All other jumpers in their default positions, see :doc:`Hardware Link Options </wiki-migration/resources/eval/user-guides/ad7124/hardware_guide>`


|image1|

Software Procedure
^^^^^^^^^^^^^^^^^^

Below details the procedure for setting up the Eval software to perform a noise test. For information opening the Eval+ software see: :doc:`Quick Start Guide </wiki-migration/resources/eval/user-guides/ad7124>` Once the software has been launched and the evaluation board is selected the, configuration tab of Eval+ software (shown below) should be displayed. For full information on the Eval+ software please go to the :doc:`Eval+ Software Windows </wiki-migration/resources/eval/user-guides/ad7124/software>` section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_homepage_noise_test.png
   :width: 600px

Noise test (1)
""""""""""""""

In order to configure the evaluation board for the Noise test demo, click the **Noise Test** button. This configures the device to the following settings:

================ ================ ==============
Section          Setting          Value
================ ================ ==============
**Channel 0**    Enabled          True
\                AINP_0           AIN0
\                AINM_0           AIN1
\                Setup            Setup 0
**Setup 0**                       
\                PGA_0            1
\                AIN_BUFP_0       Enabled
\                AIN_BUFM_0       Enabled
\                BIPOLAR          Enabled
\                Filter Mode      Sinc4
\                Output Data Rate 9.38sps
**ADC Control**                   
\                Conversion Mode  Single Capture
\                Power Mode       Full Power
**IO Control 1**                  
\                IOUT0 Select     Off
\                IOUT1 Select     Off
================ ================ ==============

Tutorial Access (2)
"""""""""""""""""""

For quick access to the tutorial click the blue question mark icon next to the Noise Test button

External Reference (3)
""""""""""""""""""""""

The external reference is set to 2.5V by default, if a different external reference is used, fill in this value in the box.

Sampling mode (4)
"""""""""""""""""

-  Setting this to **single capture** causes a single batch of samples to be collected.
-  Setting the program to **repeated capture** causes the software to continuously capture batches of samples from the ADC when sample is clicked.
-  Setting this to **data logging** causes the samples to be written to a file. Upon pressing sample in this mode, a dialog box will appear allowing the file name and save location to be set.

Required Samples (5)
""""""""""""""""""""

To select the number of samples per batch required from the ADC in a batch, enter the value in the samples box. Default value is 100 samples

Sample (6)
""""""""""

The sample button sends the configuration to the evaluation board and initiates the data collection effort.

While the software is communicating with the board and retrieving the data, the window below will be displayed


|image2|

Waveform Tab
^^^^^^^^^^^^

Following the completion of the test, the waveform tab will display the the gathered samples. The plot shows each successive sample of the ADC (input referred). Indicators on the right of the screen show the channels being converted. These conversions can be displayed as codes or as volts

The **analysis** section displays key parameters for the current batch of samples including; *peak-to-peak noise* and *rms noise*. More information on the :doc:`waveform tab can be found here </wiki-migration/resources/eval/user-guides/ad7124/software>`

Histogram Tab
^^^^^^^^^^^^^

The data histogram graph shows the number of times each sample of the ADC output occurs. More information on the :doc:`histogram tab can be found here </wiki-migration/resources/eval/user-guides/ad7124/software>`

Saving the conversion data
^^^^^^^^^^^^^^^^^^^^^^^^^^

To **save the conversion data** into an Excel file, right-click the waveform graph and select Export Data from the drop-down list that appears. A save dialog box displays, prompting the user to save the data to an appropriate folder location.

2 Wire RTD Demo
~~~~~~~~~~~~~~~

The AD7124-4/8 offers programmable precision current sources for use with RTD sensors. In 2-wire RTD mode a single current source is required and this current can be made available on any AINx pin. Due to the error associated with lead resistance 2-wire RTD configurations should only be used when lead wires are short to minimize the error.

.. _hardware-set-up-1:

Hardware Set-up
^^^^^^^^^^^^^^^

Specific Requirements
"""""""""""""""""""""

-  2-wire Pt100 RTD sensor
-  Sensor voltage measured across AIN2-AIN3
-  5.11kΩ precision resistor
-  250Ω resistor for headroom on the REFIN- buffer.

The configuration for the 2-wire RTD circuit is shown below. The current flows through RL1, the RTD and RL2. The voltage generated is sensed across AIN2 and AIN3. In this configuration RL1 and RL2 will add errors as they are in series with the RTD. To minimize this error, ensure that lead wires are as short as possible.

This current also flows through the precision 5.11kΩ resistor. The resistor is connected across REFIN1+ and REFIN1- which generated the reference voltage for the ADC allowing for a ratiometric configuration.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/2-wire_circuit.png
   :width: 400px

.. _jumper-positions-1:

Jumper positions
""""""""""""""""

See layout below for jumper locations

-  **LK1** noise test jumper must be **removed**.
-  **LK2** Bypass CJ must be **removed**.
-  **LK3** REFIN- from J1 /J2 In **position B** (J1).
-  **LK4** jumper between REFIN- and AVss must be **removed**.
-  **LK5** REFIN+ from J1 /J2 In **position B** (J1).
-  **LK6** is used to apply external 2.5V or internal 2.5V to REFIN+ must be **removed**.

All other jumpers in their default positions, see :doc:`Hardware Link Options </wiki-migration/resources/eval/user-guides/ad7124/hardware_guide>`

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7124/software/ad7124_silk_2wire.png
   :width: 600px

Software
^^^^^^^^

Below details the procedure for setting up the Eval software to perform a 2-Wire RTD measurement. For information opening the Eval+ software see: :doc:`Quick Start Guide </wiki-migration/resources/eval/user-guides/ad7124>`.

Once the software has been launched and the evaluation board is selected the, configuration tab of Eval+ software (shown below) should be displayed. For full information on the Eval+ software please go to the :doc:`Eval+ Software </wiki-migration/resources/eval/user-guides/ad7124/software>` section.


|image3|

2-Wire RTD (1)
""""""""""""""

In order to configure the evaluation board for the 2-wire RTD measurement demo, click the **2-Wire RTD** button. This configures the device to the following settings:

================ ================ ==============
Section          Setting          Value
================ ================ ==============
**Channel 0**    Enabled          True
\                AINP_0           AIN2
\                AINM_0           AIN3
\                Setup            Setup 0
**Setup 0**                       
\                PGA_0            16
\                AIN_BUFP_0       Enabled
\                AIN_BUFM_0       Enabled
\                REF_SEL_0        REFIN1(+/-)
\                REF_BUFP_0       Enabled
\                REF_BUFM_0       Enabled
\                BIPOLAR          Enabled
\                Filter Mode      Sinc4
\                Output Data Rate 50sps
**ADC Control**                   
\                Conversion Mode  Single Capture
\                Power Mode       Full Power
**IO Control 1**                  
\                CH SEL IOUT0     AIN0
\                IOUT0 Select     500uA
\                IOUT1 Select     Off
================ ================ ==============

.. _tutorial-access-2-1:

Tutorial Access (2)
"""""""""""""""""""

For quick access to the tutorial click the blue question mark icon next to the 2-Wire RTD button

Sampling mode (3)
"""""""""""""""""

-  Setting this to **single capture** causes a single batch of samples to be collected
-  Setting the program to **repeated capture** causes the software to continuously capture batches of samples from the ADC when sample is clicked.
-  Setting this to **data logging** causes the samples to be written to a file. Upon pressing sample in this mode, a dialog box will appear allowing the file name and save location to be set.

Required Samples (4)
""""""""""""""""""""

To select the number of samples required from the ADC in a batch, enter the value in the samples box. Default value is 100 samples.

Sample (5)
""""""""""

The sample button sends the configuration to the evaluation board and initiates the data collection effort.

While the software is communicating with the board and retrieving the data, the window below will be displayed


|image4|

.. _waveform-tab-1:

Waveform Tab
^^^^^^^^^^^^

Following the completion of the test, the waveform tab will display the the gathered samples. The plot shows each successive sample of the ADC (input referred). Indicators on the right of the screen show the channels being converted. These conversions can be displayed as codes or as volts

The **analysis** section displays key parameters for the current batch of samples including; *peak-to-peak noise* and *rms noise*. More information on the :doc:`waveform tab can be found here </wiki-migration/resources/eval/user-guides/ad7124/software>`

.. _histogram-tab-1:

Histogram Tab
^^^^^^^^^^^^^

The data histogram graph shows the number of times each sample of the ADC output occurs. More information on the :doc:`histogram tab can be found here </wiki-migration/resources/eval/user-guides/ad7124/software>`

.. _saving-the-conversion-data-1:

Saving the conversion data
^^^^^^^^^^^^^^^^^^^^^^^^^^

To **save the conversion data** into an Excel file, right-click the waveform graph and select Export Data from the drop-down list that appears. A save dialog box displays, prompting the user to save the data to an appropriate folder location.

.. _wire-rtd-demo-1:

3 Wire RTD Demo
~~~~~~~~~~~~~~~

The AD7124-4/8 offers programmable precision current sources for use with RTD sensors. In 3-wire RTD mode, two identically matched current sources are required and this current can be made available on any AINx pin.

.. _hardware-set-up-2:

Hardware Set-up
^^^^^^^^^^^^^^^

.. _specific-requirements-1:

Specific Requirements
"""""""""""""""""""""

-  3-wire Pt100 RTD sensor
-  Sensor voltage measured across AIN2-AIN3
-  5.11kΩ precision resistor
-  250Ω resistor for headroom may be required if a Pt1000 RTD is used with a gain of 1.

The configuration for the 3-wire RTD circuit is shown below. The reference voltage is generated across a precision resistor connected between REFIN1+ and REFIN1- using one of the matched currents. This ensures that the analog input voltage remains ratiometric to the reference voltage.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/3-wire_circuit.png
   :align: center
   :width: 400px

.. _jumper-positions-2:

Jumper positions
""""""""""""""""

See layout below for jumper locations

-  **LK1** noise test jumper must be **removed**.
-  **LK2** Bypass CJ must be **removed**.
-  **LK3** REFIN- from J1 /J2 In **position B** (J1).
-  **LK4** jumper between REFIN- and AVss must be **removed**.
-  **LK5** REFIN+ from J1 /J2 In **position B** (J1).
-  **LK6** is used to apply external 2.5V or internal 2.5V to REFIN+ must be **removed**.

All other jumpers in their default positions, see :doc:`Hardware Link Options </wiki-migration/resources/eval/user-guides/ad7124/hardware_guide>`

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7124/software/ad7124_silk_2wire.png
   :width: 600px

.. _software-1:

Software
^^^^^^^^

Below details the procedure for setting up the Eval software to perform a 3-Wire RTD measurement. For information opening the Eval+ software see: :doc:`Quick Start Guide </wiki-migration/resources/eval/user-guides/ad7124>`.

Once the software has been launched and the evaluation board is selected the, configuration tab of Eval+ software (shown below) should be displayed. For full information on the Eval+ software please go to the :doc:`Eval+ Software </wiki-migration/resources/eval/user-guides/ad7124/software>` section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_homepage_3-wire_rtd.png
   :width: 600px

.. _wire-rtd-1-1:

3-Wire RTD (1)
""""""""""""""

In order to configure the evaluation board for the 3-wire RTD measurement demo, click the **3-Wire RTD** button. This configures the device to the following settings:

================ ================ ==============
Section          Setting          Value
================ ================ ==============
**Channel 0**    Enabled          True
\                AINP_0           AIN2
\                AINM_0           AIN3
\                Setup            Setup 0
**Setup 0**                       
\                PGA_0            16
\                AIN_BUFP_0       Enabled
\                AIN_BUFM_0       Enabled
\                REF_SEL_0        REFIN1(+/-)
\                REF_BUFP_0       Enabled
\                REF_BUFM_0       Enabled
\                BIPOLAR          Enabled
\                Filter Mode      Sinc4
\                Output Data Rate 50sps
**ADC Control**                   
\                Conversion Mode  Single Capture
\                Power Mode       Full Power
**IO Control 1**                  
\                CH SEL IOUT0     AIN0
\                IOUT0 Select     500uA
\                CH SEL IOUT1     AIN1
\                IOUT1 Select     500uA
================ ================ ==============

.. _tutorial-access-2-2:

Tutorial Access (2)
"""""""""""""""""""

For quick access to the tutorial click the blue question mark icon next to the 3-Wire RTD button

.. _sampling-mode-3-1:

Sampling mode (3)
"""""""""""""""""

-  Setting this to **single capture** causes a single batch of samples to be collected
-  Setting the program to **repeated capture** causes the software to continuously capture batches of samples from the ADC when sample is clicked.
-  Setting this to **data logging** causes the samples to be written to a file. Upon pressing sample in this mode, a dialog box will appear allowing the file name and save location to be set.

.. _required-samples-4-1:

Required Samples (4)
""""""""""""""""""""

To select the number of samples required from the ADC in a batch, enter the value in the samples box. Default value is 100 samples.

.. _sample-5-1:

Sample (5)
""""""""""

The sample button sends the configuration to the evaluation board and initiates the data collection effort.

While the software is communicating with the board and retrieving the data, the window below will be displayed


|image5|

.. _waveform-tab-2:

Waveform Tab
^^^^^^^^^^^^

Following the completion of the test, the waveform tab will display the the gathered samples. The plot shows each successive sample of the ADC (input referred). Indicators on the right of the screen show the channels being converted. These conversions can be displayed as codes or as volts

The **analysis** section displays key parameters for the current batch of samples including; *peak-to-peak noise* and *rms noise*. More information on the :doc:`waveform tab can be found here </wiki-migration/resources/eval/user-guides/ad7124/software>`

.. _histogram-tab-2:

Histogram Tab
^^^^^^^^^^^^^

The data histogram graph shows the number of times each sample of the ADC output occurs. More information on the :doc:`histogram tab can be found here </wiki-migration/resources/eval/user-guides/ad7124/software>`

.. _saving-the-conversion-data-2:

Saving the conversion data
^^^^^^^^^^^^^^^^^^^^^^^^^^

To **save the conversion data** into an Excel file, right-click the waveform graph and select Export Data from the drop-down list that appears. A save dialog box displays, prompting the user to save the data to an appropriate folder location.

.. _wire-rtd-demo-2:

4 Wire RTD Demo
~~~~~~~~~~~~~~~

The AD7124-4/8 offers a programmable precision current source for use with 4-wire RTD sensors. In 4-wire RTD mode, a single current source is required and this current can be made available on any AINx pin.

.. _hardware-set-up-3:

Hardware Set-up
^^^^^^^^^^^^^^^

.. _specific-requirements-2:

Specific Requirements
"""""""""""""""""""""

-  4-wire Pt100 RTD sensor
-  Sensor voltage measured across AIN2-AIN3
-  5.11kΩ precision resistor
-  250Ω resistor for headroom

The configuration for the 4-wire RTD circuit is shown below. The reference voltage is generated across a precision resistor connected between REFIN1+ and REFIN1- using the generated current. This ensures that the analog input voltage remains ratiometric to the reference voltage. The voltage generated across the RTD sensor corresponds to the voltage between AIN2 and AIN3. The current flows through RL1 and RL4.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/4-wire_circuit.png
   :align: center
   :width: 400px

.. _jumper-positions-3:

Jumper positions
""""""""""""""""

See layout below for jumper locations

-  **LK1** noise test jumper must be **removed**.
-  **LK2** Bypass CJ must be **removed**.
-  **LK3** REFIN- from J1 /J2 In **position B** (J1).
-  **LK4** jumper between REFIN- and AVss must be **removed**.
-  **LK5** REFIN+ from J1 /J2 In **position B** (J1).
-  **LK6** is used to apply external 2.5V or internal 2.5V to REFIN+ must be **removed**.

All other jumpers in their default positions, see :doc:`Hardware Link Options </wiki-migration/resources/eval/user-guides/ad7124/hardware_guide>`

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7124/software/ad7124_silk_2wire.png
   :align: center
   :width: 600px

.. _software-2:

Software
^^^^^^^^

Below details the procedure for setting up the Eval software to perform a 4-Wire RTD measurement. For information opening the Eval+ software see: :doc:`Quick Start Guide </wiki-migration/resources/eval/user-guides/ad7124>`.

Once the software has been launched and the evaluation board is selected the, configuration tab of Eval+ software (shown below) should be displayed. For full information on the Eval+ software please go to the :doc:`Eval+ Software </wiki-migration/resources/eval/user-guides/ad7124/software>` section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_homepage_4-wire_rtd.png
   :align: center
   :width: 600px

.. _wire-rtd-1-2:

4-Wire RTD (1)
^^^^^^^^^^^^^^

In order to configure the evaluation board for the 4-wire RTD measurement demo, click the **4-Wire RTD** button. This configures the device to the following settings:

================ ================ ==============
Section          Setting          Value
================ ================ ==============
**Channel 0**    Enabled          True
\                AINP_0           AIN2
\                AINM_0           AIN3
\                Setup            Setup 0
**Setup 0**                       
\                PGA_0            16
\                AIN_BUFP_0       Enabled
\                AIN_BUFM_0       Enabled
\                REF_SEL_0        REFIN1(+/-)
\                REF_BUFP_0       Enabled
\                REF_BUFM_0       Enabled
\                BIPOLAR          Enabled
\                Filter Mode      Sinc4
\                Output Data Rate 50sps
**ADC Control**                   
\                Conversion Mode  Single Capture
\                Power Mode       Full Power
**IO Control 1**                  
\                CH SEL IOUT0     AIN0
\                IOUT0 Select     500uA
\                IOUT1 Select     Off
================ ================ ==============

.. _tutorial-access-2-3:

Tutorial Access (2)
"""""""""""""""""""

For quick access to the tutorial click the blue question mark icon next to the 4-Wire RTD button

.. _sampling-mode-3-2:

Sampling mode (3)
"""""""""""""""""

-  Setting this to **single capture** causes a single batch of samples to be collected
-  Setting the program to **repeated capture** causes the software to continuously capture batches of samples from the ADC when sample is clicked.
-  Setting this to **data logging** causes the samples to be written to a file. Upon pressing sample in this mode, a dialog box will appear allowing the file name and save location to be set.

.. _required-samples-4-2:

Required Samples (4)
""""""""""""""""""""

To select the number of samples required from the ADC in a batch, enter the value in the samples box. Default value is 100 samples.

.. _sample-5-2:

Sample (5)
""""""""""

The sample button sends the configuration to the evaluation board and initiates the data collection effort.

While the software is communicating with the board and retrieving the data, the window below will be displayed


|image6|

.. _waveform-tab-3:

Waveform Tab
^^^^^^^^^^^^

Following the completion of the test, the waveform tab will display the the gathered samples. The plot shows each successive sample of the ADC (input referred). Indicators on the right of the screen show the channels being converted. These conversions can be displayed as codes or as volts

The **analysis** section displays key parameters for the current batch of samples including; *peak-to-peak noise* and *rms noise*. More information on the :doc:`waveform tab can be found here </wiki-migration/resources/eval/user-guides/ad7124/software>`

.. _histogram-tab-3:

Histogram Tab
^^^^^^^^^^^^^

The data histogram graph shows the number of times each sample of the ADC output occurs. More information on the :doc:`histogram tab can be found here </wiki-migration/resources/eval/user-guides/ad7124/software>`

.. _saving-the-conversion-data-3:

Saving the conversion data
^^^^^^^^^^^^^^^^^^^^^^^^^^

To **save the conversion data** into an Excel file, right-click the waveform graph and select Export Data from the drop-down list that appears. A save dialog box displays, prompting the user to save the data to an appropriate folder location.

Thermocouple Demo
~~~~~~~~~~~~~~~~~

The voltage generated across the thermocouple is measured with respect to an absolute reference, for example this reference is the internal reference.

.. _hardware-set-up-4:

Hardware Set-up
^^^^^^^^^^^^^^^

.. _specific-requirements-3:

Specific Requirements
"""""""""""""""""""""

-  Thermocouple type T
-  Sensor voltage measured across AIN2-AIN3
-  5.11kΩ precision resistor
-  250Ω resistor for headroom on the REFIN- buffer.

Shown in the diagram are the connections used for the measurement. Thermocouple itself is connected to A2 connector (see the silk screen below) on the EVAL Board. This connector is connected to analog pins AIN2 and AIN3.

A thermistor or a RTD is connected between AIN4 and AIN5 used for the cold junction measurement, this uses a ratiometric configuration where the reference is provided externally from one of the on chip precision excitation currents and a precision resistor across the REFIN1(+/-).

In this example a thermistor is used (R28) which is connected across AIN4 and AIN5. The cold junction compensation measurement uses a ratiometric configuration where the 500μA on-chip excitation current is used to excite the thermistor. This current is also connected across the 5.11kΩ precision resistor.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/thermocouple_circuit.png
   :align: center
   :width: 400px

.. _jumper-positions-4:

Jumper positions
""""""""""""""""

See layout below for jumper locations

-  **LK1** noise test jumper must be **removed**.
-  **LK2** Bypass CJ must be **in place**.
-  **LK3** REFIN- from J1 /J2 In **position B** (J1).
-  **LK4** jumper between REFIN- and AVss must be **removed**.
-  **LK5** REFIN+ from J1 /J2 In **position B** (J1).
-  **LK6** is used to apply external 2.5V or internal 2.5V to REFIN+ must be **removed**.

All other jumpers in their default positions, see :doc:`Hardware Link Options </wiki-migration/resources/eval/user-guides/ad7124/hardware_guide>`

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7124/software/ad7124_silk_theromocouple.png
   :align: center
   :width: 600px

.. _software-3:

Software
^^^^^^^^

Below details the procedure for setting up the Eval software to perform a Thermocouple measurement. For information opening the Eval+ software see: :doc:`Quick Start Guide </wiki-migration/resources/eval/user-guides/ad7124>`.

Once the software has been launched and the evaluation board is selected the, configuration tab of Eval+ software (shown below) should be displayed. For full information on the Eval+ software please go to the :doc:`Eval+ Software </wiki-migration/resources/eval/user-guides/ad7124/software>` section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_homepage_thermocouple.png
   :width: 600px

Thermocouple (1)
^^^^^^^^^^^^^^^^

In order to configure the evaluation board for the Thermocouple measurement demo, click the **Thermocouple** button. This configures the device to the following settings:

================ ================== ==============
Section          Setting            Value
================ ================== ==============
**Channel 0**    Enabled            True
\                AINP_0             AIN2
\                AINM_0             AIN3
**Channel 1**    Enabled            True
\                AINP_1             AIN4
\                AINM_1             AIN5
\                Setup              Setup 0
**Setup 0**                         
\                PGA_0              128
Channel_0        Internal reference True
\                AIN_BUFP_0         Enabled
\                AIN_BUFM_0         Enabled
\                REF_SEL_1          REFIN1(+/-)
\                REF_BUFP_1         Enabled
\                REF_BUFM_1         Enabled
\                BIPOLAR            Enabled
\                Filter Mode        Sinc4
\                Output Data Rate   50sps
**ADC Control**                     
\                Conversion Mode    Single Capture
\                Power Mode         Full Power
**IO Control 1**                    
\                CH SEL IOUT0       AIN1
\                IOUT0 Select       500uA
\                IOUT1 Select       Off
================ ================== ==============

.. _tutorial-access-2-4:

Tutorial Access (2)
"""""""""""""""""""

For quick access to the tutorial click the blue question mark icon next to the Thermocouple button

.. _sampling-mode-3-3:

Sampling mode (3)
"""""""""""""""""

-  Setting this to **single capture** causes a single batch of samples to be collected
-  Setting the program to **repeated capture** causes the software to continuously capture batches of samples from the ADC when sample is clicked.
-  Setting this to **data logging** causes the samples to be written to a file. Upon pressing sample in this mode, a dialog box will appear allowing the file name and save location to be set.

.. _required-samples-4-3:

Required Samples (4)
""""""""""""""""""""

To select the number of samples required from the ADC in a batch, enter the value in the samples box. Default value is 100 samples.

.. _sample-5-3:

Sample (5)
""""""""""

The sample button sends the configuration to the evaluation board and initiates the data collection effort.

While the software is communicating with the board and retrieving the data, the window below will be displayed


|image7|

.. _waveform-tab-4:

Waveform Tab
^^^^^^^^^^^^

Following the completion of the test, the waveform tab will display the the gathered samples. The plot shows each successive sample of the ADC (input referred). Indicators on the right of the screen show the channels being converted. These conversions can be displayed as codes or as volts

The **analysis** section displays key parameters for the current batch of samples including; *peak-to-peak noise* and *rms noise*. More information on the :doc:`waveform tab can be found here </wiki-migration/resources/eval/user-guides/ad7124/software>`

.. _histogram-tab-4:

Histogram Tab
^^^^^^^^^^^^^

The data histogram graph shows the number of times each sample of the ADC output occurs. More information on the :doc:`histogram tab can be found here </wiki-migration/resources/eval/user-guides/ad7124/software>`

.. _saving-the-conversion-data-4:

Saving the conversion data
^^^^^^^^^^^^^^^^^^^^^^^^^^

To **save the conversion data** into an Excel file, right-click the waveform graph and select Export Data from the drop-down list that appears. A save dialog box displays, prompting the user to save the data to an appropriate folder location.

Thermistor Demo
~~~~~~~~~~~~~~~

For this thermistor demo, a 10kΩ (44031) NTC thermistor sensor was used which is specified to measure temperature from -50°C to 150°C. The 44031 has a resistance of 10kΩ at 25°C, 441.117kΩ at -50°C and 237.16Ω at 150°C. This thermistor was chosen as it is a precision thermistor (accuracy of 0.1°C between 0°C and 70°C) and highlights the precision achievable from the AD7124. There are a large number of thermistors available with different accuracies ranging from 0.5°C to 1°C.

.. _hardware-set-up-5:

Hardware Set-up
^^^^^^^^^^^^^^^

.. _specific-requirements-4:

Specific Requirements
"""""""""""""""""""""

-  10kΩ 44031 NTC thermistor
-  Sensor voltage measured across AIN2-AIN3
-  10kΩ precision resistor

Shown in the diagram is the configuration used for this Thermistor demo. The thermistor is connected in series with a precision reference resistor (RSENSE) in a voltage divider configuration. The internal 2.5V reference of the AD7124-4/AD7124-8 is connected to the thermistor top side of the voltage divider and the bottom side of the precision reference resistor is connected to AVSS. The precision resistor, RSENSE is used to calculate the current through the thermistor. Voltage excitation rather than an excitation current is used to excite the thermistor, the reason for this is that as the thermistor has high resistance at low temperatures, (441.117kOhms), therefore and even the lowest excitation current provided by the AD7124-4/8 would generate a voltage greater than (AVDD – AVSS) at these low temperatures.

For this demo the voltage across the thermistor is measured using analog inputs the Ain2 and Ain3 inputs of the AD7124-4/AD7124-8. This voltage is then used to calculate the current through the thermistor [REFOUT/(Vthermistor + Vrsense)] where Vrsense = (REFOUT - Vthermistor) and from this hence the resistance of the thermistor is calculated.

Since the thermistor has higher resistance values at lower temperature, the signal levels are larger (approximately 2.44V at -50°C) thus a gain of 1 is used in this configuration.

As the thermistor and RSENSE are driven from the internal reference and, the internal reference is also used as the reference for the ADC measurement, this gives a ratiometric configuration. This means that any variation of the reference voltage does not affect the system accuracy.


|image8|

.. _jumper-positions-5:

Jumper positions
""""""""""""""""

See layout below for jumper locations

-  **LK1** noise test jumper must be **removed**.
-  **LK2** Bypass CJ must be **removed**.
-  **LK3** REFIN- from J1 /J2 In **position B** (J1).
-  **LK4** jumper between REFIN- and AVss must be **in place**.
-  **LK5** REFIN+ from J1 /J2 In **position B** (J1).
-  **LK6** is used to apply external 2.5V or internal 2.5V to REFIN+ must be in **position B** (internal).

All other jumpers in their default positions, see :doc:`Hardware Link Options </wiki-migration/resources/eval/user-guides/ad7124/hardware_guide>`

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7124/software/ad7124_silk_2wire.png
   :align: center
   :width: 600px

.. _software-4:

Software
^^^^^^^^

Below details the procedure for setting up the Eval software to perform a thermistor measurement. For information opening the Eval+ software see: :doc:`Quick Start Guide </wiki-migration/resources/eval/user-guides/ad7124>`.

Once the software has been launched and the evaluation board is selected the, configuration tab of Eval+ software (shown below) should be displayed. For full information on the Eval+ software please go to the :doc:`Eval+ Software </wiki-migration/resources/eval/user-guides/ad7124/software>` section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7124/software/eval_plus_homepage_thermistor.png
   :align: center
   :width: 600px

Thermistor (1)
""""""""""""""

In order to configure the evaluation board for the Thermistor measurement demo, click the \**Thermistor \*\* button. This configures the device to the following settings:

=============== ================ ==============
Section         Setting          Value
=============== ================ ==============
**Channel 0**   Enabled          True
\               AINP_0           AIN2
\               AINM_0           AIN3
\               Setup            Setup 0
**Setup 0**                      
\               PGA_0            1
\               AIN_BUFP_0       Enabled
\               AIN_BUFM_0       Enabled
\               REF_SEL_0        REFIN1(+/-)
\               REF_BUFP_0       Disabled
\               REF_BUFM_0       Disabled
\               Internal Ref     Enabled
\               BIPOLAR          Enabled
\               Filter Mode      Sinc4
\               Output Data Rate 6.25sps
**ADC Control**                  
\               Conversion Mode  Single Capture
\               Power Mode       Low Power
**IO Control**                   
\               IOUT0 Select     Off
\               IOUT1 Select     Off
=============== ================ ==============

.. _tutorial-access-2-5:

Tutorial Access (2)
"""""""""""""""""""

For quick access to the tutorial click the blue question mark icon next to the Thermistor button

.. _sampling-mode-3-4:

Sampling mode (3)
"""""""""""""""""

-  Setting this to **single capture** causes a single batch of samples to be collected
-  Setting the program to **repeated capture** causes the software to continuously capture batches of samples from the ADC when sample is clicked.
-  Setting this to **data logging** causes the samples to be written to a file. Upon pressing sample in this mode, a dialog box will appear allowing the file name and save location to be set.

.. _required-samples-4-4:

Required Samples (4)
""""""""""""""""""""

To select the number of samples required from the ADC in a batch, enter the value in the samples box. Default value is 100 samples.

.. _sample-5-4:

Sample (5)
""""""""""

The sample button sends the configuration to the evaluation board and initiates the data collection effort.

While the software is communicating with the board and retrieving the data, the window below will be displayed


|image9|

.. _waveform-tab-5:

Waveform Tab
^^^^^^^^^^^^

Following the completion of the test, the waveform tab will display the the gathered samples. The plot shows each successive sample of the ADC (input referred). Indicators on the right of the screen show the channels being converted. These conversions can be displayed as codes or as volts

The **analysis** section displays key parameters for the current batch of samples including; *peak-to-peak noise* and *rms noise*. More information on the :doc:`waveform tab can be found here </wiki-migration/resources/eval/user-guides/ad7124/software>`

.. _histogram-tab-5:

Histogram Tab
^^^^^^^^^^^^^

The data histogram graph shows the number of times each sample of the ADC output occurs. More information on the :doc:`histogram tab can be found here </wiki-migration/resources/eval/user-guides/ad7124/software>`

.. _saving-the-conversion-data-5:

Saving the conversion data
^^^^^^^^^^^^^^^^^^^^^^^^^^

To **save the conversion data** into an Excel file, right-click the waveform graph and select Export Data from the drop-down list that appears. A save dialog box displays, prompting the user to save the data to an appropriate folder location.

4 wire Bridge Demo
~~~~~~~~~~~~~~~~~~

.. _wire-bridge-demo-1:

6 wire Bridge Demo
~~~~~~~~~~~~~~~~~~

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_layout_noise_test.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_test_underway.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_homepage_2-wire_rtd.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_test_underway.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_test_underway.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_test_underway.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_test_underway.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7124/software/thermistor_circuit.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software_examples/eval_plus_test_underway.png
   :width: 400px
