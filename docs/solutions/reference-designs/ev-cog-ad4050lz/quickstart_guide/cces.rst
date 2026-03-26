EV-COG-AD4050LZ with CrossCore Embedded Studio
==============================================

IDE Setup
---------

-  Install Cross Core Embedded Studio

   -  `CrossCore Embedded Studio 2.7.0 for Windows <http://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.7.0/ADI_CrossCoreEmbeddedStudio-Rel2.7.0.exe>`_
   -  `CrossCore Embedded Studio 2.7.0 for Ubuntu Linux 14.04 x86 <http://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.7.0/adi-CrossCoreEmbeddedStudio-linux-x86-2.7.0.deb>`_

-  License Installation

   -  Start CCES and navigate to Help -> Manage Licenses.
   -  Click New and enter the license key provided with the EV-COG-AD4050LZ box.
   -  Follow the on-screen instructions to register and activate the license.

Software Packs and Driver Setup
-------------------------------

-  Download the following packs for EV-COG-AD4050LZ

   -  `ARM CMSIS Pack <https://keilpack.azureedge.net/pack/ARM.CMSIS.5.1.1.pack>`_
   -  `Analog Devices ADuCM4050_DFP Pack 3.2.0 (Latest) <http://download.analog.com/tools/EZBoards/ADuCM4050/Releases/AnalogDevices.ADuCM4x50_DFP.3.2.0.pack>`_
   -  `Analog Devices EV-COG-AD4050 Off-Chip Drivers and Examples 3.1.0 (Latest) <http://download.analog.com/tools/EZBoards/COG_4050/Releases/AnalogDevices.EV-COG-AD4050LZ_BSP.3.1.0.pack>`_

-  Start CrossCore Embedded Studio.
-  Go to CMSIS Pack Manager by navigating to Windows ->Perspective ->Open Perspective ->Others -> CMSIS Pack Manager.
-  Click Import Existing Packs icon |image1|. `Refer for more details <https://wiki.analog.com/resources/ev/user-guides/ev-cog-ad4050lz/tools/cces_guide>`_.
-  Select all the packs and import. This will install the packs. Ignore the warnings seen on the console window. In order to remove these warnings, additional packs needs to be installed which are available in the last section of this page.
-  Please refer to this `link <https://os.mbed.com/handbook/Windows-serial-configuration>`_ to download and install mbed serial driver on PC.

Running an Example Project
--------------------------

-  Power the MCU Cog using a USB (micro-B) Cable. You should see a red LED and a
   yellow LED turn on by default.

.. image:: ../images/img_20171030_180904.jpg
   :align: center
   :width: 200

-  In CCES IDE, click CMSIS Pack Manager icon |image2|.
-  Select EV-COG-AD4050LZ from the Boards tab on the Left panel. (see below image)
-  Copy button_press example from the Examples tab on the Right panel.

.. image:: ../images/cmsis_pack_manager.jpg
   :align: center

-  Click C/C++ perspective icon

.. image:: ../images/c_persp.jpg

-  Under Project Explorer select button_press example, click build icon |image3|.
-  Click on Debug icon |image4| once build is complete. Below are the Debug Configuration settings.

.. image:: ../images/debug.jpg
   :align: center
   :width: 700

-  Click "ok" on Perspective Switch and Semihosting Enabled window.

|image5|

.. image:: ../images/perspective_switch.jpg
   :align: center
   :width: 500

-  Click run |image6| on the Debug perspective.
-  Now press BTN1 or BTN2 on EV-COG-AD4050LZ and inspect corresponding LED.

You are all set!

.. |image1| image:: ../images/import_existing_packs_icon.jpg
.. |image2| image:: ../images/pack_manager.jpg
.. |image3| image:: ../images/build_icon.jpg
.. |image4| image:: ../images/debug_icon.jpg
.. |image5| image:: ../images/semihosting.jpg
   :width: 500
.. |image6| image:: ../images/run_icon.jpg
