SOFTWARE OVERVIEW
=================

INSTALLING THE ETHERNET PHY SOFTWARE
------------------------------------

The Ethernet PHY software GUI requires the installation of the Ethernet PHY software and the installation of the FTDI USB drivers. Both installations must be complete before connecting the EVAL-ADIN1100FMCZ to the USB port of the PC to ensure that the evaluation system is properly recognized when connected to the PC. First, install the Ethernet PHY software and the associated documentation. The installation steps are listed in the following section. The default location for the Ethernet PHY software GUI installation is the C:\\Analog Devices\\ADIN1100 folder. When the Ethernet PHY software installation is complete, install the USB communications drivers. The EVAL-ADIN1100FMCZ uses the FT232RQ for UART to USB communication and requires the installation of drivers for the FTDI chip. Locate and install this driver separately. These drivers are available at: www.ftdichip.com/Drivers/CDM/CDM21228_Setup.zip.

Ethernet PHY Software GUI Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   To install the Ethernet PHY software GUI, take the following steps:

-  Ordered List ItemUnordered List ItemLaunch the installer file to begin the Ethernet PHY software installation.
-  If a window appears asking for permission to allow the program to make changes to the PC, click Yes.
-  The welcome window appears. Click Next.

|02-063798-01-b_f17.png|

-  The Ethernet PHY software launches. An overview of what is being installed and recommendations in terms of hardware power-up appears. Read the overview and click Next.

|02-063798-01-b_f18.png|

-  A license agreement appears. Read the agreement and click I Agree to allow the installation to proceed.

|02-063798-01-b_f19.png|

-  Select a location to install the Ethernet PHY software and then click Install.

|02-063798-01-b_f20.png|

-  A window appears stating that the installation is complete. Click Finish to continue.

|02-063798-01-b_f21.png|

-  The Ethernet PHY software is automatically installed in the Analog Devices folder on the PC. Access the Ethernet PHY software via Windows® explorer at C:\\Analog Devices\\ADIN1100 or from the Start menu.

INITIAL EVALUATION BOARD SETUP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   To set up the EVAL-ADIN1100FMCZ and use it with the Ethernet PHY software GUI, take the following steps:

-  Connect a 5-30 V power supply to the EVAL-ADIN1100FMCZ via the P1 connector or the P2 barrel connector.
-  Connect the USB cable to P5.
-  Connect the USB cable to the PC. When connecting the EVAL-ADIN1100FMCZ to the PC for the first time, the drivers are automatically installed. Wait until the driver installation is complete before proceeding to the next step.
-  Launch the Ethernet PHY software from the Analog Devices folder in the Start menu.

USING THE EVALUATION SOFTWARE
-----------------------------

When the Ethernet PHY software is launched, the GUI window shown below appears, and the succeeding Table lists the GUI labels and the corresponding descriptions. |02-063798-01-b_f22.png| > **GUI Label Descriptions**

+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Label | GUI Label Descriptions                                                                                                                                                                                                         |
+=======+================================================================================================================================================================================================================================+
| 1     | Select Local section. Shows connected evaluation hardware. The board name shown corresponds to the EVAL-ADIN1100FMCZ.                                                                                                          |
+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2     | User buttons.                                                                                                                                                                                                                  |
+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3     | Link Properties tab. Use this tab to change the PHY configuration.                                                                                                                                                             |
+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4     | Register Access tab. Allows the user read or write device registers. (4b) shows an option to have the Manual Register Access always on the main GUI screen by pulling the <> arrows to the left. This is not shown by default. |
+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 5     | Test Modes tab. Provides access to the various test modes on the device.                                                                                                                                                       |
+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 6     | Frame Generator/Checker tab. Configures and enables the frame generator and frame checker.                                                                                                                                     |
+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 7     | Board status information window. This window provides an overview of the PHY status, activity, reads, and writes issued to the selected device.                                                                                |
+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 8     | Activity Log section. Section shows read, write, and status activity for the selected PHY.                                                                                                                                     |
+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 9     | Dropdown menu to load a script file. This allows the user to load a script file with a sequence of write commands to load to the device.                                                                                       |
+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

