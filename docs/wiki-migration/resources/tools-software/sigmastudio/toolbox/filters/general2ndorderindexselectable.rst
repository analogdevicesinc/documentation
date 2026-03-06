General (2nd-Order / Index Selectable) Graphical
================================================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| The General (2nd-Order / Index Selectable) block provides a wide variety of 2nd-order filter algorithms. This block extends the functionality of the General (2nd-Order / Lookup) filter with an enhanced graphical filter design tool. In addition, each of this filter's response curves can be designed independently, allowing you to use complex filter configurations to match your desired system response.

This filter provides:

-  Selection from a set of filter responses via external control input pin.
-  Graphical design of filter response curves.
-  Independent filter type and settings for each response curve.
-  Loading of filter coefficients from a text file containing the same.

| This block is implemented as a biquad filter that has multiple sets of coefficients stored in tables on the DSP. See :doc:`General 2nd-Order Filters </wiki-migration/resources/tools-software/sigmastudio/toolbox/algorithminformation/general2ndorderfilters>` (in Algorithm Information) for details about the biquad filter design techniques used for this block.
|

.. important::

   As of SigmaStudio 4.5, Index Selectable Filters are not working on ADAU1701 or ADAU1401. The block is tested and working for ADAU176x, ADAU144x, ADAU145x, and ADAU146x.


.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/general2ndindexpic2.jpg
   :align: center

Input Pins
----------

+----------------------------+------------------------------------+------------------------------------------------+
| Name                       | Format [int/dec] - [control/audio] | Function Description                           |
+============================+====================================+================================================+
| Pin 0: Input               | decimal - audio                    | Input to the filter                            |
+----------------------------+------------------------------------+------------------------------------------------+
| Pin 1: Filter Select Index | decimal - audio                    | Index of the selected frequency response curve |
+----------------------------+------------------------------------+------------------------------------------------+

Output Pins
-----------

============= ================================== ====================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== ====================
Pin 0: Output decimal - audio                    The filtered output
============= ================================== ====================

| NOTE: The selection input should be a 28.0 format integer value between 0 and the number of curves. For example if your filter has 6 curves, the selection input value should be a 28.0 integer value from 0 to 5.
| |image1|

Configuration
-------------

| To open the Filter Control Window, Click the icon button:|general2ndindexpic4.png|
| |image2|
| ^GUI Control Name^Default Value^Range^Function Description^

