EV-COG-AD4050LZ with Keil
=========================

IDE Setup
---------

-  Install Keil MDK-Arm

   -  `Keil MDK-Arm for Windows <https://www.keil.com/demo/eval/arm.htm>`__ (Fill up the form presented in this link to get to download page)

Software Packs and Driver Setup
-------------------------------

1. After installing the Keil MDK-Arm IDE open the IDE and click on Pack Manager


|image1|

2. After opening the pack manger wait for it to get the list of packs.It may take a while depending on your internet speed

3. Once the list of packs is updated,Expand the Analog Devices section, choose your device (ADuCM3029 or ADuCM4050) and in the Packs section install the corresponding DFP and BSP based on your Board type as EV-COG-AD3029LZ_BSP or EV-COG-AD4050LZ_BSP depending on the board you have as shown in the below picture.

|image2| 5. Also install WiFi or BLE or Sensor packs, if your are using them in your project.

6. Once you click install the below window will pop up, check "Agree" and then click next until the pack is installed.Follow this for all packs.


|image3|

Running the example project
---------------------------

1. Connect the EV-COG-3029LZ or EV-COG-4050LZ/WZ to the computer using micro-B usb cable.You should see a Red LED (power LED) glowing as shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/img_20171030_180904.jpg
   :align: center
   :width: 200px

2. Inside the pack manager click on examples tab and the click copy as shown in the below picture.\


|image4|

3. Once the project is copied and opened in the workspace click Project -> Options for target and then Project options dialog box opens as shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/project_options_dialog_box.png

4. Under the "Debug" section of the dialog box, change the "use" option to "CMSIS DAP" and then click on settings to the right of it.The following dialog box opens,change the options in your dialog box to the one shown below and click OK and then click OK to exit target options dialog box.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/capture14.png

5. Then click of Start/Stop Debug section in the tool bar as shown below

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/capture33.png

6. After entering the debug session you can hit on run to run the program.The IDE window during debug should look something similar to the below picture

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/capture44.png

Now you are all set!

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/capture22.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/capture3.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/capture4.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/copy_example.png
