General (2nd-Order w/ Param / Lookup / Slew)
============================================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| ----------------------------------------------------------------------------------------------------

|general2ndparampic1.png| The General (2nd-Order / Lookup) block gives access to a wide variety of 2nd-order IIR (infinite impulse response) filter algorithms. See General 2nd-Order Filters (in Algorithm Information) for details about the algorithms driving these blocks.

The filters available are: Tone Peaking General LP/HP Butterworth LP/HP Bessel LP/HP Chebyshev LP/HP

The block is simply a :ez:`double-precision <message/73876>` biquad filter that has stored a set of coefficients in tables in the DSP. To select curves (lookup), use an :doc:`Index Lookup Table </wiki-migration/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/indexlookuptable>`, a :doc:`Counter </wiki-migration/resources/tools-software/sigmastudio/toolbox/counters/counter>` block, or a :doc:`DC Input </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/dcinputentry>` block in your design and connect it to the red pin. Using the GPIO blocks you could control the selected responses with a knob, rotary encoder or button.

**To open the Filter Control Window:**

Click the icon button:|general2ndparampic2.png|. The curve is defined using the Tone Control window (shown below).

Enter the number of curves desired in the # Curves field. Enter Boosts, (overall) Gain, and Q in their fields. Enter the desired cutoff or center (peaking filters) frequency in the Frequency fields. Other parameters to enter will vary with filter type.

| The variety and range of filters are remarkable, as can be seen from the many examples in the :doc:`General (2nd-Order / Lookup) </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/general2ndorderlookup>` topic page. Below is one:
| |general2ndparampic3.png|
| For more details see the Example illustrating usage of this block.

The chief difference between the :doc:`General (2nd-Order / Lookup) </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/general2ndorderlookup>` block and this Slew version may be observed when the index changes (red pin) to select a new curve. The transition from previous curve to next curve is smooth, without any occasional zipping or clicking sounds, the reason being that the Slew version takes more memory space. As the designer, you will want to match your hardware appropriately. Consider the General (1st-Order w/ Param / Lookup / Slew) if system resources are scarce.

.. hint::

   Note: For n curves, the selected index shouldn't exceed n - 1, i.e., the index range is 0 to n - 1. If you select an n th curve, misbehavior or errors may result.


.. |general2ndparampic1.png| image:: https://wiki.analog.com/_media/general2ndparampic1.png
.. |general2ndparampic2.png| image:: https://wiki.analog.com/_media/general2ndparampic2.png
.. |general2ndparampic3.png| image:: https://wiki.analog.com/_media/general2ndparampic3.png
