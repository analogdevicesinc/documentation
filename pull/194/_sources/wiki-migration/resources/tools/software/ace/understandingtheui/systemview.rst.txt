Navigation
==========

You can return to the ACE Application User Guide Homepage here:

-  :doc:`Previous (Start View) </wiki-migration/resources/tools/software/ace/understandingtheui/startview>`
-  :doc:`Next (Board View) </wiki-migration/resources/tools/software/ace/understandingtheui/boardview>`

System View
-----------

The System View, shown below, shows the subsystems that have been added by the user to the system. From here subsystems can be linked to real hardware through the acquire/release hardware menu or removed from the system by clicking the remove button.

.. image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/AttachRel.PNG
   :alt: AttachRel.PNG

Acquiring and Releasing Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware subsystems, both attached and local can be acquired/released through the acquire/release hardware menu, see above, which can be accessed by pressing the USB connectivity button. The compatible subsystems list contains a list of available hardware which can be acquired by a subsystem. This list is comprised of both attached hardware and local only plug-ins. To acquire a subsystem select it from the compatible subsystems list and select the use selected hardware button.

To release the acquired subsystem select the operate without hardware option and then click the release button. Acquiring (local only) hardware will result in the same behavior as using the operate without hardware mode. The register map will store values that are written to it, however dependent behavior such as changes in read only status registers will not be modelled when an attached controller is not acquired.

Subsystem Connection State
~~~~~~~~~~~~~~~~~~~~~~~~~~

The USB icon on the USB connectivity button indicates the connection state of the subsystem. The color of the USB icon will change based on the current state of the connection, with the following states being represented:

.. image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/Green.png
   :alt: Green.png
   :align: left

::

   * Acquired - Subsystem is connected to a controller.

.. image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/Grey.png
   :alt: Grey.png
   :align: left

::

   * Released - Subsystem is not connected to a controller.

.. image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/Red.png
   :alt: Red.png
   :align: left

::

   *Error - The Controller is not responding as expected, Hardware may need reset.

.. image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/Yellow.png
   :alt: Yellow.png
   :align: left

::

   *Warning - An Operation on the Subsystem did not succeed, or behave as expected, but the Controller

is still available and responding.

Navigating from the System View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Double-clicking on a particular board transfers focus to the associated Board View for that board; alternatively double-clicking on a subsystem in this view will transfer focus to the Subsystem View.
