Wav Player
==========

| :doc:`Click here to return to the Master Control Port section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/mastercontrolport>`
| \|\| This module can be used to read PCM/WAV files from external Flash connected to ADAU145x via SPI. This module also can perform pitch shifting while playing the file.
| |image1|
| The following list shows the various audio files supported by this module.

-  Audio Samples in 8.24 Fixed point format (Mono/Stereo)
-  Wav file with out header (PCM) (Mono/Stereo)

   -  8 Bits per Sample (Signed Integer)

      -  16 Bits per Sample (Signed Integer)

         -  24 Bits per Sample (Signed Integer)
         -  32 Bits per Sample (Signed Integer)

-  Wav file with Wav header(Mono/Stereo)

   -  16 Bits per Sample (Signed Integer)

      -  24 Bits per Sample (Signed Integer)

         -  32 Bits per Sample (Signed Integer)

| **Note:** 8 Bits per sample is not supported for Wav file.
| **Note:** Pitch shifting is not supported for stereo files.
| :doc:`Flash Programmer </wiki-migration/resources/tools-software/sigmastudio/toolbox/mastercontrolport/flashprogrammer>` can be used to write wav files to the SPI flash from ADAU145x.

Input Pins
----------

+---------------------+------------------------------------+--------------------------------------------------------------------------------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description                                                                       |
+=====================+====================================+============================================================================================+
| Pin 0: Trigger      | int- control                       | Rising edge in the input triggers the Wav File read from SPI flash.                        |
+---------------------+------------------------------------+--------------------------------------------------------------------------------------------+
| Pin 1: Wav Select   | int- control                       | Selects the wav file from the SPI flash. 0 -> first file, 1-> second file, etc.            |
+---------------------+------------------------------------+--------------------------------------------------------------------------------------------+
| Pin 2: Pitch factor | dec- control                       | Speed of the Wav player. This pin will be available only if the pitch shifting is enabled. |
+---------------------+------------------------------------+--------------------------------------------------------------------------------------------+

| 
| ===== Output Pins =====

+------------------+------------------------------------+--------------------------------------------------------------------------------------------------+
| Name             | Format [int/dec] - [control/audio] | Function Description                                                                             |
+==================+====================================+==================================================================================================+
| Pin 0: Left Out  | decimal - audio                    | Left Audio Sample                                                                                |
+------------------+------------------------------------+--------------------------------------------------------------------------------------------------+
| Pin 0: Right Out | decimal - audio                    | Right Audio Sample. This pin will be available only if the number of audio channels is set as 2. |
+------------------+------------------------------------+--------------------------------------------------------------------------------------------------+

| 

Grow Algorithm
--------------

| The module currently does not support grow/add functionality.
| ===== Configurations ===== Click on the image |image2| to configure the SPI interface for the module.

| |image3|
| ^GUI Control Name^Default Value^Range^Function Description^

+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Bit Rate                 | 100kHZ               | 100 kHZ - 100000 kHZ                                                  | SPI Speed                                                                                                           |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| SPI Slave Select         | 0                    | 0-6                                                                   | Slave Select for the SPI. Register window should be configured to match this selection.Please refer the note below. |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Sub-Address Bytes        | 2                    | 1-4                                                                   | Number of address bytes excluding the read/write command                                                            |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| SPI Mode                 | Mode 3               | Mode0/Mode3                                                           | SPI operation mode                                                                                                  |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| R/W (Chip Address) Bytes | 1                    | 0-255                                                                 | Command Bytes (Number of bytes required for command)                                                                |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Read Instruction (SPI)   | 0                    | 0-255                                                                 | Instruction value for a read operation (0x1 for ADI audio devices, typically 0x3 for eeprom/flash)                  |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Audio File Format        | Audio Sample in 8.24 | Wav without header (PCM)/ Wav with header/Audio Sample in 8.24 format | Selection of audio file format                                                                                      |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Number of Channels       | 2                    | 1/2                                                                   | Number of channels in the audio file stored in SPI flash.                                                           |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Bits Per Sample          | 16                   | 8/16/24/32                                                            | Bits per sample in the audio file stored in SPI flash.                                                              |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Number of Audio Files    | 1                    | 1-16                                                                  | Number of audio files written in the SPI flash.                                                                     |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Loopback                 | Disabled             | Enabled/Disabled                                                      | Enable/Disable loopback.                                                                                            |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Pitch Shifting           | Disabled             | Enabled/Disabled                                                      | Enable/Disable pitch shifting.                                                                                      |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Start Address1\*         | 0                    | 0 - 16777216 (16 MBytes)                                              | Start Address of Audio file 1 in the SPI flash. (in Bytes)                                                          |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Length1\*                | 192000               | 1 - 16777216 (16 MBytes)                                              | Length of Audio file 1 in the SPI flash. (in Bytes)                                                                 |
+--------------------------+----------------------+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

