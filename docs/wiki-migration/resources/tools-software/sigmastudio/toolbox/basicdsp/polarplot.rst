Polar Plot
==========

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| |polar_plot.png|
| |polar_plotgraph.png|

Description
-----------

| The polar plot module displays the input signal coefficient in a polar plot
| ===== Usage ===== Polar plot is a plot of magnitude versus phase angle in complex plane . (i.e. locus of magnitude traced by the phasor by varying frequency from zero to infinity). The polar plot can capture the system behavior over the entire frequency range in a single plot

Targets Supported
-----------------

========= ========== ================ =============
Name      ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x
========= ========== ================ =============
PolarPlot NA         Block            NA
========= ========== ================ =============

| 
| ===== Pins =====

Input
~~~~~

=============== ===== =============
Name            Type  Description
=============== ===== =============
Address Pointer Audio Input Address
=============== ===== =============

| 
| ===== Configurable Parameters =====

+--------------------------+---------------+------------+-------------------------------------------------+
| GUI Parameter Name       | Default Value | Range      | Function Description                            |
+==========================+===============+============+=================================================+
| Angle division in degree | 30            | 1 to 360   | Sets the angle divisions in the graph           |
+--------------------------+---------------+------------+-------------------------------------------------+
| UpperLimits              | 0             | -120 to 0  | Sets the upper graph limit                      |
+--------------------------+---------------+------------+-------------------------------------------------+
| LowerLimits              | -90           | -121 to 0  | Sets the lower graph limit                      |
+--------------------------+---------------+------------+-------------------------------------------------+
| NumberOfDivisions        | 3             | 1 to 10    | Sets the graph divisions                        |
+--------------------------+---------------+------------+-------------------------------------------------+
| Show Magnitude Labels    | True          | True/False | Enable or disable the magnitude labels          |
+--------------------------+---------------+------------+-------------------------------------------------+
| RefreshTime(ms)          | 100           | 10 to 5000 | Graph refresh/update interval                   |
+--------------------------+---------------+------------+-------------------------------------------------+
| TotalNumberOfPoints      | 64            | 16 to 256  | Number of points to read from the given address |
+--------------------------+---------------+------------+-------------------------------------------------+
| Read                     | Off           | On/Off     | Enable/Disable the read                         |
+--------------------------+---------------+------------+-------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+----------------------------------+------------------------+---------------+
| Parameter Name | Description                      | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+==================================+========================+===============+
| Value          | Read back value from the address | Float                  | NA            |
+----------------+----------------------------------+------------------------+---------------+

| 

.. |polar_plot.png| image:: https://wiki.analog.com/_media/polar_plot.png
.. |polar_plotgraph.png| image:: https://wiki.analog.com/_media/polar_plotgraph.png
