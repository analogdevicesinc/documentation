General (1st-Order)
===================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| -----------------------------------------------------------------------------------------------------

|general1stpic1.png| The General 1st-Order block allows you to design 1st-order lowpass and highpass filters.

Drag the block into the workspace and it's ready to use. As with other blocks, there's the option to :doc:`Grow </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/algorithms>` or :doc:`Add </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/algorithms>` to this algorithm. Observe, however, that with this block **growing** the algorithm will add another frequency band to the block, which is equivalent to having two filters in series. Adding an algorithm adds another input/output pair to the block, which is equivalent to **adding** a filter in parallel.

To switch among highpass, lowpass, and flat, click the blue frequency response icon. This can be done in real time, without needing to recompile the project. Enter your desired values in the text fields to set the cutoff frequency and overall gain (sometimes called scale gain) of the filter. Or click the arrows to increment values for these parameters. To increment them very quickly, click and hold, dragging a little.

To view your work, drag a filter block into the workspace, a Simulation Stimulus block as input, a Simulation Probe to come after the filter, set some test parameters, and click Probe, then Stimulus. To see some results, take a look at the filter examples.

Calculating Filter Coefficients
-------------------------------

Use the following formulas to calculate the coefficients for first order filters.

Variables:

-  frequency = Cutoff frequency
-  gain = Linear Gain
-  fs = Sample Rate
-  PI = π

For lowpass filters,

-  A1 = 2.7^(-2 \* PI \* frequency/fs))
-  B0 = gain \* (1.0 - A1)
-  B1 = 0

For highpass filters,

-  A1 = e^(-2 \* PI \* frequency/fs)) where e = 2.718.....
-  B1 = (1.0 + A1) \* 0.5 \* gain
-  B0 = -B1

For allpass filters,

-  A1 = 2.7^(-2 \* PI \* frequency/fs))
-  B0 = -gain \* A1
-  B1 = gain

.. |general1stpic1.png| image:: https://wiki.analog.com/_media/general1stpic1.png
