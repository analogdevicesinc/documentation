Text-In Eq Slew -(ADAU145x)
===========================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |image1|

| An alternative to the :doc:`General (2nd Order)Slew </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/generaleq2ndorderslew>` filter, the Text-In block lets you set parameters using text fields, without having to open another window. The algorithms are the same, giving access to the wide variety of 2nd-order-filter behaviors, although not all the algorithms are offered with Text-In.
| The slewing functionality is added for smooth transition from one set of filter coefficients to another when the filter parameters are changed. The slewing takes place approximately in the time set by the user in the GUI. The slew time can be entered in the GUI slew Text box. The slew time range is limited between (0 to 1 second).The slew computation is always performed in single precision.
| See the\ :doc:`General (2nd Order)Slew </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/generaleq2ndorderslew>` page for information about the algorithms driving these blocks. The available filters are:

-  Parametric Filter
-  Shelving EQ: Low-Shelf
-  Shelving EQ: High-Shelf
-  General: Lowpass Filter
-  General: Highpass Filter
-  Peaking EQ
-  Notch EQ
-  General: Bandpass Filter
-  General: Bandstop Filter
-  Allpass filter

To use this block:

-  Drag into the workspace, right-click the block and select **Add Algorithm > IC N**.
-  Select your desired algorithm:

   -  Double-Precision
   -  Single-Precision

-  Click the blue icon to choose your filter: Peak, Lowpass, Highpass, Low-Shelf, High-Shelf.
-  Enter values in the param tab for Boost (Peak and Shelf EQ), Freq, Q/Slope. Click the right arrow and the gain tab and enter the filter gain.

   -  Boost is the amount of boost / cut applied to the designated frequency range
   -  Freq is the center frequency
   -  Q/slope is the sharpness of the curve
   -  Gain is the overall gain of filter.
   -  Slew(s) field sets the slew time(seconds) for slewing of filter coefficients when a filter parameter is changed. The slew computation is in single precision and implements RC slewing. The slew time can be set between 0-1 second.

| 
| As with other blocks, there's the option :doc:`Grow </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/algorithms>` this algorithm. Observe that with this block, growing the algorithm adds another frequency band to the block, which is equivalent to having two filters in series.

**NOTE: Due to fixed point operations, the filter coefficients do not slew exactly in the set slew time.**

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/txt-ineqslew1.png
   :width: 150px
