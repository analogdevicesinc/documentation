:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Getting Started with SigmaStudio Scripting Helper Extension
===========================================================

This guide will walk you through installing and using the SigmaStudio Scripting Helper extension for Visual Studio Code. This extension accelerates your SigmaStudio+ scripting workflow with intelligent API suggestions, live parameter completion, and real-time project data integration.

| 
| ===== Table of Contents =====

-  `Prerequisites <https://wiki.analog.com/>`__
-  `Installing Visual Studio Code <https://wiki.analog.com/>`__
-  `Installing the Extension <https://wiki.analog.com/>`__
-  `Connecting to SigmaStudio+ <https://wiki.analog.com/>`__
-  `Troubleshooting Connection Issues <https://wiki.analog.com/>`__
-  `Using Intelligent Suggestions <https://wiki.analog.com/>`__
-  `On-the-Fly Documentation <https://wiki.analog.com/>`__

| 
| ===== Prerequisites ===== Before you begin, ensure you have:

-  **SigmaStudio+ Application** installed and running

   -  The extension requires SigmaStudio+ to be active for live parameter suggestions
   -  RPC server should be enabled (default port: 9090)

-  **Python** installed (if working with Python scripts)

   -  **Recommended version: Python 3.12.x or later**
   -  Minimum supported: Python 3.6 or later

-  **Jupyter Extension for VS Code** (recommended for working with examples)

   -  VS Code natively supports Jupyter notebooks
   -  If your VS Code installation doesn't include it, install from:
   -  `Jupyter Extension <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>`__
   -  Required for running ``.ipynb`` example files

-  **VSIX File Location**

   -  The extension VSIX file is included with your SigmaStudio+ installation at:
   -  ``C:\Analog Devices\SigmaStudioPlus-<version>\Examples\ScriptingClient\``
   -  Example: ``C:\Analog Devices\SigmaStudioPlus-Rel3.4.0\Examples\ScriptingClient\sigmastudio-scripting-helper.vsix``

| 
| ===== Installing Visual Studio Code ===== If you don't have Visual Studio Code installed:

Download VS Code
----------------

-  Visit: `Download VS Code <https://code.visualstudio.com/download>`__
-  Choose the appropriate version for your operating system (Windows, macOS, or Linux)

Install VS Code
---------------

-  **Windows**: Run the downloaded ``.exe`` installer and follow the setup wizard
-  **macOS**: Open the ``.dmg`` file and drag VS Code to the Applications folder
-  **Linux**: Follow the distribution-specific instructions on the download page

Launch VS Code
--------------

-  Open Visual Studio Code after installation completes

| 
| ===== Installing the Extension =====

Option 1: Install via VS Code UI (Recommended)
----------------------------------------------

.. image:: https://wiki.analog.com/_media/offcfg/installation.gif
   :align: left
   :width: 400px

-  **Open Extensions View**

   -  Press ``Ctrl+Shift+X`` (Windows/Linux) or ``Cmd+Shift+X`` (macOS)
   -  Or click the Extensions icon in the Activity Bar (left sidebar)

-  **Install from VSIX**

   -  Click the ``...`` menu (three dots) at the top right of the Extensions panel
   -  Select **"Install from VSIX..."**

-  **Browse to the VSIX File**

   -  Navigate to: ``C:\Analog Devices\SigmaStudioPlus-<version>\Examples\ScriptingClient\``
   -  Select the ``sigmastudio-scripting-helper.vsix`` file
   -  Click **"Install"**

-  **Reload VS Code**

   -  Click **"Reload"** when prompted, or restart VS Code manually

Option 2: Install via Command Line
----------------------------------

Open a terminal/command prompt and run:

.. code:: bash

   code --install-extension "C:\Analog Devices\SigmaStudioPlus-<version>\Examples\ScriptingClient\sigmastudio-scripting-helper.vsix"

Replace ``<version>`` with your actual SigmaStudio+ version number.

Verify Installation
-------------------

