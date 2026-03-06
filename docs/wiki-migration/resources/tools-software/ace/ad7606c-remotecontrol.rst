AD7606B/C ACE remote control
============================

By using :doc:`ACE Remote Control </wiki-migration/resources/tools-software/ace/remotecontrol>`, AD7606B and AD7606C plug-ins can be automated to perform several evaluation activities across the different analog input ranges, bandwidth modes, channels, etc. Different example code are given on the MATLAB examples section.

Without hardware, the :adi:`AD7606x Family software model <en/products/ad7606b.html#product-tools>` can be used to try different configurations for both AD7606C and AD7606B: sampling rate, RC filtering, oversampling, calibration; and analyze frequency response, noise performance, interface timing or power consumption, among others.

All the below features can also be tested by using the :doc:`MBed Example Code </wiki-migration/resources/tools-software/product-support-software/ad7606_mbed_iio_application>`, that makes use of No-OS drivers and interface with SDP-K or STM32 Nucleo boards.

Getting Started
---------------

Hardware
~~~~~~~~

-  :adi:`SDP-H Controller board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-h1.html>` and its 12V DC wall adapter
-  :adi:`AD7606C Evaluation Board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad7606c-18.html>` or an equivalent board that has any of the following ADCs

   -  AD7606B
   -  AD7606C-18
   -  AD7606C-16

Software
~~~~~~~~

-  :adi:`ACE software <en/design-center/evaluation-hardware-and-software/ace-software.html>`
-  AD7606B or AD7606C ACE plugin can be downloaded from within ACE environment, through the plug-in manager section
-  A MATLAB or python environment.

ACE Environment
---------------

Refer to the :adi:`AD7606C Evaluation Board user guide <media/en/technical-documentation/user-guides/eval-ad7606c-fmcz-ug-1870.pdf>` on powering the board up and setting up the ACE plugin. Please make sure that the plugin is functional and the device responds to the plugin interaction before proceeding further.

Setting up communication with ACE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Open ACE, then go to Settings.
-  Go to IPC Server Tab and ensure that it is enabled. Also ensure that a port is allocated.

::

                {{ :resources:tools-software:ace:ipcserver.png?400 |}}

Recording macros
----------------

Start recording macros as explained on :doc:`Recording a macro </wiki-migration/software-tools/ace/recording-macros>` wiki page

Editing macros in MATLAB
------------------------

The code generated on previous section can be imported into MATLAB, and it works to set the exact configuration loaded during the macro recording. In order to give ACE an extra layer of flexibility, the execute_macro function created can be edited to perform repetitive task. For example, an 'AD7606C configuration' macro can be easily recorded with the macro recording tool. This macro could fully configure the AD7606C device: mode, range, OSR, reference, data interface, throughput, etc.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/execute_macro.jpg
   :align: center
   :width: 400px

In order to automate operations:

-  Each of the parameters used (strings) can be replaced by variables that can be managed in the main code.

::

   *These variables would then be input parameters to the function, along with 'Client'
   *Several macros can be recorded, and each of them used as a 'function'. So the 'execute_macro' function can be renamed to a more intuitive name.

Explore each of the following MATLAB scripts to see different functions created to automate tests, e.g.: configure_ad7606c(), run_capture(), get_config(), etc.

MATLAB examples
---------------

