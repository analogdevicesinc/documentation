Clock Generation and Distribution Evaluation Software User Guide
================================================================

General Description
-------------------

This software user guide is intended to introduce the next generation of evaluation software provided for clock generation and distribution products from Analog Devices Inc. This user guide will cover the basic functionality and feature set for new clock and distribution evaluation software GUIs. A list of all current products which are supported by this user guide are listed in the **Supported Products** section. All supported products will have an individualized wiki user guide associated with them to describe device specific GUI functionality.

|

.. container:: centeralign

   | |image1|
   | *Figure 1. Example of CSG Evaluation Software Main Window*


SUPPORTED PRODUCTS
------------------

-  :adi:`AD9528 <EVAL-AD9528>`
-  :adi:`AD9554 <EVAL-AD9554>`
-  :adi:`AD9554-1 <EVAL-AD9554-1>`
-  :adi:`AD9559 <EVAL-AD9559>`

PC REQUIREMENTS
---------------

-  Windows XP or Windows 7
-  32-bit and 64-bit compatible

FEATURES
--------

-  Fully interactive block diagram GUI

   -  Active calculation of frequencies based on user entries and device configuration
   -  Active feedback from the GUI lets the user know if specific configurations are valid based on datasheet limits.

-  Frequency wizard for easy device configuration (not supported on some products with smaller feature sets)
-  Creates a register setup file to save and reuse configurations.
-  Can be used with or without an evaluation board for device setup.

INSTALLATION OPTIONS
--------------------

Microsoft® .NET Framework must be installed for the evaluation board software to run properly. Analog Devices Inc. provides both a web installer and full installer for evaluation software which can be downloaded from a specific product evaluation board page links located in the **Supported Products** section. The full installer is a larger file, which has Microsoft® .NET Framework embedded in the installer. The web installer is a smaller file which relies on an internet connection to download and install Microsoft® .NET Framework. Both installers will first check the user's machine to see if Microsoft® .NET Framework needs to be installed or updated.

Running the Software
~~~~~~~~~~~~~~~~~~~~

The evaluation software can be used with or without an evaluation board. Using the software without an evaluation board is useful for creating or verifying register settings for a given PLL setup without needing any hardware. When using the software with an evaluation board, power up and connect the board to the PC prior to starting the evaluation software. The evaluation board hardware is detailed on the evaluation boards specific product page in the **Evaluation Board Hardware** section.

-  Double-click appropriate AD95xx Evaluation Software icon to run the evaluation software. If the evaluation board was properly found by the software, the lower left hand corner of the Main Window (shown in **Figure 1**) will read "<fc #339933>AD95xx Evaluation Board \| SPI 3 -wire</fc>" in green. If the evaluation board was not found, the lower left hand corner of the screen will read "<fc #FF0000>No Hardware Connected!</fc>" in red.
-  If the evaluation board is found, proceed to the **Evaluation Software Components** section for details about using the software. If the evaluation board is not found, click **File > Select Hardware**. Select the appropriate evaluation board connected and press OK. The select hardware window is shown in **Figure 12**.

   -  The bottom left corner of the main window should now read "<fc #339933>AD95xx Evaluation Board \| SPI 3 -wire</fc>" in green.

See the individual product wikis for detailed information about specific device software.

TABS
----

This section describes the selectable tabs within the evaluation software GUI.

Block Diagram
~~~~~~~~~~~~~

The **Block Diagram** tab features the main interactive GUI interface as shown in **Figure 1**. This tab is also referred to as the **GUI Main Window**. Many blocks and sub windows are accessible through this tab.

Frequency Limits
~~~~~~~~~~~~~~~~

The **Frequency Limits** tab features specification limit excerpts from the individual product datasheet. These limits are used by the GUI block diagram to display if any frequency limits are being violated by the current user configuration. Please refer to the product datasheet for limit verification.

|

.. container:: centeralign

   | |image2|
   | *Figure 2. Frequency Limits Tab*


Pinout
~~~~~~

The **Pinout Tab** shows the pinout and pin descriptions of the product which is being evaluated. Please refer to the product datasheet for the most up to date version of the pinout and pin descriptions.

|

.. container:: centeralign

   | |image3|
   | *Figure 3. Pinout Tab*


