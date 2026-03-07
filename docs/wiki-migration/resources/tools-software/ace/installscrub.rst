About
=====

Sometimes we change things or you change something and ACE isn't quite right afterwards. To get back to a fresh, cleanly installed state there's a few things you have to do. Soon we'll introduce a feature to do this automatically. For now, to fix up plug-ins not loading, failed updates or ACE failing to load, try the steps below to scrub things clean and get back to a blank slate.

.. important::

   WARNING: You will lose your session files, preferences, exported data and plug-ins etc.


Steps
=====

.. note::

   From ACE v1.14+ you can perform a scrub uninstall using uninstall.exe


Step 1. Open the install directory for ACE and run the uninstall.exe

Step 2. Ensure you check the ScrubUninstall check box in the Components window as shown below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/scrub_uninstall.png
   :width: 400px

If you have any issues with this method, you can still perform a manual scrub using the steps outlined below.

Manual Scrub
============

Step 1. Run the ACE uninstaller

Step 2. Launch Windows File Explorer with ADMIN privileges (Windows 7)

-  Hit Ctrl Alt Delete and click "Start Task Manager"
-  In the bottom of "Task Manager" click "Show processes from all users"
-  If required enter details for the admin account
-  Click File→New Task(Run...)
-  Type explorer.exe and select "Create this task with administrative privileges"

Step 3. Open %ProgramFiles(x86)%\\Analog Devices\\ACE and delete any files contained within

Step 4. Open %LocalAppData%\\Analog Devices\\ACE and delete files within

Step 5. Open %ProgramData%\\Analog Devices\\ACE and delete files within

Step 6. Download the latest ACE version from :adi:`ace` and re-install
