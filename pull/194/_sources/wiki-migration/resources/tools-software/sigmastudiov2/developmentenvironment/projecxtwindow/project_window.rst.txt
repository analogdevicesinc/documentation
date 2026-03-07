| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/developmentenvironment>`

Project Window
==============

| |image1|
| This Window displays the tree structure of the project in a hierarchical manner. As depicted in the figure, starting from the system, the canvas of the system has SC589 platform and USBi for communication and hence the PC, platform and the usbi communication device are depicted as children of the system. Further the SC589 platform has an SC5xx processor which consists of two SHARC cores and each SHARC core has a schematic. The settings tab related to a particular platform, processor, core or schematic can be opened from the project window.
| This window is useful if we have to navigate to a particular element in the schematic. Option for renaming the nodes is also available in the project window. By selecting a particular node entry and pressing the rename button on top of the window, allows the user to rename the node to a user desired name.
| In cases where multiple platforms or processors are present in the project, the user also has an option to specify the order in which the compilation of the ICs has to take place. By using the up and down arrow marks present at the top, it is possible to reorder the ICs in the desired way. Individual download of platforms or processors in cases of multiple platforms/processors being present is also possible. This can be achieved by selecting a particular processor/platform and pressing on the download button present on top of the window.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/developmentenvironment/projecxtwindow/projectwidnow.png
   :width: 250px
