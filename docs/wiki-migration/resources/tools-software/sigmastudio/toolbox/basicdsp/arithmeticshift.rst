Shift
=====

:doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

The Shift block allows you to perform an arithmetic shift operation on the input data.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/shiftcell.png
   :alt: shiftcell.png

Click the image to switch between left shift or right shift. The shift value represents the number of bits to shift the incoming value.

If a shift results in an overflow the data will be saturated to the minimum negative or maximum positive value [-128.0, +127.9999].
