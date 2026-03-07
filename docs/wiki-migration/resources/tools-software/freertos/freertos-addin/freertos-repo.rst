FreeRTOS Add-In GIT Sources
===========================

The following sections will describe how the add-in clones the sources from the Analog Devices FreeRTOS Add-In Repository.

--------------

Repository
----------

The FreeRTOS Add-In will automatically download the latest version of the sources into your project, when you add the FreeRTOS Add-In to your project, so you would normally have no need to look at the GitHub repository the files come from.

The repository is available at https://github.com/analogdevicesinc/freertos-addin-rtos.

Version
-------

The FreeRTOS Add-In automatically downloads the most up to date version of the FreeRTOS sources that are available. This is done by the Repository having a **Tag Structure** that follows a specific naming convention. This convention will always be as follows

**REL-ADIFRTOS-**\ *<ADI-FreeRTOS-version>*\ **\_FREERTOSv**\ *<FreeRTOS-Kernel-Version>*\ **\_**\ *<architecture>*

**REL-ADIFRTOS-2.0.0_FREERTOSv10.4.3_SHARC**

--------------

Swapping Tags
-------------

Since the **Source** directory contains a cloned repository, the user can choose whether or not they want to switch branches. This can have unforseen repercussions and should only be done if you are certain you want to. This can be done in the usual way of using the GIT command line.

It is important that the user **ONLY** checks out **TAGS**, as these will be the supported versions. The tags will follow the naming convention stated in the section above. Using the GIT command line, you can get the list off available **TAGS** and checkout whichever you require.

--------------

Restoring Source
----------------

If for some reason the **Source** directory is missing in the project structure, the add-in will automatically attempt to re-clone the sources into this directory. This will only be done when CCES is restarted, or the project is re-opened.

It is important to note that the commit-id of the repo source is stored in the system.svc, meaning that the correct version of source will be cloned, assuming that the add-in is still installed in the project. If you have manually changed the tag being used, this will be ignored and replaced with the original version installed.
