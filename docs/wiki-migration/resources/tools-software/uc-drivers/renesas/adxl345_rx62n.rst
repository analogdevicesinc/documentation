Integration Example for Renesas RX62N Processor
===============================================

Overview
========

The Renesas Demonstration Kit (RDK) for RX62N is an evaluation and demonstration tool for Renesas RX62N microcontrollers. The goal is to provide the user with a powerful debug and demonstration platform targeted at common applications. The board also provides a useful platform for evaluating the Renesas suite of development tools for coding and debugging, using the High-performance Embedded Workshop (HEW) IDE as well as programming the device using the on-board SEGGER J-Link JTAG debugger.

.. image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/yrdkrx62n.jpg
   :align: center
   :width: 400px

More Information
----------------

-  :adi:`ADXL345 Product Info <ADXL345>` - pricing, samples, datasheet
-  `Renesas Demo Kit for RX62N <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/yrdkrx62n-yrdkrx62n-demonstration-kit-rx62n>`__ - pricing, documentation

Project Description
===================

In this project it was used the generic driver for the ADXL345 part; the functions from the Communication Driver were implemented to run on a RX62N microcontroller.

It was also created an example of using the functions implemented in the ADXL345 driver.

In this example, the output data of each axis is read and displayed on the Renesas Demonstration Kit for RX62N board’s LCD. Were also activated “Single Tap”, “Double Tap” and “Free-Fall” interrupts. When one of them occurs, on the LCD screen appears a corresponding message.


|image1|

.. container:: centeralign

   Main Screen


Getting Started
===============

The first objective is to ensure that you have all of the items needed and to install the software tools so that you are ready to create and run the evaluation project.

Hardware Items
--------------

Below is presented the list of required hardware items:

-  Renesas Demonstration Kit (RDK) for RX62N board.
-  A compatible Windows PC.

Software Tools
--------------

Below is presented the list of required software tools:

-  High-performance Embedded Workshop V.4.09.00.
-  Renesas Peripheral Driver Library for RX62N processor.

The High-performance Embedded Workshop and the Renesas Peripheral Driver Library are available on the RX62N RDK DVD or on the Renesas web page.

Downloads
---------

-  `Source code of integration example for Renesas RX62N Processor of the ADXL345 Driver <https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/adxl345_rx62n.zip>`__

RX62N Software Design
=====================

This section presents the steps for developing a software application that will run on the RX62N RDK board for controlling and monitoring the operation of the ADI part.

Run “High-performance Embedded Workshop” integrated development environment.


|image2|

.. container:: centeralign

   Choose “Create a new project workspace” option and press “OK”.


   |image3|

.. container:: centeralign

   From “Project Types” option select “Application”, name the Workspace and the Project “ADIEvalBoard”, select the “RX” CPU family and “Renesas RX Standard” tool chain. Press “OK”.


   |image4|

.. container:: centeralign

   In the first windows, select “RX600” CPU series, “RX62N” CPU Type and press “Next”.


   |image5|

.. container:: centeralign

   In the first “Option Setting” window keep default settings and press “Next”.


   |image6|

.. container:: centeralign

   In the second “Option Setting” window keep default settings and press “Next”.


   |image7|

.. container:: centeralign

   In the “Setting the Content of Files to be generated” window keep default settings and press “Next”.


   |image8|

.. container:: centeralign

   In the “Setting the Standard Library” press “Disable all” and then “Next”.


   |image9|

.. container:: centeralign

   In the “Setting the Stack Area” window keep default settings and press “Next”.


   |image10|

.. container:: centeralign

   In the “Setting the Vector” window keep default settings and press “Next”.


   |image11|

.. container:: centeralign

   In the “Setting the Target System for Debugging” window choose “RX600 Segger J-Link” target and press “Next”.


   |image12|

.. container:: centeralign

   In the “Setting the Debugger Options” window keep default settings and press “Next”.


   |image13|

.. container:: centeralign

   In the “Changing the Files Name to be created” window keep default settings and press “Finish”.


   |image14|

.. container:: centeralign

   On the “Project Summary” window appeared press “OK”.


   |image15|

.. container:: centeralign

   The workspace is created.


Now we have to integrate into our project the RPDL (Renesas Peripheral Driver Library).

Unzip the RPDL files (double-click on the file “RPDL_RX62N.exe”). The default location is “C:\\Renesas\\RPDL_RX62N”.


