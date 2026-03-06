| :doc:`Click here to return to the basicdsp page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

Pooled Delay
============

| 
| This Module contains a common pool of delay buffer, which can be used for introducing delay in one or more channels subject to a total maximum delay of 120 ms. The number of channels can be grown up to 14. When the sum of the individual maximum delays of channels exceed 120 ms, only the first N channels whose delays can be accommodated would be applied. The rest of the channels are bypassed without any delay.
| |image1|
| ====Input Pins====

============ ================================== ====================
Name         Format [int/dec] - [control/audio] Function Description
============ ================================== ====================
Pin 0: Input decimal - Audio                    Audio Input
============ ================================== ====================

| 
| ====Output Pins====

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - Audio                    Delayed Output
============= ================================== ====================

| 
| ==== Grow Algorithm ==== The module supports Growth. The module does not support Add.
| ====Configuration====
| |image2|
| ^GUI Control Name^Default Value^Range^Function Description^

+-----------+-----+----------------+----------------------------------------------------+
| Delay     | 0ms | 0 to Max Delay | Delay(milliseconds), fractional values are allowed |
+-----------+-----+----------------+----------------------------------------------------+
| Max Delay | 1ms | 0 to 120ms     | Maximum allowed delay(milliseconds)                |
+-----------+-----+----------------+----------------------------------------------------+

| 
| ====DSP Parameter Information====

+------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------+
| GUI Control Name | Compiler Name                                                                                      | Function Description                                   |
+==================+====================================================================================================+========================================================+
| Delay            | <fc #008000>PooledDelay_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Delay</fc><fc #800000>1</fc>    | Delay(milliseconds), fractional values are allowed     |
+------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------+
| Max Delay        | <fc #008000>PooledDelay_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>MaxDelay</fc><fc #800000>1</fc> | Max Delay(milliseconds), fractional values are allowed |
+------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name
-  <fc #800000>Brown</fc> - Stage number

| 
| ==== Algorithm Description ==== This Module contains a common pool of delay buffer, which can be used for introducing delay in one or more channels subject to a total maximum delay of 120 ms. The number of channels can be grown up to 14. When the sum of the individual maximum delays of channels exceed 120 ms, only the first N channels whose delays can be accommodated would be applied. The rest of the channels are bypassed without any delay.
| ==== Supported ICs ====

-  ADSP215xx
-  ADSPSC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/pooleddelay-tbx.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/pooleddelay-gui.jpg
