Known Issues (ACE Software)
===========================

You can return to the ACE WIKI Homepage here: :doc:`ACE Homepage </wiki-migration/resources/tools-software/ace>`

ACE Offline Installation, Application Won't Start
-------------------------------------------------

In some cases after using the ACE offline installer on a machine that has no connection to the internet the ACE application will seem to install as expected but will not load or will close while the splash screen is loading the application. On checking the application log file you will see an error message similar to the one below:

**"ERROR: A certificate chain could not be built to a trusted root authority."**

This happens when the certs on the offline machine are out of date. There are a number of things that could be in need of an update but it is most likely the intermediate cert, this can be updated easily by following these steps:

-  Download the latest cert from here `DigiCertTrustedG4CodeSigning <http://cacerts.digicert.com/DigiCertTrustedG4CodeSigningRSA4096SHA3842021CA1.crt>`__
-  Copy this cert to the offline machine
-  Right click on the cert file and click "Install Certificate" in the context menu
-  Retry the ACE application (you may need to restart the machine)

If there are still issues with the certs and the error is still occurring, you can also try the following to update all of the windows certs on an offline machine:

-  Get the latest cert updates file for windows certs here `MSDownload authrootstl.cab <http://ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/authrootstl.cab>`__
-  You need to extract or copy the STL file from the .cab file and can use Powershell of CMD to install all of the certs in the file.
-  There are details in this article on how you can install from this file - https://www.itechtics.com/update-root-certificates/

If you are still observing the issue at this point, please contact us on ACE support at `ace.portal@analog.com <https://wiki.analog.com/mailto/ace.portal@analog.com>`__.

ACEZIP File Installation Unsuccessful Due to Security Block
-----------------------------------------------------------

In some cases downloading an ACEZIP file from an e-mail or from a remote/networked location has caused the file to become blocked by a security feature in Windows. This is not made clear during the download process but when the user attempts to install the ACE plug-in it will not work correctly.

If this happens, follow these steps to verify the ACEZIP has not been blocked and resolve the issue if it has:

-  Right click the file.
-  Select properties in the context menu.
-  Under the General tab, if a file has been blocked a new Security tag and Unblock button will have appeared.

|image1|

-  Click Unblock.
-  Retry the plug-in installation by double clicking the ACEZIP.

Graphing Issues
---------------

On some machines it has been found that the ACE application is not graphing as expected. If this occurs then open the settings tab in ACE and toggle the “Use Hardware Acceleration” checkbox. Also please check that the PC in question has the most UpToDate graphics driver.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/graphing_issue_2.png
   :width: 600px

Note: ACE will need to be restarted to reflect any changes made on this settings page.

High-Speed DAC Eval Boards are not discovered
---------------------------------------------

The High-Speed DAC boards have a second on-board USB controller, make sure this is connected as well as the main FPGA controller board. To avoid potential confusion, ACE only reports boards on the second controller (where it is required).

| 
| As of version 1.15, ACE includes an option to use ADI SDP driver for the on-board USB controller to avoid any of the conflicts with VISA drivers listed below and another option to install the DPG Lite application to replace the High-Speed DAC Software Suite. Both options can be activated by selecting the "High Speed DAC Components" option upon installation: |image2|

| 
| However, at this time, the High-Speed DAC Eval Boards listed below are not yet supported through ACE but through a dedicated SPI application that requires the NI VISA driver. The recommended action if you are actively using these High-Speed DAC Eval Boards with dedicated SPI applications is to not select the options discussed above.

================================= ===================================
Not yet supported through ACE ••• Supported through ACE with DPG Lite
================================= ===================================
AD9963/61                         AD9129/19
AD9148                            AD9122/21/25
AD9789                            AD9135
AD9993                            AD9136
\                                 AD9142A
\                                 AD9144
\                                 AD9162/1/3/4
\                                 AD9172/1/3/4/5/6
\                                 AD9739A/7A
\                                 AD9747/6/5/3/1
\                                 AD9783/81/80
\                                 AD9717/16/15/14
\                                 AD9117/16/15/14
\                                 AD9707/06/05/04
\                                 AD9736/35/34
\                                 AD9779A/78A/76A
\                                 AD9146
\                                 AD9739/37
\                                 AD9788/87/85
\                                 AD9748/44/42/40 (on DPG Lite only)
\                                 AD9767/65/63/09 (on DPG Lite only)
================================= ===================================

| 
| If the HSDAC components are not installed, there is a known driver conflict issue between the NI VISA driver and Keysight's VISA driver (used for automation of equipment). To work around this, try setting the Keysight VISA driver as the secondary VISA driver. This can be done with the Keysight installer. If this doesn't work, you may need to uninstall the Keysight Driver.
| The same workaround may be necessary for Rhode-Schwarz VISA.

| 
| If you need to automate equipment and use ACE at the same time you might have to use two separate PCs. The ACE remote control/scripting interface can be used by networking the PCs and setting Firewall rules appropriately.

