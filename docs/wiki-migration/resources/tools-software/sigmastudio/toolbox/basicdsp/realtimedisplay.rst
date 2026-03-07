| :doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| ====== Real-Time Display ======
| |image1|
| |image2|

Description
===========

| The Real-Time Display block lets allow us read the data from the target and display it in the graph.
| ===== Usage ===== Click on the "Graph" icon to open the real-time display graph window. 'Start' button allows to read the data from the target for specified time of 'Time Span' and 'Stop' allows us to to stop readback from the target. 'Continous Read' allows us to read the data from the target irrespective of 'Time Span'. 'Reset' resets the graph and Format allows us to specify the format of reading data.
| ===== Targets Supported =====

================= =============== ================ =============
Name              ADSP-214xx      ADSP-215xx/SC5xx ADAU145x/146x
================= =============== ================ =============
Real Time Display Block/Schematic Block/Schematic  Schematic
================= =============== ================ =============

| 
| ===== Pins =====

Input
-----

===== ===== ===============
Name  Type  Description
===== ===== ===============
Input Audio Input Channel 0
===== ===== ===============

Output
------

====== ===== ================
Name   Type  Description
====== ===== ================
Output Audio Output channel 0
====== ===== ================

| 
| ===== Configurable Parameters =====

+---------------+---------------+-------------------------+---------------------------------------------------------+
| GUI Parameter | Default Value | Range                   | Function Description                                    |
+===============+===============+=========================+=========================================================+
| Y-Max/Y-Min   | 1             | -134999999 to 134999999 | Displays the input signal in the specified y-axis scale |
+---------------+---------------+-------------------------+---------------------------------------------------------+
| Multiplier    | 1             | 1 to 100                | multiplies the input signal by this value               |
+---------------+---------------+-------------------------+---------------------------------------------------------+
| TimeSpan      | 1             | 1 to 20                 | x-axis scale- upper limit on the display                |
+---------------+---------------+-------------------------+---------------------------------------------------------+

DSP Parameters
==============

+----------------+--------------------------------+------------------------+----------------+
| Parameter Name | Description                    | ADSP-214xx/SC5xx/215xx | ADAU145x/146x  |
+================+================================+========================+================+
| ReadData       | Contains the input signal data | Float                  | FixedPoint8d24 |
+----------------+--------------------------------+------------------------+----------------+

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/realtimedisplay.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/real_graph.png
