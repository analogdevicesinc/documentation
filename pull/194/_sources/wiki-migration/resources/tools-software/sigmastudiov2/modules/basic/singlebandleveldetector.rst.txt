:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Single Band Level Detector
==========================

| 
| |singlebandlvldetector.png| |leveldetectordesigner.png|
| |leveldetectordesignpopup.png|

Variants
--------

::

   -Single Band Level Detector
   -Level Detector Designer (RTA to OUTPUT)
   -Level Detector Designer (Pass Through)
   -Single Band Level Detector (Direct Read)
   -Level Detector Low DSP MIPS
   -Single Band Level Detector (Running Average)

Description
-----------

The Single Band Level Detector blocks calculate the input signal level, reading directly from the hardware in real time, and display the level graphically in meter displays. The Single-Level Detector calculates and displays the rms level of the signal, shown in dB.

The level detector performs analysis only and does not modify the input signal. The signal at the output pin is identical to the input.

| 
| Single Band Level Detector (Direct Read) module is similar to the Single Level Detector w Numeric Display. However, the calculations are split between the DSP and SigmaStudio. The DSP calculates the level of the signal in dB, as dB = 20\*Log(SampleValue), and then SigmaStudio reads back this value and averages according to y = tc\*y(n-1) + (1-tc)x

| 
| The Level Detector Low DSP MIPS block acts as an audio sample readback register. The DSP does not perform any level detector calculations. Instead, SigmaStudio reads back the sample, converts it to dB, and performs averaging. As with the Direct Read algorithm, transient peaks may be missed by this level detector.

| 
| Level Detector Designer (Pass Through) module algorithm receives a 8.24 number (8 bytes to represent the integer portion of the value, 24 bytes for the decimal portion) during readback and converts it to a decimal value represented in decibels. This is what is seen on the display bar. Because this is a passthrough system, the output is the same signal being sent to the block.

| 
| Level Detector Designer (RTA to OUTPUT) module algorithm outputs the rms level value through the output pin. This pin is red because no actual audio is being sent out, just the level values for each frequency band. Observe that when you grow this algorithm, each pin corresponds to a frequency band.

Usage
-----

Use the On / Off button to enable or disable the display. The level detector will not function until the schematic design has been compiled and downloaded to the hardware and a USB communication channel is properly configured.

The refresh rate of the display is approximately 10 Hz, while the green cross-bar tracks the maximum rms value with a slight delay. Note that the display's performance is limited by your PC system and USB communication resources. Using multiple level detectors may degrade the responsiveness.

| 
| Level Detector Designer (RTA to OUTPUT) & Level Detector Designer (Pass Through) : Click the Wnd button to bring up the window for entering your design parameters. The default block contains only one color bar, but when you grow your algorithm you can account for multiple frequency bands. To make the most of your level detector, it's important to understand the parameters in the designer window. The parameters are Filter type, Center Frequency, and Q or Bandwidth depending on filter type. There also is an overall Time Constant and Decay value that can be set in dB/s to control the refresh time.

Targets Supported
-----------------

+----------------------------------------------+------------+------------------+---------------+------------------+
| Name                                         | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==============================================+============+==================+===============+==================+
| Single Band Level Detector                   | B/S        | B/S              | NA            | B                |
+----------------------------------------------+------------+------------------+---------------+------------------+
| Level Detector Designer (RTA to OUTPUT)      | NA         | NA               | S             | NA               |
+----------------------------------------------+------------+------------------+---------------+------------------+
| Level Detector Designer (Pass Through)       | NA         | NA               | S             | NA               |
+----------------------------------------------+------------+------------------+---------------+------------------+
| Single Band Level Detector (Direct Read)     | NA         | NA               | S             | NA               |
+----------------------------------------------+------------+------------------+---------------+------------------+
| Level Detector Low DSP MIPS                  | NA         | NA               | S             | NA               |
+----------------------------------------------+------------+------------------+---------------+------------------+
| Single Band Level Detector (Running Average) | NA         | NA               | S             | NA               |
+----------------------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Audio Input Channel 0
====== ===== ===============

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

