Special T Connection
====================

| :doc:`Click here to return to the System page </wiki-migration/resources/tools-software/sigmastudio/toolbox/systemschematicdesign>`

|

| |specialtconnection.png|

Description
-----------

The Special T Connection splits a signal into multiple times, depending on the type specified.

There are two types which can be selected by right clicking the module

PCMx - Only PCMX input and output modules can be connected using this type of t connection.

BS24 - Only compressed audio input and output modules can be connected using this type of t connection

Targets Supported
-----------------

==================== ========== ================ =============
Name                 ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x
==================== ========== ================ =============
Special T connection Block      Block            NA
==================== ========== ================ =============

Pins
----

Input
~~~~~

For PCMX type :

===== ========= =============== ======
Name  Type      Description     Signal
===== ========= =============== ======
Reset PCMx data Input channel 0 Analog
===== ========= =============== ======

For BS24 type :

====== ===================== =============== =======
Name   Type                  Description     Signal
====== ===================== =============== =======
Input0 Compressed audio data Input channel 0 Digital
====== ===================== =============== =======

Output
~~~~~~

For PCMX type :

======= ========= ================ ======
Name    Type      Description      Signal
======= ========= ================ ======
Output0 PCMx data Output channel 0 Analog
======= ========= ================ ======

For BS24 type :

======= ===================== ================ =======
Name    Type                  Description      Signal
======= ===================== ================ =======
Output0 Compressed audio data Output channel 0 Digital
======= ===================== ================ =======

.. |specialtconnection.png| image:: https://wiki.analog.com/_media/specialtconnection.png
