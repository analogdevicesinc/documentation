:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Register Read or Write
======================

|registerread.png| |regwrite.png|

Description
-----------

| The Register Read module reads any user accessible register from the DSP and gives out in the output Pin.
| The Register Write module writes the value in the input pin to the DSP register address configured.
| ===== Configuration ===== This module supports growth. Address control will be repeated for each channels when grown. And address can be specified either in hexadecimal or decimal.

Variants
--------

-  Register Read
-  Register Write

| 
| ===== Targets Supported =====

+----------------+------------+------------------+---------------+------------------+
| Name           | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+================+============+==================+===============+==================+
| Register Read  | NA         | NA               | S             | NA               |
+----------------+------------+------------------+---------------+------------------+
| Register Write | NA         | NA               | S             | NA               |
+----------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

======================= ======= ========================================
Name                    Type    Description
======================= ======= ========================================
Input<fc #ff0000>X</fc> Control Input Channel X (Only for RegisterWrite)
======================= ======= ========================================

Output
~~~~~~

+--------------------------+---------+------------------------------------------+
| Name                     | Type    | Description                              |
+==========================+=========+==========================================+
| Output<fc #ff0000>X</fc> | Control | Output Channel X (Only for RegisterRead) |
+--------------------------+---------+------------------------------------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+---------------------------------+---------------+-----------------+-----------------------------------------------------------+
| GUI Parameter                   | Default Value | Range           | Function Description                                      |
+=================================+===============+=================+===========================================================+
| Address <fc #ff0000>X</fc>      | 0xF000        | 0xF000 - 0xF890 | Register Address to be read/write                         |
+---------------------------------+---------------+-----------------+-----------------------------------------------------------+
| Address Type <fc #ff0000>X</fc> | Hex           | Hex / Dec       | Address can be specified either in hexadecimal or decimal |
+---------------------------------+---------------+-----------------+-----------------------------------------------------------+

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== DSP Parameters =====

============== ================ ====================== =============
Parameter Name Description      ADSP-214xx/SC5xx/215xx ADAU145x/146x
============== ================ ====================== =============
address        Register address NA                     Integer32
============== ================ ====================== =============

.. |registerread.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/registerread.png
.. |regwrite.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/regwrite.png