-  **Look for the Extension Icon**

   -  Check the Activity Bar (left sidebar) for the **SigmaStudio Helper** icon
   -  It should appear alongside other icons like Explorer, Search, Source Control, etc.

-  **Open a Python File**

   -  Create or open a ``.py`` file
   -  The extension activates automatically when Python files are opened

-  **Check Extension is Active**

   -  Press ``Ctrl+Shift+P`` (Windows/Linux) or ``Cmd+Shift+P`` (macOS)
   -  Type "SigmaStudio Helper"
   -  You should see extension commands listed

| 
| ===== Video Tutorial for First-Time Users ===== If you're new to using Jupyter notebooks in Visual Studio Code, we recommend watching this tutorial:

**📺 Getting Started with Jupyter Notebooks in VS Code**

-  **YouTube Link**: `Watch on YouTube <https://www.youtube.com/watch?v=suAkMeWJ1yE&pp=ygUoZ2V0dGluZyBzdGFydGVkIHZzIGNvZGUganVweXRlciBub3RlYm9vaw%3D%3D>`__
-  This tutorial covers:

   -  Setting up Jupyter in Visual Studio Code
   -  Creating and running Jupyter notebooks
   -  Working with cells and executing code
   -  Using notebooks for interactive development

This knowledge will help you make the most of the SigmaStudio+ example scripts provided in Jupyter format.

| 
| ===== Connecting to SigmaStudio+ ===== The extension needs to connect to SigmaStudio+ to provide live parameter suggestions and real-time project data.

Step 1: Ensure SigmaStudio+ is Running
--------------------------------------

-  Launch **SigmaStudio+ Application**
-  Configure the RPC server port:

   -  Go to **Tools** > **Settings**
   -  Navigate to **SigmaStudio+ Scripting** section
   -  Check the port number (default: **9090**)
   -  Change the port if required as per your configuration
   -  Click **Configure Port** to apply the settings

-  Note the configured server port for use in VS Code extension settings

Step 2: Configure Connection Settings
-------------------------------------

