Level Detector Designer
=======================

:doc:`Click here to return to the Level Detectors/Lookup Tables page </wiki-migration/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/leveldetectordesigner_008.jpg
   :align: right

The Level Detector blocks calculate the input signal level, reading directly from the hardware in real time, and display the level graphically in meter displays. The Level Detector Designer block lets you define your own frequency bands and time constants for the display.

The level detector performs analysis only and does not modify the input signal. The signal at the output pin is identical to the input.

Use the On / Off button to enable or disable the display. The level detector will not function until the schematic design has been compiled and downloaded to the hardware and a USB communication channel is properly configured.

Note: The refresh rate of the display is approximately 10 Hz, while the green cross-bars track the maximum rms value with a slight delay. The display's performance is limited by your PC system and USB communication resources. Using multiple level detectors may degrade the responsiveness.

To use this block:

-  Unordered List ItemDrag it into the workspace.
-  Right-click it and select Add Algorithm > IC #.
-  From the list, select the algorithm that meets your needs:

   -  Passthrough
   -  RTA to output
   -  Passthrough / minimal reading, single-precision
   -  Passthrough / minimal reading, double-precision

-  Click the red Wnd button to bring up the window (below) for entering your design parameters.

After selecting your default algorithm, there's an option to Grow it. The default block contains only one color bar, but when you grow your algorithm you can account for multiple frequency bands. The figure above right shows the Passthrough algorithm grown by 1.

To make the most of your level detector, it's important to understand the parameters in the designer window. Shown below is that window for a passthrough algorithm grown by 8. There are a 9 bands total, each with the option of choosing Filter type, Center Frequency, and Q or Bandwidth depending on filter type. (There also is an overall Time Constant and Decay value that can be set in dB/s to control the refresh time of the color display.)

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/leveldetectordesigner_009.jpg
   :align: center

Parameters:
-----------

-  Filter Type: Lowpass, highpass, and bandpass filters can be set for the individual bands of the color display.
-  Center Frequency: Specify the center / cutoff frequency of the filter.
-  Q: Available with LP and HP filters, Q determines the steepness of the filter skirts and its -3dB points.
-  Bandwidth: Available with the BP filter, Bandwidth determines the range of frequencies your design will affect.
-  Time Constant: This value, in dB/s, designates the averaging time of the detector: how rapidly it assesses and responds to signal level changes.
-  Decay: Another type of time constant, Decay designates the rate at which signal returns to a lower detected level. Decay is responsible for releasing the signal at the given rate.

Algorithms:
-----------

-  Passthrough: This algorithm receives a 5.19 number (5 bytes to represent the integer portion of the value, 19 bytes for the decimal portion) during readback and converts it to a decimal value represented in decibels. This is what is seen on the display bar. Because this is a passthrough system, the output is the same signal being sent to the block.
-  RTA to output: The RTA-to-output algorithm outputs the rms level value through the output pin. This pin is red because no actual audio is being sent out, just the level values for each frequency band. Observe that when you grow this algorithm, each pin corresponds to a frequency band.
-  Passthrough / minimal reading, single- and double-precision: This functions in a manner similar to Passthrough but saves on communication bandwidth at the expense of losing precision. It uses only 1 byte for the readback value, then converts the value to a decimal which is represented in decibels.

Normally you should use double-precision: 56 bits for each calculation and 10 instructions per filter. Single-precision uses 28 bits for calculations and 6 instructions per filter, saving 3 data ram spaces over the double-precision algorithm. Note that single-precision should not be employed either for frequencies below 1/10 the sampling rate or for high-Q filters.

Supported ICs
-------------

ADAU1401, ADAU144x, ADAU145x, ADAU146x and ADAU176x
