Plug-in Quickstart Guide
========================

This WIKI page will give a brief overview of an ACE plug-in being used for the first time. The features and functions outlined in this section will be explained in more detail in future WIKI articles. It will contain brief introductions to the main views available in a standard plug-in as well as creating and reusing ACE Session files.

You can return to the ACE WIKI Homepage here: :doc:`ACE Homepage </wiki-migration/resources/tools-software/ace>`

Launching a Plug-in
-------------------

To begin using a plug-in, as stated in the previous article, you simply need to double click on a plug-in (either in your "Attached Hardware" list or the "Explore without Hardware" list. As soon as you open your first plug-in, a "subsystem" is added to the ACE "System" view and ACE creates a new active :doc:`Session </wiki-migration/resources/tools-software/ace/userguide/quickstart/quickstartplugin>`.

The system view can be made up of multiple subsystems. Each subsystem is a representation of the boards that make it up. These can be made up of a single board or multiple boards and depending on whether you have attached hardware they can represent the physical hardware attached to your machine or a virtual subsystem defined by the plug-in developer.

Plug-in Structure
-----------------

You can access the system view using the "Systems" button in the sidebar menu. The view will not be opened if you have not added a subsystem to your current system. Double click a plug-in to add a new subsystem.


|image1|

.. container:: centeralign

   
   Fig. 1: System View
   ^^^^^^^^^^^^^^^^^^^
   


Most plug-ins will have their own default view defined, meaning when you open them they will launch and open the most relevant view for the user as selected by the plug-in developer. This might be the board component, chip component or one of their other child views depending on the particular requirements for the plug-in.

ACE is based on a hierarchy of views which mirrors the evaluation setup from the system level all the way down to the register level.

See **Fig. 2** showing a series of examples of common plug-in architecture.

==================== ===================== ==========
Standard Memory Chip Standard Capture Chip Multi Chip
==================== ===================== ==========
|image2|             |image3|              |image4|
==================== ===================== ==========

.. container:: centeralign

   
   Fig. 2: Plug-in Hierarchy Examples
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   


Session
-------

Sessions are used to save and reopen the user’s work inside the ACE application. Opening a session will restore the system that was created when the session was saved. All subsystems and views that were opened will be restored to the same state as when they were saved. Sessions also store macros that were created or used when the session was saved as well as the current state of all of the user selected values for various elements exposed in a plug-in, for example the values entered in the memory map view for writing part registers or values entered in the plug-in block diagrams.

.. note::

   Only one session can be open at a time. When a session is active it's name will be displayed in the application title bar.


Previous sessions can be opened and new sessions created from the Sessions Menu in the top right hand corner of the Start View. Recently opened sessions can be viewed and opened from the Recent Sessions list in the sidebar menu.



|image5|

.. container:: centeralign

   
   Fig. 3: Start Screen Session Controls
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   


The main plug-in view is usually opened as soon as you launch a plug-in. If you find yourself on the Systems tab when you launch a plug-in you can still access the plug-in content by double clicking on the darker green board elements in the subsystem to access the board level view for the plug-in.

.. tip::

   You can optionally disable default navigation for plug-ins from the Preferences view in the Settings tool. This means that the System view will always open when you add a new plug-in or simply disable the default navigation enabled by the plug-in developer.


Board Views
-----------

Most plug-ins in ACE follow a very similar structure and style to simplify the experience for users. Darker colored controls are "active" control that will usually incur some action when clicked. The Board view (shown in **Fig. 4** below) in most cases operates as way to navigate to one of the on-board chip components. The chip selector block shown can be used to double click navigate to the chip view.


|image6|

.. container:: centeralign

   
   Fig. 4: Board View Tour
   ^^^^^^^^^^^^^^^^^^^^^^^
   


The device state can be determined from the two methods shown. A direct board connection status is illustrated in the board level status indicator. The status bar on the bottom of the window shows the current state of the system. A plug-in is shipped with sequence that is used to check the state of the hardware and ensure it loads in a known condition. If this sequence fails, the hardware can fall into an Unknown state and may impact the plug-in usability.

.. tip::

   If this happens, try the Reset function in the Device Sequence Toolbar. If this doesn't help try deleting the subsystem in your system view and reconnecting your hardware. If all else fails, use the Report Issue button in the lower left corner of the screen to report the problem!


.. important::

   When operating without hardware, the State will usually be unknown and reported errors are not necessarily indicative of problems in ACE, it may just be failing since there is no hardware to communicate with! It depends on how the plug-in has been built to handle this scenario.


Chip Views
----------

Chip views share a similar in structure to the board view and use the same control set to provide their diagrams. The Device Sequence Toolbar, Status Bar Updates and user interactions are all the same implementation but content can vary.

Interactive elements are still identified by their darker color and will incur some action when a user clicks or double clicks the control. For the majority of plug-ins most of the interactivity takes place at this level and contains more variability than the board view. Chips for the most part contain a Memory Map view for interacting with and controlling the lower level controls for the chip component, e.g. the Registers or Bitfields exposed in the plug-in. Chips often expose their child nodes using standard navigation buttons on the lower right hand side of the diagram as shown in **Fig. 5** below. These are simply convenient ways to access the chips child views but there are many ways that a developer can introduce navigation to other elements in their views, but this will be covered in more detail in another WIKI article.


|image7|

.. container:: centeralign

   
   Fig. 5: Chip View
   ^^^^^^^^^^^^^^^^^
   


Other standard options for navigation through the ACE application are Breadcrumb Navigation and the System Explorer. The Breadcrumbs are always available at the top of the screen and allow you to see what children are available at a given node and select them to navigate to that view.

Alternatively, you can enable the System Explorer from the Tools drop down list in the sidebar menu. This will bring up a tree view with all of the current subsystems added to your system and each of their child nodes exposed as a hierarchy of view for navigation.


|image8|

.. container:: centeralign

   
   Fig. 6: Alternative Navigation Options
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   


The table below shows the Analysis View and Memory Map view for the chip. These views can be opened using any of the standard navigation schemes outlined above, e.g. Standard Navigation Buttons in Diagram View (where available), Breadcrumbs or System Explorer.

=============== =============
Memory Map View Analysis View
=============== =============
|image9|        |image10|
=============== =============

.. container:: centeralign

   
   Fig. 7: Chip Child Node Examples
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/quickstart/systemview.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/quickstart/plugin-architecture.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/quickstart/plugin-architecture_cap.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/quickstart/plugin-architecture_multi.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/quickstart/start_sessions.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/quickstart/plugin_boardview.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/quickstart/plugin_chipview.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/quickstart/plugin_altnavigation.png
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/quickstart/plugin_memorymap.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/quickstart/plugin_capture.png
   :width: 400px