| 
| Another possible issue causing ACE to not detect Hsdac boards is an outdated version of the "Evaluation Board Service" library. This library is installed as part of DPGDownloader. The "BitFlipper" application installer overwrites the currently installed version of the library with an incompatible one. Reinstalling the :doc:`latest version of High-Speed DAC Software Suite </wiki-migration/resources/eval/dpg/dacsoftwaresuite>` will restore the correct version of the library.

This is the ACE log entry indicating an incompatible version of the "Evaluation Board Service"

::

   Could not initialise DPG Client System.Exception: Could not query DPG3 for connected evaluation boards --->
   System.Exception: DeviceNotResponding at AnalogDevices.DPG.USB.CSA_USB.ControlIn(Int16 requestType, Int16 request, UInt16 wValue, UInt16 wIndex, Int16 length) at
   AnalogDevices.DPG.EvaluationBoards.Communication.DPG3_CSA.Finder.AttachedBoards(String[] DevicePaths)

Register Debugger Does Not Update Software Values
-------------------------------------------------

While not a bug, the behavior of the register debugger can be confusing and lead users to think that ACE is not successful communicating to the hardware. The register debugger reads and writes directly to the hardware, and it does not update register values stored in the software. This allows the user to avoid any events that would be triggered in the plug-in based on the register change, but this will cause the register map to be out of sync between the hardware and the software. The registers that are out of sync will be indicated by bold lettering in the register map, as seen in the figure below. If the user clicks the "Apply Changes" or if the Apply Changes transaction is executed by any other sequence in the plug-in, then ACE will update the hardware to match the UI, overriding changes made in the register debugger.

| 
| |image3|

As of ACE 1.13, there is an option to change the behavior of the register debugger using the "Update Software Registers" option. Selecting this will cause both the GUI and the hardware to update when registers are read or written through the register debugger.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/updatesoftwareregiserschecked.png
   :align: center
   :width: 600px

| 

To preserve the changes made in the register debugger, click the "Read All" toolbar button after completing register debugger writes and before performing any additional operations in ACE.

Board & Chip Diagrams Distorted (Regional Formatting Bug)
---------------------------------------------------------

.. note::

   This issue is addressed in ACE versions 1.7+


There is a known issue with some regional formats that causes bad loading and rendering of board and chip views. When the problem occurs, you may see some shapes appear with missing content and exaggerated size. The problem is particular to formats that use a comma (',') or any character besides '.' as the decimal separator.

To use the workaround, you need to temporarily change the format settings in Windows to a format that uses '.' as the decimal separator such as English (United States). For example, in Windows 7, you can access the setting through Control Panel -> Change display language, click the Formats tab, and select "English (United States)" in the "Format" drop-down.

.. image:: https://wiki.analog.com/_media/resources/tools-software/formats.png
   :alt: Region and Language : Formats
   :align: center
   :width: 300px

ACE or SDP Driver Install Fails or Warns me the driver/exe is unsigned
----------------------------------------------------------------------

Warnings may be safely ignored and dismissed, but they do highlight likely issues with your PC. The SDPDrivers and ACE package uses the latest signing technology and your PC may be out of date and unable to recognise the signing key.

-  Make sure the PC is connected to the Internet and can get root certificate updates, normally this happens automatically.
-  Check group policies to automatically update these run gpedit.msc

   -  Make sure the setting below is either Not Configured or Disabled


   |UpdateRoot.png|

-  Check for and install all the latest Windows updates
-  Check your group policy settings, these may be controlled by IT or a System Administrator
-  Ideally select Warn as the safer option in case you later encounter malicious software
-  Run gpedit.msc and navigate to the setting below

|CodeSigning.png|

ACE Plug-ins Fail to Load When a Different User Logs in
-------------------------------------------------------

.. note::

   This issue may affect ACE versions 1.14 and earlier.


When a machine is shared between users, the file access permissions may not be set correctly on all the installed plug-ins. The effect of this is that the plug-in cannot be accessed and fails to load. To fix this issue you will need Administrator privileges (or contact your Admin) in order to wipe out existing file permissions and reset appropriately.

-  Using Windows File Explorer navigate to the ACE plug-ins folder (%ProgramData%\\Analog Devices\\ACE\\Plugins)
-  Right Click on the "Plugins" folder and select "Properties"
-  Select the "Security" tab and click "Advanced"

|image4|

-  Choose "Change Permissions"
-  If you see "Everyone" or "Users" click "Edit" otherwise click "Add"
-  Grant "Full Control" or at minimum read/write/execute, click OK to dismiss the dialog

|image5|

-  Check the box "Replace all child object..."

|image6|

-  Click Apply

ACE Version Updater not working
-------------------------------

.. note::

   This issue only affects ACE Version 1.13


Some of the earlier versions of ACE Release 1.13 had an issue where the ACE updater was not detecting and downloading the latest version of ACE. If this happens, simply download the latest version of ACE from the :adi:`Analog Website <en/design-center/evaluation-hardware-and-software/ace-software.html>` and install manually.

