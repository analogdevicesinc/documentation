4 – Wire Electrochemical Dual Toxic Gas Measurement using the Arduino Uno
=========================================================================

The **CN0396_example** is a dual toxic gas detector demo project, for the Arduino Uno base board with additional EVAL-CN0396-ARDZ shield, created using the Arduino IDE.

General Description/Overview
----------------------------

The **CN0396_example** project uses the :adi:`EVAL-CN0396-ARDZ shield <CN0396>` which is a single-supply, low noise, portable gas detector, using a **4-electrode electrochemical** sensor, for simultaneous detection of two distinct gases - for this example is used the Alphasense COH-A2 sensor, which detects carbon monoxide(**CO**) and hydrogen sulfide(**H2S**).

The **EVAL-CN0396-ARDZ** board provides a potentiostatic circuit for biasing the electrochemical sensor, along with dual programmable TIA's and 16-bit Sigma-Delta ADC. The TIA's convert the small currents passing in the sensor to a voltage that can be read by the :adi:`ad7798` a 3-channel, low noise, low power 16-bit ADC that converts the analog voltage into digital data. The **16-bit** ADC outputs are received via SPI interface of the EVAL-ADICUP360 board. An :adi:`ADT7310` digital **temperature sensor** is also included to measure ambient temperature in order for correction of temperature effects.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/arduino-uno/reference_designs/img_20180123_170715.jpg
   :align: left
   :width: 500px

The **CN0396_example** application reads temperature value from ADT7310 and ADC values for each gas channel (CO and H2S), processes the values and make all necessary conversions in order to provide the gas concentrations. A **UART** interface (**9600** baud rate and **8-bits** data length) is used to send the results to terminal window. The output data will be displayed continuously considering a data refresh parameter (see *DISPLAY_REFRESH*).

Based on the **maximum sensor sensitivity** for each gas the system should be configured before using it. The application will calculate the gas concentration using sensor **gas sensitivity** and then compensate these values using measured temperature value.

.. note::

   **Maximum sensitivity** and **gas sensitivity** are dependent on sensor type. These value will need to be updated in case of using another sensor that the one presented here.


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0396/cn0396_demo_3.png
   :align: center
   :width: 800px

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  Arduino Uno Rev 3
   -  EVAL-CN0396-ARDZ
   -  Type B to Type A USB cable
   -  PC or Laptop with a USB port

-  Software

   -  CN0396_example sketch
   -  Arduino Interactive Development Environment(IDE)

Setting up the Hardware
-----------------------

-  Plug the **EVAL-CN0396-ARDZ** shield on top of the **Arduino Uno** development board by matching up the **POWER, ANALOG, DIGI0, DIGI1** connectors.

   -  Note, the boards should only plug together one way, preventing reverse connections.

-  Connect your electrochemical gas sensor to the EVAL-CN0396-ARDZ via **M1**.
-  Set the jumpers on EVAL-CN0396-ARDZ board, as shown in the picture below.\

|image1|

-   Plug in the Type B USB cable into the USB port on the Arduino Uno, and the other end into the PC or laptop.

Obtaining the Source Code
-------------------------

The source code and include files of the **CN0396_example** can be found here:

.. admonition:: Download
   :class: download

   
   :git-arduino:`CN0396_example at Github <Arduino%20Uno%20R3/examples/CN0396_example>`
   


Project Structure
-----------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/arduino-uno/reference_designs/arduino2.png
   :align: center
   :width: 700px

The Arduino Sketch is used to open the example into Arduino IDE. The project is composed of three main parts:

-  the main program (arduino sketch)
-  application layer
-  communication layer
-  driver layer (IC drivers and sensor data)

Configuring the Software Parameters
-----------------------------------

Configure the ADC gain value in *CN0396.h* file.

::

   #define ADC_GAIN      AD7798_GAIN_1

Configure the ADC samples/second value in the *CN0396.h* file.

::

   #define ADC_SPS        0x05  //50SPS

Set the refres time in the *CN0396.h* file. This is how often to display output values on terminal.(in ms)

::

   #define DISPLAY_REFRESH        500   //[msec]

Set CO range for the sensor in the *CN0396.h* file.

::

   #define MAX_CO_SENS  (100 * pow(10, -9))
   #define CO_SENS      (75 * pow(10, -9))    /* Sensitivity nA/ppm CO 50 to 100 */
   #define CO_RANGE     1000 /* Range ppm CO limit of performance warranty 1,000 */

Set H2S range for the sensor in the *CN0396.h* file.

::

   #define MAX_H2S_SENS (1000 * pow(10, -9))
   #define H2S_SENS     (800 * pow(10, -9)) /* Sensitivity nA/ppm  H2S 450 to 900 */
   #define H2S_RANGE    200  /* Range ppm H2S limit of performance warranty 200 */

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

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0396/cn0396_demo_4.png
   :width: 600px
