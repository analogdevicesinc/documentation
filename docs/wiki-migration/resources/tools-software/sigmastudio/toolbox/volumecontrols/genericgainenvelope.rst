Generic Gain Envelope
=====================

:doc:`Click here to return to the Volume Controls section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/volumecontrols>`

+---+---+
| The Generic Gain Envelope generates a fully-programmable envelope and applies it to an input signal. | |genericgainenvelope033.jpg| |
+---+---+

There are two versions of the algorithm available:

-  Generic Gain Envelope Alg
-  Generic Gain Envelope Alg EndlessLoop

| 
| |image1|

Input Pins
----------

+----------------------+------------------------------------+----------------------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description             |
+======================+====================================+==================================+
| Pin 0: Control Input | int - control                      | Switch used to activate envelope |
+----------------------+------------------------------------+----------------------------------+
| Pin 1: Audio Input   | decimal - audio                    | Input audio signal               |
+----------------------+------------------------------------+----------------------------------+

Output Pins
-----------

+----------------------+------------------------------------+------------------------------------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description                           |
+======================+====================================+================================================+
| Pin 0: Control Input | decimal - audio                    | Audio output signal with gain envelope applied |
+----------------------+------------------------------------+------------------------------------------------+

GUI Controls
------------

+-------------------+---------------+------------+--------------------------------------------------------------+
| GUI Control Name  | Default Value | Range      | Function Description                                         |
+===================+===============+============+==============================================================+
| Maximum Time (ms) | 1104          | 240 to 440 | Controls the length of the gain envelope                     |
+-------------------+---------------+------------+--------------------------------------------------------------+
| Gain (dB)         | n/a           | -120 to 24 | Controls the gain of the corresponding point on the envelope |
+-------------------+---------------+------------+--------------------------------------------------------------+
| Time (ms)         | n/a           | 0 to max   | Controls the time of the corresponding point on the envelope |
+-------------------+---------------+------------+--------------------------------------------------------------+

DSP Parameter Information
-------------------------

+----------+---------------------------------------+-----------------------------------------------------------------------------------+
| GUI Name | Compiler Name                         | Function Description                                                              |
+==========+=======================================+===================================================================================+
| n/a      | GenericGainEnvelopegainincrementtable | Controls the way that the output gain changes from point to point on the envelope |
+----------+---------------------------------------+-----------------------------------------------------------------------------------+
| n/a      | GenericGainEnvelopestartgain          | Controls the starting gain of the envelope                                        |
+----------+---------------------------------------+-----------------------------------------------------------------------------------+
| n/a      | GenericGainEnvelopegaintable          | Stores the values that control the output gain of the algorithm                   |
+----------+---------------------------------------+-----------------------------------------------------------------------------------+

Algorithm Description
---------------------

The Generic Gain Envelope algorithm has a fully programmable gain envelope. The envelope is accessible by clicking the cell’s icon.

| 
| |image2|
| The length of the envelope is controlled by the Maximum Time control, which is set in milliseconds.
| Points on the curve can be moved by click-dragging. New points can be added by double-clicking. Points can be removed by right-clicking and selecting “remove point.” In this case, the point closest to the mouse cursor will be removed. The envelope must have at least 3 points. Point values can be fine-tuned using the text input boxes on the right side of the envelope control window.

| 
| |image3|
| When the control input goes to 1, the gain envelope begins. When the control input goes to 0, the gain envelope stops, regardless of whether the envelope has completed or not.
| In the case of the Generic Gain Envelope Alg EndlessLoop algorithm, the envelope will loop continuously until the control input goes to 0.
| The example below shows the algorithm’s input and output signals using the gain envelope shown above.

| 
| |image4|

Example
-------

| The following schematic image shows the Generic Gain Envelope cell being controlled by a 28.0 On/Off Switch and applied to a Sine Tone. The processed audio is output to a DAC. The schematic below uses the Switch, Generic Gain Envelope, Sine Tone, and Output cells.
| |image5|

Algorithm Details
-----------------

+----------------------------+------------------------------------------------+
| Toolbox Path               | Sources – Chime – Modulated Frequency and Gain |
+----------------------------+------------------------------------------------+
| Cores Supported            | ADAU144x                                       |
|                            | ADAU176x                                       |
|                            | ADAU1781                                       |
+----------------------------+------------------------------------------------+
| "Grow Algorithm" Supported | yes - see Algorithm Growth Information         |
+----------------------------+------------------------------------------------+
| "Add Algorithm" Supported  | no                                             |
+----------------------------+------------------------------------------------+
| Subroutine/Loop Based      | no                                             |
+----------------------------+------------------------------------------------+
| Program RAM                | 44\*                                           |
+----------------------------+------------------------------------------------+
| Data RAM                   | 9\*                                            |
+----------------------------+------------------------------------------------+
| Parameter RAM              | 15\*                                           |
+----------------------------+------------------------------------------------+

\*Numbers are based on one instance of the algorithm with no additional "add" or "grow"

Algorithm Growth Information
----------------------------

======================== =========================================
Description              Adds a new input pin and a new output pin
Program RAM Repetition   2 per growth
Data RAM Repetition      1 per growth
Parameter RAM Repetition none
======================== =========================================

.. |genericgainenvelope033.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/genericgainenvelope033.jpg
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/genericgainenvelope034.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/genericgainenvelope035.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/genericgainenvelope036.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/genericgainenvelope037.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/genericgainenvelope038.jpg
