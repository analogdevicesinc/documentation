:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Seven Band Level Detector
=========================

| 
| |sevenband.png|

Description
-----------

The Seven-Band Level Detector block calculates the input signal level, reading directly from the hardware in real-time, and displays the level graphically in seven frequency band meter displays:

-  <100Hz
-  250Hz
-  500Hz
-  1kHz
-  2.5kHz
-  5kHz
-  >10kHz

The level detector performs the analysis only and does not modify the input signal. The signal at the output pin is identical to the input.

| Use the On / Off button to enable or disable the display. The level detector will not function until the schematic design has been compiled and downloaded to the hardware and a USB communication channel is properly configured.
| ===== Targets Supported =====

+---------------------------+------------+------------------+---------------+------------------+
| Name                      | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===========================+============+==================+===============+==================+
| Seven Band Level Detector | B/S        | B/S              | NA            | NA               |
+---------------------------+------------+------------------+---------------+------------------+

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

============= ============= ====== ====================================
GUI Parameter Default Value Range  Function Description
============= ============= ====== ====================================
On/Off Switch OFF           ON/OFF Enable or Disable the Level Detector
============= ============= ====== ====================================

| 
| ===== DSP Parameters ===== No DSP Parameters

.. |sevenband.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/sevenband.png
