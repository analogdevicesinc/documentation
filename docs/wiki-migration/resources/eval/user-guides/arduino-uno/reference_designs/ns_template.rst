Demo Title
==========

FIXME - You need to fix the header here, the page names itself after this heading.

General Description/Overview
----------------------------

FIXME - Add text, picture, images, that describe what you are doing. Focus on the application, sensor types, end goal, any important themes or theories, equations or other important tables/information. The more info here the better.

Demo Requirements
-----------------

FIXME - Add text, part numbers, hyper links and other important information and where to get it in order to recreate this demo.

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  Arduino Uno Rev 3
   -  EVAL-CN0397-ARDZ
   -  Type B to Type A USB cable
   -  PC or Laptop with a USB port

-  Software

   -  Arduino_Uno_CN0397 sketch
   -  Arduino Interactive Development Environment(IDE)

Setting up the Hardware
-----------------------

FIXME

-  Plug the **EVAL-CN0391-ARDZ** shield on top of the **Arduino Uno** development board by matching up the **POWER, ANALOG, DIGI0, DIGI1** connectors.

   -  Note, the boards should only plug together one way, preventing reverse connections.

-  Connect your thermocouple sensor to the EVAL-CN0391-ARDZ via (**P1**-**P4**).
-  Set the jumper **JP1** of **EVAL-CN0391-ARDZ** board as shown in the picture\

|image1|

-   Plug in the Type B USB cable into the USB port on the Arduino Uno, and the other end into the PC or laptop.

Obtaining the Source Code
-------------------------

The source code and include files of the FIXME **file_name_of_demo** can be found here:

.. admonition:: Download
   :class: download

   
   FIXME - Add correct link
   
   :git-arduino:`AduCM360_demo_cn0398 at Github <Arduino%20Uno%20R3>`
   


Project Structure
-----------------

FIXME - Add text, picture, images, that describe the project structure. Any software flow diagrams or decision trees can be added her to help customers understand how the applications are structures.

Configuring the Software Parameters
-----------------------------------

Before running your program, make sure that you have configured the software appropriately to your settings:

FIXME - Add text, picture, images, code blocks that describe how to configure the software. Things like changing the accelerometer range from 2g to 4g should be a trivial change for the customer. We don't have to show them everything, but think of the application, and what parameters are most likely need to be customized by the user. (like providing a an ID or password for a local gateway using WI-FI)

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
     Baud rate: 9600
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

| 

Tools Download and Help
-----------------------

The Arduino tools are easy to use, and there are many tutorials and users guides to help learn how to use the Arduino IDE.

For more information on how to use the tool basics, please check out the `Arduino tutorials page. <https://www.arduino.cc/en/Tutorial/HomePage>`__

.. admonition:: Download
   :class: download

   To download the Arduino tools, check out the `Arduino software page. <https://www.arduino.cc/en/Main/Software>`__


// End of Document //

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0391//cn0391_demo_9.png
   :width: 600px