This was resolved in ACE version 1.14.2763.1212.

ACE Crashes on Startup after Update
-----------------------------------

.. tip::

   This issues has been fixed with the latest release of ACE, v1.15.2818.1254


When updating from an older version of ACE there is an issue that can cause ACE to crash on startup. ACE can crash with one of the two following errors present in the exception.txt or AppTrace.log application log files:

.. important::

   
   ::
   
       System.NullReferenceException: 
       Object reference not set to an instance of an object.
       at AnalogDevices.Csa.UI.Themes.ThemeSelector.ApplyPreferredTheme()
       at AnalogDevices.Csa.App.Wpf.CsaApplication..ctor()
       at AnalogDevices.Csa.App.Wpf.Program.Main()
   


.. important::

   
   ::
   
       System.Exception: Cannot find resource named 'WindowBackgroundBrush'. Resource names are case sensitive.
   


This occurs because of a missing user setting when moving from older versions of ACE. This should not occur if you perform a scrub uninstall prior to updating the software, if you are updating from a version of ACE higher than v1.12 or if you are installing ACE for the first time.

The issue will not occur with the latest update of ACE, however if you are already experiencing this and need to resolve it in order for ACE to start, follow the steps below:

-  Ensure ACE is not running
-  Open the AnalogDevices folder in LocalAppData (C:\\Users\\username\\AppData\\Local\\Analog Devices)
-  Open the ACE folder
-  Open the UserSettings folder
-  Delete the Configuration.Settings.xml file
-  Restart ACE

This will fix the startup issue and allow ACE to generate a new complete user settings file.

.. tip::

   This issues has been fixed with the latest release of ACE, v1.15.2818.1254


ACEZIP file crashing when launched
----------------------------------

In some cases when you try to open an ACEZIP file it may result in the ACE application crashing.

If this happens, follow these steps to add the plug-in within the ACE application.

-  Open ACE
-  Click on Plug-In MarketPlace (Plug-in manager)
-  Click on Installed Packages
-  Enter the name of the plug-in to the search box eg. AD1234
-  If the plug-in is found then Select it and click "Uninstall Selected"
-  Click on Settings
-  Click on Plug-ins
-  Click on the + sign to the right of the "Zipped Plug-in Sources"
-  Under name , enter a new value eg "NewSource"
-  In the Source Column click on the box with three dots "...".
-  When the pop-up opens find and select the ACEZIP file
-  Click open (This will now have created a new Zipped Plug-in source )
-  Click Ok to return to the "Plug-in Manager"
-  Click on "Available Packages "
-  Click on the name you used in step 9 "NewSource"
-  Click on available plug-in eg. Board.AD1234
-  Click "Install Selected"
-  Click Close (The plug-in should now be available for use)

IIO Controllers not being detected
----------------------------------

Using ACE (x86)
~~~~~~~~~~~~~~~

IIO currently does not work with ACE x86. It requires the 64-bit version of ACE.

IIO WCF Wrapper
~~~~~~~~~~~~~~~

If you're having issues with IIO controllers and are seeing a console application opening up along with ACE called IIOWCFServerHelper or LibIIO WCF Server, you might be running older versions of the IIO packages and can possibly encounter issues when loading plugins.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/iiowrapperdetecteddevice.png
   :width: 600px

To resolve this, you'll need to update your packages using the ACE plugin manager.

-  Open ACE and navigate to the **Plug-in Manager** using the sidebar on the left.
-  Click on the **Available Updates** tab.
-  Click Update All and wait for the process to complete. Restart ACE if you're prompted to do so.
-  Repeat the process one more time to make sure all packages are updated.

Visual Studio redistributables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visual Studio 2013 redistributables are required for IIO controllers to be detected in ACE. If your IIO controller isn't being detected try downloading the redistributables from here: https://www.microsoft.com/en-us/download/details.aspx?id=40784.

Restart ACE after the installaion.

Contact ACE Support
-------------------

.. important::

   
   If the above solutions do not resolve your issue, then please use the "Report Issue" function from the ACE menu. This will generate an email to the ACE support team (and attach any relevant diagnostic files)
   
   .. image:: https://wiki.analog.com/_media/resources/tools-software/ace/ace_report_issue.png
      :width: 200px
   
   Alternatively please contact ACE support at `ace.portal@analog.com <https://wiki.analog.com/mailto/ace.portal@analog.com>`__
   


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/acezipfileaccessissue.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/ace/hsdac_install.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/ace/updatesoftwareregisersunchecked.png
   :width: 600px
.. |UpdateRoot.png| image:: https://wiki.analog.com/_media/resources/tools-software/updateroot.png
   :width: 1000px
.. |CodeSigning.png| image:: https://wiki.analog.com/_media/resources/tools-software/codesigning.png
   :width: 1000px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/ace/knownissues.folderproperties.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/ace/knownissues.fullcontrol.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/ace/knownissues.advancedfilepermissions.png
