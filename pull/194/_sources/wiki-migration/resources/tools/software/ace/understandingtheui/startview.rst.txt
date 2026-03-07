Navigation
==========

You can return to the ACE Application User Guide Homepage here: :doc:`Application User Guide </wiki-migration/resources/tools-software/ace/applicationuserguide>`

-  :doc:`Previous (Navigation) </wiki-migration/resources/tools/software/ace/understandingtheui/navigation>`
-  :doc:`Next (System View) </wiki-migration/resources/tools/software/ace/understandingtheui/systemview>`

Start View
----------

When the application opens you will be presented with the Start View. This view allows you to set up a system to be used in a session. A system can be made up of a single or multiple subsystems and can be a mixture of attached hardware and unattached local plug-ins.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/understandingtheui/Start.PNG
   :alt: Start.PNG

Attached Hardware Section
~~~~~~~~~~~~~~~~~~~~~~~~~

The attached hardware section displays all subsystems which are physically atta= ched to the PC through the USB and for which there are plug-ins. The identify hardware button can be used to identify the detected hardware, generally by flashing an LED on the board. This allows the user to verify which piece of evaluation hardware they are connecting to. By double clicking a subsystem in this section it will be added to the system and ACE will try to automatically acquire this hardware.

Explore Without Hardware Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The explore local plug-ins section contains a list of subsystems for plug-ins which are installed on your local machine, without hardware attached. This allows you to preview ADI components without access to the associated hardware.

Sessions
~~~~~~~~

Sessions are used to save and reopen the user’s work inside the application. Opening a session will restore the system that was created when the session was saved and the state of the views opened. They also store macros that were created or used when the session was saved.

Previous sessions can be opened and new sessions created from the left-hand pane of the Start View, Recently opened sessions can be viewed and opened from the recent sessions’ section.  Only one session can be open at a time.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/understandingtheui/Sessions.PNG
   :alt: Sessions.PNG

Navigation from the Start View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The add subsystems button, see Figure 5, adds all selected subsystems local or attached to the system and navigates to the next level of the hierarchy, the System View. Alternatively a single subsystem can be added by double-clicking on the desired subsystem. By default adding a subsystem using the double-click method will add the subsystem to the system and bring you to the default view as set in the plug-in. This can be changed by unselecting the navigate to default page option at which point the double-click method will bring you to the System View.
