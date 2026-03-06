CN0540 and the STM Discovery Kit
================================

General Setup
-------------

The following sections on setup describe the steps for setting up the CN0540 board using the `32F746GDISCOVERY <https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/32f746gdiscovery.html>`__ micro-controller boards.

Equipment
---------

-  `32F746GDISCOVERY <https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/32f746gdiscovery.html>`__ micro-controller board
-  :adi:`EVAL-CN0540-ARDZ Shield <cn0540>`
-  PC with a USB port and Windows 7 (32-bit) or higher
-  Serial Terminal Software (Putty/TeraTerm or similar)
-  USB Standard-A to Mini-B cable
-  ICP/IEPE piezo vibration sensor

   -  Such as the :adi:`CN0532 featuring the ADXL1002 <cn0532>`

-  `32F746GDISCOVERY Discovery kit User Manual <https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/32f746gdiscovery.html#resource>`__

Hardware Setup
--------------

The following sections describe the process of setting up the hardware for the `32F746GDISCOVERY <https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/32f746gdiscovery.html>`__ micro-controller boards. It's important to note that the Arduino headers on the CN0540 are surface mounted and as such the user should take care not to bend or break the headers.

32F746 Discovery
~~~~~~~~~~~~~~~~

Shown below is the **CN0540 board** mounted on the **32F746GDISCOVERY board** via the Arduino headers. The 32F746GDISCOVERY board only requires a Standard-A to Mini-B USB cable to connect to the PC. If properly connected the large red LED LD7 should light as well as the red LED LD2.


|image1|

Software Setup
--------------

Porting the EVAL-CN0540-ARDZ MBED Example program to DISCO-F746NG Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The first step in interfacing the EVAL-CN0540-ARDZ to DISCO-F746NG board is importing the EVAL-CN0540-ARDZ into your online compiler. Refer to this link for the instructions: `Importing the EVAL-CN0540-ARDZ MBED Example program <https://wiki.analog.com/[[/resources/eval/user-guides/circuits-from-the-lab/cn0540/sdp-k1>`__
-  Then click the "Platform Selection" section of your online IDE.\

|image2|

-  After that, select the "Add Board" option.\

|image3|

-  Then, search for the DISCO-F746NG board on the available platforms.\

|image4|

-  Next is to add the DISCO-F746NG board to your online compiler.\

|image5|

-  After that, the DISCO-F746NG board will be available to your available platforms.
-  Then select it and recompile the code.\

|image6|

-  The extracted binary can be loaded to the DISCO-F746NG board by dragging and dropping the binary file to the DISCO-F746NG directory.

Note: Refer to this video for the example on how to load a program: https://youtu.be/3xbzuPLcmCk?t=233

Installing the 32F746 Discovery Board driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following are the steps then required to be completed to set up the :adi:`EVAL-CN0540-ARDZ Shield <CN0540>` using the **32F746G Discovery board**:

-  Download the `ST-LINK/V2 driver <https://os.mbed.com/teams/ST/wiki/ST-Link-Driver>`__ and run the .exe file. Follow the instructions on the window that appears to install the drives. **(Note: This requires a free account for my.st.com)**


|image7|

-  Plug the USB cables from the PC into the **32F746G Discovery board**. If installation was successful a new device named DIS_F746NG should appear under 'This PC' in Windows File Explorer.

|image8|

-  Download the AD7768_demo.bin firmware.
-  Copy and paste or drag and drop the AD7768_demo.bin file into the DIS_F746NG device/folder. This will load the firmware onto the board.
-  If the download fails, a FAIL.TXT file will appear on the DIS_F746NG device.
-  If the download is successful the .bin file will disappear from the DIS_F746NG device and there will be no FAIL.TXT file.
-  Unplug the **32F746G Discovery board** from the PC and plug it back in to hard reset the board and finalize installation.

Designing User Interface using the 32F746NG Discovery board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the major features of the 32F746G Discovery board is the on-board touchscreen, which can be used by the CN0540 board. User can design their own User Interface (UI) by by adding the `DISCOF746NG Board Support Package (BSP) <https://os.mbed.com/teams/ST/code/BSP_DISCO_F746NG/#85dbcff443aa>`__. Using the DISCOF746NG BSP custom UI can be done as shown in the images below.


|image9|

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_gui_data.png
   :align: center
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_gui_fft.png
   :align: center
   :width: 600px

*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_f746gdisco.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_stm1.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_stm2.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_stm3.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_stm4.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_stm5.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/f746gdisco_download.png
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_f746gdiscopc.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_gui_menu.png
   :width: 600px
