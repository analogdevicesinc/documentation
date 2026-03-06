AD5758 + ADP1031 Eight Channel Analog Output Module
===================================================

Software
--------

Firmware Installation
~~~~~~~~~~~~~~~~~~~~~

The demo board comes with the latest version of the firmware pre-installed. If you would like to re-install the firmware or update to the latest version, please follow these steps:-

-  Download the latest version of the Demo board firmware. This file is called "`adi5758_20180910.zip <https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/demo-ad5757-ao8z/firmware/adi5758_20180910.zip>`__"
-  Unzip this file.
-  Install the latest version of the :adi:`CrossCore Serial Flash Programmer <en/design-center/processors-and-dsp/evaluation-and-development-software/crosscore-serial-flash-programmer.html#dsp-overview>` from Analog.com. - *You can skip this step if you have the latest version already installed*.
-  Start the CrossCore Serial Flash Programmer.

::

     -Set Target to "ADuCM302x".
     * Select firmware file “adi5758_20180910.hex” in the <File to download> field. (This is the file you downloaded and unzipped in steps 1 & 2.)
     * Apply 24 V to the "**24 V SYS**" connector
     * Plug the USB cable into the demo board.
     * Hold down S2 (Boot) button while briefly pressing the S1 (Reset) button. Then release S2. (See Figure 1) //This sequence is important//. \\ <wrap>{{:resources:demo:reference-designs:demo-ad5758-ao8z:demo-ad5758-ao8z:software:image2018-5-3_10-49-20.png?600|Reset and Boot buttons}} \\ //Figure 1 - **Reset** and **Boot** buttons//</wrap>

* On the CrossCore SFP, select the correct COM port. (//Be sure to select the correct COM port here. It is usually the highest COMnn.//)
   * Press [Start] to program device. (If you get the message “Failed to open serial device”, then repeat step 5 above, taking care to follow the exact button press sequence.)
   * Programming the board takes about 10 seconds. When it is complete, you will see a message to that effect in the Status Window. (See Figure 2) \\ <wrap>

| |The CrossCore GUI|
| *Figure 2 - The CrossCore GUI* </wrap>

-  Press the reset button (S1) on the demo board or unplug it from the USB cable and reconnect.

The demo board now has the latest version of the firmware.

GUI Installation
~~~~~~~~~~~~~~~~

This section outline how to download and install the latest version of AD5758 Eight Channel Demo Board GUI software. You can skip this step if you already have the latest version installed which is version 0911.

These instructions are for installation on Windows-10 but should also work for Windows-7 with minor differences.

Step-by-step guide
^^^^^^^^^^^^^^^^^^

-  Download the latest version of the `ad5758 GUI Software <https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/gui/demo-ad5758-ao8z_installer.zip>`__ and save to a folder of your choice.
-  Unzip the file "*DEMO-AD5758-AO8Z_Installer.zip*"
-  Double click the "*DEMO-AD5758-AO8Z_Installer.exe*" file to run it.
-  Click Next in the pop-up that appears. (See Figure 3)
   <wrap>

   |Welcome to AD5758 8 Channel Setup|

   *Figure 3 - Welcome to DEMO AD5758 AO8Z 11.12 Setup* </wrap>

-  Read carefully the License Agreement and click "I Agree" if you agree to its content. <wrap>


|image1|

   *Figure 4 - The License Agreement* </wrap>

-  Click **Install** to install the software in the default location or **Browse...** to a new location first.


|image2|

   Figure 5 - Choosing the Install Location
-  Click "Finish" in the final pop-up.

--------------

Navigation
----------

`Top <https://wiki.analog.com/../ad5758_adp1031>`__ \| `Previous(Hardware Description) <https://wiki.analog.com/hardware_details>`__ \| `Next(Demonstration guide) <https://wiki.analog.com/demonstration_guide>`__

.. |The CrossCore GUI| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/demo-ad5758-ao8z/software/cross_core.png
.. |Welcome to AD5758 8 Channel Setup| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/13-11-2019_11-56-36.png
   :width: 600px
.. |image1| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/demo-ad5758-ao8z/demo-ad5758-ao8z/software/image2018-10-18_10-21-47.png
.. |image2| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/demo-ad5758-ao8z/demo-ad5758-ao8z/gui-installation-default_location.png
   :width: 600px
