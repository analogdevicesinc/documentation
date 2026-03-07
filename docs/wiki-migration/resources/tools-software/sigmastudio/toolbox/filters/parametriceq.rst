Parametric EQ
=============

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| |parametricpic1.png| The Parametric EQ block extends the functionality of the General (2nd-Order) filter with an enhanced graphical filter design tool. In addition, multiple 2-nd order filter stages can be cascaded to create complex filter responses.

This filter provides:

-  Graphical design of filter response curves.
-  High order filtering, via cascaded 2nd order filters (maximum of 15)
-  Independent filter type and settings for each filter stage.

| This block is implemented using cascaded biquad filters. See :doc:`General 2nd-Order Filters </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/general2ndorder>` (in :doc:`Algorithm Information </wiki-migration/resources/tools-software/sigmastudio/toolbox>`) for details about the biquad filter design techniques used by this block.

.. important::

   The shelving filters' "Q factor" parameter actually controls the Slope parameter, not Q. See `Audio EQ Cookbook <https://www.w3.org/TR/audio-eq-cookbook/>`_ for the relationship between shelf slope S and Q factor. When this parameter is 1, it produces the steepest shelving filter with monotonic gain.


Tree Toolbox Path
-----------------

| Filter->Miscellaneous->Parametric EQ
| |parametricpic7.png|

Filter Control Window:
----------------------

The window will initially show a single filter control, as depicted in the figure below.

| **To open the Filter Control Window, Click the icon button:** |parametricpic2.png|
| |parametricpic3.png|

To add additional filter stages, click the **Add Filter** button. Up to a maximum of 15 filters can be cascaded. To remove a filter, select the filter in the graph or by clicking its index in the Filter column and press the **Remove Filter** button.

Controls:
---------

Each filter's response can be independently adjusted using the graph controls or spin control at the bottom.

-  To change a filter's characteristics, like **"Frequency"** or **"Boost"**, just click on the colored circle on filter graph, and drag to the desirable position. If preferred, any of the parameters can be changed directly from the spin controls.

.. image:: https://wiki.analog.com/_media/parametricpic4.png
   :alt: parametricpic4.png
   :align: center

-  To change the **"Q"** factor using the graph, click on the horizontal line control above the colored circle, and drag it left or right, adjusting the filter's width.

.. image:: https://wiki.analog.com/_media/parametricpic5.png
   :alt: parametricpic5.png
   :align: center

-  In the **"Type"** column, choose between Low-Pass, High-Pass, Peaking, Tone, IIR, and First Order filters.

.. image:: https://wiki.analog.com/_media/parametricpic6.png
   :alt: parametricpic6.png
   :align: center

-  The **"Sub Type"** section is only available for the First Order filter type. In first order mode, you have the flexibility of choosing between two cascaded first order filters in a configuration of Low - Low, Low - High, High - Low, or High - High combinations. The "Active 1" and "Active 2" check boxes also apply to First Order filters only, and allow you to independently enable or disable either of the two first order filters.

-  The **"View"** section only applies for the First Order filter type, this tool allows you to manage each first order filter and control its settings graphically. Refer to the Example for more details.

-  The **"Bypass"** check box disables the filter when checked.

-  The plot view can be modified by changing the **Frequency** and **Magnitude** settings. These settings apply to the interface only and do not affect filter response.

.. |parametricpic1.png| image:: https://wiki.analog.com/_media/parametricpic1.png
.. |parametricpic7.png| image:: https://wiki.analog.com/_media/parametricpic7.png
.. |parametricpic2.png| image:: https://wiki.analog.com/_media/parametricpic2.png
.. |parametricpic3.png| image:: https://wiki.analog.com/_media/parametricpic3.png
