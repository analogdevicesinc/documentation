:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Data Controlled Clip (Hard/Soft)
================================

| 
| |dataclipper.png| |asymmclipperdatacontrolled.png|

Description
-----------

| The Data Controlled Clip is a hard-clipper that clips the input data signal according to threshold values set by data control input pins. The data controlled clipper strictly saturates the input signal once it crosses an upper or lower threshold boundary. The output signal will be retained at the threshold value so long as the input signal is above the upper threshold limit, or below the lower threshold limit. For values within the threshold boundaries, the output signal will equal the input signal
| ===== Variants =====

-  Hard Clipper - Data Controlled
-  Soft Clipper - Data Controlled

Targets Supported
-----------------

+--------------------------------+------------+------------------+---------------+------------------+
| Name                           | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+================================+============+==================+===============+==================+
| Hard Clipper - Data Controlled | B/S        | B/S              | S             | B                |
+--------------------------------+------------+------------------+---------------+------------------+
| Soft Clipper - Data Controlled | NA         | NA               | S             | NA               |
+--------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

+-------------------------+---------+-----------------------------------------------------------------------------+
| Name                    | Type    | Description                                                                 |
+=========================+=========+=============================================================================+
| High_Threshold          | Control | Threshold clip level for the top of the waveform (Only for Hard Clipper)    |
+-------------------------+---------+-----------------------------------------------------------------------------+
| Low_Threshold           | Control | Threshold clip level for the bottom of the waveform (Only for Hard Clipper) |
+-------------------------+---------+-----------------------------------------------------------------------------+
| DataControl             | Control | Threshold clip level o the waveform (Only for Soft Clipper)                 |
+-------------------------+---------+-----------------------------------------------------------------------------+
| Input<fc #ff0000>X</fc> | Audio   | Input Channel X                                                             |
+-------------------------+---------+-----------------------------------------------------------------------------+

Output
~~~~~~

======================== ===== ===================================
Name                     Type  Description
======================== ===== ===================================
Output<fc #ff0000>X</fc> Audio Hard clipped output audio Channel X
======================== ===== ===================================

Note:

-  <fc #ff0000>X</fc> - Channel Index

Configurable Parameters
-----------------------

+--------------------+---------------+-------+---------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range | Function Description                                                            |
+====================+===============+=======+=================================================================================+
| NumChannels        | 1             | 20    | Number of input and output channels. Change in channels requires re-compilation |
+--------------------+---------------+-------+---------------------------------------------------------------------------------+

DSP Parameters
--------------

No DSP Parameters

.. |dataclipper.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/dataclipper.png
.. |asymmclipperdatacontrolled.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/asymmclipperdatacontrolled.png