EXPLANATION OF GUI FEATURES
---------------------------

Tool Tips
~~~~~~~~~

The clock evaluation software incorporates **Tool Tips** to all interactive blocks, pins, wires, buttons, check boxes and indicators. These **Tool Tips** give the user active feedback of the state of a component, the limits of a component, and instruction about how to interact with the component if applicable. **Tool Tips** are brought up by simply hovering the cursor over a component of interest. The images below show examples of **Tool Tips** when hovering over a reference divider block, wire, and VCO.

|

.. container:: centeralign


   ..

|tool_tip.png|

   | |Tool Tip_Wire.png|
   | |Tool Tip_VCOcal.png|
   | *Figure 4. Various Tool Tip Examples*


Latching Values Into Interactive Blocks and Text Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Values may be entered into a block or text field by clicking the appropriate item. When a block/text field is selected, a blue outline and cursor appears as shown in **Figure 5**. All items which require text input from the user require an **Enter** keystroke to latch the value into the software. If an evaluation board is connected, a change to a block's value followed by an **Enter** keystroke will automatically load the value into the active registers of the device. Text fields within child windows require for the **Load** button to be pressed for any text values to be loaded into the device.
| Automatic loading of user inputs can be disabled by unchecking the **Enable Auto IO Update** option within the **File**>\ **Options** menu.

|

.. container:: centeralign


   ..

|image4|

   | *Figure 5. Selecting a Block To Edit Text*


Highlighted and Grayed Blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Various blocks within the GUI are represented as active by highlighting the block(white background). A block that is inactive is represented by graying the block and text. Blocks that are able to be activated and deactivated are done so by simply clicking the block. If an evaluation board is connected and a block is deactivated within the GUI, the appropriate register settings are automatically written to the active registers of the device by default. **Figure 5** below shows four reference inputs, with only RefA and RefC active.
| Automatic loading of user inputs can be disabled by unchecking the **Enable Auto IO Update** option within the **File**>\ **Options** menu.
|

.. container:: centeralign

   |image5| *Figure 6. Active and Deactive Block Representation*


Active Frequency Calculation and Frequency Violation Indication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The interactive GUI within the **Block Diagram** tab allows the user to configure the product to many valid functioning and non functioning states. The GUI uses the independent variable information contained in each block's state and text box to calculate dependent frequencies throughout the device. The GUI actively monitors and displays when a device frequency specification is being violated by highlighting the unsupported component in <fc #FF0000>red</fc>. Errors are also displayed when when reference and feedback frequencies are not matched for a given PLL. **Figure 7** below shows a user configuration with many frequency errors.

.. container:: centeralign

   |image6| *Figure 7. Active Frequency Validation*


Frequency Limits Tab
^^^^^^^^^^^^^^^^^^^^

Frequency violations are also highlighted <fc #FF0000>red</fc> in the **Frequency Limits** tab. **Figure 8** shows an example of a maximum VCO frequency violation.

.. container:: centeralign

   |image7| *Figure 8. Active Frequency Validation in the Frequency Limits Tab*


VCO Calibration
~~~~~~~~~~~~~~~

A VCO calibration is issued by clicking on a VCO block within the GUI.

Expansion Windows
~~~~~~~~~~~~~~~~~

**Expansion Windows** are used to display small sections of a part at a time. Expansion windows allow the user to switch between multiple PLL channels or output banks for devices with large output distribution. Each window uses a different background color to represent a different section of the device. Selecting an **Expansion Window** does not reconfigure the device or alter blocks contained in other expansion windows. **Figure 9** shows the **Expansion Window** buttons for the AD9554 which allow the user to select one of four channels.

|

.. container:: centeralign


   ..

|image8|

   | *Figure 9. Expansion Window Buttons*


Main Window Buttons
~~~~~~~~~~~~~~~~~~~

The following buttons are available at the bottom of the evaluation software main window:

|

.. container:: centeralign


   ..

|image9|

   | *Figure 10. Main Window Buttons*


