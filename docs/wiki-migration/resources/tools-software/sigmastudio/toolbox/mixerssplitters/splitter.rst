Signal Splitter
===============

:doc:`Click here to return to the Mixers/Splitters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/mixerssplitters>`

| 
| |image1|

Description
-----------

| The Splitter block splits an input signal to two are more outputs.
| Complex Splitter module split the complex input to real part and imaginary part.
| ===== Variants =====

-  Splitter
-  Block Splitter
-  Splitter (Frequency Domain)
-  Complex Splitter

| 
| ===== Targets Supported =====

+-----------------------------+-----------------+------------------+---------------+
| Name                        | ADSP-214xx      | ADSP-215xx/SC5xx | ADAU145x/146x |
+=============================+=================+==================+===============+
| Splitter                    | Block/Schematic | Block/Schematic  | NA            |
+-----------------------------+-----------------+------------------+---------------+
| Block Splitter              | NA              | NA               | Block         |
+-----------------------------+-----------------+------------------+---------------+
| Splitter (Frequency Domain) | NA              | NA               | Block         |
+-----------------------------+-----------------+------------------+---------------+
| Complex Splitter            | NA              | NA               | Block         |
+-----------------------------+-----------------+------------------+---------------+

| 
| ===== Pins =====

Input
~~~~~

+--------+---------------------------------------------------------------------+-----------------+
| Name   | Type                                                                | Description     |
+========+=====================================================================+=================+
| Input0 | Audio(Complex Pin for Complex Splitter & Splitter Frequency domain) | Input channel 0 |
+--------+---------------------------------------------------------------------+-----------------+

Output
~~~~~~

+--------------------------+----------------------------------------------------+------------------+
| Name                     | Type                                               | Description      |
+==========================+====================================================+==================+
| Output<fc #ff0000>X</fc> | Control(Complex Pin for Splitter Frequency domain) | Output channel X |
+--------------------------+----------------------------------------------------+------------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-------+-------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range | Function Description                                                    |
+====================+===============+=======+=========================================================================+
| NumChannels        | 2             | 1-14  | Number of output channels. Change in this value requires re-compilation |
+--------------------+---------------+-------+-------------------------------------------------------------------------+

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/splitter.png
