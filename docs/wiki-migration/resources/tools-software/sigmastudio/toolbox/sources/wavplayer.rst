Wav Player
==========

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

This module can be used to read PCM/WAV files from internal memory of ADAU145x. This module also provides playback controls as Play/Pause, Stop and Loopback.This module also can perform pitch shifting while playing the file.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/wavplayercell.jpg
   :align: center

The following list shows the various audio files supported by this module.

-  Audio Samples in 8.24 Fixed point format (Mono)
-  Wav file with out header (PCM) (Mono)

   -  8 Bits per Sample (Signed Integer)

      -  16 Bits per Sample (Signed Integer)

         -  24 Bits per Sample (Signed Integer)
         -  32 Bits per Sample (Signed Integer)

Output Pins
-----------

+-------------------------+------------------------------------+----------------------+
| Name                    | Format [int/dec] - [control/audio] | Function Description |
+=========================+====================================+======================+
| Pin 0: WavPlayer OutPut | decimal - audio                    | Audio Sample         |
+-------------------------+------------------------------------+----------------------+

| 
| ===== Grow Algorithm ===== The module currently does not support grow/add functionality.

Configurations
--------------

Click on the image |image1| to open the Wav Player Properties Window.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/wavplayerpropertieswndw.jpg
   :align: center

+-------------------+----------------------+------------------------------------------------------+-----------------------------------------+
| GUI Control Name  | Default Value        | Range                                                | Function Description                    |
+===================+======================+======================================================+=========================================+
| Audio File Format | Audio Sample in 8.24 | Wav without header (PCM)/Audio Sample in 8.24 format | Selection of audio file format          |
+-------------------+----------------------+------------------------------------------------------+-----------------------------------------+
| Bits Per Sample   | 32                   | 8/16/24/32                                           | Bits per sample in the audio file Load. |
+-------------------+----------------------+------------------------------------------------------+-----------------------------------------+
| Sample to Start   | 0                    | 0 - number of samples in file                        | To allow phase shift.                   |
+-------------------+----------------------+------------------------------------------------------+-----------------------------------------+
| File Type         | ASCII                | ASCII/Binary                                         | To select text file or PCM file.        |
+-------------------+----------------------+------------------------------------------------------+-----------------------------------------+

**Note:** The size of the file shall not exceed the (Maximum DM0 Memory(20kb) - Available DM0 Memory).

Any change in these configuration parameters requires a recompilation.

DSP Parameter Information
-------------------------

+---------------------+---------------------------------------------+----------------------------+
| GUI Control Name    | Compiler Name                               | Function Description       |
+=====================+=============================================+============================+
| ForwardPlay         | WavPlayerInternalAlg1ForwardPlay            | To Play or Pause the Audio |
+---------------------+---------------------------------------------+----------------------------+
| Loopback            | WavPlayerInternalAlg1Loopback               | To Enable/Disable Loopback |
+---------------------+---------------------------------------------+----------------------------+
| PitchScalingFactor  | WavPlayerInternalAlg1PitchScalingFactor_Hi  | To provide pitch shifting  |
+---------------------+---------------------------------------------+----------------------------+
| PitchScalingFactor  | WavPlayerInternalAlg1PitchScalingFactor_Lo  | To provide pitch shifting  |
+---------------------+---------------------------------------------+----------------------------+
| PitchScalingCounter | WavPlayerInternalAlg1PitchScalingCounter_Hi | To provide phase shift     |
+---------------------+---------------------------------------------+----------------------------+
| PitchScalingCounter | WavPlayerInternalAlg1PitchScalingCounter_Lo | To provide phase shift     |
+---------------------+---------------------------------------------+----------------------------+

| 
| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name

Supported ICs
-------------

-  ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/wavplayericon.jpg
