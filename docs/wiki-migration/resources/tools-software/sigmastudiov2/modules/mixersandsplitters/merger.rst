:doc:`Click here to return to the Mixers and Splitters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mixersandsplitters>`

Signal Merger
=============

| 
| |merger.png|
| ===== Variants =====

-  Signal Merger
-  Complex Signal Merger

| 
| ===== Description ===== The Signal Merger block mixes a group of input signals and automatically decreases the signal levels in proportion to the number of inputs. This block helps to avoid level clipping without the need to manually adjust mix levels.
| Complex Merger takes the real and imaginary part of input signal and merges to complex output signal. This is a block based module.
| ===== Targets Supported =====

====== ========== ================ ============= ================
Name   ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
====== ========== ================ ============= ================
Merger B/S        B/S              B/S           B
====== ========== ================ ============= ================

| 
| ===== Pins =====

Input
-----

====== ==================================== ===============
Name   Type                                 Description
====== ==================================== ===============
Input0 Audio(ComplexPin for complex merger) Input channel 0
Input1 Audio(ComplexPin for complex merger) Input channel 1
====== ==================================== ===============

Output
------

======= ====================================== ================
Name    Type                                   Description
======= ====================================== ================
Output0 Control(ComplexPin for complex merger) Output channel 0
======= ====================================== ================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-------+------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range | Function Description                                                   |
+====================+===============+=======+========================================================================+
| NumChannels        | 2             | 20    | Number of input channels. Change in this value requires re-compilation |
+--------------------+---------------+-------+------------------------------------------------------------------------+

DSP Parameters
~~~~~~~~~~~~~~

+--------------------------+---------------+------------------------+---------------+
| Parameter Name           | Description   | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+==========================+===============+========================+===============+
| gain[<fc #ff0000>X</fc>] | 1/NumChannels | NA                     | FixPoint8d24  |
+--------------------------+---------------+------------------------+---------------+

Note:

-  <fc #ff0000>X</fc> - size of array. If NumChannels<4 then X=NumChannels else X=4

| 

.. |merger.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/merger.png
