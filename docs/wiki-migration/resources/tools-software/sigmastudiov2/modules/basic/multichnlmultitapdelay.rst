:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Multi-Channel Multi-Tap Delay
=============================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/mcmtdelay.png
   :alt: mcmtdelay.png

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/mcmtdelaywindow.png
   :alt: mcmtdelaywindow.png

Description
-----------

The Multi Channel Multi Tap Delay cell provides a variable delay for each output
from one of the selected input channel. Each input signal is called as channel
and output is called as Tap. The amount of delay for each tap can be modified in
real time by updating the current delay.

Targets Supported
-----------------

+-----------------------------+------------+------------------+---------------+------------------+
| Name                        | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=============================+============+==================+===============+==================+
| MultiChannel MultiTap Delay | B          | B                | S             | B                |
+-----------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

======= ===== ===============
Name    Type  Description
======= ===== ===============
Input X Audio Input Channel X
======= ===== ===============

| ==== Output ====

======== ===== ================
Name     Type  Description
======== ===== ================
Output X Audio Output channel X
======== ===== ================

Note:

-  X - Channel Index

Configurable Parameters
-----------------------

+-----------------------------+---------------+--------------------------+-------------------------------------------------------------------------+
| GUI Parameter Name          | Default Value | Range                    | Function Description                                                    |
+=============================+===============+==========================+=========================================================================+
| InputSelection_OutputX_SetY | Input0        | Input Channels list      | Output delay maximum value depends on the selected input                |
+-----------------------------+---------------+--------------------------+-------------------------------------------------------------------------+
| Delay_OutputX_SetY          | 0             | 0 to selectedinput value | current delay value                                                     |
+-----------------------------+---------------+--------------------------+-------------------------------------------------------------------------+
| MaxDelay_InputX             | 10            | 10 to 2500               | max delay values                                                        |
+-----------------------------+---------------+--------------------------+-------------------------------------------------------------------------+
| NumInputs                   | 1             | 32                       | Number of input channels. Change in this value requires re-compilation  |
+-----------------------------+---------------+--------------------------+-------------------------------------------------------------------------+
| NumOutputs                  | 1             | 32                       | Number of Output channels. Change in this value requires re-compilation |
+-----------------------------+---------------+--------------------------+-------------------------------------------------------------------------+

Note:

-  X - Channel Index
-  Y - Tab Index

DSP Parameters
--------------

+------------------------+------------------------------+------------------------+---------------+
| Parameter Name         | Description                  | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+========================+==============================+========================+===============+
| InputSelection_OutputX | Selected input               | Integer32              | Integer32     |
+------------------------+------------------------------+------------------------+---------------+
| Delay_OutputX          | Current delay                | Integer32              | Integer32     |
+------------------------+------------------------------+------------------------+---------------+
| MaxDelayArray          | Maximum allowed Delay values | Integer32              | Integer32     |
+------------------------+------------------------------+------------------------+---------------+

| 
