Data Controlled Clip
====================

+-----------------------------------------------------------------------------------------------------------------------------------+----------+
| The Data Controlled Clip is a hard-clipper that clips the input data signal according to threshold values set by data input pins. | |image2| |
+-----------------------------------------------------------------------------------------------------------------------------------+----------+

Input Pins
----------

+-----------------------+------------------------------------+-----------------------------------------------------+
| Name                  | Format [int/dec] - [control/audio] | Function Description                                |
+=======================+====================================+=====================================================+
| Pin 0: High Threshold | decimal - control                  | Threshold clip level for the top of the waveform    |
+-----------------------+------------------------------------+-----------------------------------------------------+
| Pin 1: Low Threshold  | decimal - control                  | Threshold clip level for the bottom of the waveform |
+-----------------------+------------------------------------+-----------------------------------------------------+
| Pin 2: Input          | decimal - audio                    | Input audio to be hard clipped                      |
+-----------------------+------------------------------------+-----------------------------------------------------+

Output Pins
-----------

+---------------+------------------------------------+---------------------------+
| Name          | Format [int/dec] - [control/audio] | Function Description      |
+===============+====================================+===========================+
| Pin 0: Output | decimal - audio                    | Hard clipped output audio |
+---------------+------------------------------------+---------------------------+

Algorithm Description
---------------------

The data controlled clipper strictly saturates the input signal once it crosses an upper or lower threshold boundary. The output signal will be retained at the threshold value so long as the input signal is above the upper threshold limit, or below the lower threshold limit. For values within the threshold boundaries, the output signal will equal the input signal.

| 
| The graph below shows an input sine tone and the resulting clipped output with threshold values at: High: 0.8 Low: -0.2

| 
| |image3|

Example
-------

The following image shows the Data Controlled Clip, being compared to a Hard Clipper and also the direct signal coming from the Inputs. A stereo switch mux allows for selection of the processing type, and then the signals are routed to the Outputs. Two DC Input blocks are used to define the threshold values for the Data Controlled Clip. They are currently set with the same values in the Hard Clip cell. The output from both clip blocks will be the same, but have different ways to control the thresholds (coefficients vs. data inputs).

| 
| |image4|

Algorithm Details
-----------------

+----------------------------+---------------------------------------------------------------------+
| Toolbox Path               | Non Linear Processors - Clippers - Hard Clip - Data Controlled Clip |
+----------------------------+---------------------------------------------------------------------+
| Cores Supported            | AD1940                                                              |
|                            | ADAU170x                                                            |
|                            | ADAU144x                                                            |
|                            | ADAU176x                                                            |
|                            | ADAU178x                                                            |
+----------------------------+---------------------------------------------------------------------+
| "Grow Algorithm" Supported | yes - see Algorithm Growth Information                              |
+----------------------------+---------------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                                  |
+----------------------------+---------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                                  |
+----------------------------+---------------------------------------------------------------------+
| Program RAM                | 10\*                                                                |
+----------------------------+---------------------------------------------------------------------+
| Data RAM                   | 1\*                                                                 |
+----------------------------+---------------------------------------------------------------------+
| Parameter RAM              | 0                                                                   |
+----------------------------+---------------------------------------------------------------------+

\*Numbers are based on one instance of the algorithm with no additional "add" or "grow"

Algorithm Growth Information
----------------------------

+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Description              | When the Data Controlled Clip is grown, an extra pair of Input/Output pins is added to the control. The High and Low Threshold pins do not grow as the same values will apply to all audio pairs grown on the control. | |image6| |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Program RAM Repetition   | 10 per growth                                                                                                                                                                                                          |          |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Data RAM Repetition      | 1 per growth                                                                                                                                                                                                           |          |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Parameter RAM Repetition | none                                                                                                                                                                                                                   |          |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/datacontrolledclip013.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/datacontrolledclip013.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/datacontrolledclip014.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/datacontrolledclip015.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/datacontrolledclip016.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/datacontrolledclip016.jpg
