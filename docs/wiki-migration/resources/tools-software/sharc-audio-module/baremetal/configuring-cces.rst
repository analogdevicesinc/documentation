Configuring CCES for Development and Debug of the Framework
===========================================================

The video below provides a walk-through of getting CCES configured to begin developing code and debugging this code in CCES and on the SHARC Audio Module. The steps covered in this video are also briefly outlined below and are provided to help with a better debug experience.

.. image:: https://wiki.analog.com/_media/youtube>GprhlU-IrXQ
   :alt: youtube>GprhlU-IrXQ

Steps to Configure CCES
-----------------------

-  Enable line numbers in the text editor. Go to Window->Preferences and then to General->Editors->Text Editors and click "Show line numbers" checkbox. Then hit "Apply and Close".
-  Build the project by going to Project->Build All. This will create binary executables for each core.
-  Select the top level of the Core 0 project in the Project Explorer window and click the bug icon in the icon bar. This will walk you through the process of creating a new debug profile.
-  Click the bug again once the debug profile has been created to download your binary files to the SHARC Audio Module.
-  Once the files have been downloaded and the debugger is halted at the start of main(), go to Target->Settings->Target Options... Check the "Mask interrupts during step" checkbox.

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#downloading-and-installing
   :alt: Opening the Framework in CCES#.|Bare Metal Framework#baremetal-framework-architecture|Bare Metal Framework Architecture