GUI DETAILED OVERVIEW
---------------------

BOARD DISPLAY SHOWING CONNECTED EVAL-ADIN1100FMCZ HARDWARE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   In the Select Local section, a unique hardware identifier is shown for each EVAL-ADIN1100FMCZ board connected to the PC. In the example shown below, there are two EVAL-ADIN1100FMCZ boards connected to the same PC (AU54KUSA and AU5F2ILS).


   |02-063798-01-b_f23.png|

   The Ethernet PHY software GUI can only communicate with one EVAL-ADIN1100FMCZ evaluation board at a time. To choose which evaluation board is addressed as the local board in this section, click the appropriate device identifier to select and highlight it. All register controls, displayed link properties, and local board information in other sections of the GUI apply to the selected EVAL-ADIN1100FMCZ evaluation board.
   In order to more easily identify which board is which, it is recommended to set the boards to different hardware PHY addresses using the S2 hardware configuration pin switch on the evaluation board. The figure below shows an overlaid snapshot of the GUI whereby one board (unique identifier AU53CSS0) is at PHY Address 7 and the other (unique identifier AU4VVV4Q) is at PHY Address 0. The PHY address is easily identifiable on the physical board connected to the PC by looking at the S2 switch configuration.

   |02-063798-01-b_f24.png|

USER BUTTONS SECTION
~~~~~~~~~~~~~~~~~~~~

   Use the buttons in this section to control the basic operation of the GUI and the ADIN1100 device.


   |02-063798-01-b_f25.png|

Software Power-Down and Power-Up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   Click Software Power Down to place the selected device into software power-down mode where the analog and digital circuits are placed into a low power state. Most clocks are gated off, any signal or energy on the MDI pins are ignored and no link will be brought up. The MAC Interface output pins are asserted low. The management interface registers are accessible, and the part can be configured using software. Click Software Power Down to enable a software power-down. The button color changes to orange and the button label changes to Software Power Up. Click Software Power Up to exit from the software power-down and restart linking. When the software power-down is asserted, the other buttons for the selected device are grey and disabled.

Auto-Neg Restart
^^^^^^^^^^^^^^^^

   If the software configuration has been changed, click Auto-Neg Restart to restart the linking process with the new configuration. If the link has already been established, the link is first brought down and then restarted.

Export Registers
^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f26.png
   :alt: 02-063798-01-b_f26.png
   :align: center
   :width: 250px

   Click Export Registers to perform a data dump to the Activity Log section. Note that two clicks are required – one to make your selection and a second to press the orange button to perform the action. The register dump can be saved to text format for offline review. Right-click within the Activity Log and click Save as to save the data to a log file.


   |02-063798-01-b_f27.png|

Reset
^^^^^

   Click Reset to use the dropdown menu to initiate different resets. Again, like the Export Registers button, two clicks are required – one to make your selection and a second to press the orange button to perform the action. The reset options include the following:


   |02-063798-01-b_f28.png|

-  Unordered List ItemPHY Core Software Reset: click Reset: PHY to perform a reset where the CRSM_SFT_RST bit resets the PHY core registers. When this bit is set, a full initialization of the chip, almost equivalent to a hardware reset, is done. See the ADIN1100 datasheet for further details.
-  PHY Subsystem Reset: click Reset: SubSys to perform a reset of the PHY subsystem. All of the PHY digital circuitry is reset and any existing link will drop. The management registers are not initialized by this reset, and access to all the management registers is available during the PHY subsystem reset. The CRSM_PHY_SUBSYS_RST bit is set to 1 to perform this reset operation.

LINK PROPERTIES TAB
~~~~~~~~~~~~~~~~~~~

   The Link Properties tab provides user access to the main linking configurations within the device. When a control is selected, the GUI provides a prompt describing the function at the bottom of the linking control box (see figure below)


   |02-063798-01-b_f29.png|

