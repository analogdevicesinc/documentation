How to setup and use IAR Embedded Workbench
===========================================

IAR Workbench is the IDE of choice for developing firmware for the AD5940. IAR provides an evaluation licence that is free but limits the code size to 32 kB. Currently, none of the evaluation examples in the AD5940 development pack exceed this.

How to Download IAR
-------------------

To download IAR Workbench click on the following `link <https://artifactory.analog.com/ui/native/iar-binaries-generic/full_network_version/9.50.2>`_

This will begin downloading the latest IAR installer. The file is large so may take some time depending on Internet Download speed.

How to Install IAR
------------------

Once the download has complete double click on the .exe file to begin the installation procedure. Then click on Install IAR Embedded Workbench® for ARM.\


|image1|

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/setup2.png
   :align: center
   :width: 400px

Click Next. The installation procedure may take some time as it is a large program.

How to Register for IAR Evaluation License
------------------------------------------

To register for the IAR free evaluation license follow these instructions:

-  Open IAR Workbench
-  Navigate to Help->License Manager
-  When the License Manager opens go to License->Get Evaluation License

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/setup3.png
   :align: center
   :width: 400px

-  The user must register with IAR to get the evaluation licence. Follow online registration instructions. Select size limited licence as opposed to time limited licence. An email is sent with a link. Click this link to reveal the license number. A similar window to the one below should be displayed with the license number.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/setup4.png
   :align: center
   :width: 400px

-  Then go back to IAR license manager and go to License->Activate License

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/setup6.png
   :align: center
   :width: 400px

-  Enter the new license number and click ok.

IAR Workbench is now ready to use with a 32KB code size limit.

How to edit and run example code in IAR
---------------------------------------

To edit and run example code in IAR Workbench follow these steps:

-  Download the AD5940 SDK from the the GitHub repository:

.. admonition:: Download
   :class: download

   
   `AD5940 SDK Source Code <https://github.com/analogdevicesinc/ad5940-examples>`_
   


-  Navigate to the **examples** folder
-  Double click on ADICUP3029.eww file. This opens all the example projects in the IAR Workspace
-  On first time opening the project, the IAR CMSIS pack manager will open with a screen like this

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/pack_manager.png
   :align: center
   :width: 600px

-  Click on Packs and expand the Device Specific option.
-  Install the AnalogDevices.ADuCM302x_DFP as highlighted below

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/pack_installation.png
   :align: center
   :width: 600px

-  Once installed exit the Pack Manager window and display the main IAR Workbench program.
-  All the example projects are shown in the Workspace view

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/project_display.png
   :align: center
   :width: 600px

-  To select a project to run, right click on it and select "Set as Active"

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/select_project.png
   :align: center
   :width: 600px

-  Expand the project to see the structure. It is divided into 4 sub sections:

   -  **AD5940Lib** - This conatins the AD5940.c source file which has all the AD5940 library functions. This file is common to all examples. The ADICUP3029Port.c file is located here also and contains port functions for the ADuCM3029 microcontroller.
   -  **Application** - This sub section contains the application code and main.c file.
   -  **CMSIS-Pack** - This pack contains the necessary files for the ADuCM3029 to function including the startup.c and system.c files
   -  **Output** - This contains the c.out file. This file should not be changed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/iar.png
   :align: center
   :width: 600px

-  Double click on AD5940_ADCPolling.c to open the file in the editor.
-  Modify code as required.
-  To compile and build the project go to Project->Rebuild All. IT may take a couple fo seconds to fully compile all the source code.
-  To download the code to the evaluation boards first ensure the boards are connected to the PC or laptop. Then click on the green "Play" button on the top toolbar. Note, if the "play" button is greyed out cloise IAR Workbench and re-open it.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/iar_debug.png
   :align: center
   :width: 600px

-  To set breakpoints click to the left of the line of code. A red dot will appear as in above screenshot.
-  The code will be loaded onto the ADuCM3029 microcontroller. To begin executing press the blue "Go" button.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/iar_debugger.png
   :align: center
   :width: 600px

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/setup1.png
   :width: 400px
