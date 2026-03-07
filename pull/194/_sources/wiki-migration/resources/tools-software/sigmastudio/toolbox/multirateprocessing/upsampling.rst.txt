Up Sampling
===========

| :doc:`Click here to return to the Multi-rate processing section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/multirateprocessing>`
| The Up sampling module is mainly used to get the input samples to a higher sampling rates after processing the audio at lower sampling rates.For example the bass of the audio can be processed at lower sampling rates and then taken to the higher sampling rates.
| |image1|

Input Pins
----------

+--------------+------------------------------------+--------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description           |
+==============+====================================+================================+
| Pin 0: Input | decimal- audio                     | Input Signal to be up-sampled. |
+--------------+------------------------------------+--------------------------------+

| 
| ===== Output Pins =====

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - audio                    Upsampled Output
============= ================================== ====================

| 
| ===== Grow Algorithm ===== The module can be grown upto 8 channels. All the input signals are upsampled by the same upsample rate.
| ===== Configurations ===== The upsample factor can be changed by combo box.

+------------------+---------------+--------------+-------------------------------------------------------------+
| GUI Control Name | Default Value | Range        | Function Description                                        |
+==================+===============+==============+=============================================================+
| Upsample Factor  | 2             | 2,3,4,6,8,16 | The factor at with the input sample rate will be multipiled |
+------------------+---------------+--------------+-------------------------------------------------------------+

The upsampler can either insert zeros or repeat the previous sample(Zero Order Hold) during upsampling. This can be configured in the contex menu.


|image2|

| Change in the 'Insertion Type' , 'Upsample Factor' or 'LPF' needs a recompilation of the schematic.
| =====DSP Parameter Information===== None
| ===== Supported ICs =====

-  ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multirateprocessing/upsampling4p6.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multirateprocessing/upsample.png
