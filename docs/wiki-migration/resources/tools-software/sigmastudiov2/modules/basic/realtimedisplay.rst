:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Real-Time Display
=================

| 
| |rtd.png|
| |rtdgraph.png|

Description
-----------

| The Real-Time Display block lets allow us read the data from the target and display it in the graph.
| ===== Usage ===== Click on the "Graph" icon to open the real-time display graph window. 'Start' button allows to read the data from the target for specified time of 'Time Span' and 'Stop' allows us to to stop readback from the target. 'Continous Read' allows us to read the data from the target irrespective of 'Time Span'. 'Reset' resets the graph and Format allows us to specify the format of reading data.
| ===== Targets Supported =====

+-------------------+------------+------------------+---------------+------------------+
| Name              | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===================+============+==================+===============+==================+
| Real Time Display | B/S        | B/S              | S             | B                |
+-------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

===== ===== ===============
Name  Type  Description
===== ===== ===============
Input Audio Input Channel 0
===== ===== ===============

Output
~~~~~~

====== ===== ================
Name   Type  Description
====== ===== ================
Output Audio Output channel 0
====== ===== ================

| 
| ===== Configurable Parameters =====

+---------------+---------------+------------------+---------------------------------------------------------+
| GUI Parameter | Default Value | Range            | Function Description                                    |
+===============+===============+==================+=========================================================+
| Y-Max/Y-Min   | 1             | -20,000 to 20000 | Displays the input signal in the specified y-axis scale |
+---------------+---------------+------------------+---------------------------------------------------------+
| Multiplier    | 1             | 1 to 100         | multiplies the input signal by this value               |
+---------------+---------------+------------------+---------------------------------------------------------+
| TimeSpan      | 1             | 1 to 20          | x-axis scale- upper limit on the display                |
+---------------+---------------+------------------+---------------------------------------------------------+

DSP Parameters
--------------

+----------------+--------------------------------+------------------------+----------------+
| Parameter Name | Description                    | ADSP-214xx/SC5xx/215xx | ADAU145x/146x  |
+================+================================+========================+================+
| ReadData       | Contains the input signal data | Float                  | FixedPoint8d24 |
+----------------+--------------------------------+------------------------+----------------+

| 

.. |rtd.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/rtd.png
.. |rtdgraph.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/rtdgraph.png
