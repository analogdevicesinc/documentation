SuperPhat Spatializer
=====================

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

+---+---+
| The SuperPhat block is an advanced algorithm that allows for a wider stereo image to be played back from two closely spaced speakers. This spatializer algorithm is only meant to widen signals that are already in stereo format, in order to enhance the image. The function is similar to the :doc:`Phat-Stereo </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/phatstereo>` algorithm but performs a much more advanced implementation of the algorithm to get a better effect. | |superphatpic1.png| |
+---+---+

Input Pins
----------

+--------------------+------------------------------------+--------------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description     |
+====================+====================================+==========================+
| Pin 0: Left Input  | decimal - audio                    | Left signal Audio input  |
+--------------------+------------------------------------+--------------------------+
| Pin 1: Right Input | decimal - audio                    | Right signal Audio input |
+--------------------+------------------------------------+--------------------------+

Output Pins
-----------

+---------------------+------------------------------------+-------------------------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description                |
+=====================+====================================+=====================================+
| Pin 0: Left Output  | decimal - audio                    | Stereo-Enhanced Left signal output  |
+---------------------+------------------------------------+-------------------------------------+
| Pin 0: Right Output | decimal - audio                    | Stereo-Enhanced Right signal output |
+---------------------+------------------------------------+-------------------------------------+

GUI Pins
--------

+------------------+---------------+------------+-----------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range      | Function Description                                                                          |
+==================+===============+============+===============================================================================================+
| Spread Frequency | 500 Hz        | 250 - 1000 | Controls the primary frequency used for spatialization.                                       |
+------------------+---------------+------------+-----------------------------------------------------------------------------------------------+
| Effect Gain      | 1.3           | 0.5-3      | Linear Gain value that controls the gain stages used in the effect for stereo spacialization. |
+------------------+---------------+------------+-----------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------+----------------------+---------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name        | Function Description                                                                  |
+==================+======================+=======================================================================================+
| Spread Frequency | SuperPhatAlg1spread1 | The spread frequency written to the DSP                                               |
+------------------+----------------------+---------------------------------------------------------------------------------------+
| Effect Gain      | SuperPhatAlg1gainHi  | When the Effect Gain is changed, 3 DSP coefficients are written to the Parameter RAM. |
|                  | SuperPhatAlg1gainLo  |                                                                                       |
|                  | SuperPhatAlg1gainInv |                                                                                       |
+------------------+----------------------+---------------------------------------------------------------------------------------+

Algorithm Description
---------------------

The SuperPhat algorithm is a playback spatializer that takes a stereo image, and widens the signal for playback from two closely spaced speakers. The algorithm accepts a stereo signal and outputs an enhanced stereo image for playback. The algorithm is based on proprietary filtering and gain adjustment in order to produce the widened image.

The two parameters available for adjustment Spread Frequency and Effect Gain, change the responsiveness of the effect. Depending on the actual physical end system, different values should be used to obtain the optimal effect. Subjective listening tests are the recommended way to set the values for these parameters.

Example
-------

| The following schematic image shows the SuperPhat algorithm in comparison with the :doc:`Phat-Stereo </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/phatstereo>` algorithm. Both algorithms have similar functions, but the effect is more pronounced with the SuperPhat algorithm at the cost of more instructions. This image shows the :doc:`Inputs </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/input>`, stereo `mux <https://wiki.analog.com/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/stereoswitchnx2>`__, and :doc:`outputs </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/output>`, along with the two methods for stereo spatialization offered in the SigmaStudio library.
| |superphatpic2.png|

Algorithm Details
-----------------

+----------------------------+--------------------------------------------------------------+
| Toolbox Path               | ADI Algorithms - Surround & 3D Audio - SuperPhat Spatializer |
+----------------------------+--------------------------------------------------------------+
| Cores Supported            | AD1940                                                       |
|                            | ADAU170x                                                     |
|                            | ADAU144x                                                     |
|                            | ADAU176x                                                     |
|                            | ADAU178x                                                     |
+----------------------------+--------------------------------------------------------------+
| "Grow Algorithm" Supported | no                                                           |
+----------------------------+--------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                           |
+----------------------------+--------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                           |
+----------------------------+--------------------------------------------------------------+
| Program RAM                | 162                                                          |
+----------------------------+--------------------------------------------------------------+
| Data RAM                   | 90                                                           |
+----------------------------+--------------------------------------------------------------+
| Parameter RAM              | 52                                                           |
+----------------------------+--------------------------------------------------------------+

.. |superphatpic1.png| image:: https://wiki.analog.com/_media/superphatpic1.png
.. |superphatpic2.png| image:: https://wiki.analog.com/_media/superphatpic2.png
