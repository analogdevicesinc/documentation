Mono to Interleaved
===================

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`
| |mot_int.png|\ \|

Description
-----------

"Mono to Interleaved" is used to interleave two mono channels into one output pin.

Input Pins
----------

+---------------------+------------------------------------+-------------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description    |
+=====================+====================================+=========================+
| Pin 1: Mono input 1 | decimal - audio                    | Mono source audio input |
+---------------------+------------------------------------+-------------------------+
| Pin 2: Mono input 2 | decimal - audio                    | Mono source audio input |
+---------------------+------------------------------------+-------------------------+

Output Pins
-----------

+---------------------+------------------------------------+----------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description |
+=====================+====================================+======================+
| Pin 0: Multichannel | decimal - audio                    | Multichannel output  |
+---------------------+------------------------------------+----------------------+

Algorithm Details
-----------------

+----------------------------+----------------------------------------------------+
| Toolbox Path               | ADI algorithm - Multichannel - Mono to interleaved |
+----------------------------+----------------------------------------------------+
| Cores Supported            | ADSP-214xx                                         |
|                            | ADSP-SC5xx/215xx                                   |
|                            | ADSP-213xx                                         |
+----------------------------+----------------------------------------------------+
| "Grow Algorithm" Supported | It will grow up to 14                              |
+----------------------------+----------------------------------------------------+
| "Add Algorithm" Supported  | no                                                 |
+----------------------------+----------------------------------------------------+

.. |mot_int.png| image:: https://wiki.analog.com/_media/mot_int.png
