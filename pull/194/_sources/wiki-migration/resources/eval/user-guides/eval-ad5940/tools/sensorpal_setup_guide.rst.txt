How to setup and use SensorPal
==============================

SensorPal is an easy to use configuration tool designed to work with the the **EVAL-AD5940BIOZ, EVAL-AD5940ELCZ, EVAl-AD5941ELCZ** and **EVAL-AD5941BATZ** evaluation kits. It provides an intuitive graphical user interface to facilitate rapid measurement prototyping and results analysis through graph form.

Download Instructions
---------------------

To download the latest SensorPal installer click on the link below. **Note**, if the link do not open correctly, try using an alternative browser such as Google Chrome, Microsoft Edge, etc.

-  AD5940 :adi:`SensorPal GUI Installer <en/products/ad5940.html#product-requirement>`

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/sensorpalinstaller_analog_com.png
   :align: center
   :width: 600px

Installation Instructions
-------------------------

-  Navigate to the folder where the installer was downloaded and double click on SensorPal Installer_v2100.exe to launch the executable
-  Follow the Install Wizard instructions to complete the setup.
-  When complete click Finish

How to Use SensorPal
--------------------

-  To launch SensorPal go to the start menu-> All Programs->SensorPal
-  To get started ensure the AD5940 evaluation kit is connected to the PC. Click on the Firmware Load button in the top toolbar as per below screenshot.

|image1|

-  Select the correct board, it should be similar to DAPLINK(E:\\). Then click Update Firmware

|image2|

-  Once the firmware is loaded plug out the evaluation kit from the PC and reconnect to power cycle the hardware.
-  In the center of the screen hit the refresh symbol beside the Com port drop-down text box. Then select the com port the ADICUP3029 microcontroller is connected to from the drop down list.

|image3|

-  To select an application to run, drag it from the left hand column of techniques and drop into the Work Area. A number of configurable parameters are available. Modify them as required.
-  To begin a measurement click on the green Measure button to the right side of the GUI.
-  The measurement results will be displayed in the graph window.
-  To stop a measurement click on the Abort Measurement button.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/firmware_load.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/firmware_load_2.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/tools/comm_port.png
   :width: 600px
