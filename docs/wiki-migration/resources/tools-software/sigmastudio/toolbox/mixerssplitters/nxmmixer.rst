NxM Mixer
=========

:doc:`Click here to return to the Mixers/Splitters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/mixerssplitters>`

| 
| |nm.png|
| |gui.png|

Description
-----------

| The NxM Mixer block multiplies the inputs with respective gains and mixes N number of inputs and sends the result to the M number of outputs.

Usage
-----

| Click on the icon to open the NxM Mixer window to configure the gain for respective input channels for respective outputs.
| ===== Targets Supported =====

======== ========== ================ =============
Name     ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x
======== ========== ================ =============
NXMMixer Block      Block            Schematic
======== ========== ================ =============

Pins
----

Input
~~~~~

======================= ===== ===============
Name                    Type  Description
======================= ===== ===============
Input<fc #ff0000>X</fc> Audio Input channel X
======================= ===== ===============

Output
~~~~~~

======================== ======= ================
Name                     Type    Description
======================== ======= ================
Output<fc #ff0000>X</fc> Control Output channel X
======================== ======= ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

Configurable Parameters
-----------------------

+---------------------------------------------------------+---------------+-------------+-------------------------------------------------------------------------+
| GUI Parameter Name                                      | Default Value | Range       | Function Description                                                    |
+=========================================================+===============+=============+=========================================================================+
| GainDB_Output<fc #ff0000>M</fc>_Input<fc #ff0000>N</fc> | 0 dB          | -30 to 6 dB | Gain factor                                                             |
+---------------------------------------------------------+---------------+-------------+-------------------------------------------------------------------------+
| ISDb_Output<fc #ff0000>M</fc>_Input<fc #ff0000>N</fc>   | True          | True/False  | Decides the Gain control in db/linear                                   |
+---------------------------------------------------------+---------------+-------------+-------------------------------------------------------------------------+
| NumInputs                                               | 2             | 14          | Number of input channels. Change in this value requires re-compilation  |
+---------------------------------------------------------+---------------+-------------+-------------------------------------------------------------------------+
| NumOutputs                                              | 1             | 15          | Number of output channels. Change in this value requires re-compilation |
+---------------------------------------------------------+---------------+-------------+-------------------------------------------------------------------------+

Note:

-  <fc #ff0000>M</fc> - Output Channel Index
-  <fc #ff0000>N</fc> - Input Channel Index

DSP Parameters
--------------

+----------------+-----------------------+------------------------+---------------+
| Parameter Name | Description           | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=======================+========================+===============+
| GainArray      | scaling of the inputs | Float                  | FixInt8d24    |
+----------------+-----------------------+------------------------+---------------+

.. |nm.png| image:: https://wiki.analog.com/_media/nm.png
.. |gui.png| image:: https://wiki.analog.com/_media/gui.png
