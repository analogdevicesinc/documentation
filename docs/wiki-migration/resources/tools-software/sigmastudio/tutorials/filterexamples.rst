Filter Examples
===============

:doc:`Click here to return to the Tutorials section. </wiki-migration/resources/tools-software/sigmastudio/tutorials>`

Example 1
---------

A simple filter circuit:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/filterexamplespicture1.jpg
   :alt: filterexamplespicture1.jpg

with these parameters:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/filterexamplespicture2.jpg
   :alt: filterexamplespicture2.jpg

produces this filter frequency response:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/filterexamplespicture3.jpg
   :alt: filterexamplespicture3.jpg

Example 2
---------

This schematic shows a General Purpose (2nd-Order) as well as a Medium-Size EQ, each with a 1-Channel - Double-Precision algorithm grown by 2. The schematic includes an input block and terminals for completion of signal flow.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/filterexamplespicture4.jpg
   :alt: filterexamplespicture4.jpg

The configuration produces the following frequency responses, with the red line the General Purpose filter and the green line the Medium-Size EQ:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/filterexamplespicture5.jpg
   :alt: filterexamplespicture5.jpg

Example 3
---------

This schematic uses the General (2nd-Order / Lookup / Slew) block, a counter, an input and two output blocks.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/filterexamplespicture6.jpg
   :alt: filterexamplespicture6.jpg

A Butterworth lowpass filter with 4 curves is selected. For them the index range possible is 0 - 3, and curve 2 uses index 1.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/filterexamplespicture7.jpg
   :alt: filterexamplespicture7.jpg

Example 4
---------

This schematic uses the State-Variable block, with a Stimulus, Probe, input and three output blocks.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/filterexamplespicture8.jpg
   :alt: filterexamplespicture8.jpg

The frequency response produced, showing the three LP, HP, and BP filters, is:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/filterexamplespicture9.jpg
   :alt: filterexamplespicture9.jpg

Example 5
---------

This schematic uses the Text-In Filter (linked) and Text-In Filter (Unlinked) with probe and stimuli blocks. Linked has 1-ch - double-precision grown by 2, which behaves as a series filter, while Unlinked has 1-ch - double-precision added by 2, which behaves as a parallel filter. Tone (lookup/sine) is the input; T connection and terminals complete the signal flow.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/filterexamplespicture10.jpg
   :alt: filterexamplespicture10.jpg

The frequency response:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/filterexamplespicture11.jpg
   :alt: filterexamplespicture11.jpg
