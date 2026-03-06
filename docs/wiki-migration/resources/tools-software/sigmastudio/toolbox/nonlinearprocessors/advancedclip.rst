Advanced Clip
=============

| :doc:`Click here to return to the Non Linear Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/nonlinearprocessors>`

+---+---+
| The Advanced Clip cell takes an input signal and rounds its edges to avoid clipping at large signal levels. As the input signal reaches the clip threshold, the algorithm rounds the edges for a smoother clipped output. | |image2| |
+---+---+

Input Pins
----------

+--------------+------------------------------------+----------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description       |
+==============+====================================+============================+
| Pin 0: Input | decimal - audio                    | Input signal to be clipped |
+--------------+------------------------------------+----------------------------+

Output Pins
-----------

============= ================================== =======================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== =======================
Pin 0: Output decimal - audio                    The soft-clipped output
============= ================================== =======================

GUI Controls
------------

+------------------+---------------+-----------+--------------------------------------------------------------------+
| GUI Control Name | Default Value | Range     | Function Description                                               |
+==================+===============+===========+====================================================================+
| n/a              | 1             | 0.1 - 0.9 | This control changes the way in which the input signal is clipped. |
+------------------+---------------+-----------+--------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------+----------------------+-------------------------------------------+
| GUI Control Name | Compiler Name        | Function Description                      |
+==================+======================+===========================================+
| n/a              | SoftClipNew1tau      | Used to calculate thetha                  |
+------------------+----------------------+-------------------------------------------+
| n/a              | SoftClipNew1scale    | Used to calculate thetha, scale = 1/1-tau |
+------------------+----------------------+-------------------------------------------+
| n/a              | SoftClipNew1onemtau  | See the Algorithm description for use     |
+------------------+----------------------+-------------------------------------------+
| n/a              | SoftClipNew1p1val    | Constants                                 |
+------------------+----------------------+-------------------------------------------+
| n/a              | SoftClipNew1thRange1 | Constants                                 |
+------------------+----------------------+-------------------------------------------+

| Note: The SoftClipNew1p1val and SoftClipNew1thRange1 parameters do not need to change when the GUI control is updated.
| ===== Algorithm Description ===== The input is compared with the threshold value:

If abs(input) < = threshold, output = input

::

     Else,
         If input > 0, output = threshold*(1+tanh(theta))
             Else,
             output = - threshold*(1+tanh(theta))
     where:  theta = (abs(input)-threshold)/threshold

| 
| ===== Algorithm Details =====

+----------------------------+---------------------------------------------------------------+
| Toolbox Path               | Non Linear Processors - Clippers - Soft Clip - Standard Cubic |
+----------------------------+---------------------------------------------------------------+
| Cores Supported            | ADAU144x                                                      |
|                            | ADAU176x                                                      |
|                            | ADAU178x                                                      |
+----------------------------+---------------------------------------------------------------+
| "Grow Algorithm" Supported | yes - see Algorithm Growth Information                        |
+----------------------------+---------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                            |
+----------------------------+---------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                            |
+----------------------------+---------------------------------------------------------------+
| Program RAM                | 63\*                                                          |
+----------------------------+---------------------------------------------------------------+
| Data RAM                   | 9\*                                                           |
+----------------------------+---------------------------------------------------------------+
| Parameter RAM              | 31\*                                                          |
+----------------------------+---------------------------------------------------------------+

\*Numbers are based on one instance of the algorithm with no additional "add" or "grow"

Algorithm Growth Information
----------------------------

+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Description              | When the Advanced Clip algorithm is grown, an extra pair of input/output pints is added to the control. The same clipping parameter affects the clipping on grown Input pins. | |image4| |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Program RAM Repetition   | 63 per growth                                                                                                                                                                 |          |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Data RAM Repetition      | 1 per growth                                                                                                                                                                  |          |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Parameter RAM Repetition | none                                                                                                                                                                          |          |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/advancedclip020.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/advancedclip020.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/advancedclip019.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/advancedclip019.jpg
