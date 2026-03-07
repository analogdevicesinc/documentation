General (2nd-Order / Lookup)
============================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| ---------------------------------------------------------------------------------------------------------

|general2ndlookpic1.png| The General (2nd-Order / Lookup) block gives access to a wide variety of 2nd-order IIR (infinite impulse response) filter algorithms. See :doc:`General 2nd-Order Filters </wiki-migration/resources/tools-software/sigmastudio/toolbox/algorithminformation/general2ndorderfilters>` (in Algorithm Information) for details about the algorithms driving these blocks.

The filters available are:

-  Tone
-  Peaking
-  General LP/HP
-  Butterworth LP/HP
-  Bessel LP/HP
-  Chebyshev LP/HP

This block is implemented by a :ez:`double-precision <message/73876>` biquad filter that has multiple sets of coefficients in tables on the DSP. To select curves (lookup), use an :doc:`Index Lookup Table </wiki-migration/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/indexlookuptable>`, a :doc:`Counter </wiki-migration/resources/tools-software/sigmastudio/toolbox/counters/counter>` block, or a :doc:`DC Input block </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/dcinputentry>` in your design and connect it to the red pin. Using the GPIO blocks you could control the selected responses with a knob, rotary encoder or button.

**To open the Filter Control Window:**

Click the icon button:|general2ndlookpic2.png|. The curve is defined using the Tone Control window (shown below).

Enter the number of curves desired in the # Curves field. Enter Boosts, (overall) Gain, and Q in their fields. Enter the desired cutoff or center (peaking filters) frequency in the Frequency fields. Other parameters to enter will vary with filter type.

| The variety and range of filters are remarkable, as can be seen from the following examples:
| |general2ndlookpic3.png|
| |general2ndlookpic4.png|
| |general2ndlookpic5.png|
| |general2ndlookpic6.png|
| |general2ndlookpic7.png|

.. hint::

   Note: For n curves, the selected index should not exceed n - 1, i.e., the index range is 0 to n - 1. If you select an n th curve, misbehavior or errors may result.


.. |general2ndlookpic1.png| image:: https://wiki.analog.com/_media/general2ndlookpic1.png
.. |general2ndlookpic2.png| image:: https://wiki.analog.com/_media/general2ndlookpic2.png
.. |general2ndlookpic3.png| image:: https://wiki.analog.com/_media/general2ndlookpic3.png
.. |general2ndlookpic4.png| image:: https://wiki.analog.com/_media/general2ndlookpic4.png
.. |general2ndlookpic5.png| image:: https://wiki.analog.com/_media/general2ndlookpic5.png
.. |general2ndlookpic6.png| image:: https://wiki.analog.com/_media/general2ndlookpic6.png
.. |general2ndlookpic7.png| image:: https://wiki.analog.com/_media/general2ndlookpic7.png
