Cross Mux
=========

:doc:`Click here to return to the Multiplexers/Demultiplexers page </wiki-migration/resources/tools-software/sigmastudio/toolbox/multiplexersdemultiplexers>`

| 
| |crosmux.png|

Description
-----------

| The Cross Mux block allows route an input to one of selected output pins. The output for each input is selected based on the numeric value on the control.
| ===== Targets Supported =====

========= ========== ================ =============
Name      ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x
========= ========== ================ =============
Cross Mux Block      Block            NA
========= ========== ================ =============

| 
| ===== Pins =====

Input
~~~~~

======================= ===== ===============
Name                    Type  Description
======================= ===== ===============
Input<fc #ff0000>X</fc> Audio Input Channel X
======================= ===== ===============

Output
~~~~~~

======================== ===== ================
Name                     Type  Description
======================== ===== ================
Output<fc #ff0000>X</fc> Audio Output Channel X
======================== ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+---------------------------------+---------------+----------+-------------------------------------------------------------------------+
| GUI Parameter                   | Default Value | Range    | Function Description                                                    |
+=================================+===============+==========+=========================================================================+
| Index_Channel<fc #ff0000>X</fc> | 0             | 0 to 100 | Selects the output channel to route the input                           |
+---------------------------------+---------------+----------+-------------------------------------------------------------------------+
| NumInputs                       | 1             | 1 to 23  | Number of input channels. Change in this value requires re-compilation  |
+---------------------------------+---------------+----------+-------------------------------------------------------------------------+
| NumOuputs                       | 1             | 1 to 23  | Number of output channels. Change in this value requires re-compilation |
+---------------------------------+---------------+----------+-------------------------------------------------------------------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== DSP Parameters =====

+---------------------------------+-----------------------------------------------+------------------------+---------------+
| Parameter Name                  | Description                                   | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+=================================+===============================================+========================+===============+
| Index_Channel<fc #ff0000>X</fc> | Selects the output channel to route the input | Float                  | NA            |
+---------------------------------+-----------------------------------------------+------------------------+---------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

.. |crosmux.png| image:: https://wiki.analog.com/_media/crosmux.png
