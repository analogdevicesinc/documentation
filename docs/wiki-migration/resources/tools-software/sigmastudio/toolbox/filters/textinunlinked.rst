Text-In (unlinked)
==================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |textinpic1.png| An alternative to the :doc:`General-Purpose </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/general2ndorder>` filter, the Text-In block lets you set parameters using text fields, without having to open another window. The algorithms are the same, giving access to the wide variety of 2nd-order-filter behaviors, although not all the algorithms are offered with Text-In.

See the :doc:`General 2nd Order Algorithms </wiki-migration/resources/tools-software/sigmastudio/toolbox/algorithminformation/general2ndorderfilters>` page for information about the algorithms driving these blocks. The available filters are:

-  Peaking EQ
-  Shelving EQ: Low-/High-Shelf
-  General: Low-/Highpass Filter

To use this block:

-  Drag into the workspace, right-click the block and select **Add Algorithm > IC N**.
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
-  Enter values in the param tab for Boost (Peak and Shelf EQ), Freq, Q/Slope. Click the right arrow and the gain tab and enter the filter gain.

   -  Boost is the amount of boost / cut applied to the designated frequency range
   -  Freq is the center frequency
   -  Q/slope is the sharpness of the curve
   -  Gain is the overall gain of filter.

As with other blocks, there's the option to either :doc:`Grow </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/algorithms>` or :doc:`Add </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/algorithms>` to this algorithm. Observe that with this block, growing the algorithm adds another frequency band to the block, which is equivalent to having two filters in series. Adding an algorithm adds another input/output pair to the block, which is equivalent to adding a filter in parallel.

The behavior of this block in terms of growing and adding algorithms is like the other filter blocks. A special version of this filter, the `Text-In (linked) <https://wiki.analog.com/resources/tools-software/sigmastudio/toolbox/textinlinked>`__ (which see), forces added algorithms to share the same parameters, and grown algorithms must add a corresponding parallel algorithm. In other words, it allows simultaneous control of added algorithms, and when you grow upon an added algorithm, a corresponding parallel filter will be added to match any previously added algorithm.

.. |textinpic1.png| image:: https://wiki.analog.com/_media/textinpic1.png
