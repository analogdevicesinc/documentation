Toxic Gas Detector using the Arduino Uno
========================================

| The **CN0357_example** is a toxic gas(CO) detector demo project for the Arduino Uno base board with additional :adi:`EVAL-CN0357-ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-CN0357-ARDZ.html>` shield, created using the Arduino IDE.

General Description/Overview
----------------------------

| This user guide gives a detailed explanation about **CN0357_example** toxic gas (CO) detection project for Arduino base board and :adi:`EVAL-CN0357-ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-CN0357-ARDZ.html>` gas sensor shield. The gas sensor shield consists of portable gas detector circuit.
| |image1|
| The :adi:`EVAL-CN0357-ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-CN0357-ARDZ.html>` shield circuit provides a potentiostatic circuit for biasing the electrochemical sensor and 16-bit Sigma-Delta ADC. The small currents passing in the sensor is being converted to a voltage that can be read by the ADC. The 16-bit ADC value is received via SPI interface of the EVAL-ADICUP3029 board, where the gas concentration is computed.
| The **CN0357_example** application configures the necessary components, processes ADC output value and make all necessary conversions in order to provide the gas concentration. A UART interface (9600 baud rate and 8-bits data length) is used to send the results to terminal window: CO Concentration in **Parts Per Million(PPM)** are the outputs provided in the terminal window.
| At the start of the project, the software computes the necessary parameters and configure the digital rheostat(AD5270) . The required parameters are the sensor sensitivity and feedback resistor range. These can be modified by changing the values of the constants **ui16sensorRange** and **ui16sensitivity** found in the **CN0357_example.ino** file of the project.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  Arduino Uno Rev 3
   -  EVAL-CN0357-ARDZ
   -  Type B to Type A USB cable
   -  PC or Laptop with a USB port

-  Software

   -  CN0357_example sketch
   -  Arduino Interactive Development Environment(IDE)

Setting up the Hardware
-----------------------

-  Plug the **EVAL-CN0357-ARDZ** shield on top of the **Arduino Uno** development board by matching up the **POWER, ANALOG, DIGI0, DIGI1** connectors.

   -  Note, the boards should only plug together one way, preventing reverse connections.

-  Connect your carbon monoxide(CO) sensor to the EVAL-CN0357-ARDZ via (**P1**).\


|image2|

-   Plug in the Type B USB cable into the USB port on the Arduino Uno, and the other end into the PC or laptop.

|

.. important::

   **Rev B** EVAL-CN0357-ARDZ boards **REQUIRE** an external power supply, plugged into the DC barrel jack of the Arduino Uno. If not supplied, the board **WILL NOT WORK PROPERLY.**


   | Rev C Eval-CN0357-ARDZ boards do not require this extra power supply.


Obtaining the Source Code
-------------------------

The source code and include files of the **CN0357_example** can be found here:

.. admonition:: Download
   :class: download

   
   :git-arduino:`CN0357_example at Github <Arduino%20Uno%20R3/examples/CN0357_example>`
   


Project Structure
-----------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/arduino-uno/reference_designs/drawing2.png
   :align: center
   :width: 700px

The Arduino Sketch is used to load the example into Arduino IDE. The project is composed of three main parts:

-  the main program (arduino sketch)
-  application layer (IC drivers and sensor data)

Configuring the Software Parameters
-----------------------------------

The CN0357 comes with a carbon monoxide sensor, and those default settings are programmed into the software.(No configuration required) If you decide to use a different type of sensor, you will need to change the sensor sensitivity and range within the software.

In *CN0357_example.ino* file the user can configure parameters:

-  **ui16sensorRange** -This is the range of the sensor and it is used to calculate the feedback resistor value.

::

       uint16_t ui16sensorRange = 2000;            //value is in units (PPM)

-  **ui16sensitivity** - sensitivity (nA/ppm) of the electrochemical sensor being used.

::

       uint16_t ui16sensitivity =  65;         //value is in units (nA/ppm)  

|

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

For more information on how to use the tool basics, please check out the `Arduino tutorials page. <https://www.arduino.cc/en/Tutorial/HomePage>`_

.. admonition:: Download
   :class: download

   To download the Arduino tools, check out the `Arduino software page. <https://www.arduino.cc/en/Main/Software>`_


// End of Document //

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/arduino-uno/reference_designs/img_20180118_154523.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/arduino-uno/reference_designs/img_20180118_154407.jpg
   :width: 500px
