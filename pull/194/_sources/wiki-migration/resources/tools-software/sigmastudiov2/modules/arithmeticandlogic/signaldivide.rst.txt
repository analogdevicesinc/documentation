:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Signal Divide
=============

| 
| |div.png|

Description
-----------

| The Signal Divide block divide two incoming signals. The division is performed by using the Newton-Rapson method.

Variants
--------

-  Signal Divide
-  Complex Signal Divide

|

| ===== Targets Supported =====

+-----------------------+------------+------------------+---------------+------------------+
| Name                  | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=======================+============+==================+===============+==================+
| Signal Divide         | B/S        | B/S              | B/S           | B                |
+-----------------------+------------+------------------+---------------+------------------+
| Complex Signal Divide | NA         | NA               | B             | NA               |
+-----------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

======== ======= ===============
Name     Type    Description
======== ======= ===============
Divident Control Input channel 0
Divisor  Control Input channel 1
======== ======= ===============

Output
~~~~~~

====== ======= ================
Name   Type    Description
====== ======= ================
Output Control Output channel 0
====== ======= ================

Configurable Parameters
-----------------------

No configurable parameters

DSP Parameters
--------------

NO DSP Parameters

.. |div.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/div.png
