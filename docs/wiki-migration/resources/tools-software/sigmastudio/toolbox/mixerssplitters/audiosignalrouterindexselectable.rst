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

==================== ===== ===================== =====================
\                          <fc #0000FF>Out0</fc> <fc #0000FF>Out1</fc>
\                          *Og0*                 *Og1*
<fc #008000>In0</fc> *Ig0* G00                   G01
<fc #008000>In1</fc> *Ig1* G10                   G11
==================== ===== ===================== =====================

-  <fc #0000FF>Out0</fc> = *Og0* \* ( G00 \* *Ig0* \* <fc #008000>In0</fc> + G10 \* *Ig1* \* <fc #008000>In1</fc>)
-  <fc #0000FF>Out1</fc> = *Og1* \* ( G01 \* *Ig0* \* <fc #008000>In0</fc> + G11 \* *Ig1* \* <fc #008000>In1</fc>)

If the input/output channels are more than 17, then the mixer window is split for 17 input/output channels to improve GUI performance.


|image2|

Labels for each of the input/output channels can be edited. This updated channel name will pear on the each of the Pin's tooltip as show below.

| |image3|
| =====DSP Parameter Information=====

+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Compiler Name                                                         | Function Description                                                                              |
+=======================================================================+===================================================================================================+
| InputGain\_<fc #FF0000>t</fc>\_<fc #008000>i</fc>                     | Gain for the Mix <fc #FF0000>t</fc> and Input <fc #008000>i</fc>.                                 |
+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| OutputGain\_<fc #FF0000>t</fc>\_<fc #0000FF>j</fc>                    | Gain for the Mix <fc #FF0000>t</fc> and Output <fc #0000FF>j</fc>.                                |
+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| CrossGain\_<fc #FF0000>t</fc>\_<fc #0000FF>j</fc>\_<fc #008000>i</fc> | CrossGain for the Mix <fc #FF0000>t</fc>, Output <fc #0000FF>j</fc> and Input <fc #008000>i</fc>. |
+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| TabIndex                                                              | Current Mix to apply                                                                              |
+-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

| **Note:**\ Here <fc #FF0000>t</fc>,<fc #008000>i</fc> and <fc #0000FF>j</fc> starts from 0.
| All the parameter names are appended with the algorithm name (e.g.)<fc #c0c0c0>AudioSignalRouterIndxSel32S300Alg1</fc>InputGain_0_0

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/audiosignalrouterindx.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/audio_router_morethan17.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mixerssplitters/channel_customization2.jpg
