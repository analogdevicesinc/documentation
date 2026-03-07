ADI Surround
============

:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

ADI Surround uses matrix-surround decoding techniques: deriving five channels of output from a two-channel input. This process entails using a sum channel (the combination of the left and right channels, L+R), which contains frontal information, and a difference channel (the difference between the left and right channels, L-R / R-L), which contains ambiance information.

Depending on the blending and distribution of the difference channel with the sum channel, we can derive the left, right, center, and side or rear surround channels. The L and R front speakers carry music, frontal sound effects, and directional dialog; the center speaker carries the rest (meaning most) of the dialog, and the surround speakers (ideally placed to the side of and slightly above the listeners) provide ambiance and surround effects.

ADI Surround has presets for the following modes:

-  Club
-  Music
-  Stadium
-  Cinema
-  Hall
-  Rock
-  Jazz
-  User1
-  User2
-  User3

It also features two room sizes:

-  Size1 = small
-  Size2 = large

These Large and Small settings are to make it sound like a small or large room. This is a setting that can be experimented with to adjust for the room the system is in and personal preference. So there is no "correct" setting for this.

The schematic shown below features an input block (two-channel), ADI Surround (configuration = Club, size = small) and output blocks.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/licensedalgorithms/adi_surround_020.jpg
   :align: center
