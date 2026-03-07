:doc:`Click here to return to the Mixers and Splitters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mixersandsplitters>`

Signal Splitter
===============

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/blocksplitter.png
   :alt: blocksplitter.png

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

+-----------------------------+------------+------------------+---------------+------------------+
| Name                        | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=============================+============+==================+===============+==================+
| Splitter                    | B/S        | B/S              | NA            | NA               |
+-----------------------------+------------+------------------+---------------+------------------+
| Block Splitter              | NA         | NA               | B             | NA               |
+-----------------------------+------------+------------------+---------------+------------------+
| Splitter (Frequency Domain) | NA         | NA               | B             | NA               |
+-----------------------------+------------+------------------+---------------+------------------+
| Complex Splitter            | NA         | NA               | B             | NA               |
+-----------------------------+------------+------------------+---------------+------------------+

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
| NumChannels        | 2             | 20    | Number of output channels. Change in this value requires re-compilation |
+--------------------+---------------+-------+-------------------------------------------------------------------------+

| 
