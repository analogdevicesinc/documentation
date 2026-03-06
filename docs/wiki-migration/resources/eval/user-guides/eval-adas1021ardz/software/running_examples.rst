Running the Examples
====================

To run the host examples on the EVAL-ADAS1021ARDZ follow the instructions below.

-  Ensure the latest version of the J-Link Software and Documentation pack for debugging is downloaded, available at: https://www.segger.com/downloads/jlink#J-LinkSoftwareAndDocumentationPack
-  Mount the EVAL-ADAS1021ARDZ board on the microprocessor development board
-  Connect the NRF-52840 Board to the PC via the USB port. Download the latest firmware available for the Nordic NRF-52840, available at: https://www.nordicsemi.com/Software-and-tools/Development-Kits/nRF52840-DK/Download#infotabs and follow the online instructions for successfully downloading the firmware to the board.
-  Download the example projects from the Analog Devices software repository.
-  Once the example projects have been successfully downloaded, open the IAR Embedded Workbench IDE. Using the “\ **File**\ ” dropdown menu (Upper left) click on the “Open Workspace” option

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software/r1.png
   :align: center
   :width: 200px

-  A file explorer window will subsequently open. Search for the location at which the example projects have been downloaded to. Once found, choose an example project such as Respiration and then navigate to the folder labelled IAR, this can be found from the following folder flow: **examples > ADAS1021_Respiration > NRF52840 > IAR**. Once in the IAR folder choose the NRF52840 IAR IDE Workspace file, then click open.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software/2.png
   :align: center
   :width: 600px

-  The IAR Embedded Workspace IDE should open as shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software/3.png
   :align: center
   :width: 600px

-  To compile the project, choose **Project>Compile**. Alternatively, click the Compile button in the toolbar.
-  To build the project, choose Project>Make, Alternatively, click the Make button in the toolbar.
-  Click the Download and Debug button or alternatively press the Ctrl+D keys on the keyboard to programme the NRF-52840 board.
-  Once the code has successfully downloaded and compiled, open your selected serial interface programme e.g Realterm serial capture program. Ensure “newline mode” box is ticked for a clearer view of the data being streamed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software/4.png
   :align: center
   :width: 400px

-  Set the baud rate = 460800 and view the outputted data in the serial terminal.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/software/5.png
   :align: center
   :width: 400px
