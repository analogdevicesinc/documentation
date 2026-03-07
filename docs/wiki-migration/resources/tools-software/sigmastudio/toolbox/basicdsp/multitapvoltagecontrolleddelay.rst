Multi-Tap Voltage Controlled Delay
==================================

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| ---------------------------------------------------------------------------------------------------------

.. _multi-tap-voltage-controlled-delay-1:

Multi-Tap Voltage Controlled Delay
----------------------------------

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+
| The Multi-Tap Voltage Controlled Delay cell provides a variable delay to a single audio input, producing multiple outputs. Each output signal is called a “tap.” The amount of delay for each tap can be modified in real-time by updating the value on the corresponding control input pin. | |multitapvoltagepic1.png| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------+

Input Pins
~~~~~~~~~~

+---------------------------------+------------------------------------+------------------------------------------+
| Name                            | Format [int/dec] - [control/audio] | Function Description                     |
+=================================+====================================+==========================================+
| Pin 0: Audio Input              | decimal - audio                    | Audio Input signal                       |
+---------------------------------+------------------------------------+------------------------------------------+
| Pin 1: Variable Delay (Tap 0)   | decimal - control                  | Delay amount for output 0 (in samples)   |
+---------------------------------+------------------------------------+------------------------------------------+
| …                               | …                                  | …                                        |
+---------------------------------+------------------------------------+------------------------------------------+
| Pin n: Variable Delay (Tap n-1) | decimal - control                  | Delay amount for output n-1 (in samples) |
+---------------------------------+------------------------------------+------------------------------------------+

Output Pins
~~~~~~~~~~~

+-----------------------+------------------------------------+-------------------------+
| Name                  | Format [int/dec] - [control/audio] | Function Description    |
+=======================+====================================+=========================+
| Pin 0: Audio Output 0 | decimal - audio                    | Delayed output signal 0 |
+-----------------------+------------------------------------+-------------------------+
| ...                   | ...                                | ...                     |
+-----------------------+------------------------------------+-------------------------+
| Pin n: Audio Output n | decimal - audio                    | Delayed output signal n |
+-----------------------+------------------------------------+-------------------------+

GUI Controls
~~~~~~~~~~~~

+------------------+---------------+-----------------------------+----------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range                       | Function Description                                                       |
+==================+===============+=============================+============================================================================+
| Max              | 1             | Depends on size of data RAM | Controls the maximum amount of delay that can be used for each output tap. |
+------------------+---------------+-----------------------------+----------------------------------------------------------------------------+

DSP Parameter Information
~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------------------------------------------------+---------------------------------------------------+
| GUI Name | Compiler Name                                       | Function Description                              |
+==========+=====================================================+===================================================+
| Max      | VoltageControlledDelay1940NoZipAlgwLimit1buffersize | The maximum delay (in samples) for each delay tap |
+----------+-----------------------------------------------------+---------------------------------------------------+

Algorithm Description
~~~~~~~~~~~~~~~~~~~~~

The multi-tap voltage controlled delay allows a single signal to be output as multiple, independently-delayed copies. By right-clicking and selecting the “grow” option, the user can increase the number of copies, or “taps”, to be output. A maximum of 16 taps is allowed per cell.

A delay “pool” size is chosen prior to compilation; this value will determine the amount of modulo data RAM that the compiler will attempt to reserve for each tap. The delay pool size is controlled by the drop-down menu in the middle of the cell. The equivalent delay in milliseconds is displayed below this menu. The calculation for the equivalent delay is based on the cell’s sample rate setting. Note that this delay pool size is reserved for each tap. It is not a shared pool that can be used by individual taps.

If the control input for any tap exceeds the maximum allowable delay for that tap, then the maximum value will be used.

Care must be taken so that the control inputs never go below zero (integer). If the control input a negative number, the output of the algorithm will jump to -1 (decimal).

| As a simple example, a single tap can be used to delay an input signal. The example below shows three signals: input, output, and control signals. The output is a delayed copy of the input, and the control signal determines how much delay is used. In this example, 100 samples of delay is used.
| |multitapvoltagepic2.png|
| If multiple taps are used, then the delay for each output will be determined separately, based on its corresponding control input pin. In the example below, Output 0 is delayed by 40 samples and Output 1 is delayed by 80 samples.
| |multitapvoltagepic3.png|
| The delay can be modified in real-time, but this will cause frequency distortion on the output. If delay needs to be modified in real-time, then muting the audio when changing the delay length can help to avoid distortion. Also, changing the delay length gradually can help to mitigate the severity of the frequency distortion. An example of extreme frequency warping is shown below.
| |multitapvoltagepic4.png|