-  **Wizard** - Opens the product configuration wizard. Wizards are product specific and not available for every product. See the individual evaluation board user guide page for detailed instruction on using a wizard.
-  **Read All** - Reads all active registers from the clocking product and updates the GUI to reflect those values.
-  **Load All** - Loads all values from the GUI to the active registers of the clocking product.
-  **Control** - Opens a window with general operational controls. Individual controls vary from product to product.
-  **Status** - Opens a window which contains status indicators such as PLL lock and reference detection. Exact indicators and controls vary from product to product.
-  **Reg Map** - Opens the register map window. Clicking the **Register Map** button brings up a table of all current register settings loaded into the clock part. Expanding **Register Details** and clicking a specific register setting will show the details of that register at the bottom of the **Register Map** Window. This detailed view is also shown when hovering the mouse cursor over a register setting. There are three main tabs in the **Register Map** window including:

   -  **All** - Shows all current register settings.
   -  **Updated** - Shows all register settings which have been entered into the GUI but have not yet been written to the device.
   -  **NonDefault** -Shows all registers that have been changed from the on chip default values.

|

.. container:: centeralign


   ..

|image10|

   | *Figure 11. Register Map Window*


-  **SYNC** - Performs an output synchronization to phase align outputs.
-  **RESET** - Performs a software reset of the clock.

Tool Bar Menu
~~~~~~~~~~~~~

File
^^^^

The **File** menu contains the following options:

Setup Files
"""""""""""

-  **Load Setup File** - Loads a user created setup file (.stp) saved from a previous evaluation configuration. All register values listed in the .stp file are loaded into the software. An evaluation board does not need to be connected to load a configuration into the evaluation GUI.

-  **Save Setup File** - Saves a user created setup file. All default and non-default register settings are saved. An evaluation board does not need to be connected to save a .stp file.

-  **Save Setup File [Non-Defaults Only]** - Saves a user created setup file containing only registers that do not match the on chip defaults. An evaluation board does not need to be connected to save a .stp file.

-  **Include Detailed Setup Information** - Checking this box includes a detailed setup information header to a saved .stp file. This box is checked by default. Checking or unchecking this box has no affect on the software's interpretation of the setup file.

Select Hardware
"""""""""""""""

**Select Hardware** brings up a window to show all of the available ADI CSG evaluation boards that are currently connected to the users PC. Select the appropriate board for a given piece of evaluation software. **Figure 12** below shows an example of the Select Hardware Window using the AD9554 evaluation board.

|

.. container:: centeralign


   ..

|image11|

   | *Figure 12. Select Hardware Window*


Options
"""""""

-  **Enable Polling** - Checking this box allows the software to actively read from the clocking part on the evaluation board and updates the software with the most up to date active register settings. This box is checked by default.

-  **Polling Interval** - Opens a window to set the time interval of the evaluation board polling in milliseconds.

-  **Enable Auto IO Update** - Checking this box will issue an IO update after each user entry to automatically latch values from the GUI to the active registers of the clocking chip. This box is checked by default.

-  **Launch Wizard on Start Up** - Checking this box allows the configuration wizard to automatically appear at start up. This only applies to evaluation software which contains a configuration wizard.

Exit
""""

Exits the evaluation software.

View
^^^^

The **View** Menu contains the following options:

Register Map
""""""""""""

Selecting **Register Map** performs the same function as pressing the **Reg Map** button. See the **Main Window Buttons** section for more details.

Debug
"""""

Selecting **Debug** brings up the debug window which allows individual register writes and reads to be issued to the clocking product. Some product debug windows allow for individual digital IO pins to be toggled. See the individual evaluation user guide page for specific detail on the debug window.

About
^^^^^

Selecting **About** brings up a window which details the revision of the evaluation board software being used.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/main_window_example.png
   :width: 700px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/figure2_frequencylimitestab.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/figure3_pinouttab.png
   :width: 500px
.. |tool_tip.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/tool_tip.png
   :width: 300px
.. |Tool Tip_Wire.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/Tool Tip_Wire.png
   :width: 300px
.. |Tool Tip_VCOcal.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/Tool Tip_VCOcal.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/editing_a_text_box.png
   :width: 200px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/enablingblocks.png
   :width: 300px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/frequency_violation_indication.png
   :width: 500px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/frequency_violation_indication_freqlimtab.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/expansion_window.png
   :width: 300px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/mainwindowbuttonspng.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/viewregistermap.png
   :width: 500px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/csg_evb_software/selecthardwarewindow.png
   :width: 300px
