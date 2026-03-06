Preparing your Laptop or PC for Large Captures
==============================================

.. important::

   You may need to contact your system administrator or IT department before changing these settings


-  Ensure you have at least 100GB of free disk space and at least 16GB of RAM.
-  Navigate to "System" in Control Panel (Windows 10)

|image1|

-  Go to "Advanced System Settings"

|image2|

-  Go to Performance and Settings

|image3|

-  Go to Advanced and Select "Change"

|image4|

-  Choose the option to "Automatically manage paging file..."

|image5|

.. important::

   Continuous use of paging files with an SSD based storage device may result in excessive wear!


Limitations and What to Expect
==============================

-  Not all ACE plug-ins can support or have been updated to support large captures.
-  The size of your paging file and amount of RAM your PC or Laptop has.
-  Most Capture Controllers (e.g. ADS7-V2) take a snapshot to onboard RAM as the data rate is often too high to continuously transfer to the PC (reliably). For the SDP-H1 that's 64MB and the ADS7-V2 about 4GB.
-  The FFT analysis library is limited to (2^31)-1 element double arrays. Note that Complex Samples are passed as an interleaved double array, the limitation for Complex FFTs is 2^30 I&Q samples.
-  Depending on the size of the Capture it could take a long time.
-  As the operation is memory intensive some applications may stop responding or your system may become unstable.

Capturing Raw Data to File to Avoid Delays
==========================================

If you want to do large captures, we still recommend that you capture the raw data directly to file using the Remote Control service and a scripting/automation language of your choice. e.g. Python, Matlab or Labview. This will bypass the ACE GUI and analysis libraries and allow you to work with the data directly.

-  :doc:`ACE Remote Control </wiki-migration/resources/tools-software/ace/remotecontrol>`

ACE Plug-ins that Support Large Captures
========================================

We will add to this list as we are informed of plug-in updates, this is not authoritative, always check for plug-in and ACE updates.

-  AD9208

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/ace/screenshot_2021-07-01_152927.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/ace/screenshot_2021-07-01_153421.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/ace/screenshot_2021-07-01_153421.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/ace/screenshot_2021-07-01_154148.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/ace/screenshot_2021-07-01_154333.png
   :width: 400px
