Down Sampling
=============

| :doc:`Click here to return to the Multi-rate processing section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/multirateprocessing>`
| The down sampling module is mainly used to get the input samples to a lower sampling rate and process. For example the bass portion of the audio need not be processed at higher sampling rates as the frequencies associated with bass are low.

| This module takes the downsample factor from the GUI parameters and down sample the input accordingly.
| |image1|
| ===== Input Pins =====

+--------------+------------------------------------+----------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description             |
+==============+====================================+==================================+
| Pin 0: Input | decimal- audio                     | Input Signal to be down-sampled. |
+--------------+------------------------------------+----------------------------------+

Output Pins
-----------

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - audio                    Downsampled Output
============= ================================== ====================

Grow Algorithm
--------------

| The module can be grown upto 8 channels. All the input signals are downsampled by the same downsample rate.
| ===== Configurations ===== The downsample factor can be changed by combo box.

+-------------------+---------------+--------------+----------------------------------------------------------+
| GUI Control Name  | Default Value | Range        | Function Description                                     |
+===================+===============+==============+==========================================================+
| Downsample Factor | 2             | 2,3,4,6,8,16 | The factor at with the input sample rate will be divided |
+-------------------+---------------+--------------+----------------------------------------------------------+

| Change in GUI configuration needs a recompilation of the schematic.
| =====DSP Parameter Information===== None
| ===== Supported ICs =====

-  ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/multirateprocessing/downsamping4p6.png
