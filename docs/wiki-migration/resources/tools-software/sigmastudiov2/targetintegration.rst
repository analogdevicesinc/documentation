:doc:`Click here to return to the SigmaStudio+ documentation landing page </wiki-migration/resources/tools-software/sigmastudiov2>`

.. note::

   This section is applicable to ADSP-214xx, ADSP-215xx and ADSP-SC5xx family of processors only


Table of Contents
=================

-  :doc:`Debug using CrossCore Embedded Studio </wiki-migration/resources/tools-software/sigmastudiov2/debug_using_crosscore_embedded_studio>`
-  :doc:`Advanced Design Mode </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/advanceddesign>`

   -  :doc:`Target and Communication Libraries Integration </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/integratecommlibrary>`
   -  :doc:`Target Library API </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi>`

      -  :doc:`Target Library and Header Files </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/libfiles>`
      -  :doc:`API Functions </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apifuncs>`
      -  :doc:`API Data Types </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apidatatypes>`
      -  :doc:`API Macros </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apimacros>`

   -  :doc:`Communication API </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi>`

      -  :doc:`Communication library and interface header file details </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/libfiles>`
      -  :doc:`API Functions of communication library </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apifuncs>`
      -  :doc:`API data structures of communication library </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apidatastructures>`
      -  :doc:`API enumerations and type defines macros of communication library </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi/apimacros>`

   -  :doc:`Target Application </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication>`

      -  :doc:`Target Framework Architecture </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/frameworkarc>`
      -  :doc:`Target Framework Status </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/frameworkstatus>`
      -  :doc:`Audio Input Output Modes </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/audioiomodes>`
      -  :doc:`Multi Core Processing and Multi Instancing </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/multicoreprocess>`
      -  :doc:`Microcontroller Mode Support </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/mcsupport>`
      -  :doc:`Target Framework Default Parameters </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/targetframework>`
      -  :doc:`System Integration </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/systemintegration>`

Target Integration
==================

This section provides a detailed instructions that software engineers can use to modify the supplied default target application, create new applications with target library APIs or integrate the SigmaStudio+ functionality to existing applications. This document also provides a detailed description of the default framework supplied within the package.

.. note::

   The ADSP-21489 support is available up to CrossCore Embedded Studio version 2.12.0, and the ADSP-21568 support is available starting from CrossCore Embedded Studio version 3.0.1.


Rebuild Demo Application
------------------------

The Default Application for ADSP-21489, ADSP-SC573, ADSP-SC584, ADSP-SC589, ADSP-21584, and ADSP-21573, ADSP-21568, ADSP-21569, ADSP-21593, ADSP-SC594 and ADSP-SC598 are supplied with the package. Follow the steps given below to rebuild the Application. The projects can be found under target specific subfolders inside “SigmaStudioPlus-Relx.y.z\\Target\\Examples\\Demo”.

-  Launch CrossCore Embedded Studio on the SigmaStudio+ Host PC. Specify the workspace when prompted.
-  Select File->Import->"Existing project into Workspace" option or use "Import an existing CCES project" option in the welcome window. Import SS_App_Core0, SS_App_Core1 and SS_App_Core2 projects of appropriate processor into CrossCore Embedded Studio. In package example projects are available for ADSP-SC573, ADSP-SC584, ADSP-SC589, ADSP-SC589 SAM, ADSP-SC594, ADSP-SC598.
-  Select File->Import->"Existing project into Workspace" option or use "Import an existing CCES project" option in the welcome window. Import SS_App_Core1 and SS_App_Core2 projects of appropriate processor into CrossCore Embedded Studio. In package example projects are available for ADSP-21584, ADSP-21573, ADSP-21593.
-  Select File->Import->"Existing project into Workspace" option or use "Import an existing CCES project" option in the welcome window. Import SS_App_Core1 project into CrossCore Embedded Studio for ADSP-21489, ADSP-21568 and ADSP-21569.
-  Select all the core projects of corresponding processor in CCES, Clean and rebuild the projects in the required buildconfiguration (Release/Debug).
-  The newly generated executable(s) will be present in “Debug” or “Release” folder based on the chosen build configuration, inside the corresponding processor application core projects folder.

Debug Using CCES
----------------

This section explains how to `debug_using_crosscore_embedded_studio <https://wiki.analog.com/debug_using_crosscore_embedded_studio>`_

Advanced Design Mode
--------------------

This section contains detailed information on integrating SigmaStudio+ with target processor and controller applications. The user can write their own Application using the APIs provided. This flexibility allows the user to integrate the SigmaStudio+ Tuning feature to existing Applications. This method also enables the user to have other algorithms along with SigmaStudio+ in a single Application.

:doc:`Advanced Design Mode </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/advanceddesign>`

This section contains information about integrating target and communication libraries into custom application
