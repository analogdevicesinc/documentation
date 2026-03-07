Inputs And Outputs
==================

| :doc:`Click here to return to the Toolbox page </wiki-migration/resources/tools-software/sigmastudio/toolbox>`
| The toolbox's I/O library gives you access to the input/output blocks essential for bringing the signal from the hardware IC's physical input connections, into the schematic design, and back out to the hardware's output connections. The available input and output blocks will depend on the particular processor used in your design.

-  :doc:`ASRC Input/Output </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/asrcinputoutput>`
-  :doc:`ASRC Input with Gain </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/asrcinputwithgain>`
-  :doc:`Aux ADC Input </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/auxadcinput>`
-  :doc:`General-Purpose Input </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/generalpurposeinput>`
-  :doc:`General-Purpose Output </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/generalpurposeoutput>`
-  :doc:`Input </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/input>`
-  :doc:`Interface Read </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/interfaceread>`
-  :doc:`Interface Write </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/interfacewrite>`
-  :doc:`Interface Write (ADAU145x) </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/inferfacewrite>`
-  :doc:`Master Control Port Interface Read </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/inferfaceread1>`
-  :doc:`Output </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/output>`
-  :doc:`SPDIF Input/Output </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/spdifinputoutput>`

.. hint::

   Note: The Input and output blocks represent physical and limited hardware resources. If you attempt to insert more input or output blocks than there are available resources you will receive the

   
   .. container:: em

      "Not enough DSP Resources for this Algorithm"

   
   error. For example, only one input block per processor can be used in a schematic. In additional, inputs and outputs can only be assigned to a single block at a time. For example, you cannot create two output blocks that represent the same output channel.


See the :doc:`GPIO Conditioning Examples </wiki-migration/resources/tools-software/sigmastudio/tutorials/gpioconditioningexample>` topic for sample schematics.
