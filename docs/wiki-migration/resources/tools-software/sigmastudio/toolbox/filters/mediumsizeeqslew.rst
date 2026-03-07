Medium Size EQ Slew-(ADAU145x)
==============================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |image1|
| This block gives access to two general 2nd-order filters: Peaking and Shelving EQ. The algorithms driving this block are the same as for the other 2nd-order filters, but it simply offers an alternate layout and control of parameters that may prove more useful for your application.
| The slewing functionality is added for smooth transition from one set of filter coefficients to another when the filter parameters are changed. The slewing takes place approximately in the time set by the user in the GUI. The slew time can be entered in the GUI slew Text box, or open the EQ Settings window by clicking on the icon button and enter the slew time in the slew text box or by using the slew slider. The slew time range is limited between (0 to 1 second).

As can be seen from the figure at right, the block controls frequency, gain, slew and filter type.

For information on this block's algorithms, see General 2nd-Order Algorithms.

To use this block:

-  Drag it into the workspace, right-click it and select Add Algorithm > IC N.
-  Choose which algorithm meets your needs.
-  Click the blue icon to choose which filter you want to implement: Peak or High- / Low-Shelf.
-  Select from the dropdown menu which of the two types of filters you want and enter the parameters desired. Peaking is the default.

After choosing the filter type, right-click the block to either Grow or Add to it. Growing adds another frequency band to the block, equivalent to having two individual filters in series, while adding an algorithm adds another input/output pair, equivalent to adding a filter in parallel.

| 
| |image2|

**Peaking EQ** Peaking boosts or cuts a designated center frequency.

*Gain:* This field sets the overall gain (scale gain) of the filter. Edit your desired value (+/-15) in the upper-right Gain field or click the arrows.

*Boost / cut level:* Control the level of the filtered portion of the response with the slider.

*Frequency:* Enter the desired peak or dip center frequency in the lower-left field, or click the slider's < > arrows. (Hold or try to drag them for faster change.)

*Q:* Set the Q you want (max 51) by entering a value in the field, clicking its arrows, or using the concentric knobs, where the outer one controls the integer value and the inner one the decimal value. Q governs the narrowness of the filter, being the ratio of the center frequency to the half-power points (-3dB) on either side. The higher the Q the faster the transition between passband and stopband.

| *Slew(s):*\ This field sets the slew time(seconds) for slewing of filter coefficients when a filter parameter is changed. The slew computation is in single precision and implements RC slewing. The slew time can be set between 0-1 second.
| This is a quick and versatile block, as can be seen by comparing the below curves with their settings. It is highly useful for developing an educated ear.
| |image3|

| Negative gain and shallow Q (above) produce this:
| |medpic5.png|

| while positive gain and narrower Q (same scale gain and same frequency; below),
| |image4|

| quickly produce this:
| |medpic7.png|

| |image5|
| *Shelving EQ:* Low / High Shelf

Shelving evenly boosts or cuts all frequencies either above (= High Shelf, ) or below (= Low Shelf,) the cutoff frequency.

The other parameters:
---------------------

*Cutoff frequency*: Enter the cutoff frequency in the field below the slider, or click its arrows. (Hold and attempt to drag the < > for rapid incrementation.) This frequency is the cutoff point between the shelf boost/cut and the unaffected (flat) response.

*Gain (filter*): Control the filter boost or cut with the slider. Negative values give a cut for all frequencies above (High Shelf) or below (Low Shelf) the cutoff, while positive values give a boost for all frequencies above (High Shelf) or below (Low Shelf) the cutoff.

*Slope (Q):* Edit the slope of the filter with the control knob, 0 - 2. Right-click it to enter more-precise values. Slope controls filter steepness and therefore the transition between the boost/cut and the flat response.

*Scale Gain (dB):* This value controls the overall gain of the filter. Enter it in the field or click the arrows at right.

| *Slew(s):*\ This field sets the slew time(seconds) for slewing of filter coefficients when a filter parameter is changed. The slew computation is in single precision and implements RC slewing. The slew time can be set between 0-1 second.

| Handy for ear training, this is a quick and versatile block, as can be seen by comparing the below curves with their parameters.
| |image6| |image7|
| |image8| |image9|

| 
| As with Peaking, Shelving parameters may be changed handily and the results immediately checked for audible effect.
| **NOTE: Due to fixed point operations, the filter coefficients do not slew exactly in the set slew time.**

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mideqslew1.png
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mideqslew2.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mideqslew4.png
   :width: 200px
.. |medpic5.png| image:: https://wiki.analog.com/_media/medpic5.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mideqslew5.png
   :width: 200px
.. |medpic7.png| image:: https://wiki.analog.com/_media/medpic7.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mideqslew6.png
   :width: 200px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mideqslew7.png
   :width: 200px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mideqslew11.png
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mideqslew8.png
   :width: 200px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/mideqslew10.png
   :width: 300px
