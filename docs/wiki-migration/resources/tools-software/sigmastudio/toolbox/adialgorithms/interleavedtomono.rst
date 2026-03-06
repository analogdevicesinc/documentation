Interleaved to Mono
===================

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`
| |int_mono.png|\ \|

"Interleaved to Mono" is used to de-interleave two channels from an interleaved input into two separate mono channels.

Input Pins
----------

+---------------------+------------------------------------+----------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description |
+=====================+====================================+======================+
| Pin 0: Multichannel | dec - audio                        | Multichannel input   |
+---------------------+------------------------------------+----------------------+

Output Pins
-----------

+-------------------+------------------------------------+--------------------------+
| Name              | Format [int/dec] - [control/audio] | Function Description     |
+===================+====================================+==========================+
| Pin 0: Mono Out 1 | decimal - audio                    | Mono source audio output |
+-------------------+------------------------------------+--------------------------+
| Pin 1: Mono Out 2 | decimal - audio                    | Mono source audio output |
+-------------------+------------------------------------+--------------------------+

Algorithm Details
-----------------

+----------------------------+----------------------------------------------------+
| Toolbox Path               | ADI algorithm - Multichannel - Interleaved to mono |
+----------------------------+----------------------------------------------------+
| Cores Supported            | ADSP-214xx                                         |
|                            | ADSP-SC5xx/215xx                                   |
|                            | ADSP-213xx                                         |
+----------------------------+----------------------------------------------------+
| "Grow Algorithm" Supported | It will grow up to 14                              |
+----------------------------+----------------------------------------------------+
| "Add Algorithm" Supported  | no                                                 |
+----------------------------+----------------------------------------------------+

.. |int_mono.png| image:: https://wiki.analog.com/_media/int_mono.png
