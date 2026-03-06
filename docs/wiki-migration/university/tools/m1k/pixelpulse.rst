.. admonition:: Download
   :class: download

   Download Windows and OS X binaries here:

   
   -  :git-Pixelpulse2:`Latest release <releases/latest>`
   


Pixelpulse
==========

Pixelpulse is a open source application, which provides a user interface for visualizing and manipulating signals while exploring systems attached to affordable analog interface devices, such as Analog Devices' :adi:`ADALM1000` or the Nonolith Labs' `CEE <http://www.nonolithlabs.com/cee/>`__.

Fully cross-platform (Windows, Linux, OS X) using the `Qt5 <http://qt-project.org/>`__ graphics toolkit and OpenGL accelerated density-gradiated rendering, it provides a powerful and accessible tool for initial interactive explorations.

Intuitive click-and-drag interfaces make exploring system behaviors across a wide range of signal amplitudes, frequencies, or phases a trivial exercise. Just click once to source a constant voltage or current and see what happens. Choose a function (sawtooth, triangle, sinusoidal, square) - adjust parameters, and make waves.

Zoom in and out with your scroll wheel or multitouch gestures (on supported platforms and hardware). Hold "Shift" to for Y-axis zooming.

Click and drag the X axis to pan in time.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/pixelpulse.png
   :width: 400px

Identify Devices
----------------

If multiple ADALM1000 are connected to Pixelpulse2, you can identify each device from the GUI by clicking each of the ADALM1000 labels from the left of the screen. The corresponding device will start blinking.

Acquisition Settings
--------------------

| There are use cases where a specific circuit may provide a delayed response to a given excitation signal.
| In **Repeated Sweep** mode Pixelpulse2 feeds such a signal periodically and since some circuits may provide a delayed response, it is sometimes desired to skip a few of the received samples (or maybe more) from the beginning, up to the time position that is desired.
| |Acquisition Settings Panel|

This can be done from the **Acquisition Settings** menu that will open up a settings dialog where the desired delay can be set.

-  **Delay** spinbox: Set the amount of time the acquisition should be delayed with. The smallest step size is 10 microseconds. A 1 ms step size is possible using the PageUp / PageDown buttons.
-  **Show delay** checkbox: If checked will make a status bar visible at the bottom of the main window that displays the delay that is currently set.

Note that during the time the acquisition is being delayed with the excitation signal continues to be transmitted. E.g. if Sample Time = 100 ms and Delay = 25 ms the excitation signal will run for 125 ms and the captured data that will be displayed will contain information from T0=25 ms until T1=125 ms.

Display Settings
----------------

.. image:: https://wiki.analog.com/_media/university/tools/m1k/pp2_display_settings.png
   :alt: Display settings panel
   :align: right
   :width: 350px

Customize the coloring scheme of the plots within the application.

The dialog can be accessed from Settings -> Display settings.

-  **Brightness** slider: Adjust the brightness of the plot by increasing the brightness of the background and the grid.
-  **Contrast** slider: Adjust the contrast of the plot by decreasing the brightness of the background and increasing the brightness of the grid.
-  **Dot brightness** slider: Adjust the brightness of the dot.
-  **Dot size** slider: Change the size of the dot.
-  **Time Plots** checkbox: If checked, settings are applied to the time plots.
-  **XY Plots** checkbox: If checked, settings are applied to the XY plots.

Scroll, use the left/right arrow or click and drag the user friendly sliders to change the settings.

Use any other feature that Pixelpulse provides without closing the display settings dialog.

Save or restore your preferred settings with all the other saved data using Save Session or Restore Session.

Data logging
------------

Pixelpulse2 contains a data logging mechanism. This can be very useful for capturing data for a longer period of time.

To enable the data logging mechanism, you can check the Data logging button from Pixelpulse's menu. |image1|\ In order to do this, you must select a Sample time of 1 or 10 seconds. After each 1, respectively 10, seconds, the generated data from the last interval of time will be stored into a file. The stored data contains the minimum, maximum and average current and voltage value for both channels A and B, for each connected device and the timestamp relative to the logging process start time.

The log file's name has the following pattern: PP_Log\_<timestamp>.csv. The timestamp is composed from the date and time at which the file was created. In the following picture you can see a sample of a log file.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/log_sample.png
   :align: center

The log files are stored in a corresponding folder, depending on the OS:

-  on Windows they are stored in **C:/Users/<User>/AppData/Roaming/ADI/Pixelpulse2/logging;**
-  on Linux they are stored in **~/.local/share/ADI/Pixelpulse2/logging;**
-  on MacOS they are stored in **~/Library/Application Support/ADI/Pixelpulse2/logging.**

Download
========

The latest release of Pixelpulse is available for download on :git-Pixelpulse2:`Github <releases/latest>`.

A release contains multiple binaries that allow Pixelpulse2 to be deployed on systems that run Windows and OS X. Linux users will currently have to build their own version from source.

The typical list of files that a release contains:

-  **Pixelpulse2-vX.YZ.dmg.zip**: Apple disk image for OS X, archived as a zip archive.
-  **pixelpulse2-vX.YZ_win_setup.exe**: Windows installer.
-  **Source code (zip)**: The source code at the time the release was made, archived as a zip archive.
-  **Source code (tar.gz)**: The source code at the time the release was made, archived as a tarball.

| where:
| X = major version of a release
| YZ = minor version of a release

Building from source
====================

:doc:`Instructions are available </wiki-migration/university/tools/m1k/pixelpulse/build>` for those interested in building Pixelpulse from source.

.. tip::

   When running Pixelpulse under Linux please make sure to run it as root.


.. |Acquisition Settings Panel| image:: https://wiki.analog.com/_media/university/tools/m1k/pp2_acquisition_settings.png
   :width: 350px
.. |image1| image:: https://wiki.analog.com/_media/university/tools/m1k/data_logging.png
   :width: 200px
