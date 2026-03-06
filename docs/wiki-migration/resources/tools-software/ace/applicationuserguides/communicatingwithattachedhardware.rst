Navigation
==========

You can return to the ACE Application User Guide Homepage here: :doc:`Application User Guide </wiki-migration/resources/tools-software/ace/applicationuserguide>`

Communicating with Attached Hardware
------------------------------------

Acquiring and Releasing Hardware
--------------------------------

When a subsystem is added to the system ACE automatically tries to acquire the associated hardware. After this point hardware can be acquired or released through the acquire/release menu in the System View which can be access by clicking on the USB connectivity button, see :doc:`System View </wiki-migration/resources/tools/software/ace/understandingtheui/systemview>` for more information.

Initialization Wizards
----------------------

Where available initialization wizards provide a setup process which collects and applies the initial startup conditions for a board and all its components. Once the software inputs are complete pressing the apply button will perform all necessary writes and reads in order to put the hardware into the defined state, see :doc:`Board View </wiki-migration/resources/tools/software/ace/understandingtheui/boardview>` for more Information

View Toolbars
-------------

The view toolbars in each of the Board, Chip and Memory Map views provide controls for communicating with hardware. The View Toolbar is Located at the top of the View as seen below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/applicationuserguides/toolbarlocation.png
   :width: 400px

Each view toolbar contains a selection of the following communication options:

::

   *  {{:resources:tools-software:ace:applicationuserguides:ResetChip.PNG?80|}} **Reset Device –** Reverts all components to their default state.****

-  |image1| **Poll Device –** If enabled causes the continuous polling of the device for state changes.***\*

  

-  |image2| **Auto Apply –** If enabled causes continuous applying of changes made by the operator to the

device.

  

-  |image3| **Apply Changes –** Applies all changes made in the software to the hardware.***\*

  

-  |image4| **Apply Selected –** Applies current software value of the selected register to the hardware.

  

-   |image5| **Read All –** Reads the register values from the hardware and updates the software to these values.

  

::

   *`{{:resources:tools-software:ace:applicationuserguides:Readselected.PNG?80|}} **Read Selected –** Reads the selected registers value from the hardware and updates the software to this value.

        

-  |image6| **Reset Device –** Resets hardware to its default state.

For more view specific information see:

-  :doc:`Board View </wiki-migration/resources/tools/software/ace/understandingtheui/boardview>`
-  :doc:`Chip View </wiki-migration/resources/tools/software/ace/understandingtheui/chipview>`
-  :doc:`Memory Map View </wiki-migration/resources/tools/software/ace/understandingtheui/memorymapview.txt>`

Register Debugger
-----------------

The Register Debugger is a Tool View which allows the performance of raw register reads and writes, see :doc:`Here </wiki-migration/resources/tools/software/ace/understandingtheui/toolviews>` for more information.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/ace/applicationuserguides/poll.PNG
   :width: 80px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/ace/applicationuserguides/autoapply.PNG
   :width: 80px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/ace/applicationuserguides/applychanges.PNG
   :width: 80px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/ace/applicationuserguides/applySelected.PNG
   :width: 80px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/ace/applicationuserguides/readall.PNG
   :width: 80px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/ace/applicationuserguides/resetchip.PNG
   :width: 80px
