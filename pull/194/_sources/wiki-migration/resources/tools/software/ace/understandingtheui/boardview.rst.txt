Navigation
==========

You can return to the ACE Application User Guide Homepage here: :doc:`Application User Guide </wiki-migration/resources/tools-software/ace/applicationuserguide>`

-  :doc:`Previous (System View) </wiki-migration/resources/tools/software/ace/understandingtheui/systemview>`
-  :doc:`Next (Chip View) </wiki-migration/resources/tools/software/ace/understandingtheui/chipview>`

Board View
----------

The Board View, shown below, shows all the ADI components located on a particular evaluation board plus the board connectors at their approximate locations.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/understandingtheui/BoardView.png
   :alt: BoardView.png

Component Types
~~~~~~~~~~~~~~~

The component classifications are:

-  **Primary (Configurable) –** The principal component for evaluation on the board.
-  **Secondary (Configurable) –** A lesser component on the board which can be explored and configured.
-  **Secondary (Non-configurable) –** A lesser component on the board which is present for informational purposes but cannot be configured.

Double-clicking a configurable component will bring the user to the device view for the selected component.

Component Styles
~~~~~~~~~~~~~~~~

The color styles and sizes representing the different components are:

|Primary.png| The primary component to be evaluated on the board.

|Secondary.png| A secondary component.

View Toolbar
~~~~~~~~~~~~

The view toolbar provides the following operations that affect all components on the board:   

-  **Reset Device –** Reverts all components to their default state.
-  **Poll Device –** If enabled causes the continuous polling of the device for state changes.
-  **Auto Apply –** If enabled causes continuous applying of changes made by the operator to the device. Please note that not all of these functions are available for all components.

If an error occurs when communicating with the device, the toolbar button will provide information regarding the error.  This notification will happen each time that clicking the button results in an error, and the error indicator will remain as long as the error condition exists.

Initialization Wizard
~~~~~~~~~~~~~~~~~~~~~

Some boards contain an initialization wizard, see bellow, to configure components. The wizard initialization setup process collects and applies the initial startup conditions for the board and all board components. No changes will be applied to the hardware until the operator clicks apply.


|Initialization Wizard, will appear on Left of Board View|

Types of Initialization Wizards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are three types of wizards

  

-  **Only one setup step –** In this type of wizard all initialization is done at once with all settings being applied when the apply button is pressed.

  

-  **Multiple steps (no order enforced) –** The wizard is broken down into multiple

steps.  Each step sets a specific component. In this type of wizard, the order in which steps are configured is not significant, so the user can jump between sections by clicking and expanding the section they are interested in. The board will not be configured until the apply button is pressed.   

-  **Multiple steps (order enforced) -** The wizard is broken down into multiple =

steps, with each step setting up a specific component of the device. In this case, previous selections impact the options for subsequent stages and all steps must be carried out in a defined order. After a step is configured, the next button is used to move to the next step in the process. Previous steps can be accessed by selecting the previous button or by clicking and expanding the desired step. Once a user navigates to a previous step, all subsequent steps must be completed again.

Initialization Wizard Buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The restore software defaults button will set all software values to their default states. This does not affect the hardware state. For wizards with a required defined order, a restore automatically brings the user back to the first section and requires all steps to be repeated before a configuration can be applied.

The apply button at the bottom of the wizard writes the configuration to the component.

The summary button opens a summary of your configuration. This summary can be viewed at any time.

Once the component has been configured, the summary is displayed where the wizard was previously displayed, see below, to allow you to easily review your settings. The modify button under the configuration allows you to reopen the wizard and change the settings.

.. image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/AfterConfig.png
   :alt: Board View with Initialization Wizard after Configuration

.. |Primary.png| image:: https://wiki.analog.com/_media/resources/tools-software/ace/understandingtheui/Primary.png
.. |Secondary.png| image:: https://wiki.analog.com/_media/resources/tools-software/ace/understandingtheui/Secondary.png
.. |Initialization Wizard, will appear on Left of Board View| image:: https://wiki.analog.com/_media/resources/tools-software/ace/understandingtheui/Wizard.png
