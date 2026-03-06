Vector Generation
=================

ACE includes a vector generation tool accessible from the left side menu.

This wiki page aims to show how to use it to create vectors. Refer to your device plug-in manual on how to download them to the device under test.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-side-menu.png
   :align: center
   :width: 100px

Available vector types
----------------------

By default, ACE enables users to generate:

-  DC Vectors : output a constant value

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-dc-waveform.png
   :align: center
   :width: 400px

-  Single Tone Vectors : output a sine wave

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-single-tone-waveform.png
   :align: center
   :width: 400px

-  Square Vectors : output a square wave

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-square-waveform.png
   :align: center
   :width: 400px

-  Triangle Vectors : output a triangle wave

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-triangle-waveform.png
   :align: center
   :width: 400px

-  Sawtooth Vectors : output a sawtooth wave

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-sawtooth-waveform.png
   :align: center
   :width: 400px

-  Chirp Vectors : output a sine wave whose fundamental frequency changes over time

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-chirp-waveform.png
   :align: center
   :width: 400px

-  Noise Vectors : output Gaussian or uniform noise signal

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-noise-waveform.png
   :align: center
   :width: 400px

-  Multi Tone Vectors : output a waveform composed of multiple sine waves

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-multi-tone-waveform.png
   :align: center
   :width: 400px

ACE also enables users to load custom vectors through different format of files:

-  Text Files : One numerical sample value per line. Values are parsed as double precision floating point values (integer values are parsed correctly). Complex (In-phase/Quadrature) vectors can be contained in one file with I/Q values interleaved or into two separate files one for I values and one for Q values.
-  Hex Files : One hexadecimal sample value per line. Values are parsed as short integer or unsigned short integer values. Complex (In-phase/Quadrature) vectors can be contained in one file with I/Q values interleaved or into two separate files one for I values and one for Q values.
-  ACE Files : Device data captures that have been saved with ACE.

Generating a vector
-------------------

The vector generator tool is composed of three panes:

-  ADD : Navigate through and select the types of vectors to generate. Add as many vectors of the same type or different types as you want.
-  GENERATE : Name and configure the vectors to generate.
-  PREVIEW : Get a time and frequency domain preview of the generated vector

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-start-window.png
   :align: center
   :width: 800px

ADD
~~~

Vector types are organized into groups. The two default groups are:

-  Common : containing the different waveforms listed above.
-  File : containing the different file formats listed above.

Groups can be expanded/collapsed using the arrow on the right of the group name.

Each vector type and file format available is on single line in their group. The (i) icon, when hovered over, provides information about the vector type or file format. The (+) icon, when clicked, adds the vector type or file format to the list of vectors to generate.

Users can search for vector types or file formats using the search box at the top of the groups.

The ADD pane can be expanded/collapse using the arrow at the right of the "ADD" title.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-add-pane.png
   :align: center
   :width: 400px

GENERATE
~~~~~~~~

After clicking the (+) icon on a vector type or file format, a vector's configuration group will be added to the GENERATE pane.

Here is an example for a single tone vector added:

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-generate-pane.png
   :align: center
   :width: 400px

All vectors have common features:

-  Name : rename the vector to be easily identifiable when used in device plug-ins. By default, the name is Vector#x where x is the current number of vectors generated.
-  Trash can icon : when clicked, the vector will be deleted from the generated vectors list and won't be usable in device plug-ins.
-  Preview button : when clicked, the vector data will be drawn in the PREVIEW pane.
-  Copy button : when clicked, an exact copy of the vector will be created.
-  Export button : when clicked, the vector data can be saved as a txt file with one sample value per line. Complex vectors' sample values are interleaved.

Vectors' configuration groups can be expanded/collapsed using the arrow at the right of the vectors' names.

The GENERATE pane can be expanded/collapsed by clicking the arrow at the right of the "GENERATE" title.

All the generated vectors can be deleted at once by clicking the "Clear All Vectors" button at the bottom right of the GENERATE pane.

PREVIEW
~~~~~~~

The PREVIEW pane display a single vector's data in time and frequency domains.

After clicking the preview button on a generated vector, the title of each graph will change to indicate which vector is currently previewed:

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-preview-pane.png
   :align: center
   :width: 400px

In the time domain, the vector data will be zoomed by default to try to match one period of data if possible, otherwise the whole data is displayed by default.

