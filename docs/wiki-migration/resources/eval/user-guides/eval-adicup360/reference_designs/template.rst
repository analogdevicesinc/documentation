|

.. important::

   THIS IS A TEMPLATE.

   
   THE GOAL IS TO CREATE A DOCUMENT CUSTOMERS WILL USE WHEN SETTING UP THEIR CFTL DEMO, SO THEY DON'T ASK YOU SO MANY QUESTIONS. IT'S DESIGNED TO HELP YOU GET STARTED WRITING YOUR REFERENCE DEMO USER GUIDE.
   
   ALL OF THE CONTENT IS PLACEHOLDER INFORMATION, SO YOU WILL NEED TO POPULATE RELEVANT INFORMATION TO YOUR CFTL. SOME(OR SEVERAL) OF THE SECTION HEADERS MAY NOT APPLY TO YOU, SIMPLY REMOVE THEM. ALSO I MAY NOT HAVE CAPTURED EVERYTHING RELATIVE TO YOUR BOARD, SO ADDING INFORMATION IS ACCEPTABLE.
   
   DON'T FORGET TO CREATE A MEDIA FOLDER SPECIFIC TO YOUR DEMO FOR ANY IMAGES, FILES, OR DOCUMENTS YOU WISH TO INCLUDE. THIS WILL HELP US KEEP THE WIKI ORGANIZED AND ENSURE YOUR CONTENT DOESN'T GET REMOVED.


Application Title Demo (w/ EVAL-CNxxxx-ADRZ)
============================================

The **ADuCM360_demo_cn0411** is a Total Dissolved Solids (TDS) measurements demo project, for the EVAL-ADICUP360 base board with additional EVAL-CN0411-ARDZ shield, created using the GNU ARM Eclipse Plug-ins in Eclipse environment.

General Description/Overview
----------------------------

The **ADuCM360_demo_cn0411** project uses the :adi:`EVAL-CN0411-ARDZ shield <en/design-center/reference-designs/hardware-reference-design/circuits-from-the-lab/cn0411>` which is a single supply, low power, high precision complete solution for Total Dissolved Solids measurements, including temperature compensation. The circuit is optimized for conductivity measurements used to determine the TDS values, using conductivity cells with BNC plug.

| The circuit is divided into three independent measurement front ends: TDS, conductivity and temperature. After signal conditioning, the three channels share an :adi:`ad7124-8`, 24-bit sigma-delta (Σ-Δ) ADC. The :adi:`ad7124-8`, is a low power, low noise, completely integrated analog front end for high precision measurement applications.
| |image1|

| For temperature compensation can be used an RTD PT100 sensor, 2-wire. The ADuCM360_demo_cn0411 application processes ADC outputs for all 5 channels (RTD, Vpeak+ and Vpeak-, VDAC, VR20S, VR200S), calculates conductivity and TDS values using as input RTD temperature value and the peak-to-peak voltage. Those data are sent to serial interface, using **UART** communication (**115200** baud rate and **8-bits** data length). The **24-bits** ADC data are received using **SPI** interface of the EVAL-ADICUP360 board.
| |image2|

| 
| The **temperature** value is calculated based on the **RTD resistance**:

::

                                                                  
          Rrtd = (CODE* Rref) / (2^24 -1)                         Rref - Reference resistor (4.02kΩ)        
                                                                  CODE - ADC output
                                                                  

| 
| **1. RTD resistance > 100Ω**

| |image3|
| **2. RTD resistance ≤ 100Ω**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0398/cn0398_demo_2.png

| 
| In order to compute the **total dissolved solids** parameter a premeasurement procedure is run in the first place that aims to select the proper gain resistance for the measurement.

The multiplexer is set to the highest gain resistance (20MΩ) and the DAC output to a value set by the user (initially set to 400mV). Then, the positive and negative input voltage are captured via ADC channel 1 and 2. If the following formula is met:

::

                                                   Vp = positive input voltage
          Vp + Vn > 0.3 * 2 * Vexc                 Vn = negative input voltage
                                                   Vexc = DAC output voltage

The excitation voltage used for computing **tds** is set to:

::

                                                                          
          Vexc = 0.4 * Vexc / (Vp + Vn)      
                                                                         

Otherwise, the gain resistor is dropped by 1 decade and the premeasurement process is repeated.

After the process is finished, the peak-to-peak voltage is measured again an the **peak-to-peak current** is computed:

::


                                                     Ipp = peak-to-peak current              
          Ipp = (2 * Vexc - (Vp + Vn)) / Rgain       Vexc = excitation voltage computed in the premeasurement procedure
                                                     Vp = positive input voltage
                                                     Vn = negative input voltage
                                                     Rgain = gain resistor set via multiplexer    
                                                                     

Based on the peak-to-peak current the **electrical conductance** is computed, also removing the **offset resistance** (optional) that is obtained via the software command *"refres"* found in the list of available commands :

::

                                                     
          g = Ipp / ((Vp + Vn) - (Ipp * Roff))       Roff = offset resistance    
                                                     g = electrical conductance
          

The **electrical conductivity** is computed using the conductance and the cell constant which can be set accordingly for low conductivities, normal conductivities and high conductivities via software commands. A temperature compensation is also performed taking into account the temperature measured via RTD resistance.

::


                                                             s = electrical conductivity
          s = k * g                                          s_cal = temperature compensated electrical conductivity
                                                             temp_coeff = solution temperature coefficient 
          s_cal = s / (1 + temp_coeff * (temp - t_cal))      temp = measured temperature
                                                             t_cal = reference temperature (25°C)
                                                     

The calculation of **total dissolved solids** is the product between the temperature compensated conductivity and the **tds factor** corresponding to the solution that is used.

::


          tds = k_e * s_cal                                  k_e = tds factor
                                                             tds = total dissolved solids
          

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP360
   -  EVAL-CN0411-ARDZ
   -  Conductivity cell with BNC Connector
   -  PT100/PT1000 RTD probe
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADuCM360_demo_CN0411 software
   -  CrossCore Embedded Studio (2.7.0 or higher)
   -  ADuCM36x DFP (1.0.2 or higher)
   -  CMSIS ARM Pack (4.3.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

- To program the base board, set the jumpers/switches as shown in the next figure. The important jumpers/switches are highlighted in red.\


|image4|

-  Connect the **EVAL-CN0411-ARDZ Shield** to the Arduino connectors **P2, P5, P6, P7, P8** of the **EVAL-ADICUP360** board.
-  Connect the conductivity cell to the **J1** connector of the EVAL-CN0411-ARDZ.
-  Connect the RTD sensor to the **P3** connector of the EVAL-CN0411-ARDZ.
-  Connect **PIN1** and **PIN2** on **P5** connector and **PIN1** and **PIN2** on **P6** connector to read data from the conductivity cell.
-  Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the Debug USB.(P14)

Configuring the Software
------------------------

The configuration parameters can be found in the **config.h** file.

-  **DAC default output value** - <fc #008000>DAC_OUT_DEFAULT_VAL</fc> - set default output voltage for the DAC. (*CN0411.h*).

::

      #define DAC_OUT_DEFAULT_VAL     0.4

-  \**KCl solution TDS factor \*\* - <fc #008000>TDS_KCL</fc> - set the TDS factor for the KCl solution. (*CN0411.h*).

::

      #define  TDS_KCL                0.5

-  \**NaCl solution TDS factor \*\* - <fc #008000>TDS_NACL</fc> - set the TDS factor for the NaCL solution. (*CN0411.h*).

::

      #define  TDS_NACL               0.47

-  \**KCl solution temperature coefficient \*\* - <fc #008000>TEMP_COEFF_KCL</fc> - set the temperature coefficient for the KCl solution. (*CN0411.h*).

::

      #define  TEMP_COEFF_KCL         1.88

-  \**NaCl solution temperature coefficient \*\* - <fc #008000>TEMP_COEFF_NACL</fc> - set the temperature coefficient for the NaCl solution. (*CN0411.h*).

::

      #define  TEMP_COEFF_NACL        2.14

Outputting Data
---------------

A serial terminal is an application that runs on a PC or laptop that is used to display data and interact with a connected device (including many of the Circuits from the Lab reference designs). The device's UART peripheral is most often connected to a UART to USB interface IC, which appears as a traditional COM port on the host PC/ laptop. (Traditionally, the device's UART port would have been connected to an RS-232 line driver / receiver and connected to the PC via a 9-pin or 25-pin serial port.) There are many open-source applications, and while there are many choices, typically we use one of the following:

-  `Tera Term <https://ttssh2.osdn.jp/index.html.en>`__
-  `Putty <https://www.putty.org/>`__
-  `Real Term <https://realterm.sourceforge.io/>`__

