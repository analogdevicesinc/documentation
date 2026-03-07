White Noise Source
==================

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

+-------------------------------------------------------------------------------------------------------------------------+---------------------+
| The White Noise cell generates a signal that contains equal energy per frequency division (hertz or similar increment). | |whitenoise001.jpg| |
+-------------------------------------------------------------------------------------------------------------------------+---------------------+

| 
| This random time-varying signal can be useful for testing equipment, although for audio situations white noise is commonly run through a pinking filter, to better simulate the behavior and response of the human ear.
| A simple on/off toggle (right) controls the cell output.
| You can add algorithms to the White Noise cell after the default has been established (if you're using more than one DSP board, you'll need to add the initial default algorithm for the desired board). Right-click the cell to select Add Algorithm > IC N > White Noise and add another output pin.
| To change the source's Sampling Rate, Right-click in the block and select Set Sampling Rate, which will open the Sampling Rate window (default is 44.1 kHz).

.. |whitenoise001.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/whitenoise001.jpg
