:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gain>`

ADI Surround
============

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/adialgorithms/adisurround.png
   :alt: adisurround.png

Description
-----------

| ADI Surround uses matrix-surround decoding techniques: deriving five channels of output from a two-channel input. This process entails using a sum channel (the combination of the left and right channels, L+R), which contains frontal information, and a difference channel (the difference between the left and right channels, L-R / R-L), which contains ambiance information. Depending on the blending and distribution of the difference channel with the sum channel, we can derive the left, right, center, and side or rear surround channels. The L and R front speakers carry music, frontal sound effects, and directional dialog; the center speaker carries the rest (meaning most) of the dialog, and the surround speakers (ideally placed to the side of and slightly above the listeners) provide ambiance and surround effects
| ===== Usage ===== ADI Surround has presets for the following modes:

::

   *Club 
   *Music
   *Stadium
   *Cinema
   *Hall
   *Rock
   *Jazz
   *User1
   *User2
   *User3

It also features two room sizes:

::

   *Small 
   *Large

These Large and Small settings are to make it sound like a small or large room. This is a setting that can be experimented with to adjust for the room the system is in and personal preference. So there is no “correct” setting for this

Targets Supported
-----------------

+--------------------+------------+------------------+---------------+------------------+
| Name               | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+====================+============+==================+===============+==================+
| ADI Surround Sound | NA         | NA               | S             | NA               |
+--------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

======= ===== ===============
Name    Type  Description
======= ===== ===============
Input 0 Audio Input channel 0
Input 1 Audio Input channel 1
======= ===== ===============

Output
~~~~~~

======= ===== =================================
Name    Type  Description
======= ===== =================================
Output0 Audio Output channel for left side
Output1 Audio Output channel for Center
Output2 Audio Output channel for Right side
Output3 Audio Output channel for Left surround
Output4 Audio Output channel for Right surround
======= ===== =================================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+---------------+----------------------------------+
| GUI Parameter Name | Default Value | Range         | Function Description             |
+====================+===============+===============+==================================+
| Mode               | Club          | NA            | 10 modes as mentioned in usage   |
+--------------------+---------------+---------------+----------------------------------+
| RoomSize           | Small         | Small / Large | Depends on the size of the rooms |
+--------------------+---------------+---------------+----------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-------------------------------------------+------------------------+---------------+
| Parameter Name | Description                               | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+===========================================+========================+===============+
| dil            | Scales the Surround sound parameters      | NA                     | Integer32     |
+----------------+-------------------------------------------+------------------------+---------------+
| gain1          | Scales the Surround sound gain parameters | NA                     | FixPoint8d24  |
+----------------+-------------------------------------------+------------------------+---------------+
| gain2          | Scales the Surround sound gain parameters | NA                     | FixPoint8d24  |
+----------------+-------------------------------------------+------------------------+---------------+
| gain3          | Scales the Surround sound gain parameters | NA                     | FixPoint8d24  |
+----------------+-------------------------------------------+------------------------+---------------+
| gain4          | Scales the Surround sound gain parameters | NA                     | FixPoint8d24  |
+----------------+-------------------------------------------+------------------------+---------------+