Before continuing, please make sure you download and install one of the above programs.

There are several parameters on all serial terminal programs that must be setup properly in order for the PC and the connected device to communicate. Below are the common settings that must match on both the PC side and the connected UART device.

#. **COM Port** - This is the physical connection made to your PC or Laptop, typically made through a USB cable but can be any serial communications cable. You can determine the COM port assigned to your device by visiting the device manager on your computer. Another method for identifying which COM port is associated with a USB-based device is to look at which COM ports are present before plugging in your device, then plug in your device, and look for a new COM port.
#. **Baud Rate** - This is the speed at which data is being transferred from the connected device to your PC. These parameters must be the same on both devices or data will be corrupted. The default setting for most of the reference designs in 115200.
#. **Data Bits** - The number of data bits per transfer. Typically UART transmits ASCII codes back to the serial port so by default this is almost always set to 8-Bits.
#. **Stop Bits** - The number of "stop" conditions per transmission. This usually set to 1, but can be set to 2 for redundancy.
#. **Parity** - Is a way to check for errors during the UART transmission. Unless otherwise specified, set parity to "none".
#. **Flow Control** - Is a way to ensure that data lose between fast and slow devices on the same UART bus are not lost during transmission. This is typically not implemented in a simple system, and unless otherwise specified, set to "none".

In many instances there are other options that each of the different serial terminal applications provide, such as **local line echo** or **local line editing**, and features like this can be turned on or off depending on your preferences. This setup guide will not go over all the options of each tool, but just the minor features that will make it easier to read back data from the connected devices.

**Example setup using Putty**

#. Plug in your connected device using a USB cable or other serial cable.
#. Wait for the device driver of the connected device to install on your PC or Laptop.
#. Open your device manager, and find out which COM port was assigned to your device.\

|image1|

#. Open up your serial terminal program (Putty for this example)
#. Click on the serial configuration tab or window, and input the settings to match the requirements of your connected device. The default baud rate for most of the reference designs is 115200. Make sure that you use the correct baud rate for your application.\

|image2|

#. Ensure you click on the checkboxes for **Implicit CR in every LF** and **Implicit LF in every CF**.
#. Ensure that local echo and line editing are enabled, so that you can see what you type and are able to correct mistakes. (Some devices may echo typed characters - if so, you will see each typed character twice. If this happens, turn off local echo.)\

|image3|

#. Click on the open button, and as long as your connected device and serial terminal program are setup the same, than you should see data displaying.

.. tip::

   Hint: If you see nothing in the serial terminal, try hitting the reset button on the embedded development board.


.. |image1| image:: https://wiki.analog.com/_media/wiki/device_manager.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/wiki/putty_serial_config.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/wiki/putty_terminal_options.png
   :width: 400px

   | - In order to view the data, you must flash the program to the EVAL-ADICUP360. - Once complete you will need to switch the USB cable from the DEBUG USB (P14) to the USER USB (P13). - Then follow the UART settings below with the serial terminal program.

Following is the UART configuration.

::

     Select COM Port
     Baud rate: 115200
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

|

-  The user must press the **<ENTER>** key to start the program.
-  To get to the command menu the user must type **<help>** into the serial program.
-  Semihosting must be enabled to see data at the console window.

Available commands
~~~~~~~~~~~~~~~~~~

Typing **help** or **h** after initial calibration sequence will display the list of commands and their short versions. Bellow is the short command list:

