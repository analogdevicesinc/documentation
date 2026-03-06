Scopy Signal Generator
======================

Video
-----

.. image:: https://wiki.analog.com/_media/youtube>zWX7VnKDYq4
   :alt: youtube>zWX7VnKDYq4

General Description
-------------------

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_14-57-31.png
   :width: 600px

The signal generator instrument can be used to generate analog output from the M2K with user configurable parameters. It consists of 3 parts:

::

   *Channel selector - enable/disable channels as well as each channel's control panel.
   *Signal Plot - visual representation of the signals
   *Control Panel - change signal paramteres

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_15-25-53.png

Four types of signals can be generated.

-  Constant - DC signal at a user selectable amplitude
-  Waveform - AC signal with various customizable parameters
-  Buffer - signal is imported from a file
-  Math - signal is defined by a mathematical equation

Constant signal only has one parameter which inputs the amplitude of the signal Waveform signal type can be one of the following

-  Sine
-  Square
-  Triangle
-  Trapezoidal
-  Rising sawtooth
-  Falling sawtooth

All signals have amplitude, offset, phase and frequency parameters. Selecting Square wave will also unlock the duty cycle parameter. Selecting trapezoidal waveform will disable the frequency, as this parameter will be computed from the other 4 values in the Timing category (Rise time, High time, Fall time, Low Time)

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_15-29-24.png

Buffer signal type takes a file as an input. The supported file types for buffered signals are:

-  .bin - 32 bit binary float format
-  .wav - Waveform Audio File Format (16 bit integers)
-  .csv - Comma separated values
-  .mat - MATLAB Mat format

CSV file format supports raw CSVs such as https://gist.github.com/adisuciu/7aa30bc9e545db23a17e86d23ae4f53c, as well as Scopy formatted CSVs such as https://gist.github.com/adisuciu/5abffa8233707c7b95585e80fbb1dde9. This means it is possible to acquire a signal in the oscilloscope and play it back in the signal generator.



.. raw:: html

   <details><summary>Click to expand XHIDDENSTARTSTOP This in not entirely true. The scope sample rate is 100 MSPS (or factors of ten less) and the signal generator sample rate is 75MSPS (or factors of 10 less) so scope samples do not inherently match up with generator samples. Scope samples would need to be re-sampled by a factor of 3 to 4 to have the signal frequency played back properly. XHIDDENEND

MAT file format only supports arrays of type real (no complex waveforms)

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_16-06-06.png
   :width: 600px

Math signal type allows generation of a signal that is defined as a math equation. .

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_15-25-02.png

On top of all the signals noise can be added. By selecting None, no noise is added to the signal. The rest of the noise types are:

-  Uniform
-  Gaussian
-  Laplacian
-  Impulse

The noise is only calculated once on the host, and simply added to the waveform buffer. This means that for cyclic waveforms the noise will be the same on each period.

Use cases
---------

Create loopback between CH1 and CH2 of the oscilloscope and the signal generator

Run a single channel
~~~~~~~~~~~~~~~~~~~~

XHIDDENSTART Click to expand</summary>

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_17-25-33.png
   :align: center
   :width: 600px

-  Disable channel 2
-  Select sine wave with 5V amplitude and 10kHz
-  Run the signal generator
-  Monitor oscilloscope

.. raw:: html

   </details>


Run both channels
~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_17-30-13.png
   :align: center
   :width: 600px

-  Continue from previous testcase
-  Enable channel 2 and select triangle wave with 5V amplitude and 20kHz
-  Add gaussian noise with 1V amplitude
-  Monitor oscilloscope

.. raw:: html

   </details>


Generate square waveform
~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_17-33-14.png
   :align: center
   :width: 600px

-  Select square wave with 25% dutycycle
-  Decrease noise amplitude to 200mV
-  Monitor oscilloscope

.. raw:: html

   </details>


Generate trapezoidal waveform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_17-34-52.png
   :align: center
   :width: 600px

-  Select trapezoidal waveform with 1ms rise/up/fall/low times
-  Monitor oscilloscope

.. raw:: html

   </details>


Generate waveform from wav file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_17-36-05.png
   :align: center
   :width: 600px

-  Select buffer mode and select a wavefile. One can usually find a suitable wavefile in C:\\Windows\\Media
-  Signal generator automatically selects appropriate sample rate
-  Monitor oscilloscope (if possible connect a speaker to the channel that is outputted)

.. raw:: html

   </details>


Generate stairstep waveform
~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_17-38-32.png
   :align: center
   :width: 600px

-  Select the stairstep csv file provided above https://gist.github.com/adisuciu/7aa30bc9e545db23a17e86d23ae4f53c
-  Remove noise, disable CH1 and increase amplitude to 5V
-  Monitor oscilloscope

.. raw:: html

   </details>


Generate waveform from math function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/mathgenerator.png
   :align: center
   :width: 600px

-  Select Math mode and input a function such as 2*(cos(6000*pi*t)*sin(2000*pi*t))
-  Set sample rate to 75MSPS (this is the sample rate of the generated signal)
-  Set record run length to 1ms.
-  Run the signal
-  Monitor oscilloscope

.. note::

   Sample rate & record length parameters: Since t goes from 0 to infinity, we need to specify how long will t be generated for the specified function - in this case it will go from 0 to 1ms with 75 MSPS granularity(13.3333 ns). These settings will generate (1 \* 10^-3) \* (75 \* 10 ^9) points = 75000 points.

.. raw:: html

   </details>


**Return to** :doc:`Scopy Main Page </wiki-migration/university/tools/m2k/scopy>`
