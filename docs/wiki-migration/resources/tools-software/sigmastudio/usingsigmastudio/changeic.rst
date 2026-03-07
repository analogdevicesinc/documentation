Change IC
=========

| :doc:`Click here to return to the Using Sigma Studio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`
| Each Schematic block contains one or more algorithms, and each algorithm is associated with a particular DSP processor in the Hardware Configuration Tab. In designs that contain more than one processor, it is possible to change the IC assignment for existing schematic algorithm.

To Change IC assignment:
------------------------

| Right-click on a block and select **Change IC** from the pop-up menu, the available processors that support the algorithm will be listed in the menu:
| |changepic1.png|

| If a block contains multiple algorithms, there will be a separate Change IC menu choice for each block algorithm. If you want to change the IC assignment for all of the block's algorithms in a single operation see below.
| |changepic2.png|

To Change IC assignment for all selected blocks:
------------------------------------------------

| It is possible to change the IC for all selected blocks and algorithms in a single operation. First, select multiple blocks that require IC re-assignment. Secondly, right-click in the Schematic tab window and select **Change IC** from the menu (all processor ICs will be listed).
| |changepic3.png|
|

.. hint::

   Note: If you select an IC that does not support all of the selected blocks' algorithms, an error dialog will be displayed and only the supported algorithms will be re-assigned to the selected IC. Also note, it is not possible to perform the Change IC command for any Input or Output blocks.


.. |changepic1.png| image:: https://wiki.analog.com/_media/changepic1.png
.. |changepic2.png| image:: https://wiki.analog.com/_media/changepic2.png
.. |changepic3.png| image:: https://wiki.analog.com/_media/changepic3.png
