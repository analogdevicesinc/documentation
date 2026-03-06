CrossCore Embedded Studio(CCES) Quick Start for Windows
=======================================================

This page is designed to show how to quickly get connected to Analog Devices evaluation boards using CCES.

Hardware Connection Types
-------------------------

There are usually 2 ways to connect to ADI evaluation boards. An In Circuit Emulator(ICE), such as the ICE-1000 or ICE-2000 can be used or some ADI evaluation boards support a direct connection to the board using an on-board debug agent. In both cases, the communication between the host PC and the hardware is USB.

.. tip::

   
   For information on hardware connections, how to to power up evaluation boards, or switch settings to allow for emulator/debug agent connection, please see the appropriate hardware documentation.
   


CCES Setup - On-board Debug Agent
---------------------------------

Follow these instructions to ensure correct operation of the product software and hardware.

Connect the board to a personal computer (PC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Plug one side of the USB cable into the evaluation board. Plug the other side into a USB port of the PC running CCES.
-  Attach power to the evaluation board unless the evaluation board is USB bus powered.

The following steps assume that CCES is installed and running on your PC.

.. important::

   Connecting the USB cable between the PC and the carrier board prior to installing CCES may result in a failure to find the appropriate Windows drivers.


-  Navigate to the CCES environment through the Start menu.
-  Once an application is ready to load to the evaluation board a debug configuration can be created.

Launching the Debug Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the **Debug Configurations** wizard to connect to the board. If a debug configuration exists already, select the appropriate configuration and click *Debug*.


|image1|

.. important::

   Be sure to select your project in the project explorer so that important details are filled in for you automatically when creating the Debug Configuration.


-  To create a debug configuration, choose Run > Debug Configurations
-  The Debug Configuration dialog box will appear.

Creating a New Debug Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/create_debug_config_da.gif

-  Select **Application with CrossCore Debugger** and click the *New* button to create a configuration.
-  The **Select Processor** page of the Session Wizard appears.
-  On the **Select Processor** page, ensure the correct processor family is selected.
-  In *Processor type*, select the processor that matches the processor on the evaluation board. Click *Next*.
-  On the **Connection Type** page, select *EZ-KIT Lite* for on-board debug agent use.
-  Choose the on-board debug agent.
-  Click *Finish* to close the wizard. The new debug configuration is created and added to the Debug Configurations list.

Selecting the Application(s) to Load
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/select_application.gif

-  In the **Name** edit box, select an appropriate name to describe the configuration, otherwise a default name is provided.
-  In the **Session** section, choose the program(s) to load (if the appropriate program is not already populated) when connecting to the board.
-  If not loading any program upon connection to the target, do not make any changes.
-  Click *Debug* to connect to the target board.

.. important::

   While connected to the target, there is no way to choose a program to download. To load a program once connected, terminate the session and then load the new program.


-  To disconnect from the target board, choose *Run > Terminate*.
-  To delete a configuration, go to the **Debug Configurations** dialog box and select the *Delete* button and choose *Yes* when asked if you wish to delete the selected launch configuration. Then Close the dialog box.

CCES Setup - ICE-1000/ICE-2000 Emulator
---------------------------------------

Follow these instructions to ensure correct operation of the product software and hardware.

.. _connect-the-board-to-a-personal-computer-pc-1:

Connect the board to a personal computer (PC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Plug one side of the USB cable into the emulator. Plug the other side into a USB port of the PC running CCES.
-  Attach power to the evaluation board unless the evaluation board is USB bus powered.

The following steps assume that CCES is installed and running on your PC.

.. important::

   Connecting the USB cable between the PC and the emulator prior to installing CCES may result in a failure to find the appropriate Windows drivers.


-  Navigate to the CCES environment through the Start menu.
-  Once an application is ready to load to the evaluation board a debug configuration can be created.

.. _launching-the-debug-configuration-1:

Launching the Debug Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the **Debug Configurations** wizard to connect to the board. If a debug configuration exists already, select the appropriate configuration and click *Debug*.


|image2|

.. important::

   Be sure to select your project in the project explorer so that important details are filled in for you automatically when creating the Debug Configuration.


-  To create a debug configuration, choose Run > Debug Configurations
-  The Debug Configuration dialog box will appear.

.. _creating-a-new-debug-configuration-1:

Creating a New Debug Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/create_debug_config_emu.gif

-  Select **Application with CrossCore Debugger** and click the *New* button to create a configuration.
-  The **Select Processor** page of the Session Wizard appears.
-  On the **Select Processor** page, ensure the correct processor family is selected.
-  In *Processor type*, select the processor that matches the processor on the evaluation board. Click *Next*.
-  On the **Connection Type** page, select *Emulator*.
-  Choose the type of emulator connected.
-  Click *Finish* to close the wizard. The new debug configuration is created and added to the Debug Configurations list.

.. _selecting-the-applications-to-load-1:

Selecting the Application(s) to Load
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/select_application_emu.gif

-  In the **Name** edit box, select an appropriate name to describe the configuration, otherwise a default name is provided.
-  In the **Session** section, choose the program(s) to load (if the appropriate program is not already populated) when connecting to the board.
-  If not loading any program upon connection to the target, do not make any changes.
-  Click *Debug* to connect to the target board.

.. important::

   While connected to the target, there is no way to choose a program to download. To load a program once connected, terminate the session and then load the new program.


-  To disconnect from the target board, choose *Run > Terminate*.
-  To delete a configuration, go to the **Debug Configurations** dialog box and select the *Delete* button and choose *Yes* when asked if you wish to delete the selected launch configuration. Then Close the dialog box.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/launch_debug_config.gif
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/launch_debug_config.gif
