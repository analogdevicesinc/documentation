Mono2Stereo
===========

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

+------------------------------------------------------------------------------------------------+-----------------+
| The Mono2Stereo algorithm takes a mono signal and creates a stereo image from a single source. | |mono2pic1.png| |
+------------------------------------------------------------------------------------------------+-----------------+

Input Pins
----------

+-------------------+------------------------------------+-------------------------+
| Name              | Format [int/dec] - [control/audio] | Function Description    |
+===================+====================================+=========================+
| Pin 0: Audio In 1 | dec - audio                        | Mono source audio input |
+-------------------+------------------------------------+-------------------------+

Output Pins
-----------

+--------------------+------------------------------------+----------------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description       |
+====================+====================================+============================+
| Pin 0: Audio Out 1 | decimal - audio                    | Left channel audio output  |
+--------------------+------------------------------------+----------------------------+
| Pin 1: Audio Out 2 | decimal - audio                    | Right channel audio output |
+--------------------+------------------------------------+----------------------------+

Algorithm Description
---------------------

The Mono2Stereo algorithm uses filtering processing to create two separate channels from a single source. There is no user control necessary for this algorithm. The block accepts a single input and the output is a stereo signal.

Example
-------

| The following image shows the Mono2Stereo block being used to separate a single source input into a left and right output. The stereo selection `Mux <https://wiki.analog.com/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers/stereoswitchnx2>`_ allows selection for comparison between the same mono source being sent to left and right versus, the stereo signal from the Mono2Stereo block.
| |mono2pic2.png|

Algorithm Details
-----------------

+----------------------------+----------------------------------------------------+
| Toolbox Path               | ADI Algorithms - Surround & 3D Audio - Mono2Stereo |
+----------------------------+----------------------------------------------------+
| Cores Supported            | ADAU144x                                           |
|                            | ADAU176x                                           |
|                            | ADAU178x                                           |
+----------------------------+----------------------------------------------------+
| "Grow Algorithm" Supported | no                                                 |
+----------------------------+----------------------------------------------------+
| "Add Algorithm" Supported  | no                                                 |
+----------------------------+----------------------------------------------------+
| Subroutine/Loop Based      | no                                                 |
+----------------------------+----------------------------------------------------+
| Program RAM                | 20                                                 |
+----------------------------+----------------------------------------------------+
| Data RAM                   | 33                                                 |
+----------------------------+----------------------------------------------------+
| Parameter RAM              | 26                                                 |
+----------------------------+----------------------------------------------------+

.. |mono2pic1.png| image:: https://wiki.analog.com/_media/mono2pic1.png
.. |mono2pic2.png| image:: https://wiki.analog.com/_media/mono2pic2.png