Method A: Using the Sidebar (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Open SigmaStudio Helper Sidebar**

   -  Click the **SigmaStudio Helper** icon in the Activity Bar (left sidebar)

-  **Configure Settings**

   -  In the **Settings** panel, you'll see:

      -  **Server IP**: Default is ``127.0.0.1`` (for local connections)
      -  **Server Port**: Default is ``9090``

-  **Edit Settings (if needed)**

   -  Click on "**Server IP**" to change the IP address
   -  Click on "**Server Port**" to change the port number
   -  For local SigmaStudio+ instances, the defaults usually work

Method B: Using VS Code Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Open Settings**

   -  Press ``Ctrl+,`` (Windows/Linux) or ``Cmd+,`` (macOS)
   -  Or go to ``File > Preferences > Settings``

-  **Search for SigmaStudio Helper**

   -  Type "SigmaStudio Helper" in the search bar

-  **Configure Connection Settings**

   -  **SigmaStudioHelper: Server Ip Address**: Enter ``127.0.0.1`` (or remote IP if applicable)
   -  **SigmaStudioHelper: Server Port**: Enter ``9090`` (or your custom port)

Step 3: Connect to SigmaStudio+
-------------------------------

-  **Open Connection Status Panel**

   -  Click the **SigmaStudio Helper** icon in the Activity Bar
   -  Locate the **Connection Status** panel

-  **Click Connect**

   -  Click on "**Connect**" in the Connection Status panel
   -  Or use Command Palette: ``Ctrl+Shift+P`` → "**SigmaStudio Helper: Connect to SigmaStudio+**"

-  **Verify Connection**

   -  Status should change to: **✅ Connected**
   -  Server info displays: ``127.0.0.1:9090`` (or your configured address)

-  **Test Connection (Optional)**

   -  Click "**Test Connection**" to verify data can be fetched
   -  You should see a success message confirming connection

Step 4: Plugin Data Loading
---------------------------

Once connected:

-  The extension automatically loads plugin data from SigmaStudio+
-  Check the **Plugin Manager** panel to see cache status
-  Should show: "**Cached: 16/16 plugins**" (or similar)
-  If not loaded, click "**Refresh Plugins**" in the Plugin Manager panel

| 
| ===== Troubleshooting Connection Issues =====

Issue 1: Connection Failed / Cannot Connect
-------------------------------------------

**Symptoms:**

-  Status shows: **❌ Error** or **Connection Failed**
-  Error message: "Failed to connect to 127.0.0.1:9090"

**Solutions:**

-  **Verify SigmaStudio+ is Running**

   -  Make sure the SigmaStudio+ application is open and active
   -  Check that the RPC server is enabled in SigmaStudio+ preferences

-  **Check IP Address and Port**

   -  Default IP: ``127.0.0.1`` (for local connections)
   -  Default Port: ``9090``
   -  If SigmaStudio+ uses a different port, update the settings accordingly

-  **Test Port Availability**

   -  Open Command Prompt or PowerShell
   -  Run: ``netstat -an

   | findstr 9090`` (Windows)
   -  Verify SigmaStudio+ is listening on port 9090

-  **Firewall and Security Software**

   -  Check if firewall is blocking the connection
   -  Add exception for VS Code and SigmaStudio+ if necessary
   -  Temporarily disable antivirus to test (re-enable after testing)

-  **Try Alternative IP Address**

   -  If ``127.0.0.1`` doesn't work, try ``localhost``
   -  Settings panel → Edit Server IP → Enter ``localhost``

Issue 2: Connected but No Suggestions Appearing
-----------------------------------------------

**Symptoms:**

-  Status shows: **✅ Connected**
-  No auto-complete suggestions when typing API functions

**Solutions:**

-  **Check Plugin Cache**

   -  Open **Plugin Manager** panel in the sidebar
   -  Verify cache status shows plugins loaded (e.g., "Cached: 16/16")
   -  If cache is empty, click "**Refresh Plugins**"

-  **Verify Extension Settings**

   -  Open Settings (``Ctrl+,``)
   -  Search for "SigmaStudio Helper"
   -  Ensure **Enable Auto Completion** is checked (enabled)
   -  Ensure **Show Parameter Hints** is checked (enabled)

-  **Test with a Python File**

   -  Create a new ``.py`` file
   -  Type a function name: ``AddShape(``
   -  Press ``Ctrl+Space`` to trigger suggestions manually
   -  You should see parameter suggestions appear

Issue 3: Wrong or Outdated Suggestions
--------------------------------------

**Symptoms:**

-  Suggestions show old data
-  Missing new shapes/modules added to project

**Solutions:**

-  **Refresh Canvas Data**

   -  Command Palette (``Ctrl+Shift+P``) → "**SigmaStudio Helper: Refresh Canvas Data**"
   -  This updates canvas and element information from SigmaStudio+

-  **Refresh Plugin Data**

   -  Click "**Refresh Plugins**" in the Plugin Manager panel
   -  Or Command Palette → "**SigmaStudio Helper: Refresh Plugins**"

-  **Reconnect to SigmaStudio+**

   -  Disconnect: Click "**Disconnect**" in Connection Status panel
   -  Wait 2-3 seconds
   -  Connect: Click "**Connect**" again

Issue 4: Extension Not Activating
---------------------------------

**Symptoms:**

-  No SigmaStudio Helper icon in Activity Bar
-  Extension commands not available

**Solutions:**

-  **Verify Extension is Installed**

   -  Open Extensions view (``Ctrl+Shift+X``)
   -  Search for "SigmaStudio"
   -  Check if "SigmaStudio Scripting Helper" appears in the list
   -  If not installed, repeat installation steps

-  **Check Extension is Enabled**

   -  In Extensions view, find "SigmaStudio Scripting Helper"
   -  Ensure it's not disabled (should show "Disable" button, not "Enable")
   -  If disabled, click "Enable" button

-  **Reload VS Code**

   -  Command Palette (``Ctrl+Shift+P``) → "**Reload Window**"
   -  Or fully restart VS Code

-  **Check Python File is Open**

   -  Extension activates only when Python files are opened
   -  Create or open a ``.py`` file to trigger activation

Issue 5: Slow Performance
-------------------------

**Symptoms:**

-  Suggestions appear slowly
-  VS Code feels sluggish when typing

**Solutions:**

-  **Reduce Auto-Refresh Frequency**

   -  Canvas/element data refreshes on each parameter trigger
   -  Consider manually refreshing only when needed

-  **Use Offline Mode**

   -  If you don't need live data, disconnect from SigmaStudio+
   -  Extension works with cached plugin data for basic suggestions

-  **Check Network Latency**

   -  If connecting to remote SigmaStudio+ instance, network latency may cause delays
   -  Consider using a local instance for better performance

|

| ===== Using Intelligent Suggestions ===== The extension provides smart auto-completion for 21+ parameter types. Here's how to use them:

Basic Auto-Completion
---------------------

-  **Start Typing a Function**

.. code:: python

   AddShape(

-  **Trigger Suggestions**

   -  Suggestions appear automatically as you type
   -  Or press ``Ctrl+Space`` to manually trigger

-  **Select from Suggestions**

   -  Use arrow keys to navigate suggestions
   -  Press ``Enter`` or ``Tab`` to accept a suggestion
   -  Press ``Esc`` to dismiss suggestions

Shape Name Suggestions
----------------------

When typing shape parameters, you'll see:

.. code:: python

   AddShape(shapeFullName="
   # → Auto-complete shows all available plugin shapes
   # Example: AnalogDevices.Plugins.Communication.USBi_v1.0.0.0

**Features:**

-  **Full Names**: Complete plugin paths
-  **Short Names**: Trimmed versions (e.g., ``USBi``)
-  **Search**: Type partial name to filter suggestions

Canvas and Element Suggestions
------------------------------

Get live data from your SigmaStudio+ project:

.. code:: python

   GetCanvasElements(parentUid="
   # → Shows all canvases in your current project (e.g., Diagram_0, Diagram_1)

   GetCanvasElements(parentUid="Diagram_0", elementUid="
   # → Shows only elements in Diagram_0 (filtered and refreshed live)

**Features:**

-  **Live Data**: Fetched from SigmaStudio+ in real-time
-  **Context Aware**: Suggestions filtered based on previous parameters
-  **Smart Refresh**: Data updates automatically when needed

Pin Suggestions (with ◈ Icon)
-----------------------------

Extension automatically detects the module and fetches its pins:

.. code:: python

   AddConnectionV2(sourceUid="USBi_0", sourcePin="
   # → Shows pins from USBi_0 module with ◈ icon
   # Example: Input1, Input2, Output1, etc.

   AddConnectionV2(..., targetUid="EVALADAU1466Z_0", targetPin="
   # → Shows pins from EVALADAU1466Z_0 module

**Features:**

-  **Automatic Detection**: Reads module UID from same line
-  **Live Fetch**: Gets current pin definitions from SigmaStudio+
-  **Visual Icons**: ◈ icon distinguishes pin parameters

Property Name and Value Suggestions
-----------------------------------

Work with module properties efficiently:

.. code:: python

   Read(elementUid="USBi_0", propertyName="
   # → Shows available properties with ⬜ icon
   # Example: SampleRate, BitDepth, Enabled, etc.

   Read(elementUid="USBi_0", propertyName="SampleRate", propertyVal="
   # → Shows current value with type: "64 (Int32)"

**Features:**

-  **Property Names**: ⬜ icon for property identifiers
-  **Property Values**: Shows current value and data type
-  **Dual Validation**: Ensures property exists before suggesting values

Position Object Suggestions
---------------------------

Get template for coordinate objects:

.. code:: python

   MoveShape(shapeUid="USBi_0", newPosition=
   # → Inserts position object template: {"X": 0, "Y": 0}

**Features:**

-  **Template Insertion**: Pre-formatted position objects
-  **Easy Editing**: Modify X/Y values as needed

| 
| ===== On-the-Fly Documentation ===== The extension provides instant documentation without leaving your editor.

Hover Information
-----------------

Hover over shape names or parameters to see documentation:

.. code:: python

   shape = "AnalogDevices.Plugins.Communication.USBi_v1.0.0.0"
   # Hover over the text → "✅ Available in cached plugin data"

**What You'll See:**

-  **Validation Status**: ✅ if shape exists, ❌ if not found
-  **Data Source**: Indicates if from cache or live data
-  **Additional Info**: Type information, current values, etc.

Parameter Hints
---------------

As you type function parameters, hints appear showing:

-  **Parameter Names**: What each parameter expects
-  **Parameter Types**: Data type (string, number, object, etc.)
-  **Examples**: Sample values you can use

API Reference Sidebar
---------------------

Access comprehensive API documentation:

-  **Open SigmaStudio Helper Sidebar**

   -  Click the SigmaStudio Helper icon in Activity Bar

-  **Navigate to API Reference Panel**

   -  Browse all available SigmaStudio+ APIs
   -  Categories: Project, Shape, Connection, Property, etc.

-  **View Function Details**

   -  Click on any API function
   -  See parameters, return types, and examples

-  **Insert Example Code**

   -  Click "Insert Code" button
   -  Example code is inserted at your cursor position

Inline Documentation Popup
--------------------------

Press ``Ctrl+K Ctrl+I`` (or ``Cmd+K Cmd+I`` on macOS) while your cursor is on a function name to see:

-  **Function Signature**: Complete parameter list
-  **Description**: What the function does
-  **Parameters**: Detailed parameter information
-  **Return Type**: What the function returns
-  **Examples**: Usage examples

Command Palette Quick Reference
-------------------------------

Access documentation commands quickly:

-  ``Ctrl+Shift+P`` → "**SigmaStudio Helper: Open API Reference**"
-  Shows searchable API browser with full documentation

| 
| ===== Next Steps ===== Now that you're set up, explore these features:

-  **Browse and Run Example Scripts** 📚

Opening the Example Scripts Panel
---------------------------------

-  **Open SigmaStudio Helper Sidebar**

   -  Click the **SigmaStudio Helper** icon in the Activity Bar (left sidebar)
   -  Look for the **Example Scripts** panel in the sidebar

-  **Browse Available Examples**

   -  You'll see a list of example scripts organized by category
   -  Each example is available in two formats:

      -  **Jupyter Notebook** (``.ipynb``) - Recommended for experimenting
      -  **Python Script** (``.py``) - For direct execution

How to Copy and Open Examples
-----------------------------

-  **Select an Example**

   -  Browse through the list of examples in the Example Scripts panel
   -  Click on an example that matches your use case

-  **Copy to Your Workspace**

   -  Click the **"Copy to Workspace"** button next to the example
   -  Or right-click the example and select **"Copy to Workspace"**
   -  The example file will be copied to your current workspace folder
   -  The complete **PythonClient SDK** is automatically included with each example

-  **Locate the Copied File**

   -  The file appears in your workspace's file explorer
   -  Look for ``.ipynb`` (Jupyter) or ``.py`` (Python) files
   -  VS Code will automatically open the file after copying

How to Run Jupyter Notebook Examples (Recommended)
--------------------------------------------------

-  **Open the Notebook**

   -  Double-click the ``.ipynb`` file in your workspace
   -  VS Code opens the notebook in Jupyter notebook editor

-  **Select Python Kernel**

   -  Click **"Select Kernel"** in the top-right corner (if prompted)
   -  Choose your Python environment (Python 3.12.x recommended)
   -  If no kernels appear, ensure Jupyter extension is installed

-  **Run the Notebook**

   -  **Run All Cells**: Click the **▶▶ "Run All"** button at the top
   -  **Run Individual Cells**: Click the **▶ Play** button next to each cell
   -  **Run Current Cell**: Press **Shift+Enter** while cursor is in a cell

-  **Watch Execution**

   -  Each cell executes sequentially
   -  Outputs appear directly below each cell
   -  Errors are highlighted inline for easy debugging

-  **Modify and Re-run**

   -  Edit any cell to change parameters or add your own code
   -  Re-run individual cells to test changes immediately
   -  Use auto-completion features while editing (press Ctrl+Space)

How to Run Python Script Examples
---------------------------------

-  **Open the Script**

   -  Double-click the ``.py`` file in your workspace
   -  VS Code opens the file in the Python editor

-  **Run the Script**

   -  **Method 1**: Right-click in the editor → **"Run Python File in Terminal"**
   -  **Method 2**: Click the **▶ Play** button in the top-right corner
   -  **Method 3**: Open terminal and run: ``python filename.py``

-  **View Output**

   -  Output appears in the integrated terminal at the bottom
   -  Errors and exceptions are displayed in the terminal

-  **Modify and Re-run**

   -  Edit the script to customize behavior
   -  Save the file (Ctrl+S)
   -  Run again to see changes take effect

Understanding the Examples
--------------------------

Each example demonstrates specific SigmaStudio+ operations:

-  **Connection Required**: Most examples require active connection to SigmaStudio+
-  **Step-by-Step**: Code is organized in logical steps with comments
-  **Reusable**: Use examples as templates for your own automation scripts
-  **SDK Included**: PythonClient SDK is automatically available in each example

What Do the Examples Demonstrate?
---------------------------------

The example scripts cover a wide range of SigmaStudio+ automation tasks:

-  **Project Management**: Creating new projects, opening existing ones, saving and compiling
-  **Adding Components**: Inserting modules, plugins, and shapes onto the canvas
-  **Making Connections**: Connecting modules, working with pins and signals
-  **Property Management**: Reading and writing module properties, configuring parameters
-  **Canvas Operations**: Moving shapes, organizing layouts, managing multiple canvases
-  **Advanced Workflows**: Complete automation scenarios combining multiple operations

Using Jupyter Notebooks (Recommended)
-------------------------------------

**We highly recommend using Jupyter notebooks (``.ipynb`` files) for experiment and development:**

-  **Cell-Based Structure**: Execute code in small, manageable chunks
-  **Runtime Validation**: Test each operation immediately and see results before proceeding
-  **Interactive Development**: Modify and re-run individual cells without restarting your entire script
-  **Visual Feedback**: See outputs, errors, and results directly inline
-  **Documentation**: Mix code with markdown explanations for better understanding
-  **Debugging**: Easier to isolate and fix issues cell-by-cell

-  **Explore Plugin Manager**

   -  View all cached plugins
   -  Export plugin data for inspection
   -  Manually refresh when needed

-  **Customize Settings**

   -  Fine-tune auto-completion behavior
   -  Adjust connection settings
   -  Toggle features on/off as needed

| 
| ===== Getting Help ===== If you encounter issues not covered in this guide:

-  **Contact Support**

   -  Describe steps to reproduce the issue
   -  Include SigmaStudio+ version and VS Code version

| 
| ===== Quick Reference =====

Essential Keyboard Shortcuts
----------------------------

===================== ================= ===============
Action                Windows/Linux     macOS
===================== ================= ===============
Trigger Auto-Complete ``Ctrl+Space``    ``Cmd+Space``
Command Palette       ``Ctrl+Shift+P``  ``Cmd+Shift+P``
Extensions View       ``Ctrl+Shift+X``  ``Cmd+Shift+X``
Settings              ``Ctrl+,``        ``Cmd+,``
Hover Info            ``Ctrl+K Ctrl+I`` ``Cmd+K Cmd+I``
===================== ================= ===============

Connection Quick Check
----------------------

**Everything Working:**

-  Status: ✅ Connected
-  Plugin Manager: Cached 16/16 plugins
-  Suggestions appear when typing

**Issues:**

-  Status: ❌ Error or ⚫ Disconnected
-  No suggestions appearing
-  → See `Troubleshooting <https://wiki.analog.com/>`__

| 
| **Happy Scripting!**
