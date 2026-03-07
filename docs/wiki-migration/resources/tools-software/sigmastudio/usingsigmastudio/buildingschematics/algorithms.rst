Algorithms: Add/Remove, Grow/Reduce
===================================

| :doc:`Click here to return to the Building Schematics page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics>`
| Each schematic block represents one or more signal processing algorithms. Algorithms range from very simple, like :doc:`Signal Add </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/signaladd>`, to advanced system components like :doc:`Dynamic Bass Boost </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms/dynamicbassboost>`. You can add or remove algorithms from blocks to meet your specific requirements. Algorithms can also be grown as explained below.

--------------

**Add Algorithm:**

| You must add an algorithm -- typically associated with set of i/o pins -- for a block to function. To Add an algorithm to a block, **right-click** the block and select **Add Algorithm > IC #**, selecting the DSP IC for the algorithm. Note, if there are multiple processors (ICs/DSPs) in your project, you can select which DSP will run an algorithm, see below for more information.
| |algorithmpic1.png|
| At this point, right-click the block on its border or label to add another algorithm if desired. (It's important to right-click the border or label; if you right-click the center, you may display the pop-up window for entering parameters values.)
| |algorithmpic2.png|
| A block that contains no algorithms will have no controls or pins and you will only see the block's name (as shown in the figure below). You must add an algorithm to empty blocks before they can be used in the schematic design.
| |algorithmpic3.png|
|

.. tip::

   Note: When using the :doc:`Tree ToolBox window </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/toolbox>`, an algorithm is always created for each inserted block. However, if you use the traditional :doc:`ToolBox </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/toolbox>` window to insert blocks, you may additionally have to add an algorithm.


When adding an algorithm, not only are you choosing the method of computation for the block, you're also selecting a particular DSP association for the algorithm. This is important if you're connect multiple DSP processors: by adding algorithms to blocks, you can share blocks and controls and communicate with multiple DSPs simultaneously.

| For example: the `Single Volume Control <https://wiki.analog.com/resources/tools-software/sigmastudio/volumecontrols/singlevolumecontrol>`_ block has a single slider control for all algorithms. If you create a project with 2 DSP processors, IC 1 (AD1940) and IC 2 (ADAU1701), and select Add Algorithm, you will be prompted for which chip you want to add this algorithm to.
| |algorithmpic4.png|
| It is possible to have the first algorithm assigned to IC 1, and a second algorithm assigned to IC 2, but they share the volume block and a single slider control. Note that you cannot create a wire between different processor, see the `Wires <https://wiki.analog.com/resources/tools-software/sigmastudio/usingsigmastudio/wiresandaliases>`_ topic for more information.

--------------

**Remove Algorithm:**

It is also possible to remove algorithms from blocks. To remove an algorithm, **right-click** the block and select **Remove Algorithm**. This will remove the last algorithm (bottom pins) which is the algorithm that was added most recently. If the block contains only one algorithm, removing the algorithm will result in an empty block

--------------

**Grow Algorithm:**

Growing algorithms, means building upon the existing algorithm of the block, keeping the same algorithm in place (expanding upon it) and the same DSP association (Adding algorithms does neither). To grow an algorithm, **right-click** the block and select **Grow Algorithm > (algorithm name) > (grow amount)**. Note that growing is not available for all algorithms.

The easiest way to understand the distinction between adding and growing is with a mixer block. Drag a Cross Mixer (2 Inputs) into the workspace. Right-click and select Grow Algorithm, See the example below.

-  Growing the mixer creates more mixer output pins, essentially you are creating extra mixer output channels that share a common input. There is still only a single algorithm in the block.
-  Adding an algorithm creates separate algorithms that share the control window, but do not share inputs/outputs pins or resources. In the mixer example, an additional input pin, oupput pin, and a cross-mixer control are added to the block.

--------------

**Reduce Algorithm:**

| Reducing is the opposite of growing, it removes the extra controls and pins that are created by the Grow Algorithm operation. Like remove algorithm, reduce will remove controls/pins starting at the bottom or the most recently grown item.
| |algorithmpic5.png|

.. |algorithmpic1.png| image:: https://wiki.analog.com/_media/algorithmpic1.png
.. |algorithmpic2.png| image:: https://wiki.analog.com/_media/algorithmpic2.png
.. |algorithmpic3.png| image:: https://wiki.analog.com/_media/algorithmpic3.png
.. |algorithmpic4.png| image:: https://wiki.analog.com/_media/algorithmpic4.png
.. |algorithmpic5.png| image:: https://wiki.analog.com/_media/algorithmpic5.png
