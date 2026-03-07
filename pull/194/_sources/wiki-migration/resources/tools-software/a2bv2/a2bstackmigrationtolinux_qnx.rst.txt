:doc:`Click here to return to the A2B SSPlus Stack User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide>`

Migrating Stack to Linux/QNX
============================

This document is a comprehensive guide for migrating stack from ADI_A2B_Software-Rel19.X.Y / ADI_A2B-SSPlus_Software-RelX.Y.Z versions to a Linux/QNX environment. Please follow the steps below.

-  Copy the “a2bstack” folder from the following Windows directory: C:\\Analog Devices\\ADI_A2B-SSPlus_Software-RelX.Y.Z\\Target Or C:\\Analog Devices\\ADI_A2B_Software-Rel19.X.Y\\Target.\


|image1|

-  Copy the a2bapp.c and a2bapp.h files from the following Windows directory “C:\\Analog Devices\\ADI_A2B-SSPlus_Software-RelX.Y.Z\\Target\\examples\\demo\\app-plugin” or C:\\Analog Devices\\ADI_A2B_Software-Rel19.X.Y\\Target\\ examples\\demo\\app-plugin.
-  Transfer the copied “a2bstack” folder, a2bapp.c and a2bapp.h files to the Linux/QNX machine.
-  Navigate to the target directory on your Linux/QNX machine: /opt/analog/a2b-software/X.Y.Z/Target/ and replace the existing “a2bstack” folder in this location with the one you copied from the Windows machine.

.. note::

   Compare this a2bapp.c and a2bapp.h files with your current version in Linux/QNX distribution and merge your project-specific application file modifications to this version.


\



|image2|

-  Refer to the user guide's Linux/QNX application compile section, which explains how to compile the application.

.. note::

   This document assumes that no modifications have been made under the "a2bstack" folder. If any modifications have been made, it is necessary to merge those changes accordingly.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2b_stack.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2b_stack_linux_folder.png
