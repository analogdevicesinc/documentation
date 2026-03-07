Copy/Paste
==========

| :doc:`Click here to return to the Using Sigma Studio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`
| SigmaStudio supports clipboard operations in the Schematic Tab window:

**Copy:**

To Copy to the clipboard, select a block or blocks in the schematic tab, and press **Ctrl+C** or select **Edit - Copy** from the application menu. You can also right-click on a block and select copy from the context menu. Selected wires will only be copied if both the source and destination blocks are included in the selection.

It is also possible copy blocks within the schematic window by holding down the **Ctrl** key, clicking on a block in the selection, and then dragging the selection (while holding down the left mouse button and Ctrl key).

**Cut:**

The Cut operation removes objects from the schematic design and copies them to the clipboard. To Cut the schematic selection, press **Ctrl+X** or select **Edit - Cut** from the application menu.

**Paste:**

Blocks and wires on the can be pasted from the clipboard within the same schematic window or to another project's schematic. It is also possible to paste objects from one Hierarchy board to another. To paste the contents of the clipboard either: press **Ctrl+V**, select*\* Edit - Paste*\* from the application menu, or right-click in the Schematic tab window and select **Paste** from the menu.

.. hint::

   Note: The names of the pasted blocks may be different, blocks within each hierarchy board must have unique names.


**Paste Special:**

| By default, a pasted block's algorithm(s) are assigned to the same IC as the source block. For designs that use multiple processors it is possible to specify the target DSP IC by using the Paste Special operation. The Paste Special command can be accessed in the main application menu, **Edit - Paste Special...** This will open the Paste Special dialog where each block and algorithm in the clipboard is listed in the left column. In the right column, select the desired DSP IC to associate with each block or algorithm.
| |copypastepic1.png|

.. hint::

   Note: this dialog will be opened automatically when pasting between projects that have different IC types or names, which requires the DSP associations to be defined.


.. |copypastepic1.png| image:: https://wiki.analog.com/_media/copypastepic1.png
