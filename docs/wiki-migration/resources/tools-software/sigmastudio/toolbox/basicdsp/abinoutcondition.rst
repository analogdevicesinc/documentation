AB In/Out Condition
===================

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| -------------------------------------------------------------------------------

|abinoutpic1.png| The AB In / CD Out Condition block lets you compare the sample-by-sample level of two incoming signals (AB) and output the sample of the signal meeting the condition.

This algorithm works only for DSPs with a conditional instruction.

Click the blue icon in the block to select what condition you want to execute:

-  greater than
-  less than
-  greater than or equal to
-  less than or equal to.

When the condition is met, your output sample is A; otherwise it's B.

.. hint::

   Note that you will need to recompile your project every time you select a different condition.


For a sample design using this block, see the :doc:`Basic DSP </wiki-migration/resources/tools-software/sigmastudio/tutorials/basicdspexamples>` example.

.. |abinoutpic1.png| image:: https://wiki.analog.com/_media/abinoutpic1.png
