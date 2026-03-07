Undo History Dialog
===================

| :doc:`Click here to return to the Dialogs page </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/dialogs>`
| The Undo History dialog shows you a list of the actions you have performed on a schematic in the current editing session. To access this dialog go the **Edit - History...** in the main application menu. You can revert the schematic design to any point in its Undo History simply by selecting an entry in the list and pressing the OK button.
| |undopic1.png|
| SigmaStudio's undo mechanism uses system memory resources. You can empty the history and free these resources by pressing the **Clear**... button.

Undo:
-----

Most actions that you perform in the Schematic and Hardware Configuration tabs can be undone. For example, inserting or deleting a block, creating a wire, re-naming a block, or moving the screen location of a block. You can undo the most recent action by choosing **Edit - Undo** from the main menu or by using the keyboard shortcut, **Ctrl-Z**.

Redo:
-----

Undoing can also be undone. After undoing an action, you can redo it by choosing **Edit - Redo** from the main menu or by using the keyboard shortcut, **Ctrl-Y** or **Ctrl-Shift-Z**.

.. |undopic1.png| image:: https://wiki.analog.com/_media/undopic1.png
