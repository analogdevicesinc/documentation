EV-COG-AD3029LZ with IAR Embedded Workbench for ARM
===================================================

First, install mBed windows serial driver from [[https://developer.mbed.org/handbook/Windows-serial-configuration%7Chttps://developer.mbed.org/handbook/Windows-serial-configuration]]

IDE Setup
---------

-   Install IAR Embedded Workbench for ARM

   -  Please visit https://www.iar.com/ to download IAR Embedded Workbench for ARM (version 8.20.1 or above)

-   License Installation

   -  Make sure valid license is installed for the corresponding version.

Software Packs and Driver Setup
-------------------------------

-  Start IAR Embedded Workbench for ARM.
-  Go to Project-> CMSIS-Pack-> Pack Installer.

|image1|

-  In **'CMSIS Pack Manager'** window, Click Search for updates.
-  Expand Analog Devices, then expand **ADuCM302x_DFP**. Right click on the latest version (for ex. 3.2.0) and click install.

|image2|

-  After successful installation of **ADuCM302x_DFP**, repeat step 4 for **EV-COG-AD3029LZ_BSP**.
-  After successful installation of **EV-COG-AD3029LZ_BSP**, expand ARM -> CMSIS and install the latest version (for ex. 5.4.0 ) available for ARM CMSIS Pack.

Running an Example Project
--------------------------

-  Power the MCU Cog using a USB (micro-B) Cable. You should see a red LED and a yellow LED turn on by default.


|image3|

-  In IAR IDE, go to Project-> Create New Project...

|image4|

-  In **'Create New Project'** window, Select **'CMSIS Pack Example'** and click 'OK'.

|image5|

-  Expand Analog Devices, select **ADuCM3029** and click 'Next'.

|image6|

-  Select **button_press** example and click 'Finish'.\

|image7|

-  Save the project to the desired location.
-  Click on 'Debug and Download' icon |image8|\ on the menu bar. This will compile, build and download the project on EV-COG-AD3029LZ using CMSIS-DAP.
-  Click on 'Run' icon |image9| to start the debug session.
-  Now press BTN1 or BTN2 on EV-COG-AD3029LZ and inspect corresponding LED

You are all set!

:doc:`Back </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz/quickstart>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/iar/cmsis_pack_install_1.png
   :width: 750px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/tools/1.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/img_20171030_180904.jpg
   :width: 200px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/iar/create_new_project_1.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/iar/example_run_1.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/tools/iar-aducm3029-cmsis-example-mcu-select1.png
   :width: 700px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/tools/iar-aducm3029-cmsis-example-buttonpress1.png
   :width: 700px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/iar/debug_debug_button.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/iar/run_button.png
