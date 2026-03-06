General 1st Order w/ param / lookup / Slew
==========================================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| -----------------------------------------------------------------------------------------------------

|firstorderwparampic1.png| The General (1st-Order / Lookup) block provides a selectable set of High-pass or Low-pass 1st-order filter responses with smooth (slew) transitions when selecting among responses.

The block allows you to define a set of filter responses (low or high pass) which be selected through the external control input in the end system. The number of selectable responses or curves is variable as is the slew rate or step which controls how quickly the filter response changes.

The filter's response is displayed in the Filter Control window (see below). Note that the response curves are linearly spaced between the low and high cutoff frequency values.

This block's algorithm stores a set of filter coefficients in a table on the DSP. To select a curve, use the Index Lookup Table, the Counter block, or the DC Input block and connect to the red pin. Using the GPIO blocks you could control the selected responses with a knob, rotary encoder or button.

**To open the Filter Control Window:**

Click the icon button:.\


|firstorderwparampic2.png|

-  Enter the number of curves desired in the # Curves field.
-  Enter desired filter Gain (-/+ dB).
-  Enter the desired frequency range for the curves (low and high frequency targets)

| |firstorderwparampic3.png|
| **Slew:** The transition between two curves (selected by the red control input pin) is smooth, without any clicking sounds or instabilities because the hardware/software Slew is used to transition between one filter response and another. Essentially one filter is cross-faded into the next. Note: Using Slew requires double the memory space of non-slew filters.

.. |firstorderwparampic1.png| image:: https://wiki.analog.com/_media/firstorderwparampic1.png
.. |firstorderwparampic2.png| image:: https://wiki.analog.com/_media/firstorderwparampic2.png
.. |firstorderwparampic3.png| image:: https://wiki.analog.com/_media/firstorderwparampic3.png
