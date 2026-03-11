Audio Signal Router Index Selectable
====================================

:doc:`Click here to return to the Mixers/Splitters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/mixerssplitters>`

|image1| Audio Signal router mixes M different inputs to N different outputs with various gains. The number of input and output pins are configurable.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/audiosignalrouterindxgrow.png
   :align: center

Configuration
-------------

This module supports multiple mixer configurations. Each mixer configuration has gains for all the inputs and outputs. A separate gain is available for each of input output combination also. All the gains has a corresponding mute control to quickly mute the particular gain. The current mixer (Mix #) can be changed during the runtime.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/audiosignalrouterform.png
   :align: center

The following equations show the calculation of the output for given sample mixer table.

=== ===== ===== =====
\         Out0  Out1
\         *Og0* *Og1*
In0 *Ig0* G00   G01
In1 *Ig1* G10   G11
=== ===== ===== =====

-  Out0 = *Og0* \* ( G00 \* *Ig0* \* In0 + G10 \* *Ig1* \* In1)
-  Out1 = *Og1* \* ( G01 \* *Ig0* \* In0 + G11 \* *Ig1* \* In1)

If the input/output channels are more than 17, then the mixer window is split for 17 input/output channels to improve GUI performance.


|image2|

Labels for each of the input/output channels can be edited. This updated channel name will pear on the each of the Pin's tooltip as show below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/channel_customization2.jpg
   :align: center

DSP Parameter Information
-------------------------

=============== ==============================================
Compiler Name   Function Description
=============== ==============================================
InputGain_t_i   Gain for the Mix t and Input i.
OutputGain_t_j  Gain for the Mix t and Output j.
CrossGain_t_j_i CrossGain for the Mix t, Output j and Input i.
TabIndex        Current Mix to apply
=============== ==============================================

**Note:**\ Here t,i and j starts from 0. All the parameter names are appended with the algorithm name (e.g.)AudioSignalRouterIndxSel32S300Alg1InputGain_0_0

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/audiosignalrouterindx.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/audio_router_morethan17.png
