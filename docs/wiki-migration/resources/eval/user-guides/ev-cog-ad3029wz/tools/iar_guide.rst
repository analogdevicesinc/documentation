EV-COG-AD3029WZ with IAR Embedded Workbench for ARM
===================================================

<note >There are no seperate toolchain,On-Board Peripheral Drivers & Software for EV-COG-AD3029WZ, the toolchain,On-Board Peripheral Drivers & Software for EV-COG-AD3029LZ works with EV-COG-AD3029WZ.The user needs to change only the pin muxing based on the application.For help regarding pinmapping refer to the Hardware Details section. </WRAP>

First, install mBed windows serial driver from [[https://developer.mbed.org/handbook/Windows-serial-configuration%7Chttps://developer.mbed.org/handbook/Windows-serial-configuration]]

IDE Setup
---------

-   Install IAR Embedded Workbench for ARM

   -  Please visit https://www.iar.com/ to download IAR Embedded Workbench for ARM (version 8.20.1 or above)

-   License Installation

   -  Make sure valid license is installed for the corresponding version.

Software Packs and Driver Setup
-------------------------------

-  Download the following packs for EV-COG-AD3029LZ \*\* (The packs are same for EV-COG-AD3029LZ and EV-COG-AD3029WZ) \*\*

   -  `ARM CMSIS Pack <https://keilpack.azureedge.net/pack/ARM.CMSIS.5.2.0.pack>`_

      -  `DFP - Device Family Pack for ADuCM302x <http://download.analog.com/tools/EZBoards/CM302x/Releases/AnalogDevices.ADuCM302x_DFP.3.1.0.pack>`_
      -  `BSP - Board Support Pack for EV-COG-AD3029LZ <http://download.analog.com/tools/EZBoards/COG_AD3029/Releases/AnalogDevices.EV-COG-AD3029LZ_BSP.3.1.0.pack>`_

-  Start IAR Embedded Workbench for ARM.
-  Go to Project-> CMSIS-Pack-> Pack Installer.

|image1|

-  In **'CMSIS Pack Manager'** window, click 'Install local pack file'.

|image2|

-  In 'Pack file to install' window navigate to the downloaded pack (as already done in step 1 of this section), select all the packs to install and click Open.

|image3|

Running an Example Project
--------------------------

-  Power the MCU Cog using a USB (micro-B) Cable. You should see a red LED and a yellow LED turn on by default.


|image4|

-  In IAR IDE, go to Project-> Create New Project...

|image5|

-  In **'Create New Project'** window, Select **'CMSIS Pack Example'** and click 'OK'.

|image6|

-  Expand Analog Devices, select **ADuCM3029** and click 'Next'.

|image7|

-  Select **button_press** example and click 'Finish'.\

|image8|

-  Save the project to the desired location.
-  Click on 'Debug and Download' icon |image9|\ on the menu bar. This will compile, build and download the project on EV-COG-AD3029WZ using CMSIS-DAP.
-  Click on 'Run' icon |image10| to start the debug session.
-  Now press BTN1 or BTN2 on EV-COG-AD3029WZ and inspect corresponding LED

You are all set!

:doc:`Back </wiki-migration/resources/eval/user-guides/ev-cog-ad3029wz/quickstart_1>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/iar/cmsis_pack_install_1.png
   :width: 750px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/iar/cmsis_pack_install_2.png
   :width: 700px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/tools/iar-aducm3029-cmsis-packs-snapshot2.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/img_20171030_180904.jpg
   :width: 200px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/iar/create_new_project_1.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/iar/example_run_1.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/tools/iar-aducm3029-cmsis-example-mcu-select1.png
   :width: 700px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/tools/iar-aducm3029-cmsis-example-buttonpress1.png
   :width: 700px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/iar/debug_debug_button.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/iar/run_button.png
