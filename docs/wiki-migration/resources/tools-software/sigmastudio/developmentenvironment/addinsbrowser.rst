Add-Ins Browser Dialog
======================

| :doc:`Click here to return to the Dialogs page </wiki-migration/resources/tools-software/sigmastudio/developmentenvironment/dialogs>`
| Additional Schematic blocks including both Algorithms and ICs can be added to the SigmaStudio environment through the Add-Ins Browser Dialog. Go to **Tools - Add-Ins Browser...** in the main application menu to access this dialog.
| |addinspic1.png|

To add a block:
---------------

-  Click the Add DLL button on the Add-Ins dialog toolbar or select File - Add DLL in the dialog's menu.
-  Navigate to the directory containing the SigmaStudio AddIn library file or files (\*.dll)
-  Select the files to be added and press the Open button.
-  Press the Save toolbar button to apply the changes.

To enable/disable a block:
--------------------------

-  Click the check box next to the file name.
-  Press the Save toolbar button to apply the changes.

To delete a block:
------------------

-  Select the file to delete in the Add-Ins file list.
-  Press the Delete Item toolbar button or choose File - Delete Item in the menu.
-  Press the Save toolbar button to apply the changes.

Added blocks are immediately available for use, you do not need to restart SigmaStudio. You should see the additional block(s) in the SigmaStudio :doc:`Toolbox </wiki-migration/resources/tools-software/sigmastudio/toolbox>` after saving.

.. tip::

   Note: Add-In information is saved in the "AddIns.xml" file located in the application's installation directory. You may want to back-up this file when installing SigmaStudio updates. Also, you can view/edit this file a text editor if you prefer.


.. |addinspic1.png| image:: https://wiki.analog.com/_media/addinspic1.png
