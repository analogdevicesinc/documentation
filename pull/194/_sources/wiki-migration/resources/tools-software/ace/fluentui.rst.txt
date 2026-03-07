ACE UI Updates (2019)
=====================

This page highlights recent product improvements to help you get up to date on what’s new in the ACE application.

You can return to the ACE WIKI Homepage here: :doc:`ACE Homepage </wiki-migration/resources/tools-software/ace>`

With the release of ACE v1.14 the user interface has undergone a major refresh. These changes have been made in an effort to modernize the application and improve the overall user experience. Key differences in the update are demonstrated below to show how you can access many of the modified/new features in the new ACE theme.

.. note::

   This is only the first in a series of updates to improve the ACE user experience. Watch this space to keep track of new updates in future releases!


Application Visual Differences
==============================

======================= ======================
Classic                 Fluent
======================= ======================
|classic_ace_theme.png| |fluent_ace_theme.png|
======================= ======================

Key Changes
-----------

1. Controls styling changed across the whole application

2. Addition of sidebar menu in updated design to make common features more accessible

3. Removal of Top Menu and Tool View buttons (features now accessed from the side bar menu)

4. File menu replaced with a "More Options/Ellipse" menu to access Session management commands

ACE UI User Settings
====================

The "Classic" ACE theme will remain supported at present and can be easily enabled from the ACE User Settings "Preferences" tab. Please note, if you opt to use the "Classic UI" this theme may not be subject to future updates/improvements.

.. tip::

   If you encounter any issues with the updated ACE theme you can change your UI preferences in the settings window, under Preferences.


Changing UI Preferences
-----------------------

1. Open the ACE settings window and click on the "Preferences" tab.

2. To revert to using the "Classic" theme, check the Use Classic ACE UI check box.

3. ACE requires a restart in order for user preferences to take effect.

+----------------------------------------------------+----------------------------------------------+
| Classic                                            | Fluent                                       |
+====================================================+==============================================+
| Access settings dialog from the Tools top bar menu | Access settings dialog from the sidebar menu |
+----------------------------------------------------+----------------------------------------------+
| |settings_use_classic.png|                         | |settings_use_fluent.png|                    |
+----------------------------------------------------+----------------------------------------------+

Fluent Theme Tour
=================

Sidebar Menu
------------

One of the most obvious and immediate changes noticed in the new Fluent application theme is the addition of the sidebar menu. This menu is visible throughout the entire application and replaces the Top Bar Menu as well as the small Tool View buttons seen at the top of the Classic theme's interface.

The majority of the ACE core features, outside of plug-in navigation, will be accessed from this sidebar menu in the updated theme.

All features currently available in the sidebar menu:

-  Home Button - Navigates to the ACE start screen
-  Systems Button - Navigates to the ACE System View when available (e.g. with an active session)
-  Vector Generator - Navigates to the ACE Vector Generator View
-  Plug-in Marketplace - Navigates to the plug-in marketplace, used to install/update/uninstall ACE plug-ins
-  Remoting Console - Launch the ACE Remote Control console application from inside ACE
-  Recent Sessions - Contains a list of your most recent ACE sessions
-  Tools - Contains a list of all available ACE tool views
-  Report Issue - Immediately after an error occurs, use this feature to capture information about the current session and create blank email with this information attached (Note: you can provide details of the situation which caused the error in the body of the email)
-  Help - Launches the new ACE Help tool view (can also be launched from the Tools list)
-  Settings - Launches the ACE Application settings view (e.g. to access user preferences)

.. tip::

   The menu also contains a pin/unpin button in the top left corner. By default the menu is pinned, if you want to unpin it just click the button and the sidebar menu will collapse whenever you move the mouse cursor out of the menu's boundary.


.. image:: https://wiki.analog.com/_media/sidebar_menu.png
   :alt: sidebar_menu.png
   :align: center

More Options/Ellipsis Menu
--------------------------

As outlined in the previous section, the majority of the ACE application core features are now accessible from the sidebar menu. In addition to this, there is a secondary menu included in the top right area of the ACE window where users can access more options.


|more_options_highlighted.png|

Currently this menu simply replaces the file menu options from the Classic ACE theme and is the new primary location for accessing ACE Session commands for Creation/Saving/Loading etc. of ACE sessions.


|more_options_focused.png|

Block Diagram Controls
======================

The updates to the ACE user interface will affect controls across the entire application, including the plug-in Block Diagrams. There is a possibility in some plug-ins that controls appearances are not as expected due to the port of the application theme.

.. important::

   While these changes are unlikely to affect plug-in usability if there are any major concerns/issues encountered please use the Report Issue feature to highlight this with the ACE development team.


Other Changes
=============

This section will document some other changes of note in v1.14 of ACE.

Start View Plug-in List Preference
----------------------------------

In previous releases of ACE we introduced the ability to swap between the Classic "Tiled" virtual plug-in list or a "Detailed List". In v1.14 the ability to hot swap between these views has been removed in favor of a fixed user preference from the Settings menu "Preferences" tab.

You can change the list style using the "Start View List Style" drop down box. This selection will be automatically made in v1.14 based on your current selection in ACE, if a clean install is performed the default selection is the "Detailed List" view.

This optimizes performance on startup when you have many plug-ins installed in your ACE application. The "Detailed List" offers further improvements/enhanced features over the "Tiled" list and is the recommended view for Start View performance.

=================== ================
Details             Tiled
=================== ================
|detailed_list.png| |tiled_list.png|
=================== ================

ACE Help Tool View
------------------

The Help top bar menu has been replaced with a new toolview that can be docked within the main ACE application or undocked as a floating tool view. The Help view is available immediately on the sidebar menu using the help button or can also be launched from within the Tools drop down menu (again within the sidebar menu).

The Help tool view contains license information, links to useful documentation and any of the ACE feedback links. As the application grows this tool view may be used for more in depth user help functionality. The help tool view is shown in the image below docked as the main content in the application. You can decide where you would like to dock this tool view to suit your own needs.

.. image:: https://wiki.analog.com/_media/help_tool_view.png
   :alt: help_tool_view.png
   :align: center

.. |classic_ace_theme.png| image:: https://wiki.analog.com/_media/classic_ace_theme.png
.. |fluent_ace_theme.png| image:: https://wiki.analog.com/_media/fluent_ace_theme.png
.. |settings_use_classic.png| image:: https://wiki.analog.com/_media/settings_use_classic.png
.. |settings_use_fluent.png| image:: https://wiki.analog.com/_media/settings_use_fluent.png
.. |more_options_highlighted.png| image:: https://wiki.analog.com/_media/more_options_highlighted.png
.. |more_options_focused.png| image:: https://wiki.analog.com/_media/more_options_focused.png
.. |detailed_list.png| image:: https://wiki.analog.com/_media/detailed_list.png
.. |tiled_list.png| image:: https://wiki.analog.com/_media/tiled_list.png
