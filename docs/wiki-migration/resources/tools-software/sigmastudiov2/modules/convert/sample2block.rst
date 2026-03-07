:doc:`Click here to return to the Convert page </wiki-migration/resources/tools-software/sigmastudiov2/modules/convert>`

Sample to Block
===============

| |sample2block.png|
| ===== Description ===== This module is used to transition from sample processing schematic to block processing schematic.
| ===== Targets Supported =====

+-----------------+------------+------------------+---------------+------------------+
| Name            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=================+============+==================+===============+==================+
| Block to Sample | NA         | NA               | S/B           | NA               |
+-----------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

===== ===== ====================
Name  Type  Description
===== ===== ====================
Input Audio Sample Input channel
===== ===== ====================

Output
------

====== ===== ====================
Name   Type  Description
====== ===== ====================
Output Audio Block Output channel
====== ===== ====================

| 
| ===== Configurable Parameters =====

+---------------+---------------+------------------------------+-------------------------------------+
| GUI Parameter | Default Value | Range                        | Function Description                |
+===============+===============+==============================+=====================================+
| Size          | 64            | 8,16,32,64,124, 256,512,1024 | BlockSize of the output channel     |
+---------------+---------------+------------------------------+-------------------------------------+
| Memory        | DM0           | DM0/DM1                      | Memory to be used for block buffers |
+---------------+---------------+------------------------------+-------------------------------------+

| 
| ===== DSP Parameters ===== NO DSP parameters

.. |sample2block.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sample2block.png