Example
~~~~~~~

| The following schematic image shows the Multi-Tap Voltage Controlled Delay being used with a sine tone generator as an input and two delay taps. The maximum delay is 100 samples. Output 0 is delayed by 20 samples and Output 1 is delayed by 40 samples. The schematic below additionally uses the Sine Tone, DC Source, and Output cells.
| |image1|

Algorithm Details
~~~~~~~~~~~~~~~~~

+----------------------------+----------------------------------------------------------------+
| Toolbox Path               | Basic DSP – DSP Functions – Multi-Tap Voltage Controlled Delay |
+----------------------------+----------------------------------------------------------------+
| Cores Supported            | AD1940                                                         |
|                            | ADAU170x                                                       |
|                            | ADAU144x                                                       |
|                            | ADAU176x                                                       |
|                            | ADAU178x                                                       |
+----------------------------+----------------------------------------------------------------+
| "Grow Algorithm" Supported | yes - see Algorithm Growth Information                         |
+----------------------------+----------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                             |
+----------------------------+----------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                             |
+----------------------------+----------------------------------------------------------------+
| Program RAM                | 16\*                                                           |
+----------------------------+----------------------------------------------------------------+
| Data RAM                   | 4*\*                                                           |
+----------------------------+----------------------------------------------------------------+
| Parameter RAM              | 1                                                              |
+----------------------------+----------------------------------------------------------------+

Multi-Tap Voltage Controlled Delay (ADAU145x/ADAU146x)
------------------------------------------------------

The Multi-Tap Voltage Controlled Delay for ADAU145x/ADAU146x provides a variable delay to a single audio input, producing multiple outputs. Each output signal is called a “tap.” The amount of delay for each tap can be modified in real-time by updating the value on the corresponding control input pin. It allows the user to choose in which memory the delay buffer to be stored.

| 
| |image2|
| ==== Input Pins ====

+---------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description                                                                                                           |
+=====================+====================================+================================================================================================================================+
| Pin 0: Input Signal | dec- audio                         | Input Audio.                                                                                                                   |
+---------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Pin 1: Dealy        | int- control                       | Delay in samples. Please note that, the dealy value in this pins hould always be in samples (Even the display of Max is in ms) |
+---------------------+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

.. _output-pins-1:

Output Pins
~~~~~~~~~~~

+-----------------------+------------------------------------+----------------------+
| Name                  | Format [int/dec] - [control/audio] | Function Description |
+=======================+====================================+======================+
| Pin 0: Delayed Signal | dec- audio                         | Delyaed audio.       |
+-----------------------+------------------------------------+----------------------+

Grow Algorithm
~~~~~~~~~~~~~~

The module can be grown for multiple taps in the delay line.

Configurations
~~~~~~~~~~~~~~

+------------------+---------------+-------------------------------+----------------------------------------+
| GUI Control Name | Default Value | Range                         | Function Description                   |
+==================+===============+===============================+========================================+
| Max              | 1             | 1- Available Memory (samples) | Maximum Delay                          |
+------------------+---------------+-------------------------------+----------------------------------------+
| Memory           | DM1           | DM0/DM1/PM                    | Memory to store the delay line buffer. |
+------------------+---------------+-------------------------------+----------------------------------------+

.. _dsp-parameter-information-1:

DSP Parameter Information
~~~~~~~~~~~~~~~~~~~~~~~~~

No DSP parameters can be tuned, Link compile download is required when the DSP parameter is changed.

Supported ICs
~~~~~~~~~~~~~

-  ADAU145x
-  ADAU146x

.. |multitapvoltagepic1.png| image:: https://wiki.analog.com/_media/multitapvoltagepic1.png
.. |multitapvoltagepic2.png| image:: https://wiki.analog.com/_media/multitapvoltagepic2.png
.. |multitapvoltagepic3.png| image:: https://wiki.analog.com/_media/multitapvoltagepic3.png
.. |multitapvoltagepic4.png| image:: https://wiki.analog.com/_media/multitapvoltagepic4.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/fractionalvoltagecontrolled.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/vcd_300.jpg
