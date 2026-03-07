Navigation
==========

You can return to the ACE Application User Guide Homepage here: :doc:`Application User Guide </wiki-migration/resources/tools-software/ace/applicationuserguide>`

-  :doc:`Previous (Board View) </wiki-migration/resources/tools/software/ace/understandingtheui/boardview>`
-  :doc:`Next (Memory Map View) </wiki-migration/resources/tools/software/ace/understandingtheui/memorymapview.txt>`

Chip View
---------

The Chip View, shown below, is an interactive block diagram for the component. It provides an insight into the functional operation of the component, and allows the user to configure high level features of the component in an intuitive manner.

.. image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/ChipView.png
   :alt: Chip View

Block Types
~~~~~~~~~~~

The diagram block classifications are:


|ChipConfigurable13.png|

-  **Configurable –** A block which is configurable by clicking on it. Depending upon the block and the associated component, clicking can enable/disable the block, allow inline editing of a single value, or present a popup for configuring multiple values

.. image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/CipNonConfigurable.png
   :alt: CipNonConfigurable.png
   :align: left
   :width: 50px
   :height: 50px

-  **Non-configurable –** A block which has no settings that can be edited from the Chip

View.  They are included in the diagram to depict signal flow, or to help with understanding the component.


|ChipDown.png|

-  **Power down/ disabled –** A block which has been disabled, either because of enabled bits or because it is powered down. The tooltip will indicate whether it can be enabled

and/or powered up with a click, others can be enabled from the Memory Map View.

.. image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/ChipError.png
   :alt: ChipError.png
   :align: left
   :width: 49px
   :height: 43px

-  **Error -** A block which is in an error condition. Either one of the block’s properties is causing the error, or associated block(s) are causing this block to receive signals that are invalid. Open the Events Tool View to see more details about the error(s).

Configuration
~~~~~~~~~~~~~

The configuration of settings for the component is done by clicking on configurable blocks, which can be identified by their darker backgrounds and a hand cursor.  Changing value(s) on block(s) will update the associated register values, and the changes will be reflected in other views like the Memory Map View. Note that these changes will only apply to software unless auto apply is enabled for the board or until an Apply action is selected.

In many cases, when there are multiple instances of similar blocks that are functionally grouped, the diagram is simplified to show one group at a time.  A selector is used to choose which group of blocks to show, and the group of blocks is indicated by a dark background. The user can click the selector to choose a particular group, or click the up and down arrows to choose the next or previous group.

View Toolbar
~~~~~~~~~~~~

Unless the auto apply has been enabled in the Board View, section 3.6.3, values changed in the Chip View will affect the software values in the Chip and Memory Map views only, they will not affect the hardware state. The following view toolbar buttons can be used to update both the hardware and software values:

  

-  **Apply Changes –** Applies all of the register changes made in the software to the hardware.

  

-  **Read All –** Reads the register values from the hardware and updates the software values.

  

-  **Reset Device –**

Resets hardware to its default state. This command does not affect the soft= ware values.

  

-  **Diff –** Shows registers that are different on the hardware in bold text when you navigate to the Memory Map View. If changes have been made to the device using an external tool, the operator should click diff before clicking apply changes to avoid unexpected writes.

-  **Software Defaults –** Updates the software to display the software specified default values.

This command does not affect the hardware.

Navigation from the Chip View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The proceed to memory map button in the bottom-right corner of the diagram will open the Memory Map View for the device when clicked.

If the product has data acquisition and analysis functionality you will be able to navigate to this view from the proceed to capture button at the bottom-right of the diagram.

.. |ChipConfigurable13.png| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/ChipConfigurable13.png
   :width: 40px
   :height: 40px
.. |ChipDown.png| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/ChipDown.png
   :width: 50px
   :height: 50px
