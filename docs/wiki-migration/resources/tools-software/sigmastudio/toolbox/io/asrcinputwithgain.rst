ASRC Input With Gain
====================

| :doc:`Click here to return to the Input/Output section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/io>`
| This module can be used to read data from ASRC and apply gain before passing to other modules in the schematic
| |image1|
| ===== Input Pins ===== No Input pins.

Output Pins
-----------

============== ================================== ====================
Name           Format [int/dec] - [control/audio] Function Description
============== ================================== ====================
Pin 0: ASRC In decimal - audio                    From ASRC with Gain
============== ================================== ====================

| 

Grow Algorithm
--------------

| The module can be grown upto 16 channels to support 16 ASRC In pins. When grown each input has a gain control corresponding to it.
| |image2|
| ===== Configurations ===== Gain can be configured for each channels.
| ^GUI Control Name^Default Value^Range^Function Description^

+------------------------------+----------+------------------+-------------------------------------------------------------------------------------------------------------+
| Gain                         | 1        | -128 to 127.999  | Linear Gain Value                                                                                           |
+------------------------------+----------+------------------+-------------------------------------------------------------------------------------------------------------+
| Gain Sharing Enable/Disable. | Disabled | Enabled/Disabled | Gain can be shared between input channels. Recompilation is required when gain sharing is enabled/disabled. |
+------------------------------+----------+------------------+-------------------------------------------------------------------------------------------------------------+

| 
| |image3|
| Click on the TinyCircle next to gain to enable/disable sharing of gain between channels.

In the example shown above.

-  Channel 0 and Channel 1 shares same gain.
-  Channel 2 to 7 has separate gains.
-  Channel 8 and 9 shares same gain.

All gains are without slew

DSP Parameter Information
-------------------------

+------------------+---------------------------------------------------------------------------------------------+-----------------------------+
| GUI Control Name | Compiler Name                                                                               | Function Description        |
+==================+=============================================================================================+=============================+
| Gain             | <fc #008000>ASRCInwithGainAlg</fc><fc #ff0000>1</fc><fc #000080>gain</fc><fc #800000>0</fc> | Gain Value for each channel |
+------------------+---------------------------------------------------------------------------------------------+-----------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name
-  <fc #800000> Brown</fc> - Channel Number (Changes for each channel)

Supported ICs
-------------

-  ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/asrcinwithgain.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/asrcinwithgain2.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/asrcinwithgain4.jpg
