Multiple Control Linear Gain
============================

:doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

This module applies gain to the input and passes to the output pin. When the
module is grown the gain value is separate for each of the inputs. It comes in
two versions.

-  Multiple Control Linear Gain (No Slew)
-  Multiple Control Linear Gain (HW Slew)

HW slew version shall apply the slew whenever gain parameter is changed to avoid
click noise.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/mclg.png
   :align: center

Input Pins
----------

============ ================================== ====================
Name         Format [int/dec] - [control/audio] Function Description
============ ================================== ====================
Pin 0: Input dec- audio                         Input Audio
============ ================================== ====================

| ===== Output Pins =====

============= ================================== =======================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== =======================
Pin 1: Output dec- audio                         Output audio with gain.
============= ================================== =======================

Grow Algorithm
--------------

The module currently supports growth. Both the control and pins are grown for
each growth. Add algorithm functionality is not supported. The figure below
shows the module when grown for 5 channels.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/mclg2.png
   :align: center

Configurations
--------------

+------------------+---------------+-----------------+-----------------------------+
| GUI Control Name | Default Value | Range           | Function Description        |
+==================+===============+=================+=============================+
| Gain\*           | 1             | -128 to 127.999 | Gain value in linear scale. |
+------------------+---------------+-----------------+-----------------------------+

**Note:** Gain control will be repeated for each channels when grown.

Slew Configuration
------------------

In the case of HW slew version. The slew shape can be chosen by right clicking
on the module.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/mclg3.png
   :align: center

DSP Parameter Information
-------------------------

No Slew
~~~~~~~

+------------------+----------------------------------+----------------------------+
| GUI Control Name | Compiler Name                    | Function Description       |
+==================+==================================+============================+
| Gain             | MultipleControlGainS300Alg1gain0 | Gain Value in linear scale |
+------------------+----------------------------------+----------------------------+

| 
| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name
-   Brown - Channel Number (Changes for each channel when grown)

HW Slew
~~~~~~~

+------------------+----------------------------------------+----------------------------+
| GUI Control Name | Compiler Name                          | Function Description       |
+==================+========================================+============================+
| Slew Mode        | MultipleControlGainHWSelwAlg1slew_mode | HW Slew Mode               |
+------------------+----------------------------------------+----------------------------+
| Gain             | MultipleControlGainHWSelwAlg1gain0     | Gain Value in linear scale |
+------------------+----------------------------------------+----------------------------+

| 
| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name
-   Brown - Channel Number (Changes for each channel when grown)

| **Note:** Gain parameter shall be repeated for each channel when the algorithm is grown.

Supported ICs
-------------

-  ADAU145x
