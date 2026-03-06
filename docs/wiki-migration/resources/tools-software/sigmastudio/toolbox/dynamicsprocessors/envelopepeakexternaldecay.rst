Envelope Peak External Decay
============================

| :doc:`Click here to return to the Dynamic Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| ---------------------------------------------------------------------------------------------------------------

+---+---+
| The Envelope Peak External Decay algorithm measures the absolute peak level of the incoming signal. A hold time is applied that will hold the value of an incoming peak level before starting the decay ramp. The decay ramp is linear and its speed can be controlled using the Decay Speed control input pin. | |envelopepeakextpic1.png| |
+---+---+

Input Pins
----------

+--------------------+------------------------------------+-----------------------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description              |
+====================+====================================+===================================+
| Pin 0: Audio Input | decimal - audio                    | Audio Input - Channel 0           |
+--------------------+------------------------------------+-----------------------------------+
| Pin 1: Decay Speed | integer - control                  | Decay speed of peak detect signal |
+--------------------+------------------------------------+-----------------------------------+

Output Pins
-----------

+-------------------+------------------------------------+-----------------------------------------------------------------------------------------------------+
| Name              | Format [int/dec] - [control/audio] | Function Description                                                                                |
+===================+====================================+=====================================================================================================+
| Pin 0: Peak Level | decimal - control                  | This signal represents the peak level of the incoming signal, with hold and variable decay applied. |
+-------------------+------------------------------------+-----------------------------------------------------------------------------------------------------+

GUI Controls
------------

+------------------+---------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range     | Function Description                                                                                                                                                                             |
+==================+===============+===========+==================================================================================================================================================================================================+
| Hold (ms)        | 0             | 0 to 2000 | Sets the length of time that an incoming peak value is held. The decay will begin once this timer has expired. The timer will reset if the incoming audio exceeds the currently held peak value. |
+------------------+---------------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+-----------+------------------------------------+-------------------------------------------+
| GUI Name  | Compiler Name                      | Function Description                      |
+===========+====================================+===========================================+
| Hold (ms) | MonoEnvelopePeakExtDecayAlg1hold_1 | Sets the hold time for the peak envelope. |
+-----------+------------------------------------+-------------------------------------------+

Algorithm Description
---------------------

This cell calculates the peak envelope of the input signal and then applies a hold time and decay (release). The hold time is fixed and can be input manually in the text input box. The decay time is variable and depends on the decay input pin.

The variable decay input is approximately 1.82 times that of a normal peak envelope cell's decay speed. For example, in order to get a decay rate of 100 dB/s, 182 (in integer format) should be input to the variable decay pin.

| With a fixed decay rate, the cell behaves just like a normal peak envelope cell. In the example below, the blue signal is the input, and the red signal is the peak envelope with a constant decay rate.
| |envelopepeakextpic2.png|
| If the decay rate is variable, then the envelope will decay at a variable rate. The example below shows the input (the blue burst signal at the right), the peak envelope, and the varying decay rate (fully-rectified sine wave).
| |envelopepeakextpic3.png|

Example
-------

| The example below shows a digital input going into the peak envelope cell with a fixed decay of 1000, which equates to around 550 dB/s. The resulting envelope is output on a digital audio serial port.
| |envelopepeakextpic4.png|

Algorithm Details
-----------------

+----------------------------+----------------------------------------------------------------------+
| Toolbox Path               | Dynamics Processors - Envelope - Peak - Envelope Peak External Decay |
+----------------------------+----------------------------------------------------------------------+
| Cores Supported            | AD1940                                                               |
|                            | ADAU144x                                                             |
|                            | ADAU170x                                                             |
|                            | ADAU1761                                                             |
|                            | ADAU1781                                                             |
+----------------------------+----------------------------------------------------------------------+
| "Grow Algorithm" Supported | no                                                                   |
+----------------------------+----------------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                                   |
+----------------------------+----------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                                   |
+----------------------------+----------------------------------------------------------------------+
| Program RAM                | 18                                                                   |
+----------------------------+----------------------------------------------------------------------+
| Data RAM                   | 6                                                                    |
+----------------------------+----------------------------------------------------------------------+
| Parameter RAM              | 1                                                                    |
+----------------------------+----------------------------------------------------------------------+

.. |envelopepeakextpic1.png| image:: https://wiki.analog.com/_media/envelopepeakextpic1.png
.. |envelopepeakextpic2.png| image:: https://wiki.analog.com/_media/envelopepeakextpic2.png
.. |envelopepeakextpic3.png| image:: https://wiki.analog.com/_media/envelopepeakextpic3.png
.. |envelopepeakextpic4.png| image:: https://wiki.analog.com/_media/envelopepeakextpic4.png