In the frequency domain, the FFT of the vector data will be zoomed by default from 0Hz to half the sampling frequency value.

Both graph has a set of control buttons:

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-preview-control-buttons.png
   :align: center
   :width: 400px

From left to right:

-  Allow zooming on graph by clicking and dragging the mouse over the zone of interest.
-  Allow moving the graph zone of interest (panning) along one or both axes within the current zoom - i.e. time/frequency span and amplitude span are not changed
-  Restrict the direction/axis along which the graph moves when using previous control.
-  Fit the entire data into the graph.
-  Reset graph to the default zoom.
-  Allow users to provide coordinates of the zone of interest to zoom on.
-  Auto zoom based on data content.

Vector configuration
--------------------

All the vectors can be renamed to easily identify them. By default, the name is set to Vector#x where x is the current number of vectors generated.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-vector-configuration-name.png
   :align: center
   :width: 400px

DC Vector
~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-vector-configuration-dc.png
   :align: center
   :width: 400px

The configuration elements are:

-  DC Value : constant value over time that represents the DC waveform.
-  Number of samples : number of times the constant value will be repeated in the output.

Single Tone, Square, Triangle, and Sawtooth Vectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These 4 types of vector share the same configuration elements:

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-vector-configuration-single-tone.png
   :align: center
   :width: 400px

-  Data Rate : sampling frequency of the generated waveform.
-  Desired Frequency : fundamental frequency of the generated waveform. Note that the frequency will be adjusted to the closest frequency that allows the generation of a coherent signal - i.e. continuous from the last sample to the first sample.
-  Resolution : number of bits that defines the peak-to-peak amplitude of the signal.
-  Quantize data : when checked, data samples are generated as integers, otherwise they are generated as double precision floating point values. Refer to your device plug-in to choose the correct option.
-  Record Length : number of samples to generate.
-  Offset : amplitude offset to apply to the signal.
-  Amplitude Control : Option to control the amplitude of the waveform either in decibels or in volts, see options below.
-  Attenuation : When the amplitude control is set to dB, the amplitude of the waveform is set according to its resolution and attenuated by this value in decibels.
-  Peak To Peak Amplitude : When the amplitude control is set to V, the amplitude of the waveform is set through this value.
-  Relative Phase : Phase in degrees to apply to the waveform.
-  Unsigned Data : If checked, the data generated will only contain positive values.
-  Allow even cycle count: If checked, the data generated may contain an even number of periods.
-  Generate Complex Data : If checked, the data generated will contain two waveforms, the In-phase and the Quadrature waveforms.

Chirp Vector
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-vector-configuration-chirp.png
   :align: center
   :width: 400px

The configuration elements are:

-  Data Rate : sampling frequency of the generated waveform.
-  Start Frequency : fundamental frequency at the start of the generated waveform.
-  Stop Frequency : fundamental frequency at the end of the generated waveform.
-  Resolution : number of bits that defines the peak-to-peak amplitude of the signal.
-  Quantize data : when checked, data samples are generated as integers, otherwise they are generated as double precision floating point values. Refer to your device plug-in to choose the correct option.
-  Record Length : number of samples to generate.
-  Offset : amplitude offset to apply to the signal.
-  Amplitude Control : Option to control the amplitude of the waveform either in decibels or in volts, see options below.
-  Attenuation : When the amplitude control is set to dB, the amplitude of the waveform is set according to its resolution and attenuated by this value in decibels.
-  Peak To Peak Amplitude : When the amplitude control is set to V, the amplitude of the waveform is set through this value.
-  Relative Phase : Phase in degrees to apply to the waveform.
-  Unsigned Data : If checked, the data generated will only contain positive values.
-  Generate Complex Data : If checked, the data generated will contain two waveforms, the In-phase and the Quadrature waveforms.

Noise Vector
~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-vector-configuration-noise.png
   :align: center
   :width: 400px

The configuration elements are:

-  Data Rate : sampling frequency of the generated waveform.
-  Resolution : number of bits that defines the peak-to-peak amplitude of the signal.
-  Quantize data : when checked, data samples are generated as integers, otherwise they are generated as double precision floating point values. Refer to your device plug-in to choose the correct option.
-  Record Length : number of samples to generate.
-  Amplitude Control : Option to control the amplitude of the waveform either in decibels or in volts, see options below.
-  Attenuation : When the amplitude control is set to dB, the amplitude of the waveform is set according to its resolution and attenuated by this value in decibels.
-  Peak To Peak Amplitude : When the amplitude control is set to V, the amplitude of the waveform is set through this value.
-  Generate Complex Data : If checked, the data generated will contain two waveforms, the In-phase and the Quadrature waveforms.
-  Unsigned Data : If checked, the data generated will only contain positive values.
-  Noise Type : Determines the type of noise to generate, either Gaussian or uniform.

