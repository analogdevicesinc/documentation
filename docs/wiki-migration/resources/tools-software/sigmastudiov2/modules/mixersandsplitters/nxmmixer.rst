:doc:`Click here to return to the Mixers and Splitters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mixersandsplitters>`

NxM Mixer
=========

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/nxmmixer.png
   :alt: nxmmixer.png

NxM Mixer

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/nxmmixerform.png
   :alt: nxmmixerform.png

NxM Mixer Linear

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/nxmlinear.png
   :alt: nxmlinear.png

Description
-----------

The NxM Mixer block multiplies the inputs with respective gains and mixes N
number of inputs and sends the result to the M number of outputs.

Variants
--------

-  NxM Mixer
-  NxM Mixer Linear
-  2x1 Mixer(Linear)
-  3x1 Mixer (Linear HW Slew)
-  4x1 Mixer(Linear)

Usage
-----

Click on the icon to open the NxM Mixer window to configure the gain for
respective input channels for respective outputs.

Targets Supported
-----------------

+---------------------------+------------+------------------+---------------+------------------+
| Name                      | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===========================+============+==================+===============+==================+
| NXMMixer                  | B          | B                | S             | B                |
+---------------------------+------------+------------------+---------------+------------------+
| NXMMixer (Linear)         | NA         | NA               | S             | NA               |
+---------------------------+------------+------------------+---------------+------------------+
| 2x1 Mixer (Linear)        | NA         | NA               | S             | NA               |
+---------------------------+------------+------------------+---------------+------------------+
| 3x1 Mixer (Linear HWSlew) | NA         | NA               | S             | NA               |
+---------------------------+------------+------------------+---------------+------------------+
| 4x1 Mixer (Linear)        | NA         | NA               | S             | NA               |
+---------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

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
| NumInputs             | 2             | 20          | Number of input channels. Change in this value requires re-compilation  |
+-----------------------+---------------+-------------+-------------------------------------------------------------------------+
| NumOutputs            | 1             | 20          | Number of output channels. Change in this value requires re-compilation |
+-----------------------+---------------+-------------+-------------------------------------------------------------------------+
| SlewType              | RC Slew       | NA          | Slew type. Applicable to HW slew modules                                |
+-----------------------+---------------+-------------+-------------------------------------------------------------------------+
| CustomVal             | 0x208A        | NA          | Custom slew value. Applicable to HW slew modules                        |
+-----------------------+---------------+-------------+-------------------------------------------------------------------------+

Note:

-  M - Output Channel Index
-  N - Input Channel Index

DSP Parameters
--------------

+----------------+----------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                        | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+====================================================+========================+===============+
| GainArray      | scaling of the inputs                              | Float                  | FixInt8d24    |
+----------------+----------------------------------------------------+------------------------+---------------+
| slew_mode      | Slew mode and value for HW slew (only for HW slew) | NA                     | Integer       |
+----------------+----------------------------------------------------+------------------------+---------------+
