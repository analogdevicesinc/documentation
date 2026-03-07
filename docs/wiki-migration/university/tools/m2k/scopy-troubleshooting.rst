Scopy troubleshooting guide
===========================

ADALM2000 doesn't show up
-------------------------

Make sure you install the latest driver -

-  :doc:`Windows Drivers </wiki-migration/university/tools/pluto/drivers/windows>`
-  :doc:`Linux Drivers </wiki-migration/university/tools/pluto/drivers/linux>`
-  :doc:`macOS Drivers </wiki-migration/university/tools/pluto/drivers/osx>`

Use compliant USB cable
-----------------------

Some USB cables are incapable of power delivery necessary to the ADALM2000 (or are just plain flakey). Please use the provided USB cable. Also in order to troubleshoot this, you try using two cables, plug in a separate cable to the USB connector for power delivery (to the USB power connector), while using the center USB connector for data transfer. If using two cables works, it normally means it's a cable, or voltage droop issue on the host.

Reinstall & INI files
---------------------

``Scopy.ini`` and ``Preferences.ini`` contain the user-settings that are saved in-between sessions. Sometimes these can get messed up and can cause problems. In order to reset them, go to: These file are located in:

-  **Windows:** ``C:\Users\<your_username>\AppData\Roaming\ADI`` Sometimes this is a hidden directory, and you `unhide it <https://cybertext.wordpress.com/2012/05/29/cant-see-the-appdata-folder/>`_.
-  **Linux:** ``/home/<your_username>/.config/ADI``
-  **Mac:** ``/Users/<your_username>/.config/analog.com``

and delete (or rename) ``Scopy.ini``, ``Scopy.ini.bak``, ``Preferences.ini``, ``Preferences.ini.bak``. The preference is to rename things with a different suffix, so if you need to report a bug, the file still exists.

Scopy configuration can sometimes get messed up when updating as opposed to uninstall/reinstall. If you are facing this issue, you can try uninstalling Scopy and then reinstall.

.. important::

   Make sure that after uninstall Scopy's folder is clear


Make sure you install Scopy in a location that doesn't require any write privileges since Scopy needs to write to it's installation folder.

Network is going down when connecting ADALM2000
-----------------------------------------------

The ADALM2000 creates a virtual network interface when connected to USB. The network interface is created with ip address 192.168.2.1 by default which can clash with your own computer's network. To change the default IP address you can check out this :doc:`link </wiki-migration/university/tools/pluto/users/customizing>`

Connecting through the network interface
----------------------------------------

If you are having trouble connecting through USB, you can always connect to the ADALM2000 through the network interface. The USB connection can cause all kinds of problems on various systems. In order to connect through the emulated network interface follow :doc:`these steps </wiki-migration/university/tools/m2k/scopy>`.

Make sure you have the latest firmware
--------------------------------------

Visit the ADALM2000 firmware page :git-m2k-fw:`releases`.

Compare the latest firmware version on this page with the one you have installed. Follow :doc:`these steps </wiki-migration/university/tools/m2k/common/firmware>` to update the firmware.

Uninstall and reinstall the software
------------------------------------

-  Run a clean uninstall
-  Delete the ini files
-  Run a clean reinstall
-  Restart your computer after the clean install can fix your problems.

Make sure the system doesn't limit the USB power consumption
------------------------------------------------------------

Some laptops limit the amount of current that can be delivered via an USB port (either native or from a docking station/usb hub). In order to workaround this issue you can try the following:

-  Go to Device Manager tool in Windows OS
-  Go to Universal Serial Bus Controllers
-  Select ASMedia USB Root hub(or which USB root hub the board is connected to), Right click on its properties
-  uncheck the "Allow the computer to turn off this device to save power" in the Power management tab
-  Reboot.

Run iio_info -a for board diagnostics
-------------------------------------

Download latest version of :git-libiio:`releases` .

Open a command prompt and run

::

   iio_info -a 

or

::

   iio_info -u "ip:192.168.2.1"

Scopy white screen on Windows
-----------------------------

Scopy displaying a white screen on startup (combined with hangs or crashes) is an issue that indicates OpenGL incompatibility with your system due to a missing or outdated graphics driver/DirectX/OpenGl Driver.

-  Disable OpenGL usage in favor software rendering by setting the **general_use_opengl** preference in preferences.ini to **false**.
-  On Windows Virtual Machine, enable 3d hardware acceleration.

In recent Scopy versions, a pop-up will appear when this issue is detected, the preference will be automatically disabled and Scopy will try to restart. For older Scopy versions, please do this manually.

Debugging with WinDbg - Advanced, Windows Only
----------------------------------------------

Download the debug files associated with your release. From the same place you downloaded the release, download the "debug-64.zip" file. If you can't remember where you downloaded the release from, a safe bet would be to redownload and reinstall Scopy and the appropriate debug archive.

.. important::

   It is critical that the debug file and Scopy is the same version for this to work


-  Unzip debug-64.zip to a location.
-  Copy the .pdb files to Scopy.exe's location. The installation folder should look like this:

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopydebugfiles.png
   :align: center
   :width: 400px

-  Open WinDbg (x64)
-  File -> Open Executable (CTRL+E) -> Navigate to Scopy.exe -> Select Scopy.exe
-  File -> Symbol File Path -> Navigate to Scopy.exe folder -> Select Scopy folder (Make sure you select "Reload" checkbox in the bottom left of the Dialog Box)
-  File -> Source File Path -> Navigate to debug-64.zip folder -> Select "scopy" folder (this file should contain the sources from github)
-  You can save this workspace if you plan to do this multiple times to save time (File -> Save workspace to file)
-  Debug -> Run (or F5)
-  Profit

You can now reproduce bug/crash/hang

-  If scopy crashes, WinDbg will stop after crash so you can investigate.
-  If scopy hangs, you can debug->break (CTRL+Brk) to see where it's hanging
-  View -> Call Stack (ALT+6) (to check out call stack when crash/hang occurs) (opens window like 2 in screenshot)
-  View -> Processes & Threads (ALT+9) (so you can cycle through different threads) (opens window like 4 in screenshot)
-  Call Stack -> Source (to enable source mapping) (button 1 in screenshot)
-  Command -> run: ".dump <file_name.dmp>" to create crash dump that can be sent to the developers (Command window input - 5 in screenshot)
-  You can look around to figure out where it crashed/why (3 in screenshot shows source mapping - where the hang occurs)

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopywindbginterface.png
   :align: center
   :width: 600px
