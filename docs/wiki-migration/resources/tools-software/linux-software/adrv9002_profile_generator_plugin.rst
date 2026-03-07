ADRV9002 Profile Generator
==========================

ADRV9002 profile generator is a tab within :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>` ADRV9002 plugin which mimics the functionality of Transceiver Evaluation Software.

Download
--------

https://analogdevicesinc.github.io/libadrv9002-iio/

How to install
--------------

-  Using the link above find the version, release you need (using the latest release is recommended) and download the installer for your platform
-  Install the software
-  Open iio-oscilloscope and connect to your adrv9002 device
-  The "Profile Generator" tab should now be unlocked

Functionalities
---------------

-  **Save to file** - generates a profile or stream image with the current configuration and saves it to a file
-  **Load to device** - sets the current profile and stream image configuration to the live device

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/iio_oscilloscope/adrv9002_profile_gen-controls.png
   :align: right
   :width: 400px

Profile Controls
----------------

-  Radio Config Controls

   -  **SSI interface** (read only) - LVDS, CMOS or CMOS/LVDS
   -  **Duplex mode** - FDD or TDD
   -  **Enable ORX** - Enable observation path

-  RX Controls

   -  **Enabled** - Enable RX channel
   -  **Frequency offset correction** - Enable DAC frequency offset correction
   -  **Bandwidth** - Channel bandwidth of interest at DAC
   -  **Interface Sample Rate** - Data rate at digital interface
   -  **RX RF Input port** - RF port source (RX_A or RX_B)

-  TX Controls

   -  **Enabled** - Enable TX channel
   -  **Frequency offset correction** - Enable DAC frequency offset correction
   -  **Bandwidth** - Channel bandwidth of interest at DAC
   -  **Interface Sample Rate** - Data rate at digital interface

Presets
-------

Refresh button resets the current configuration to the default values.

-  **LTE** - some controls are limited to a set of LTE compatible profiles
-  **Live Device** - default values are read from the live device and all values can be freely changed by the user
