| :doc:`Click here to return to the SigmaStudio+ documentation landing page </wiki-migration/resources/tools-software/sigmastudiov2>`
|

.. note::

   This section is applicable to ADSP-214xx, ADSP-215xx and ADSP-SC5xx family of processors only


Table of Contents
=================

::

   *[[/resources/tools-software/sigmastudiov2/debug_using_crosscore_embedded_studio|Debug using CrossCore Embedded Studio]]
   *[[/resources/tools-software/sigmastudiov2/targetintegration/advanceddesign|Advanced Design Mode]]
     *[[/resources/tools-software/sigmastudiov2/targetintegration/integratecommlibrary|Target and Communication Libraries Integration]]
     *[[/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi|Target Library API]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/libfiles|Target Library and Header Files]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apifuncs|API Functions]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apidatatypes|API Data Types]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi/apimacros|API Macros]]
     *[[/resources/tools-software/sigmastudiov2/targetintegration/commapi|Communication API]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/commapi/libfiles|Communication library and interface header file details]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/commapi/apifuncs|API Functions of communication library]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/commapi/apidatastructures|API data structures of communication library]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/commapi/apimacros|API enumerations and type defines macros of communication library]]
     *[[/resources/tools-software/sigmastudiov2/targetintegration/targetapplication|Target Application]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/frameworkarc|Target Framework Architecture]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/frameworkstatus|Target Framework Status]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/audioiomodes|Audio Input Output Modes]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/multicoreprocess|Multi Core Processing and Multi Instancing]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/mcsupport|Microcontroller Mode Support]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/targetframework|Target Framework Default Parameters]]
       *[[/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/systemintegration|System Integration]]

| 
| ====== Target Integration ====== This section provides a detailed instructions that software engineers can use to modify the supplied default target application, create new applications with target library APIs or integrate the SigmaStudio+ functionality to existing applications. This document also provides a detailed description of the default framework supplied within the package.

.. note::

   The ADSP-21489 support is available up to CrossCore Embedded Studio version 2.12.0, and the ADSP-21568 support is available starting from CrossCore Embedded Studio version 3.0.1.


   | ===== Rebuild Demo Application ===== The Default Application for ADSP-21489, ADSP-SC573, ADSP-SC584, ADSP-SC589, ADSP-21584, and ADSP-21573, ADSP-21568, ADSP-21569, ADSP-21593, ADSP-SC594 and ADSP-SC598 are supplied with the package. Follow the steps given below to rebuild the Application. The projects can be found under target specific subfolders inside “SigmaStudioPlus-Relx.y.z\\Target\\Examples\\Demo”.

-  Launch CrossCore Embedded Studio on the SigmaStudio+ Host PC. Specify the workspace when prompted.
-  Select File->Import->"Existing project into Workspace" option or use "Import an existing CCES project" option in the welcome window. Import SS_App_Core0, SS_App_Core1 and SS_App_Core2 projects of appropriate processor into CrossCore Embedded Studio. In package example projects are available for ADSP-SC573, ADSP-SC584, ADSP-SC589, ADSP-SC589 SAM, ADSP-SC594, ADSP-SC598.
-  Select File->Import->"Existing project into Workspace" option or use "Import an existing CCES project" option in the welcome window. Import SS_App_Core1 and SS_App_Core2 projects of appropriate processor into CrossCore Embedded Studio. In package example projects are available for ADSP-21584, ADSP-21573, ADSP-21593.
-  Select File->Import->"Existing project into Workspace" option or use "Import an existing CCES project" option in the welcome window. Import SS_App_Core1 project into CrossCore Embedded Studio for ADSP-21489, ADSP-21568 and ADSP-21569.
-  Select all the core projects of corresponding processor in CCES, Clean and rebuild the projects in the required buildconfiguration (Release/Debug).
-  The newly generated executable(s) will be present in “Debug” or “Release” folder based on the chosen build configuration, inside the corresponding processor application core projects folder.

|

| ===== Debug Using CCES ===== This section explains how to `debug_using_crosscore_embedded_studio <https://wiki.analog.com/debug_using_crosscore_embedded_studio>`_
| ===== Advanced Design Mode ===== This section contains detailed information on integrating SigmaStudio+ with target processor and controller applications. The user can write their own Application using the APIs provided. This flexibility allows the user to integrate the SigmaStudio+ Tuning feature to existing Applications. This method also enables the user to have other algorithms along with SigmaStudio+ in a single Application.
| :doc:`Advanced Design Mode </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/advanceddesign>`
| This section contains information about integrating target and communication libraries into custom application