+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
| Function                   | Command | Description                                                                                   | Example |
+============================+=========+===============================================================================================+=========+
| General commands           |         |                                                                                               |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *h*     | Display available commands.                                                                   |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *stts*  | Display parameters of the application.                                                        |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
| Internal register commands |         |                                                                                               |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *r*     | Display voltage or current on the selected channel.                                           |         |
|                            |         | <*chan*> = channel to be shown                                                                |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *sur*   | Change channel update rate.                                                                   |         |
|                            |         | <rate> = new channel update rate in Hz.                                                       |         |
|                            |         | If it is bigger than output data rate divided by 80 can cause unpredictable behaviour.        |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
| HART commands              |         |                                                                                               |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *he*    | Enable HART channel.                                                                          |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *hd*    | Disable HART channel.                                                                         |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *hcc*   | Select wanted channel.                                                                        |         |
|                            |         | <*chan*> = Channel to be selected.                                                            |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *ht*    | Transmit string through HART.                                                                 |         |
|                            |         | <*string*> = string to be transmitted.                                                        |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *hg*    | Send the received buffer through UART connection.                                             |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *hcz*   | Send command zero with the specified number of FFs in the preambule.                          |         |
|                            |         | <*pbsize*> = size of the preambule (no. of 0xFFs in the beginning).                           |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *hpt*   | Send command zero with the specified number of FFs in the preambule.                          |         |
|                            |         | <*byte*> = byte to send in loop.                                                              |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
| ADC commands               |         |                                                                                               |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *arr*   | Display value of ADC register of the given address.                                           |         |
|                            |         | <*reg*> = address of the register.                                                            |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *awr*   | Change value of the ADC register of the given address.                                        |         |
|                            |         | <*reg*> = address of the register.                                                            |         |
|                            |         | <*val*> = new value of the register.                                                          |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *ags*   | Get a specific number of samples from the given channel.                                      |         |
|                            |         | <*ch*> = selected chanel.                                                                     |         |
|                            |         | <*nr*> = number of channels; cannot exceed 2048.                                              |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *aso*   | Set sample rate.                                                                              |         |
|                            |         | <*sps*> = selected sample rate option.                                                        |         |
|                            |         | If it is smaller than channel update rate multiplied by 80 can cause unpredictable behaviour. |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *asf*   | Set filter option.                                                                            |         |
|                            |         | <*filter*> = selected filter option.                                                          |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *aep*   | Enable post filter.                                                                           |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *adp*   | Select postfilter.                                                                            |         |
|                            |         | <*opt*> = selected postfilter option.                                                         |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *asp*   | Reset controller, parameters and faults                                                       |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *aowe*  | Enable open wire detection.                                                                   |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *aowd*  | Disable open wire detection.                                                                  |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
| EEPROM commands            |         |                                                                                               |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+
|                            | *de*    | Discover EEPROM I2C addresses if there are any.                                               |         |
+----------------------------+---------+-----------------------------------------------------------------------------------------------+---------+

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/eval_cn0414_console.png
   :alt: Terminal example
   :align: center

Obtaining the Source Code
-------------------------

We recommend not opening the project directly, but rather import it into CrossCore Embedded Studios and make a local copy in your workspace.

The source code and include files of the **ADuCM360_demo_cn0411** can be found here:

|

.. admonition:: Download
   :class: download

   | CrossCore Embedded Studio Application Source Code:
   | :git-EVAL-ADICUP360:`AduCM360_demo_cn0411 at Github <projects/ADuCM360_demo_cn0411>`
   
   `AduCM360_demo_cn0411.BIN </>`__
   


.. note::

   For more information on importing, debugging, or other tools related questions, please see the :doc:`tools user guide. </wiki-migration/resources/eval/user-guides/eval-adicup360/tools/cces_user_guide>`


How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to import existing projects into your workspace </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to configure the debug session </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>` section.

Project Structure
~~~~~~~~~~~~~~~~~

The program is composed of two main parts:

-  Board setup with initial values.
-  Main process.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0414_main_flowchart.png
   :alt: Main flow chart
   :align: center

Board setup initializes **UART**, **SPI** and **I2C** communication and verifies if there is an active **EVAL-CN0414-ARDZ** board connected by reading the AD4111 ID register. Here is also initialized the update timer for the internal channel registers.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0414_board_setup_flow.png
   :alt: Board setup flow chart
   :align: center

The main process routine implements the **CLI** and calls the commands input by the user. This routine also checks the flags asserted in the asynchronous events (the update channel register flag, the HART received flag and the floating channel flags) and calls the appropriate handler methods. There is also a flag asserted by the channel register update rate and the **ADC** output data rate. If the update rate would be too close to the output data rate, the actual update rate might slow down to be possible for the program to maintain all functionality. The update rate may never be bigger or equal to the **ADC** output data rate divided by 8 (for 8 channels).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0414_process_flow.png
   :alt: Process flow chart
   :align: center

The flow chart below represents the way the channel registers are updated. Only one channel is active at any one time (the channel that must be read).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0414_update_channel_flow.png
   :alt: Update channel flow chart
   :align: center

// End of Document //

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0411_demo_4.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0411_demo_1.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0398/cn0398_demo_1.png
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0398/adicup360_hardware.jpg
   :width: 650px
