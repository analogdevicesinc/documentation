Scopy
=====

About
-----

Scopy is a multi-functional software toolset with strong capabilities for signal analysis. If you are interested in some :doc:`screen_shots </wiki-migration/university/tools/m2k/scopy/screen_shots>`

.. important::

   This documentation is regarding Scopy version 1 (v1.4.1, v1.5.0). For documentation regarding Scopy v2.0.0 and onwards refer to the github docs https://analogdevicesinc.github.io/scopy/.


Download
--------

.. admonition:: Download
   :class: download

   
   \**Scopy for Windows \*\*
   
   -  Download: :git-scopy:`Installer for latest release (Windows 64/32-bit) <releases/tag/v1.5.0-rc1>`
   
   \**Scopy for Linux \*\*
   
   -  Download: :git-scopy:`Scopy Flatpak installer <releases/tag/v1.5.0-rc1>`
   
   \**Scopy for OSX \*\*
   
   -  Download: :git-scopy:`OSX installer <releases/tag/v1.5.0-rc1>`
   
   \**Scopy for Android \*\*
   
   -  Download: :git-scopy:`Android installer <releases/tag/v1.5.0-rc1>`
   -  Google Play store link: `Scopy <https://play.google.com/store/apps/details?id=org.adi.scopy>`_
   
   \**Scopy all platforms latest(nightly) builds \*\*
   
   -  Download: :git-scopy:`Installer for latest (nightly) build <releases/tag/continous>`
   


.. important::

   In order to have Scopy working with :adi:`ADALM2000` please make sure that the Device Drivers are installed. A guide on this topic can be found in the section:

   
   -  :doc:`ADALM2000 for End Users </wiki-migration/university/tools/m2k/users>`.
   


Installation
------------

Scopy for Windows
~~~~~~~~~~~~~~~~~

Once you downloaded the installer, run it and follow all the required steps. After completion, system reboot is required.

Video
~~~~~

| |youtube>894HkVXf7-U|
| === Scopy for Linux === Before downloading and extracting the scopy-v1.1.1-Linux-flatpak.zip archive, you need to setup Flatpak using `this setup guide <https://flatpak.org/setup/>`_ for your Linux distribution.

For Ubuntu, you can use the following steps:

::

       **sudo add-apt-repository ppa:alexlarsson/flatpak
       sudo apt update
       sudo apt install flatpak
       flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo**

After this, get the **Scopy.flatpak** file from the downloaded archive and run:

::

       **flatpak install scopy-v1.1.1-Linux-flatpak.flatpak**

.. _video-1:

Video
~~~~~

| |youtube>9qgxmmTrcSE|
| === Scopy for OSX === Double click the downloaded .dmg to make its content available. "Scopy" will show up in the Finder sidebar and a window showing the content should open up.
| Drag the application from the .dmg window into Applications to install and wait for the process to finish.

.. _video-2:

Video
~~~~~

| |youtube>To0ACQ77tkg|
| === Scopy for Android === Tap on the downloaded .apk file to start the installation process and proceed by hitting the "Install" button. Optionally, you may be warned that this application comes from unknown sources, hit the "Install anyway" button. Now, you can find "Scopy" together with your other apps.
| In order to connect :adi:`ADALM2000` to your device, you will need an OTG adapter that will mediate the connection between your device and the USB cable, as shown in the image below.
|

.. container:: centeralign

   \ |Scopy Android setup|\


Launching
---------

| Run Scopy from the Desktop Shortcut / Start Menu / Installation Folder.
| On Linux, you can also run it using:

::

       **flatpak run org.adi.Scopy**

Using the Application
=====================

Home
----

The Home view is divided into four sections:

-  **Devices(1)**: List of devices (USB or remote) that Scopy can connect to. USB devices are detected automatically at startup. The *Add* button can be used to add remote devices to the list.
-  **Instruments Menu(2)**: List with instruments provided by the application.
-  **Information Window(3)**: Section containing the welcome, add device page and for each device a description.
-  **General Settings Menu(4)**: Save and load session and the preferences menu.

.. container:: centeralign

   \


   |Scopy Home View|

Connecting to a USB device
~~~~~~~~~~~~~~~~~~~~~~~~~~

If a compatible USB device is available it will be displayed in the **Devices** section.

To connect to that device click on the device and then click the **Connect** button in the **Information Window**.

If the connection was established, the device will have a green status line under it and you will be able to disconnect from it in the same **Information Window**.

.. container:: centeralign

   \


   |image1|

Connecting to a remote device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| To connect to a remote device click on the **Plus** icon. Enter the IP of the remote device into the **Hostname** field and click the **Connect** button. If a device can be detected at the IP you provided, the **Connect** button will change to an **Add** button and you can click on it to add the remote device to the list of detected devices.
|

