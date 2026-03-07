ACE - Getting Started
=====================

This WIKI site will introduce ACE and ACE Plug-ins with a brief description and also take you through the installation steps to get the ACE application installed on your machine.

You can return to the ACE WIKI Homepage here: :doc:`ACE Homepage </wiki-migration/resources/tools-software/ace>`

What is ACE?
------------

ACE stands for **Analysis \| Control \| Evaluation** and is a proprietary software developed at ADI to facilitate the evaluation and control of multiple evaluation systems, from across ADI’s portfolio.

ACE is a desktop software that runs on the Windows Operating system.

**Supported OS:**

-  Windows 10 (x86)
-  Windows 10 (x64)

**Potentially Compatible OS:** Extended support for Windows 7 ended on January 14, 2020 and as a result Windows 7 is no longer a prioritised OS for support. There is potential for future releases to be unsupported as a result.

-  Windows 7 (x86)
-  Windows 7 (x64)

**Legacy OS:**

Older versions of ACE were supported on previous versions of the Windows OS and may still retain some functionality but they are no longer supported and are not actively tested for compatibility with the software. Use of the ACE software cannot be guarenteed on these platforms.

-  Windows Vista (x86)
-  Windows Vista (x64)

-  Windows 8 (x86)
-  Windows 8 (x64)

-  Windows XP (x86)
-  Windows XP (x64)

Installing ACE
~~~~~~~~~~~~~~

.. important::

   Close all instances of ACE before starting the installation process.


.. tip::

   Once installed, new Updates to the software will become available from within the application!


The latest version of ACE is available from www.analog.com/ace. Simply download the latest installer and run it to launch the ACE Setup Wizard. This step by step installation will guide you when installing ACE and it's accompanying software support modules as necessary. 

.. raw:: html

   <details><summary>Click here to view the installation steps</summary>

.. container:: centeralign

   
   Step 1: Launch the Setup Wizard
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   


.. container:: centeralign

   Click Next to begin the installation process.


   |image1|

.. container:: centeralign

   
   Step 2: Check for Updates
   ^^^^^^^^^^^^^^^^^^^^^^^^^
   


.. container:: centeralign

   Choose to check online for updates or continue installation offline. Click Next to continue.


   |image2|

.. container:: centeralign

   
   Step 3: License Agreement
   ^^^^^^^^^^^^^^^^^^^^^^^^^
   


.. container:: centeralign

   Read the ACE software license agreement. If you agree to the terms and conditions, you must click "I Agree" to continue.


   |image3|

.. container:: centeralign

   
   Step 4: Installation Directory
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   


.. container:: centeralign

   Choose your installation directory or use the default location. Click Next to continue.


   |image4|

.. container:: centeralign

   
   Step 5: Choose Components to Install
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   


.. container:: centeralign

   Choose the features of ACE you want to install. It is recommended that you install all of the prerequisites since ACE needs them to function correctly. Click Next to continue.


   |image5|

.. container:: centeralign

   
   Step 6: Installation
   ^^^^^^^^^^^^^^^^^^^^
   


.. container:: centeralign

   Wait for the selected components to be installed. Click Next to continue.


   |image6|

.. container:: centeralign

   
   Step 7: Complete Installation
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   


.. container:: centeralign

   Final installer step, click Finish to complete the installation.


   |image7|

.. raw:: html

   </details>


Installation Directories
~~~~~~~~~~~~~~~~~~~~~~~~

Newer versions of ACE ship with a mixed x64 and x86 installation allowing you to run either from your local machine. The default locations for the application to install are as follows:

-  x86 - C:\\Program Files (x86)\\Analog Devices\\ACE
-  x64 - C:\\Program Files\\Analog Devices\\ACE

Uninstalling ACE
~~~~~~~~~~~~~~~~

Uninstalling ACE is done using the uninstall.exe located in the x86 installation directory. This will uninstall both the x86 and x64 version of the application.

Uninstalling ACE with the default settings will only remove the currently installed application and leave all current user settings, ACE plug-ins, session files etc. installed on your machine. It can be preferable to remove all of this content from your machine under certain circumstances, for example if you find your installation has entered an unknown state and you would like to restore ACE to factory settings.

To remove all ACE content for your installation you can perform a "Scrub Uninstall", either manually or using the option to Scrub during the uninstall.exe wizard.

You can find more information about this process here: :doc:`Uninstall Scrub </wiki-migration/resources/tools-software/ace/installscrub>`

What is an ACE Plug-in
----------------------

ACE consists of a common software framework and individual component specific "plug-ins". An ACE plug-in is a piece of software written using the ACE framework to evaluate a particular product or product group. ACE is driven by the plug-ins available to the application. The plug-ins are added to ACE as software extensions when they are installed through the application plug-in management tool. The plug-ins themselves provide ACE with the information used to evaluate the products (boards and chips) supported by a particular plug-in.

Next Steps
----------

Use the Quickstart Guides below to understand how to launch the ACE application for the first time and start downloading new plug-ins to start your product evaluation:

-  :doc:`Quickstart - ACE Quickstart and Plug-in Installation </wiki-migration/resources/tools-software/ace/userguide/quickstart>`
-  :doc:`Quickstart - Using a Plug-in </wiki-migration/resources/tools-software/ace/userguide/quickstart/quickstartplugin>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/page_1.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/page_2.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/page_3.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/page_4.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/page_5.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/page_6.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/ace/userguide/page_7.png
   :width: 600px
