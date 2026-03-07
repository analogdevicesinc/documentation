| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>`
| =====Store/Restore Links=====

| In SigmaStudio+, it is possible to connect multiple modules to the output pin of a given module. When such a module (with multiple connections) has to be replaced with another module, all the connections from the module has to be redrawn in addition to replacing the module. The 'Store-Restore Link' feature can be used to simplify the process of re-establishing the connections. Using this feature, a user could store the collection of links originating from specified pin and restore the connections on to an output pint on any other modules in the signal flow.
| Right click on the module and choose one of the output pins from "Store output links" option to temporarily store all the links originating from that pin. Select the module on to which the links are to be restored and use the option "Re-store output links" from the context menu to restore the links. Choose the output pin and the saved collection from the context menu. Links will be validated before restoring. Invalid links in the collection (e.g. the destination pin is consumed) will be skipped.
| |image1| |image2|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/store.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/restore.png
   :width: 400px
