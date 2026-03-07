MCU Cog Quick Start Guide [using CCES]
======================================

Setting up EV-COG-AD3029LZ is a three step process.

-  IDE Setup
-  Software Packs & Drivers Setup
-  Running an Example Project

IDE Setup
---------

-  Install Cross Core Embedded Studio

   -  `CrossCore Embedded Studio 2.7.0 or higher for Windows <http://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.7.0/ADI_CrossCoreEmbeddedStudio-Rel2.7.0.exe>`_
   -  `CrossCore Embedded Studio 2.7.0 or higher for Ubuntu Linux 14.04 x86 <http://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.7.0/adi-CrossCoreEmbeddedStudio-linux-x86-2.7.0.deb>`_

-  License Installation

   -  Start CCES and navigate to Help -> Manage Licenses.
   -  Click New and enter the license key provided with the EV-COG-AD3029LZ box.
   -  Follow the on-screen instructions to register and activate the license.

Software Packs and Driver Setup
-------------------------------

-  Download the following packs for EV-COG-AD3029LZ

   -  `ARM CMSIS Pack <https://keilpack.azureedge.net/pack/ARM.CMSIS.5.1.1.pack>`_
   -  `Analog Devices ADuCM302x Device Support Pack 3.1.0 (latest) <http://download.analog.com/tools/EZBoards/CM302x/Releases/AnalogDevices.ADuCM302x_DFP.3.1.0.pack>`_
   -  `Analog Devices EV-COG-AD3029LZ Off-Chip Drivers and Examples 3.1.0 (Latest) <http://download.analog.com/tools/EZBoards/COG_AD3029/Releases/AnalogDevices.EV-COG-AD3029LZ_BSP.3.1.0.pack>`_

-  Start CrossCore Embedded Studio.
-  Go to CMSIS Pack Manager by navigating to Windows ->Perspective ->Open Perspective ->Others -> CMSIS Pack Manager.
-  Click Import Existing Packs icon |image1|.\ :doc:`Refer for more details </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz/tools/cces_guide>`.
-  Select all the packs and import. This will install the packs. Ignore the warnings seen on the console window. In order to remove these warnings, additional packs needs to be installed which are available in the last section of this page.
-  Please refer to this `link <https://os.mbed.com/handbook/Windows-serial-configuration>`_ to download and install mbed serial driver on PC.

Running an Example Project
--------------------------

-  Power the MCU Cog using a USB (micro-B) Cable. You should see a red LED and a yellow LED turn on by default.\


|image2|

-  In CCES IDE, click CMSIS Pack Manager icon |image3|.
-  Select EV-COG-AD3029LZ from the Boards tab on the Left panel. (see below image)
-  Copy button_press example from the Examples tab on the Right panel.\

|image4|

-  Click C/C++ perspective icon

|image5|

-  Under Project Explorer select button_press example, click build icon |image6|.
-  Click on Debug icon |image7| once build is complete. Below are the Debug Configuration settings.

|image8|

-  Click ok on Hardware Breakpoint Limited and Semihosting Enabled window.\ |image9|

|image10|

-  Click run |image11| on the Debug perspective.
-  Now press BTN1 or BTN2 on EV-COG-AD3029LZ and inspect corresponding LED.

You are all set!

Additional Packs
================

For Sensor based application with BLE connectivity please download and install below packages.

::

     * Download below packs
       * [[http://download.analog.com/tools/Sensor_Software/Releases/AnalogDevices.ADI-SensorSoftware.1.1.0.pack| Analog Devices Sensor Drivers and Examples]] - [[/resources/eval/user-guides/ev-cog-ad3029lz/software/sensor|Refer for more details]]
       * [[http://download.analog.com/tools/BLE_Software/Releases/AnalogDevices.ADI-BleSoftware.1.0.0.pack|Analog Devices Bluetooth Low Energy Software]] - [[/resources/eval/user-guides/ev-cog-ad3029lz/software/connectivity|Refer for more details]]
   * Start CrossCore Embedded Studio. 
   * Go to CMSIS Pack Manager by navigating to Windows ->Perspective ->Open Perspective ->Others -> CMSIS Pack Manager.
   * Install above downloaded packs by clicking Import Existing Packs icon  {{:resources:eval:user-guides:ev-cog-ad3029lz:import_existing_packs_icon.jpg?nolink|}}.
   * Refer "Running Example Project" section as mentioned above to copy existing sensor or BLE based application to workspace.

| 
| End Document
| :doc:`Back </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/import_existing_packs_icon.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/img_2668.jpg
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/pack_manager.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/pack_manager_example.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/c_persp.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/build_icon.jpg
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/debug_icon.jpg
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/debug_config.png
   :width: 700px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/semihosting.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/hw_breakpoint.jpg
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/run_icon.jpg
