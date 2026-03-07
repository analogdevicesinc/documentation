GPIO Conditioning Examples
==========================

| :doc:`Click here to return to the Tutorials section. </wiki-migration/resources/tools-software/sigmastudio/tutorials>`
| These examples all use the 1701 DSP evaluation board, which supports two analog and seven digital inputs.

Example 1
---------

| Blocks: Up/Down Control, Index Lookup Table, Push and Hold
| Two General Purpose input blocks drive the push and hold block. Its outputs are used to select the index for the Index Lookup Table. The Up/Down block increments or decrements the index, based level. The Interface Read block connects to the light-green pin of Up/Down Control block, which drives both the index lookup table and the Interface Write blocks. The output of the Lookup Table drives the red pin (used for external connection) of Single Slew Ext(ernal) Vol(ume). Then the signals are given to two DACs — which are nothing but the analog outputs of the board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/gpioconditioningexample1.jpg
   :alt: gpioconditioningexample1.jpg

Example 2
---------

| Blocks: Rotary Encoder and Up/Down Control w/ Lookup Table (Up/Down + INTF)
| Two General Purpose input blocks drive the Rotary Encoder block. Its outputs are used to select the index for the Up/Down Control w/ Lookup Table. The Interface Read block connects to the light-green pin of Up/Down Control w/ Lookup Table block, which drives both the Single Slew Ext Vol and Interface Write blocks. Then the signals are given to two DACs, which are the analog outputs of the board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/gpioconditioningexample2.jpg
   :alt: gpioconditioningexample2.jpg

Example 3
---------

| Blocks: Push and Hold, Up/Down Control w/ Lookup Table (Up/Down + INTF)
| Two General Purpose input blocks drive the Push and Hold block. Its three outputs are used to select the index for the Up/Down Control w/ Lookup Table. The Interface Read block connects to the light-green pin of Up/Down Control w/ Lookup Table block,which drives both the Single Slew Ext Vol and Interface Write blocks. Then the signals are given to two DACs, which are the analog outputs of the board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/gpioconditioningexample3.jpg
   :alt: gpioconditioningexample3.jpg
