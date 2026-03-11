Virtual Control Interface
=========================

:doc:`Click here to return to the Using SigmaStudio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| The SigmaStudio virtual control interface provides a user customizable graphical interface to define a virtual hardware control for software tuning. A single user interface control can be configured to modify multiple software parameters simultaneously. Virtual Controls can emulate the behavior of a physical interface or external system controller. | |vci.png| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

| 
| **Key Features of the control interface are:**

-  User customizable GUI control interface (Knob, slider, button or switch)
-  Mapping of GUI control to algorithm parameters in a SigmaStudio schematic design
-  Define data value mapping tables to convert control values to parameters values
-  Fully integrated into the SigmaStudio development environment

.. important::

   This document describes the Virtual Control Interface (also known as “HMI”) of the SigmaStudio development environment. This feature provides a user configurable interface for multiple parameter control within the SigmaStudio development environment for system tuning and control emulation. The examples or explanations and any source-code contained in this document are provided to you “AS IS” without any warranties of any kind. The implied warranties of non-infringement, merchantability and fitness for a particular purpose are expressly disclaimed.

   


Installation
------------

The Virtual Control Interface requires **SigmaStudio version 3.7.7** or later. The ALPHA version is distributed separately from the SigmaStudio installation software.

Files required: **VirtualInterface.dll**

-  To install, copy the “VirtualInterface.dll” file into the SigmaStudio installation directory (typically C:\\Program Files\\Analog Devices\\SigmaStudio 3.7). Note this step may require that your Windows user account has administrative privileges.
-  Either: (a) Restart SigmaStudio OR (b) Select the “Tools \| Add-Ins Browser…” menu, click “Add DLL” button, choose the VirtualInterface.dll file copied in step one, and press the “Save” button.
-  Create a New project or open an existing SigmaStudio project file.
-  The “Control UI” cell is available in the “Processors” folder of the Hardware Configuration toolbox.

Getting Started
---------------

Drag and drop the “Control UI” cell from the Toolbox into the Hardware Configuration tab of a SigmaStudio project.


|vci1.png|

**Control Interface:** Open the Virtual Control Window by click the “Show…” button or right click on the control interface cell and select “Control Window” from the menu.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci2.png
   :alt: vci2.png
   :align: center

The Control Window consists of 10 control cells. Each cell can contain a virtual user control, a knob, a slider, a button or a switch.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci3.png
   :alt: vci3.png
   :align: center

Define a Virtual Control
------------------------

There are 3 steps to creating and configuring a virtual UI control:

-  Create a GUI Control (Knob, Slider, button or switch)
-  Assign one or more schematic parameters to the GUI Control
-  Define a value mapping table for each assigned parameter

**Create a Control:** To create a control Click the arrow in a control cell or right click on a cell and choose a control type from the “Insert…” menu.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci4.png
   :alt: vci4.png
   :align: center

A control of the selected type is created in the control window cell.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci5.png
   :alt: vci5.png
   :align: center

**Define Control Properties:** Name: Each Virtual control has a Label which is user editable. To rename a control, double click the name label under the control and enter a new name.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci6.png
   :alt: vci6.png
   :align: center

Values: The control’s minimum and maximum display value and value resolution (“step”) can be modified. To change the control’s values, right click on the control and control the desired values in the properties window.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci7.png
   :alt: vci7.png
   :align: center

Note the mapping between a virtual control’s value and an assigned parameter is defined via lookup tables as described below. The min, max, and step settings of the virtual control have no direct relationship to the parameter lookup tables; the parameter lookup index is calculated dynamically accordingly to the position between min and max. Meaning, you can set the GUI range to any arbitrary range of values per your preference, internally the control range is converted to a linear map of lookup table indices.

Assign Parameters
-----------------

One or more schematic cell algorithm parameters can be assigned to a virtual control. To assign a parameter for control, click on the control cell arrow or right click on the control cell and select “Assign…” from the menu. This will open the parameter assignment dialog.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci8.png
   :alt: vci8.png
   :align: center

The “Assign Parameter Control” dialog lists all parameters in a SigmaStudio schematic project that are available for control. They are organized according to schematic hierarchy and cell name.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci9.png
   :alt: vci9.png
   :align: center

Select the check box next to one or more parameters to assign them to the Virtual Interface control.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci10.png
   :alt: vci10.png
   :align: center

When selection is complete, press the “Assign” button to commit the parameter control assignment operation.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci11.png
   :alt: vci11.png
   :align: center

Parameter assignment will automatically open the *Value Conversion Table Editor* window.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci12.png
   :alt: vci12.png
   :align: center

Value Conversion Table Editor
-----------------------------

A value conversion table must be defined for each assigned parameter. The Virtual Control (knob or slider) value is converted to an integer index between 0 and the number of “Steps” defined for the lookup table. Schematic parameter values are set according to the values defined for each step in the virtual control lookup table.

The Value Conversion Table Editor window can be opened at any time by clicking the arrow in a control cell or by right clicking and selecting “Properties…” from the menu.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci13.png
   :alt: vci13.png
   :align: center

**How to define the Parameter Conversion Tables**

**Step-1:** Set the number of “Steps” for the parameter lookup tables (default table size is 16). The lookup table step size applies to all parameters assigned to the Virtual Control and a conversion table must be defined for each assigned parameter.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci14.png
   :alt: vci14.png
   :align: center

**Step-2:** Define a value for each parameter at each step in the conversion table. To edit a table value, double click on a cell in the table window.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci15.png
   :alt: vci15.png
   :align: center

**Step-3:** Press “OK” to commit the parameter table value assignment.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci16.png
   :alt: vci16.png
   :align: center

**Table Import/Export:**

All values in the parameter conversion table editor window can be Imported from or exported to a text file. To import table data, click the “Import…” button in the Table Editor window, and to export the table data, click the “Export…” button.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci17.png
   :alt: vci17.png
   :align: center

The text file format is CSV (comma separated values) where each table column is enclosed in curly braces, for example a file with two parameter columns:

::

       {0, -5, -7, -9, -12, -15, -18, -24, -28, -30, -32, -36, -40, -44, -50, -60 },
       {-60, -50, -44, -40, -36, -32, -30, -28, -24, -18, -15, -12, -9, -7, -5, 0 },

If the data file contains less data than the defined table ‘Steps’, zeros are inserted for any undefined indices. If the file contains more data than the defined table Steps, only the first n-step values are imported and the excess data is ignored.

**Table Column Commands:** Right click on a value conversion table column to open the table commands menu.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci18.png
   :alt: vci18.png
   :align: center

Each column in the table editor represents the value mapping for a single parameter in the schematic design. The following editing commands are supported for each parameter table column:

+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Copy Column Data:**  | Copies a single table column’s value to the clipboard. A table can be copied and pasted between columns in the editor window.                                     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Paste Column Data:** | Paste column data from the clipboard.                                                                                                                             |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Import Column:**     | Import table values into a single column from a text file. Supported formats are CSV (comma separated values) or line break separated values.                     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Export Column:**     | Export the values form a table column to a text file (export format is a single table value on each line in the file, the standard for SigmaStudio value tables). |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Invert:**            | Invert the values of the column (i.e. swap values at indices 0 and max steps).                                                                                    |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Usage
-----

The Virtual controls, settings, and value mappings are saved in a SigmaStudio project file. The virtual control will modify the value of the assigned parameters simultaneously and can be used during design tuning. Note that the virtual control is a SigmaStudio user interface object only, and does not generate any additional DSP assembly code or directly affect the final program.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci19.png
   :alt: vci19.png
   :align: center

The control and value mapping is One-Way, from the virtual control to the assigned parameter control. The virtual control will set the value of all assigned schematic controls when changed. However, setting the value of an assigned parameter directly in the schematic view does NOT update the value(s) of the virtual control or other assigned parameters.

**Capture Window Bypass**

The Virtual Control Interface bypasses the capture window for UI efficiency (a large number of parameter write operations are generated for each increment of a Virtual Control). For this reason control changes from the Virtual Control Interface window are not shows in the capture window even though the values are being written to the USB interface.

Known Issues
------------

ALPHA v1.0
~~~~~~~~~~

-  Schematic view name changes, both hierarchy boards or algorithm cells will not update the Virtual Interface Control and assignment is lost. All renamed cell(s) must be manually re-assigned to the virtual control. (will be addressed in 1.1 release).
-  Virtual Interface assignment is only available for cell GUI controls (algorithm parameters without a schematic view GUI control cannot be assigned). Also a cell’s GUI parameters must support the UI “settings” feature of SigmaStudio (some legacy cells and interim custom cells may not support this feature). Can be addresses on a case-by-case basis as needed.

.. |vci.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci.png
.. |vci1.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/vci1.png
