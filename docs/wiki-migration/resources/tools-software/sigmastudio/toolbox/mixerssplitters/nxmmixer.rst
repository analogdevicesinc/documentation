NxM Mixer
=========

:doc:`Click here to return to the Mixers/Splitters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/mixerssplitters>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/nm.png
   :alt: nm.png

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/gui.png
   :alt: gui.png

Description
-----------

The NxM Mixer block multiplies the inputs with respective gains and mixes N
number of inputs and sends the result to the M number of outputs.

Usage
-----

Click on the icon to open the NxM Mixer window to configure the gain for
respective input channels for respective outputs.

Targets Supported
-----------------

======== ========== ================ =============
Name     ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x
======== ========== ================ =============
NXMMixer Block      Block            Schematic
======== ========== ================ =============

Pins
----

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
InputX Audio Input channel X
====== ===== ===============

Output
~~~~~~

======= ======= ================
Name    Type    Description
======= ======= ================
OutputX Control Output channel X
======= ======= ================

Note:

-  X - Channel Index

Configurable Parameters
-----------------------

+-----------------------+---------------+-------------+-------------------------------------------------------------------------+
| GUI Parameter Name    | Default Value | Range       | Function Description                                                    |
+=======================+===============+=============+=========================================================================+
| GainDB_OutputM_InputN | 0 dB          | -30 to 6 dB | Gain factor                                                             |
+-----------------------+---------------+-------------+-------------------------------------------------------------------------+
| ISDb_OutputM_InputN   | True          | True/False  | Decides the Gain control in db/linear                                   |
+-----------------------+---------------+-------------+-------------------------------------------------------------------------+
| NumInputs             | 2             | 14          | Number of input channels. Change in this value requires re-compilation  |
+-----------------------+---------------+-------------+-------------------------------------------------------------------------+
| NumOutputs            | 1             | 15          | Number of output channels. Change in this value requires re-compilation |
+-----------------------+---------------+-------------+-------------------------------------------------------------------------+

Note:

-  M - Output Channel Index
-  N - Input Channel Index

DSP Parameters
--------------

+----------------+-----------------------+------------------------+---------------+
| Parameter Name | Description           | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=======================+========================+===============+
| GainArray      | scaling of the inputs | Float                  | FixInt8d24    |
+----------------+-----------------------+------------------------+---------------+
