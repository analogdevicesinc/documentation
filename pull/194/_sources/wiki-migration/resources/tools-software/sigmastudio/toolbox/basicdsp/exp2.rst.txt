Exp2
====

| :doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| This module computes the 2 Power of the incoming data

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/2powerx.jpg
   :width: 200px

| 
| ====Input Pins====

+-------------------+------------------------------------+--------------------------------------------+
| Name              | Format [int/dec] - [control/audio] | Function Description                       |
+===================+====================================+============================================+
| Pin 0: Input Data | decimal - audio                    | Input data whose 2 Power is to be computed |
+-------------------+------------------------------------+--------------------------------------------+

| 
| ====Output Pins==== ^Name^Format [int/dec] - [control/audio]^Function Description^ \|Pin 0: 2 Power value|decimal - control|Pow2(input)\| \|Pin 1: 2 Overflow/Underflow flag|decimal - control|Flag set when the output of the module Overflows/Underflows\|
| ====Configuration==== |image1|

Grow Algorithm
--------------

The module supports Add functionality. Growth is not supported.

GUI Controls
------------

None

DSP Parameter Information
-------------------------

None

Algorithm Description
---------------------

2 Power x is equivalent to e^(x ln 2). Taylor series expansion of e^x is used to compute the value of 2 Power x.

Supported IC's
--------------

| 1. ADSP-213xx
| 2. ADSP-214xx
| 3. ADSP-SC5xx
| 4. ADSP-215xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/2powerx_config.jpg
   :width: 100px
