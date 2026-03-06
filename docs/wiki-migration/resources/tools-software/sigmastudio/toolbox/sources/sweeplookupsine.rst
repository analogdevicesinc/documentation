Sweep (Lookup/Sine)
===================

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

+---+---+
| The Sweep (Lookup/Sine) block generates a sinewave that sweeps from a start to an end frequency. The sweep speed is determined by the number of steps and cycles per step. | |image2| |
+---+---+

Enter the desired start and stop frequency and step size using the edit controls:

-  **Initial Freq**

   -  The frequency at which to begin the sweep.

-  **Ending Freq**

   -  The frequency at which to end the sweep.

-  **Step**

   -  Determines the number of steps in the sweep.

-  **Reset**

   -  Resets the current sweep frequency to the "Initial Freq".

-  **Sweep**

   -  Starts the frequency sweep.

-  **Speed**

   -  Sets the sweep speed, the relative duration of each sweep step.

A valid slope range will be computed depending on the step size entered. The ending tone will be held until reset is clicked, which returns to the initial frequency. The plot below shows the correlation for sweep plots with varying step sizes and slopes.

| 
| |image3|

Example
-------

This sample schematic uses the Sweep (Lookup/Sine), General (1st-Order) and an Output block to show how the Sweep block can be utilized with a filter.

| 
| |image4|
| This setup can be used in conjunction with a spectrum analyzer to determine the response of a particular filter or algorithm.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/sweeplookupsine007.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/sweeplookupsine007.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/sweeplookupsine008.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/sweeplookupsine009.jpg
