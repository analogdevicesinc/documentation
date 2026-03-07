General-Purpose Input
=====================

:doc:`Click here to return to the Inputs and Outputs Toolbox page. </wiki-migration/resources/tools-software/sigmastudio/toolbox/io>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/gpio_intput_016.jpg
   :align: right

The General Purpose Input block allows signals from the hardware's GPIO input pins to be used in a schematic design. The orange output pin should typically be connected to a GPIO Conditioning block.

There are 12 selectable inputs to this GPIO block.

.. note::

   Note: The block is only available for DSPs that include GPIO. To configure the hardware's GPIO input and outputs settings, see the processors Register Control Window.


Select the channel desired for sending your signal using the General Purpose Input drop-down control.

-  Every enabled input must be connected to an output, else there will be errors on compilation.
-  Observe that as you drag more output blocks to your schematic, your number of input channels available in the drop-down decreases.
-  To change the Sampling Rate for the Input, Right-click the block name and select Set Sampling Rate, which brings up the Sampling Rate window (default is 44.1 kHz):

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/gpio_intput_017.jpg
   :align: center
