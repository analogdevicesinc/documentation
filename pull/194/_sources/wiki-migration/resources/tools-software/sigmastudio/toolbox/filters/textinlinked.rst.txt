Text-In (Linked)
================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |textinlinkedpic1.png| An alternative to the :doc:`General-Purpose </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/general2ndorder>` filter, the Text-In block lets you set parameters using text fields, without having to open another window. The algorithms are the same, giving access to the wide variety of 2nd-order-filter behaviors, although not all the algorithms are offered with Text-In.

The Text-In (linked) filter differs from the unlinked version in that (1) it allows simultaneous control of added algorithms and (2) when you grow upon an added algorithm, a corresponding parallel filter will be added to match the previously added algorithm.

At right is an example of a default algorithm of 1ch - Double Precision grown by 1, with an added 2ch - Double Precision. The parameters are the same in the vertical settings because of the linked nature of this block; see below for more about that.

See :doc:`General 2nd-Order Algorithms </wiki-migration/resources/tools-software/sigmastudio/toolbox/algorithminformation/general2ndorderfilters>` for information about the algorithms driving these blocks. The available filters are: Peaking EQ Shelving EQ: Low-/High-Shelf General: Low-/Highpass

To use this block:

-  Drag into the workspace, right-click the block and select Add Algorithm > IC N.
-  Select your desired algorithm:

   -  1-channel - Double-Precision
   -  1-channel - Single-Precision
   -  2-channel - Double-Precision
   -  2-channel - Single-Precision
   -  3-channel - Double-Precision
   -  3-channel - Single-Precision
   -  4-channel - Single-Precision
   -  4-channel - Double-Precision
   -  5-channel - Double-Precision
   -  5-channel - Single-Precision
   -  6-channel - Double-Precision
   -  6-channel - Single-Precision

-  Click the blue icon to choose your filter: Peak, Lowpass, Highpass, Low-Shelf, High-Shelf.
-  Use the < / > arrows to select gain, with the Gain text field, or param, clicking which displays the text fields Boost (Peak and Shelf EQ only), Freq, Q/Slope:

   -  Boost is the amount of boost or cut applied to the designated frequency range
   -  Freq is the center frequency
   -  Q/slope is the sharpness of the curve
   -  Gain is the overall gain of filter.

As with other blocks, there's the option to either Grow or Add to this algorithm. Observe that with this block, **growing** the algorithm adds another frequency band to the block, which is equivalent to having two filters in series. **Adding** an algorithm adds another input/output pair to the block, which is equivalent to adding a filter in parallel.

Since this is a linked block, changing the values in one parameter box after you add an algorithm automatically updates the other filter in parallel. Better yet, after adding an algorithm, if you grow it the series filter automatically adds parallel filters to match the previous case. The same is true when you add onto a grown algorithm: the parallel filter will automatically add series filters to match.

.. |textinlinkedpic1.png| image:: https://wiki.analog.com/_media/textinlinkedpic1.png