Master or Slave Preference
~~~~~~~~~~~~~~~~~~~~~~~~~~

   For the selected device, prefer master or prefer slave can be chosen. Auto-Negotiation is used to resolve master or slave status. During Auto-Negotiation, when prefer slave is selected, and the remote end is preferred or forced Master, the local PHY will be set to slave (and remote to master). When the remote end is preferred or forced slave, the local PHY will be set to master (and remote to slave).

..

   Note, Auto-Negotiation is enabled by default for the ADIN1100 and it is strongly recommended that Auto-Negotiation is always enabled.

Transmit Amplitude
~~~~~~~~~~~~~~~~~~

   The Tx Level drop-down can be used to configure the required transmit amplitude mode for the intended application. The ADIN1100 can be configured by default to be:

-  Capable of 2.4 V pk-pk and request 2.4 V pk-pk transmit level
-  Capable of 2.4 V pk-pk and request 1.0 V pk-pk transmit level
-  Capable of 1.0 V pk-pk.

..

   Auto-Negotiation will determine the transmit level that the link will operate at.

REGISTER ACCESS TAB
~~~~~~~~~~~~~~~~~~~

   The Browse tab within the Register Access tab allows the user to review the bank of registers and edit the register fields or bit fields as required (see Figure below). Note that the Address field is a concatenation of the Device Address and Register Address as listed in the ADIN1100 datasheet.


   |02-063798-01-b_f30.png|

   The Manual tab within the Register Access tab allows the user to perform basic reads from and writes to individual ADIN1100 registers (see Figure below). Again, the “Address” field here is a concatenation of the Device Address and Register Address as listed in the ADIN1100 datasheet.

   |02-063798-01-b_f31.png|

   Access to the Manual tab of the Register Access section is also available on the right-hand side of the Activity Log section. To access this function, slide the arrow to the left to expose it (see Figure below).

   |02-063798-01-b_f32.png|

TESTMODES TAB
~~~~~~~~~~~~~

   Use this tab to initiate the various test mode functions in the device. Select the appropriate test mode and click Apply Mode (see Figure below).


   |02-063798-01-b_f33.png|

FRAME GENERATOR/CHECKER TAB
~~~~~~~~~~~~~~~~~~~~~~~~~~~

   This tab provides access to the frame generator and frame checker features of the ADIN1100 (see Figure below).


   |02-063798-01-b_f34.png|

   Control the number of frames generated by the generator, the frame length, and the content of the frame within this tab. Choose to have the frame generator to either run in burst mode or run continuously. To halt the frame generator when the frame generator is running continuously, use the Terminate button (note that the Generate button becomes the Terminate button once the Frame Generator is active).
   The Frame Generator can be used with & without Remote Loopback enabled.

Using the Frame Generator with Remote Loopback enabled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Before initiating the routine, choose which connected board (under the Select Local section) is to be considered the “local” and “link partner” board.

-  Configure the link partner board in remote loopback using the Remote Loopback button.


|02-063798-01-b_f35.png|

-  Enable the Frame Generator on the local board by clicking Generate.

|02-063798-01-b_f36.png|

-  The ADIN1100 device which generates the frames also receives frames looped by the link partner ADIN1100. The frame checker information displayed on the screen accumulates the number of frames sent and shows the number of errors observed.

|02-063798-01-b_f37.png|

Using the Frame Generator without Remote Loopback enabled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Before initiating the routine, choose which connected board (under the Select Local section) is to be considered the “local” and “link partner” board.

-  Enable the Frame Generator on the local board by clicking the Generate button.
-  Observe the frame checker information by selecting the link partner board.

>

BOARD STATUS INFORMATION WINDOW
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   This window displays the current status of the selected PHY chip (as determined in the Select Local section), including whether a link is established, the speed of the link (in this case, always 10BASE-T1L), the Auto-Negotiation Status, whether the selected PHY is master or slave and the transmit voltage amplitude. If the user switches between two EVAL-ADIN1100FMCZ boards in the Select Local section, the information shown in these fields will be updated to reflect the information provided from the currently selected board.


   |02-063798-01-b_f38.png|

   The GUI displays a color code to show the status of the link depending on how the user has configured the device (see Figure below).

   |02-063798-01-b_f39.png|

