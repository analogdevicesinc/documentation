:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

ControlParse
============

| 
| |controlparse.png|

Description
-----------

| This module parse specific sample value back from a block of samples and pass to outputs
| ===== Targets Supported =====

============ ========== ================ ============= ================
Name         ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============ ========== ================ ============= ================
ControlParse B          B                NA            B
============ ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

====== ===== ==============
Name   Type  Description
====== ===== ==============
Input0 Audio Input channel0
====== ===== ==============

Output
~~~~~~

======================== ===== ================
Name                     Type  Description
======================== ===== ================
Output<fc #ff0000>X</fc> Audio Output channel X
======================== ===== ================

| 
| ===== Configurable Parameters =====

+----------------------------------+---------------+----------------+--------------------------------------+
| GUI Parameter Name               | Default Value | Range          | Function Description                 |
+==================================+===============+================+======================================+
| Sample_channel<fc #ff0000>0</fc> | 1             | 1 to BlockSize | To set the sample value of the block |
+----------------------------------+---------------+----------------+--------------------------------------+

| 
| ===== DSP Parameters =====

+----------------------------------+----------------------+------------------------+---------------+
| Parameter Name                   | Description          | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+==================================+======================+========================+===============+
| Sample_Channel<fc #ff0000>0</fc> | Current Sample value | FixInt32               | NA            |
+----------------------------------+----------------------+------------------------+---------------+

| 

.. |controlparse.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/controlparse.png
