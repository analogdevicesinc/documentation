Visible Light Detection Demo with Bluetooth [with EVAL-CN0397-ARDZ]
===================================================================

The **ADICUP3029_CN0397** is a RGB light detection demo project for the **EVAL-ADICUP3029** base board with additional **EVAL-CN0397-ARDZ** shield, created using the Analog Devices Cross Core Embedded Studio.

General Description/Overview
----------------------------

The **ADICUP3029_CN0397** project uses the :adi:`EVAL-CN0397-ARDZ shield <en/design-center/reference-designs/hardware-reference-design/circuits-from-the-lab/cn0397>` which is a single-supply, low power, low noise, 16-bit light detector utilizing wavelength specific photodiodes. The photodiodes used in this circuit are sensitive at different wavelengths, to read light intensity levels over the visible light spectrum where the plants are photosynthetically active.

| 
| The **EVAL-CN0397-ARDZ** board uses :adi:`ad8500`, a low power, precision CMOS op amp with a low input bias current of a typical 1pA which is used in a transipedance amplifier configuration to convert the current output of the photodiodes into voltage. It also features :adi:`ad7798` a 3-channel, low noise, low power 16-bit ADC that converts the analog voltage into digital data in for the processing of data into light intensity. The circuit utilizes RGB photodiodes from Everlight with their peak sensitivities 620nm (**R**), 550nm (**G**) and 470nm (**B**).

The **ADICUP3029_CN0397** application perform ADC readings for all 3 channels, processes them and make all necessary calculations in order to provide light intensity and light concentration for each color.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0397/cn0397_adicup.png
   :align: left
   :width: 515px

The 16-bits ADC data are received using **SPI interface** of the EVAL-ADICUP360 board. The **UART interface** (**38400** baud rate and **8-bits** data length) is used to send(and to receive) data to (from) a terminal window.

**Light intensity** [Lux] is calculated using ADC output value for selected channel and a constant value for each color:

::

   Light Intensity = CODE * Light intensity Constant

**Light Concentration** [%] is calculated based on the light intensity and optimal level for each color:

::

   Light concentration = Intensity*100/Optimal Level

Beside **light intensity** and **light concentration** values, for each channel will be displayed a **colored bar** in [0%, 100%] format for light concentration representation. It will inform the user when the concentration for a specific channel will reach **100%**. Application offer the possibility to perform a system offset calibration for each **RGB channel**. All calculation are using data specific to each color of the used LEDs:

| |image1|
| ====Calibration procedure ====

The **CN0397** needs to be calibrated first before using it in order to achieve best performance. A system zero offset calibration needs to be run to cancel the offset for all of the channels. This can be done by covering and not allowing any light to reach the photodiodes.

If the calibration routine is enabled (check *USE_CALIBRATION* parameter) in a terminal window will pop up messages asking the user to cover the photodiodes one of the time so the calibration can be performed. With the photodiodes covered press **<ENTER>** button on the key board and the next message will prompt to cover the next photodiodes.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0397/calibration.jpg
   :width: 1000px

Once all the channels have been calibrated, the circuit is now ready for use. The output data will be available for each LED.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0397/data.jpg
   :width: 1000px

| 

Setting up the Hardware
-----------------------

Plug the **EVAL-CN0397-ARDZ** shield into the **EVAL-ADICUP3029** board. In order to program the base board you need to use the **USB** located at P10 on the edge of the board next to power jack.

| The **ADICUP3029_CN0397** use **UART** connection via **P0.10/P0.11** of :adi:`ADuCM3029 <en/products/processors-dsp/microcontrollers/precision-microcontrollers/aducm3029.html>` to communicate with PC terminal. Make sure S2 switch is towards **USB**. **SPI** communication via SPI0 between ADICUP3029 and EVAL-CN0397-ARDZ. Also connect a jumper on **P1** between position **1-2** on EVAL-CN0397-ARDZ.
| |image2|

Following is the UART configuration.

::

     Select COM Port
     Baud rate: 38400
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

Configuring the Software
------------------------

| In the *CN0398.h* header files you can configure parameters:
| \* **Terminal refresh** - *DISPLAY_REFRESH* parameter - how often to refresh the output data - input time value in [msec].

-  **System offset calibration** - *USE_CALIBRATION* parameter - enable/disable system offset calibration on all 3 channels - *YES* -> enable calibration; *NO* -> disable calibration.


|image3|

-  **Enable BLE** - Uncomment ENABLE_BLE macro in main.h file enable send data over BLE to Android App.

Outputting Data
---------------

| Once the hardware and software is configured, user needs to follow on screen instructions to run Visible Light Detection\\Measurement demo.
| |image4|

| |image5|
| ===== Obtaining the Source Code ===== We recommend not opening the project directly, but rather import it into CrossCore Embedded Studios and make a local copy in your workspace.

The source code and include files of the **ADICUP3029_CN0397** can be found below:

.. admonition:: Download
   :class: download

   
   <fc #ff0000>\ **ADD GITHUB LINK HERE!**\ </fc>


How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to import existing projects into your workspace </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to configure the debug session </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>` section.

-  Make sure the target board is connected to workstation (via **USB** at P10) and using the tool bar, navigate to the small Debug icon\ |image6| and select the debugging session you created. The application will programmed and the program execution will stop at the beginning of the main() function.
-  Use step-by-step execution or directly run the program.

After completion of the steps above the program will be loaded onto the system FLASH and it will run by default every time the board is powered up.

| |image7|
| ==== Project Structure ==== The **ADICUP3029_CN0397** is a C project that uses ADuCM3029 C/C++ Project structure.

This project contains: system initialization part - disabling watchdog, setting system clock, enabling clock for peripherals; port configuration for ADC, SPI read/write; configuring and reading from AD7798, UART read/write functions; calibration and calculation of light information.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0397/structure.png
   :align: left

| 
| Source and header files related to **ADICUP3029_CN0397** software application can be found in **src** and **inc** folders respectively. The *Communication.c/h* files contain **SPI** and **UART** specific APIs, meanwhile the *CN0397.c/h* files contain the calculation part, the *AD7798.c/h* files contain ADC channels handling.
| The **system** folder contains system related files.

-  **pinmux** – contains GPIO pinmuxing for UART and SPI.

The **RTE** folder contains ADuCM3029 Device Family Pack and Board Support Package files related to ADICUP3029_CN0397 project.

| 
| // End of Document //

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0397/table.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/hardware/adicup3029_uart_switch_usb.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0397/code_calibration.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0397/visible_light_terminal_output.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0397/app_1.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-aducm360-ardz/quickstart/bug.png
   :width: 30px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0397/debug.png