.. important::

   Copyright © 2020 by Analog Devices, Inc. All rights reserved. This software is proprietary to Analog Devices, Inc. and its licensors. This software is provided on an “as is” basis without any representations, warranties, guarantees or liability of any kind. Use of the software is subject to the terms and conditions of the Clear BSD License ( https://spdx.org/licenses/BSD-3-Clause-Clear.html ).


.. admonition:: Download
   :class: download

   
   `ad7606x-matlab-example-code.zip <https://wiki.analog.com/_media/resources/tools-software/ace/ad7606x-matlab-example-code.zip>`__


Along the different examples, a set of variables are used to define the AD7606C configuration:

::

   ***generic**            →Either AD7606B, AD7606C-18 or AD7606C-16, depending on the Hardware used
   ***mode**                →True=Software mode; False=Hardware mode
   ***range**              →range=3-->+/-10V Single Ended Range, see register summary in datasheet
   ***ref_sel**            →True= Internal Reference; False = External reference
   ***par_serb**           →True=Parallel Interface; False = Serial Interface
   ***throughput**         → sample frequency in kSPS
   ***no_samples**            →number of samples on each DataSet
   ***OSR**                  → Oversampling Ratio= 2^OSR
   ***sdo_lines**          → number of SDO lines, in serial interface
   ***graph**             →Either 'histogram, 'waverform' or 'FFT

Oversampling Benefits
~~~~~~~~~~~~~~~~~~~~~

The benefits of oversampling are the increased noise performance at the expense of reducing the throughput rate. This can be seen through DC Histograms. So, in order to validate Oversampling feature

-  Tie the inputs Vx+ and Vx- together, to AGND.
-  Start ACE and navigate to Analysis tab.
-  Store the OversamplingSweep.m file in your C:\\ drive
-  Open the OversamplingSweep.m in MATLAB and hit run

The script runs through all possible oversampling ratios and shows the histogram of codes of all channels.


|image1|

.. warning::

   This validation method is not valid for Unipolar single-ended ranges: 0 to 5V, 0 to 10V and 0 to 12.5V because tying the inputs to AGND may saturate the ADC. Tie them to a DC level instead


.. note::

   If you are rather visualizing the Waveform or FFT on the screen instead of the Histogram, modify the script and assign the graph variable with either 'waveform' or 'FFT'. Make sure the correct columns are loaded after 'readtable' function by exploring the .csv files


Offset calibration
~~~~~~~~~~~~~~~~~~

AD7606B and AD7606C have on chip offset calibration, that eliminates any offset caused externally for example because of a mismatch on the external resistors.


|image2|

In order to validate the offset calibration:

-  Place the required external front-end resistors and/or caps (e.g. RC filter)
-  Tie the evaluation board inputs Vx+ and Vx- together, to AGND, or the expected 0V level.
-  Start ACE and navigate to Analysis tab.
-  Store the OffsetCalibration.m file in your C:\\ drive
-  Open the OffsetCalibration.m in MATLAB and hit run

The script displays the data gathered before and after offset calibration.


|image3|

.. warning::

   This validation method is not valid for Unipolar single-ended ranges: 0 to 5V, 0 to 10V and 0 to 12.5V because tying the inputs to AGND may saturate the ADC. Tie them to a DC level instead


.. note::

   If you are rather visualizing the Waveform or FFT on the screen instead of the Histogram, modify the script and assign the graph variable with either 'waveform' or 'FFT'


Gain calibration
~~~~~~~~~~~~~~~~

AD7606B and AD7606C have on chip gain calibration, that eliminates any gain error caused by the external resistors

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/ad7606b_gaincal.png
   :align: center
   :width: 400px

In order to validate the offset calibration:

-  Place the required external front-end resistors and/or caps (e.g. RC filter) on one channel
-  Connect a sinewave signal to the desired channel input/s Vx+ and Vx-
-  Start ACE and navigate to Analysis tab.
-  Store the OffsetCalibration.m file in your C:\\ drive
-  Open the OffsetCalibration.m in MATLAB
-  Look up the ch_num variable and update it with the channel number that has the external resistors
-  Look up the Rfilter variable and update it with the resistor value used (in Ω)
-  Run the script

The script displays the data gathered before and after gain calibration. The example below shows the same signal on two channels, CH1 has no resistors in front of the AD7606C-16 while CH8 has a 10kΩ in front of both V8+ and V8-. The two subplots show the CH8 attenuated because of the external resistor, on the left, and the ADC output when the gain errors is calibrated. CH1 is shown for reference.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/ad7606c_gaincalcal_waveform.png
   :align: center
   :width: 1400px

.. warning::

   Gain calibration feature is not available for Unipolar single-ended ranges: 0 to 5V, 0 to 10V and 0 to 12.5V


Phase calibration
~~~~~~~~~~~~~~~~~

Having an RC filter does not only impact the gain error but the phase error, due to its time constant. In order to validate the phase calibration feature:

-  Place the required external RC filter on one channel
-  Connect a sinewave signal to the desired channel input/s Vx+ and Vx- and at least one more channel, without RC filter
-  Start ACE and navigate to Analysis tab.
-  Store the PhaseCalibration.m file in your C:\\ drive
-  Open the PhaseCalibration.m in MATLAB, look up the ch_num variable and update with the channel number that has the external RC filter
-  Run the script

Open Circuit Detection
~~~~~~~~~~~~~~~~~~~~~~

AD7606B and AD7606C have on-chip Open Circuit Detection features, capable to detect if the analog input signal has been disconnected. A resistor (RPD > 20kΩ) in parallel to the input source is required, as shown on the diagram:

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/ad7606c_opendetectsch.png
   :align: center
   :width: 400px

There are two modes of operation, automatic and manual mode.

In order to validate the **Automatic Open Circuit Detection**, follow the steps:

-  (*optional*) Place the required external RC, if any, through the provided placeholders (check the board schematic)
-  Populate the RPD resistor on one channel, through the provided placeholders (check the board schematic)
-  Connect a sinewave or DC signal to the desired channel input's Vx+ and Vx- test points (or P8/P10 connectors)
-  Start ACE and navigate to Analysis tab.
-  Store the OpenCircuitAutoMode.m file in your C:\\ drive
-  Open the OpenCircuitAutoMode.m in MATLAB
-  Look up the 'ch_num' and 'queue' variables, and update them with the channel under test and a queue size greater than 5
-  Run the script

The script gathers sets of data, whose size is defined by the variable no_samples. It will continuously gather and plot ADC data on the figure window (overwriting every time). Eventually, if the source signal is disconnected from the board's input, the script will stop and show the last set of data gathered on the figure window. Observe how the ADC output has dropped to near zero and MATLAB's Command Window displays the message:

*Channel Disconnected*

In order to verify the **Manual Mode**, follow the same steps as above, but run the OpenCircuitManualMode.m script instead. After some time, disconnect the analog input signal. In this case, when the ADC output code drops below a certain threshold (see flowchart on the datasheet), the script will change the PGA common mode. If the ADC output code varies, as shown in the below graph, it implies the analog input signal has been disconnected, so the '*Channel Disconnected*' message will be displayed on the Command Window.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/ad7606c_od_manualmode.png
   :align: center
   :width: 400px

However, if the analog input signal amplitude is lowered below the threshold, the script will still trigger. Then the PGA common mode will be changed, but the ADC output will be unaltered. In that case, the script will effectively decide that the analog input was not disconnected and therefore will keep working until the inputs are indeed disconnected.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/ad7606c_od_manualmode_connected.png
   :align: center
   :width: 400px

.. important::

   Note that the Open Circuit Detection features only work on the bipolar input ranges and Vx- needs to be tied to ground


.. tip::

   Feel free to consult :ez:`Analog Devices Engineer-Zone <data_converters/precision_adcs>` for additional support.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/ace/ad7606c18_oversampling.png
   :width: 1000px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/ace/ad7606b_offsetcal.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/ace/ad7606c_offsetcal_histo.png
   :width: 800px