Multi Tone Vector
~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-vector-configuration-multi-tone.png
   :align: center
   :width: 400px

The configuration elements are:

-  Data Rate : sampling frequency of the generated waveform.
-  Resolution : number of bits that defines the peak-to-peak amplitude of the signal.
-  Quantize data : when checked, data samples are generated as integers, otherwise they are generated as double precision floating point values. Refer to your device plug-in to choose the correct option.
-  Record Length : number of samples to generate.
-  Offset : amplitude offset to apply to the signal.
-  Amplitude Control : Option to control the amplitude of the waveform either in decibels or in volts, see options below.
-  Attenuation : When the amplitude control is set to dB, the amplitude of the waveform is set according to its resolution and attenuated by this value in decibels.
-  Peak To Peak Amplitude : When the amplitude control is set to V, the amplitude of the waveform is set through this value.
-  Relative Phase : Phase in degrees to apply to the waveform.
-  Unsigned Data : If checked, the data generated will only contain positive values.
-  Allow even cycle count: If checked, the data generated will contain an even number of periods.
-  Generate Complex Data : If checked, the data generated will contain two waveforms, the In-phase and the Quadrature waveforms.
-  Number of Sine Waves : number of fundamental frequencies in the waveform to generate. When this number is changed, the number of frequency configuration boxes will be adjusted accordingly.
-  Frequency x : Fundamental frequency to add to the waveform.

TXT File
~~~~~~~~

The txt file vector must have one and only one numerical sample value per line. Values are parsed as double precision floating point values (integer values are parsed correctly). Complex (In-phase/Quadrature) vectors can be contained in one file with I/Q values interleaved or into two separate files one for I values and one for Q values.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-vector-configuration-txtfile.png
   :align: center
   :width: 400px

The configuration elements are:

-  File Format:

Real Vector : One txt file containing the values for a single waveform. Complex - Interleaved : One txt file containing interleaved values for In-phase and Quadrature waveforms. Complex - Separate Files : Two txt files containing values for In-phase and Quadrature waveforms respectively.

-  File Path : path to the first or only txt file to retrieve the data from.
-  Second File Path : path to the second txt file to retrieve the quadrature data from when using “Complex - Separate Files” option.
-  Resolution : informational value that won't impact the data but that can be used by the device plug-in for verification and display purposes.
-  Data Rate : informational value that won't impact the data but that can be used by the device plug-in for verification and display purposes.

Hex File
~~~~~~~~

The hex file vector must have one and only one hexadecimal sample value per line. Values are parsed as short integer or unsigned short integer values. Complex (In-phase/Quadrature) vectors can be contained in one file with I/Q values interleaved or into two separate files one for I values and one for Q values.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-vector-configuration-hexfile.png
   :align: center
   :width: 400px

The configuration elements are:

-  File Format:

Real Vector : One txt file containing the values for a single waveform. Complex - Interleaved : One txt file containing interleaved values for In-phase and Quadrature waveforms. Complex - Separate Files : Two txt files containing values for In-phase and Quadrature waveforms respectively.

-  File Path : path to the first or only hex file to retrieve the data from.
-  Second File Path : path to the second hex file to retrieve the quadrature data from when using “Complex - Separate Files” option.
-  Resolution : informational value that won't impact the data but that can be used by the device plug-in for verification and display purposes.
-  Data Rate : informational value that won't impact the data but that can be used by the device plug-in for verification and display purposes.
-  Unsigned Data : If checked, the data will be parsed as positive values only.

ACE File
~~~~~~~~

The ACE file format is the one used when device data captures are saved with ACE. For example, you could capture data from an ADC device and then re-play this captured data on a DAC device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/vector-generator-vector-configuration-acefile.png
   :align: center
   :width: 400px

The configuration elements are:

-  File Path : path to the csv file from capture.

Saving the vector generator state
---------------------------------

Everything done in the vector generator can be saved as part of an ACE session file. The session will contain all the configuration elements and ACE will regenerate all the vectors based on this configuration when the session file is loaded.
