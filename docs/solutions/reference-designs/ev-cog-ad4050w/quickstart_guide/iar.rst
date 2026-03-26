EV-COG-AD4050WZ with IAR Embedded Workbench for ARM
===================================================

.. note::

   There are no separate toolchain, On-Board Peripheral Drivers & Software for
   EV-COG-AD4050WZ; the toolchain, On-Board Peripheral Drivers & Software for
   EV-COG-AD4050LZ works with EV-COG-AD4050WZ. The user needs to change only
   the pin muxing based on the application. For help regarding pin mapping refer
   to the Hardware Details section.

IDE Setup
---------

-   Install IAR Embedded Workbench for ARM

   -  Please visit https://www.iar.com/ to download IAR Embedded Workbench for ARM (version 8.20.1 or above).

-   License Installation

   -  Make sure valid license is installed for the corresponding version.

Software Packs and Driver Setup
-------------------------------

-  Download the following packs for EV-COG-AD4050LZ

   -  `ARM CMSIS Pack <https://keilpack.azureedge.net/pack/ARM.CMSIS.5.2.0.pack>`_

      -  `Analog Devices ADuCM4x50 Device Support 3.1.0 (Latest) <http://download.analog.com/tools/EZBoards/ADuCM4050/Releases/AnalogDevices.ADuCM4x50_DFP.3.1.0.pack>`_
      -  `Analog Devices EV-COG-AD4050 Off-Chip Drivers and Examples 3.1.0 (Latest) <http://download.analog.com/tools/EZBoards/COG_4050/Releases/AnalogDevices.EV-COG-AD4050LZ_BSP.3.1.0.pack>`_

-  Start IAR Embedded Workbench for ARM.
-  Go to Project-> CMSIS-Pack-> Pack Installer.

.. image:: ../images/cmsis_pack_install_1.png
   :align: center
   :width: 750

-  In **'CMSIS Pack Manager'** window, click 'Install local pack file'.

.. image:: ../images/cmsis_pack_install_2.png
   :align: center
   :width: 700

-  In 'Pack file to install' window navigate to the downloaded pack (as already
   done in step 1 of this section), select all the packs to install and click
   Open.

.. image:: ../images/cmsis_pack_install_3.png
   :align: center
   :width: 700

Running an Example Project
--------------------------

.. important::

   The pins for LEDs and BUTTONs are different in example project as they are
   developed for LZ version of 4050.So before running the example in your WZ
   board change the pinmuxing appropriately by looking at the hardware details
   section.

-  Power the MCU Cog using a USB (micro-B) Cable. You should see a red LED and a
   yellow LED turn on by default.

.. image:: ../images/img_20171030_180904.jpg
   :align: center
   :width: 200

-  In IAR IDE, go to Project-> Create New Project...

.. image:: ../images/create_new_project_1.png
   :align: center

-  In **'Create New Project'** window, Select **'CMSIS Pack Example'** and click 'OK'.

.. image:: ../images/example_run_1.png
   :align: center

-  Expand Analog Devices, select **ADuCM4050** and click 'Next'.

.. image:: ../images/example_run_2.png
   :align: center
   :width: 700

-  Select **button_press** example and click 'Finish'.

.. image:: ../images/example_run_3.png
   :align: center
   :width: 700

-  Save the project to the desired location.
-  Click on 'Debug and Download' icon |image1| on the menu bar. This will compile, build and download the project on EV-COG-AD4050LZ using CMSIS-DAP.
-  Click on 'Run' icon |image2| to start the debug session.
-  Now press BTN1 or BTN2 on EV-COG-AD4050LZ and inspect corresponding LED

You are all set!

.. |image1| image:: ../images/debug_debug_button.png
.. |image2| image:: ../images/run_button.png
