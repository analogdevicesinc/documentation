Reporting a Bug
===============

Bug
---

A `Software_bug <https://en.wikipedia.org/wiki/Software_bug>`_ is a flaw, error in a software application that causes it to **behave unexpected**, **hang** or even **crash**. No matter how sharp our skills are, or rigorous our testing, a few bugs are bound to slip through the cracks every now and then. As much as you don't want them; we don't want/like them either. However, some bugs can be difficult to replicate, track down and eventually fix without a well written bug report. If you encounter one of the what you believe is a software bug, this guide is here to provide a step by step approach into reporting the bug on our :git-scopy:`issue tracker <issues>`.

What we need is:

-  Brief description of the bug
-  Steps to reproduce the bug
-  Expected result
-  Actual result with a screenshot or screen capture

Before reporting a bug
----------------------

Is it a bug? or is it a feature request? Something not working properly (a bug) is different than something working differently than you want. :git-scopy:`Feature requests <issues>` are tracked in the same place as bugs, but will not have a ``bug`` label.

Some :doc:`troubleshooting steps </wiki-migration/university/tools/m2k/scopy-troubleshooting>` that might be worth looking at to understand if you have a potential common hardware problem.

Scopy is continuously being improved from one version to another, (with bug fixes) and with new features.

-  ensure you are using the :git-scopy:`latest release version <releases/latest>` of scopy. If you can replicate the bug on that, try
-  the most recent `nightly Winbdows builds <https://ci.appveyor.com/project/analogdevicesinc/scopy/build/artifacts>`_. It's possible that someone else already reported the bug, and it has been solved.

If the bug exists in the nightly - You will need to report a bug (sorry). First check to see if someone else has reported the same :git-scopy:`bug <issues?q=is%3Aissue+is%3Aopen+label%3Abug>`.

Description of the Bug
----------------------

The easiest/most straightforward way to describe the bug, is to let us see how scopy was configured when the bug occurred. From one session to another, Scopy uses ``.ini`` files to load its previous state when it was closed. These file are located in:

-  **Windows:** ``C:\Users\<your_username>\AppData\Roaming\ADI`` Sometimes this is a hidden directory, and you `unhide it <https://cybertext.wordpress.com/2012/05/29/cant-see-the-appdata-folder/>`_.
-  **Linux:** ``/home/<your_username>/.config/ADI``
-  **Mac:** ``/Users/<your_username>/.config/analog.com``

The ``*.ini`` files are simple text files:

-  **``Scopy.ini``** : captures the state of all the instruments, and menu settings, and locations of all windows.
-  **``Preferences.ini``** : controls the preferences of scopy

When a bug/crash occurs, this files can be trivial in inspecting the configuration that caused Scopy to fail, and can be critical in getting allowing a developer to easily replicate the problem.

In the Windows folder where the ".ini", a ``crashdmp`` folder will also be there that will contain additional information about the crash and where it happened. This is a Windows *small memory dump file*. The memory dump file contains the following information:

-  The Stop message, its parameters, and other data
-  A list of loaded drivers
-  The processor context (PRCB) for the processor that stopped
-  The process information and kernel context (EPROCESS) for the process that stopped
-  The process information and kernel context (ETHREAD) for the thread that stopped
-  The Kernel-mode call stack for the thread that stopped

This can allow scopy developers to troubleshoot the issue with the Windows Debugger (``WinDbg.exe``) tool and understand where things crashed, without even having to replicate the steps that caused the crash. The easier it is to find the problem, the easier it is to fix it, and faster you can get back to work.

Alongside the ".ini" files, if logging is enabled in Scopy, there should also be a file with the name "ScopyLog-yymmdd-hhmmss.id". In order to generate a log file, the debug logging must first be enabled via the Preferences Menu from the Debug Section(Enable Session Logging). Once Scopy is closed the debug logging is disabled. For each connection a new logging file is generated. This files will never be deleted by Scopy, they can be manually deleted by the user.

In order to generate a logging file that provides the most information, after encountering a bug, restart Scopy, enable the session logging from the Preferences menu, then connect to the board and reproduce the exact steps that lead to the bug.

.. important::

   Making a backup of the entire folder where the ``.ini`` files are located and adding it to the bug report is critical for developers.


Older Versions of Scopy (v 1.2.0 and older) do not capture:

-  **Operating System:** Scopy runs on Windows, Linux and MacOS. This is important for us as the dependencies we use for Scopy might have different implementations on different operating systems and we could track the bug to one of them if we knew the system.
-  \**Scopy Version: \*\* Scopy is continuously being improved from one version to another, with bug fixes and with new features. Sometimes this new features also bring hidden bugs, but sometimes they also fix older bugs. So making sure that we now exactly the version of Scopy that crashed greatly improves our debugging.
-  \**Firmware Version: \*\* The firmware version is also important, as the bug might be tracked down into the firmware that is currently installed on the device itself.

Steps to reproduce the Bug
--------------------------

Some bugs might be obvious to reproduce (always clicking a button crashes Scopy), but some are hard and only happen in a specific configuration. Mentioning the exact steps that lead to the bug are trivial for us in order to properly reproduce it.

Example Report
--------------

**Operating System:** Linux

**Scopy Version:** v1.2.0 or git tag

**Firmware Version:** 0.25

**Steps to reproduce the bug**:

- Started the Signal Generator with the following configuration: 5khz 2V sine wave on channel 1 ...

- Started the Oscilloscope

- On the Oscilloscope, selected the measurements menu

- When enabling statistics in the measurements menu, Scopy crashes.

Attached the ".ini" files also containing the "crashdump" folder (if on Windows) and the logging files if present