|image16|

.. container:: centeralign

   Navigate to where the RPDL files were unpacked and double-click on the “Copy_RPDL_RX62N.bat” to start the copy process.


   |image17|

.. container:: centeralign

   Type “4” to choose the LQFP package and press “Enter”.


   |image18|

.. container:: centeralign

   Type the full path where the project was created and press “Enter”. The default location is “C:\\WorkSpace\\ADIEvalBoard\\ADIEvalBoard”.


   |image19|

.. container:: centeralign

   After the files were copied, press any key to close the window.


Now, we have to include the new directory into our project.

Use the key sequence Alt, B, R to open the “RX Standard Toolchain” window.

Select the C/C++ tab, select “Show entries for: Include file directories” and press “Add”.


|image20|

.. container:: centeralign

   Select “Relative to: Project directory”, type “RPDL” as sub-directory and press “OK” two times.


Now, we have to include the new source files into our project.

Use the key sequence Alt, P, A to open the “Add files to project ‘ADIEvalBoard’” window.


|image21|

.. container:: centeralign

   Double click on the RPDL folder.

   
   From the “Files of type” drop-down list, select “C source file (\*.C)”.
   
   Select all of the files and press “Add”.


To avoid conflicts with standard project files, we have to remove the files “intprg.c” and “vecttbl.c” which are included in the project.

Use the key sequence Alt, P, R to open the “Remove Project Files” window.


|image22|

.. container:: centeralign

   Select the files, click on Remove and press “OK”.


Now, we have to add the library file path into our project.

Use the key sequence Alt, B, R to open the “RX Standard Toolchain” window.

Select the Link/Library tab, select “Show entries for: Library files” and press “Add”.


|image23|

.. container:: centeralign

   Select “Relative to: Project directory”, type “RPDL\\RX62N_library” as file path and press “OK”.


Because we removed the “intprg.c” file, we have to remove “PIntPrg” specified in option “start”.



|image24|

.. container:: centeralign

   Change “Category” to “Section”.


   |image25|

.. container:: centeralign

   Press “Edit”, select “PIntPRG”, press “Remove” and “OK” two times.


Now, we have to add our files (extracted from the zip file located in the "Software Tools" section) into the project.



|image26|

.. container:: centeralign

   We will copy all the files from the archive into the project folder.

   
   Note: We will replace the original “ADIEvalBoard.c” file.


Now, we have to include the files into our project.

Use the key sequence Alt, P, A to open the “Add files to project ‘ADIEvalBoard’” window.


|image27|

.. container:: centeralign

   Navigate into ADI folder.

   
   From the “Files of type” drop-down list, select “Project Files”.
   
   Select all the copied files except “ADIEvalBoard.c” (“ADIEvalBoard.c” is already included) and press “Add”.


Now, the project is ready to be built.

Press “F7”. The message after the Build Process is finished has to be “0 Errors, 0 Warnings”.

To run the program on the board, you have to download the firmware into the microprocessor’s memory.


|image28|

.. container:: centeralign

   Change the Debug Session to “JLink”.


   |image29|

.. container:: centeralign

   Save the “DefaultSession”.


   |image30|

.. container:: centeralign

   In the “Device” window select “RX62N Group”, “R5F562N8” device and press “Next”.


   |image31|

.. container:: centeralign

   In the “Communication” window keep default settings and press “Finish”.


   |image32|

.. container:: centeralign

   In the “Configuration Properties” select 12 MHz input clock and press “OK”.


   |image33|

.. container:: centeralign

   From the top menu bar, select “Debug”, then “Download Modules”, finally “All Download Modules”.


   |image34|

.. container:: centeralign

   After the download is complete, click the “Reset Go” icon.


Now, the program is running on the board.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/adxl345_screen.jpg
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_01.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_02.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_03.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_04.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_05.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_06.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_07.png
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_08.png
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_09.png
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_10.png
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_11.png
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_12.png
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_13.png
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_14.png
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_15.png
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_16.png
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_17.png
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_18.png
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_19.png
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_20.png
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_21.png
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_22.png
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_23.png
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_24.png
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_25.png
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_26.png
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_27.png
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_28.png
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_29.png
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_30.png
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_31.png
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_32.png
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/renesas/rx62n/tutorial_33.png
