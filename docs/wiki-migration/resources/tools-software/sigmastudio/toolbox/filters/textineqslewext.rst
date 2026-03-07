Text-In Eq Slew Ext-(ADAU145x)
==============================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |image1|

| An alternative to the :doc:`General (2nd Order)Slew Ext </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/generaleq2ndorderslewext>` filter, the Text-In block lets you set parameters using text fields, without having to open another window. The algorithms are the same, giving access to the wide variety of 2nd-order-filter behaviors, although not all the algorithms are offered with Text-In.
| The slewing functionality is added for smooth transition from one set of filter coefficients to another when the filter parameters are changed. The slewing takes place approximately in the slew time set by the user. The slew time can be set by providing the value :math:`\lambda` to the control pin. The parameter :math:`\lambda` determines the slew rate. Upon growing the number of filter stages, a new control pin is added to the module for :math:`\lambda` value for each stage. The slew computation is always performed in single precision.
| See the :doc:`General (2nd Order)Slew Ext </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/generaleq2ndorderslewext>` page for information about the algorithms driving these blocks. The available filters are:

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

| 
| As with other blocks, there's the option :doc:`Grow </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/algorithms>` this algorithm. Observe that with this block, growing the algorithm adds another frequency band to the block, which is equivalent to having two filters in series.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/txt-ineqslewext.png
   :width: 100px
