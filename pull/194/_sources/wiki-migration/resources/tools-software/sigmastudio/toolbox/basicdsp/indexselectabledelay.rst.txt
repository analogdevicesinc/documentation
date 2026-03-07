Index Selelctable Delay
=======================

| :doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| \|\| Delays the input signal by the maximum number of samples selected on the list of spin text box using index select control input.
| |image1|
| ===== Input Pins =====

+---------------------+------------------------------------------+-----------------------------------+
| Name                | Format [int/dec/float] - [control/audio] | Function Description              |
+=====================+==========================================+===================================+
| Pin 0: control Data | int                                      | Control input to select the delay |
+---------------------+------------------------------------------+-----------------------------------+
| Pin 1: Audio Data   | Float                                    | Audio input                       |
+---------------------+------------------------------------------+-----------------------------------+

| 
| ===== Output Pins =====

+-------------------+------------------------------------+----------------------+
| Name              | Format [int/dec] - [control/audio] | Function Description |
+===================+====================================+======================+
| Pin 2: Audio Data | Float                              | Delayed audio signal |
+-------------------+------------------------------------+----------------------+

| 

GUI Controls
------------

+------------------+---------------+----------+--------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range    | Function Description                                                                                         |
+==================+===============+==========+==============================================================================================================+
| Max              | 1             | 1 - 2500 | Variable delay can vary in between 0 to max delay value. There will be an option to display the delay in ms. |
+------------------+---------------+----------+--------------------------------------------------------------------------------------------------------------+
| Cur_1            | 0             | 0 - Max  | Samples delayed by this amount                                                                               |
+------------------+---------------+----------+--------------------------------------------------------------------------------------------------------------+
| Cur_2            | 0             | 0 - Max  | Samples delayed by this amount                                                                               |
+------------------+---------------+----------+--------------------------------------------------------------------------------------------------------------+

| 
| ===== Add-Growth Behaviour ===== Add algorithm is not supported.

Grow Algorithm is supported for Cur Delay control up to 16 and is not supported for input and output channels.

| 
| =====DSP Parameter Information=====

======== ============== =====================
Paramter Calculation    Integer/Decimal/Float
======== ============== =====================
Delay1   Cur Spin text1 Int
Delay2   Cur Spin text1 Int
======== ============== =====================

| 

Implementation
--------------

This module shall implement a multiple delay line with the 'Delay Tap' signal as the actual delay value and delay tap applied to the input signal is selected by the external control index.

| y(n) = { x(n-d(n)), if d(n)<Max
| { x(n-Max), if d(n)>=Max

Here,

::

       y(n) is the output signal 
       y(n) is the input signal
       d(n) is the Delay tap signal(delay value)
       Max is the maximum delay value
       

Supported ICs
-------------

-  ADSP-215xx
-  ADSP-SC58x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/index_sel_delay.png
