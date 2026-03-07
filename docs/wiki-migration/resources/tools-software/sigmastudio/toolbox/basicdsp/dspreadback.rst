DSP Readback
============

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| -------------------------------------------------------------------------------------------------------

|dspreadbackpic1.png| The DSP Readback block lets you read values back from the DSP at any point in your schematic design.

The number displayed onscreen is the data value sent back from the DSP considering all the blocks to the left of the Readback block. Every time you click Read, this value will be updated with the latest from the DSP. By displaying the output value from any block, in any format desired, Readback is used extensively for debugging. Readbacks can also be used to hold values for a microcontroller to access over the control port.

Values can be read back in either hex or decimal. For the latter, you must specify what format you want the number to be displayed in.

-  The default for 1st generation SigmaDSPs (including AD1940, AD1941, ADAU1701, ADAU1702, ADAU1401) is 5.19: 5 bits for the integer, 19 for the decimal. Any changes to this format will shift the decimal value of the number displayed.
-  Second-generation SigmaDSPs like the ADAU1761, ADAU1781, and ADAU1442 are able to read back in full 28-bit (5.23) accuracy.
-  Third-generation SigmaDSPs, such as ADAU1452, ADAU1466, and ADAU1467 are able to read back in full 32-bit (8.24) accuracy.

See :doc:`here for more information about the numeric formats </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/numericformats>` used in SigmaDSP.

.. important::

   First-generation SigmaDSP processors, such as ADAU1701, do not read back with 28-bit accuracy. They only support 24-bit data, so small 28.0 format integers will be truncated and display as 0.000000000. To display 28.0 format integers on these DSPs, the value from Readback must be bit shifted, such as multiplying the value by 4 twice (since 16.0 does not exist in 5.23 format) and setting the DSP Readback to 24.0 format.


For a sample design using this block, see the :doc:`Basic DSP </wiki-migration/resources/tools-software/sigmastudio/tutorials/basicdspexamples>` example.

For some examples of using this cell to check the peak or RMS level of a signal, please see this EngineerZone forum FAQ: :ez:`Monitoring average and instantaneous signal levels <message/7669>`

Configuring Continuous Readback
-------------------------------

The DSP Readback cell can be configured to read back from the target DSP repeatedly at regular intervals. To enable this mode, right-click the cell and select **Start Continuous Read**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/dspreadbackstartcontinuousread.jpg
   :align: center

You can also click the small circle in the cell to enable or disable Continuous Read mode. When the circle is blue, Continuous Read mode is active. When the circle is orange, Continuous Read mode is inactive.

|image1|\ |image2|

When Continuous Read mode is active, you can change the update rate by right-clicking on the cell and selecting from a list of options. Selecting a slower update rate will allow you to have more readback cells operating at the same time, and will lower the chances of a buffer underrun error on the USB interface.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/dspreadbackreadtiming.jpg
   :align: center

Accessing Readback Values from a Microcontroller
================================================

The following assumes you have a working microcontroller platform, with SigmaDSP interface code based on :doc:`Interfacing SigmaDSP Processors with a Microcontroller </wiki-migration/resources/tools-software/sigmastudio/tutorials/microcontroller>`.

.. tip::

   It is always recommended to access block parameter addresses from the \*PARAMS.h file exported by SigmaStudio. This ensures that as your SigmaStudio project evolves the system controller is always accessing the proper device registers.


The Readback block has a single read-only address which holds the value from the input pin. The value is updated with each audio sample. You can read the value and decode to float:

.. code:: cpp

   double readback_val = SIGMA_READ_REGISTER_FLOAT(MOD_READBACK1_READBACKALGNEWSIGMA3001VALUE_ADDR);

Retain the integer representation:

.. code:: cpp

   int32_t readback_val = SIGMA_READ_REGISTER_INTEGER(MOD_READBACK1_READBACKALGNEWSIGMA3001VALUE_ADDR, 4);

Or simply print the value to the serial port; great for debugging.

.. code:: cpp

   SIGMA_PRINT_REGISTER(MOD_READBACK1_READBACKALGNEWSIGMA3001VALUE_ADDR, 4);

Example output: ``VALUE AT 0x35: 0x01 00 00 00``

.. |dspreadbackpic1.png| image:: https://wiki.analog.com/_media/dspreadbackpic1.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/continuousreadactive.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/continuousreadinactive.jpg
