Evaluating the ADRF6755 I/Q Modulator
=====================================

Accessing ACE Software:
-----------------------

To begin you will want to Install the ACE Evaluation software from the following link:

`Control \| Evaluation (ACE) Software \| Design Center \| Analog Devices <https://wiki.analog.com/analysis>`_

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/acedownloader.png
   :align: center
   :width: 600px

Once the ACE software has been downloaded it can be launched from your devices start menu for from a local shortcut icon. An in depth guide to using the ACE Software can be found here:

`ace\_-\_getting_started\_[analog_devices_wiki <https://wiki.analog.com/ace_-_getting_started_[analog_devices_wiki>`_]

Downloading the ADRF6755 Plugin from ACE:
-----------------------------------------

To download the ACE plugin for the ADRF6755 evaluation board, first open up the ACE software on your computer as seen below:

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/adrf6755_ace_mainmenu.png
   :align: center

Upon opening ACE, navigate to the "Available Packages" section in the "Plug-in Manager" tab as seen below:

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/adrf6755_ace_pluginmanager_2.png
   :align: center

Once you have navigated to this section of the ACE software, inspect the contents in the center of the screen until you locate the item labeled "Board.ADRF6755". Once located, select the item and select the install option at the bottom of the screen.

If you are unable to locate this item in the 'Available Packages" section, proceed to the "Installed Packages" section in the 'Plug-in Manager" tab and check to make sure that the plugin is not already installed.

Connecting to the ADRF6755 using ACE:
-------------------------------------

Once the ACE plugin for the ADRF6755 evaluation board is installed the next step is to properly configure the test setup for the board.

Basic setup of the ADRF6755 requires an SDP-S SPI communication board with its associated mini USB cable in addition to a 5V and 3.3V supply. The 5V supply is attached to J14 Labeled "DUT +5V" and the 3.3V supply is attached to J15 labeled "OSC\_+V".

{{ :resources:eval:sdp:2213537-40_1\_.jpg?600 \|\


|image1|

Once the hardware setup has been completed navigate to the ACE start menu as seen below and look for the board to connect to through ACE in the "Attached Hardware" section. If the option to connect doesn't show up immediately wait and try pressing the refresh button.

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/adrf6755_ace_mainmenu.png
   :align: center

Once the plugin opens it should look something like the image below:

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/adrf6755_ace_pluginview.png
   :align: center

Performing Actions With the ADRF6755 ACE GUI
--------------------------------------------

Initialize LO Frequency
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/lofrequency.png
   :align: center
   :width: 600px

This section can be used to initialize the different frequency components of the board going to the PFD.

Power Up/Down
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/powerupdown.png
   :align: center
   :width: 600px

This section controls what will be powered up or down on startup of the part. The charge pump current can also be configured here

Output Settings
~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/outputsettings.png
   :align: center
   :width: 600px

Here you can control both the MUXOUT and LOMON outputs. LOMON can be used to view the LO Signal while the part is in operation

VCO and Autocalibration Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/vcoautocal.png
   :align: center
   :width: 600px

This section allows you to control the auto-calibration time as well as disable auto-calibration altogether

Lock Detector
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/ldet.png
   :align: center
   :width: 600px

This section is used to enable/disable the lock detector as well as determine its pulse count and precision

Basic Test Case
---------------

1. Begin by enabling the modulator power up setting

2. Attach a +5.0V supply to the DUT pin with a current limit of 400mA

3. Attach a Spectrum Analyzer to the RFOut pin of the ADRF6755

4. Hit the apply button at the bottom of the ACE

5. Set the center frequency of the Spectrum Analyzer to 1875MHz and the span to 80MHz

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/adrf6755testcase.jpg
   :width: 400px

6. Measure the output frequency and output power of the main RF output on the spectrum analyzer. The highest power tone at 1850MHz should read be greater than -4dBm

7. The power of the carrier feedthrough at 1875MHz should be at least 45dB below the 1850MHz tone (-45dBc)

8. The power of the suppressed sideband at 1900MHz should be at least 30dB below the 1850MHz tone (-30dBc)

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/sdp/2213537-40.jpg
   :width: 600px
