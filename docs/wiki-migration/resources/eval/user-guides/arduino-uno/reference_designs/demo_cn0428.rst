Electrochemical Water Quality Measurement Demo
==============================================

General Description/Overview
----------------------------

The **CN0428_example** is a demo using the **EVAL-CN0428-EBZ**, the **EVAL-M355-ARDZ-INT** and the **Arduino Uno** board as a system to detect several important parameters that affect water quality, including chemical indicators, biological and bacteriological indicators and even some low level contaminants like heavy metals.

The :adi:`CN0428` circuit shown is a modular sensing platform that allows the user to design a flexible electrochemical water quality measurement solution. Its high level of integration enables an electrochemical measurement platform applicable to a variety of water quality probes including pH, oxidation reduction potential (ORP), and conductivity cells.

This example uses three types of boards:


|image1|

-  The **EVAL-CN0428-EBZ** Water Sensor Board

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0428/shield_board.jpg
   :align: center

-  The **EVAL-M355-ARDZ-INT** Arduino Shield Board
-  The **Arduino Uno** Board

Using the specified setup the system is capable of measuring pH, Conductivity, Temperature and ORP of a solution. It can be configured for customized measurements such as Dissolved Oxygen (DO) measurement, Ion Concentration measurement, i.e., Ion Selective Electrode (ISE) measurement and many other water quality factors. Up to 4 sensor boards can be connected for measurements simultaneousl and temperature can be measured on one or all sensor boards.

General Setup
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0428/functional_block_diag2.jpg

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  Arduino Uno
   -  :adi:`EVAL-M355-ARDZ-INT Arduino-compatible platform. <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-M355-ARDZ-INT.html>`
   -  :adi:`EVAL-CN0428-EBZ Water Quality Sensor Board loaded with firmware. <cn0428>` (Up to 4)
   -  BNC connectorized probe. (Up to 4)
   -  Type B to Type A USB cable
   -  PC or Laptop with a USB port
   -  (Optional) RCA connectorized temperature probe. (Up to 4)

-  Software

   -  CN0428_example sketch
   -  Arduino Interactive Development Environment(IDE)
   -  Arduino AVR Boards Built-In by Arduino package (1.6.23 or higher)

Setting up the Hardware
-----------------------

-  Before plugging all boards together, user should ensure the switch S2 is set to “I2C” on the EVAL-M355-ARDZ-INT shield board.
-  Connect up to 4 **EVAL-CN0428-EBZ** to the **EVAL-M355-ARDZ-INT** and secure them with the included hardware as shown in the pictures. This mounting should include two bolts, two standoffs and two nuts for each of the :adi:`EVAL-CN0428-EBZ <cn0428>` board. Use of the hardware mount for the :adi:`EVAL-CN0428-EBZ <cn0428>` board is strongly recommended to ensure mechanical stability and to protect the Samtec connector on the bottom of the board.

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   \ |image4|\


-  Connect the system to the Arduino connectors DIGITAL (PWM~), POWER, ANALOG IN and ICSP of the Arduino Uno board.

   -  Note, the boards should only plug together one way, preventing reverse connections.

-  Choose the desired measurement probes and connect them to the :adi:`EVAL-CN0428-EBZ <cn0428>` boards.
-  Plug in the Type B USB cable into the USB port on the Arduino Uno, and the other end into the PC or laptop.

Obtaining the Source Code
-------------------------

We recommend not opening the project directly, but rather make a local copy in your workspace and open it using Arduino/Genuino IDE.

The source code and include files of the **CN0428_example** can be found here:

.. admonition:: Download
   :class: download

   
   :git-arduino:`CN0428_example at Github <Arduino%20Uno%20R3/examples/CN0428_example>`
   


Project Structure
-----------------

The CN0411_example is a C Arduino sketch. All files are in the same folder as the .ino file and include the source and header files.

Compiling, Verifying, and Programming
-------------------------------------

-  Once the project has been imported and the software parameters have been appropriately configured, you must Compile/Verify the project within the Arduino IDE. You can do this by clicking on the Sketch menu, and then on the *Compile/Verify* option.
-  Once the project is compiled and free of errors, you can now upload the project to the Arduino Uno. Click on the Sketch menu item, and then click *Upload*.

These two steps can also be done using the quick buttons on the Arduino sketch. Check out the image below for locations of the quick buttons.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/arduino-uno/reference_designs/arduino_ide_verify_upload_buttons.png
   :align: center
   :width: 500px

Outputting Data
---------------

Data is output using the USB cable from the Arduino to the PC. The USB port acts as a serial terminal to display the data being transmitted via UART. Opening the serial terminal window from the Arduino IDE is very easy, simply click on the button shown in the picture below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/arduino-uno/reference_designs/arduino_ide_serial_terminal_button.png
   :align: center
   :width: 500px

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~

You may need to configure the serial terminal depending on the current settings of the Arduino IDE. Make sure the settings are as follows:

::

     Select COM Port
     Baud rate: 115200
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

| 

Tools Download and Help
-----------------------

The Arduino tools are easy to use, and there are many tutorials and users guides to help learn how to use the Arduino IDE.

For more information on how to use the tool basics, please check out the `Arduino tutorials page. <https://www.arduino.cc/en/Tutorial/HomePage>`_

.. admonition:: Download
   :class: download

   To download the Arduino tools, check out the `Arduino software page. <https://www.arduino.cc/en/Main/Software>`_


// End of Document //

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0428/cn0428_ebz.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0428/img_0421.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0428/img_0415.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0428/img_0418.jpg
