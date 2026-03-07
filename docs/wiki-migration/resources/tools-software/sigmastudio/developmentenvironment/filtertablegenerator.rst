Filter Table Generator
======================

| :doc:`Click Here to return to the Dialogs page </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/dialogs>`
| The Filter Table Generator dialog is used to calculate filter coefficients and coefficient tables. Go to Tools - Fixed-Point Filter Table Generator... in the main application menu to access this dialog.
| |filtertablepic1.png|
| To use the generator, select a filter type tab on the left, set the filter design parameters and press the **Generate** button.
| The table generator provides a variety of design option including filter type, center frequency, Q, gain and number of table steps. A graph of the filter frequency response is displayed as well as a list of filter coefficients, in both decimal and hex (parameter RAM-ready hexadecimal) format. The hex values are sign-extended from the fourth bit. To see the coefficient values in decimal format check the **Show Values** box in the **Value Table** tab and press the **Generate** button.
| This tool is most useful for designing a set of filter coefficients with stepped gain response (as in the above image) for such applications as an graphic equalizer.

.. |filtertablepic1.png| image:: https://wiki.analog.com/_media/filtertablepic1.png
