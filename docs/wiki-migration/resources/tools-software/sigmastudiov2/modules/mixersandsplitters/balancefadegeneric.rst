:doc:`Click here to return to the Mixers and Splitters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/mixersandsplitters>`

Balance Fader Generic
=====================

| 
| |balancefadergeneric.png|
| |balanceconfig.png| |faderconfig.png|

Description
-----------

| 
| Reposition the image in front of the listener by adjusting gain levels of speakers. User can configure all the front and rear channel coefficients values.

Usage
-----

| Click on the config button to open the balance fader coefficient window to configure the gain for respective input channels for respective outputs.
| ===== Targets Supported =====

+-----------------------+------------+------------------+---------------+------------------+
| Name                  | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=======================+============+==================+===============+==================+
| Balance Fader Generic | B          | B                | NA            | B                |
+-----------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

================ ===== ==============================================
Name             Type  Description
================ ===== ==============================================
FrontRight_Input Audio Front right channel input to the balance fader
FrontLeft_Input  Audio Front left channel input to the balance fader
RearRight_Input  Audio Rear right channel input to the balance fader
RearLeft_Input   Audio Rear left channel input to the balance fader
Center_Input     Audio Center channel input to the balance fader
SW_Input         Audio Sub woofer input to the balance fader
================ ===== ==============================================

Output
~~~~~~

+-------------------+-------+---------------------------------------------------+
| Name              | Type  | Description                                       |
+===================+=======+===================================================+
| FrontRight_Output | Audio | Front right channel output from the balance fader |
+-------------------+-------+---------------------------------------------------+
| FrontLeft_Output  | Audio | Front left channel output from the balance fader  |
+-------------------+-------+---------------------------------------------------+
| RearRight_Output  | Audio | Rear right channel output from the balance fader  |
+-------------------+-------+---------------------------------------------------+
| RearLeft_Output   | Audio | Rear left channel output from the balance fader   |
+-------------------+-------+---------------------------------------------------+
| Center_Output     | Audio | Center channel output from the balance fader      |
+-------------------+-------+---------------------------------------------------+
| SW_Output         | Audio | Sub woofer output from the balance fader          |
+-------------------+-------+---------------------------------------------------+

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-----------+----------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range     | Function Description                                                             |
+====================+===============+===========+==================================================================================+
| Balance            | 0             | -10 to 10 | Controls the balance of audio level between the left and right channels          |
+--------------------+---------------+-----------+----------------------------------------------------------------------------------+
| Fade               | 0             | -10 to 10 | Controls the fade out of audio level between the front and rear channels.        |
+--------------------+---------------+-----------+----------------------------------------------------------------------------------+
| StepSize (SW Slew) | 11            | 8 to 16   | Controls the smooth transition of change in audio level                          |
+--------------------+---------------+-----------+----------------------------------------------------------------------------------+
| Config             | NA            | NA        | Adjust the gain level of each parameter value of Balance and Fader configuration |
+--------------------+---------------+-----------+----------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                 | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=============================================================+========================+===============+
| Balance        | Balance of audio level between the left and right channels  | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| Fade           | Fade out of audio level between the front and rear channels | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| StepSize       | Allows smooth transition of change in audio level           | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| BFrontRight    | Balance Front Right channel coefficients                    | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| BFrontLeft     | Balance Front Left channel coefficients                     | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| BRearRight     | Balance Rear Right channel coefficients                     | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| BRearLeft      | Balance Rear Left channel coefficients                      | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| BCenter        | Balance Center channel coefficients                         | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| BSubWoofer     | Balance Subwoofer channel coefficients                      | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| FFrontRight    | Fader Front Right channel coefficients                      | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| FFrontLeft     | Fader Front Left channel coefficients                       | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| FRearRight     | Fader Rear Right channel coefficients                       | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| FRearLeft      | Fader Rear Left channel coefficients                        | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| FCenter        | Fader Center channel coefficients                           | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+
| FSubWoofer     | Fader Subwoofer channel coefficients                        | Float                  | NA            |
+----------------+-------------------------------------------------------------+------------------------+---------------+

| 

.. |balancefadergeneric.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/balancefadergeneric.png
.. |balanceconfig.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/balanceconfig.png
   :width: 300px
.. |faderconfig.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/mixersandsplitters/faderconfig.png
   :width: 300px
