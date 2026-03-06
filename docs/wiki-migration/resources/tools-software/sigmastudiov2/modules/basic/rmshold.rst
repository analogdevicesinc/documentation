:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

RMS Hold
========

| 
| |rmstchold.png|

Description
-----------

| The RMS Hold block computes the RMS of the input signals with time constant specified in the text field and holds the maximum value. Hold/Reset the maximum rms value is controlled by the external input pin.
| ===== Targets Supported =====

======== ========== ================ ============= ================
Name     ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
======== ========== ================ ============= ================
RMS Hold B/S        B/S              NA            NA
======== ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

======================== ======= ================================
Name                     Type    Description
======================== ======= ================================
Reset                    Control Reset/Hold the maximum rms value
Input <fc #ff0000>X</fc> Audio   Input channel X
======================== ======= ================================

| 
| ==== Output ====

========================= ===== ================
Name                      Type  Description
========================= ===== ================
Output <fc #ff0000>X</fc> Audio Output channel X
========================= ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-------------+-----------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range       | Function Description                                                              |
+====================+===============+=============+===================================================================================+
| TimeConstant       | 121           | 1-8686      | Determines how rapidly the RMS value compute with change in input level           |
+--------------------+---------------+-------------+-----------------------------------------------------------------------------------+
| IsDBps             | False         | Truie/False | Control value is in dB/s or ms                                                    |
+--------------------+---------------+-------------+-----------------------------------------------------------------------------------+
| NumChannels        | 1             | 20          | Number of input and Output channels. Change in this value requires re-compilation |
+--------------------+---------------+-------------+-----------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-----------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                         | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=====================================================+========================+===============+
| TimeConstant   | TC for RMS value compute with change in input level | Float                  | NA            |
+----------------+-----------------------------------------------------+------------------------+---------------+
| LogCoeff       | Constant values                                     | Float                  | NA            |
+----------------+-----------------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== TimeConstant = ABS(1-10^(TimeConstant(linear)/(10*FS)))
| Where FS is the Sampling rate

.. |rmstchold.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/rmstchold.png