.. container:: centeralign

   \


   |image2|

.. container:: centeralign

   \


   |image3|

Clicking the **Forget Device** button will remove the device from the list. Clicking the **Identify** button will make the device blink.

| 

General Settings Menu
---------------------

.. container:: centeralign

   \


   |image4|

The save/load buttons can be used to save the current session or load another session. The preferences button will open the preferences for Scopy where different options for different tools can be modified.

.. container:: centeralign

   \


   |image5|

Clicking the **Reset Scopy** button will reset the application to a default configuration.

Checking the **user notes preference** will enable a tool where the user can add different pages with html formatted text

.. container:: centeralign

   \


   |image6|

| 
| ===== User Guides ===== Scopy interacts with only one hardware device at a time. Once a device is selected to be used with the application, a list of instruments that are available for that device will be enabled. Each instrument can be opened from the left menu. The icon on the right of the instrument name specifies that the instrument is enabled and provides a shortcut that allows an instrument to be turned on or off.

The instruments menu can be minimized by clicking on the **Scopy** button near the top-left window.

.. container:: centeralign

   \


   |Scopy Minimized Menu View|

Detaching Instruments
~~~~~~~~~~~~~~~~~~~~~

Scopy provides the detaching into multiple windows feature for each instrument available, providing a better view/manipulation.

There are 2 ways to do this:

-  *Drag and Drop* - select the desired instrument drag it outside Instrument Menu section and drop it inside the application window area.

.. container:: centeralign

   \


   |Scopy Drag and Drop|

-  *Double Click* - first make sure that the **Double click to detach a tool** option is enabled in the **Preferences** menu; double-click on the desired instrument to detach it.

.. container:: centeralign

   \


   |Scopy Double Click Detach|

| 
| ==== Instruments Overview====

.. container:: centeralign

   \


   |image7|

Complete user guides on how to use each Scopy instrument:

-  :doc:`Oscilloscope </wiki-migration/university/tools/m2k/scopy/oscilloscope>`
-  :doc:`Spectrum Analyzer </wiki-migration/university/tools/m2k/scopy/spectrumanalyzer>`
-  :doc:`Network Analyzer </wiki-migration/university/tools/m2k/scopy/networkanalyzer>`
-  :doc:`Signal Generator </wiki-migration/university/tools/m2k/scopy/siggen>`
-  :doc:`Logic Analyzer </wiki-migration/university/tools/m2k/scopy/logicanalyzer>`
-  :doc:`Pattern Generator </wiki-migration/university/tools/m2k/scopy/pattgen>`
-  :doc:`Digital IO </wiki-migration/university/tools/m2k/scopy/digitalio>`
-  :doc:`Voltmeter </wiki-migration/university/tools/m2k/scopy/voltmeter>`
-  :doc:`Power Supply </wiki-migration/university/tools/m2k/scopy/power-supply>`

Scripts
^^^^^^^

User guide on how to use scripts with Scopy:

-  :doc:`Scopy - Scripting Guide </wiki-migration/university/tools/m2k/scopy/scripting-guide>`

| 
| ====== Building ====== Complete Scopy build guides on:

-  :doc:`Windows </wiki-migration/university/tools/m2k/scopy/build-windows>`
-  :doc:`Linux </wiki-migration/university/tools/m2k/scopy/build-linux>`
-  :doc:`OSX </wiki-migration/university/tools/m2k/scopy/build-osx>`

| 
| ====== Source code ====== The source code for the entire application can be found on `github <https://github.com/analogdevicesinc/scopy>`_.

.. |youtube>894HkVXf7-U| image:: https://wiki.analog.com/_media/youtube>894HkVXf7-U
.. |youtube>9qgxmmTrcSE| image:: https://wiki.analog.com/_media/youtube>9qgxmmTrcSE
.. |youtube>To0ACQ77tkg| image:: https://wiki.analog.com/_media/youtube>To0ACQ77tkg
.. |Scopy Android setup| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy-android-setup-example.png
.. |Scopy Home View| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy_home_view.png
.. |image1| image:: https://wiki.analog.com/_media/university/tools/m2k/device_connected.png
.. |image2| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy_add_device_page1.png
.. |image3| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy_add_device_page2.png
.. |image4| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy_general_settings1.png
.. |image5| image:: https://wiki.analog.com/_media/university/tools/m2k/preferences1.png
.. |image6| image:: https://wiki.analog.com/_media/university/tools/m2k/notes1.png
.. |Scopy Minimized Menu View| image:: https://wiki.analog.com/_media/university/tools/m2k/min_menu.png
.. |Scopy Drag and Drop| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy_drag_n_drop.gif
.. |Scopy Double Click Detach| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy_dc_detach.gif
.. |image7| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy_instruments_menu.png
