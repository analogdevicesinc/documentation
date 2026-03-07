Block T Connection
==================

| 
| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| Block T connection takes the Block of real signals as input and pass the signal to each Output Pin.
| |image1|
| ====Input Pins====

+---------------------+------------------------------------+----------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description |
+=====================+====================================+======================+
| Pin 0: Input Signal | audio                              | input signal         |
+---------------------+------------------------------------+----------------------+

| 
| ====Output Pins====

+----------------------+------------------------------------+----------------------------------------------+
| Name                 | Format [int/dec] - [control/audio] | Function Description                         |
+======================+====================================+==============================================+
| Pin 1: Output Signal | audio                              | Output signal is pass trough of input signal |
+----------------------+------------------------------------+----------------------------------------------+

| 
| ====Grow Algorithm==== Grow algorithm supported for Output pins up to 8 channels.
| |image2|
| ====Add Algorithm==== Add algorithm supported for the module.
| ====Supported DSPs===== IDspSigma300 (Block Schematic only)

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/blocktconnection.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/blocktconnectiongrowth.png
