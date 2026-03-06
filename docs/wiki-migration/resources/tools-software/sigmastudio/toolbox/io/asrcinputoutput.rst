ASRC Input/Output
=================

:doc:`Click here to return to the Inputs and Outputs Toolbox page. </wiki-migration/resources/tools-software/sigmastudio/toolbox/io>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/asrc_input_output_020.jpg
   :align: right

The ASRC Input and Output blocks route signals between the schematic design and the hardwares ASRCs (Asynchronous Sample Rate Converters).

Use the input block's check boxes to enable or disable particular inputs. Use the output block's drop-down list control to select from the available ASRCs.

-  Every ASRC Output must have its input connected, else there will be errors on compilation.
-  Observe that as you drag more ASRC output blocks into the schematic, the number of available outputs in the drop-down decreases because they can only be represented by one block at a time.
-  To change the ASRC input's Sampling Rate , Right-click the block name and select Set Sampling Rate, which brings up the Sampling Rate window (default is 44.1 kHz).

.. note::

   These blocks are only available for use with DSPs that have integrated ASRCs.