| 
| ===== Configurable Parameters =====

+------------------------------------------+---------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter                            | Default Value | Range                          | Function Description                                                                                                                                                                                                            |
+==========================================+===============+================================+=================================================================================================================================================================================================================================+
| On/Off Switch                            | OFF           | 20 to 20000                    | Enable or disable the Level Detector                                                                                                                                                                                            |
+------------------------------------------+---------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Stage<fc #ff0000>X</fc>_Corner Frequency | 100           | 20 to 20000                    | Specify the center / cutoff frequency of the filter (Only applicable for Pass-through & RTA to Output )                                                                                                                         |
+------------------------------------------+---------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Stage<fc #ff0000>X</fc>_QFactor          | 0.7           | 0.01 to 15                     | Available with LP and HP filters, Q determines the steepness of the filter skirts and its -3dB points (Only applicable for Pass-through & RTA to Output )                                                                       |
+------------------------------------------+---------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Stage<fc #ff0000>X</fc>_BandWidth        | 2             | 0.01 to 15                     | Available with the BP filter, Bandwidth determines the range of frequencies your design will affect (Only applicable for Pass-through & RTA to Output )                                                                         |
+------------------------------------------+---------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Stage<fc #ff0000>X</fc>_Filter Type      | Band Pass     | Low Pass, Band Pass, High Pass | LP, HP, and BP filters can be set for the individual bands (Only applicable for Pass-through & RTA to Output )                                                                                                                  |
+------------------------------------------+---------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Time Constant                            | 10            | 10 to 1000                     | This value, in dB/s, designates the averaging time of the detector: how rapidly it assesses and responds to signal level changes (Only applicable for Pass-through & RTA to Output )                                            |
+------------------------------------------+---------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay                                    | 0             | 0 to 1000                      | Another type of time constant, Decay designates the rate at which signal returns to a lower detected level. Decay is responsible for releasing the signal at the given rate (Only applicable for Pass-through & RTA to Output ) |
+------------------------------------------+---------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumStages                                | 1             | 1 to 14                        | Number of stages (Only applicable for Pass-through & RTA to Output ). Change in this value requires re-compilation                                                                                                              |
+------------------------------------------+---------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note:

-  <fc #ff0000>X</fc> - Stage Index

| 
| ===== DSP Parameters =====

+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                                                                                                                                     | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=================================================================================================================================================================================+========================+===============+
| TimeConstant   | Used to calculate the RMS Value of the input signal. The time constant determines how rapidly the compressor will respond to input signal level changes, e.g. the “Attack” time | Float                  | FixPoint8d24  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Log            | Constant Log Coefficients                                                                                                                                                       | Float                  | NA            |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Decay          | Controls the rate at which the compressor gain decreases in response to decrease in the input signal level, e.g. the “Release” time                                             | Float                  | FixPoint8d24  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Hold           | Controls the time (in ms) the compressor maintains its current output gain setting before it starts decreasing as the input level decrease                                      | Float                  | NA            |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| ReadBack       | Reads the RMS level of the input signal                                                                                                                                         | Float                  | NA            |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| LinX           | Reads the level of the input signal                                                                                                                                             | NA                     | FixPoint8d24  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| LinX_lo        | Reads the level of the input signal                                                                                                                                             | NA                     | FixPoint8d24  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| level          | Reads the level of the input signal                                                                                                                                             | NA                     | FixPoint8d24  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== TimeConstant = Abs(1.0 - 10^(500/(10 \* Sampling Rate)))
| Decay = 96/Sampling Rate
| Hold = Sampling Rate \* 0.01

.. |singlebandlvldetector.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/singlebandlvldetector.png
.. |leveldetectordesigner.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/leveldetectordesigner.png
.. |leveldetectordesignpopup.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/leveldetectordesignpopup.png
