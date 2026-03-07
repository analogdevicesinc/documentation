Medium Size EQ Slew Ext-(ADAU145x)
==================================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |image1|
| This block gives access to two general 2nd-order filters: Peaking and Shelving EQ. The algorithms driving this block are the same as for the other 2nd-order filters, but it simply offers an alternate layout and control of parameters that may prove more useful for your application.
| The slewing functionality is added for smooth transition from one set of filter coefficients to another when the filter parameters are changed. The slewing takes place approximately in the slew time set by the user. The slew time can be set by providing the value :math:`\lambda` to the control pin. The parameter :math:`\lambda` determines the slew rate. Upon growing the number of filter stages, a new control pin is added to the module for :math:`\lambda` value for each stage. The slew computation is always performed in single precision.

As can be seen from the figure at right, the block controls frequency, gain, and filter type.

For information on this block's algorithms,see :doc:`General (2nd Order)Slew Ext </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/generaleq2ndorderslewext>` Algorithms.

To use this block:

-  Drag it into the workspace, right-click it and select Add Algorithm > IC N.
-  Choose which algorithm meets your needs.
-  Click the blue icon to choose which filter you want to implement: Peak or High- / Low-Shelf.
-  Double-click right in the middle of the block to bring up the EQ parameter window:
-  Select from the dropdown menu which of the two types of filters you want and enter the parameters desired. Peaking is the default.

After choosing the filter type, right-click the block to either Grow or Add to it. Growing adds another frequency band to the block, equivalent to having two individual filters in series, while adding an algorithm adds another input/output pair, equivalent to adding a filter in parallel.

| 
| |medpic3.png| **Peaking EQ** Peaking boosts or cuts a designated center frequency.

*Gain:* This field sets the overall gain (scale gain) of the filter. Edit your desired value (+/-15) in the upper-right Gain field or click the arrows.

*Boost / cut level:* Control the level of the filtered portion of the response with the slider.

*Frequency:* Enter the desired peak or dip center frequency in the lower-left field, or click the slider's < > arrows. (Hold or try to drag them for faster change.)

| *Q:* Set the Q you want (max 51) by entering a value in the field, clicking its arrows, or using the concentric knobs, where the outer one controls the integer value and the inner one the decimal value. Q governs the narrowness of the filter, being the ratio of the center frequency to the half-power points (-3dB) on either side. The higher the Q the faster the transition between passband and stopband.
| This is a quick and versatile block, as can be seen by comparing the below curves with their settings. It is highly useful for developing an educated ear.
| |medpic4.png|

| Negative gain and shallow Q (above) produce this:
| |medpic5.png|

| while positive gain and narrower Q (same scale gain and same frequency; below),
| |medpic6.png|

| quickly produce this:
| |medpic7.png|
| |medpic8.png| *Shelving EQ:* Low / High Shelf

Shelving evenly boosts or cuts all frequencies either above (= High Shelf, ) or below (= Low Shelf,) the cutoff frequency.

The other parameters:
---------------------

*Cutoff frequency*: Enter the cutoff frequency in the field below the slider, or click its arrows. (Hold and attempt to drag the < > for rapid incrementation.) This frequency is the cutoff point between the shelf boost/cut and the unaffected (flat) response.

*Gain (filter*): Control the filter boost or cut with the slider. Negative values give a cut for all frequencies above (High Shelf) or below (Low Shelf) the cutoff, while positive values give a boost for all frequencies above (High Shelf) or below (Low Shelf) the cutoff.

*Slope (Q):* Edit the slope of the filter with the control knob, 0 - 2. Right-click it to enter more-precise values. Slope controls filter steepness and therefore the transition between the boost/cut and the flat response.

| *Scale Gain (dB):* This value controls the overall gain of the filter. Enter it in the field or click the arrows at right.

| Handy for ear training, this is a quick and versatile block, as can be seen by comparing the below curves with their parameters.
| |medpic9.png|
| |medpic10.png|

As with Peaking, Shelving parameters may be changed handily and the results immediately checked for audible effect.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mideqslewext1.png
   :width: 100px
.. |medpic3.png| image:: https://wiki.analog.com/_media/medpic3.png
.. |medpic4.png| image:: https://wiki.analog.com/_media/medpic4.png
.. |medpic5.png| image:: https://wiki.analog.com/_media/medpic5.png
.. |medpic6.png| image:: https://wiki.analog.com/_media/medpic6.png
.. |medpic7.png| image:: https://wiki.analog.com/_media/medpic7.png
.. |medpic8.png| image:: https://wiki.analog.com/_media/medpic8.png
.. |medpic9.png| image:: https://wiki.analog.com/_media/medpic9.png
.. |medpic10.png| image:: https://wiki.analog.com/_media/medpic10.png