+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| icon button                    | -          | -             | Opens the Filter Control Window                                                                                                                                                                                                                                                                                                                                                                                                              |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Select Filter by Filter Number | 0          | 0-99          | Selects a filter response curve by filter number selected                                                                                                                                                                                                                                                                                                                                                                                    |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Frequency                      | 100Hz      | 0-96KHz       | Set the cutoff frequency of the filter                                                                                                                                                                                                                                                                                                                                                                                                       |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Boost                          | 10         | -150 to 30dB  | Set the boost value for a particular filter curve                                                                                                                                                                                                                                                                                                                                                                                            |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Q factor                       | 1.41       | 0.05 to 15    | Set the Q factor                                                                                                                                                                                                                                                                                                                                                                                                                             |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ripple                         | 0.1        | 0.1 to 5      | Set the Ripple factor for particular filter type(this control is not enabled for all filter types)                                                                                                                                                                                                                                                                                                                                           |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Gain                           | 6          | -96dB to 10dB | Set the Gain for a particular filter response curve.                                                                                                                                                                                                                                                                                                                                                                                         |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Graph                          | -          | -             | The filter response curves in the graph can be dragged to suitably change the filter characteristics                                                                                                                                                                                                                                                                                                                                         |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Filter Type                    | Peaking(0) | 0-13          | Select the type of filter                                                                                                                                                                                                                                                                                                                                                                                                                    |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Filter Sub-type                | 0          | 0-4           | The “Sub Type” section is only available for the First Order filter type. In first order mode, you have the flexibility of choosing between two cascaded first order filters in a configuration of Low - Low, Low - High, High - Low, or High - High combinations. The “Active 1” and “Active 2” check boxes also apply to First Order filters only, and allow you to independently enable or disable either of the two first order filters. |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Load All                       | -          | -             | The ISF form also has a load all button. On clicking the Load all button the filter types of all added filters is changed to IIR Coefficient and enables loading of filter coefficient for all filters from a single text file containing the coefficients for all filters.                                                                                                                                                                  |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Opacity                        | -          | -             | The "Opacity" control sets the transparency value of the control window                                                                                                                                                                                                                                                                                                                                                                      |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Slew                           | 12         | 0-46/ 0-100   | ADAU144x/ADAU176x supports upto 46 slew points.The "Slew Points" control sets how many transition points the algorithm uses to transition from one selected filter curve to another, increasing the number of points will provide smoother transitions                                                                                                                                                                                       |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Bypass                         | 0          | 0 or 1        | The "Bypass" check box disables the filter when checked                                                                                                                                                                                                                                                                                                                                                                                      |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| View                           | -          | -             | The "View" section only applies for the First Order filter type, this tool allows you to manage each first order filter and control its settings graphically. Refer to the Example for more details                                                                                                                                                                                                                                          |
+--------------------------------+------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. important::

   The shelving filters' "Q factor" parameter actually controls the Slope parameter, not Q. See `Audio EQ Cookbook <https://www.w3.org/TR/audio-eq-cookbook/>`__ for the relationship between shelf slope S and Q factor. When this parameter is 1, it produces the steepest shelving filter with monotonic gain.


| You can add additional filter curves by clicking the **Add Filter** button. To remove a filter, select the filter in the graph or clicking its index in the Filter column and press the **Remove Filter** button.
| Coefficients can be loaded for all added filters using the load all button which opens the choose file dialogue where the file containing all coefficients can be loaded as shown in the figure. Coefficients file is expected as a text file containing the biquad coefficients in the following order.

-  B0
-  B1
-  B2
-  A1
-  A2

| 
| |image3|

| 
| When the filter type chosen is IIR, coefficients for that particular filter can be chosen by clicking the load button which opens a choose file dialogue where the file containing all coefficients can be loaded as shown in the figure.
| |image4|

DSP Parameter Information
-------------------------

| 
| ^GUI Control Name^Compiler Name^Function Description^

== == =========================================================
B2 B2 Bi-quad coefficient of the selected filter response curve
B1 B1 Bi-quad coefficient of the selected filter response curve
B0 B0 Bi-quad coefficient of the selected filter response curve
A2 A2 Bi-quad coefficient of the selected filter response curve
A1 A1 Bi-quad coefficient of the selected filter response curve
== == =========================================================

| 
| =====Example=====
| |general2ndindexpic9.png|

| In this example, ISF1 and ISF2 are the names of the two consecutive blocks on Figure c. Both blocks contain four filters, and are set to the "zeroth" index filter, curve 0, selected by the DC input in "28.0" format. (Other formats cannot be used for selection). The ISF1 window is shown below. The cascaded Transfer Function is represented at the bottom. A different filter response curve can be selected by changing the value of the DC input block to corresponding filter index.
| |general2ndindexpic10.png|
| Using cascaded Index Selectable Filters (ISF) as in the above example, it is possible to simulate complex responses like the Fletcher & Manson psychoacoustic contours of loudness.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/general2ndindexpic3.png
.. |general2ndindexpic4.png| image:: https://wiki.analog.com/_media/general2ndindexpic4.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/isfloadiir1.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/isfloadiir2.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/isfloadiir3.png
.. |general2ndindexpic9.png| image:: https://wiki.analog.com/_media/general2ndindexpic9.png
.. |general2ndindexpic10.png| image:: https://wiki.analog.com/_media/general2ndindexpic10.png
