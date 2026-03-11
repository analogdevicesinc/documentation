Schematic Blocks
================

:doc:`Click here to return to the Building Schematics page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics>`

Schematic Blocks are used to build a SigmaStudio design. The blocks available for each processor are displayed in the ToolBox and Tree ToolBox windows and can be dragged and dropped into the schematic.

--------------

Pins:
-----

Each schematic block can contains one or more pins used to connect the blocks together. Pins are used to route audio and control data in the schematic flow. There are 3 different types of pins:

-  Input Pin (Green)
-  Output Pin (Blue)
-  Control Data Pin (Orange)

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/schemblockpic1.png
   :alt: schemblockpic1.png
   :align: center

.. hint::

   Note: Input pins can only connect to Output pins and Output pins can only connect to Input pins. Typically, control data pins are only connected to other control data pins, but it is possible to connect an audio data pin to a control data pin and a control data pin to an audio data pin when necessary.


Hover over a block's pin with the cursor to display the pin's tool-tip which includes the pin number, unique name, and signal data type.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/schemblockpic2.png
   :alt: schemblockpic2.png
   :align: center

--------------

Algorithms:
-----------

Each block represents one or more algorithms. You can add algorithms to blocks or modify them to meet your specific requirements by selecting Add Algorithm or Grow Algorithm from the block's right-click context menu. A block that contains no algorithms will have no controls or input/output pins. See :doc:`Algorithms (Adding and Growing) </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/algorithms>` for more information.

--------------

Naming:
-------

To change the name of a block, double click on the block label and type a new name. Note that within each hierarchy board all block names must be unique. You will see an error dialog if you attempt to use a name that is already present in the current window.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/schemblockpic3.png
   :alt: schemblockpic3.png
   :align: center

--------------

Selecting:
----------

To select a block, click its border or label. To select multiple blocks, hold down the Shift or Ctrl key while clicking. You also can click in the schematic window and drag a box around blocks to select the, this will select any blocks that are in the selected screen area. To select all block you can press **Ctrl + A** or use the **Select All** button in the Schematic Layout toolbar. Selection is indicated by a light-green outline.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/schemblockpic4.png
   :alt: schemblockpic4.png
   :align: center

--------------

Deleting:
---------

To remove a block from the schematic select the block and then press the **Delete** key. You can also remove selected blocks by choosing **Edit - Cut** from the main application menu or by pressing **Ctrl + X**.

--------------

Action Menu:
------------

Right-click on a block to bring up the block's popup menu. This menu includes items for control `Settings <https://wiki.analog.com/resources/tools-software/sigmastudio/usingsigmastudio/schematicactionsandcommands/schematicsettings>`_, Add/Remove Algorithm, Grow/Reduce Algorithm, Changing IC, and Cut/Copy/Paste editing.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/schemblockpic5.png
   :alt: schemblockpic5.png
   :align: center

--------------

Layout:
-------

You can change the position of a block by selecting it with the mouse and dragging it to a new screen location. Use the `Schematic Layout toolbar <https://wiki.analog.com/resources/tools-software/sigmastudio/developmentenvironment/toobars>`_ buttons to align groups of blocks in your schematic. Alignment is applied to all selected blocks. The blocks with a blue outline will be aligned to the block with a green outline.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/schemblockpic6.png
   :alt: schemblockpic6.png
   :align: center

--------------

Controls:
---------

Blocks can contain a variety of controls for editing algorithm parameters.

Spin Controls:
~~~~~~~~~~~~~~

Spin controls allow you to change values either by entering the value directly in the edit-box or by clicking the left/right or up/down arrows. You can left-click and hold an arrow to make large adjustments or click-hold-drag to increase the rate of change. A grey control (for example the top control show below) means the control is disabled and the value cannot be changed for the current algorithm.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/schemblockpic7.png
   :alt: schemblockpic7.png
   :align: center

Knobs & Sliders:
~~~~~~~~~~~~~~~~

To change the value of knobs or slider control, click and hold the left mouse button on the control and drag to adjust the value. You can also change the knob or slider control's value, range, and step size. To modify the knob or slider settings, right-click on the control which displays the control pop-up window (shown below).

-  **Value** Set the control's value.
-  **Min/Max** Adjust the control's value range (within the limits of the block's algorithm).
-  **Step** Set the control's step size or granularity.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/schemblockpic8.png
   :alt: schemblockpic8.png
   :align: center

Pop-up Control Windows:
~~~~~~~~~~~~~~~~~~~~~~~

Some blocks include pop-up control windows providing advanced functionality, for example the `General (2nd Order) filter <https://wiki.analog.com/resources/tools-software/sigmastudio/filters/general2ndorder>`_. To open a block's advanced control window, click on the icon button.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/buildingschematics/schemblockpic9.png
   :alt: schemblockpic9.png
   :align: center