ACTIVITY LOG INFORMATION SECTION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   The activity log reports status information and register writes issued to the selected EVAL-ADIN1100FMCZ board (see Figure below). The activity log captures the activity in the GUI corresponding to the activity on the local PHY, which indicates the various reads, writes, and information on whether a link is established. When the frame generator is enabled, this window shows the frame generator activity. The board identification is recorded with each bit field change to clarify which device is being addressed.


   |02-063798-01-b_f40.png|

   To clear the activity log, right-click and then click Clear. To export the contents of the activity log for offline review, right-click and then click Save as. The file saved is a text file with a default location in the Analog Devices > ADIN1100 folder.

LOADING A SCRIPT FILE
~~~~~~~~~~~~~~~~~~~~~

   The GUI allows the user to load a sequence of register write commands from a file. Within the GUI window, there is a dropdown menu under the Activity Log section where the user can select the script file to run. Click the dropdown menu, choose the script by name, and then click the dropdown menu again to load the selected script. The Activity log displays the register writes issued from the script.


   |02-063798-01-b_f41.png|

   The script file is located in the ADIN1100 folder and is named registers_scripts.json (see Figure below).

   |02-063798-01-b_f42.png|

   The register write commands can be loaded with either the register name or the register address, as shown in the simple examples in the file. The commands are loaded sequentially. Create the sequence of write commands using a text editor. Ensure that the exact syntax is copied and match the register names with those in the datasheet to prevent errors reported in the activity log. Give the script a unique name.
   When the SftPd Down & Up routine is selected, see the following example:

::

        {
         "Name": "SftPd Down&Up",
         "RegisterAccesses": [
           {
             "MemoryMap" : "SPEPhy",
             "RegisterName": "CRSM_SFT_PD",
             "Value": 1
           },
           {
             "MemoryMap" : "SPEPhy",
             "RegisterName": "CRSM_SFT_PD",
             "Value": 0
           },
         ]
       },

.. |02-063798-01-b_f17.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f17.png
   :width: 400px
.. |02-063798-01-b_f18.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f18.png
   :width: 400px
.. |02-063798-01-b_f19.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f19.png
   :width: 400px
.. |02-063798-01-b_f20.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f20.png
   :width: 400px
.. |02-063798-01-b_f21.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f21.png
   :width: 400px
.. |02-063798-01-b_f22.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f22.png
.. |02-063798-01-b_f23.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f23.png
   :width: 200px
.. |02-063798-01-b_f24.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f24.png
.. |02-063798-01-b_f25.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f25.png
   :width: 250px
.. |02-063798-01-b_f27.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f27.png
   :width: 250px
.. |02-063798-01-b_f28.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f28.png
   :width: 250px
.. |02-063798-01-b_f29.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f29.png
   :width: 450px
.. |02-063798-01-b_f30.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f30.png
   :width: 450px
.. |02-063798-01-b_f31.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f31.png
   :width: 450px
.. |02-063798-01-b_f32.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f32.png
   :width: 450px
.. |02-063798-01-b_f33.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f33.png
   :width: 450px
.. |02-063798-01-b_f34.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f34.png
   :width: 450px
.. |02-063798-01-b_f35.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f35.png
   :width: 450px
.. |02-063798-01-b_f36.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f36.png
   :width: 450px
.. |02-063798-01-b_f37.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f37.png
   :width: 450px
.. |02-063798-01-b_f38.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f38.png
   :width: 450px
.. |02-063798-01-b_f39.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f39.png
   :width: 225px
.. |02-063798-01-b_f40.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f40.png
   :width: 450px
.. |02-063798-01-b_f41.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f41.png
   :width: 450px
.. |02-063798-01-b_f42.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin_1100/02-063798-01-b_f42.png
   :width: 450px
