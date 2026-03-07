:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gain>`

Surround Sound Volume Control
=============================

| 
| |surroundvol.png|
| |surroundsoundcartesian.png| |surroundsoundpolar.png|
| |setpositionswindow.png|

Description
-----------

The Surround Sound Volume Control block enables positioning of source elements relative to a listener head. The default block has one source centered in front of the listener. Right-click the block border or title to grow the algorithm up to 6 sources. Sources and head can be dragged to any position in the room, or set more precisely via the Set Positions and Room Dimensions form (right-click the center of the block). Its parameters include:

-  Units -- English (US) or Metric
-  Coordinate System -- Cartesian or Polar
-  Width and length of the room
-  Head location
-  Source locations

| 
| Press Resize to accept changes. Grayed-out source locations mean the source is not currently added.

Targets Supported
-----------------

+-------------------------------+------------+------------------+---------------+------------------+
| Name                          | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===============================+============+==================+===============+==================+
| Surround Sound Volume Control | NA         | B                | NA            | B                |
+-------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

======================== ===== ===============
Name                     Type  Description
======================== ===== ===============
Input <fc #ff0000>X</fc> Audio Input channel X
======================== ===== ===============

Output
~~~~~~

========================= ===== ================
Name                      Type  Description
========================= ===== ================
Output <fc #ff0000>X</fc> Audio Output channel X
========================= ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                               | Function Description                                                              |
+====================+===============+=====================================+===================================================================================+
| HeadGain           | -32dB         | 0 to -32dB                          | Scales the input signal by the specified gain                                     |
+--------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+
| Units              | US-Feet       | US-Feet, Metric                     | Switches between the units                                                        |
+--------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+
| CoordinateSystem   | Cartesian     | Cartesian, Polar                    | Switches between the coordinate systems                                           |
+--------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+
| HeadLocationX      | 0             | Depends on coordinate system, units | X-Coordinate of the head knob on the chart                                        |
+--------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+
| HeadLocationY      | 0             | Depends on coordinate system, units | Y-Coordinate of the head knob on the chart                                        |
+--------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+
| SourceLocationX    | -0.88         | Depends on coordinate system, units | X-Coordinates of the output speakers on the chart                                 |
+--------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+
| SourceLocationY    | 0.88          | Depends on coordinate system, units | Y-Coordinates of the output speakers on the chart                                 |
+--------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+
| RoomLength         | 5             | 0.01 - 30                           | Length of the room(chart length on the module)                                    |
+--------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+
| RoomWidth          | 5             | 0.01 - 30                           | Width of the room(chart width on the module)                                      |
+--------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+
| NumChannels        | 1             | 6                                   | Number of input and output channels. Change in this value requires re-compilation |
+--------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-----------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                   | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+===============================================+========================+===============+
| Gain           | Scales the input signal by the specified gain | Float                  | NA            |
+----------------+-----------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== Cartesian:
| distance= Math.Sqrt(Math.Pow(sourceX - \_headLocationX, 2) + Math.Pow(sourceY - \_headLocationY, 2));
| Polar:
| headXCart = \_headLocationX \* Math.Sin(\_headLocationY);
| headYCart = \_headLocationX \* Math.Cos(\_headLocationY);

| sourceXCart = sourceX \* Math.Sin(sourceY);
| sourceYCart = sourceX \* Math.Cos(sourceY);
| distance = Math.Sqrt(Math.Pow(sourceXCart - headXCart, 2) + Math.Pow(sourceYCart - headYCart, 2));

| US-Feet:
| if (distance <= 2) then, computedGain = \_globalGain + 6 - 10 \* Math.Log10((distance + 2) / 2);
| if (distance > 2) then, computedGain = \_globalGain + 8.989 - 20 \* Math.Log10((distance + 2) / 2);
| Metric:

| 
| Gain(Linear) = 10^(Gain(dB)/20)

.. |surroundvol.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/surroundvol.png
.. |surroundsoundcartesian.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/surroundsoundcartesian.png
.. |surroundsoundpolar.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/surroundsoundpolar.png
.. |setpositionswindow.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/setpositionswindow.png