**Note:** Length and Start Address controls will be repeated for 'Number of Audio Files' times. Any change in these configuration parameters requires a recompilation.

**Note:** Please make sure that the Length is accurate in bytes. If Flash Programmer module is used to write the file to the SPI EEPROM, check the wav file size from the properties in windows and enter it into length field.

| |image4|
| ==== Support for Different Slave Select==== If the Slave Select is 0 and MP0 is used as chip select, no configuration is required in the register controls. Otherwise particular multipurpose pin should be configured to act as the slave select in the register window. (Hardware Configuration -> ICx - ADAU145x Register Controls -> MULTIPURPOSE/ AUXADC)

| |image5|
| \* Slave Select Channel -> 'Slave Select Channel x'

-  MPx pin mode -> 'Slave Select for Master SPI port'
-  MPx pin function -> 'Multipurpose function'

| 
| The following table shows the mapping between module's parameter and the register control window.

+----------------------------------------+------------------------------------------------+
| 'Slave Select' in Configuration Window | 'Slave Select Channel' in the Register control |
+========================================+================================================+
| 1                                      | Slave Select Channel 0                         |
+----------------------------------------+------------------------------------------------+
| 2                                      | Slave Select Channel 1                         |
+----------------------------------------+------------------------------------------------+
| 3                                      | Slave Select Channel 2                         |
+----------------------------------------+------------------------------------------------+
| 4                                      | Slave Select Channel 3                         |
+----------------------------------------+------------------------------------------------+
| 5                                      | Slave Select Channel 4                         |
+----------------------------------------+------------------------------------------------+
| 6                                      | Slave Select Channel 5                         |
+----------------------------------------+------------------------------------------------+

| 
| ====Support for Multiple Files==== Number of wav files can be configured in the 'Control Port Properties' window. Start Address and Length for each of the wav file should be configured in the 'Control Port Properties' window. |image6|
| Dynamically the wav file can be selected from the external pin. |image7|

Pitch Shifting
~~~~~~~~~~~~~~

Pitch shifting option can be enabled to control the speed of the Wav file playback.


|image8|

In the above example the pitch shifting factor/speed is set as 1.5 (Note that this should be in 8.24 fixed point format). So the file plays at the speed of 1.5. Assume the EEPROM/Flash contains the sine tone of 500 Hz. The playback will be sine tone of 750Hz (1.5 \* 500).

DSP Parameter Information
-------------------------

+------------------+-----------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name                                                                                                   | Function Description                                                                     |
+==================+=================================================================================================================+==========================================================================================+
| StartAddress1    | <fc #008000>WavPlayerAlg</fc><fc #ff0000>1</fc><fc #000080>sample</fc><fc #800000>1</fc><fc #000080>_start</fc> | Array of start addresses of Audio files in SPI flash                                     |
+------------------+-----------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Length1          | <fc #008000>WavPlayerAlg</fc><fc #ff0000>1</fc><fc #000080>sample</fc><fc #800000>1</fc><fc #000080>_end</fc>   | Array of end addresses of Audio files in SPI flash (Calculated as StartAddress + Length) |
+------------------+-----------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name
-  <fc #800000> Brown</fc> - File Number (Changes for each files)

Supported ICs
-------------

-  ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/wavplayer1.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/wavplayericon.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/wavplayerconfig.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/fileprop.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/mp5_slaveselect.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/wavplayer_4files.jpg
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/wavplayer_example.jpg
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/wavplayer_pitch.jpg
